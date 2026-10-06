"""Renderiza as artes do Instagram do Wally (1080x1350) a partir de posts.json."""
import html, json, sys, pathlib
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
SHOTS = ROOT / "tools" / "shots"
E = html.escape

CSS = """
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1350px}
body{font-family:'Geist',sans-serif;font-variant-numeric:tabular-nums;-webkit-font-smoothing:antialiased;color:#1B2437}
.f{width:1080px;height:1350px;padding:84px 84px 64px;display:flex;flex-direction:column;position:relative;overflow:hidden;background:#F6F7F9}
.f.dark{background:#0E1A33;color:#fff}
.f.dark::before{content:"";position:absolute;right:-260px;top:-260px;width:760px;height:760px;border-radius:50%;background:radial-gradient(circle,rgba(42,91,215,.45),transparent 68%)}
.f.light::before{content:"";position:absolute;right:-300px;top:-300px;width:800px;height:800px;border-radius:50%;background:radial-gradient(circle,rgba(42,91,215,.09),transparent 68%)}
.tag{align-self:flex-start;display:inline-flex;align-items:center;gap:12px;padding:12px 22px;border-radius:99px;font-size:26px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;background:#EDF2FD;color:#2A5BD7;border:1.5px solid #BFD0F7;position:relative}
.dark .tag{background:rgba(255,255,255,.08);color:#BFD0F7;border-color:rgba(191,208,247,.3)}
.tag i{width:10px;height:10px;border-radius:50%;background:currentColor;display:block}
.body{flex:1;display:flex;flex-direction:column;justify-content:center;position:relative;gap:40px}
h1{font-size:92px;line-height:1.03;font-weight:600;letter-spacing:-.045em;color:#0E1A33}
h1.m{font-size:80px}h1.s{font-size:68px}
.dark h1{color:#fff}
h1 em{font-style:normal;color:#2A5BD7}.dark h1 em{color:#93AEF0}
.sub{font-size:36px;line-height:1.45;color:#5E6679;letter-spacing:-.01em}
.dark .sub{color:#A3B1CC}
.list{display:flex;flex-direction:column;gap:18px}
.row{display:flex;gap:24px;align-items:flex-start;background:#fff;border:1.5px solid #E9ECF1;border-radius:24px;padding:30px 34px}
.n{flex:none;width:60px;height:60px;border-radius:16px;background:#EDF2FD;color:#2A5BD7;font-weight:700;font-size:30px;display:flex;align-items:center;justify-content:center}
.n.ck{background:#E8F5EF;color:#13875B}
.row p{font-size:36px;line-height:1.34;color:#1B2437;padding-top:6px;letter-spacing:-.01em}
.row p b{font-weight:600;color:#0E1A33}
.big{font-size:190px;font-weight:600;letter-spacing:-.06em;line-height:.95;color:#fff}
.big.m{font-size:140px}.big.s{font-size:104px}
.light .big{color:#0E1A33}
.big em{font-style:normal;color:#93AEF0}.light .big em{color:#2A5BD7}
.foot{display:flex;justify-content:space-between;align-items:center;position:relative;padding-top:36px;border-top:1.5px solid #E9ECF1}
.dark .foot{border-top-color:rgba(255,255,255,.12)}
.brand{display:flex;align-items:center;gap:14px;font-size:34px;font-weight:600;letter-spacing:-.03em;color:#0E1A33}
.dark .brand{color:#fff}
.logo{width:50px;height:50px;border-radius:13px;background:#0E1A33;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:28px;letter-spacing:-.03em}
.dark .logo{background:#fff;color:#0E1A33}
.handle{font-size:26px;color:#8E95A5;font-weight:500}
.dark .handle{color:#A3B1CC}
/* chat */
.chat{background:#E9EEF4;border-radius:28px;padding:30px;display:flex;flex-direction:column;gap:18px;border:1.5px solid #E3E7EE}
.chead{display:flex;align-items:center;gap:16px;padding-bottom:18px;border-bottom:1.5px solid #D9DFE8}
.chead .logo{width:56px;height:56px;border-radius:50%}
.chead b{font-size:32px;color:#0E1A33;display:block;letter-spacing:-.02em}.chead small{font-size:25px;color:#6E8FC0}
.u{align-self:flex-end;background:#DCF3D2;border-radius:22px 22px 6px 22px;padding:22px 28px;font-size:34px;max-width:80%;color:#1B2437}
.wt{align-self:flex-start;background:#fff;border-radius:22px 22px 22px 6px;padding:22px 28px;font-size:32px;max-width:86%;line-height:1.4;color:#1B2437}
.card{align-self:flex-start;background:#fff;border-radius:22px;padding:24px 26px;min-width:66%;display:flex;flex-direction:column;gap:16px}
.card .top{display:flex;gap:18px;align-items:center}
.ic{width:72px;height:72px;border-radius:16px;background:#F1F3F6;display:flex;align-items:center;justify-content:center;font-size:32px;flex:none}
.card .nm{flex:1}.card .nm b{font-size:34px;color:#0E1A33;display:block;letter-spacing:-.02em}.card .nm small{font-size:26px;color:#5E6679}
.amt{font-size:38px;font-weight:600;letter-spacing:-.03em;white-space:nowrap}
.amt.exp{color:#C8464F}.amt.inc{color:#13875B}
.ok{align-self:flex-start;background:#E8F5EF;color:#13875B;font-size:25px;font-weight:600;padding:8px 16px;border-radius:99px}
/* tela */
.shot{border-radius:24px;overflow:hidden;border:1.5px solid #E9ECF1;background:#fff;box-shadow:0 24px 64px rgba(14,26,51,.14)}
.dark .shot{border-color:rgba(255,255,255,.15);box-shadow:0 24px 64px rgba(0,0,0,.35)}
.bar{height:44px;background:#F6F7F9;border-bottom:1.5px solid #E9ECF1;display:flex;align-items:center;gap:9px;padding:0 18px}
.bar i{width:13px;height:13px;border-radius:50%;background:#D3D8E2;display:block}
.shot img{display:block;width:100%}
/* mito */
.mv{display:flex;flex-direction:column;gap:20px}
.mc{border-radius:24px;padding:34px 36px;display:flex;flex-direction:column;gap:14px;border:1.5px solid}
.mc.x{background:#FBEEEF;border-color:#F3D2D5}.mc.v{background:#E8F5EF;border-color:#BFE3D1}
.mc span{font-size:27px;font-weight:700;letter-spacing:.08em;text-transform:uppercase}
.mc.x span{color:#C8464F}.mc.v span{color:#13875B}
.mc p{font-size:42px;line-height:1.35;letter-spacing:-.015em;color:#1B2437}
/* comp */
.cp{display:grid;grid-template-columns:1fr 1fr;gap:18px}
.col{border-radius:24px;padding:30px;display:flex;flex-direction:column;gap:20px;background:#fff;border:1.5px solid #E9ECF1}
.col.hi{background:#0E1A33;border-color:#0E1A33}
.col h3{font-size:36px;font-weight:600;letter-spacing:-.02em;color:#8E95A5}
.col.hi h3{color:#93AEF0}
.col p{font-size:33px;line-height:1.35;color:#5E6679;display:flex;gap:12px}
.col.hi p{color:#fff}
.col p b{flex:none;font-weight:700}
.col p b.no{color:#C8464F}.col p b.yes2{color:#13875B}.col p span b{font-weight:600;color:#0E1A33}.col.hi p span b{color:#fff}.col p b.yes{color:#6FD3A6}
/* cta */
.btn{align-self:flex-start;background:#2A5BD7;color:#fff;font-size:38px;font-weight:600;padding:26px 44px;border-radius:18px;letter-spacing:-.02em;box-shadow:0 10px 28px rgba(42,91,215,.4)}
.url{font-size:30px;color:#A3B1CC}.light .url{color:#5E6679}
.price{display:flex;align-items:baseline;gap:14px}.price b{font-size:120px;font-weight:600;letter-spacing:-.05em;color:#fff}.price span{font-size:34px;color:#A3B1CC}
.feat{display:flex;flex-direction:column;gap:14px}.feat p{font-size:36px;color:#fff;display:flex;gap:16px}.feat p b{color:#6FD3A6}
"""

