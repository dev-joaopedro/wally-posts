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

ROOT = Path(__file__).parent
PUBLISHED_FILE = ROOT / "published.json"


def load_json(path, default=None):
    if not path.exists():
        return default
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def scheduled_at(date_str, time_str):
    return datetime.fromisoformat(f"{date_str}T{time_str}").replace(tzinfo=TZ)


def collect_due(now, published_ids):
    """Retorna os itens vencidos e ainda nao publicados, do mais antigo ao mais novo."""
    due = []

    for p in load_json(ROOT / "posts.json", []):
        when = scheduled_at(p["d"], POST_TIME)
        if p["id"] not in published_ids and now - LOOKBACK <= when <= now:
            due.append({
                "id": p["id"],
                "kind": "post",
                "when": when,
                "image_url": f"{REPO_RAW_BASE}/posts/{p['id']}.jpg",
                "caption": p.get("caption", ""),
            })

    for s in load_json(ROOT / "stories.json", []):
        when = scheduled_at(s["d"], s["time"])
        if s["id"] not in published_ids and now - LOOKBACK <= when <= now:
            due.append({
                "id": s["id"],
                "kind": "story",
                "when": when,
                "image_url": f"{REPO_RAW_BASE}/stories/{s['id']}.jpg",
                "caption": None,  # Stories via API nao aceitam legenda.
            })

    due.sort(key=lambda i: i["when"])
    return due


def publish(item, ig_user_id, token):
    """Cria o container e publica. Retorna o media id do Instagram."""
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
    due = collect_due(now, set(published))

    print(f"agora: {now:%Y-%m-%d %H:%M:%S %Z} | vencidos: {len(due)} | ja publicados: {len(published)}")
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
