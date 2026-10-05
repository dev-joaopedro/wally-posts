"""Trilhas originais por estilo/época (sem direitos autorais).
estilos: bright (dias comuns), energetic (Black Friday), festive (Natal/dezembro),
warm (véspera de Natal), hopeful (metas), celebration (Réveillon)."""
import numpy as np, wave
from music2 import reverb
SR=44100
def nf(m): return 440*2**((m-69)/12)
def lp(x,k): return np.convolve(x,np.ones(k)/k,'same')
def hp(x,k): return x-lp(x,k)
def put(buf,s,sig):
    e=min(len(buf),s+len(sig))
    if s<len(buf) and e>s: buf[s:e]+=sig[:e-s]
def pluck(m,L=.5,g=.2,dec=7):
    tt=np.arange(int(L*SR))/SR;f=nf(m)
    return g*(np.sin(2*np.pi*f*tt)+.4*np.sin(4*np.pi*f*tt)+.15*np.sin(6*np.pi*f*tt))*np.exp(-tt*dec)*np.minimum(1,tt/.004)
def bell(m,L=1.2,g=.12,dec=3.5):
    tt=np.arange(int(L*SR))/SR;f=nf(m);y=0
    for r,a in((1,1),(2.76,.45),(5.4,.22),(8.93,.1)): y=y+a*np.sin(2*np.pi*f*r*tt)*np.exp(-tt*dec*(1+.35*r))
    return g*y*np.minimum(1,tt/.002)
def kick(g=.5):
    tt=np.arange(int(.24*SR))/SR;f=120*np.exp(-tt*20)+48;return g*np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-tt*11)
def clap(rng,g=.12):
    L=int(.14*SR);return g*hp(rng.standard_normal(L),20)*np.exp(-np.arange(L)/SR*26)
def hat(rng,g=.05,dec=90):
    L=int(.06*SR);return g*hp(rng.standard_normal(L),6)*np.exp(-np.arange(L)/SR*dec)
def sleigh(rng,g=.05):
    L=int(.18*SR);tt=np.arange(L)/SR
    y=sum(np.sin(2*np.pi*f*tt+rng.random()*6) for f in(3150,4300,5700,7000))*.25+hp(rng.standard_normal(L),5)*.5
    return g*y*np.exp(-tt*24)
def saw(m,L,g=.2):
    tt=np.arange(int(L*SR))/SR;f=nf(m);y=sum(np.sin(2*np.pi*f*k*tt)/k for k in range(1,7))
    return g*lp(y,3)*np.exp(-tt*2.5)*np.minimum(1,tt/.005)
