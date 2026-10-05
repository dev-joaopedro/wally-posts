"""Troca a trilha de um MP4 (mantém o vídeo): python3 remux.py <arquivo.mp4> <seed> <bpm>"""
import sys,subprocess,os,tempfile
sys.path.insert(0,os.path.dirname(__file__))
import music2
def remux(path,seed,bpm):
    d=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',path]).decode())
    wav=path+'.wav';tmp=path+'.tmp.mp4';music2.gen(wav,d,seed=seed,bpm=bpm)
    subprocess.run(['ffmpeg','-y','-loglevel','error','-i',path,'-i',wav,'-map','0:v','-map','1:a','-c:v','copy','-c:a','aac','-b:a','160k','-shortest','-movflags','+faststart',tmp],check=True)
    os.replace(tmp,path);os.remove(wav)
if __name__=='__main__': remux(sys.argv[1],int(sys.argv[2]),float(sys.argv[3]))
