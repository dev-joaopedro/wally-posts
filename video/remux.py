"""Troca a trilha de um MP4 (mantém o vídeo): python3 remux.py <id> [estilo] [seed]. Usa trilhas.py."""
import sys,subprocess,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import music3
from trilhas import STYLE
ROOT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','reels')
def remux(rid,style=None,seed=None):
    path=os.path.join(ROOT,rid+'.mp4');style=style or STYLE[rid];seed=int(seed if seed is not None else int(rid[1:3]))
    d=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',path]).decode())
    wav=path+'.wav';tmp=path+'.tmp.mp4';music3.gen(wav,d,style,seed)
    subprocess.run(['ffmpeg','-y','-loglevel','error','-i',path,'-i',wav,'-map','0:v','-map','1:a','-c:v','copy','-c:a','aac','-b:a','160k','-shortest','-movflags','+faststart',tmp],check=True)
    os.replace(tmp,path);os.remove(wav)
if __name__=='__main__': remux(*sys.argv[1:])
