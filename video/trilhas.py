"""Estilo de trilha de cada Reel (por época/tema). Usado por remux e pelo render_engine."""
STYLE={}
for r in ["r01-50-30-20","r02-telegram","r03-mito-reserva","r04-painel","r05-gastos-invisiveis","r06-pergunta","r07-checklist","r08-mito-anotar","r09-mito-poupar","r10-texto-livre","r11-antes-comprar","r12-mito-cartao","r13-quanto-gastar","r14-assinaturas"]: STYLE[r]="bright"
for r in ["r15-black-friday","r16-mito-bf"]: STYLE[r]="energetic"
for r in ["r17-dezembro","r18-treze","r19-mito-dezembro","r21-presentes","r22-presente-chat"]: STYLE[r]="festive"
for r in ["r20-balanco","r23-meta-2027","r25-metas-2027"]: STYLE[r]="hopeful"
STYLE["r24-natal"]="warm";STYLE["r26-reveillon"]="celebration"
