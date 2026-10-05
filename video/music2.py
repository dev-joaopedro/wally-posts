"""Trilha original de mistério/investigação (sem direitos autorais): drone grave, pad menor,
notas esparsas com eco e reverb, relógio ao fundo, batida de coração e acordes dissonantes."""
import numpy as np, wave
def nf(m): return 440*2**((m-69)/12)
def lp(x,k):  # passa-baixa simples
    return np.convolve(x,np.ones(k)/k,'same')
def reverb(x,sr,rng,sec=2.2,mix=.35):
    L=int(sr*sec); ir=rng.standard_normal(L)*np.exp(-np.arange(L)/sr*2.6); ir=lp(ir,6); ir/=np.sqrt((ir**2).sum())
    n=len(x)+L; X=np.fft.rfft(x,n); Y=np.fft.rfft(ir,n); wet=np.fft.irfft(X*Y,n)[:len(x)]
    return x*(1-mix)+wet*mix*2.2
def echo(x,sr,d=.375,fb=.45,n=4):
    y=x.copy()
    for i in range(1,n+1):
        s=int(d*sr*i)
        if s<len(x): y[s:]+=x[:len(x)-s]*fb**i
    return y
# acordes (MIDI): Am(maj7), Fmaj7#11, Dm9, E7b9
CH=[[45,57,60,64,68],[41,53,57,64,71],[38,50,57,60,64],[40,52,56,59,62,65]]
SC=[57,59,60,62,64,65,68,69,72,71]  # A menor harmônica
def gen(path,dur,seed=1,bpm=72):
    sr=44100;rng=np.random.default_rng(seed*7+3);n=int(sr*dur);t=np.arange(n)/sr;beat=60/bpm;bar=beat*4
    rot=seed%4; prog=CH[rot:]+CH[:rot]
    pad=np.zeros(n);bass=np.zeros(n)
    for i in range(int(dur/bar)+2):
        s=int(i*bar*sr);e=min(n,int((i+1)*bar*sr+beat*sr))
        if s>=n: break
        tt=np.arange(e-s)/sr;c=prog[i%4]
        env=np.minimum(1,tt/1.2)*np.minimum(1,(len(tt)-np.arange(len(tt)))/(1.2*sr))
        v=sum(np.sin(2*np.pi*nf(m)*tt)+.5*np.sin(2*np.pi*nf(m)*2*tt)+.25*np.sin(2*np.pi*nf(m)*3*tt) for m in c[1:])
        pad[s:e]+=0.028*lp(v,3)*env*(1+.15*np.sin(2*np.pi*.18*tt))
        bass[s:e]+=0.2*np.sin(2*np.pi*nf(c[0])*tt)*env
    drone=0.11*np.sin(2*np.pi*nf(33)*t)*(.7+.3*np.sin(2*np.pi*.11*t))
    # notas esparsas (motivo) com eco
    mel=np.zeros(n);k=0;pos=2.0*beat;idx=3
    while pos<dur-1:
        idx=int(np.clip(idx+rng.choice([-2,-1,1,2]),0,len(SC)-1));m=SC[idx]+(12 if rng.random()<.2 else 0)
        L=int(1.4*sr);s=int(pos*sr)
        if s+L<n:
            tt=np.arange(L)/sr;mel[s:s+L]+=0.11*(np.sin(2*np.pi*nf(m)*tt)+.3*np.sin(2*np.pi*nf(m)*2*tt))*np.exp(-tt*3.2)*np.minimum(1,tt/.01)
        pos+=beat*rng.choice([1,1.5,2,2,3])
    mel=echo(mel,sr,d=beat*.75,fb=.5)
    # relógio (tique-taque) e batida de coração
    tick=np.zeros(n)
    for j in range(int(dur/(beat/2))):
        s=int(j*beat/2*sr);L=int(.03*sr)
        if s+L<n: tick[s:s+L]+=(0.05 if j%2==0 else .028)*np.sin(2*np.pi*(2600 if j%2==0 else 2100)*np.arange(L)/sr)*np.exp(-np.arange(L)/sr*180)
    heart=np.zeros(n)
    for j in range(int(dur/(beat*2))):
        for off,g in((0,.5),(.3,.32)):
            s=int((j*beat*2+off)*sr);L=int(.22*sr)
            if s+L<n:
                tt=np.arange(L)/sr;f=70*np.exp(-tt*14)+38;heart[s:s+L]+=g*np.sin(2*np.pi*np.cumsum(f)/sr)*np.exp(-tt*12)
    # acorde dissonante raro (trítono) com cauda
    stab=np.zeros(n)
    for pos in np.arange(bar*3,dur-2,bar*4):
        s=int(pos*sr);L=int(2.5*sr)
        if s+L<n:
            tt=np.arange(L)/sr;stab[s:s+L]+=0.06*(np.sin(2*np.pi*nf(45)*tt)+np.sin(2*np.pi*nf(51)*tt)+.5*np.sin(2*np.pi*nf(57)*tt))*np.exp(-tt*1.6)
    mix=reverb(pad+mel+stab,sr,rng)+bass+drone+tick+heart*0.9
    mix*=np.minimum(1,t/1.5)*np.minimum(1,(dur-t)/1.8)
    mix=mix/np.max(np.abs(mix))*0.82
    st=np.stack([mix,np.roll(mix,int(.015*sr))],1)
    w=wave.open(path,'wb');w.setnchannels(2);w.setsampwidth(2);w.setframerate(sr);w.writeframes((st*32767).astype('<i2').tobytes());w.close()
