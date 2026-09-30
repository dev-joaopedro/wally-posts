from common import P, card, LINK, SALVE

POSTS = [

P("2027-01-01", "frase", "Feliz 2027",
"""Feliz 2027! 🎆

Que este ano venha com mais tranquilidade, mais conquistas e menos sustos no fim do mês.

A gente vai estar aqui o ano todo, com dicas, ideias e o Wally cuidando da parte chata da organização.

Um brinde ao ano novo! 🥂💙
""", ["vida", "meta"],
title="Feliz _2027!_ 🎆",
sub="Mais tranquilidade, mais conquistas e menos sustos no fim do mês."),

P("2027-01-04", "dica", "Contas de janeiro",
"""IPVA, IPTU: pagar à vista ou parcelar? 🤔

Não existe resposta única, mas dá para decidir com calma:

1️⃣ Veja o desconto oferecido para pagamento à vista
2️⃣ Confira se você tem o dinheiro sem mexer na reserva de emergência
3️⃣ Se parcelar, registre cada parcela para ela não pegar você de surpresa
4️⃣ Anote as datas de vencimento. Multa por atraso anula qualquer vantagem

Regra de ouro: se pagar à vista vai te obrigar a entrar no cheque especial, parcelar costuma ser o caminho mais seguro.

""" + SALVE, ["org", "econ"],
title="IPVA e IPTU: _à vista ou parcelado?_",
items=["Veja o **desconto** para pagamento à vista",
       "Confira se dá para pagar **sem mexer na reserva**",
       "Se parcelar, **registre cada parcela**",
       "Anote os **vencimentos**: multa anula qualquer vantagem"]),

P("2027-01-06", "dica", "Wally na prática",
"""Conta corrente, carteira, cartão de crédito… tudo num lugar só. 🏦

No Wally Pro você cadastra quantas contas e cartões quiser:
💳 Cada cartão com seu dia de fechamento e vencimento
🏦 Cada conta com seu saldo
📊 Uma visão consolidada de tudo no painel

Nada de abrir 4 apps de banco para saber quanto você tem. 😉

No plano gratuito, você pode cadastrar 1 conta ou cartão.
""" + LINK, ["cartao", "org"],
title="Todas as contas e cartões _num lugar só._",
items=["Cadastre **quantas contas e cartões** quiser",
       "Cada cartão com seu **fechamento e vencimento**",
       "Uma **visão consolidada** de tudo no painel"]),

P("2027-01-08", "destaque", "Desafio",
"""Topa um desafio para 2027? 💪

O desafio das 52 semanas funciona assim:
📅 Semana 1: guarde R$ 1
📅 Semana 2: guarde R$ 2
📅 Semana 3: guarde R$ 3
…e assim por diante até a semana 52.

No fim do ano, você terá R$ 1.378 guardados, quase sem sentir no começo.

Dica: se as últimas semanas ficarem pesadas, faça o desafio ao contrário, começando por R$ 52.

Crie uma meta no Wally chamada "52 semanas" e acompanhe cada depósito. Marca aqui quem vai fazer com você! 👇
""", ["meta", "reserva"],
title="Desafio das 52 semanas",
big="R$ 1.378",
text="Guarde **R$ 1** na semana 1, **R$ 2** na semana 2… até a semana 52. É quanto você terá no fim do ano."),

P("2027-01-11", "dica", "Volta às aulas",
"""Material escolar sem estourar o orçamento. 📚

1️⃣ Veja o que dá para reaproveitar do ano passado
2️⃣ Compare preços em pelo menos 3 lojas
3️⃣ Combine compras em grupo com outros pais
4️⃣ Nem tudo precisa ser de marca ou de personagem
5️⃣ Se parcelar, veja se as parcelas cabem nos próximos meses

Dica: crie uma categoria "Educação" no Wally para acompanhar quanto o começo do ano letivo custa de verdade.

""" + SALVE, ["fam", "econ"],
title="Material escolar _sem estourar_ o orçamento",
items=["**Reaproveite** o que der do ano passado",
       "Compare preços em **pelo menos 3 lojas**",
       "Combine **compras em grupo** com outros pais",
       "Nem tudo precisa ser **de marca**",
       "Veja se as **parcelas cabem** nos próximos meses"]),

P("2027-01-13", "chat", "Wally na prática",
"""Quer saber como está o mês? Pergunta para o Wally. 📊

No Telegram, mande:
💬 /saldo para ver o resumo do mês atual
💬 /saldo 12/2026 para ver um mês específico
💬 /listar para ver e editar seus lançamentos

Em 2 segundos você sabe quanto entrou, quanto saiu e quanto sobrou, sem abrir nenhum app.
""" + LINK, ["app", "org"],
title="Seu mês _numa mensagem._",
msgs=[("u", "/saldo"),
      ("wt", "📊 **Resumo de janeiro**\nReceitas: R$ 5.200,00\nDespesas: R$ 2.870,40\nSaldo do mês: R$ 2.329,60"),
      ("u", "/saldo 12/2026"),
      ("wt", "📊 **Resumo de dezembro**\nReceitas: R$ 7.300,00\nDespesas: R$ 4.915,20\nSaldo do mês: R$ 2.384,80")]),

P("2027-01-15", "mito", "Mito ou verdade",
"""Mito ou verdade? 🤔

"Só dá para começar a guardar dinheiro quando eu ganhar mais."

❌ MITO!

Se não sobra nada hoje, um aumento tende a ser absorvido por novos gastos. É o famoso "quanto mais ganho, mais gasto".

O hábito de guardar vem antes do valor. Comece com R$ 20, R$ 50, o que for possível. O importante é que seja todo mês.

Quando o salário aumentar, você já vai ter o hábito. Aí é só aumentar o valor. 😉
""", ["reserva", "vida"],
title="Só dá para guardar _quando eu ganhar mais?_",
mito="Só dá para começar a guardar dinheiro quando eu ganhar mais.",
verdade="O **hábito vem antes do valor**. Comece com o que for possível, mas todo mês."),

P("2027-01-18", "comp", "Dica de finanças",
"""Tem mais de uma dívida? Existem dois métodos famosos para quitar. 💪

❄️ BOLA DE NEVE
Você quita primeiro a dívida de menor valor. Cada dívida eliminada dá motivação para a próxima.

🏔️ AVALANCHE
Você quita primeiro a dívida com os juros mais altos. Matematicamente, é o que economiza mais dinheiro.

Nos dois casos:
✅ Pague o mínimo de todas as outras
✅ Não faça dívidas novas enquanto isso
✅ Tente negociar os juros antes de começar

Qual combina mais com você? 👇

""" + SALVE, ["cartao", "vida"],
title="Bola de neve _ou_ avalanche?",
left_ok=True,
left=("Bola de neve", ["Quita a **menor** dívida primeiro", "Mais **motivação**", "Vitórias rápidas"]),
right=("Avalanche", ["Quita a dos **maiores juros** primeiro", "**Economiza** mais dinheiro", "Resultado no longo prazo"])),

P("2027-01-20", "tela", "Wally na prática",
"""Cada gasto no seu lugar. 🧾

No Wally, todas as transações ficam organizadas com:
🏷️ Categoria e ícone
📅 Data, com "Hoje" e "Ontem" para facilitar
💰 Valor, com despesas e receitas bem separadas

E, do lado, o card Quanto posso gastar mostra o que ainda cabe no mês.

Registrou pelo Telegram? Aparece aqui na hora. ⚡
""" + LINK, ["org", "app"],
title="Cada gasto _no seu lugar._",
sub="Transações organizadas e, ao lado, quanto ainda cabe no mês.",
img="dash-bottom"),

P("2027-01-22", "frase", "Pra pensar",
"""Janeiro está passando voando. E as metas para 2027? 🎯

Conta aqui nos comentários qual é a sua principal meta financeira para este ano:

✈️ Viajar
🛟 Montar a reserva de emergência
💳 Sair das dívidas
🏠 Juntar para a entrada da casa
🚗 Trocar de carro
📈 Começar a investir

Escrever a meta já é o primeiro passo. 👇
""", ["meta", "vida"],
title="Qual é a sua _meta financeira_ para 2027?",
sub="Escreve aqui nos comentários. Tornar pública ajuda a cumprir. 👇"),

P("2027-01-25", "dica", "Dica de finanças",
"""Já ouviu falar em orçamento base zero? 🧮

A ideia é dar uma função para cada real que entra, até sobrar zero sem destino.

Como fazer:
1️⃣ Anote tudo o que vai entrar no mês
2️⃣ Distribua cada real: contas, mercado, lazer, reserva, investimentos
3️⃣ Receita menos destinos tem que dar zero
4️⃣ Acompanhe durante o mês e ajuste quando precisar

"Zero" não significa gastar tudo. Guardar também é um destino. 😉

No Wally, os orçamentos por categoria ajudam a colocar esse plano em prática.

""" + SALVE, ["org", "meta"],
title="Orçamento _base zero_",
sub="Dê uma função para cada real que entra.",
items=["Anote tudo o que **vai entrar** no mês",
       "**Distribua cada real**: contas, lazer, reserva…",
       "Receita menos destinos **tem que dar zero**",
       "**Guardar também é destino**. Zero não é gastar tudo"]),

P("2027-01-27", "dica", "Wally na prática",
"""As categorias do Wally são suas. 🏷️

Quando você cria a conta, o Wally já traz as categorias mais comuns, como Alimentação, Transporte, Moradia e Saúde. Mas você pode:

✏️ Renomear qualquer uma
➕ Criar novas, como Pet, Filhos ou Freelas
🎨 Escolher a cor de cada uma

Assim os relatórios mostram exatamente o que importa para a sua vida. 💙
""" + LINK, ["org", "app"],
title="Categorias com _a sua cara._",
items=["O Wally já começa com as **categorias mais comuns**",
       "**Renomeie** ou **crie novas**: Pet, Filhos, Freelas…",
       "Escolha a **cor** de cada uma"]),

P("2027-01-29", "dica", "Checklist",
"""Fim de mês é hora de um ritual rápido: 5 minutos de revisão. ⏱️

☑️ Registrei todos os gastos do mês?
☑️ Em qual categoria gastei mais?
☑️ Estourei algum orçamento?
☑️ Consegui guardar alguma coisa?
☑️ O que vou ajustar no mês que vem?

Com o Wally, as respostas estão no painel e nos relatórios. Você só precisa olhar e decidir. 😉

""" + SALVE, ["org", "meta"],
title="Revisão do mês _em 5 minutos_",
style="check",
items=["Registrei **todos os gastos**?",
       "Em qual categoria **gastei mais**?",
       "Estourei algum **orçamento**?",
       "Consegui **guardar** alguma coisa?",
       "O que vou **ajustar** no próximo mês?"]),

P("2027-02-01", "destaque", "Dica de finanças",
"""Pague-se primeiro. 💰

A maioria das pessoas faz assim:
Salário ➡️ gastos ➡️ guarda o que sobrar (quase nunca sobra 😅)

O jeito que funciona:
Salário ➡️ guarda primeiro ➡️ vive com o resto

Quando o salário cair, separe logo o valor que você quer guardar, como se fosse uma conta a pagar. O que fica é o que você tem para o mês.

Pode começar com 5% ou 10% da renda. O importante é ser automático.
""", ["reserva", "vida"],
title="Salário caiu?",
big="_Pague-se_ primeiro.",
text="Separe o que vai guardar **antes** de gastar, como se fosse uma conta. O que sobrar é o que você tem para o mês."),

P("2027-02-03", "chat", "Wally na prática",
"""Não sabe em qual categoria colocar? A IA escolhe por você. 🤖

Você manda:
💬 "farmácia 62,30"
💬 "netflix 39,90"

E o Wally entende que farmácia é Saúde e Netflix é Entretenimento, sem você precisar escolher nada.

Tudo registrado, categorizado e pronto para aparecer nos seus relatórios. ✨
""" + LINK, ["app", "org"],
title="A IA _escolhe a categoria._",
msgs=[("u", "farmácia 62,30"),
      card("💊", "Farmácia", "Saúde · Hoje", "62,30"),
      ("u", "netflix 39,90"),
      card("🎬", "Netflix", "Entretenimento · Hoje", "39,90")]),

P("2027-02-05", "dica", "Carnaval",
"""O Carnaval está chegando! 🎉 Bora curtir sem ressaca financeira?

1️⃣ Defina um teto de gastos para os dias de folia
2️⃣ Leve o valor em dinheiro ou use um cartão pré-pago
3️⃣ Combine a divisão de gastos com a galera antes
4️⃣ Hidrate-se com água: ela é barata 😂
5️⃣ Registre os gastos para não levar susto na quarta-feira

Crie um orçamento "Carnaval" no Wally e acompanhe quanto do teto já foi. 🎭

""" + SALVE, ["econ", "vida"],
title="Carnaval _sem ressaca_ financeira",
items=["Defina um **teto de gastos** para a folia",
       "Leve o valor em **dinheiro** ou use um **pré-pago**",
       "Combine a **divisão** com a galera antes",
       "**Registre os gastos** para não se assustar na quarta"]),

P("2027-02-08", "frase", "Carnaval",
"""Bom Carnaval! 🎊🎭

Aproveite a folia, curta com quem você gosta e lembre do teto de gastos combinado. 😉

A gente volta na quarta-feira. 💙
""", ["vida"],
title="Bom _Carnaval!_ 🎭",
sub="Curta muito e não esqueça do teto de gastos combinado. 😉",
dark=False),

P("2027-02-10", "chat", "Wally na prática",
"""Quarta-feira de cinzas: hora de conferir o estrago. 😅

Se você registrou os gastos durante a folia, agora é só perguntar para o Wally:
💬 /saldo

E se esqueceu de algum, dá tempo de lançar agora:
💬 "bloco sábado 80 reais"

Sem susto quando a fatura chegar. 🎭
""" + LINK, ["app", "org"],
title="Quarta-feira de cinzas: _confere aí._",
msgs=[("u", "bloco sábado 80 reais"),
      card("🎭", "Bloco de sábado", "Lazer · Hoje", "80,00"),
      ("u", "/saldo"),
      ("wt", "📊 **Resumo de fevereiro**\nReceitas: R$ 5.200,00\nDespesas: R$ 1.948,70\nSaldo do mês: R$ 3.251,30")]),

P("2027-02-12", "mito", "Mito ou verdade",
"""Mito ou verdade? 🤔

"Cartão de crédito é um vilão."

❌ MITO!

O cartão é uma ferramenta. Usado com controle, ele organiza os gastos numa fatura só, dá prazo para pagar e pode render pontos ou cashback.

O problema começa quando:
⚠️ A fatura vira uma segunda renda
⚠️ Você paga só o mínimo
⚠️ Você perde a noção de quanto já gastou

O vilão é o descontrole, não o cartão. 😉
""", ["cartao", "vida"],
title="Cartão de crédito é _vilão?_",
mito="Cartão de crédito é um vilão e deve ser evitado.",
verdade="O cartão é uma ferramenta. **O vilão é o descontrole**, como pagar só o mínimo ou perder a noção do que gastou."),

P("2027-02-15", "dica", "Dica de finanças",
"""5 regras para usar o cartão de crédito a seu favor. 💳

1️⃣ Pague sempre a fatura inteira, nunca só o mínimo
2️⃣ Trate o limite como teto de emergência, não como renda
3️⃣ Acompanhe os gastos durante o mês, não só quando a fatura chega
4️⃣ Saiba o dia de fechamento: compras logo depois dele dão mais prazo
5️⃣ Evite ter cartões demais, porque fica difícil controlar

No Wally, cada compra aparece no mês em que a fatura vence, e você vê o total antes de a fatura fechar.

""" + SALVE, ["cartao", "org"],
title="5 regras para o cartão _jogar a seu favor_",
items=["Pague sempre a **fatura inteira**",
       "Limite é **teto**, não renda",
       "Acompanhe os gastos **durante o mês**",
       "Conheça o **dia de fechamento**",
       "Evite ter **cartões demais**"]),

P("2027-02-17", "dica", "Segurança",
"""Seus dados estão seguros no Wally. 🔒

✅ O Wally não pede acesso à sua conta bancária. Você registra só o que quiser.
✅ Senhas guardadas com criptografia forte, nunca em texto puro
✅ Verificação em duas etapas opcional, com código por e-mail
✅ Proteção contra tentativas repetidas de login

Suas finanças são suas. Nossa parte é proteger. 💙
""" + LINK, ["org", "app"],
title="Seus dados _seguros._",
style="check",
items=["**Sem acesso** à sua conta bancária",
       "Senhas com **criptografia forte**",
       "**Verificação em duas etapas** opcional",
       "**Proteção** contra tentativas repetidas de login"]),

P("2027-02-19", "frase", "Enquete",
"""Enquete rápida! 🗳️

Quando você compra algo mais caro, você prefere:

1️⃣ Pagar à vista, de preferência com desconto
2️⃣ Parcelar sem juros e deixar o dinheiro rendendo
3️⃣ Depende da compra

Responde com o número nos comentários e conta o porquê. Vamos ver qual time ganha! 👇
""", ["compras", "vida"],
title="À vista _ou_ parcelado?",
sub="Responde nos comentários: 1 à vista, 2 parcelado, 3 depende. 👇"),

P("2027-02-22", "dica", "Dica de finanças",
"""Hora de fazer uma faxina nas assinaturas. 🧹

Streaming, música, aplicativos, academia, clube de assinatura… Uma por uma parece barata, mas juntas podem pesar bastante.

1️⃣ Liste todas as assinaturas. Olhe a fatura do cartão.
2️⃣ Marque as que você usou no último mês
3️⃣ Cancele as que não usou
4️⃣ Veja se dá para dividir planos família
5️⃣ Reveze: um mês um streaming, no outro mês outro

Quanto você gasta por mês com assinaturas? Chuta aí! 👇

""" + SALVE, ["econ", "org"],
title="Faça uma _faxina_ nas assinaturas",
items=["**Liste todas**: confira a fatura do cartão",
       "Marque as que **usou no último mês**",
       "**Cancele** as que não usou",
       "Divida **planos família**",
       "**Reveze** os streamings a cada mês"]),

P("2027-02-24", "tela", "Wally na prática",
"""Gastou mais ou menos do que no mês passado? 📊

A comparação mensal do Wally mostra, categoria por categoria:
📏 Quanto você gastou este mês e no anterior
📉 Onde você economizou
📈 Onde os gastos subiram

É o jeito mais rápido de perceber se aquele esforço para economizar está funcionando. 💪
""" + LINK, ["org", "app"],
title="Compare _mês a mês._",
sub="Veja, categoria por categoria, onde os gastos subiram ou caíram.",
img="comparacao", w=800),

P("2027-02-26", "cta", "Plano Pro",
"""Já pensou em registrar seus gastos sem abrir nenhum app? 🤖

Com o Wally Pro você manda uma mensagem no Telegram e pronto:
💬 "mercado 187,40"
✅ Registrado e categorizado

E ainda tem:
💳 Várias contas e cartões
📊 Relatórios avançados
📥 Exportação para Excel
⭐ Suporte prioritário

Tudo por R$ 19,90 por mês. Se desistir em até 7 dias, o cancelamento é imediato.
""" + LINK, ["app", "org"],
title="Registre gastos _sem abrir app nenhum._",
price=True,
feats=["Bot com IA no Telegram", "Várias contas e cartões", "Relatórios avançados", "Exportação para Excel"],
button="Assinar o Pro"),

P("2027-03-01", "dica", "Imposto de Renda",
"""A temporada do Imposto de Renda está chegando. Comece a separar os documentos! 📂

☑️ Informes de rendimentos do trabalho e dos bancos
☑️ Recibos de despesas médicas e de plano de saúde
☑️ Comprovantes de gastos com educação
☑️ Documentos de compra e venda de bens
☑️ A declaração do ano passado

O prazo de entrega costuma ir de março a maio. Confira as datas oficiais no site da Receita Federal.

Quem se organiza antes declara com calma e evita erro. 😉

""" + SALVE, ["ir", "org"],
title="IR: comece a _separar os documentos_",
style="check",
items=["**Informes de rendimentos** do trabalho e dos bancos",
       "Recibos de **saúde** e plano de saúde",
       "Comprovantes de **educação**",
       "Documentos de **compra e venda** de bens",
       "A **declaração** do ano passado"]),

P("2027-03-03", "dica", "Wally na prática",
"""Todos os seus lançamentos em uma planilha, com um clique. 📥

No Wally Pro você exporta suas transações para Excel:
1️⃣ Escolha o período
2️⃣ Clique em exportar
3️⃣ Pronto: data, descrição, categoria, conta e valor, tudo organizado

Perfeito para revisar os gastos com saúde e educação na hora do Imposto de Renda, ou para quem gosta de fazer as próprias análises. 📊
""" + LINK, ["ir", "app"],
title="Exporte para Excel _com um clique._",
items=["Escolha o **período**",
       "Clique em **exportar**",
       "Receba tudo **organizado**: data, categoria, conta e valor"]),

P("2027-03-05", "frase", "Pra pensar",
"""Um lembrete para a sua sexta-feira: 💙

Organizar o dinheiro não é sobre ser perfeito. É sobre ser constante.

Vai ter mês que você vai esquecer de registrar tudo. Vai ter mês que o orçamento vai estourar. Tudo bem.

O que muda o jogo é voltar no dia seguinte. 🚀

Bom fim de semana!
""", ["vida"],
title="Não é sobre ser perfeito. _É sobre ser constante._",
dark=False),

P("2027-03-08", "dica", "Dia da Mulher",
"""Dia Internacional da Mulher. 💜

Hoje o assunto é autonomia financeira, a liberdade de tomar decisões com segurança.

4 passos importantes:
1️⃣ Tenha uma conta e uma reserva no seu nome
2️⃣ Conheça as finanças da casa: renda, contas e dívidas
3️⃣ Participe das decisões financeiras importantes
4️⃣ Invista em você: conhecimento é o melhor investimento

Marca aqui uma mulher que te inspira! 👇
""", ["vida", "reserva"],
title="Autonomia financeira _também é liberdade._",
items=["Tenha **conta e reserva** no seu nome",
       "Conheça as **finanças da casa**",
       "Participe das **decisões** importantes",
       "**Invista em você**"]),

P("2027-03-10", "tela", "Wally na prática",
"""Onde está indo o seu dinheiro? O gráfico responde. 🍩

Nos Relatórios do Wally, os gastos por categoria aparecem num gráfico com a porcentagem de cada uma.

É só bater o olho para descobrir:
🔍 Qual categoria pesa mais
🔍 Se aquele "gastinho" virou um gastão
🔍 Onde vale a pena ajustar primeiro
""" + LINK, ["org", "app"],
title="Seus gastos _num gráfico._",
sub="A porcentagem de cada categoria no total do mês.",
img="rel-cat"),

P("2027-03-12", "mito", "Mito ou verdade",
"""Mito ou verdade? 🤔

"Só quem ganha muito precisa se preocupar com o Imposto de Renda."

❌ MITO!

A obrigação de declarar não depende só do salário. As regras levam em conta vários critérios, como rendimentos, bens e outras situações.

Além disso, muita gente que não é obrigada pode ter imposto a restituir ao declarar.

Na dúvida, confira as regras deste ano no site oficial da Receita Federal. 😉
""", ["ir", "vida"],
title="IR é só para _quem ganha muito?_",
mito="Só quem ganha muito precisa se preocupar com o Imposto de Renda.",
verdade="A obrigação considera **vários critérios**, não só o salário. Confira as regras no site da Receita Federal."),

P("2027-03-15", "dica", "Dia do Consumidor",
"""Hoje é Dia do Consumidor! 🛒

Além das promoções, é um bom dia para lembrar de alguns direitos garantidos pelo Código de Defesa do Consumidor:

1️⃣ Comprou fora da loja física, como pela internet? Você tem 7 dias para se arrepender.
2️⃣ O preço anunciado deve ser respeitado.
3️⃣ Produto com defeito: você tem prazo para reclamar, 30 dias para não duráveis e 90 para duráveis.

E sobre as promoções de hoje: lembra da regra das 72h? 😉

""" + SALVE, ["compras", "vida"],
title="Seus direitos _de consumidor_",
items=["Compra fora da loja física: **7 dias** para se arrepender",
       "O **preço anunciado** deve ser respeitado",
       "Defeito: **30 dias** (não duráveis) ou **90 dias** (duráveis) para reclamar"]),

P("2027-03-17", "chat", "Wally na prática",
"""Registrou errado? Sem problema. ✏️

No Telegram, mande /listar e o Wally mostra seus últimos lançamentos. Dali você escolhe qual quer editar ou apagar.

Você também pode ver um mês específico:
💬 /listar 02/2027

E, se preferir, dá para ajustar tudo pelo app também. 😉
""" + LINK, ["app", "org"],
title="Errou? _É só editar._",
msgs=[("u", "/listar"),
      ("wt", "🧾 **Seus lançamentos de março**\n1. Mercado · − R$ 187,40\n2. Uber · − R$ 22,90\n3. Salário · + R$ 5.200,00\n\nToque em um lançamento para editar ou apagar.")]),

P("2027-03-19", "frase", "Pra pensar",
"""Pergunta para você que já registra os gastos: 🧐

Qual categoria mais te surpreendeu quando você começou a acompanhar?

🍔 Delivery?
☕ Cafezinho?
🛍️ Compras online?
🚗 Transporte por aplicativo?

Conta aqui! Aposto que muita gente vai se identificar. 👇
""", ["org", "vida"],
title="Qual categoria mais _te surpreendeu?_",
sub="Conta aqui nos comentários. Aposto que muita gente vai se identificar. 👇"),

P("2027-03-22", "comp", "Dica de finanças",
"""Reserva de emergência e dinheiro para objetivos não são a mesma coisa. ⚠️

🛟 RESERVA DE EMERGÊNCIA
É para imprevistos: perda de renda, saúde, consertos urgentes. Precisa estar sempre disponível e em lugar seguro.

🎯 DINHEIRO PARA OBJETIVOS
É para planos: viagem, carro, reforma. Tem data e valor definidos.

Misturar os dois é perigoso: você usa a reserva na viagem e fica sem proteção quando o imprevisto chega.

No Wally, crie metas separadas para cada um. 😉
""", ["reserva", "meta"],
title="Reserva _x_ objetivos",
left_ok=True,
left=("Reserva", ["Para **imprevistos**", "Sempre **disponível**", "Sem data para usar"]),
right=("Objetivos", ["Para **planos**", "Tem **valor e prazo**", "Viagem, carro, reforma"])),

P("2027-03-24", "dica", "Wally na prática",
"""O Wally cabe no seu bolso. 📱

Pelo navegador do celular você tem o app completo:
📊 Painel com saldo e gráficos
➕ Botão rápido para nova transação
🧭 Menu na parte de baixo da tela, fácil de alcançar com o polegar
🌙 Modo claro, escuro ou automático

E, com o bot do Telegram, registrar um gasto é tão rápido quanto mandar uma mensagem.
""" + LINK, ["app", "org"],
title="O Wally _no seu bolso._",
items=["Funciona completo no **navegador do celular**",
       "**Botão rápido** para nova transação",
       "Menu **fácil de alcançar** com o polegar",
       "Modo **claro, escuro** ou automático"]),

P("2027-03-26", "frase", "Pra pensar",
"""Já se passaram 3 meses de 2027. ⏳

Hora de uma checagem rápida:
🎯 As metas de janeiro ainda estão de pé?
💰 Você está conseguindo guardar alguma coisa?
📊 Algum gasto saiu do controle?

Se não estiver tudo perfeito, tudo bem. Ainda tem 9 meses pela frente para ajustar a rota. 💪
""", ["meta", "vida"],
title="3 meses de 2027. _Como estão as metas?_",
sub="Ainda tem 9 meses pela frente para ajustar a rota. 💪"),

P("2027-03-29", "dica", "Dica de finanças",
"""Como negociar uma dívida. 🤝

1️⃣ Saiba exatamente quanto você deve e a quem
2️⃣ Descubra quanto cabe no seu orçamento por mês, com folga
3️⃣ Procure o credor e pergunte pelas condições. Muitas vezes há desconto para quitar.
4️⃣ Nunca aceite uma parcela que você não consegue pagar
5️⃣ Peça tudo por escrito antes de pagar

Fique de olho nos mutirões de negociação e canais oficiais dos próprios credores. 😉

""" + SALVE, ["cartao", "vida"],
title="Como _negociar_ uma dívida",
items=["Saiba **quanto deve** e a quem",
       "Descubra **quanto cabe** por mês, com folga",
       "Procure o credor: pode haver **desconto para quitar**",
       "Nunca aceite parcela que **não cabe**",
       "Peça tudo **por escrito**"]),

P("2027-03-31", "tela", "Wally na prática",
"""Fechou o primeiro trimestre? Hora de olhar os números. 📈

Nos Relatórios do Wally, escolha o período de 3 meses e veja:
💰 Receita e despesa média
📊 Receitas x despesas mês a mês
📈 Evolução do patrimônio
🎯 Taxa de poupança

Dá para trocar para 6 ou 12 meses e comparar com períodos maiores.
""" + LINK, ["org", "meta"],
title="Seu trimestre _em números._",
sub="Receitas, despesas e patrimônio dos últimos 3, 6 ou 12 meses.",
img="rel-top"),
]
