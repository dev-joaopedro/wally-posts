"""Reels de janeiro a setembro/2027 (motor engine.html). Ter/qui às 19h.
Cada item: id, data, estilo da trilha (music4.py) e cenas; a legenda é montada por caption().
Trilha: cada Reel tem a sua (estilo + semente própria), diferente das de 2026."""
EM=lambda x:f"<em style='font-style:normal;color:#93AEF0'>{x}</em>"
def H(tag,title,sub=None,size=None,dur=None,cls=None):
    d=dict(type="hook",tag=tag,title=title)
    if sub:d["sub"]=sub
    if size:d["size"]=size
    if dur:d["dur"]=dur
    if cls:d["cls"]=cls
    return d
def M(myth,truth,sub=None,at=2.5):
    d=dict(type="myth",myth=myth,truth=truth,strikeAt=at)
    if sub:d["sub"]=sub
    return d
def I(tag,title,items):return dict(type="items",tag=tag,title=title,items=items)
def C(title,msgs,tag="WhatsApp"):return dict(type="chat",tag=tag,title=title,msgs=msgs)
def U(t):return dict(u=t)
def K(icon,name,cat,amt,inc=False):return dict(card=dict(icon=icon,name=name,cat=cat,amt=amt,inc=inc))
def S(rec,desp,saldo):return dict(sum=[["Receitas",rec],["Despesas",desp],["Saldo do mês",saldo,"tot"]])
def B(html,t=2.2):return dict(bot=html,t=t)
def O(t,sub=None):
    d=dict(type="outro",title=t)
    if sub:d["sub"]=sub
    return d
BASE="#wally #financaspessoais #educacaofinanceira"
CTA="👉 Crie sua conta grátis: link na bio."
def R(id,d,style,scenes,body,tags,save=None,cta=CTA):
    cap=body.strip()+"\n\n"+((save+"\n") if save else "")+cta+"\n\n"+tags+" "+BASE
    return dict(id=id,d=d,style=style,scenes=scenes,caption=cap)
CONF=lambda desc,val,cat:B(f"<b>Entendi! Confirme o lançamento:</b><br>📝 Descrição: {desc}<br>💰 Valor: R$ {val}<br>🗂️ Categoria: {cat}<br>🔴 Tipo: Despesa<br>Está correto?",2.4)
OK=lambda desc,val:B(f"✅ <b>Lançamento confirmado!</b><br>{desc} — R$ {val}",1.8)
BT=dict(btns=["✅ Confirmar","❌ Cancelar"])