def tag(t): return f'<div class="tag"><i></i>{E(t)}</div>'

def rich(s):
    """**negrito** e _destaque_ (azul) em texto simples."""
    s = E(s)
    out, b, e = "", False, False
    i = 0
    while i < len(s):
        if s.startswith("**", i):
            out += "</b>" if b else "<b>"; b = not b; i += 2; continue
        if s[i] == "_":
            out += "</em>" if e else "<em>"; e = not e; i += 1; continue
        out += s[i]; i += 1
    return out.replace("\n", "<br>")

def hsize(t, big=34, mid=52):
    n = len(t)
    return "" if n <= big else ("m" if n <= mid else "s")

def foot():
    return ('<div class="foot"><div class="brand"><div class="logo">W</div>Wally</div>'
            '<div class="handle">@wally_financeiro</div></div>')

def frame(inner, dark=False, tagtxt=""):
    return (f'<div class="f {"dark" if dark else "light"}">{tag(tagtxt)}'
            f'<div class="body">{inner}</div>{foot()}</div>')

def h1(t): return f'<h1 class="{hsize(t)}">{rich(t)}</h1>'

def t_dica(p):
    ck = p.get("style") == "check"
    rows = "".join(
        f'<div class="row"><div class="n{" ck" if ck else ""}">{"✓" if ck else i+1}</div><p>{rich(x)}</p></div>'
        for i, x in enumerate(p["items"]))
    sub = f'<p class="sub">{rich(p["sub"])}</p>' if p.get("sub") else ""
    return frame(f'<div>{h1(p["title"])}</div>{sub}<div class="list">{rows}</div>', False, p["tag"])