KEYS=[0,7,2,5,9,4,10]  # C G D F A E Bb
def gen(path,dur,style='bright',seed=1):
    rng=np.random.default_rng(seed*13+5);n=int(SR*dur);t=np.arange(n)/SR
    bpm={'bright':100,'energetic':124,'festive':104,'warm':72,'hopeful':96,'celebration':112}[style]
    bpm+=[-4,0,4,2,-2][seed%5]; beat=60/bpm;bar=beat*4
    root=48+KEYS[seed%len(KEYS)]
    prog=[[0,4,7],[7,11,14],[9,12,16],[5,9,12]]; 
    if style=='hopeful': prog=[[0,4,7],[5,9,12],[9,12,16],[7,11,14]]
    pent=[0,2,4,7,9,12,14,16,19,21]
    pad=np.zeros(n);mel=np.zeros(n);bass=np.zeros(n);drm=np.zeros(n);fx=np.zeros(n)
    nb=int(dur/bar)+2
    for i in range(nb):
        s0=i*bar;c=prog[i%4];cm=[root+x for x in c]
        S=int(s0*SR);L=int((bar+beat)*SR);tt=np.arange(L)/SR
        env=np.minimum(1,tt/.25)*np.minimum(1,(L-np.arange(L))/(.5*SR))
        gp={'warm':.05,'energetic':.03}.get(style,.04)
        v=sum(np.sin(2*np.pi*nf(m)*tt)+.35*np.sin(4*np.pi*nf(m)*tt) for m in cm)
        put(pad,S,gp*lp(v,3)*env)
        # baixo
        if style in('bright','festive','hopeful','celebration'):
            for b in range(4): 
                if b%2==0 or style=='celebration': put(bass,int((s0+b*beat)*SR),pluck(cm[0]-12,.4,.22,6))
        elif style=='energetic':
            for b in range(8): put(bass,int((s0+b*beat/2)*SR),saw(cm[0]-12,.28,.16))
        else: put(bass,S,pluck(cm[0]-12,2.0,.18,1.5))
    # melodia
    step=beat/2;k=0;idx=4
    for j in range(int(dur/step)):
        pos=j*step;bi=int(pos//bar)%4;cm=[root+12+x for x in prog[bi]]
        strong=(j%8 in(0,4))
        pr={'bright':.5,'energetic':.35,'festive':.6,'warm':.4,'hopeful':.5,'celebration':.55}[style]
        if style=='warm' and j%2: continue
        if rng.random()<pr or j%8==0:
            if strong: m=int(rng.choice(cm))+(12 if rng.random()<.3 else 0)
            else:
                idx=int(np.clip(idx+rng.choice([-2,-1,1,2]),0,len(pent)-1));m=root+12+pent[idx]
            if style in('festive','warm','celebration'): put(mel,int(pos*SR),bell(m+ (12 if style=='warm' else 0),1.4,.11))
            elif style=='energetic': put(mel,int(pos*SR),saw(m,.22,.07))
            else: put(mel,int(pos*SR),pluck(m,.5,.13,6))
    # bateria
    for b in range(int(dur/beat)+1):
        s=int(b*beat*SR)
        if style=='warm': 
            if rng.random()<.25: put(fx,s,sleigh(rng,.025))
            continue
        if style=='energetic' or (style=='celebration' and True): put(drm,s,kick(.45 if style=='energetic' else .3))
        elif b%4 in(0,2) and (b>=8 or style!='hopeful'): put(drm,s,kick(.32))
        if b%4 in(1,3): put(drm,s,clap(rng,.11 if style=='energetic' else .08))
        put(drm,s+int(beat/2*SR),hat(rng,.06 if style=='energetic' else .04))
        if style=='festive':
            for q in range(4): put(fx,s+int(q*beat/4*SR),sleigh(rng,.035 if q%2==0 else .02))
    if style=='celebration':
        for pos in np.arange(2.5,dur-1.5,rng.uniform(2.2,3.2)):
            S=int(pos*SR);L=int(.5*SR);tt=np.arange(L)/SR;sw=0.05*np.sin(2*np.pi*np.cumsum(500+1400*tt/.5)/SR)*np.exp(-tt*3)
            put(fx,S,sw);L2=int(1.0*SR);tt2=np.arange(L2)/SR
            put(fx,S+L,.12*lp(rng.standard_normal(L2),10)*np.exp(-tt2*5))
            for _ in range(6): put(fx,S+L+int(rng.uniform(.05,.6)*SR),.05*hp(rng.standard_normal(int(.03*SR)),4)*np.exp(-np.arange(int(.03*SR))/SR*150))
    if style=='energetic':
        duck=np.ones(n);ph=(t%beat)/beat;duck=1-.65*np.exp(-ph*7)
        pad*=duck;bass*=duck
        for i in range(0,nb,4):
            S=int((i*bar+bar*3)*SR);L=int(bar*SR);tt=np.arange(L)/SR
            put(fx,S,.08*hp(rng.standard_normal(L),12)*(tt/(bar))**2)
    wet=reverb(pad+mel,SR,rng,sec=1.8,mix=.3 if style!='warm' else .45)
    mix=wet+bass+drm+fx
    fi={'warm':1.5}.get(style,.4)
    mix*=np.minimum(1,t/fi)*np.minimum(1,(dur-t)/1.5)
    mix=mix/np.max(np.abs(mix))*.85
    st=np.stack([mix,np.roll(mix,int(.012*SR))],1)
    w=wave.open(path,'wb');w.setnchannels(2);w.setsampwidth(2);w.setframerate(SR);w.writeframes((st*32767).astype('<i2').tobytes());w.close()
