"""Renderiza os stories (1080x1920) a partir de stories.json."""
import base64, json, pathlib, sys
from playwright.sync_api import sync_playwright
import render as R

ROOT = R.ROOT
E, rich = R.E, R.rich

CSS = R.CSS.replace("html,body{width:1080px;height:1350px}", "html,body{width:1080px;height:1920px}") + """
.sty{width:1080px;height:1920px;padding:230px 90px 250px;display:flex;flex-direction:column;position:relative;overflow:hidden;background:#F6F7F9}
.sty.dark{background:#0E1A33;color:#fff}
.sty.dark::before{content:"";position:absolute;right:-300px;top:-200px;width:900px;height:900px;border-radius:50%;background:radial-gradient(circle,rgba(42,91,215,.5),transparent 68%)}
.sty.light::before{content:"";position:absolute;right:-300px;top:-200px;width:900px;height:900px;border-radius:50%;background:radial-gradient(circle,rgba(42,91,215,.10),transparent 68%)}
.sty .tag{font-size:30px;padding:14px 26px}
.sty .body{gap:48px}
.sty h1{font-size:112px;line-height:1.02}
.sty h1.m{font-size:96px}.sty h1.s{font-size:82px}
.sty .sub{font-size:44px;line-height:1.4}
.sty .big{font-size:260px}.sty .big.m{font-size:190px}.sty .big.s{font-size:140px}
.sty .foot{border-top:none;padding-top:0;justify-content:center}
.sty .brand{font-size:40px}.sty .logo{width:60px;height:60px;font-size:34px;border-radius:15px}
.cta{align-self:flex-start;font-size:40px;font-weight:600;padding:22px 34px;border-radius:99px;background:#2A5BD7;color:#fff}
.post{border-radius:28px;overflow:hidden;box-shadow:0 30px 80px rgba(0,0,0,.45);align-self:center;width:860px}
.post img{display:block;width:100%}
.sty .row p{font-size:52px}.sty .n{width:70px;height:70px;font-size:34px}
.sty .mc p{font-size:58px}.sty .mc span{font-size:30px}
.sty .u{font-size:42px}.sty .wt{font-size:40px}.sty .chead b{font-size:38px}.sty .chead small{font-size:28px}
.sty .card .nm b{font-size:40px}.sty .card .nm small{font-size:30px}.sty .amt{font-size:44px}.sty .ok{font-size:30px}.sty .ic{width:84px;height:84px;font-size:42px}
"""

def frame(inner, dark, tag):
    return (f'<div class="sty {"dark" if dark else "light"}">{R.tag(tag)}<div class="body">{inner}</div>'
            f'<div class="foot"><div class="brand"><div class="logo">W</div>@wally_financeiro</div></div></div>')

def h1(t):
    n = len(t)
    c = "" if n <= 40 else ("m" if n <= 70 else "s")
    return f'<h1 class="{c}">{rich(t)}</h1>'

def b64(path):
    return "data:image/jpeg;base64," + base64.b64encode(path.read_bytes()).decode()

def s_post(s):
    img = b64(ROOT / "posts" / f'{s["post"]}.jpg')
    return frame(f'<h1 class="s" style="font-size:88px">Post novo <em>no feed</em> 👀</h1>'
                 f'<div class="post"><img src="{img}"></div>', True, "Acabou de sair")

def s_tip(s):
    sub = f'<p class="sub">{rich(s["sub"])}</p>' if s.get("sub") else ""
    return frame(f'{h1(s["title"])}{sub}', s.get("dark", True), s["tag"])

def s_num(s):
    big = s["big"]; c = "" if len(big) <= 4 else ("m" if len(big) <= 7 else "s")
    head = f'<p class="sub" style="font-size:52px">{rich(s["pre"])}</p>' if s.get("pre") else ""
    return frame(f'{head}<div class="big {c}">{rich(big)}</div><p class="sub">{rich(s["text"])}</p>',
                 s.get("dark", True), s["tag"])

def s_q(s):
    return frame(f'{h1(s["title"])}<p class="sub">{rich(s.get("sub", ""))}</p>'
                 f'<div class="cta">Responde no direct 💬</div>', True, s.get("tag", "Pergunta do dia"))

def s_mito(s):
    return frame(f'<div class="mv"><div class="mc x"><span>✕ Mito</span><p>{rich(s["mito"])}</p></div>'
                 f'<div class="mc v"><span>✓ Verdade</span><p>{rich(s["verdade"])}</p></div></div>',
                 False, "Mito ou verdade")

def s_list(s):
    rows = "".join(f'<div class="row"><div class="n">{i+1}</div><p>{rich(x)}</p></div>' for i, x in enumerate(s["items"]))
    return frame(f'{h1(s["title"])}<div class="list">{rows}</div>', False, s["tag"])

def s_app(s):
    parts = [f'{h1(s["title"])}']
    if s.get("sub"): parts.append(f'<p class="sub">{rich(s["sub"])}</p>')
    if s.get("img"):
        img = "data:image/png;base64," + base64.b64encode((R.SHOTS / f'{s["img"]}.png').read_bytes()).decode()
        parts.append(f'<div class="shot"><div class="bar"><i></i><i></i><i></i></div><img src="{img}"></div>')
    if s.get("msgs"):
        fake = dict(title="", tag="", msgs=s["msgs"])
        html = R.t_chat(fake)
        chat = html[html.index('<div class="chat">'):html.index('</div><div class="foot">')]
        parts.append(chat)
    return frame("".join(parts), s.get("dark", False), s.get("tag", "Wally na prática"))

T = dict(post=s_post, tip=s_tip, num=s_num, q=s_q, mito=s_mito, list=s_list, app=s_app)

def page(inner):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{inner}</body></html>'

def main():
    stories = json.loads((ROOT / "stories.json").read_text())
    only = set(sys.argv[1:])
    out = ROOT / "img"; out.mkdir(exist_ok=True)
    with sync_playwright() as pw:
        b = pw.chromium.launch(executable_path="/opt/pw-browsers/chromium-1194/chrome-linux/chrome")
        pg = b.new_page(viewport={"width": 1080, "height": 1920})
        for s in stories:
            if only and s["id"] not in only: continue
            pg.set_content(page(T[s["t"]](s)), wait_until="load")
            pg.wait_for_timeout(40)
            if pg.evaluate("document.querySelector('.body').scrollHeight > document.querySelector('.body').clientHeight + 2"):
                print("ESTOURO:", s["id"])
            pg.screenshot(path=str(out / f'{s["id"]}.png'))
        b.close()
    print("ok")

if __name__ == "__main__":
    main()