def t_destaque(p):
    big = p["big"]; cls = "" if len(big) <= 5 else ("m" if len(big) <= 8 else "s")
    head = f'<h1 class="{hsize(p["title"])}">{rich(p["title"])}</h1>' if p.get("title") else ""
    return frame(f'{head}<div class="big {cls}">{rich(big)}</div><p class="sub">{rich(p["text"])}</p>',
                 p.get("dark", True), p["tag"])

def t_frase(p):
    sub = f'<p class="sub">{rich(p["sub"])}</p>' if p.get("sub") else ""
    t = p["title"]; c = "" if len(t) <= 60 else ("m" if len(t) <= 95 else "s")
    return frame(f'<h1 class="{c}" style="font-size:{ {"":104,"m":88,"s":74}[c] }px">{rich(t)}</h1>{sub}',
                 p.get("dark", True), p["tag"])

def t_chat(p):
    parts = ['<div class="chead"><div class="logo">W</div><div><b>Wally Finance</b><small>bot · sempre disponível</small></div></div>']
    for kind, v in p["msgs"]:
        if kind == "u": parts.append(f'<div class="u">{E(v)}</div>')
        elif kind == "wt": parts.append(f'<div class="wt">{rich(v)}</div>')
        else:
            inc = v.get("inc", False)
            badge = v.get("badge", "Receita registrada" if inc else "Despesa registrada")
            parts.append(
                f'<div class="card"><div class="top"><div class="ic">{v["icon"]}</div>'
                f'<div class="nm"><b>{E(v["name"])}</b><small>{E(v["cat"])}</small></div>'
                f'<div class="amt {"inc" if inc else "exp"}">{"+" if inc else "−"} R$ {E(v["amt"])}</div></div>'
                f'<div class="ok">✓ {E(badge)}</div></div>')
    return frame(f'<div>{h1(p["title"])}</div><div class="chat">{"".join(parts)}</div>', False, p["tag"])

