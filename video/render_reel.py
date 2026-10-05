import subprocess,pathlib,sys
from playwright.sync_api import sync_playwright
D=pathlib.Path(__file__).parent;F=D/'frames3';FPS=30;DUR=15.5
only=[float(x) for x in sys.argv[1:]]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
    pg=b.new_page(viewport={'width':1080,'height':1920});pg.on('pageerror',lambda e:print('ERR',e));pg.goto((D/'reel_503020.html').as_uri());pg.wait_for_timeout(600)
    if only:
        for t in only: pg.evaluate(f'render({t})');pg.screenshot(path=str(D/f'chk_{t}.jpg'),type='jpeg',quality=90)
        sys.exit()
    for i in range(int(FPS*DUR)):
        pg.evaluate(f'render({i/FPS})');pg.screenshot(path=str(F/f'f{i:04d}.jpg'),type='jpeg',quality=92)
    b.close()
subprocess.run(['ffmpeg','-y','-loglevel','error','-framerate',str(FPS),'-i',str(F/'f%04d.jpg'),'-c:v','libx264','-pix_fmt','yuv420p','-crf','18','-movflags','+faststart',str(D/'wally-reel-50-30-20.mp4')],check=True)
