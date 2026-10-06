"""Os Reels de outubro/2026 que usam o motor (engine.html). Ter/qui às 19h."""
P1=[[57,60,64,67],[53,57,60,64],[48,52,55,59],[55,59,62,65]]
P2=[[52,55,59,62],[57,60,64,67],[50,53,57,60],[55,59,62,66]]
P3=[[60,64,67,71],[57,60,64,67],[53,57,60,64],[55,59,62,65]]
SPECS=[
 dict(id="r02-telegram",seed=2,bpm=88,prog=P2,scenes=[
  dict(type="hook",tag="WhatsApp",title="Anotar um gasto leva <em>5 segundos.</em>",sub="Sem planilha. Sem abrir app.",dur=3.4),
  dict(type="chat",title="É só mandar uma mensagem",msgs=[
   dict(u="/despesa 32 Almoço"),dict(card=dict(icon="🍽️",name="Almoço",cat="Alimentação · Hoje",amt="32,00",inc=False)),
   dict(u="/receita 150 Freela"),dict(card=dict(icon="🏷️",name="Freela",cat="Outras receitas · Hoje",amt="150,00",inc=True)),
   dict(u="/saldo"),dict(sum=[["Receitas","R$ 3.900,00"],["Despesas","R$ 1.845,20"],["Saldo do mês","R$ 2.054,80","tot"]])]),
  dict(type="outro",title="Seu dinheiro, <em style='font-style:normal;color:#93AEF0'>no WhatsApp.</em>")]),
 dict(id="r03-mito-reserva",seed=3,bpm=80,prog=P1,scenes=[
  dict(type="hook",tag="Mito ou verdade?",title="Reserva de emergência é <em>luxo?</em>",dur=3.0),
  dict(type="myth",myth="Reserva de emergência é só para quem ganha bem.",truth="Quem ganha menos sofre mais com imprevistos.",sub="Comece pequeno: qualquer valor por mês já conta.",strikeAt=2.6),
  dict(type="outro",title="Defina sua meta no <em style='font-style:normal;color:#93AEF0'>Wally.</em>")]),
 dict(id="r05-gastos-invisiveis",seed=4,bpm=84,prog=P3,scenes=[
  dict(type="hook",tag="Atenção",title="3 gastos que você <em>nem percebe.</em>",dur=3.2),
  dict(type="items",tag="Gastos invisíveis",title="Olhe com atenção para:",items=[["Assinaturas esquecidas","Streaming, apps e planos que você não usa mais"],["Taxas e tarifas","Anuidade, tarifa de conta e juros que passam batido"],["Pequenos extras","Delivery, café e compras por impulso"]]),
  dict(type="outro",title="Registre tudo e <em style='font-style:normal;color:#93AEF0'>enxergue.</em>")]),
 dict(id="r06-pergunta",seed=5,bpm=78,prog=P2,scenes=[
  dict(type="hook",tag="Teste rápido",title="Quanto você gastou <em>ontem?</em>",dur=3.6),
  dict(type="hook",tag="Se não sabe…",title="o problema quase nunca é <em>falta de dinheiro.</em>",size="m",dur=3.8),
  dict(type="hook",tag="É falta de visão",title="Registrar leva <em>5 segundos</em> no WhatsApp.",size="m",dur=3.6),
  dict(type="outro",title="Comece hoje no <em style='font-style:normal;color:#93AEF0'>Wally.</em>")]),
 dict(id="r07-checklist",seed=6,bpm=86,prog=P1,scenes=[
  dict(type="hook",tag="Fim de mês",title="Checklist para <em>fechar o mês.</em>",dur=3.2),
  dict(type="items",tag="Checklist",title="4 passos rápidos:",items=[["Confira os lançamentos","Nada ficou de fora?"],["Compare com o planejado","O que passou do limite?"],["Separe a reserva","Antes de gastar o resto"],["Defina as metas","Do próximo mês"]]),
  dict(type="outro",title="Tudo isso no <em style='font-style:normal;color:#93AEF0'>Wally.</em>")]),
 dict(id="r08-mito-anotar",seed=7,bpm=90,prog=P3,scenes=[
  dict(type="hook",tag="Mito ou verdade?",title="Anotar gastos <em>dá trabalho?</em>",dur=3.0),
  dict(type="myth",myth="Anotar gastos é chato e demora.",truth="No Wally é só mandar uma mensagem no WhatsApp.",sub="Texto livre, sem formulário. Leva uns 5 segundos.",strikeAt=2.4),
  dict(type="outro",title="Teste grátis. <em style='font-style:normal;color:#93AEF0'>Link na bio.</em>",sub="Controle total, web e WhatsApp.")]),
]

# ---------- Novembro e dezembro/2026 ----------
def O(t,sub=None): 
    d=dict(type="outro",title=t)
    if sub: d["sub"]=sub
    return d
