import subprocess,pathlib,sys,json,shutil
from playwright.sync_api import sync_playwright
sys.path.insert(0,str(pathlib.Path(__file__).parent))
import music2 as music
D=pathlib.Path(__file__).parent;FPS=30
def make(spec,out,only=None):
    F=D/'frames_e';shutil.rmtree(F,ignore_errors=True);F.mkdir()
    with sync_playwright() as p:
        b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
        pg=b.new_page(viewport={'width':1080,'height':1920});pg.on('pageerror',lambda e:print('ERR',e))
        pg.goto((D/'engine.html').as_uri());pg.wait_for_timeout(500)
        total=pg.evaluate(f'build({json.dumps(spec)})')
        if only:
            for t in only: pg.evaluate(f'render({t})');pg.screenshot(path=str(D/f'chk_{spec["id"]}_{t}.jpg'),type='jpeg',quality=88)
            return total
        for i in range(int(FPS*total)):
            pg.evaluate(f'render({i/FPS})');pg.screenshot(path=str(F/f'f{i:04d}.jpg'),type='jpeg',quality=90)
        b.close()
    wav=D/f'trilha_{spec["id"]}.wav';music.gen(str(wav),total,seed=spec['seed'],bpm=spec['bpm'])
    subprocess.run(['ffmpeg','-y','-loglevel','error','-framerate',str(FPS),'-i',str(F/'f%04d.jpg'),'-i',str(wav),'-c:v','libx264','-pix_fmt','yuv420p','-crf','19','-c:a','aac','-b:a','160k','-shortest','-movflags','+faststart',out],check=True)
    wav.unlink();shutil.rmtree(F,ignore_errors=True);return total
