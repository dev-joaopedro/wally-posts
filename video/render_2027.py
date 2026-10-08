"""Renderiza os Reels de 2027 (reels_2027.py) em ../reels/<id>.mp4, com trilha própria (music4.py).
Uso: python3 render_2027.py [id ...]   (sem ids: todos que ainda não existem)
     python3 render_2027.py --retrack [id ...] (refaz só as trilhas)
     python3 render_2027.py --part 0/2 (divide a lista para rodar em paralelo)"""
import subprocess,pathlib,sys,json,shutil,time
from playwright.sync_api import sync_playwright
D=pathlib.Path(__file__).parent;sys.path.insert(0,str(D))
import music4, reels_2027
FPS=30;OUT=D.parent/'reels'
def seed_of(rid): return int(rid[1:].split('-')[0])
def variant_of(rid):
    st=next(s['style'] for s in reels_2027.SPECS if s['id']==rid)
    return [s['id'] for s in reels_2027.SPECS if s['style']==st].index(rid)
def retrack(rid):
    """Refaz só a trilha de um Reel já renderizado (mantém o vídeo)."""
    spec=next(s for s in reels_2027.SPECS if s['id']==rid);mp4=OUT/f'{rid}.mp4'
    d=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',str(mp4)]).decode())
    wav=D/f'trilha_{rid}.wav';tmp=OUT/f'{rid}.tmp.mp4';music4.gen(str(wav),d,spec['style'],seed_of(rid),variant_of(rid))
    subprocess.run(['ffmpeg','-y','-loglevel','error','-i',str(mp4),'-i',str(wav),'-map','0:v','-map','1:a','-c:v','copy','-c:a','aac','-b:a','160k','-shortest','-movflags','+faststart',str(tmp)],check=True)
    tmp.replace(mp4);wav.unlink()
def make(spec,browser):
    F=D/f'frames_{spec["id"]}';shutil.rmtree(F,ignore_errors=True);F.mkdir()
    pg=browser.new_page(viewport={'width':1080,'height':1920});pg.on('pageerror',lambda e:print('ERR',spec['id'],e))
    pg.goto((D/'engine.html').as_uri());pg.wait_for_timeout(400)
    total=pg.evaluate(f'build({json.dumps({"id":spec["id"],"scenes":spec["scenes"]})})')
    for i in range(int(FPS*total)):
        pg.evaluate(f'render({i/FPS})');pg.screenshot(path=str(F/f'f{i:04d}.jpg'),type='jpeg',quality=90)
    pg.close()
    wav=D/f'trilha_{spec["id"]}.wav';music4.gen(str(wav),total,spec['style'],seed_of(spec['id']),variant_of(spec['id']))
    tmp=OUT/f'{spec["id"]}.tmp.mp4'
    subprocess.run(['ffmpeg','-y','-loglevel','error','-framerate',str(FPS),'-i',str(F/'f%04d.jpg'),'-i',str(wav),'-c:v','libx264','-pix_fmt','yuv420p','-crf','19','-c:a','aac','-b:a','160k','-shortest','-movflags','+faststart',str(tmp)],check=True)
    tmp.replace(OUT/f'{spec["id"]}.mp4');wav.unlink();shutil.rmtree(F,ignore_errors=True);return total
if __name__=='__main__':
    args=sys.argv[1:];specs=reels_2027.SPECS
    if args and args[0]=='--retrack':
        for s in specs if len(args)==1 else [x for x in specs if x['id'] in args[1:]]: retrack(s['id'])
        sys.exit()
    if args and args[0]=='--part':
        k,n=map(int,args[1].split('/'));specs=[s for i,s in enumerate(specs) if i%n==k]
        specs=[s for s in specs if not (OUT/f'{s["id"]}.mp4').exists()]
    elif args: specs=[s for s in specs if s['id'] in args]
    else: specs=[s for s in specs if not (OUT/f'{s["id"]}.mp4').exists()]
    with sync_playwright() as p:
        exe=pathlib.Path('/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
        b=p.chromium.launch(**({'executable_path':str(exe)} if exe.exists() else {}))
        for s in specs:
            t=time.time();d=make(s,b);print(f'{s["id"]} {d:.1f}s em {time.time()-t:.0f}s',flush=True)
        b.close()
