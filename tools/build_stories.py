"""Monta stories.json: story do post (17h30) + bônus (17h31) nos dias de post; bônus (17h30) nos outros dias úteis."""
import datetime as dt, json, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import stories_content as C

posts = json.load(open(ROOT / "posts.json")) + json.load(open(ROOT / "posts-extra.json"))
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
json.dump(out, open(ROOT / "stories.json", "w"), ensure_ascii=False, indent=1)
print(len(days), "dias;", len(out), "stories;", sum(1 for s in out if s["t"] == "post"), "de post;", len(seq), "bônus do pool usados de", sum(len(v) for v in pools.values()))
