"""Gera uma trilha de fundo original (sem direitos autorais): pad + baixo + pluck + batida leve."""
import numpy as np, wave, sys
def note(m): return 440*2**((m-69)/12)
def gen(path, dur, seed=1, bpm=84, prog=None, pulse=True):
    sr=44100; beat=60/bpm; n=int(sr*dur); t=np.arange(n)/sr; rng=np.random.default_rng(seed)
    prog=prog or [[57,60,64,67],[53,57,60,64],[48,52,55,59],[55,59,62,65]]
    bar=beat*4; out=np.zeros(n)
    for i in range(int(dur/bar)+2):
        s=int(i*bar*sr); e=min(n,int((i+1)*bar*sr+beat*sr))
        if s>=n: break
        tt=np.arange(e-s)/sr
        env=np.minimum(1,tt/0.35)*np.exp(-tt/(bar*1.4))*np.minimum(1,(len(tt)-np.arange(len(tt)))/(0.4*sr))
        c=prog[i%len(prog)]
        pad=sum(np.sin(2*np.pi*note(m)*tt)+0.3*np.sin(2*np.pi*note(m)*2*tt+0.5)+0.15*np.sin(2*np.pi*note(m)*tt*1.003) for m in c)
        out[s:e]+=0.05*pad*env
        out[s:e]+=0.16*np.sin(2*np.pi*note(c[0]-12)*tt)*env
    pat=[[1,2,3,2,1,3,2,3],[3,2,1,2,3,2,1,2],[1,3,2,3,1,2,3,2]][seed%3]
    for k in range(int(dur/(beat/2))):
        s=int(k*beat/2*sr); L=int(0.45*sr)
        if s+L>n: break
        c=prog[int((k*beat/2)//bar)%len(prog)]; m=c[pat[k%8]]+12; tt=np.arange(L)/sr
        out[s:s+L]+=0.07*np.sin(2*np.pi*note(m)*tt)*np.exp(-tt*7)
    if pulse:
        for k in range(int(dur/beat)):
            s=int(k*beat*sr)
            if k%4 in(0,2) or k%8==3:
                L=int(.25*sr);tt=np.arange(L)/sr;f=110*np.exp(-tt*18)+45
                if s+L<=n: out[s:s+L]+=0.35*np.sin(2*np.pi*np.cumsum(f)/sr)*np.exp(-tt*10)
            for h in (0,.5):
                hs=int((k+h)*beat*sr);L=int(.05*sr)
                if hs+L<=n: out[hs:hs+L]+=0.04*rng.standard_normal(L)*np.exp(-np.arange(L)/sr*70)*(1.0 if h==0 else .6)
            if k%4 in(1,3):
                L=int(.16*sr)
                if s+L<=n: out[s:s+L]+=0.08*rng.standard_normal(L)*np.exp(-np.arange(L)/sr*22)
    out=np.convolve(out,np.ones(5)/5,'same')
    out*=np.minimum(1,t/1.0)*np.minimum(1,(dur-t)/1.5)
    out=out/np.max(np.abs(out))*0.85
    st=np.stack([out,np.roll(out,int(0.012*sr))],1)
    w=wave.open(path,'wb');w.setnchannels(2);w.setsampwidth(2);w.setframerate(sr)
    w.writeframes((st*32767).astype('<i2').tobytes());w.close()
