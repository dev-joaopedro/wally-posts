"""Trilhas originais de 2027 (sintetizadas aqui, sem direitos autorais).
Estilos: piano, lofi, bossa, acoustic, synthwave, chill, tropical, house, funk, samba, forro.
Cada Reel usa gen(path, dur, style, seed) com a sua própria semente: o tom, o andamento,
a progressão de acordes, a melodia e os detalhes da percussão mudam de um para outro."""
import numpy as np, wave
from music2 import reverb, echo
SR=44100

def nf(m): return 440*2**((m-69)/12)
def lp(x,k): return np.convolve(x,np.ones(k)/k,'same') if k>1 else x
def hp(x,k): return x-lp(x,k)
def put(buf,s,sig):
    if s<0: sig=sig[-s:];s=0
    e=min(len(buf),s+len(sig))
    if s<len(buf) and e>s: buf[s:e]+=sig[:e-s]
def T(L): return np.arange(int(L*SR))/SR
def att(t,a): return np.minimum(1,t/a)

# ---------- instrumentos ----------
def piano(m,L=1.6,g=.16,bright=1.0):
    t=T(L);f=nf(m);y=0
    for k,a in enumerate((1,.55,.3,.18,.1,.06),1):
        fk=f*k*np.sqrt(1+.0004*k*k);y=y+a*bright**(k-1)*np.sin(2*np.pi*fk*t)*np.exp(-t*(1.6+.9*k))
    return g*y*att(t,.003)
def epiano(m,L=1.8,g=.14):
    t=T(L);f=nf(m);mod=np.sin(2*np.pi*f*t)*1.2*np.exp(-t*3)
    y=np.sin(2*np.pi*f*t+mod)+.25*np.sin(2*np.pi*2*f*t)*np.exp(-t*4)
    return g*y*np.exp(-t*1.4)*att(t,.004)*(1+.15*np.sin(2*np.pi*4.5*t))
def ks(m,L=1.2,g=.22,damp=.996,bright=.5,rng=None):
    """Karplus-Strong (cordas: violão, nylon)."""
    rng=rng or np.random.default_rng(int(m));P=max(2,int(SR/nf(m)));n=int(L*SR)
    y=np.zeros(n+P+1);y[:P]=lp(rng.uniform(-1,1,P),2 if bright>.4 else 4)
    for s in range(P,n+P,P):
        e=min(s+P,n+P+1);prev=y[s-P:e-P];prev2=y[s-P-1:e-P-1] if s-P-1>=0 else np.r_[0,prev[:-1]]
        if len(prev2)<len(prev): prev2=np.r_[prev2,np.zeros(len(prev)-len(prev2))]
        y[s:e]=damp*(bright*prev+(1-bright)*.5*(prev+prev2[:len(prev)]))
    y=y[:n];t=np.arange(n)/SR
    return g*y*np.minimum(1,(n-np.arange(n))/(.05*SR))*(1 if L<3 else np.exp(-t*.5))
def marimba(m,L=.7,g=.2):
    t=T(L);f=nf(m)
    return g*(np.sin(2*np.pi*f*t)*np.exp(-t*6)+.35*np.sin(2*np.pi*4*f*t)*np.exp(-t*22))*att(t,.002)
def pulse(m,L=.25,g=.08,w=.3,cut=4):
    t=T(L);ph=(nf(m)*t)%1;y=np.where(ph<w,1.,-1.)
    return g*lp(y,cut)*np.exp(-t*7)*att(t,.003)
def sawp(m,L,g=.1,cut=6,dec=1.5,det=.004):
    t=T(L);f=nf(m);y=0
    for d in(-det,0,det): y=y+2*((f*(1+d)*t)%1)-1
    return g*lp(y/3,cut)*np.exp(-t*dec)*att(t,.02)
def sub(m,L,g=.25,dec=3):
    t=T(L);return g*np.sin(2*np.pi*nf(m)*t)*np.exp(-t*dec)*att(t,.005)*np.minimum(1,(len(t)-np.arange(len(t)))/(.01*SR))
