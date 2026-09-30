from common import P, card, LINK, SALVE

POSTS = [

P("2026-10-05", "frase", "Prazer, Wally",
"""Prazer, eu sou o Wally! 👋

Nasci para resolver um problema que quase todo mundo tem: saber para onde o dinheiro está indo sem perder horas com planilhas.

Comigo funciona assim:
💬 Você manda uma mensagem no Telegram, tipo "gastei 35 no almoço"
🤖 A IA entende, categoriza e registra na hora
📊 Tudo aparece no seu painel, com gráficos, orçamentos e metas

Por aqui você vai encontrar dicas de finanças, truques para economizar e o Wally na prática.

Segue o perfil e vem organizar o dinheiro com a gente.
""" + LINK, ["org", "app"],
title="Seu dinheiro sob controle, _sem esforço nenhum._",
sub="Conheça o Wally: o app que organiza suas finanças a partir de uma simples mensagem."),

P("2026-10-07", "chat", "Wally na prática",
"""Registrar um gasto nunca foi tão rápido. ⚡

Nada de abrir app, escolher categoria e preencher formulário. No Wally você só manda uma mensagem no Telegram, do jeito que você falaria com um amigo:

💬 "Gastei 35 reais no almoço"
💬 "Recebi 2200 de freela hoje"

A IA entende o valor, identifica se é gasto ou receita, escolhe a categoria e salva. Você recebe a confirmação na hora, e tudo já aparece no seu painel.

Menos de 5 segundos por lançamento. Assim fica fácil manter o controle todo dia.

O bot do Telegram faz parte do plano Pro.
""" + LINK, ["app", "org"],
title="Mandou, _registrou._",
msgs=[("u", "Gastei 35 reais no almoço"),
      card("🍔", "Almoço", "Alimentação · Hoje", "35,00"),
      ("u", "Recebi 2200 de freela hoje"),
      card("💼", "Freelance", "Rendimentos · Hoje", "2.200,00", inc=True)]),

P("2026-10-09", "tela", "Wally na prática",
"""Seu mês inteiro em uma tela. 📊

No painel do Wally você vê de cara:
✅ Seu saldo atual e a comparação com o mês anterior
✅ Quanto entrou, quanto saiu e quanto sobrou
✅ O fluxo de receitas e despesas dos últimos 6 meses
✅ Para onde foi cada real, separado por categoria

Nada de juntar extrato, somar na calculadora ou montar gráfico na mão. Você registra e o Wally organiza.

E o painel está no plano gratuito. 😉
""" + LINK, ["org", "app"],
title="Tudo o que importa, _num painel só._",
img="dash-top"),

P("2026-10-12", "dica", "Dia das Crianças",
"""Feliz Dia das Crianças! 🧸

Que tal um presente que dura a vida toda? Aprender a lidar com dinheiro desde cedo faz muita diferença lá na frente.

Algumas ideias para começar:
1️⃣ Dê uma mesada fixa, com dia certo, adequada à idade
2️⃣ Use três potinhos: um para gastar, um para guardar e um para doar
3️⃣ Deixe a criança escolher e, às vezes, errar. Faz parte do aprendizado
4️⃣ Mostre como você compara preços no mercado

Educação financeira começa pelo exemplo. 💙

Você recebia mesada quando era criança? Conta aqui nos comentários!
""", ["fam", "vida"],
title="Ensinar dinheiro também é _presente._",
items=["Dê uma **mesada fixa**, com dia certo e valor adequado à idade",
       "Use **3 potinhos**: gastar, guardar e doar",
       "Deixe a criança **escolher e errar**. Faz parte do aprendizado",
       "Mostre como você **compara preços** no mercado"]),

P("2026-10-14", "dica", "Primeiros passos",
"""Começar a organizar as finanças leva menos de 3 minutos. ⏱️

1️⃣ Crie sua conta grátis. Não pede cartão de crédito.
2️⃣ Cadastre sua conta ou cartão principal.
3️⃣ Registre seu primeiro gasto, pelo app ou pelo Telegram no plano Pro.

Pronto! A partir daí o Wally organiza tudo em categorias e mostra no painel para onde está indo o seu dinheiro.

O segredo não é fazer tudo perfeito no primeiro dia. É começar. 🚀
""" + LINK, ["org", "app"],
title="Comece em _3 passos._",
items=["**Crie sua conta grátis.** Não pede cartão de crédito",
       "**Cadastre** sua conta ou cartão principal",
       "**Registre** seu primeiro gasto e veja o painel ganhar vida"]),

P("2026-10-16", "mito", "Mito ou verdade",
"""Mito ou verdade? 🤔

"Controlar gastos é coisa de quem ganha pouco."

❌ MITO!

Organização financeira não tem a ver com o tamanho do salário, e sim com o que você faz com ele. Tem muita gente com renda alta que vive no aperto, porque o padrão de vida cresce junto com o salário.

Saber para onde vai cada real é o que permite fazer escolhas: viajar, trocar de carro, montar uma reserva ou simplesmente dormir tranquilo.

Você já acreditou nesse mito? 👇
""", ["org", "vida"],
title="Controlar gastos é coisa de _quem ganha pouco?_",
mito="Só precisa controlar gastos quem ganha pouco.",
verdade="Quanto mais você ganha, mais fácil é o dinheiro **escapar sem você perceber**. Controle é para todo mundo."),

P("2026-10-19", "destaque", "Dica de finanças",
"""Já ouviu falar da regra 50-30-20? 📐

É um jeito simples de dividir o que você ganha:

🏠 50% para necessidades: aluguel, contas, mercado, transporte
🎉 30% para desejos: lazer, restaurantes, compras
💰 20% para o futuro: reserva de emergência, investimentos, quitar dívidas

Não precisa seguir à risca. Os números servem de ponto de partida para você ajustar à sua realidade.

No Wally você acompanha quanto está indo para cada categoria e percebe rapidinho se algum lado está pesando demais.

""" + SALVE, ["org", "reserva"],
big="50·30·20",
text="**50%** necessidades · **30%** desejos · **20%** futuro. Um ponto de partida simples para dividir o que você ganha."),

P("2026-10-21", "tela", "Wally na prática",
""""Quanto eu ainda posso gastar este mês?" 🤔

Essa é a pergunta que o card Quanto posso gastar responde por você.

O Wally olha para os seus orçamentos e para o que você já gastou e mostra:
💰 Quanto ainda sobra no mês
📅 Quanto dá para gastar por dia até o fim do mês
📏 Uma barra de quanto do limite você já usou

É o jeito mais simples de não chegar no fim do mês no vermelho.
""" + LINK, ["org", "app"],
title="Quanto posso gastar _hoje?_",
sub="O Wally faz a conta por você, com o valor disponível por dia até o fim do mês.",
img="posso-gastar", w=720),

P("2026-10-23", "frase", "Pra pensar",
"""Pergunta sincera: você sabe quanto gastou com delivery este mês? 🛵

A maioria das pessoas chuta um valor bem menor do que o real. Pedidos pequenos, taxa de entrega e gorjeta vão se somando sem a gente perceber.

Não é para cortar o delivery. É para decidir com consciência se ele merece esse espaço no seu orçamento.

Responde aqui: quanto você acha que gastou? Depois confere e conta se chegou perto. 👇
""", ["econ", "org"],
title="Você sabe quanto gastou com _delivery_ este mês?",
sub="Chute um valor e depois confira. A diferença costuma surpreender."),

P("2026-10-26", "dica", "Dica de finanças",
"""Os gastos invisíveis são os que mais pesam no fim do mês. 👻

Eles são pequenos, frequentes e passam despercebidos:

1️⃣ Assinaturas que você nem usa mais
2️⃣ Tarifas bancárias e anuidade de cartão
3️⃣ Delivery e taxas de entrega
4️⃣ O cafezinho e o lanche de todo dia
5️⃣ Juros de parcelamento e de atraso

Um bom exercício: registre tudo durante 30 dias, até os gastos de R$ 5. No fim do mês, olhe as categorias e veja o que te surpreendeu.

Com o Wally no Telegram, registrar um cafezinho leva 3 segundos. ☕

""" + SALVE, ["econ", "org"],
title="5 gastos _invisíveis_ que pesam no mês",
items=["**Assinaturas** que você nem usa mais",
       "**Tarifas** bancárias e anuidade de cartão",
       "**Delivery** e taxas de entrega",
       "O **cafezinho** e o lanche de todo dia",
       "**Juros** de parcelamento e de atraso"]),

P("2026-10-28", "chat", "Wally na prática",
"""Não precisa decorar nenhum formato. 😌

Você escreve do seu jeito e a IA do Wally entende:
💬 "uber 15,50"
💬 "padaria pão de ouro 20 reais"
💬 "academia mensal 89.90"

Vírgula, ponto, com "reais" ou sem, tanto faz. O Wally identifica valor, descrição e categoria e registra tudo certinho.

E se quiser conferir o mês, é só mandar /saldo. 📊
""" + LINK, ["app", "org"],
title="Escreva _do seu jeito._",
msgs=[("u", "uber 15,50"),
      card("🚗", "Uber", "Transporte · Hoje", "15,50"),
      ("u", "academia mensal 89.90"),
      card("🏋️", "Academia", "Saúde · Hoje", "89,90")]),

P("2026-10-30", "comp", "Planilha x Wally",
"""Planilha ou Wally? 🥊

A planilha funciona, até o dia em que você esquece de atualizar. E aí vira aquele arquivo abandonado no Drive. 😅

No Wally:
✅ Você registra por mensagem, em segundos
✅ A categoria é escolhida automaticamente
✅ Gráficos e relatórios ficam prontos sozinhos
✅ Você acompanha tudo pelo celular

Qual você usa hoje? Conta aqui! 👇
""", ["org", "app"],
title="Planilha _x_ Wally",
left=("Planilha", ["Abrir o arquivo toda vez", "Categorizar na mão", "Montar gráfico sozinho", "Esquecer de atualizar"]),
right=("Wally", ["Registrar por mensagem", "Categoria automática", "Gráficos prontos", "Tudo no celular"])),

P("2026-11-02", "dica", "Dica de finanças",
"""Reserva de emergência: por onde começar? 🛟

Ela é o dinheiro que te protege dos imprevistos, como um conserto do carro, um problema de saúde ou a perda do emprego, sem precisar recorrer a empréstimo ou cheque especial.

Passo a passo:
1️⃣ Descubra seu custo de vida mensal
2️⃣ Defina um alvo. É comum mirar de 3 a 6 meses de custo de vida
3️⃣ Comece pequeno: separar um valor fixo todo mês já conta
4️⃣ Deixe o dinheiro num lugar seguro e com resgate rápido

No Wally você cria uma meta de reserva e acompanha o progresso a cada depósito. 🎯

""" + SALVE, ["reserva", "meta"],
title="Reserva de emergência: _por onde começar_",
items=["Descubra seu **custo de vida** mensal",
       "Defina um alvo: é comum mirar em **3 a 6 meses** desse custo",
       "Comece pequeno: **um valor fixo todo mês** já conta",
       "Guarde num lugar **seguro e com resgate rápido**"]),

P("2026-11-04", "dica", "Wally na prática",
"""Sabe aquela compra no cartão que "some" do controle? 💳

No Wally, cada compra no cartão de crédito conta no mês em que você paga a fatura, e não no mês em que passou o cartão.

Exemplo:
🛒 Compra no dia 23/09
📅 Fatura vence em 05/10
➡️ No Wally, ela entra nas contas de outubro

Assim seu painel mostra o dinheiro que realmente sai da conta em cada mês. E, na lista de transações, as compras aparecem agrupadas por fatura, com a data real de cada uma.
""" + LINK, ["cartao", "org"],
title="Compra no cartão conta _no mês que você paga._",
items=["Você compra no dia **23/09**",
       "A fatura vence em **05/10**",
       "No Wally, a compra entra nas contas de **outubro**, o mês em que o dinheiro sai de verdade"]),

P("2026-11-06", "cta", "Plano Pro",
"""Conheça o Wally Pro. 💙

Por R$ 19,90 por mês você desbloqueia tudo:
🤖 Bot com IA no Telegram, para registrar gastos por mensagem
💳 Várias contas e cartões numa visão só
📊 Relatórios avançados
📥 Exportação para Excel, uma mão na roda no Imposto de Renda
⭐ Suporte prioritário

Não quer assinar agora? Sem problema: o plano gratuito tem painel completo, histórico e relatórios básicos.

Se assinar e desistir em até 7 dias, o cancelamento é imediato.
""" + LINK, ["app", "org"],
title="Tudo o que o Wally faz, _por R$ 19,90._",
price=True,
feats=["Bot com IA no Telegram", "Várias contas e cartões", "Relatórios avançados", "Exportação para Excel"],
button="Assinar o Pro"),

P("2026-11-09", "dica", "Black Friday",
"""A Black Friday está chegando, e o melhor momento para se preparar é agora. 🛍️

1️⃣ Faça uma lista do que você realmente precisa
2️⃣ Defina um valor máximo e não passe dele
3️⃣ Anote os preços de hoje para comparar no dia
4️⃣ Pesquise a reputação da loja antes de comprar
5️⃣ Veja se as parcelas cabem nos próximos meses

Desconto bom é o de algo que você já ia comprar. Compra por impulso com desconto continua sendo compra por impulso. 😉

""" + SALVE, ["compras", "econ"],
title="Black Friday: _planeje antes._",
items=["Faça uma **lista** do que você realmente precisa",
       "Defina um **valor máximo** e não passe dele",
       "**Anote os preços** de hoje para comparar no dia",
       "Pesquise a **reputação** da loja",
       "Veja se as **parcelas cabem** nos próximos meses"]),

P("2026-11-11", "tela", "Wally na prática",
"""Para onde foi o seu dinheiro este mês? 🧐

No Wally, a resposta está a um toque. O painel separa suas despesas por categoria e mostra quanto cada uma pesou no mês:

🏠 Moradia
🍽️ Alimentação
🛍️ Compras
🚗 Transporte
…e todas as categorias que você quiser criar.

Quando você vê os números lado a lado, fica muito mais fácil decidir onde ajustar.
""" + LINK, ["org", "app"],
title="Para onde foi _seu dinheiro?_",
sub="Suas despesas separadas por categoria, com o peso de cada uma no mês.",
img="categorias", w=700),

P("2026-11-13", "mito", "Mito ou verdade",
"""Mito ou verdade? 🤔

"Parcelar sem juros é sempre um bom negócio."

❌ MITO!

Parcelar sem juros pode, sim, ajudar a organizar o fluxo do mês. O problema é quando as parcelas se acumulam. Cada uma parece pequena, mas juntas comprometem a renda dos próximos meses.

Antes de parcelar, pergunte:
👉 Eu compraria à vista se tivesse o dinheiro?
👉 Quanto da minha renda já está comprometido com parcelas?
👉 Tem desconto para pagamento à vista?

No Wally, cada parcela aparece no mês em que será paga. Assim você enxerga o futuro antes de ele chegar.
""", ["cartao", "compras"],
title="Parcelar sem juros é _sempre bom?_",
mito="Parcelar sem juros é sempre um bom negócio.",
verdade="Ajuda no fluxo do mês, mas **parcelas acumuladas** comprometem a renda dos meses seguintes."),

P("2026-11-16", "destaque", "Dica de finanças",
"""Já ouviu falar da regra das 72 horas? ⏳

Deu vontade de comprar algo que não estava nos planos? Espere 72 horas antes de fechar a compra.

Nesse tempo, a empolgação passa e você consegue pensar com calma:
🤔 Eu realmente preciso disso?
💸 Cabe no orçamento deste mês?
🔍 Achei o melhor preço?

Se depois de 3 dias a vontade continuar e couber no bolso, compre sem culpa. Na maioria das vezes, a vontade simplesmente vai embora.

Perfeito para testar nesta época de promoções. 😉
""", ["compras", "vida"],
big="72h",
text="Deu vontade de comprar algo fora do plano? **Espere 72 horas.** Se a vontade continuar e couber no bolso, compre sem culpa."),

P("2026-11-18", "dica", "Wally na prática",
"""Compras parceladas sem bagunça. 🧾

Quando você registra uma compra parcelada no Wally:
1️⃣ Informe o valor e o número de parcelas
2️⃣ O Wally cria cada parcela no mês em que ela vence
3️⃣ Seus próximos meses já mostram o que está comprometido

Chega de ser surpreendido por aquela parcela de 8/10 que você nem lembrava mais. 😅
""" + LINK, ["cartao", "org"],
title="Parcelas no lugar certo, _mês a mês._",
items=["Registre a compra informando o **número de parcelas**",
       "O Wally cria **cada parcela no mês** em que ela vence",
       "Seus próximos meses mostram **o que já está comprometido**"]),

P("2026-11-20", "frase", "Pra pensar",
"""Um exercício rápido antes da Black Friday: 🛒

Pense nas coisas que estão no seu carrinho. Agora imagine que elas estão com o preço normal.

Você ainda compraria?

Se a resposta for sim, ótimo: o desconto é um bônus. Se for não, talvez o que você queira seja a promoção, e não o produto.

Conta aqui: qual item você está esperando baixar de preço? 👇
""", ["compras", "vida"],
title="Você compraria _se não estivesse em promoção?_",
sub="Se a resposta for sim, o desconto é um bônus. Se for não, talvez você queira só a promoção."),

P("2026-11-23", "dica", "Checklist",
"""Checklist para a semana da Black Friday. ✅

Antes de clicar em "comprar", confira:
☑️ Eu realmente preciso disso?
☑️ O preço está menor do que o de semanas atrás?
☑️ Já somei o frete?
☑️ As parcelas cabem nos próximos meses?
☑️ O site é confiável?

Passou em tudo? Pode comprar tranquilo! 🛍️

Salve e mande para aquele amigo que vive caindo nas promoções. 😂
""", ["compras", "econ"],
title="Antes de clicar em _comprar_",
style="check",
items=["Eu **realmente preciso** disso?",
       "O preço está **menor** do que semanas atrás?",
       "Já somei o **frete**?",
       "As **parcelas cabem** nos próximos meses?",
       "O site é **confiável**?"]),

P("2026-11-25", "dica", "Wally na prática",
"""Um limite para cada categoria. 🎯

Com os orçamentos do Wally você define quanto quer gastar por mês em cada categoria, como Compras, Lazer ou Delivery.

1️⃣ Escolha a categoria
2️⃣ Defina o limite mensal
3️⃣ Acompanhe a barra enchendo conforme você gasta

Quando chegar perto do limite, o Wally te avisa. Nesta semana de promoções, um orçamento para "Compras" pode salvar seu dezembro. 😉
""" + LINK, ["org", "compras"],
title="Um limite para _cada categoria._",
items=["Escolha a **categoria**, como Compras ou Lazer",
       "Defina o **limite mensal**",
       "Acompanhe a barra enchendo e receba um **aviso perto do limite**"]),

P("2026-11-27", "frase", "Black Friday",
"""Hoje é Black Friday! 🖤

Um lembrete carinhoso antes de abrir os apps das lojas:

A melhor promoção é a que cabe no seu orçamento.

Comprou algo hoje? Registre no Wally para o gasto não sumir no meio da fatura. 😉

Boas compras e com consciência! 🛍️
""", ["compras", "econ"],
title="A melhor promoção é a que _cabe no seu orçamento._",
sub="Boa Black Friday! 🖤"),

P("2026-11-30", "dica", "13º salário",
"""O 13º caiu (ou está para cair)? 💸

Antes de gastar, vale pensar no destino desse dinheiro extra:

1️⃣ Quite dívidas com juros altos, como cartão e cheque especial
2️⃣ Reserve para as contas de janeiro: IPVA, IPTU e material escolar
3️⃣ Reforce sua reserva de emergência
4️⃣ Separe uma parte para aproveitar, sem culpa

Não existe resposta única. O importante é decidir antes que o dinheiro decida por você. 😉

""" + SALVE, ["reserva", "org"],
title="4 destinos inteligentes para _o 13º_",
items=["**Quite dívidas** com juros altos, como cartão e cheque especial",
       "**Reserve** para as contas de janeiro",
       "**Reforce** a reserva de emergência",
       "Separe uma parte para **aproveitar, sem culpa**"]),

P("2026-12-02", "chat", "Wally na prática",
"""13º na conta? Registre em 2 segundos. 💰

Mande para o Wally no Telegram:
💬 "Recebi o 13º 2500"

Pronto, a receita já está registrada. E se quiser ver como está o mês, é só mandar /saldo.

Com tudo registrado, fica muito mais fácil decidir para onde vai cada parte desse dinheiro extra.
""" + LINK, ["app", "org"],
title="Recebeu o 13º? _Registrou._",
msgs=[("u", "Recebi o 13º 2500"),
      card("💰", "13º salário", "Salário · Hoje", "2.500,00", inc=True),
      ("u", "/saldo"),
      ("wt", "📊 **Resumo de dezembro**\nReceitas: R$ 7.300,00\nDespesas: R$ 2.140,00\nSaldo do mês: R$ 5.160,00")]),

P("2026-12-04", "destaque", "Dica de finanças",
"""R$ 10 por dia parece pouco, né? 🤏

Mas em um ano são R$ 3.650. ☕🍫🥤

Não é sobre cortar o cafezinho. É sobre enxergar quanto os pequenos gastos somam para decidir se eles valem a pena para você.

Faz o teste: qual gasto de todo dia você tem? Multiplica por 365 e conta aqui o resultado. 👇
""", ["econ", "vida"],
title="R$ 10 por dia viram",
big="R$ 3.650",
text="em um ano. Pequenos gastos somam, e **enxergar** é o primeiro passo para decidir se valem a pena."),

P("2026-12-07", "dica", "Natal",
"""Natal sem susto na fatura de janeiro. 🎄

1️⃣ Liste para quem você vai dar presente
2️⃣ Defina um valor por pessoa, e o total
3️⃣ Proponha amigo secreto na família ou no trabalho
4️⃣ Compre com antecedência para fugir da correria e dos preços altos
5️⃣ Presente feito à mão ou experiência também vale, e muito

Dica bônus: crie um orçamento para a categoria "Presentes" no Wally e acompanhe quanto já foi. 🎁

""" + SALVE, ["compras", "fam"],
title="Presentes de Natal _sem susto_ em janeiro",
items=["Liste **para quem** você vai dar presente",
       "Defina um **valor por pessoa** e o total",
       "Proponha **amigo secreto** na família ou no trabalho",
       "**Compre antes** para fugir da correria",
       "Presente **feito à mão** ou experiência também vale"]),

P("2026-12-09", "dica", "Wally na prática",
"""Tem um sonho para 2027? Transforme em meta. 🎯

No Wally você cria metas financeiras e acompanha o progresso:

1️⃣ Dê um nome, como Viagem, Reserva de emergência ou Carro novo
2️⃣ Defina o valor e o prazo
3️⃣ Vá depositando e veja a barra avançar

Ver o objetivo ficando cada vez mais perto é a melhor motivação para continuar guardando. 💙

Qual vai ser a sua primeira meta? 👇
""", ["meta", "reserva"],
title="Transforme o sonho _em meta._",
items=["Dê um **nome**: Viagem, Reserva, Carro novo…",
       "Defina o **valor** e o **prazo**",
       "Vá depositando e **veja a barra avançar**"]),

P("2026-12-11", "mito", "Mito ou verdade",
"""Mito ou verdade? 🤔

"Dezembro é mês perdido para a organização financeira."

❌ MITO!

Dezembro tem mais gastos, sim: presentes, confraternizações, viagens. Mas é justamente por isso que é o mês em que o controle mais faz diferença.

Quem acompanha os gastos em dezembro chega em janeiro sabendo exatamente o que ficou na fatura. Quem larga tudo leva um susto.

Não precisa ser perfeito. Registrar os gastos maiores já ajuda muito. 😉
""", ["org", "vida"],
title="Dezembro é mês _perdido?_",
mito="Dezembro é mês perdido para a organização financeira.",
verdade="É o mês em que o controle **mais faz diferença**, porque é o que decide como janeiro vai começar."),

P("2026-12-14", "dica", "Dica de finanças",
"""Janeiro chega com uma fila de contas. Prepare-se agora. 📋

As mais comuns no começo do ano:
🚗 IPVA
🏠 IPTU
📚 Material e matrícula escolar
💳 A fatura das compras de fim de ano

Como se preparar:
1️⃣ Liste as contas e os valores estimados
2️⃣ Veja se há desconto para pagamento à vista
3️⃣ Separe o dinheiro antes das festas, se possível do 13º

Janeiro fica bem mais leve quando você já sabe o que vem. 😌

""" + SALVE, ["org", "econ"],
title="Prepare-se para as contas _de janeiro_",
items=["Liste **IPVA, IPTU, material escolar** e a fatura de dezembro",
       "Veja se há **desconto** para pagar à vista",
       "**Separe o dinheiro** antes das festas, se possível do 13º"]),

P("2026-12-16", "tela", "Wally na prática",
"""Como foi o seu ano financeiro? 📈

Na tela de Relatórios do Wally você vê:
📊 Receitas x despesas mês a mês
📈 A evolução do seu patrimônio
💰 Sua taxa de poupança
🍩 Os gastos por categoria

Dá para olhar os últimos 3, 6 ou 12 meses. É a retrospectiva perfeita para fechar o ano e planejar o próximo.
""" + LINK, ["org", "meta"],
title="Seu ano _em números._",
sub="Receitas, despesas, patrimônio e taxa de poupança de até 12 meses.",
img="rel-top"),

P("2026-12-18", "frase", "Pra pensar",
"""O ano está acabando e hoje o convite é para comemorar. 🎉

Qual foi a sua maior vitória financeira em 2026?

Pode ser grande ou pequena:
✅ Quitou uma dívida
✅ Começou a reserva de emergência
✅ Parou de entrar no cheque especial
✅ Finalmente sabe para onde vai o dinheiro

Toda conquista conta. Compartilha aqui nos comentários que a gente comemora junto! 👇
""", ["vida", "meta"],
title="Qual foi sua maior _vitória financeira_ em 2026?",
sub="Grande ou pequena, toda conquista conta. Conta pra gente! 👇"),

P("2026-12-21", "dica", "Retrospectiva",
"""Antes de fazer planos para 2027, vale olhar para trás. 🔍

5 perguntas para fechar o ano:
1️⃣ Quanto eu ganhei e quanto eu gastei?
2️⃣ Em qual categoria gastei mais do que imaginava?
3️⃣ Consegui guardar alguma coisa?
4️⃣ Tenho dívidas? Elas aumentaram ou diminuíram?
5️⃣ O que eu faria diferente?

Se você registrou seus gastos no Wally, as respostas estão prontas em Relatórios. 😉

""" + SALVE, ["meta", "org"],
title="5 perguntas para _fechar o ano_",
items=["Quanto eu **ganhei** e quanto eu **gastei**?",
       "Em qual categoria gastei **mais do que imaginava**?",
       "Consegui **guardar** alguma coisa?",
       "Minhas **dívidas** aumentaram ou diminuíram?",
       "O que eu faria **diferente**?"]),

P("2026-12-23", "dica", "Festas",
"""Ceia e festas de fim de ano sem pesar no bolso. 🍽️

1️⃣ Faça ceia compartilhada: cada um leva um prato
2️⃣ Monte a lista de compras e fuja do mercado na véspera
3️⃣ Aproveite o que já tem em casa
4️⃣ Combine o valor do amigo secreto antes
5️⃣ Divida as despesas da viagem com antecedência

O que importa mesmo é estar junto de quem a gente gosta. 💙
""", ["fam", "econ"],
title="Festas de fim de ano _sem pesar no bolso_",
items=["Faça **ceia compartilhada**: cada um leva um prato",
       "Monte a **lista** e fuja do mercado na véspera",
       "Aproveite o que **já tem em casa**",
       "Combine o valor do **amigo secreto** antes"]),

P("2026-12-25", "frase", "Feliz Natal",
"""Feliz Natal! 🎄✨

Hoje o dia é para descansar, estar com quem você ama e aproveitar.

O Wally deseja um Natal leve, cheio de afeto e com o coração tranquilo.

Obrigado por estar com a gente por aqui. 💙
""", ["vida"],
title="Feliz _Natal!_ 🎄",
sub="Que seu dia seja leve, cheio de afeto e de gente querida por perto."),

P("2026-12-28", "dica", "Metas 2027",
"""Metas financeiras para 2027 que funcionam de verdade. 🎯

"Economizar mais" não é meta, é desejo. Uma boa meta tem:

1️⃣ Objetivo claro: "juntar para a viagem de julho"
2️⃣ Valor definido: R$ 3.000
3️⃣ Prazo: até junho
4️⃣ Plano mensal: R$ 500 por mês

Com isso, você sabe exatamente o que fazer todo mês e consegue acompanhar se está no caminho.

Crie sua meta no Wally e veja o progresso a cada depósito. 💙

""" + SALVE, ["meta", "vida"],
title="Metas para 2027 que _funcionam_",
items=["**Objetivo claro:** juntar para a viagem de julho",
       "**Valor definido:** R$ 3.000",
       "**Prazo:** até junho",
       "**Plano mensal:** R$ 500 por mês"]),

P("2026-12-30", "cta", "Ano novo",
"""2027 está chegando. Que tal começar o ano com o dinheiro organizado? ✨

Não precisa esperar segunda-feira nem dia 1º. Leva 3 minutos:

1️⃣ Crie sua conta grátis no Wally
2️⃣ Cadastre sua conta principal
3️⃣ Registre os gastos do dia

E em janeiro você já vai saber exatamente para onde está indo cada real. 💙
""" + LINK, ["meta", "org"],
title="Comece 2027 com o dinheiro _organizado._",
sub="Leva 3 minutos e é grátis para começar."),
]

