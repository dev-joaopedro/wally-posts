"""Utilitários compartilhados pelos arquivos de conteúdo."""

H = {
    "base": "#wally #financaspessoais #educacaofinanceira",
    "org": "#organizacaofinanceira #controlefinanceiro #controledegastos",
    "econ": "#economizar #economia #dinheiro",
    "app": "#appdefinancas #whatsapp #inteligenciaartificial",
    "cartao": "#cartaodecredito #fatura #dividas",
    "reserva": "#reservadeemergencia #poupar #investimentos",
    "meta": "#metasfinanceiras #planejamentofinanceiro #objetivos",
    "fam": "#financasfamiliares #familia #mesada",
    "compras": "#consumoconsciente #compras #promocao",
    "vida": "#vidafinanceira #mentalidadefinanceira #habitos",
    "ir": "#impostoderenda #declaracao #ir2027",
}


def P(d, t, tag, cap, tags, **kw):
    """Um post: data (AAAA-MM-DD), template, rótulo da arte, legenda, grupos de hashtags e campos da arte."""
    groups = ["base"] + tags
    hashtags = " ".join(H[g] for g in groups)
    return dict(d=d, t=t, tag=tag, caption=cap.strip() + "\n\n" + hashtags, **kw)


def card(icon, name, cat, amt, inc=False, badge=None):
    v = dict(icon=icon, name=name, cat=cat, amt=amt, inc=inc)
    if badge:
        v["badge"] = badge
    return ("card", v)


LINK = "\n👉 Crie sua conta grátis: link na bio."
SALVE = "💾 Salve este post para consultar depois."