EM=lambda x:f"<em style='font-style:normal;color:#93AEF0'>{x}</em>"
SPECS2=[
 dict(id="r09-mito-poupar",d="2026-11-03",seed=9,bpm=70,scenes=[
  dict(type="hook",tag="Mito ou verdade?",title="Preciso ganhar mais para <em>poupar?</em>",dur=3.2),
  dict(type="myth",myth="Só consigo poupar quando ganhar mais.",truth="Poupar é hábito antes de ser valor.",sub="Comece com o que couber e aumente com o tempo.",strikeAt=2.4),
  O("Defina sua meta no "+EM("Wally."))]),
 dict(id="r10-texto-livre",d="2026-11-05",seed=10,bpm=74,scenes=[
  dict(type="hook",tag="WhatsApp",title="Escreva do jeito que <em>você fala.</em>",dur=3.2),
  dict(type="chat",title="O Wally entende",msgs=[dict(u="Padaria 37"),
   dict(bot="<b>Entendi! Confirme o lançamento:</b><br>📝 Descrição: Padaria<br>💰 Valor: R$ 37,00<br>🗂️ Categoria: Alimentação<br>🔴 Tipo: Despesa<br>Está correto?",t=2.4),
   dict(btns=["✅ Confirmar","❌ Cancelar"]),dict(bot="✅ <b>Lançamento confirmado!</b><br>Padaria — R$ 37,00",t=1.8)]),
  O("Seu dinheiro, "+EM("no WhatsApp."))]),
 dict(id="r11-antes-comprar",d="2026-11-10",seed=11,bpm=68,scenes=[
  dict(type="hook",tag="Antes de comprar",title="3 perguntas para <em>fazer antes.</em>",dur=3.2),
  dict(type="items",tag="Compra consciente",title="Pergunte-se:",items=[["Eu preciso disso?","Ou só estou com vontade agora?"],["Cabe no orçamento?","Sem apertar o resto do mês"],["Compraria daqui a 30 dias?","Se sim, a decisão é mais segura"]]),
  O("Registre e "+EM("acompanhe."))]),
 dict(id="r12-mito-cartao",d="2026-11-12",seed=12,bpm=76,scenes=[
  dict(type="hook",tag="Mito ou verdade?",title="Cartão de crédito é <em>vilão?</em>",dur=3.0),
  dict(type="myth",myth="Cartão de crédito sempre leva à dívida.",truth="O problema é gastar sem acompanhar a fatura.",sub="Com controle, ele pode ajudar.",strikeAt=2.4),
  O("Acompanhe suas faturas no "+EM("Wally."))]),
 dict(id="r13-quanto-gastar",d="2026-11-17",seed=13,bpm=72,scenes=[
  dict(type="hook",tag="Dica prática",title="Quanto posso gastar <em>por dia?</em>",dur=3.2),
  dict(type="items",tag="Limite diário",title="Em 3 passos:",items=[["Veja o que sobrou no mês","Exemplo: R$ 680 disponíveis"],["Divida pelos dias restantes","4 dias: R$ 170 por dia"],["Fique dentro do limite","Simples e sem planilha"]]),
  O("O Wally "+EM("calcula pra você."))]),
 dict(id="r14-assinaturas",d="2026-11-19",seed=14,bpm=66,scenes=[
  dict(type="hook",tag="Teste rápido",title="Você sabe quanto paga em <em>assinaturas?</em>",size="m",dur=3.8),
  dict(type="hook",tag="Pense bem",title="Muita gente <em>esquece</em> alguma.",size="m",dur=3.4),
  dict(type="hook",tag="Revise hoje",title="Liste, some e cancele o que <em>não usa.</em>",size="m",dur=3.8),
  O("Veja tudo no "+EM("Wally."))]),
 dict(id="r15-black-friday",d="2026-11-24",seed=15,bpm=74,scenes=[
  dict(type="hook",tag="Black Friday",title="4 cuidados antes de <em>comprar.</em>",dur=3.2),
  dict(type="items",tag="Black Friday",title="Antes de clicar:",items=[["Defina um teto","Antes de ver as ofertas"],["Liste o que precisa","Foque no que já estava nos planos"],["Compare o preço de antes","Nem toda promoção é desconto"],["Cuide do parcelamento","Parcelas somam no mês"]]),
  O("Controle o gasto no "+EM("Wally."))]),
 dict(id="r16-mito-bf",d="2026-11-26",seed=16,bpm=70,scenes=[
  dict(type="hook",tag="Mito ou verdade?",title="Black Friday tem o <em>menor preço?</em>",size="m",dur=3.2),
  dict(type="myth",myth="Black Friday sempre tem o menor preço do ano.",truth="Nem toda promoção é desconto real.",sub="Compare o histórico de preços antes de comprar.",strikeAt=2.6),
  O("Compre com "+EM("planejamento."))]),
 dict(id="r17-dezembro",d="2026-12-01",seed=17,bpm=72,scenes=[
  dict(type="hook",tag="Dezembro",title="Fim de ano pesa no <em>bolso.</em>",dur=3.2),
  dict(type="items",tag="Planeje agora",title="3 pontos de atenção:",items=[["Presentes","Defina um limite por pessoa"],["Festas e viagens","Reserve o valor antes"],["13º salário","Decida o destino antes de gastar"]]),
  O("Planeje no "+EM("Wally."))]),
 dict(id="r18-treze",d="2026-12-03",seed=18,bpm=76,scenes=[
  dict(type="hook",tag="WhatsApp",title="Chegou o <em>13º?</em> Registre.",dur=3.2),
  dict(type="chat",title="Leva 5 segundos",msgs=[dict(u="/receita 2500 13º salário"),dict(card=dict(icon="💰",name="13º salário",cat="Salário · Hoje",amt="2.500,00",inc=True)),dict(u="/saldo"),dict(sum=[["Receitas","R$ 6.400,00"],["Despesas","R$ 1.845,20"],["Saldo do mês","R$ 4.554,80","tot"]])]),
  O("Seu dinheiro, "+EM("no WhatsApp."))]),
 dict(id="r19-mito-dezembro",d="2026-12-08",seed=19,bpm=68,scenes=[
  dict(type="hook",tag="Mito ou verdade?",title="Dezembro não conta no <em>orçamento?</em>",size="m",dur=3.4),
  dict(type="myth",myth="Em dezembro posso gastar sem controle.",truth="Muita conta chega junto em janeiro.",sub="Quem registra em dezembro começa o ano mais tranquilo.",strikeAt=2.4),
  O("Registre tudo no "+EM("Wally."))]),
 dict(id="r20-balanco",d="2026-12-10",seed=20,bpm=72,scenes=[
  dict(type="hook",tag="Balanço do ano",title="3 perguntas sobre seu <em>ano.</em>",dur=3.2),
  dict(type="items",tag="Balanço",title="Responda:",items=[["Quanto entrou?","Some todas as receitas do ano"],["Quanto saiu?","Veja para onde foi o dinheiro"],["Quanto sobrou?","Esse é o ponto de partida de 2027"]]),
  O("Veja o ano no "+EM("Wally."))]),
 dict(id="r21-presentes",d="2026-12-15",seed=21,bpm=74,scenes=[
  dict(type="hook",tag="Presentes",title="Presente que <em>cabe no bolso.</em>",dur=3.2),
  dict(type="items",tag="Natal sem susto",title="3 passos:",items=[["Liste quem vai ganhar","Sem esquecer ninguém"],["Defina um valor máximo","Por pessoa e no total"],["Anote cada compra","Para não estourar o limite"]]),
  O("Controle no "+EM("Wally."))]),
 dict(id="r22-presente-chat",d="2026-12-17",seed=22,bpm=70,scenes=[
  dict(type="hook",tag="WhatsApp",title="Comprou um presente? <em>Anote.</em>",size="m",dur=3.4),
  dict(type="chat",title="Registre na hora",msgs=[dict(u="/despesa 80 Presente Ana"),dict(card=dict(icon="🎁",name="Presente Ana",cat="Compras · Hoje",amt="80,00",inc=False)),dict(u="/despesa 120 Presente Pedro"),dict(card=dict(icon="🎁",name="Presente Pedro",cat="Compras · Hoje",amt="120,00",inc=False))]),
  O("Seu dinheiro, "+EM("no WhatsApp."))]),
 dict(id="r23-meta-2027",d="2026-12-22",seed=23,bpm=66,scenes=[
  dict(type="hook",tag="Pense em 2027",title="Qual é a sua <em>meta financeira?</em>",size="m",dur=3.8),
  dict(type="hook",tag="Dica",title="Uma meta boa tem <em>valor e prazo.</em>",size="m",dur=3.6),
  O("Crie a sua no "+EM("Wally."))]),
 dict(id="r24-natal",d="2026-12-24",seed=24,bpm=64,scenes=[
  dict(type="hook",tag="Feliz Natal",title="Que 2027 seja o ano da sua <em>organização.</em>",size="m",sub="Equipe Wally",dur=4.6),
  O("Boas festas, "+EM("com tranquilidade."),"Link na bio.")]),
 dict(id="r25-metas-2027",d="2026-12-29",seed=25,bpm=74,scenes=[
  dict(type="hook",tag="Metas 2027",title="3 passos para <em>sair do papel.</em>",dur=3.2),
  dict(type="items",tag="Metas",title="Para cada meta:",items=[["Escolha uma meta clara","Uma de cada vez"],["Defina valor e prazo","Quanto e até quando"],["Acompanhe todo mês","Ajuste o que for preciso"]]),
  O("Acompanhe no "+EM("Wally."))]),
 dict(id="r26-reveillon",d="2026-12-31",seed=26,bpm=68,scenes=[
  dict(type="hook",tag="Réveillon",title="O melhor presente para 2027:",size="m",dur=3.0),
  dict(type="hook",tag="Comece o ano",title="um orçamento que você <em>acompanha.</em>",size="m",dur=3.8),
  O("Feliz ano novo "+EM("com o Wally."),"Crie sua conta grátis. Link na bio.")]),
]