SPECS=[
# ---------------- Janeiro ----------------
R("r27-janeiro-contas","2027-01-05","piano",[
  H("Janeiro","O mês das <em>contas extras.</em>"),
  I("Prepare-se","Chegam juntas:",[["IPVA e IPTU","Veja se compensa pagar à vista"],["Material escolar","Liste antes de ir à loja"],["Fatura das festas","Some o que passou no cartão"]]),
  O("Organize janeiro no "+EM("Wally."))],
 "Janeiro chega com as contas extras. 📋\n\n• IPVA e IPTU: veja se compensa pagar à vista\n• Material escolar: faça a lista antes de sair\n• Fatura das festas: some tudo o que foi no cartão\n\nSaber o total evita susto no meio do mês.",
 "#janeiro #ipva #iptu","💾 Salve para não esquecer."),
R("r28-mito-ano-novo","2027-01-07","lofi",[
  H("Mito ou verdade?","Ano novo, <em>vida financeira nova?</em>",size="m"),
  M("Virar o ano resolve minhas finanças.","O que muda é o hábito, não o calendário.","Comece registrando o que você gasta."),
  O("Comece hoje no "+EM("Wally."))],
 "Mito: virar o ano resolve a vida financeira. ❌\n\nVerdade: o que muda é o hábito, não o calendário. O primeiro passo é saber para onde o dinheiro vai.",
 "#anonovo #habitosfinanceiros #organizacaofinanceira"),
R("r29-primeiro-registro","2027-01-12","bossa",[
  H("WhatsApp","Seu primeiro gasto de <em>2027.</em>"),
  C("Registre em segundos",[U("/despesa 18 Café da manhã"),K("☕","Café da manhã","Alimentação · Hoje","18,00"),U("/despesa 6 Ônibus"),K("🚌","Ônibus","Transporte · Hoje","6,00")]),
  O("Seu dinheiro, "+EM("no WhatsApp."))],
 "O primeiro gasto de 2027 já pode ir pro controle. ☕\n\nÉ só mandar no WhatsApp:\n/despesa 18 Café da manhã\n/despesa 6 Ônibus\n\nSem planilha, sem abrir app.",
 "#whatsapp #controlefinanceiro #appdefinancas"),
R("r30-ipva","2027-01-14","synthwave",[
  H("IPVA","À vista ou <em>parcelado?</em>"),
  I("Antes de decidir","Compare:",[["Desconto à vista","Quanto você economiza de fato"],["Sua reserva","Pagar à vista não pode zerar ela"],["Parcelas no mês","Cabem junto com as outras contas?"]]),
  O("Planeje no "+EM("Wally."))],
 "IPVA: à vista ou parcelado? 🚗\n\n• Veja quanto o desconto à vista economiza de fato\n• Não zere a reserva para pagar à vista\n• Se parcelar, confira se as parcelas cabem no mês\n\nA melhor escolha é a que não aperta o resto do orçamento.",
 "#ipva #carro #orcamento","💾 Salve para decidir com calma."),
R("r31-material-escolar","2027-01-19","acoustic",[
  H("Volta às aulas","Material escolar <em>sem susto.</em>"),
  I("Economize","4 passos:",[["Veja o que sobrou","Do ano passado"],["Faça a lista","E siga ela na loja"],["Pesquise preços","Em mais de um lugar"],["Defina um teto","Antes de começar"]]),
  O("Anote cada compra no "+EM("Wally."))],
 "Material escolar sem susto. ✏️\n\n1. Veja o que sobrou do ano passado\n2. Faça a lista e siga ela na loja\n3. Pesquise em mais de um lugar\n4. Defina um teto antes de começar",
 "#voltasaulas #materialescolar #economizar","💾 Salve e mande para quem precisa."),
R("r32-fatura-dezembro","2027-01-21","chill",[
  H("Teste rápido","Você sabe quanto foi a <em>fatura de dezembro?</em>",size="m",dur=3.8),
  H("Se não sabe…","janeiro vai <em>ensinar.</em>",size="m",dur=3.2),
  H("Para fevereiro","Acompanhe a fatura <em>durante o mês.</em>",size="m",dur=3.6),
  O("Acompanhe no "+EM("Wally."))],
 "Você sabe quanto foi a fatura de dezembro? 💳\n\nQuem acompanha a fatura durante o mês não leva susto quando ela chega.",
 "#cartaodecredito #fatura #controledegastos"),
R("r33-mito-planilha","2027-01-26","tropical",[
  H("Mito ou verdade?","Organizar dinheiro exige <em>planilha?</em>",size="m"),
  M("Sem planilha não dá para controlar gastos.","Basta registrar cada gasto num lugar só.","No Wally, você manda uma mensagem e pronto."),
  O("Teste grátis. "+EM("Link na bio."))],
 "Mito: sem planilha não dá para controlar os gastos. ❌\n\nVerdade: basta registrar cada gasto num lugar só. No Wally você manda uma mensagem no WhatsApp e pronto.",
 "#planilha #organizacaofinanceira #controlefinanceiro"),
R("r34-fechando-janeiro","2027-01-28","house",[
  H("Fim de janeiro","Como foi seu <em>primeiro mês?</em>"),
  C("Veja na hora",[U("/saldo"),S("R$ 3.900,00","R$ 3.120,40","R$ 779,60")]),
  O("Feche o mês no "+EM("Wally."))],
 "Como foi o primeiro mês do ano? 📊\n\nMande /saldo no WhatsApp e veja receitas, despesas e o que sobrou.",
 "#fechamentodomes #saldo #controledegastos"),
# ---------------- Fevereiro ----------------
R("r35-fevereiro-curto","2027-02-02","funk",[
  H("Fevereiro","O mês mais curto <em>engana.</em>"),
  I("Atenção","Lembre-se:",[["As contas são as mesmas","Mesmo com menos dias"],["Tem Carnaval","Reserve o valor antes"],["Fatura de janeiro","Ela chega agora"]]),
  O("Planeje no "+EM("Wally."))],
 "Fevereiro é curto, mas as contas não. 📆\n\n• As contas fixas são as mesmas\n• Tem Carnaval: reserve o valor antes\n• A fatura de janeiro chega agora",
 "#fevereiro #carnaval #orcamento"),
R("r36-carnaval-orcamento","2027-02-04","samba",[
  H("Carnaval","Folia que <em>cabe no bolso.</em>"),
  I("Antes de sair","Defina:",[["Um valor total","Para os dias de festa"],["Um limite por dia","E respeite ele"],["Transporte de volta","Já separado"]]),
  O("Curta com "+EM("tranquilidade."))],
 "Carnaval que cabe no bolso. 🎉\n\n• Defina um valor total para os dias de festa\n• Divida em um limite por dia\n• Separe o dinheiro do transporte de volta",
 "#carnaval #folia #economizar","💾 Salve para o bloco."),
R("r37-carnaval-chat","2027-02-09","samba",[
  H("Terça de Carnaval","Gastou no bloco? <em>Anote.</em>",size="m"),
  C("Leva 5 segundos",[U("/despesa 25 Abadá"),K("🎭","Abadá","Lazer · Hoje","25,00"),U("/despesa 30 Bebidas"),K("🥤","Bebidas","Lazer · Hoje","30,00")]),
  O("Seu dinheiro, "+EM("no WhatsApp."))],
 "Gastou no bloco? Anota rapidinho. 🎭\n\n/despesa 25 Abadá\n/despesa 30 Bebidas\n\nNa quarta-feira você sabe exatamente quanto foi.",
 "#carnaval #whatsapp #controledegastos"),
R("r38-quarta-cinzas","2027-02-11","piano",[
  H("Depois da folia","Hora de olhar o <em>saldo.</em>"),
  I("Recomece","3 passos:",[["Some os gastos","De todos os dias de festa"],["Compare com o planejado","Passou? Quanto?"],["Ajuste o resto do mês","Corte onde der"]]),
  O("Veja tudo no "+EM("Wally."))],
 "A folia acabou. Hora de olhar o saldo. 🧾\n\n1. Some os gastos dos dias de festa\n2. Compare com o que tinha planejado\n3. Ajuste o resto do mês",
 "#carnaval #saldo #orcamento"),
R("r39-mito-dinheiro-trocado","2027-02-16","lofi",[
  H("Mito ou verdade?","Gasto pequeno <em>não conta?</em>"),
  M("Gasto pequeno não pesa no fim do mês.","Somados, eles podem virar uma conta grande.","Um café por dia são cerca de 20 por mês."),
  O("Registre tudo no "+EM("Wally."))],
 "Mito: gasto pequeno não pesa. ❌\n\nVerdade: somados, eles viram uma conta grande. Um café por dia são uns 20 cafés no mês. Registrar mostra o tamanho real.",
 "#gastospequenos #economizar #controledegastos"),
R("r40-texto-livre-2","2027-02-18","bossa",[
  H("WhatsApp","Nem precisa de <em>comando.</em>"),
  C("Escreva normal",[U("Mercado 142,50"),CONF("Mercado","142,50","Alimentação"),BT,OK("Mercado","142,50")]),
  O("Simples assim, "+EM("no WhatsApp."))],
 "Nem precisa de comando. 💬\n\nEscreva \"Mercado 142,50\" e o Wally entende a descrição, o valor e a categoria. É só confirmar.",
 "#whatsapp #appdefinancas #praticidade"),
R("r41-regra-30-dias","2027-02-23","synthwave",[
  H("Compra por impulso","Conhece a regra dos <em>30 dias?</em>",size="m"),
  I("Como funciona","Antes de comprar:",[["Anote o que quer","Com o preço"],["Espere 30 dias","Sem comprar"],["Ainda quer?","Se sim, compre com calma"]]),
  O("Anote seus desejos no "+EM("Wally."))],
 "A regra dos 30 dias contra a compra por impulso. ⏳\n\n1. Anote o que quer comprar e o preço\n2. Espere 30 dias\n3. Se ainda fizer sentido, compre com calma",
 "#compraporimpulso #consumoconsciente #economizar","💾 Salve para a próxima vontade."),
R("r42-fim-fevereiro","2027-02-25","acoustic",[
  H("Fim de mês","Quanto sobrou de <em>fevereiro?</em>"),
  H("Dica","Separe a sobra <em>antes</em> de gastar.",size="m",dur=3.4),
  O("Feche o mês no "+EM("Wally."))],
 "Quanto sobrou de fevereiro? 🧮\n\nDica: separe a sobra para a reserva antes que ela vire gasto.",
 "#fechamentodomes #reservadeemergencia #poupar"),
# ---------------- Março ----------------
R("r43-marco-metas","2027-03-02","chill",[
  H("Março","Suas metas do ano <em>ainda estão de pé?</em>",size="m",dur=3.6),
  I("Revise","Pergunte:",[["Qual era a meta?","Valor e prazo"],["Quanto já guardou?","Seja honesto"],["Precisa ajustar?","Tudo bem recalcular"]]),
  O("Acompanhe no "+EM("Wally."))],
 "Suas metas do ano ainda estão de pé? 🎯\n\n• Qual era a meta, com valor e prazo?\n• Quanto você já guardou?\n• Precisa ajustar? Tudo bem recalcular.",
 "#metasfinanceiras #planejamento #poupar"),
R("r44-imposto-renda","2027-03-04","piano",[
  H("Imposto de Renda","Comece a separar os <em>documentos.</em>",size="m"),
  I("Organize","Junte:",[["Informes de rendimento","Do trabalho e do banco"],["Recibos de saúde","Consultas e exames"],["Gastos com educação","Escola e faculdade"]]),
  O("Organize-se com o "+EM("Wally."))],
 "Época de Imposto de Renda: comece a separar os documentos. 📂\n\n• Informes de rendimento do trabalho e do banco\n• Recibos de saúde\n• Gastos com educação\n\nConfira prazos e regras no site da Receita Federal.",
 "#impostoderenda #irpf #organizacao","💾 Salve a lista."),
R("r45-mito-renda-extra","2027-03-09","tropical",[
  H("Mito ou verdade?","Renda extra resolve <em>tudo?</em>"),
  M("Se eu ganhar mais, sobra dinheiro.","Sem controle, o gasto cresce junto.","Primeiro organize, depois aumente a renda."),
  O("Organize no "+EM("Wally."))],
 "Mito: ganhando mais, sobra dinheiro. ❌\n\nVerdade: sem controle, o gasto cresce junto com a renda. Primeiro organize, depois aumente.",
 "#rendaextra #dinheiro #organizacaofinanceira"),
R("r46-freela","2027-03-11","house",[
  H("WhatsApp","Entrou uma <em>renda extra?</em>"),
  C("Registre também",[U("/receita 400 Freela design"),K("💼","Freela design","Outras receitas · Hoje","400,00",True),U("/saldo"),S("R$ 4.300,00","R$ 2.210,90","R$ 2.089,10")]),
  O("Receitas e despesas "+EM("num lugar só."))],
 "Entrou uma renda extra? Registra também. 💼\n\n/receita 400 Freela design\n/saldo\n\nReceitas e despesas num lugar só.",
 "#rendaextra #freela #controlefinanceiro"),
R("r47-dia-consumidor","2027-03-16","funk",[
  H("Dia do Consumidor","Promoção <em>não é obrigação.</em>",size="m"),
  I("Antes de clicar","Confira:",[["Estava na lista?","Se não, desconfie"],["O preço caiu mesmo?","Compare com antes"],["Cabe no mês?","Sem parcelar o futuro"]]),
  O("Compre com "+EM("planejamento."))],
 "Dia do Consumidor: promoção não é obrigação. 🏷️\n\n• Estava na sua lista?\n• O preço caiu mesmo?\n• Cabe no mês sem parcelar o futuro?",
 "#diadoconsumidor #promocao #consumoconsciente"),
R("r48-reserva-quanto","2027-03-18","lofi",[
  H("Reserva de emergência","Quanto ter <em>guardado?</em>"),
  I("Referência comum","Um caminho:",[["Some seu custo mensal","Só o essencial"],["Multiplique por 3 a 6","Conforme sua estabilidade"],["Comece pelo primeiro mês","Um passo de cada vez"]]),
  O("Defina a meta no "+EM("Wally."))],
 "Quanto ter na reserva de emergência? 🛟\n\nUma referência comum:\n1. Some seu custo mensal essencial\n2. Multiplique por 3 a 6, conforme sua estabilidade\n3. Comece guardando o primeiro mês",
 "#reservadeemergencia #poupar #metasfinanceiras","💾 Salve para fazer a conta."),
R("r49-pergunta-categoria","2027-03-23","bossa",[
  H("Teste rápido","Em qual categoria você <em>mais gasta?</em>",size="m",dur=3.8),
  H("Muita gente erra","O palpite quase nunca <em>bate.</em>",size="m",dur=3.2),
  H("Descubra","Registre por um mês e <em>compare.</em>",size="m",dur=3.6),
  O("Veja por categoria no "+EM("Wally."))],
 "Em qual categoria você mais gasta? 🗂️\n\nO palpite quase nunca bate. Registre por um mês e compare.",
 "#categorias #controledegastos #autoconhecimento"),
R("r50-mito-investir","2027-03-25","synthwave",[
  H("Mito ou verdade?","Investir é só para <em>quem tem muito?</em>",size="m"),
  M("Investir é coisa de rico.","O primeiro passo é ter sobra todo mês.","Organizar os gastos vem antes de investir."),
  O("Comece pelo "+EM("controle."))],
 "Mito: investir é coisa de rico. ❌\n\nVerdade: o primeiro passo é ter sobra todo mês, e isso começa organizando os gastos.",
 "#investimentos #educacaofinanceira #poupar"),
R("r51-fim-trimestre","2027-03-30","acoustic",[
  H("Fim do trimestre","3 meses de 2027. <em>E aí?</em>"),
  I("Balanço rápido","Veja:",[["O mês que mais gastou","E por quê"],["Quanto guardou","No total"],["Um ajuste","Para o próximo trimestre"]]),
  O("Veja o histórico no "+EM("Wally."))],
 "Três meses de 2027. E aí? 📈\n\n• Qual mês você mais gastou e por quê\n• Quanto guardou no total\n• Um ajuste para o próximo trimestre",
 "#balanco #trimestre #planejamento"),
# ---------------- Abril ----------------
R("r52-abril-assinaturas","2027-04-01","chill",[
  H("Novo mês","Hora de revisar as <em>assinaturas.</em>",size="m"),
  I("Revisão","Para cada uma:",[["Usou no último mês?","Se não, cancele"],["Tem plano mais barato?","Muitas têm"],["Divide com alguém?","Planos família ajudam"]]),
  O("Veja tudo no "+EM("Wally."))],
 "Novo mês, hora de revisar as assinaturas. 📺\n\n• Usou no último mês? Se não, cancele\n• Tem plano mais barato?\n• Dá para dividir num plano família?",
 "#assinaturas #streaming #economizar"),
R("r53-mito-pascoa","2027-04-06","piano",[
  H("Mito ou verdade?","Gasto de data comemorativa <em>não conta?</em>",size="m"),
  M("Datas especiais ficam fora do orçamento.","Elas acontecem todo ano. Dá para prever.","Reserve um pouco por mês para elas."),
  O("Planeje no "+EM("Wally."))],
 "Mito: datas especiais ficam fora do orçamento. ❌\n\nVerdade: elas acontecem todo ano. Dá para prever e reservar um pouco por mês.",
 "#datascomemorativas #planejamento #orcamento"),
R("r54-delivery","2027-04-08","funk",[
  H("Delivery","Quanto foi o <em>delivery</em> do mês?",size="m"),
  C("Some na hora",[U("/despesa 48 Pizza"),K("🍕","Pizza","Alimentação · Hoje","48,00"),U("/despesa 36 Lanche"),K("🍔","Lanche","Alimentação · Hoje","36,00")]),
  O("Veja o total no "+EM("Wally."))],
 "Quanto foi o delivery do mês? 🍕\n\nRegistre cada pedido e veja o total no fim. Muita gente se surpreende.",
 "#delivery #gastos #controledegastos"),
R("r55-orcamento-base-zero","2027-04-13","lofi",[
  H("Método","Todo real com <em>uma função.</em>"),
  I("Orçamento base zero","Como fazer:",[["Anote a renda do mês","O valor total"],["Distribua cada real","Contas, desejos e futuro"],["Feche em zero","Nada fica sem destino"]]),
  O("Acompanhe no "+EM("Wally."))],
 "Orçamento base zero: todo real com uma função. 🧩\n\n1. Anote a renda do mês\n2. Distribua cada real entre contas, desejos e futuro\n3. Feche em zero: nada fica sem destino",
 "#orcamento #metodo #organizacaofinanceira","💾 Salve para testar."),
R("r56-pergunta-poupou","2027-04-15","tropical",[
  H("Teste rápido","Quanto você guardou <em>mês passado?</em>",size="m",dur=3.6),
  H("Zero?","Comece com <em>qualquer valor.</em>",size="m",dur=3.2),
  H("O segredo","é guardar <em>no começo</em> do mês.",size="m",dur=3.4),
  O("Defina sua meta no "+EM("Wally."))],
 "Quanto você guardou no mês passado? 🐷\n\nSe foi zero, comece com qualquer valor. O segredo é guardar no começo do mês, não com o que sobra.",
 "#poupar #guardardinheiro #metasfinanceiras"),
R("r57-mito-dinheiro-vivo","2027-04-20","bossa",[
  H("Mito ou verdade?","Pix e cartão fazem <em>gastar mais?</em>",size="m"),
  M("Só com dinheiro vivo dá para controlar.","Dá para controlar qualquer forma de pagamento.","O que importa é registrar cada gasto."),
  O("Registre tudo no "+EM("Wally."))],
 "Mito: só com dinheiro vivo dá para controlar. ❌\n\nVerdade: dá para controlar qualquer forma de pagamento. O que importa é registrar cada gasto.",
 "#pix #cartao #controlefinanceiro"),
R("r58-feriado","2027-04-22","acoustic",[
  H("Feriado","Viagem curta, <em>gasto grande?</em>"),
  I("Antes de ir","Planeje:",[["Hospedagem e transporte","Os maiores gastos"],["Comida","Um valor por dia"],["Imprevistos","Uma pequena folga"]]),
  O("Planeje no "+EM("Wally."))],
 "Feriado: viagem curta, gasto grande? 🧳\n\n• Hospedagem e transporte primeiro\n• Comida: um valor por dia\n• Uma folga para imprevistos",
 "#feriado #viagem #planejamento"),
R("r59-dividas","2027-04-27","piano",[
  H("Dívidas","Por onde <em>começar?</em>"),
  I("Organize","Primeiro passo:",[["Liste todas","Valor e juros de cada uma"],["Priorize juros altos","Cartão e cheque especial"],["Negocie","Peça condições melhores"]]),
  O("Organize-se no "+EM("Wally."))],
 "Dívidas: por onde começar? 🧾\n\n1. Liste todas, com valor e juros\n2. Priorize as de juros mais altos, como cartão e cheque especial\n3. Negocie condições melhores",
 "#dividas #juros #organizacaofinanceira","💾 Salve se precisar."),
R("r60-fim-abril","2027-04-29","house",[
  H("Fim de abril","Mande um <em>/saldo.</em>"),
  C("Resumo na hora",[U("/saldo"),S("R$ 3.900,00","R$ 2.980,30","R$ 919,70")]),
  O("Seu dinheiro, "+EM("no WhatsApp."))],
 "Fim de abril. Já mandou um /saldo? 📊\n\nReceitas, despesas e o que sobrou, na hora, no WhatsApp.",
 "#saldo #fechamentodomes #whatsapp"),
# ---------------- Maio ----------------
R("r61-maio-planejamento","2027-05-04","chill",[
  H("Maio","Tem <em>Dia das Mães</em> chegando.",size="m"),
  I("Planeje","Defina:",[["Presente","Um valor máximo"],["Almoço ou passeio","Divida com os irmãos?"],["Data","Compre sem pressa"]]),
  O("Planeje no "+EM("Wally."))],
 "Tem Dia das Mães chegando. 💐\n\n• Defina um valor máximo para o presente\n• Almoço ou passeio: dá para dividir?\n• Compre sem pressa",
 "#diadasmaes #presente #planejamento"),
R("r62-dia-das-maes","2027-05-06","acoustic",[
  H("Dia das Mães","O melhor presente <em>não precisa custar caro.</em>",size="m",dur=3.8),
  H("Dica","Presente que cabe no orçamento é <em>presente sem culpa.</em>",size="m",dur=3.8),
  O("Feliz Dia das Mães, "+EM("com carinho."),"Equipe Wally.")],
 "O melhor presente não precisa custar caro. 💐\n\nPresente que cabe no orçamento é presente sem culpa. Feliz Dia das Mães!",
 "#diadasmaes #maes #carinho"),
R("r63-mito-salario","2027-05-11","synthwave",[
  H("Mito ou verdade?","O salário <em>some sozinho?</em>"),
  M("Meu salário some e eu não sei como.","Ele vai para lugares. Você só não está vendo.","Registrar por um mês mostra o caminho."),
  O("Descubra no "+EM("Wally."))],
 "Mito: o salário some sozinho. ❌\n\nVerdade: ele vai para lugares, você só não está vendo. Registre por um mês e veja o caminho.",
 "#salario #controledegastos #organizacaofinanceira"),
R("r64-mercado","2027-05-13","bossa",[
  H("Mercado","Gaste menos <em>sem passar vontade.</em>",size="m"),
  I("No mercado","4 hábitos:",[["Vá com lista","E siga ela"],["Não vá com fome","Sério"],["Compare o preço por quilo","Nem sempre o maior compensa"],["Registre o total","E acompanhe a média"]]),
  O("Acompanhe no "+EM("Wally."))],
 "Gaste menos no mercado sem passar vontade. 🛒\n\n1. Vá com lista\n2. Não vá com fome\n3. Compare o preço por quilo\n4. Registre o total e acompanhe a média",
 "#mercado #economizar #supermercado","💾 Salve para a próxima compra."),
R("r65-ir-prazo","2027-05-18","piano",[
  H("Imposto de Renda","O prazo está <em>acabando.</em>"),
  H("Não deixe pro fim","Atraso pode gerar <em>multa.</em>",size="m",dur=3.4),
  O("Organize-se com o "+EM("Wally."))],
 "Imposto de Renda: o prazo está acabando. ⏰\n\nNão deixe para o último dia: atraso pode gerar multa. Confira o prazo no site da Receita Federal.",
 "#impostoderenda #irpf #prazo"),
R("r66-chat-conta-luz","2027-05-20","lofi",[
  H("WhatsApp","Pagou uma conta? <em>Registre.</em>"),
  C("Contas do mês",[U("/despesa 156 Conta de luz"),K("💡","Conta de luz","Moradia · Hoje","156,00"),U("/despesa 89 Internet"),K("📶","Internet","Moradia · Hoje","89,00")]),
  O("Seu dinheiro, "+EM("no WhatsApp."))],
 "Pagou uma conta? Registre na hora. 💡\n\n/despesa 156 Conta de luz\n/despesa 89 Internet\n\nNo fim do mês você sabe quanto foi de moradia.",
 "#contas #whatsapp #controlefinanceiro"),
R("r67-mito-poupanca-sobra","2027-05-25","tropical",[
  H("Mito ou verdade?","Guardar o que <em>sobra?</em>"),
  M("Eu guardo o que sobrar no fim do mês.","Quase nunca sobra. Guarde primeiro.","Trate a reserva como uma conta fixa."),
  O("Defina sua meta no "+EM("Wally."))],
 "Mito: guardar o que sobra no fim do mês. ❌\n\nVerdade: quase nunca sobra. Guarde primeiro e trate a reserva como uma conta fixa.",
 "#poupar #reservadeemergencia #habitos"),
R("r68-fim-maio","2027-05-27","funk",[
  H("Fim de maio","3 perguntas para <em>fechar o mês.</em>",size="m"),
  I("Responda","Rápido:",[["Gastei mais que entrou?","Se sim, onde?"],["Guardei algo?","Mesmo pouco conta"],["O que muda em junho?","Um ajuste só"]]),
  O("Feche o mês no "+EM("Wally."))],
 "Três perguntas para fechar maio. ✅\n\n• Gastei mais do que entrou? Onde?\n• Guardei algo? Mesmo pouco conta\n• O que muda em junho?",
 "#fechamentodomes #planejamento #orcamento"),
# ---------------- Junho ----------------
R("r69-junho-metade","2027-06-01","chill",[
  H("Junho","Metade do ano <em>chegando.</em>"),
  H("Pergunta","Você está mais perto <em>da sua meta?</em>",size="m",dur=3.6),
  O("Acompanhe no "+EM("Wally."))],
 "Junho: metade do ano chegando. ⏳\n\nVocê está mais perto da sua meta do que em janeiro?",
 "#metasfinanceiras #meiodoano #planejamento"),
R("r70-chat-cinema","2027-06-03","synthwave",[
  H("WhatsApp","Lazer também <em>entra na conta.</em>",size="m"),
  C("Registre o rolê",[U("Cinema 64"),CONF("Cinema","64,00","Lazer"),BT,OK("Cinema","64,00")]),
  O("Seu dinheiro, "+EM("no WhatsApp."))],
 "Lazer também entra na conta. 🎬\n\nEscreva \"Cinema 64\" e confirme. Saber quanto vai para lazer ajuda a curtir sem culpa.",
 "#lazer #whatsapp #controledegastos"),
R("r71-mito-namorados","2027-06-08","bossa",[
  H("Mito ou verdade?","Amor se mede no <em>presente?</em>"),
  M("Presente caro mostra o quanto eu gosto.","Carinho não tem etiqueta de preço.","Um presente que cabe no bolso vale muito."),
  O("Planeje no "+EM("Wally."))],
 "Mito: presente caro mostra o quanto você gosta. ❌\n\nVerdade: carinho não tem etiqueta de preço. Um presente que cabe no bolso vale muito.",
 "#diadosnamorados #presente #consumoconsciente"),
R("r72-namorados","2027-06-10","acoustic",[
  H("Dia dos Namorados","3 ideias que <em>cabem no bolso.</em>",size="m"),
  I("Ideias","Com carinho:",[["Jantar em casa","Feito a dois"],["Piquenique","No parque mais perto"],["Carta à mão","Nunca sai de moda"]]),
  O("Comemore "+EM("sem apertar."))],
 "Dia dos Namorados: ideias que cabem no bolso. 💕\n\n• Jantar feito a dois em casa\n• Piquenique no parque\n• Uma carta à mão",
 "#diadosnamorados #casal #economizar","💾 Salve e mande pro seu amor."),
R("r73-financas-casal","2027-06-15","lofi",[
  H("Finanças a dois","Como dividir as <em>contas do casal?</em>",size="m"),
  I("Combinem","Opções:",[["Meio a meio","Simples, se a renda é parecida"],["Proporcional à renda","Cada um paga uma parte justa"],["Conta conjunta","Para os gastos da casa"]]),
  O("Organizem juntos no "+EM("Wally."))],
 "Como dividir as contas do casal? 💑\n\n• Meio a meio, se a renda é parecida\n• Proporcional à renda de cada um\n• Uma conta conjunta para os gastos da casa\n\nO importante é combinar.",
 "#financasacasal #casal #organizacaofinanceira"),
R("r74-pergunta-impulso","2027-06-17","house",[
  H("Teste rápido","Qual foi sua última <em>compra por impulso?</em>",size="m",dur=3.8),
  H("Você usa?","Muita coisa fica <em>parada na gaveta.</em>",size="m",dur=3.4),
  H("Dica","Espere um dia <em>antes de pagar.</em>",size="m",dur=3.4),
  O("Registre e "+EM("repense."))],
 "Qual foi sua última compra por impulso? 🛍️\n\nMuita coisa fica parada na gaveta. Dica: espere um dia antes de pagar.",
 "#compraporimpulso #consumoconsciente #economizar"),
R("r75-festa-junina","2027-06-22","forro",[
  H("Festa junina","Arraiá <em>sem estourar.</em>"),
  I("No arraiá","Dicas:",[["Leve um valor fixo","Em dinheiro ou no Pix"],["Coma antes de ir","Ajuda a gastar menos"],["Combine com a turma","Quanto cada um leva"]]),
  O("Anote no "+EM("Wally."))],
 "Arraiá sem estourar o orçamento. 🌽\n\n• Leve um valor fixo\n• Coma algo antes de ir\n• Combine com a turma quanto cada um leva",
 "#festajunina #arraia #economizar"),
R("r76-arraia-chat","2027-06-24","forro",[
  H("São João","Pamonha, quentão… <em>quanto foi?</em>",size="m"),
  C("Anote na festa",[U("/despesa 12 Pamonha"),K("🌽","Pamonha","Alimentação · Hoje","12,00"),U("/despesa 15 Quentão"),K("🍵","Quentão","Alimentação · Hoje","15,00")]),
  O("Seu dinheiro, "+EM("no WhatsApp."))],
 "Pamonha, quentão… quanto foi? 🌽\n\n/despesa 12 Pamonha\n/despesa 15 Quentão\n\nAnota na hora e curte a festa.",
 "#saojoao #festajunina #whatsapp"),
R("r77-balanco-semestre","2027-06-29","piano",[
  H("Fim do semestre","Seu balanço de <em>6 meses.</em>"),
  I("Balanço","Compare:",[["Receitas","Quanto entrou no semestre"],["Despesas","As 3 maiores categorias"],["Sobra","Quanto foi para as metas"]]),
  O("Veja o semestre no "+EM("Wally."))],
 "Fim do semestre: hora do balanço. 📊\n\n• Quanto entrou\n• As 3 categorias que mais pesaram\n• Quanto foi para as metas",
 "#balanco #semestre #planejamento","💾 Salve para fazer hoje."),
# ---------------- Julho ----------------
R("r78-julho-recomeco","2027-07-01","chill",[
  H("Segundo semestre","Um novo <em>recomeço.</em>"),
  H("Escolha","<em>Uma</em> meta para os próximos 6 meses.",size="m",dur=3.6),
  O("Crie a sua no "+EM("Wally."))],
 "Segundo semestre: um novo recomeço. 🌱\n\nEscolha uma meta para os próximos seis meses, com valor e prazo.",
 "#metasfinanceiras #recomeco #planejamento"),
R("r79-ferias","2027-07-06","tropical",[
  H("Férias","Viajar sem voltar <em>no vermelho.</em>",size="m"),
  I("Planeje","Antes de ir:",[["Defina o total","Da viagem inteira"],["Divida por dia","Comida e passeios"],["Evite parcelar","O que já foi consumido"]]),
  O("Planeje no "+EM("Wally."))],
 "Viajar sem voltar no vermelho. ✈️\n\n• Defina o total da viagem\n• Divida comida e passeios por dia\n• Evite parcelar o que já foi consumido",
 "#ferias #viagem #planejamento","💾 Salve para a viagem."),
R("r80-mito-ferias","2027-07-08","samba",[
  H("Mito ou verdade?","Nas férias <em>pode tudo?</em>"),
  M("Férias é para gastar sem pensar.","Férias é para descansar, inclusive da fatura.","Um teto por dia deixa tudo mais leve."),
  O("Curta com "+EM("tranquilidade."))],
 "Mito: férias é para gastar sem pensar. ❌\n\nVerdade: férias é para descansar, inclusive da fatura. Um teto por dia deixa tudo mais leve.",
 "#ferias #viagem #consumoconsciente"),
R("r81-filhos-ferias","2027-07-13","acoustic",[
  H("Férias das crianças","Diversão que <em>não pesa.</em>",size="m"),
  I("Ideias baratas","Programe:",[["Parques e praças","Gratuitos"],["Museus","Muitos têm dia grátis"],["Cinema em casa","Pipoca feita em casa"]]),
  O("Anote os gastos no "+EM("Wally."))],
 "Férias das crianças sem pesar no bolso. 🧒\n\n• Parques e praças\n• Museus (muitos têm dia gratuito)\n• Cinema em casa, com pipoca feita em casa",
 "#feriasescolares #familia #economizar"),
R("r82-chat-viagem","2027-07-15","bossa",[
  H("Na viagem","Registre <em>direto do celular.</em>",size="m"),
  C("Onde estiver",[U("/despesa 220 Hotel"),K("🏨","Hotel","Viagem · Hoje","220,00"),U("/despesa 74 Restaurante"),K("🍽️","Restaurante","Alimentação · Hoje","74,00")]),
  O("Seu dinheiro, "+EM("no WhatsApp."))],
 "Na viagem, registre direto do celular. 🏨\n\n/despesa 220 Hotel\n/despesa 74 Restaurante\n\nVocê volta sabendo quanto custou.",
 "#viagem #whatsapp #controledegastos"),
R("r83-pergunta-taxas","2027-07-20","lofi",[
  H("Teste rápido","Quanto você paga de <em>tarifa bancária?</em>",size="m",dur=3.8),
  H("Confira","Existem contas <em>sem tarifa.</em>",size="m",dur=3.2),
  H("Revise","Anuidade também dá para <em>negociar.</em>",size="m",dur=3.4),
  O("Veja tudo no "+EM("Wally."))],
 "Quanto você paga de tarifa bancária? 🏦\n\nExistem contas sem tarifa, e anuidade de cartão também dá para negociar.",
 "#tarifas #banco #economizar"),
R("r84-mito-cartao-limite","2027-07-22","synthwave",[
  H("Mito ou verdade?","Limite do cartão é <em>dinheiro meu?</em>",size="m"),
  M("O limite do cartão é dinheiro disponível.","Limite é crédito. A conta chega depois.","Use como meio de pagamento, não como renda."),
  O("Acompanhe a fatura no "+EM("Wally."))],
 "Mito: o limite do cartão é dinheiro disponível. ❌\n\nVerdade: limite é crédito, e a conta chega depois. Use o cartão como meio de pagamento, não como renda.",
 "#cartaodecredito #limite #dividas"),
R("r85-volta-ferias","2027-07-27","house",[
  H("Fim das férias","Hora de <em>reorganizar.</em>"),
  I("Volta","3 passos:",[["Some a viagem","Tudo, inclusive o cartão"],["Veja as faturas","Que ainda vão chegar"],["Ajuste agosto","Para compensar"]]),
  O("Organize no "+EM("Wally."))],
 "Fim das férias: hora de reorganizar. 🗓️\n\n1. Some tudo da viagem, inclusive o cartão\n2. Veja as faturas que ainda vão chegar\n3. Ajuste agosto para compensar",
 "#ferias #organizacaofinanceira #orcamento"),
R("r86-fim-julho","2027-07-29","funk",[
  H("Fim de julho","Seu <em>/saldo</em> de julho.",size="m"),
  C("Resumo do mês",[U("/saldo"),S("R$ 3.900,00","R$ 3.410,60","R$ 489,40")]),
  O("Seu dinheiro, "+EM("no WhatsApp."))],
 "Já viu seu saldo de julho? 📊\n\nMande /saldo no WhatsApp e veja o mês inteiro em segundos.",
 "#saldo #fechamentodomes #whatsapp"),
# ---------------- Agosto ----------------
R("r87-agosto","2027-08-03","piano",[
  H("Agosto","Mês sem feriado nacional = <em>mês de foco.</em>",size="m",dur=3.8),
  I("Aproveite","Para:",[["Rever metas","Do segundo semestre"],["Cortar um gasto","O que menos faz falta"],["Reforçar a reserva","Mesmo que pouco"]]),
  O("Foque no "+EM("Wally."))],
 "Agosto é mês de foco. 🎯\n\n• Reveja as metas do semestre\n• Corte o gasto que menos faz falta\n• Reforce a reserva, mesmo que pouco",
 "#agosto #foco #metasfinanceiras"),
R("r88-dia-dos-pais","2027-08-05","acoustic",[
  H("Dia dos Pais","Presente com carinho e <em>com limite.</em>",size="m"),
  I("Ideias","Que cabem no bolso:",[["Um almoço especial","Feito em casa"],["Um passeio juntos","Tempo vale muito"],["Presente coletivo","Dividido entre os irmãos"]]),
  O("Feliz Dia dos Pais, "+EM("com carinho."),"Equipe Wally.")],
 "Dia dos Pais: presente com carinho e com limite. 👨‍👧\n\n• Um almoço especial feito em casa\n• Um passeio juntos\n• Um presente coletivo, dividido entre os irmãos",
 "#diadospais #presente #familia"),
R("r89-mito-orcamento-rigido","2027-08-10","lofi",[
  H("Mito ou verdade?","Orçamento é <em>passar vontade?</em>"),
  M("Ter orçamento é viver sem lazer.","Orçamento bom tem espaço para lazer.","O lazer planejado não vira culpa."),
  O("Planeje no "+EM("Wally."))],
 "Mito: ter orçamento é viver sem lazer. ❌\n\nVerdade: orçamento bom tem espaço para lazer. E lazer planejado não vira culpa.",
 "#orcamento #lazer #organizacaofinanceira"),
R("r90-gasolina","2027-08-12","synthwave",[
  H("Transporte","Quanto custa <em>se locomover?</em>"),
  C("Registre o transporte",[U("/despesa 200 Gasolina"),K("⛽","Gasolina","Transporte · Hoje","200,00"),U("/despesa 22 Estacionamento"),K("🅿️","Estacionamento","Transporte · Hoje","22,00")]),
  O("Veja por categoria no "+EM("Wally."))],
 "Quanto custa se locomover no mês? ⛽\n\n/despesa 200 Gasolina\n/despesa 22 Estacionamento\n\nVeja o total de transporte no fim do mês.",
 "#transporte #gasolina #controledegastos"),
R("r91-emprestimo","2027-08-17","chill",[
  H("Empréstimo","Antes de <em>assinar.</em>"),
  I("Confira","Sempre:",[["O custo total","Não só a parcela"],["A taxa de juros","Compare em mais de um banco"],["Se cabe no mês","Por todos os meses"]]),
  O("Organize-se no "+EM("Wally."))],
 "Empréstimo: antes de assinar, confira. ✍️\n\n• O custo total, não só a parcela\n• A taxa de juros, comparando bancos\n• Se a parcela cabe em todos os meses",
 "#emprestimo #juros #credito","💾 Salve para consultar."),
R("r92-pergunta-meta","2027-08-19","bossa",[
  H("Teste rápido","Sua meta tem <em>prazo?</em>",dur=3.4),
  H("Sem prazo…","ela vira só <em>um desejo.</em>",size="m",dur=3.2),
  H("Defina","Quanto, até quando e <em>quanto por mês.</em>",size="m",dur=3.6),
  O("Crie a meta no "+EM("Wally."))],
 "Sua meta tem prazo? ⏰\n\nSem prazo, ela vira só um desejo. Defina quanto, até quando e quanto guardar por mês.",
 "#metasfinanceiras #prazo #planejamento"),
R("r93-parcelas","2027-08-24","tropical",[
  H("Parcelamento","Parcelas <em>se acumulam.</em>"),
  I("Antes de parcelar","Pense:",[["Quantas já tenho?","Some todas"],["Até quando vão?","Meses comprometidos"],["Sobra para o resto?","Contas e reserva"]]),
  O("Acompanhe no "+EM("Wally."))],
 "Parcelas se acumulam. 💳\n\n• Quantas você já tem?\n• Até quando elas vão?\n• Sobra para as contas e para a reserva?",
 "#parcelamento #cartaodecredito #dividas"),
R("r94-mito-app-dificil","2027-08-26","house",[
  H("Mito ou verdade?","App de finanças é <em>complicado?</em>",size="m"),
  M("App de finanças dá trabalho para usar.","No Wally você só manda uma mensagem.","Texto livre ou comando, do jeito que preferir."),
  O("Teste grátis. "+EM("Link na bio."))],
 "Mito: app de finanças dá trabalho. ❌\n\nVerdade: no Wally você só manda uma mensagem no WhatsApp, em texto livre ou com comando.",
 "#appdefinancas #whatsapp #praticidade"),
R("r95-fim-agosto","2027-08-31","funk",[
  H("Fim de agosto","Mês de foco <em>cumprido?</em>"),
  H("Comemore","Cada real guardado <em>conta.</em>",size="m",dur=3.2),
  O("Veja o mês no "+EM("Wally."))],
 "Mês de foco cumprido? 🙌\n\nComemore: cada real guardado conta.",
 "#fechamentodomes #poupar #metasfinanceiras"),
# ---------------- Setembro ----------------
R("r96-setembro","2027-09-02","acoustic",[
  H("Setembro","Faltam 4 meses <em>para o fim do ano.</em>",size="m"),
  I("Prepare-se","Já pense em:",[["Fim de ano","Presentes e festas"],["13º salário","Destino definido"],["Contas de janeiro","Elas sempre voltam"]]),
  O("Planeje no "+EM("Wally."))],
 "Faltam quatro meses para o fim do ano. 🗓️\n\n• Presentes e festas\n• Destino do 13º\n• As contas de janeiro, que sempre voltam",
 "#setembro #planejamento #fimdeano"),
R("r97-feriado-7-setembro","2027-09-07","samba",[
  H("Feriado","Folga prolongada, <em>gasto controlado.</em>",size="m"),
  I("No feriado","Lembre:",[["Um valor para os dias","E respeite"],["Programas gratuitos","Existem vários"],["Anote tudo","Na hora"]]),
  O("Bom feriado, "+EM("com o Wally."))],
 "Feriado prolongado, gasto controlado. 🇧🇷\n\n• Um valor para os dias de folga\n• Programas gratuitos\n• Anote tudo na hora",
 "#feriado #7desetembro #economizar"),
R("r98-chat-farmacia","2027-09-09","lofi",[
  H("WhatsApp","Saúde também <em>entra no orçamento.</em>",size="m"),
  C("Registre",[U("Farmácia 58,90"),CONF("Farmácia","58,90","Saúde"),BT,OK("Farmácia","58,90")]),
  O("Seu dinheiro, "+EM("no WhatsApp."))],
 "Saúde também entra no orçamento. 💊\n\nEscreva \"Farmácia 58,90\", confirme, e o gasto vai para a categoria certa.",
 "#saude #whatsapp #controledegastos"),
R("r99-dia-cliente","2027-09-14","synthwave",[
  H("Dia do Cliente","Cupom bom é o que <em>você ia usar.</em>",size="m"),
  I("Antes de comprar","Confira:",[["Estava nos planos?","Se não, é gasto novo"],["Frete incluso?","Muda o preço final"],["Cabe no mês?","Sem parcelar"]]),
  O("Compre com "+EM("planejamento."))],
 "Dia do Cliente: cupom bom é o que você ia usar. 🏷️\n\n• Estava nos planos?\n• O frete muda o preço final?\n• Cabe no mês sem parcelar?",
 "#diadocliente #promocao #consumoconsciente"),
R("r100-mito-sorte","2027-09-16","piano",[
  H("Mito ou verdade?","Organização financeira é <em>sorte?</em>",size="m"),
  M("Quem tem dinheiro guardado teve sorte.","Na maioria das vezes, é hábito repetido.","Pequenas decisões, todo mês."),
  O("Crie o hábito no "+EM("Wally."))],
 "Mito: quem tem dinheiro guardado teve sorte. ❌\n\nVerdade: na maioria das vezes é hábito repetido. Pequenas decisões, todo mês.",
 "#habitosfinanceiros #disciplina #poupar"),
R("r101-primavera","2027-09-21","bossa",[
  H("Primavera","Hora de fazer uma <em>faxina financeira.</em>",size="m"),
  I("Faxina","Limpe:",[["Assinaturas paradas","Cancele"],["Cartões sem uso","Avalie a anuidade"],["Gastos repetidos","Que não fazem falta"]]),
  O("Comece no "+EM("Wally."))],
 "Primavera: hora da faxina financeira. 🌸\n\n• Cancele assinaturas paradas\n• Avalie a anuidade dos cartões sem uso\n• Corte gastos repetidos que não fazem falta",
 "#primavera #economizar #organizacaofinanceira","💾 Salve para fazer no fim de semana."),
R("r102-pergunta-reserva","2027-09-23","chill",[
  H("Teste rápido","Se a renda parasse hoje, quanto tempo <em>você aguentaria?</em>",size="s",dur=4.2),
  H("Esse número","é a sua <em>reserva em meses.</em>",size="m",dur=3.2),
  H("Meta","Aumentar <em>um mês</em> por vez.",size="m",dur=3.2),
  O("Defina sua meta no "+EM("Wally."))],
 "Se a renda parasse hoje, quanto tempo você aguentaria? 🛟\n\nEsse número é a sua reserva em meses. A meta é aumentar um mês por vez.",
 "#reservadeemergencia #seguranca #poupar"),
R("r103-trimestre-final","2027-09-28","house",[
  H("Último trimestre","Prepare o fim do ano <em>agora.</em>",size="m"),
  I("Comece já","3 ações:",[["Faça a lista de presentes","Com valor por pessoa"],["Guarde um pouco por mês","Para as festas"],["Planeje janeiro","IPVA, IPTU e escola"]]),
  O("Planeje no "+EM("Wally."))],
 "Prepare o fim do ano agora. 🎄\n\n• Lista de presentes com valor por pessoa\n• Guarde um pouco por mês para as festas\n• Planeje janeiro: IPVA, IPTU e escola",
 "#fimdeano #planejamento #organizacaofinanceira"),
R("r104-fim-setembro","2027-09-30","tropical",[
  H("Fim de setembro","9 meses de registros. <em>Olhe para trás.</em>",size="m"),
  C("Seu resumo",[U("/saldo"),S("R$ 3.900,00","R$ 2.870,10","R$ 1.029,90")]),
  O("Seu dinheiro, "+EM("no WhatsApp."))],
 "Nove meses de registros. Olhe para trás. 📈\n\nMande /saldo e compare com o começo do ano. Pequenos hábitos fazem diferença.",
 "#fechamentodomes #saldo #habitosfinanceiros"),
]