EXTRA = [

P("2026-10-02", "frase", "Pra pensar",
"""Pergunta rápida para a sua sexta-feira: 🤔

Você sabe quanto gastou esta semana?

Não precisa ser o valor exato. Só um chute.

Se veio um "sei lá" na cabeça, você não está sozinho. A maioria das pessoas só descobre quando a fatura chega. E aí já foi.

Saber para onde vai o dinheiro é o primeiro passo para decidir para onde você quer que ele vá. 💙

Chuta aí nos comentários quanto você acha que gastou. 👇
""", ["org", "vida"],
title="Você sabe quanto gastou _esta semana?_",
sub="Chuta um valor. Se veio um “sei lá”, o Wally resolve isso."),

P("2026-10-05", "dica", "Primeiros passos",
"""Quer organizar o dinheiro mas não sabe por onde começar? 🧭

Esquece planilha complicada. Comece por aqui:

1️⃣ Anote tudo o que gastar por 30 dias, até o cafezinho
2️⃣ No fim do mês, veja quais categorias pesaram mais
3️⃣ Escolha só uma para ajustar no mês seguinte
4️⃣ Defina um limite para ela e acompanhe

Um passo de cada vez funciona muito melhor do que tentar mudar tudo de uma vez.

E para o passo 1, o Wally deixa tudo a uma mensagem de distância. 😉

""" + SALVE, ["org", "vida"],
title="Por onde começar a _organizar o dinheiro_",
items=["**Anote tudo** o que gastar por 30 dias",
       "Veja quais **categorias pesaram mais**",
       "Escolha **só uma** para ajustar",
       "Defina um **limite** e acompanhe"]),
]