def t_tela(p):
    import base64
    img = "data:image/png;base64," + base64.b64encode((SHOTS / f'{p["img"]}.png').read_bytes()).decode()
    sub = f'<p class="sub">{rich(p["sub"])}</p>' if p.get("sub") else ""
    w = p.get("w")
    st = f' style="width:{w}px;align-self:center"' if w else ""
    return frame(f'<div>{h1(p["title"])}</div>{sub}<div class="shot"{st}><div class="bar"><i></i><i></i><i></i></div>'
                 f'<img src="{img}"></div>', p.get("dark", False), p["tag"])

def t_mito(p):
    return frame(f'<div>{h1(p["title"])}</div><div class="mv">'
                 f'<div class="mc x"><span>✕ Mito</span><p>{rich(p["mito"])}</p></div>'
                 f'<div class="mc v"><span>✓ Verdade</span><p>{rich(p["verdade"])}</p></div></div>', False, p["tag"])

def t_comp(p):
    (la, li), (ra, ri) = p["left"], p["right"]
    lm = '<b class="yes2">✓</b>' if p.get("left_ok") else '<b class="no">✕</b>'
    L = "".join(f'<p>{lm}<span>{rich(x)}</span></p>' for x in li)
    R = "".join(f'<p><b class="yes">✓</b><span>{rich(x)}</span></p>' for x in ri)
    return frame(f'<div>{h1(p["title"])}</div><div class="cp"><div class="col"><h3>{E(la)}</h3>{L}</div>'
                 f'<div class="col hi"><h3>{E(ra)}</h3>{R}</div></div>', False, p["tag"])

def t_cta(p):
    extra = ""
    if p.get("price"):
        feats = "".join(f'<p><b>✓</b>{E(x)}</p>' for x in p.get("feats", []))
        extra = f'<div class="price"><b>R$ 19,90</b><span>/mês</span></div><div class="feat">{feats}</div>'
    sub = f'<p class="sub">{rich(p["sub"])}</p>' if p.get("sub") else ""
    return frame(f'{h1(p["title"])}{sub}{extra}<div class="btn">{E(p.get("button","Crie sua conta grátis"))}</div>'
                 f'<div class="url">wallyfinance.netlify.app</div>', True, p["tag"])

T = dict(dica=t_dica, destaque=t_destaque, frase=t_frase, chat=t_chat, tela=t_tela,
         mito=t_mito, comp=t_comp, cta=t_cta)

def page(inner):
    return f'<!doctype html><html><head><meta charset="utf-8"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&display=swap" rel="stylesheet"><style>{CSS}</style></head><body>{inner}</body></html>'

def main():
    posts = json.loads((ROOT / "posts.json").read_text(encoding="utf-8")) + (json.loads((ROOT / "posts-extra.json").read_text(encoding="utf-8")) if (ROOT / "posts-extra.json").exists() else [])
    only = set(sys.argv[1:])
    out = ROOT / "img"  # PNGs; convertidos para posts/*.jpg; out.mkdir(exist_ok=True)
    with sync_playwright() as pw:
        _exe = pathlib.Path("/opt/pw-browsers/chromium-1194/chrome-linux/chrome")
        b = pw.chromium.launch(**({"executable_path": str(_exe)} if _exe.exists() else {}))
        pg = b.new_page(viewport={"width": 1080, "height": 1350})
        for p in posts:
            if only and p["id"] not in only: continue
            pg.set_content(page(T[p["t"]](p)), wait_until="load")
            pg.evaluate("document.fonts.ready")
            pg.wait_for_timeout(60)
            # checagem de estouro: o corpo não pode passar do quadro
            over = pg.evaluate("document.querySelector('.body').scrollHeight > document.querySelector('.body').clientHeight + 2")
            if over: print("ESTOURO:", p["id"])
            pg.screenshot(path=str(out / f'{p["id"]}.png'))
        b.close()
    print("ok")

if __name__ == "__main__":
    main()