def slap(m,L=.3,g=.22):
    t=T(L);f=nf(m);y=np.sin(2*np.pi*f*t)+.5*np.sin(2*np.pi*2*f*t)*np.exp(-t*30)+.3*np.sin(2*np.pi*3*f*t)*np.exp(-t*40)
    return g*np.tanh(1.6*y)*np.exp(-t*8)*att(t,.002)
def clav(m,L=.18,g=.07):
    t=T(L);ph=(nf(m)*t)%1;y=np.where(ph<.15,1.,-1.)
    return g*hp(lp(y,3),40)*np.exp(-t*18)
def accordion(m,L,g=.07):
    t=T(L);f=nf(m);vib=1+.004*np.sin(2*np.pi*5.5*t)
    y=sum(np.sign(np.sin(2*np.pi*f*vib*(1+d)*t))*.5+ (2*((f*(1+d)*t)%1)-1)*.5 for d in(-.003,.003))
    return g*lp(y,7)*att(t,.03)*np.minimum(1,(len(t)-np.arange(len(t)))/(.03*SR))
def padv(ms,L,g=.035,kind='sine'):
    t=T(L);y=0
    for m in ms:
        f=nf(m)
        if kind=='saw': y=y+lp(2*((f*1.003*t)%1)-1,9)+lp(2*((f*.997*t)%1)-1,9)
        else: y=y+np.sin(2*np.pi*f*t)+.3*np.sin(2*np.pi*2*f*t)
    env=np.minimum(1,t/.4)*np.minimum(1,(len(t)-np.arange(len(t)))/(.5*SR))
    return g*y*env
# percussão
def kick(g=.5,f0=120,f1=45,dec=10):
    t=T(.3);f=(f0-f1)*np.exp(-t*22)+f1;return g*np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-t*dec)
def snare(rng,g=.12,tone=190):
    t=T(.2);return g*(.6*hp(rng.standard_normal(len(t)),4)*np.exp(-t*20)+.4*np.sin(2*np.pi*tone*t)*np.exp(-t*30))
def clap(rng,g=.1):
    t=T(.16);n=hp(rng.standard_normal(len(t)),6);env=np.exp(-t*24)
    for d in(.008,.016): env=env+.6*np.exp(-np.maximum(0,t-d)*120)*(t>=d)
    return g*n*env*.6
def hat(rng,g=.04,dec=80):
    t=T(.07);return g*hp(rng.standard_normal(len(t)),3)*np.exp(-t*dec)
def ohat(rng,g=.035): return hat(rng,g,18)
def shaker(rng,g=.03):
    t=T(.09);return g*hp(rng.standard_normal(len(t)),3)*np.sin(np.pi*np.minimum(1,t/.09))
def rim(g=.08):
    t=T(.05);return g*(np.sin(2*np.pi*1700*t)+.5*np.sin(2*np.pi*820*t))*np.exp(-t*90)
def surdo(g=.35):
    t=T(.5);f=70*np.exp(-t*4)+52;return g*np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-t*5)
def tamborim(rng,g=.07):
    t=T(.06);return g*(np.sin(2*np.pi*620*t)+.4*hp(rng.standard_normal(len(t)),3))*np.exp(-t*70)
def agogo(hi,g=.06):
    t=T(.35);f=920 if hi else 690;return g*(np.sin(2*np.pi*f*t)+.4*np.sin(2*np.pi*f*2.7*t))*np.exp(-t*9)
def zabumba(g=.3):
    t=T(.35);f=95*np.exp(-t*8)+60;return g*np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-t*7)
def triangle(g=.035,open_=True):
    t=T(.5 if open_ else .06);return g*(np.sin(2*np.pi*4200*t)+.6*np.sin(2*np.pi*6900*t)+.4*np.sin(2*np.pi*9800*t))*np.exp(-t*(5 if open_ else 60))
