"""Monta stories.json: story do post (17h30) + bônus (17h31) nos dias de post; bônus (17h30) nos outros dias úteis."""
import datetime as dt, json, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import stories_content as C

posts = json.load(open(ROOT / "posts.json", encoding="utf-8")) + json.load(open(ROOT / "posts-extra.json", encoding="utf-8"))
post_by_day = {p["d"]: p["id"] for p in posts}
post_by_day["2026-09-30"] = "001-2026-10-05"   # post de apresentação, adiantado para hoje
# o id 001 originalmente era 05/10; ali agora está o extra 000b
post_by_day["2026-10-05"] = "000b-2026-10-05"

days, d = [], dt.date(2026, 9, 30)
while d <= dt.date(2027, 10, 1):
    if d.weekday() < 5: days.append(d.isoformat())
    d += dt.timedelta(1)

pools = {
 "tip": [dict(t="tip", tag="Dica rápida", title=a, sub=b) for a, b in C.TIPS],
 "q": [dict(t="q", title=a, sub=b) for a, b in C.QUESTIONS],
 "num": [dict(t="num", tag="Pra pensar", big=a, text=b, pre=c) for a, b, c in C.NUMS],
 "mito": [dict(t="mito", mito=a, verdade=b) for a, b in C.MITOS],
 "list": [dict(t="list", title=a, tag=b, items=c) for a, b, c in C.LISTS],
 "app": [dict(C.APP[i], t="app") for i in range(len(C.APP))],
}
seq = []
for k, items in pools.items():
    n = len(items)
    for i, it in enumerate(items):
        seq.append(((i + 0.5) / n + hash(k) % 97 / 10000, it))
seq = [it for _, it in sorted(seq, key=lambda x: x[0])]
# dark/light alternado nas dicas
for i, it in enumerate(seq):
    if it["t"] == "tip": it["dark"] = i % 2 == 0

free = [x for x in days if x not in C.DATED]
assert len(seq) >= len(free), (len(seq), len(free))
seq = seq[:len(free)]
bonus = dict(zip(free, seq))
for k, v in C.DATED.items():
    assert k in days, k
    bonus[k] = dict(v)

out = []
for day in days:
    if day in post_by_day:
        out.append(dict(id=f"s-{day}-post", d=day, time="17:30:00", t="post", post=post_by_day[day]))
        b = dict(bonus[day]); b.update(id=f"s-{day}-bonus", d=day, time="17:31:00"); out.append(b)
    else:
        b = dict(bonus[day]); b.update(id=f"s-{day}-bonus", d=day, time="17:30:00"); out.append(b)
