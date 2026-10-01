import subprocess,pathlib
from playwright.sync_api import sync_playwright
D=pathlib.Path(__file__).parent;F=D/'frames';FPS=24;DUR=17.5
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
    pg=b.new_page(viewport={'width':1080,'height':1920})
    pg.goto((D/'pilot.html').as_uri());pg.wait_for_timeout(500)
    for i in range(int(FPS*DUR)):
        pg.evaluate(f'render({i/FPS})');pg.screenshot(path=str(F/f'f{i:04d}.jpg'),type='jpeg',quality=92)
    b.close()
subprocess.run(['ffmpeg','-y','-loglevel','error','-framerate',str(FPS),'-i',str(F/'f%04d.jpg'),'-c:v','libx264','-pix_fmt','yuv420p','-crf','18','-movflags','+faststart',str(D/'wally-piloto.mp4')],check=True)
