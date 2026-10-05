"""Os Reels de outubro/2026 que usam o motor (engine.html). Ter/qui às 19h."""
P1=[[57,60,64,67],[53,57,60,64],[48,52,55,59],[55,59,62,65]]
P2=[[52,55,59,62],[57,60,64,67],[50,53,57,60],[55,59,62,66]]
P3=[[60,64,67,71],[57,60,64,67],[53,57,60,64],[55,59,62,65]]
SPECS=[
 dict(id="r02-telegram",seed=2,bpm=88,prog=P2,scenes=[
  dict(type="hook",tag="Telegram",title="Anotar um gasto leva <em>5 segundos.</em>",sub="Sem planilha. Sem abrir app.",dur=3.4),
  dict(type="chat",title="É só mandar uma mensagem",msgs=[
   dict(u="/despesa 32 Almoço"),dict(card=dict(icon="🍽️",name="Almoço",cat="Alimentação · Hoje",amt="32,00",inc=False)),
   dict(u="/receita 150 Freela"),dict(card=dict(icon="🏷️",name="Freela",cat="Outras receitas · Hoje",amt="150,00",inc=True)),
   dict(u="/saldo"),dict(sum=[["Receitas","R$ 3.900,00"],["Despesas","R$ 1.845,20"],["Saldo do mês","R$ 2.054,80","tot"]])]),
  dict(type="outro",title="Seu dinheiro, <em style='font-style:normal;color:#93AEF0'>no Telegram.</em>")]),
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
  dict(type="hook",tag="É falta de visão",title="Registrar leva <em>5 segundos</em> no Telegram.",size="m",dur=3.6),
  dict(type="outro",title="Comece hoje no <em style='font-style:normal;color:#93AEF0'>Wally.</em>")]),
 dict(id="r07-checklist",seed=6,bpm=86,prog=P1,scenes=[
  dict(type="hook",tag="Fim de mês",title="Checklist para <em>fechar o mês.</em>",dur=3.2),
  dict(type="items",tag="Checklist",title="4 passos rápidos:",items=[["Confira os lançamentos","Nada ficou de fora?"],["Compare com o planejado","O que passou do limite?"],["Separe a reserva","Antes de gastar o resto"],["Defina as metas","Do próximo mês"]]),
  dict(type="outro",title="Tudo isso no <em style='font-style:normal;color:#93AEF0'>Wally.</em>")]),
 dict(id="r08-mito-anotar",seed=7,bpm=90,prog=P3,scenes=[
  dict(type="hook",tag="Mito ou verdade?",title="Anotar gastos <em>dá trabalho?</em>",dur=3.0),
  dict(type="myth",myth="Anotar gastos é chato e demora.",truth="No Wally é só mandar uma mensagem no Telegram.",sub="Texto livre, sem formulário. Leva uns 5 segundos.",strikeAt=2.4),
  dict(type="outro",title="Teste grátis. <em style='font-style:normal;color:#93AEF0'>Link na bio.</em>",sub="Controle total, web e Telegram.")]),
]
