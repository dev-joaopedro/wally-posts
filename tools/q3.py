from common import P, card, LINK, SALVE

POSTS = [

P("2027-04-02", "mito", "Mito ou verdade",
"""Mito ou verdade? 🤔

"Investir é só para quem tem muito dinheiro."

❌ MITO!

Hoje existem opções de investimento com valores iniciais bem baixos. O mais importante não é quanto você começa, e sim começar e manter a constância.

Antes de investir, garanta o básico:
✅ Saber para onde vai o seu dinheiro
✅ Não ter dívidas caras, como cartão e cheque especial
✅ Ter uma reserva de emergência, mesmo que pequena

Organizar vem antes de investir. E aí o Wally ajuda. 😉
""", ["reserva", "vida"],
title="Investir é só para _quem tem muito?_",
mito="Investir é só para quem tem muito dinheiro.",
verdade="Há opções com **valores iniciais baixos**. O que importa é começar e manter a **constância**."),

P("2027-04-05", "dica", "Dica de finanças",
"""Quer começar a investir? Antes do "onde", vem o "como". 📈

1️⃣ Organize o orçamento e descubra quanto sobra por mês
2️⃣ Quite as dívidas com juros altos
3️⃣ Monte a reserva de emergência
4️⃣ Defina o objetivo e o prazo de cada investimento
5️⃣ Entenda o risco de cada opção antes de aplicar

Desconfie de promessas de ganho alto, rápido e garantido. 🚩

Este post é educativo e não é recomendação de investimento. Na dúvida, procure um profissional certificado.

""" + SALVE, ["reserva", "meta"],
title="Antes de investir, _faça isto_",
items=["Organize o orçamento e veja **quanto sobra**",
       "Quite as **dívidas caras**",
       "Monte a **reserva de emergência**",
       "Defina **objetivo e prazo**",
       "Entenda o **risco** antes de aplicar"]),

P("2027-04-07", "chat", "Wally na prática",
"""Renda variável? O Wally acompanha cada entrada. 💼

Freelancers, autônomos e quem tem uma renda extra sabem: o dinheiro entra em dias diferentes, de clientes diferentes.

No WhatsApp, é só mandar:
💬 "Recebi 800 do projeto do site"
💬 "Recebi 350 de aula particular"

No fim do mês, você sabe exatamente quanto entrou e de onde veio. 📊
""" + LINK, ["app", "org"],
title="Cada entrada, _registrada._",
msgs=[("u", "Recebi 800 do projeto do site"),
      card("💻", "Projeto do site", "Rendimentos · Hoje", "800,00", inc=True),
      ("u", "Recebi 350 de aula particular"),
      card("📚", "Aula particular", "Rendimentos · Hoje", "350,00", inc=True)]),

P("2027-04-09", "frase", "Enquete",
"""Enquete da sexta! 🗳️

Você já tem uma reserva de emergência?

1️⃣ Sim, completa
2️⃣ Comecei, mas ainda falta
3️⃣ Ainda não comecei

Responde com o número nos comentários. Sem julgamento: todo mundo começa de algum lugar. 💙👇
""", ["reserva", "vida"],
title="Você já tem _reserva de emergência?_",
sub="1 sim, completa · 2 comecei · 3 ainda não. Responde nos comentários! 👇"),

P("2027-04-12", "dica", "Renda variável",
"""Ganha por projeto, comissão ou como autônomo? Estas regras fazem diferença. 💼

1️⃣ Calcule sua renda média dos últimos meses
2️⃣ Pague a si mesmo um "salário" fixo todo mês
3️⃣ Nos meses bons, guarde o excedente para os meses fracos
4️⃣ Tenha uma reserva de emergência maior
5️⃣ Se tiver CNPJ, separe as contas da empresa das pessoais

Renda variável pede ainda mais organização, e mais tranquilidade quando ela está em dia.

""" + SALVE, ["org", "reserva"],
title="Renda variável: _5 regras de ouro_",
items=["Calcule sua **renda média**",
       "Pague a si mesmo um **salário fixo**",
       "Nos meses bons, **guarde o excedente**",
       "Tenha uma **reserva maior**",
       "**Separe** as contas da empresa das pessoais"]),

P("2027-04-14", "dica", "Wally na prática",
"""O Wally te avisa antes de o orçamento estourar. 🔔

Quando você define um limite para uma categoria:
🟦 A barra enche conforme você gasta
🔔 Passou de 80% do limite? O Wally te avisa no WhatsApp
🟥 Passou do limite? A barra fica vermelha

Assim você corrige a rota no meio do mês, e não só quando já é tarde. 😉
""" + LINK, ["org", "app"],
title="Um aviso _antes de estourar._",
items=["A barra **enche** conforme você gasta",
       "Passou de **80%**? O Wally **te avisa** no WhatsApp",
       "Passou do limite? A barra **fica vermelha**"]),

P("2027-04-16", "frase", "Pra pensar",
"""Sabe aquela ideia de "vou começar a me organizar mês que vem"? 🤔

O melhor dia para começar era ontem. O segundo melhor é hoje.

Não precisa de planilha perfeita nem de todos os gastos do ano. Comece registrando o que você gastar hoje. Amanhã você registra de novo.

Em 30 dias, você vai saber mais sobre o seu dinheiro do que nos últimos 12 meses. 🚀
""" + LINK, ["vida", "org"],
title="O melhor dia para começar era ontem. _O segundo melhor é hoje._"),

P("2027-04-19", "dica", "Imposto de Renda",
"""Ainda não declarou o Imposto de Renda? Fuja destes erros comuns. ⚠️

1️⃣ Deixar para a última hora
2️⃣ Esquecer algum rendimento, como freelas, aluguéis e aplicações
3️⃣ Informar despesa médica sem ter o comprovante
4️⃣ Errar os dados de dependentes
5️⃣ Não conferir a declaração pré-preenchida

Confira sempre o prazo oficial no site da Receita Federal.

Se você registrou tudo no Wally, a exportação para Excel ajuda a revisar os gastos do ano. 📥

""" + SALVE, ["ir", "org"],
title="IR: _5 erros_ para evitar",
items=["Deixar para a **última hora**",
       "Esquecer **algum rendimento**",
       "Despesa médica **sem comprovante**",
       "Errar os dados de **dependentes**",
       "Não conferir a **pré-preenchida**"]),

P("2027-04-21", "chat", "Feriado",
"""Feriado de Tiradentes! 🇧🇷

Vai pegar a estrada? Registrar os gastos da viagem pode ser tão rápido quanto mandar uma mensagem:
💬 "pedágio 23,40"
💬 "almoço na estrada 96"

Na volta, é só mandar /saldo e ver quanto custou o passeio. Bom feriado! 🚗
""" + LINK, ["app", "vida"],
title="Feriado na estrada? _Registra aí._",
msgs=[("u", "pedágio 23,40"),
      card("🛣️", "Pedágio", "Transporte · Hoje", "23,40"),
      ("u", "almoço na estrada 96"),
      card("🍽️", "Almoço na estrada", "Alimentação · Hoje", "96,00")]),

P("2027-04-23", "mito", "Mito ou verdade",
"""Mito ou verdade? 🤔

"Só vale a pena anotar os gastos grandes."

❌ MITO!

Os gastos grandes a gente lembra. São os pequenos que escapam: o cafezinho, o app de transporte, a taxa de entrega, a lojinha do celular.

Sozinhos eles parecem irrelevantes, mas juntos podem virar uma das maiores categorias do mês.

Por isso o Wally foi feito para registrar em segundos: para que valha a pena anotar até os R$ 5. ☕
""", ["org", "econ"],
title="Só vale anotar _os gastos grandes?_",
mito="Só vale a pena anotar os gastos grandes.",
verdade="São os **pequenos que escapam**. Juntos, podem virar uma das **maiores categorias** do mês."),

P("2027-04-26", "dica", "Dica de finanças",
"""5 truques para economizar no mercado. 🛒

1️⃣ Faça uma lista e siga a lista
2️⃣ Não vá com fome, é sério 😂
3️⃣ Compare o preço por quilo ou por litro, não só o da embalagem
4️⃣ Olhe as prateleiras de cima e de baixo, onde costumam ficar as opções mais baratas
5️⃣ Planeje as refeições da semana e evite desperdício

Quanto você gasta de mercado por mês? Registra no Wally por um mês e descubra. 👀

""" + SALVE, ["econ", "fam"],
title="5 truques para economizar _no mercado_",
items=["Faça uma **lista** e siga a lista",
       "**Não vá com fome**",
       "Compare o **preço por quilo ou litro**",
       "Olhe as prateleiras de **cima e de baixo**",
       "**Planeje as refeições** da semana"]),

P("2027-04-28", "comp", "Dica de finanças",
"""Guardar dinheiro "para quando der" ou para uma meta? 🎯

Quando você guarda sem objetivo, fica fácil usar o dinheiro na primeira vontade. Quando tem uma meta com nome, valor e prazo, cada depósito é um passo em direção a algo que você quer.

No Wally você cria metas e acompanha a barra de progresso a cada depósito. É muito mais motivador. 💙
""" + LINK, ["meta", "reserva"],
title="Guardar _com meta_ muda tudo",
left=("Sem meta", ["Guarda **quando sobra**", "Usa na **primeira vontade**", "Sem saber **quanto falta**"]),
right=("Com meta", ["Valor e **prazo definidos**", "Cada depósito **tem propósito**", "Progresso **visível**"])),

P("2027-04-30", "frase", "Dia do Trabalhador",
"""Amanhã é Dia do Trabalhador. 💪

Todo mês você troca horas da sua vida por um salário. Então cada real tem um valor que vai além do número: ele representa o seu tempo e o seu esforço.

Organizar o dinheiro é garantir que esse esforço vire aquilo que importa para você: segurança, sonhos, liberdade.

Bom feriado! 💙
""", ["vida"],
title="Seu dinheiro é o seu _tempo e o seu esforço._",
sub="Faça ele virar o que importa para você. Bom feriado! 💙"),

P("2027-05-03", "dica", "Primeiros passos",
"""Como montar o seu primeiro orçamento mensal. 📋

1️⃣ Some tudo o que entra no mês
2️⃣ Liste as contas fixas: aluguel, luz, internet, escola
3️⃣ Estime os gastos variáveis: mercado, transporte, lazer
4️⃣ Separe um valor para guardar
5️⃣ Compare: entradas precisam ser maiores do que as saídas

Se não fechar, ajuste primeiro os gastos variáveis.

No Wally, os orçamentos por categoria viram limites que você acompanha o mês todo. 😉

""" + SALVE, ["org", "meta"],
title="Seu primeiro _orçamento mensal_",
items=["Some **tudo o que entra**",
       "Liste as **contas fixas**",
       "Estime os **gastos variáveis**",
       "Separe um valor para **guardar**",
       "Entradas precisam ser **maiores que as saídas**"]),

P("2027-05-05", "chat", "Wally na prática",
"""Contas fixas também entram no Wally. 🏠

Pagou a luz, a internet, o condomínio? Manda para o Wally:
💬 "paguei a conta de luz 158,70"
💬 "internet 99,90"

Tudo vai para a categoria certa, e você começa a enxergar quanto as contas da casa pesam no mês.
""" + LINK, ["app", "org"],
title="Contas da casa, _sem esquecer nenhuma._",
msgs=[("u", "paguei a conta de luz 158,70"),
      card("💡", "Conta de luz", "Moradia · Hoje", "158,70"),
      ("u", "internet 99,90"),
      card("📶", "Internet", "Moradia · Hoje", "99,90")]),

P("2027-05-07", "frase", "Dia das Mães",
"""Domingo é Dia das Mães! 💐

Para quem ensinou a gente a esticar o dinheiro até o fim do mês, a fazer lista de mercado e a guardar "para uma emergência": obrigado. 💙

Dica de presente com carinho e sem apertar o orçamento: tempo junto, uma refeição feita em casa, uma carta escrita à mão. Os melhores presentes nem sempre são os mais caros.

Marca aqui a sua mãe, ou quem cumpre esse papel na sua vida! 👇
""", ["fam", "vida"],
title="Para quem ensinou a gente a _esticar o dinheiro_ até o fim do mês: obrigado. 💐",
dark=False),

P("2027-05-10", "dica", "Dica de finanças",
"""As contas fixas parecem imutáveis, mas muitas dão para reduzir. ✂️

1️⃣ Ligue para a operadora de internet e celular e pergunte por planos mais baratos
2️⃣ Revise seguros e compare com outras seguradoras
3️⃣ Confira a conta de luz: aparelhos em standby também gastam
4️⃣ Reveja o plano da academia: você usa o que paga?
5️⃣ Veja se há pacote de tarifas bancárias que você nem usa

Uma ligação de 10 minutos pode economizar dinheiro todo mês, pelo ano inteiro. 📞

""" + SALVE, ["econ", "fam"],
title="Dá para _reduzir_ as contas fixas",
items=["Negocie **internet e celular**",
       "Compare **seguros**",
       "Cuidado com o **standby**",
       "Você usa **a academia** que paga?",
       "Revise as **tarifas bancárias**"]),

P("2027-05-12", "tela", "Wally na prática",
"""Quanto sobrou este mês? 💰

No topo do painel do Wally você vê:
🟢 Receitas do mês
🔴 Despesas do mês
🔵 Economia: quanto sobrou e qual porcentagem da renda isso representa

E ainda compara com o mês anterior. Dá gosto ver a economia crescendo. 📈
""" + LINK, ["org", "reserva"],
title="Quanto _sobrou_ este mês?",
sub="Receitas, despesas e economia, com a comparação com o mês anterior.",
img="dash-top"),

P("2027-05-14", "frase", "Enquete",
"""Queremos te conhecer melhor! 💬

Qual é o seu maior desafio com dinheiro hoje?

1️⃣ Saber para onde ele vai
2️⃣ Conseguir guardar
3️⃣ Sair das dívidas
4️⃣ Resistir às compras por impulso
5️⃣ Organizar as finanças a dois

Responde com o número nos comentários. As respostas vão guiar os próximos posts! 👇
""", ["vida", "org"],
title="Qual é o seu _maior desafio_ com dinheiro?",
sub="Responde nos comentários. As respostas vão guiar os próximos posts! 👇"),

P("2027-05-17", "dica", "Finanças a dois",
"""Como dividir as contas a dois? 💑

Não existe jeito certo, e sim o jeito que funciona para vocês. As opções mais comuns:

1️⃣ Meio a meio: cada um paga 50%
2️⃣ Proporcional: cada um contribui conforme a renda
3️⃣ Conta conjunta: tudo entra numa conta só
4️⃣ Híbrido: uma conta conjunta para as despesas da casa e o restante individual

O mais importante é conversar abertamente e revisar o combinado quando a vida mudar.

Qual é o jeito de vocês? 👇

""" + SALVE, ["fam", "vida"],
title="Como dividir as contas _a dois_",
items=["**Meio a meio**: cada um paga 50%",
       "**Proporcional** à renda de cada um",
       "**Conta conjunta** para tudo",
       "**Híbrido**: conjunta para a casa, o resto individual"]),

P("2027-05-19", "dica", "Wally na prática",
"""Tem cartões com datas de fechamento diferentes? O Wally entende. 💳

Para cada cartão, você informa:
📅 O dia de fechamento
📅 O dia de vencimento

Com isso, cada compra vai automaticamente para a fatura certa, e aparece no mês em que você realmente vai pagar.

Nada de fazer conta de cabeça para saber em qual fatura aquela compra caiu. 😌
""" + LINK, ["cartao", "org"],
title="Cada compra _na fatura certa._",
items=["Informe o **dia de fechamento** de cada cartão",
       "Informe o **dia de vencimento**",
       "Cada compra vai **sozinha** para a fatura certa"]),

P("2027-05-21", "mito", "Mito ou verdade",
"""Mito ou verdade? 🤔

"Falar de dinheiro com quem a gente ama estraga o clima."

❌ MITO!

Evitar o assunto é o que costuma gerar problema: dívidas escondidas, expectativas diferentes e brigas no fim do mês.

Uma conversa sincera, sem julgamento, ajuda a:
💬 Alinhar objetivos
💬 Dividir as responsabilidades
💬 Planejar sonhos em conjunto

Que tal marcar um "encontro financeiro" com seu par? ☕💙
""", ["fam", "vida"],
title="Falar de dinheiro _estraga o clima?_",
mito="Falar de dinheiro com quem a gente ama estraga o clima.",
verdade="Evitar o assunto é que gera problema. Conversar ajuda a **alinhar objetivos** e **planejar juntos**."),

P("2027-05-24", "destaque", "Post nº 100",
"""Chegamos ao post número 100! 🎉

São 100 posts falando de dinheiro de um jeito simples, sem complicação e sem julgamento.

Obrigado a cada pessoa que curtiu, comentou, salvou, compartilhou ou só leu em silêncio. 💙

Conta aqui: qual dica daqui você já colocou em prática? 👇
""", ["vida"],
big="100",
text="posts falando de dinheiro **sem complicação**. Obrigado por estar aqui! 💙"),

P("2027-05-26", "chat", "Wally na prática",
"""Carro também é uma categoria que pesa. 🚗

Combustível, estacionamento, manutenção, seguro, IPVA… Quando você soma tudo, o custo do carro costuma surpreender.

No Wally é só mandar:
💬 "gasolina 200"
💬 "estacionamento 18"

E, nos relatórios, você vê quanto o transporte custa de verdade por mês.
""" + LINK, ["app", "org"],
title="Quanto custa _o seu carro?_",
msgs=[("u", "gasolina 200"),
      card("⛽", "Gasolina", "Transporte · Hoje", "200,00"),
      ("u", "estacionamento 18"),
      card("🅿️", "Estacionamento", "Transporte · Hoje", "18,00")]),

P("2027-05-28", "frase", "Imposto de Renda",
"""Lembrete importante: já declarou o Imposto de Renda? 📄

O prazo costuma terminar no fim de maio, mas confira a data oficial deste ano no site da Receita Federal.

Se ainda não declarou:
✅ Separe os informes e comprovantes
✅ Use a declaração pré-preenchida
✅ Revise tudo antes de enviar

Não deixe para o último minuto! ⏰
""", ["ir", "org"],
title="Já declarou o _Imposto de Renda?_",
sub="Confira o prazo oficial deste ano no site da Receita Federal. ⏰"),

P("2027-05-31", "dica", "Hábitos",
"""Como criar o hábito de registrar os gastos. 🧠

1️⃣ Registre na hora. Deixar para depois é esquecer.
2️⃣ Deixe o jeito de registrar a um toque de distância
3️⃣ Comece pelo mínimo: registre só os gastos do dia
4️⃣ Reserve 5 minutos por semana para revisar
5️⃣ Comemore as pequenas vitórias

Com o Wally no WhatsApp, registrar é tão fácil quanto mandar uma mensagem. Fica difícil esquecer. 😉

""" + SALVE, ["vida", "org"],
title="Como criar o hábito de _registrar os gastos_",
items=["**Registre na hora**",
       "Deixe o registro a **um toque** de distância",
       "Comece pelo **mínimo**",
       "**5 minutos** por semana de revisão",
       "**Comemore** as pequenas vitórias"]),

P("2027-06-02", "tela", "Wally na prática",
"""É assim que é registrar um gasto no Wally. 👇

Você manda a mensagem e, em segundos, a despesa ou receita está registrada, categorizada e aparecendo no seu painel.

Sem formulário, sem abrir app, sem esquecer. 💬

O bot do WhatsApp faz parte do plano Pro.
""" + LINK, ["app", "org"],
title="O bot _em ação._",
img="telegram", w=860),

P("2027-06-04", "frase", "Pra pensar",
"""Reflexão para a sexta-feira: 💭

Dinheiro não é o objetivo. É a ferramenta.

O objetivo é o que ele permite: tranquilidade, tempo com quem você ama, experiências, segurança para o futuro.

Organizar as finanças é sobre colocar o dinheiro a serviço da vida que você quer ter. 💙
""", ["vida"],
title="Dinheiro não é o objetivo. _É a ferramenta._"),

P("2027-06-07", "dica", "Dia dos Namorados",
"""O Dia dos Namorados está chegando! 💘 Ideias criativas e que cabem no bolso:

1️⃣ Jantar especial feito em casa, a dois
2️⃣ Piquenique no parque ao pôr do sol
3️⃣ Uma carta escrita à mão
4️⃣ Reviver o primeiro encontro
5️⃣ Uma sessão de cinema em casa, com pipoca e tudo

Se for sair, combine um valor antes e reserve com antecedência. Os preços costumam subir na data. 😉

""" + SALVE, ["fam", "econ"],
title="Dia dos Namorados _criativo e econômico_",
items=["**Jantar especial** feito em casa",
       "**Piquenique** ao pôr do sol",
       "Uma **carta escrita à mão**",
       "Reviver o **primeiro encontro**",
       "**Cinema em casa**, com pipoca e tudo"]),

P("2027-06-09", "chat", "Wally na prática",
"""O Wally fica de olho nos seus orçamentos por você. 🔔

Todo dia de manhã, ele confere suas categorias e, se alguma passar de 80% do limite, te avisa no WhatsApp:

⚠️ Seu orçamento de Lazer está em 92% do limite.

Assim você decide com calma se vale a pena gastar mais, ou se é melhor segurar até o mês que vem. 😉
""" + LINK, ["app", "org"],
title="O Wally _te avisa._",
msgs=[("wt", "☀️ Bom dia! Passando para avisar:"),
      ("wt", "⚠️ **Orçamento de Lazer**\nVocê está em **92%** do limite deste mês.\nGasto: R$ 276,00 de R$ 300,00"),
      ("u", "Valeu! Vou segurar o delivery essa semana 😅")]),

P("2027-06-11", "frase", "Dia dos Namorados",
"""Amanhã é Dia dos Namorados! 💘

E se o presente deste ano for um plano?

Sentar juntos, conversar sobre os sonhos do casal e criar uma meta a dois: a viagem, a casa, o casamento, o que for.

Amor também é construir o futuro juntos. 💙

Marca seu par aqui! 👇
""", ["fam", "meta"],
title="Amor também é _planejar juntos._ 💘",
sub="Que tal criar uma meta a dois neste Dia dos Namorados?"),

P("2027-06-14", "dica", "Festa junina",
"""Arraiá bão e barato! 🌽🔥

1️⃣ Defina quanto vai gastar na festa antes de sair de casa
2️⃣ Leve em dinheiro. O controle fica mais fácil.
3️⃣ Coma antes de ir para não exagerar nas barraquinhas
4️⃣ Numa festa entre amigos, faça tudo compartilhado: cada um leva um prato
5️⃣ Reaproveite a decoração e o traje do ano passado

Quanto você costuma gastar em festa junina? 👇
""", ["econ", "vida"],
title="Arraiá _bão e barato_ 🌽",
items=["Defina **quanto vai gastar** antes",
       "Leve em **dinheiro**",
       "**Coma antes** de ir",
       "Festa entre amigos? **Cada um leva um prato**",
       "**Reaproveite** traje e decoração"]),

P("2027-06-16", "dica", "Wally na prática",
"""Seus gastos mudam ao longo do ano, e o Wally mostra isso. 📅

Nos Relatórios, escolha o período de 12 meses e descubra:
📈 Os meses em que você mais gasta, como dezembro e janeiro
📉 Os meses mais tranquilos
🏷️ As categorias que sobem em certas épocas

Com isso, você se prepara antes: separa dinheiro para os meses pesados e aproveita os leves para guardar mais. 😉
""" + LINK, ["org", "meta"],
title="Seus gastos _ao longo do ano._",
items=["Veja os meses em que você **mais gasta**",
       "Descubra os meses **mais tranquilos**",
       "Identifique categorias que **sobem em certas épocas**"]),

P("2027-06-18", "mito", "Mito ou verdade",
"""Mito ou verdade? 🤔

"Quem organiza as finanças não pode se divertir."

❌ MITO!

Organização não é cortar tudo o que dá prazer. É decidir para onde vai o seu dinheiro, incluindo o lazer.

Quando você reserva um valor para diversão no orçamento, pode aproveitar sem culpa, porque sabe que o resto está garantido. 🎉

A diferença entre quem se diverte com e sem organização? A culpa depois. 😉
""", ["vida", "org"],
title="Quem se organiza _não se diverte?_",
mito="Quem organiza as finanças não pode se divertir.",
verdade="Com organização, o lazer entra **no orçamento**, e você aproveita **sem culpa**."),

P("2027-06-21", "dica", "Férias",
"""Férias de julho chegando? Planeje a viagem agora. ✈️

1️⃣ Defina o orçamento total: transporte, hospedagem, comida, passeios
2️⃣ Crie uma meta com esse valor
3️⃣ Pesquise e reserve com antecedência
4️⃣ Considere destinos e datas fora do pico
5️⃣ Separe uma margem para imprevistos

Viajar com o dinheiro já separado é outra viagem. 😌

""" + SALVE, ["meta", "econ"],
title="Planeje as _férias de julho_",
items=["Defina o **orçamento total**",
       "Crie uma **meta** com esse valor",
       "**Reserve** com antecedência",
       "Considere destinos e datas **fora do pico**",
       "Separe uma **margem para imprevistos**"]),

P("2027-06-23", "dica", "Wally na prática",
"""Uma meta para a viagem dos sonhos. ✈️

No Wally:
1️⃣ Crie a meta "Viagem de férias"
2️⃣ Defina o valor total e a data
3️⃣ Registre cada depósito que fizer
4️⃣ Acompanhe a barra de progresso chegando a 100%

E durante a viagem, registre os gastos pelo WhatsApp para saber exatamente quanto ela custou. 🏖️
""" + LINK, ["meta", "app"],
title="A viagem dos sonhos _vira meta._",
items=["Crie a meta **Viagem de férias**",
       "Defina o **valor total** e a **data**",
       "Registre **cada depósito**",
       "Veja a barra chegando a **100%**"]),

P("2027-06-25", "frase", "Enquete",
"""Enquete das férias! 🏖️⛰️

Se você pudesse viajar agora, com o dinheiro já guardado, para onde iria?

🏖️ Praia
⛰️ Montanha
🏙️ Cidade grande
🌎 Exterior

Comenta aqui o destino, e quanto você acha que precisaria juntar! 👇
""", ["meta", "vida"],
title="_Praia ou montanha?_ E quanto custa?",
sub="Comenta o destino dos sonhos e quanto precisaria juntar. 👇"),

P("2027-06-28", "dica", "Meio do ano",
"""Metade do ano! Hora de uma revisão rápida. ⏸️

☑️ As metas de janeiro continuam fazendo sentido?
☑️ Quanto consegui guardar até aqui?
☑️ As dívidas diminuíram?
☑️ Qual categoria mais pesou no semestre?
☑️ O que vou mudar no segundo semestre?

Seis meses é tempo suficiente para mudar muita coisa. Bora? 💪

""" + SALVE, ["meta", "org"],
title="Revisão de _meio de ano_",
style="check",
items=["As **metas** ainda fazem sentido?",
       "Quanto consegui **guardar**?",
       "As **dívidas** diminuíram?",
       "Qual categoria **mais pesou**?",
       "O que vou **mudar** no 2º semestre?"]),

P("2027-06-30", "tela", "Wally na prática",
"""Primeiro semestre fechado! 📊

Nos Relatórios do Wally, selecione 6 meses e veja o semestre inteiro de uma vez:
💰 Receita e despesa média
📊 Receitas x despesas mês a mês
📈 A evolução do seu patrimônio
🎯 Sua taxa de poupança

Como foi o seu semestre? 👇
""" + LINK, ["org", "meta"],
title="Seu semestre _em números._",
sub="Selecione 6 meses nos Relatórios e veja tudo de uma vez.",
img="rel-top"),
]
