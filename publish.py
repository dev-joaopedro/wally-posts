"""Publica no Instagram os posts e stories cujo horario ja chegou.

Le posts.json e stories.json, pula o que ja esta em published.json, e publica o
restante via Instagram Graph API. Pensado para rodar no GitHub Actions a cada 30
minutos; a janela de LOOKBACK evita que uma interrupcao longa despeje um backlog
inteiro de uma vez.
"""

import json
import os
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

import requests

REPO_RAW_BASE = "https://raw.githubusercontent.com/dev-joaopedro/wally-posts/main"
API_BASE = "https://graph.instagram.com/v21.0"
TZ = ZoneInfo("America/Sao_Paulo")

# posts.json so tem a data; este e o horario em que o post do feed sai.
POST_TIME = "12:00:00"

# Nao publica itens atrasados alem disso (evita backlog apos uma queda longa).
LOOKBACK = timedelta(hours=3)

# Teto por execucao, como rede de seguranca contra um erro de dados.
MAX_PER_RUN = 5

# Tempo maximo esperando o Instagram processar a imagem do container.
CONTAINER_TIMEOUT = 120

ROOT = Path(__file__).parent
PUBLISHED_FILE = ROOT / "published.json"


def load_json(path, default=None):
    if not path.exists():
        return default
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def scheduled_at(date_str, time_str):
    return datetime.fromisoformat(f"{date_str}T{time_str}").replace(tzinfo=TZ)


def all_items():
    """Normaliza posts e stories num formato unico."""
    for p in load_json(ROOT / "posts.json", []):
        yield {
            "id": p["id"],
            "kind": "post",
            "when": scheduled_at(p["d"], POST_TIME),
            "image_url": f"{REPO_RAW_BASE}/posts/{p['id']}.jpg",
            "caption": p.get("caption", ""),
        }

    for s in load_json(ROOT / "stories.json", []):
        yield {
            "id": s["id"],
            "kind": "story",
            "when": scheduled_at(s["d"], s["time"]),
            "image_url": f"{REPO_RAW_BASE}/stories/{s['id']}.jpg",
            "caption": None,  # Stories via API nao aceitam legenda.
        }


def collect_due(now, published_ids):
    """Retorna os itens vencidos e ainda nao publicados, do mais antigo ao mais novo."""
    due = [
        i for i in all_items()
        if i["id"] not in published_ids and now - LOOKBACK <= i["when"] <= now
    ]
    due.sort(key=lambda i: i["when"])
    return due


def collect_forced(ids):
    """Itens pedidos explicitamente, ignorando horario e published.json.

    Serve para testar, republicar algo apagado por engano ou recuperar um atraso
    que passou da janela.
    """
    por_id = {i["id"]: i for i in all_items()}
    forced, faltando = [], []
    for item_id in ids:
        if item_id in por_id:
            forced.append(por_id[item_id])
        else:
            faltando.append(item_id)
    if faltando:
        raise SystemExit(f"id(s) nao encontrado(s) nos JSONs: {', '.join(faltando)}")
    return forced


def wait_ready(creation_id, token, timeout=CONTAINER_TIMEOUT):
    """Espera o container ficar FINISHED.

    Publicar logo apos criar o container devolve o erro 9007 ("media is not ready
    for publishing"): o Instagram ainda esta baixando e processando a imagem.
    """
    deadline = time.time() + timeout
    while time.time() < deadline:
        r = requests.get(
            f"{API_BASE}/{creation_id}",
            params={"fields": "status_code", "access_token": token},
            timeout=30,
        )
        status = r.json().get("status_code")
        if status == "FINISHED":
            return
        if status in ("ERROR", "EXPIRED"):
            raise RuntimeError(f"container {creation_id} terminou como {status}")
        time.sleep(3)
    raise RuntimeError(f"container {creation_id} nao ficou pronto em {timeout}s")


def publish(item, ig_user_id, token):
    """Cria o container, espera ficar pronto e publica. Retorna o media id."""
    params = {"access_token": token, "image_url": item["image_url"]}
    if item["kind"] == "story":
        params["media_type"] = "STORIES"
    elif item["caption"]:
        params["caption"] = item["caption"]

    r = requests.post(f"{API_BASE}/{ig_user_id}/media", data=params, timeout=60)
    body = r.json()
    if "id" not in body:
        raise RuntimeError(f"falha ao criar container: {body}")
    creation_id = body["id"]

    wait_ready(creation_id, token)

    r = requests.post(
        f"{API_BASE}/{ig_user_id}/media_publish",
        data={"access_token": token, "creation_id": creation_id},
        timeout=60,
    )
    body = r.json()
    if "id" not in body:
        raise RuntimeError(f"falha ao publicar container {creation_id}: {body}")
    return body["id"]


def main():
    token = os.environ.get("IG_ACCESS_TOKEN")
    ig_user_id = os.environ.get("IG_USER_ID")
    dry_run = os.environ.get("DRY_RUN", "").lower() in ("1", "true", "yes")

    if not token or not ig_user_id:
        sys.exit("IG_ACCESS_TOKEN e IG_USER_ID sao obrigatorios")

    now = datetime.now(TZ)
    published = load_json(PUBLISHED_FILE, {}) or {}
    forced_ids = [i.strip() for i in os.environ.get("FORCE_IDS", "").split(",") if i.strip()]

    if forced_ids:
        due = collect_forced(forced_ids)
        print(f"MODO FORCADO: {len(due)} item(ns) pedidos explicitamente")
    else:
        due = collect_due(now, set(published))

    print(f"agora: {now:%Y-%m-%d %H:%M:%S %Z} | a publicar: {len(due)} | ja publicados: {len(published)}")
    if dry_run:
        print("DRY_RUN ativo, nada sera publicado")

    if not due:
        return

    if len(due) > MAX_PER_RUN:
        print(f"AVISO: {len(due)} itens vencidos, limitando a {MAX_PER_RUN} nesta execucao")
        due = due[:MAX_PER_RUN]

    failures = 0
    for item in due:
        label = f"{item['kind']} {item['id']} (previsto {item['when']:%d/%m %H:%M})"
        if dry_run:
            print(f"[dry-run] publicaria {label}")
            continue
        try:
            media_id = publish(item, ig_user_id, token)
            published[item["id"]] = {
                "ig_media_id": media_id,
                "published_at": datetime.now(TZ).isoformat(timespec="seconds"),
                "kind": item["kind"],
            }
            print(f"OK {label} -> ig_media_id={media_id}")
            # Grava a cada item: se o proximo falhar, o que ja saiu nao se perde.
            with open(PUBLISHED_FILE, "w", encoding="utf-8") as f:
                json.dump(published, f, indent=2, ensure_ascii=False, sort_keys=True)
                f.write("\n")
            time.sleep(5)
        except Exception as e:
            failures += 1
            print(f"ERRO {label}: {e}", file=sys.stderr)

    if failures:
        sys.exit(f"{failures} item(ns) falharam")


if __name__ == "__main__":
    main()
