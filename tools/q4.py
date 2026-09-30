from common import P, card, LINK, SALVE

POSTS = [

P("2027-07-02", "frase", "Boas férias",
"""Julho chegou, e com ele as férias! 🏖️

Se você planejou e separou o dinheiro antes, agora é só aproveitar, sem culpa e sem medo da fatura.

Se não deu para viajar desta vez, tudo bem também: descansar em casa conta, e muito. 😌

Boas férias! 💙
""", ["vida", "meta"],
title="Boas férias! _Aproveite sem culpa._ 🏖️",
sub="Dinheiro separado antes, tranquilidade durante.",
dark=False),

P("2027-07-05", "dica", "Férias",
"""Crianças de férias em casa? Diversão não precisa custar caro. 🎈

1️⃣ Parques e praças da cidade
2️⃣ Bibliotecas públicas, muitas com atividades infantis
3️⃣ Eventos gratuitos: confira a agenda cultural da sua cidade
4️⃣ Piquenique com lanche feito em casa
5️⃣ Cinema em casa, com pipoca e cabana de lençol

As melhores memórias da infância raramente foram as mais caras. 💙

Tem outra ideia? Deixa aqui para ajudar outras famílias! 👇
""", ["fam", "econ"],
title="Férias das crianças _sem gastar muito_",
items=["**Parques e praças** da cidade",
       "**Bibliotecas públicas** com atividades",
       "**Eventos gratuitos** da agenda cultural",
       "**Piquenique** com lanche de casa",
       "**Cinema em casa** com cabana de lençol"]),

P("2027-07-07", "chat", "Wally na prática",
"""Viajando? Registre os gastos em tempo real. ✈️

Entre um passeio e outro, é só mandar uma mensagem:
💬 "pousada 450"
💬 "passeio de barco 120"

Na volta você sabe exatamente quanto a viagem custou, e se ficou dentro do planejado. 🏝️
""" + LINK, ["app", "meta"],
title="Viagem registrada _em tempo real._",
msgs=[("u", "pousada 450"),
      card("🏨", "Pousada", "Viagem · Hoje", "450,00"),
      ("u", "passeio de barco 120"),
      card("⛵", "Passeio de barco", "Viagem · Hoje", "120,00")]),

P("2027-07-09", "mito", "Mito ou verdade",
"""Mito ou verdade? 🤔

"Guardar dinheiro é sacrifício."

❌ MITO!

Guardar não é abrir mão de viver. É escolher o que importa mais para você: uma viagem, a tranquilidade de ter uma reserva, o sonho da casa própria.

Quando o dinheiro tem um destino que você quer, guardar deixa de ser sacrifício e passa a ser conquista. 🎯
""", ["reserva", "vida"],
title="Guardar dinheiro _é sacrifício?_",
mito="Guardar dinheiro é sacrifício.",
verdade="É **escolher o que importa mais** para você. Com um objetivo claro, guardar vira **conquista**."),

P("2027-07-12", "dica", "Dica de finanças",
"""Por que a gente compra por impulso? Conheça os gatilhos. 🧠

1️⃣ Tédio: rolar o feed da loja "só para olhar"
2️⃣ Urgência: "só hoje", "últimas unidades"
3️⃣ Cansaço: o famoso "eu mereço" depois de um dia difícil
4️⃣ Redes sociais: ver alguém usando e querer igual
5️⃣ Emoção: comprar para se sentir melhor

Reconhecer o gatilho já ajuda a parar e pensar antes de clicar. E a regra das 72h continua valendo. 😉

""" + SALVE, ["compras", "vida"],
title="5 gatilhos da _compra por impulso_",
items=["**Tédio**: olhar a loja “só por olhar”",
       "**Urgência**: “só hoje”, “últimas unidades”",
       "**Cansaço**: o famoso “eu mereço”",
       "**Redes sociais**: querer igual",
       "**Emoção**: comprar para se sentir melhor"]),

P("2027-07-14", "dica", "Wally na prática",
"""A lista de transações do Wally agrupa as compras do cartão por fatura. 💳

Isso quer dizer que:
📂 Todas as compras de uma mesma fatura aparecem juntas
📅 Cada compra mostra a data real em que foi feita
💳 Cartões diferentes ficam em grupos separados, mesmo que vençam no mesmo dia

Na hora de conferir a fatura, está tudo ali, organizado. 😌
""" + LINK, ["cartao", "org"],
title="Compras do cartão _agrupadas por fatura._",
items=["Compras da mesma fatura aparecem **juntas**",
       "Cada compra mostra a **data real**",
       "Cada cartão com seu **próprio grupo**"]),

P("2027-07-16", "frase", "Pra pensar",
"""Pequenas escolhas, repetidas todos os dias, constroem grandes resultados. 🌱

Registrar um gasto. Adiar uma compra por impulso. Guardar R$ 20.

Sozinhas, parecem nada. Somadas ao longo de meses, mudam a sua vida financeira.

Qual pequena escolha você fez esta semana? 👇
""", ["vida", "meta"],
title="Pequenas escolhas, todos os dias, _constroem grandes resultados._",
dark=False),

P("2027-07-19", "dica", "Dica de finanças",
"""Aconteceu um imprevisto e o dinheiro apertou? Respira. Dá para organizar. 🧘

1️⃣ Liste as contas essenciais: moradia, alimentação, saúde, contas básicas
2️⃣ Priorize o essencial e pause os gastos que podem esperar
3️⃣ Use a reserva de emergência, se tiver. É para isso que ela existe.
4️⃣ Converse com credores antes de atrasar. Muitas vezes dá para negociar.
5️⃣ Evite cobrir o buraco com crédito caro, como cheque especial

Quando a situação passar, reconstrua a reserva aos poucos. 💙

""" + SALVE, ["reserva", "vida"],
title="O dinheiro apertou? _Um plano de ação_",
items=["Liste as **contas essenciais**",
       "**Pause** o que pode esperar",
       "Use a **reserva**. É para isso que ela existe",
       "**Converse com os credores** antes de atrasar",
       "Evite **crédito caro**"]),

P("2027-07-21", "tela", "Wally na prática",
"""Quanto a moradia pesa no seu mês? E a alimentação? 🏠🍽️

No painel do Wally, cada categoria aparece com o valor gasto e a porcentagem do total.

É o raio-x do seu mês: dá para ver na hora onde está a maior parte do dinheiro e onde vale a pena ajustar.
""" + LINK, ["org", "app"],
title="O raio-x _do seu mês._",
sub="Cada categoria com o valor gasto e o peso no total.",
img="categorias", w=700),

P("2027-07-23", "frase", "Enquete",
"""Confissão da sexta! 🙈

Você confere os lançamentos da fatura do cartão antes de pagar?

1️⃣ Sempre, linha por linha
2️⃣ Às vezes, quando o valor assusta
3️⃣ Nunca, só pago

Responde com o número! Na segunda tem post ensinando a ler a fatura. 😉👇
""", ["cartao", "vida"],
title="Você confere _a fatura_ antes de pagar?",
sub="1 sempre · 2 às vezes · 3 nunca. Responde nos comentários! 👇"),

P("2027-07-26", "dica", "Dica de finanças",
"""Como ler a fatura do cartão de crédito. 🔍

1️⃣ Valor total: é o que você deve pagar para não ter juros
2️⃣ Pagamento mínimo: evite. O restante entra no rotativo, com juros altos.
3️⃣ Vencimento: a data limite para pagar
4️⃣ Fechamento: compras depois dessa data vão para a próxima fatura
5️⃣ Lançamentos: confira um a um e conteste o que não reconhecer

Conferir a fatura leva 5 minutos e pode evitar cobranças indevidas. 😉

""" + SALVE, ["cartao", "org"],
title="Como ler _a fatura_ do cartão",
items=["**Valor total**: pague tudo para não ter juros",
       "**Mínimo**: evite, o resto vira rotativo",
       "**Vencimento**: a data limite",
       "**Fechamento**: depois dele, vai para a próxima",
       "**Lançamentos**: confira um a um"]),

P("2027-07-28", "chat", "Wally na prática",
"""Gosta de ir direto ao ponto? O Wally também tem comandos rápidos. ⚡

💬 /despesa 50 Farmácia
💬 /receita 300 Venda do monitor

O valor e a descrição já vão certinhos, e o registro é imediato.

Mas, se preferir escrever do seu jeito, a IA entende do mesmo jeito. 😉
""" + LINK, ["app", "org"],
title="Comandos _rápidos._",
msgs=[("u", "/despesa 50 Farmácia"),
      card("💊", "Farmácia", "Saúde · Hoje", "50,00"),
      ("u", "/receita 300 Venda do monitor"),
      card("🖥️", "Venda do monitor", "Outras receitas · Hoje", "300,00", inc=True)]),

P("2027-07-30", "comp", "Dica de finanças",
"""Pagar o mínimo ou o total da fatura? 💳

Pagar o mínimo parece um alívio no mês, mas o restante entra no crédito rotativo, uma das linhas de crédito mais caras que existem.

Se não der para pagar o total:
✅ Pague o máximo que conseguir
✅ Veja se o parcelamento da fatura sai mais barato que o rotativo
✅ Pare de usar o cartão até organizar a situação

""" + SALVE, ["cartao", "vida"],
title="Pagar o _mínimo_ ou o _total?_",
left=("Mínimo", ["O resto vira **rotativo**", "Juros **muito altos**", "A dívida **cresce**"]),
right=("Total", ["**Sem juros**", "Fatura **zerada**", "Mês seguinte **tranquilo**"])),

P("2027-08-02", "dica", "Dica de finanças",
"""Recebeu um aumento? Parabéns! 🎉 Agora, cuidado com a armadilha.

É muito comum o padrão de vida subir junto com o salário, e no fim do mês continua sem sobrar nada.

1️⃣ Decida o destino do aumento antes de ele cair na conta
2️⃣ Direcione pelo menos parte dele para guardar ou investir
3️⃣ Se tiver dívidas, use o aumento para acelerar a quitação
4️⃣ Comemore, mas com um valor definido

O aumento é uma ótima chance de dar um salto na vida financeira. 🚀

""" + SALVE, ["reserva", "meta"],
title="Ganhou aumento? _Cuidado com a armadilha._",
items=["Decida o **destino** antes de o dinheiro cair",
       "Direcione parte para **guardar**",
       "Use para **acelerar** a quitação de dívidas",
       "**Comemore**, mas com um valor definido"]),

P("2027-08-04", "dica", "Wally na prática",
"""Claro, escuro ou automático: você escolhe. 🌙☀️

O Wally tem modo escuro para quem gosta de conferir as finanças à noite sem cansar a vista.

No modo automático, ele acompanha a configuração do seu celular ou computador.

Qual time você é: claro ou escuro? 👇
""" + LINK, ["app", "org"],
title="Claro, escuro _ou automático._",
items=["**Modo claro** para o dia",
       "**Modo escuro** para a noite",
       "**Automático**: acompanha o seu aparelho"]),

P("2027-08-06", "frase", "Dia dos Pais",
"""Domingo é Dia dos Pais! 💙

Para quem ensinou a gente a pesquisar antes de comprar, a desconfiar de "negócio da China" e a guardar para o futuro: obrigado.

Presente com carinho não precisa ser caro: um almoço em família, um passeio juntos, um tempo de qualidade.

Marca aqui o seu pai, ou quem cumpre esse papel na sua vida! 👇
""", ["fam", "vida"],
title="Para quem ensinou a gente a _pesquisar antes de comprar_: obrigado. 💙",
dark=False),

P("2027-08-09", "dica", "Dica de finanças",
"""Pensando em pegar um empréstimo? Responda antes estas perguntas. 🤔

1️⃣ Para que eu preciso desse dinheiro? É essencial?
2️⃣ Qual é o Custo Efetivo Total (CET)? Ele inclui juros, taxas e seguros.
3️⃣ A parcela cabe no meu orçamento com folga?
4️⃣ Existe uma alternativa mais barata?
5️⃣ Comparei as condições em mais de uma instituição?

Empréstimo pode ser útil, por exemplo para trocar uma dívida cara por uma mais barata. Só não pode ser decidido no impulso. 😉

""" + SALVE, ["cartao", "vida"],
title="Antes de pegar _um empréstimo_",
items=["Para que eu preciso? **É essencial?**",
       "Qual é o **CET**, o custo total?",
       "A parcela cabe **com folga**?",
       "Existe **alternativa** mais barata?",
       "**Comparei** mais de uma instituição?"]),

P("2027-08-11", "tela", "Wally na prática",
"""Pensar no orçamento por dia muda tudo. 📅

"Tenho R$ 680 até o fim do mês" parece bastante. "Tenho R$ 170 por dia pelos próximos 4 dias" deixa tudo mais claro.

O card Quanto posso gastar faz essa conta por você, e mostra quanto do limite do mês você já usou. 😉
""" + LINK, ["org", "app"],
title="Pense _por dia_, não por mês.",
sub="O Wally divide o que sobrou pelos dias que faltam até o fim do mês.",
img="posso-gastar", w=720),

P("2027-08-13", "mito", "Mito ou verdade",
"""Mito ou verdade? 🤔

"Ter cheque especial é ter um dinheiro extra."

❌ MITO!

O limite do cheque especial não é seu: é um empréstimo automático, e dos mais caros do mercado.

Se você entra nele todo mês, é sinal de que as contas não estão fechando. O caminho é:
✅ Descobrir onde o dinheiro está indo
✅ Ajustar os gastos
✅ Trocar essa dívida por uma mais barata, se precisar

Saber para onde vai cada real é o primeiro passo. E é aí que o Wally entra. 😉
""", ["cartao", "org"],
title="Cheque especial _é dinheiro extra?_",
mito="Ter cheque especial é ter um dinheiro extra.",
verdade="É um **empréstimo automático** e dos **mais caros** do mercado. Não é seu dinheiro."),

P("2027-08-16", "dica", "Dica de finanças",
"""Aposentadoria parece longe? Por isso mesmo vale pensar nela agora. ⏳

1️⃣ O tempo é o seu maior aliado: quem começa cedo precisa guardar menos por mês
2️⃣ Saiba como está a sua contribuição para a previdência pública
3️⃣ Pense em complementar com investimentos de longo prazo
4️⃣ Crie uma meta de longo prazo, separada da reserva de emergência
5️⃣ Revise o plano todo ano

Este post é educativo e não é recomendação de investimento. Na dúvida, procure um profissional certificado.

""" + SALVE, ["meta", "reserva"],
title="Aposentadoria: _por que pensar agora_",
items=["O **tempo** é seu maior aliado",
       "Saiba como está sua **previdência pública**",
       "Pense em **complementar** no longo prazo",
       "Crie uma **meta de longo prazo** separada",
       "**Revise** o plano todo ano"]),

P("2027-08-18", "tela", "Wally na prática",
"""Seu patrimônio está crescendo? O Wally mostra. 📈

Nos Relatórios, o gráfico de evolução do patrimônio mostra mês a mês o resultado das suas escolhas.

Não tem sensação melhor do que ver essa linha subindo. 💙
""" + LINK, ["meta", "reserva"],
title="Veja seu patrimônio _crescer._",
sub="O resultado das suas escolhas, mês a mês.",
img="patrimonio", w=860),

P("2027-08-20", "frase", "Pra pensar",
"""Pergunta sincera: com quantos anos você aprendeu sobre dinheiro? 🤔

Na escola? Em casa? Sozinho, errando? Ou está aprendendo agora?

Não importa quando: nunca é tarde para aprender. E ensinar quem vem depois é um presente enorme.

Conta sua história aqui! 👇
""", ["vida", "fam"],
title="Com quantos anos você _aprendeu sobre dinheiro?_",
sub="Nunca é tarde para aprender. Conta sua história! 👇"),

P("2027-08-23", "dica", "Segurança",
"""Golpes financeiros: 5 sinais de alerta. 🚨

1️⃣ Promessa de ganho alto, rápido e garantido
2️⃣ Urgência: "só hoje", "sua conta será bloqueada"
3️⃣ Pedido de senha, código de verificação ou token
4️⃣ Links estranhos por SMS, e-mail ou mensagem
5️⃣ Pedido de Pix para alguém "conhecido" com número novo

Na dúvida, desligue e entre em contato pelos canais oficiais. Nenhuma instituição séria pede sua senha. 🔒

Compartilhe com quem você quer proteger! 💙
""", ["vida", "org"],
title="Golpes: _5 sinais de alerta_",
items=["Ganho **alto, rápido e garantido**",
       "**Urgência**: “só hoje”, “conta bloqueada”",
       "Pedido de **senha ou código**",
       "**Links estranhos** por SMS ou mensagem",
       "Pix para **“conhecido” com número novo**"]),

P("2027-08-25", "dica", "Wally na prática",
"""Achar um gasto antigo no Wally é rapidinho. 🔎

1️⃣ Escolha o mês no seletor de período, no topo
2️⃣ Filtre por tipo, categoria ou conta
3️⃣ Pronto: a lista mostra tudo organizado, com as compras do cartão agrupadas por fatura

Aquele "quanto foi mesmo o conserto do carro em março?" se resolve em segundos. 😉
""" + LINK, ["org", "app"],
title="Encontre qualquer gasto _em segundos._",
items=["Escolha o **mês** no seletor de período",
       "Filtre por **tipo, categoria ou conta**",
       "Veja tudo **organizado**, com o cartão agrupado por fatura"]),

P("2027-08-27", "destaque", "Pra pensar",
"""Faltam 4 meses para acabar 2027. ⏳

Ainda dá tempo de:
🎯 Bater aquela meta
🛟 Reforçar a reserva
💳 Quitar uma dívida
📊 Criar o hábito de registrar os gastos

4 meses são mais de 120 dias. Muita coisa muda nesse tempo. Bora? 💪
""", ["meta", "vida"],
title="Faltam",
big="4 meses",
text="para acabar 2027. **Ainda dá tempo** de bater a meta do ano. 💪"),

P("2027-08-30", "dica", "Dica de finanças",
"""Black Friday, Natal, presentes, IPVA… O fim do ano é caro. Comece a se preparar agora. 🎄

1️⃣ Liste os gastos de novembro a janeiro
2️⃣ Estime o valor total
3️⃣ Divida pelos meses que faltam até lá
4️⃣ Crie uma meta "Fim de ano" e guarde esse valor todo mês

Em dezembro, você vai agradecer ao seu eu de agosto. 😉

""" + SALVE, ["meta", "org"],
title="Crie o seu _fundo de fim de ano_",
items=["Liste os gastos de **novembro a janeiro**",
       "Estime o **valor total**",
       "**Divida** pelos meses que faltam",
       "Crie a meta **Fim de ano** e guarde todo mês"]),

P("2027-09-01", "chat", "Wally na prática",
"""Começo de mês: salário na conta e contas para pagar. 📅

Registrar tudo no Wally leva segundos:
💬 "salário 5200"
💬 "aluguel 1250"

E o mês já começa organizado, com o painel mostrando quanto entrou e quanto já tem destino. 😉
""" + LINK, ["app", "org"],
title="O mês começa _organizado._",
msgs=[("u", "salário 5200"),
      card("💰", "Salário", "Salário · Hoje", "5.200,00", inc=True),
      ("u", "aluguel 1250"),
      card("🏠", "Aluguel", "Moradia · Hoje", "1.250,00")]),

P("2027-09-03", "mito", "Mito ou verdade",
"""Mito ou verdade? 🤔

"Organizar as finanças dá muito trabalho."

❌ MITO!

Dava. Com planilhas, cadernos e calculadora, era mesmo trabalhoso.

Com o Wally:
⚡ Registrar um gasto leva menos de 5 segundos
🤖 A categoria é escolhida automaticamente
📊 Gráficos e relatórios ficam prontos sozinhos

O trabalho pesado fica com a gente. Você só manda a mensagem. 😉
""" + LINK, ["org", "app"],
title="Organizar as finanças _dá muito trabalho?_",
mito="Organizar as finanças dá muito trabalho.",
verdade="Com o Wally, registrar um gasto leva **menos de 5 segundos**, e o resto fica **pronto sozinho**."),

P("2027-09-06", "dica", "Independência",
"""Amanhã é 7 de Setembro, e hoje o papo é independência financeira. 🇧🇷

Independência financeira não é ficar rico. É ter liberdade de escolha:
1️⃣ Não depender do próximo salário para dormir tranquilo
2️⃣ Ter reserva para os imprevistos
3️⃣ Não ter dívidas caras
4️⃣ Poder dizer "não" para o que não faz sentido

E o primeiro passo para chegar lá é saber para onde vai o seu dinheiro. 💙
""", ["vida", "reserva"],
title="Independência financeira é _liberdade de escolha_",
items=["Não depender do **próximo salário**",
       "Ter **reserva** para imprevistos",
       "Não ter **dívidas caras**",
       "Poder dizer **“não”** ao que não faz sentido"]),

P("2027-09-08", "comp", "Planos",
"""Grátis ou Pro: qual plano é o seu? 🤔

🆓 GRÁTIS
✅ Painel completo
✅ Histórico de transações
✅ Relatórios básicos
✅ 1 conta ou cartão

💙 PRO, R$ 19,90 por mês
✅ Tudo do grátis
✅ Bot com IA no Telegram
✅ Várias contas e cartões
✅ Relatórios avançados
✅ Exportação para Excel
✅ Suporte prioritário

Comece grátis e faça o upgrade quando sentir falta de algo. 😉
""" + LINK, ["app", "org"],
title="Grátis _ou_ Pro?",
left_ok=True,
left=("Grátis", ["Painel completo", "Histórico", "Relatórios básicos", "1 conta ou cartão"]),
right=("Pro · R$ 19,90", ["Bot com IA no Telegram", "Várias contas e cartões", "Relatórios avançados", "Exportação para Excel"])),

P("2027-09-10", "frase", "Pra pensar",
"""Pergunta para a comunidade: 💬

Qual hábito financeiro mudou a sua vida?

Pode ser simples:
📝 Anotar todos os gastos
⏳ Esperar antes de comprar
💰 Guardar assim que o salário cai
🚫 Cancelar assinaturas que não usava

Compartilha aqui. Sua resposta pode inspirar alguém! 👇
""", ["vida"],
title="Qual hábito financeiro _mudou sua vida?_",
sub="Compartilha aqui. Pode inspirar alguém! 👇"),

P("2027-09-13", "dica", "Dia do Cliente",
"""Quarta-feira, 15/09, é Dia do Cliente, e as promoções já começaram. 🛍️

Para aproveitar sem cair em armadilha:
1️⃣ Compre só o que já estava na sua lista
2️⃣ Compare o preço com o de semanas atrás
3️⃣ Desconfie de descontos exagerados em sites desconhecidos
4️⃣ Some o frete antes de comemorar o desconto
5️⃣ Veja se as parcelas cabem nos próximos meses

E lembre: compras online dão direito a 7 dias de arrependimento. 😉

""" + SALVE, ["compras", "econ"],
title="Dia do Cliente _sem armadilhas_",
items=["Compre só o que **estava na lista**",
       "**Compare** com o preço de semanas atrás",
       "Desconfie de descontos **exagerados**",
       "Some o **frete**",
       "Veja se as **parcelas cabem**"]),

P("2027-09-15", "frase", "Dia do Cliente",
"""Hoje é Dia do Cliente, e o dia é de agradecer. 💙

A cada pessoa que usa o Wally, manda mensagem para o bot, dá sugestões e confia a organização do seu dinheiro à gente: muito obrigado.

É por vocês que o Wally existe e continua melhorando.

Tem alguma sugestão para o Wally? Deixa aqui nos comentários, a gente lê tudo! 👇
""", ["vida", "app"],
title="Obrigado por _confiar no Wally._ 💙",
sub="Tem uma sugestão? Deixa nos comentários. A gente lê tudo!"),

P("2027-09-17", "destaque", "Wally na prática",
"""5 segundos. ⚡

É o tempo que leva para registrar um gasto no Wally pelo Telegram.

Menos tempo do que para desbloquear o celular, abrir um app, achar o formulário e escolher a categoria.

Por isso fica fácil manter o hábito todos os dias. 😉
""" + LINK, ["app", "org"],
big="5s",
text="é o tempo para registrar um gasto no Wally. **Mande uma mensagem** e pronto."),

P("2027-09-20", "dica", "Checklist",
"""Como está a sua saúde financeira? Faça o check-up. 🩺

☑️ Sei para onde vai o meu dinheiro
☑️ Gasto menos do que ganho
☑️ Tenho reserva de emergência, mesmo que pequena
☑️ Não tenho dívidas caras
☑️ Tenho pelo menos uma meta com valor e prazo
☑️ Guardo algum valor todo mês

Quantos você marcou? Conta aqui! 👇

""" + SALVE, ["org", "reserva"],
title="Check-up da sua _saúde financeira_",
style="check",
items=["Sei para onde vai **meu dinheiro**",
       "Gasto **menos do que ganho**",
       "Tenho **reserva de emergência**",
       "Não tenho **dívidas caras**",
       "Tenho uma **meta** com valor e prazo",
       "Guardo algum valor **todo mês**"]),

P("2027-09-22", "tela", "Wally na prática",
"""Tudo o que importa sobre o seu dinheiro, numa tela só. 📊

✅ Saldo atual
✅ Receitas, despesas e economia do mês
✅ O fluxo dos últimos 6 meses
✅ Os gastos por categoria

É o check-up financeiro que se atualiza sozinho, a cada gasto registrado.
""" + LINK, ["org", "app"],
title="Seu check-up _que se atualiza sozinho._",
img="dash-top"),

P("2027-09-24", "frase", "Enquete",
"""Queremos saber: o que você quer ver mais por aqui? 💬

1️⃣ Dicas para economizar no dia a dia
2️⃣ Como sair das dívidas
3️⃣ Primeiros passos para investir
4️⃣ Finanças em casal e em família
5️⃣ Truques do Wally

Responde com o número (ou números 😄) nos comentários! 👇
""", ["vida"],
title="O que você quer _ver mais_ por aqui?",
sub="Responde nos comentários. Sua resposta decide os próximos posts! 👇"),

P("2027-09-27", "dica", "Fim de ano",
"""Outubro começa esta semana, e o fim do ano está logo ali. Hora de planejar. 🗓️

1️⃣ Defina um teto para a Black Friday de novembro
2️⃣ Decida antes o destino do 13º
3️⃣ Faça a lista e o orçamento dos presentes de Natal
4️⃣ Separe o dinheiro das contas de janeiro

Quem planeja em outubro chega em janeiro tranquilo. 😌

""" + SALVE, ["meta", "org"],
title="Prepare-se para _o fim do ano_",
items=["Defina um **teto** para a Black Friday",
       "Decida o **destino do 13º**",
       "Faça o **orçamento** dos presentes",
       "Separe as **contas de janeiro**"]),

P("2027-09-29", "cta", "Plano Pro",
"""O fim do ano é a época em que mais vale a pena ter tudo sob controle. 🎯

Com o Wally Pro:
🤖 Registre cada gasto por mensagem no Telegram
💳 Controle todos os cartões e as faturas de fim de ano
📊 Acompanhe tudo em relatórios avançados
📥 Exporte para Excel quando quiser

Tudo por R$ 19,90 por mês. Se desistir em até 7 dias, o cancelamento é imediato.
""" + LINK, ["app", "org"],
title="Chegue ao fim do ano _com tudo sob controle._",
price=True,
feats=["Bot com IA no Telegram", "Várias contas e cartões", "Relatórios avançados", "Exportação para Excel"],
button="Assinar o Pro"),

P("2027-10-01", "frase", "Um ano juntos",
"""Um ano de conteúdo por aqui! 🎉

Foram dezenas de dicas, mitos derrubados, desafios e muitos gastos registrados em 5 segundos.

Obrigado por acompanhar, comentar, salvar e compartilhar. O próximo ano vai ser ainda melhor. 💙

Conta aqui: qual foi o post que mais te ajudou? 👇
""", ["vida"],
title="Um ano de dicas, conquistas e _dinheiro organizado._ 💙",
sub="Obrigado por estar com a gente. Vem mais por aí!"),
]