json.dump(out, open(ROOT / "stories.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(days), "dias;", len(out), "stories;", sum(1 for s in out if s["t"] == "post"), "de post;", len(seq), "bônus do pool usados de", sum(len(v) for v in pools.values()))

# ---------------------------------------------------------------------------
# Grade nova (a partir de 01/10/2026): post 12h, story do post 13h,
# bônus 9h (os de cima), 16h e 20h (conteúdo de stories_content2.py).
import random
import stories_content2 as C2
START = "2026-10-01"
for s in out:
    if s["d"] < START: continue
    s["time"] = "13:00:00" if s["t"] == "post" else "09:00:00"

pools2 = {
 "tip": [dict(t="tip", tag="Dica rápida", title=a, sub=b) for a, b in C2.TIPS]
        + [dict(t="tip", tag="Lembrete", title=a, sub=b) for a, b in C2.LEMBRETES],
 "q": [dict(t="q", title=a, sub=b) for a, b in C2.QUESTIONS],
 "num": [dict(t="num", tag="Pra pensar", big=a, text=b, pre=c) for a, b, c in C2.NUMS],
 "mito": [dict(t="mito", mito=a, verdade=b) for a, b in C2.MITOS],
 "list": [dict(t="list", title=a, tag=b, items=c) for a, b, c in C2.LISTS],
 "app": [dict(C2.APP[i], t="app") for i in range(len(C2.APP))],
}
rng = random.Random(7)
for k in pools2: rng.shuffle(pools2[k])

def rule(it):
    txt = (it.get("title") or it.get("big") or "") + " " + (it.get("sub") or "")
    W = {"Segunda-feira": 0, "Terça-feira": 1, "Quarta-feira": 2, "Quinta-feira": 3, "Sexta-feira": 4,
         "Pizza de sexta": 4, "_fim de semana_": 4, "Show do fim de semana": 0, "Hambúrguer de domingo": 0,
         "Feira do sábado": 0, "Domingo à noite": 4}
    for key, wd in W.items():
        if key in txt: return lambda d, sl, wd=wd: d.weekday() == wd
    if any(k in txt for k in ["Boa noite", "Antes de dormir", "Bom descanso", "Fim do dia?", "Fim de expediente"]):
        return lambda d, sl: sl == "20"
    if any(k in txt for k in ["Tarde de", "_o almoço_", "Sorvete da tarde", "Lanche no trabalho"]):
        return lambda d, sl: sl == "16"
    if any(k in txt for k in ["Começo de mês", "Primeiro dia do mês", "Salário caiu?", "_começo do ano_"]):
        extra = (lambda d: d.month == 1) if "ano" in txt else (lambda d: True)
        return lambda d, sl, e=extra: d.day <= 5 and e(d)
    if any(k in txt for k in ["Mês quase no fim", "Último dia do mês", "_revisar o mês_"]):
        return lambda d, sl: d.day >= 24
    if "Todo dia 15" in txt: return lambda d, sl: 12 <= d.day <= 18
    if "_presentes do ano_" in txt: return lambda d, sl: d.month == 1
    if "_Natal_" in txt: return lambda d, sl: (d.month, d.day) >= (11, 3) and (d.month, d.day) <= (12, 15)
    if "_Black Friday_" in txt: return lambda d, sl: d.month == 11 and 9 <= d.day <= 25
    if "_o 13º_" in txt or "fazer com o _13º" in txt: return lambda d, sl: d.month in (11, 12)
    if "_fechar o ano_" in txt: return lambda d, sl: d.month == 12 and d.day <= 20
    if "_restituição do IR_" in txt: return lambda d, sl: 6 <= d.month <= 8
    if "_Dia das Mães e dos Pais_" in txt: return lambda d, sl: (d.month == 4 and d.day >= 20) or (d.month == 7 and d.day >= 20)
    if "_o IPVA._" in txt: return lambda d, sl: d.month in (2, 3, 4, 5, 6)
    return None

slots = [(dt.date.fromisoformat(day), sl) for day in days if day >= START for sl in ("16", "20")]
day_types = {}
for s in out:
    if s["t"] != "post": day_types.setdefault(s["d"], []).append(s["t"])
assign = {}
constrained, free_items = [], []
for k, items in pools2.items():
    for it in items:
        (constrained if rule(it) else free_items).append(it)
# datados primeiro: espalha pelo ano nos slots que casam
for it in constrained:
    f = rule(it)
    cands = [x for x in slots if x not in assign and f(*x) and it["t"] not in day_types.get(x[0].isoformat(), [])]
    if not cands: cands = [x for x in slots if x not in assign and f(*x)]
    assert cands, it
    x = rng.choice(cands); assign[x] = it
    day_types.setdefault(x[0].isoformat(), []).append(it["t"])
# resto: intercala os tipos
seq2 = []
for k in pools2:
    items = [i for i in free_items if i["t"] == k]
    n = len(items)
    for i, it in enumerate(items): seq2.append(((i + rng.random()) / n, it))
queue = [it for _, it in sorted(seq2, key=lambda x: x[0])]
for x in slots:
    if x in assign: continue
    used = day_types.get(x[0].isoformat(), [])
    j = next((j for j, it in enumerate(queue[:30]) if it["t"] not in used), 0)
    it = queue.pop(j); assign[x] = it; used.append(it["t"]); day_types[x[0].isoformat()] = used
print("sobraram", len(queue), "itens novos (não usados)")
tipn = 0
for (d, sl), it in sorted(assign.items()):
    it = dict(it)
    if it["t"] == "tip": it["dark"] = tipn % 2 == 0; tipn += 1
    it.update(id=f"s-{d.isoformat()}-b{sl}", d=d.isoformat(), time=f"{sl}:00:00")
    out.append(it)
out.sort(key=lambda s: (s["d"], s["time"]))
json.dump(out, open(ROOT / "stories.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("grade nova:", len(out), "stories no total;", len(assign), "novos")