def crackle(n,rng,g=.012):
    y=np.zeros(n);idx=rng.integers(0,n,int(n/SR*18));y[idx]=rng.uniform(-1,1,len(idx))
    return g*lp(y,3)*8+g*.15*lp(rng.standard_normal(n),40)

# ---------- harmonia ----------
MAJ=[0,2,4,5,7,9,11];MIN=[0,2,3,5,7,8,10]
def chord(root,scale,deg,ext=3):
    """acorde por graus da escala; ext=3 tríade, 4 com sétima, 5 com nona"""
    return [root+scale[(deg+2*i)%7]+12*((deg+2*i)//7) for i in range(ext)]
PROGS={
 'maj':[[0,4,5,3],[0,5,3,4],[3,4,2,5],[0,3,4,4],[5,3,0,4],[0,2,3,4],[3,0,4,5],[0,4,3,3]],
 'min':[[0,5,2,6],[0,3,4,0],[0,6,5,6],[0,5,3,4],[0,2,5,4],[0,3,6,5]],
 'jazz':[[1,4,0,5],[0,5,1,4],[3,2,1,4],[0,3,1,4],[5,1,4,0]],
}
CFG={ # escala, família de progressões, bpm base, extensão do acorde
 'piano':('maj','maj',76,4),'lofi':('maj','jazz',78,5),'bossa':('maj','jazz',132,5),
 'acoustic':('maj','maj',96,3),'synthwave':('min','min',104,3),'chill':('maj','maj',88,4),
 'tropical':('maj','maj',104,3),'house':('min','min',122,4),'funk':('min','min',104,4),
 'samba':('maj','maj',100,3),'forro':('maj','maj',112,3),
}
KEYS=[0,5,10,3,8,1,6,11,4,9,2,7]

BPMOFF=[0,-5,4,-2,6,-6,2,-3,5,-1,3,-4]
def gen(path,dur,style,seed,variant=None):
    """variant = posição do Reel entre os do mesmo estilo (0,1,2…): garante tom, progressão e
    andamento diferentes dentro do estilo. Sem variant, deriva tudo da semente."""
    rng=np.random.default_rng(seed*7919+len(style));sc_name,fam,bpm0,ext=CFG[style]
    scale=MAJ if sc_name=='maj' else MIN;v=seed if variant is None else variant
    key=KEYS[(v*7+len(style))%12];root=48+key if key<7 else 36+key
    bpm=bpm0+BPMOFF[v%12];beat=60/bpm;bar=beat*4
    prog=PROGS[fam][v%len(PROGS[fam])]
    swing=.62 if style in('lofi','chill') else .5
    n=int(SR*dur);t=np.arange(n)/SR;nb=int(dur/bar)+2
    pads=np.zeros(n);harm=np.zeros(n);mel=np.zeros(n);bass=np.zeros(n);drm=np.zeros(n);fx=np.zeros(n)
    def at(pos): return int(pos*SR)
    def eighth(j): return j*beat/2+(beat*(swing-.5) if j%2 else 0)
    pent=[0,2,4,7,9] if sc_name=='maj' else [0,3,5,7,10]
    mscale=[p+12*o for o in(0,1,2) for p in pent]
    # ----- harmonia e baixo por compasso -----
    for i in range(nb):
        s0=i*bar;deg=prog[i%4];ch=chord(root,scale,deg,ext);bn=root+scale[deg%7]-12
        if bn<root-12: bn+=12
        intro=i==0
        if style=='piano':
            put(pads,at(s0),padv([c+12 for c in ch[:3]],bar+beat,.012))
            for b,(o,v) in enumerate([(0,1),(1,.7),(2,.85),(3,.7)]):
                put(harm,at(s0+b*beat),piano(ch[b%len(ch)]+12,1.8,.07*v))
            put(bass,at(s0),piano(bn,2.4,.07,.6))
        elif style=='lofi':
            put(harm,at(s0),sum(epiano(c+12,bar*1.1,.05) for c in ch))
            if not intro: put(harm,at(s0+eighth(5)),sum(epiano(c+12,.6,.025) for c in ch[1:]))
            put(bass,at(s0),sub(bn,beat*1.5,.13,2));put(bass,at(s0+eighth(5)),sub(bn+7,beat*.8,.1,3))
        elif style=='bossa':
            for j,on in enumerate([1,0,1,1,0,1,1,0]):  # batida de violão
                if on: put(harm,at(s0+j*beat/2),sum(ks(c+12,.45,.06,.993,.15,rng) for c in ch[1:]))
            put(bass,at(s0),ks(bn,beat*1.6,.26,.997,0,rng));put(bass,at(s0+2*beat),ks(bn+7,beat*1.6,.22,.997,0,rng))
        elif style=='acoustic':
            pat=[0,1,2,1,0,1,2,1] if seed%2 else [0,2,1,2,0,2,1,2]
            for j,p in enumerate(pat): put(harm,at(s0+j*beat/2),ks(ch[p]+12,1.0,.13,.996,.12,rng))
            put(bass,at(s0),ks(bn,bar,.22,.998,0,rng));put(bass,at(s0+2*beat),ks(bn+7,beat*1.8,.15,.997,0,rng))
        elif style=='synthwave':
            put(pads,at(s0),padv([c+12 for c in ch],bar+beat,.03,'saw'))
            arp=[ch[0],ch[1],ch[2],ch[1]+12,ch[2],ch[1],ch[0]+12,ch[2]]
            if not intro:
                for j in range(16): put(harm,at(s0+j*beat/4),pulse(arp[j%8]+12,.18,.05,.25+.1*(seed%3)))
            for j in range(8): put(bass,at(s0+j*beat/2),sawp(bn,beat*.45,.09,5,6))
        elif style=='chill':
            put(pads,at(s0),padv([c+12 for c in ch],bar+beat*2,.025))
            put(harm,at(s0),sum(epiano(c+12,bar,.04) for c in ch));put(harm,at(s0+beat*2.5),sum(epiano(c+24,.8,.02) for c in ch[1:3]))
            put(bass,at(s0),sub(bn,bar*.9,.11,1))
        elif style=='tropical':
            put(pads,at(s0),padv([c+12 for c in ch],bar+beat,.018))
            for j,on in enumerate([1,0,0,1,0,0,1,0]):
                if on: put(harm,at(s0+j*beat/2),sum(marimba(c+24,.5,.07) for c in ch))
            for j in(0,3,6): put(bass,at(s0+j*beat/2),sub(bn,beat*.9,.15,4))
        elif style=='house':
            if not intro:
                for j in range(4): put(harm,at(s0+j*beat+beat/2),sum(sawp(c+12,beat*.35,.06,4,8) for c in ch))
            put(pads,at(s0),padv([c+12 for c in ch],bar+beat,.012,'saw'))
            for j in range(4): put(bass,at(s0+j*beat+beat/2),sub(bn,beat*.45,.16,5))
        elif style=='funk':
            for j in range(16):
                if rng.random()<.55 or j%4==2: put(harm,at(s0+j*beat/4),sum(clav(c+12,.12,.09) for c in ch[:3]))
            for j,(o,dn) in enumerate([(0,0),(3,0),(6,12),(8,0),(10,7),(14,12)]): put(bass,at(s0+o*beat/4),slap(bn+12+dn,.25,.12))
        elif style=='samba':
            for j in range(8):
                if j in(0,3,5,6): put(harm,at(s0+j*beat/2),sum(ks(c+12,.3,.05,.99,.3,rng) for c in ch))  # cavaquinho
            put(bass,at(s0),ks(bn,beat,.25,.996,0,rng));put(bass,at(s0+beat*1.5),ks(bn+7,beat,.2,.996,0,rng))
            put(bass,at(s0+beat*2),ks(bn,beat,.25,.996,0,rng));put(bass,at(s0+beat*3.5),ks(bn+7,beat,.2,.996,0,rng))
        elif style=='forro':
            put(harm,at(s0),accordion(ch[0]+12,beat*.9,.09));put(harm,at(s0+beat*2),accordion(ch[1]+12,beat*.9,.07))
            put(pads,at(s0),sum(accordion(c+12,bar*.95,.02) for c in ch))
            put(bass,at(s0),sub(bn,beat*.9,.14,3));put(bass,at(s0+beat*1.5),sub(bn+7,beat*.5,.11,4));put(bass,at(s0+beat*2),sub(bn,beat*.9,.14,3))
    # ----- melodia -----
    if style not in('house',) or True:
        lead={'piano':lambda m,L:piano(m,1.2,.08),'lofi':lambda m,L:epiano(m,.9,.05),'bossa':lambda m,L:ks(m,.7,.12,.995,.15,rng),
              'acoustic':lambda m,L:ks(m,.8,.12,.996,.2,rng),'synthwave':lambda m,L:sawp(m,L,.06,4,2.5,.006),
              'chill':lambda m,L:marimba(m,.8,.07)+epiano(m,.8,.03),'tropical':lambda m,L:marimba(m,.6,.1),
              'house':lambda m,L:piano(m,.6,.1,1.3),'funk':lambda m,L:sawp(m,L*.8,.05,3,5),'samba':lambda m,L:ks(m,.35,.09,.99,.3,rng),
              'forro':lambda m,L:accordion(m,L*.9,.05)}[style]
        dens={'piano':.45,'lofi':.4,'bossa':.5,'acoustic':.4,'synthwave':.55,'chill':.35,'tropical':.55,'house':.3,'funk':.4,'samba':.55,'forro':.6}[style]
        idx=int(rng.integers(3,7));motif=[int(x) for x in rng.choice([-2,-1,1,2,0],8)]
        start=1 if style in('house','synthwave','lofi') else 0
        for j in range(int(dur/(beat/2))):
            pos=eighth(j);b=int(pos//bar)
            if b<start: continue
            if pos>dur-1.2: break
            hit=(rng.random()<dens) or j%8==0
            if b%2==1 and j%8<4: hit=hit and rng.random()<.6  # pergunta/resposta
            if not hit: continue
            if j%8==0:
                ch=chord(root,scale,prog[b%4],3);m=ch[int(rng.integers(0,3))]+12
            else:
                idx=int(np.clip(idx+motif[j%8]+(rng.integers(-1,2) if rng.random()<.3 else 0),0,len(mscale)-1));m=root+12+mscale[idx]
            L=beat*(1 if rng.random()<.3 else .5);put(mel,at(pos),lead(m,L))
    # ----- bateria -----
    nbeats=int(dur/beat)+1
    for b in range(nbeats):
        s=b*beat;bb=b%4;intro=b<4
        if style=='piano':
            if b>=8 and bb in(0,2): put(drm,at(s),kick(.18,90,45,12))
            if b>=8 and bb in(1,3): put(drm,at(s),rim(.05))
        elif style=='lofi':
            if bb==0 or (bb==2 and rng.random()<.6): put(drm,at(s),kick(.4,100,48,9))
            if bb in(1,3): put(drm,at(s),snare(rng,.08,180))
            put(drm,at(s),hat(rng,.025));put(drm,at(s+beat*swing),hat(rng,.02))
        elif style=='bossa':
            if bb in(0,2): put(drm,at(s),kick(.22,80,45,12))
            for k,o in enumerate([0,.75,1.5,2.5,3.25] if bb==0 else []): put(drm,at(s+o*beat),rim(.05))
            put(drm,at(s),shaker(rng,.02));put(drm,at(s+beat/2),shaker(rng,.025))
        elif style=='acoustic':
            if not intro:
                if bb in(0,2): put(drm,at(s),kick(.25,100,48,10))
                if bb in(1,3): put(drm,at(s),clap(rng,.07))
            put(drm,at(s+beat/2),shaker(rng,.025))
        elif style=='synthwave':
            if not intro or bb==0: put(drm,at(s),kick(.3,130,46,9))
            if bb in(1,3) and not intro:
                sn=snare(rng,.13,200);put(drm,at(s),sn);put(fx,at(s),reverb(np.r_[sn,np.zeros(int(.3*SR))],SR,rng,.6,.9)[:int(.5*SR)]*.5)
            put(drm,at(s+beat/2),hat(rng,.03))
        elif style=='chill':
            if b>=4 and bb==0: put(drm,at(s),kick(.3,95,46,9))
            if b>=4 and bb==2 and rng.random()<.5: put(drm,at(s+beat/2),kick(.22,95,46,10))
            if bb==2 and b>=4: put(drm,at(s),clap(rng,.05))
            put(drm,at(s+beat*swing),hat(rng,.035))
        elif style=='tropical':
            put(drm,at(s),kick(.24,110,46,10))
            if bb in(1,3) and not intro: put(drm,at(s+beat*.75),snare(rng,.06,240));put(drm,at(s),snare(rng,.08,240))
            for q in range(4): put(drm,at(s+q*beat/4),shaker(rng,.018 if q%2 else .028))
        elif style=='house':
            put(drm,at(s),kick(.3,140,48,8))
            if bb in(1,3) and not intro: put(drm,at(s),clap(rng,.1))
            put(drm,at(s+beat/2),ohat(rng,.03))
            if not intro: put(drm,at(s+beat/4),hat(rng,.015));put(drm,at(s+3*beat/4),hat(rng,.015))
        elif style=='funk':
            if bb==0: put(drm,at(s),kick(.28,110,46,10))
            if bb==2: put(drm,at(s+beat*.5),kick(.25,110,46,10))
            if bb in(1,3): put(drm,at(s),snare(rng,.12,210))
            for q in range(4): put(drm,at(s+q*beat/4),hat(rng,.03 if q%2==0 else .018))
        elif style=='samba':
            put(drm,at(s),surdo(.19 if bb in(1,3) else .11))
            for q,on in enumerate([1,0,1,1]):
                if on: put(drm,at(s+q*beat/4),tamborim(rng,.05))
            for q in range(4): put(drm,at(s+q*beat/4),shaker(rng,.02))
            if bb==0: put(drm,at(s),agogo(True));put(drm,at(s+beat*.5),agogo(False))
        elif style=='forro':
            if bb in(0,2): put(drm,at(s),zabumba(.19))
            if bb in(1,3): put(drm,at(s+beat*.5),zabumba(.12))
            put(drm,at(s),triangle(.025,False));put(drm,at(s+beat/2),triangle(.03,True))
    # ----- mixagem -----
    wetamt={'piano':.35,'lofi':.25,'bossa':.25,'acoustic':.25,'synthwave':.35,'chill':.4,'tropical':.25,'house':.2,'funk':.15,'samba':.15,'forro':.15}[style]
    melfx=echo(mel,SR,beat*.75,.3,3) if style in('synthwave','chill','house') else mel
    wet=reverb(pads+harm+melfx,SR,rng,sec=1.6,mix=wetamt)
    mix=wet+bass+drm+fx
    if style=='lofi':
        mix=lp(mix,3)+crackle(n,rng)
    if style=='house':
        ph=(t%beat)/beat;mix=mix-(1-(1-.5*np.exp(-ph*8)))*(wet+bass)
    mix=mix*np.minimum(1,t/.5)*np.minimum(1,(dur-t)/1.5)
    mix=np.tanh(mix/np.max(np.abs(mix))*1.2)
    mix=mix/np.max(np.abs(mix))*.88
    d=int(.011*SR);st=np.stack([mix,np.r_[np.zeros(d),mix[:-d]]*.92+mix*.08],1)
    w=wave.open(path,'wb');w.setnchannels(2);w.setsampwidth(2);w.setframerate(SR);w.writeframes((st*32767).astype('<i2').tobytes());w.close()

if __name__=='__main__':
    import sys;gen(sys.argv[1],float(sys.argv[2]),sys.argv[3],int(sys.argv[4]))
