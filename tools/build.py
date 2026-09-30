"""Junta os arquivos de conteúdo em posts.json e confere o calendário (seg/qua/sex, sem buracos)."""
import datetime as dt, json, pathlib, sys, importlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

posts = []
for mod in ["q1", "q2", "q3", "q4"]:
    try:
        posts += importlib.import_module(mod).POSTS
    except ModuleNotFoundError:
        pass

expected, d = [], dt.date(2026, 10, 5)
while len(expected) < 156:
    if d.weekday() in (0, 2, 4):
        expected.append(d.isoformat())
    d += dt.timedelta(1)

dates = [p["d"] for p in posts]
assert len(dates) == len(set(dates)), "data repetida"
assert dates == expected[:len(dates)], [(a, b) for a, b in zip(dates, expected) if a != b][:3]
for i, p in enumerate(posts, 1):
    p["id"] = f"{i:03d}-{p['d']}"
    assert len(p["caption"]) <= 2200, (p["id"], len(p["caption"]))
    assert p["caption"].count("#") <= 30

(ROOT / "posts.json").write_text(json.dumps(posts, ensure_ascii=False, indent=1))
print(len(posts), "posts;", "próxima data:", expected[len(posts)] if len(posts) < 156 else "-")
