# wally-posts

Artes e legendas do Instagram [@wally_financeiro](https://instagram.com/wally_financeiro), de
05/10/2026 a 01/10/2027. O próprio repositório é o agendador: um workflow do GitHub Actions lê os
JSONs e publica na hora marcada, sem depender de nenhuma máquina ligada.

> **Desde 05/10/2026 a publicação não é mais feita por aqui.** Os itens foram importados para o
> agendador `posts_automatic`, que publica a partir dos mesmos links. Os workflows foram movidos para
> `.github/workflows-desativados/` e não rodam mais; o `published.json` deixou de ser atualizado. As
> seções sobre o Actions abaixo ficam só como histórico. As artes e vídeos continuam sendo servidos
> daqui: **não apague nem renomeie** os arquivos de `posts/`, `reels/` e `stories/`.

## Conteúdo

- `posts/` — artes do feed (1080×1350). **Não apague nem renomeie**: as publicações apontam para esses links.
- `stories/` — artes dos stories (1080×1920).
- `posts.json` — data, template, arte e legenda de cada post. Posts saem às **12:00** (horário de São Paulo).
- `posts-extra.json` — posts avulsos no mesmo formato (000a em 02/10 e 000b em 05/10), publicados junto com os do `posts.json`. O 001 foi adiantado e publicado à mão em 30/09.
- `reels/` — Reels em vídeo (1080×1920, MP4 H.264 + AAC), já com a trilha original embutida. **Não apague nem renomeie**: a publicação aponta para esses links.
- `reels.json` — data, horário (19:00, terça e quinta) e legenda de cada Reel (outubro a dezembro/2026, 26 vídeos). Os vídeos são gerados por `video/engine.html`, `video/reels_spec.py` e `video/render_engine.py` (as músicas, por `video/music.py`).
- `stories.json` — data, **horário** e arte de cada story.
- `published.json` — o que já foi publicado, gravado pelo próprio workflow. Serve para não repetir post.
- `tools/` — conteúdo (`q1.py` a `q4.py`) e geradores das artes (`build.py`, `render.py`, `build_stories.py`).

Para mudar um post: edite o `q*.py`, rode `python3 tools/build.py && python3 tools/render.py <id>` e
converta o PNG em `posts/<id>.jpg`.

## Publicação automática

`publish.py` roda a cada 30 minutos pelo Actions. Ele publica o que já venceu e ainda não está no
`published.json`, e grava o resultado de volta no repositório.

Itens atrasados mais de **3 horas são ignorados** de propósito: se o workflow ficar quebrado por
dias, ninguém quer que ele despeje uma semana de stories de uma vez ao voltar.

### Configuração (uma vez)

Em *Settings → Secrets and variables → Actions*, crie:

| Secret | O que é |
| ------ | ------- |
| `IG_ACCESS_TOKEN` | Token da conta. No painel da Meta: *API do Instagram → Gerar tokens de acesso → Gerar token*. |
| `IG_USER_ID` | ID da conta do Instagram (`17841427529757454`). |
| `GH_PAT` | PAT fine-grained com permissão **Secrets: read and write** neste repositório. Só é usado para renovar o token. |

Depois, em *Actions → Publicar no Instagram → Run workflow*, marque **Simular sem publicar** para
conferir o que ele faria antes de deixar no automático.

### Token

O token do Instagram expira em **60 dias**. O workflow `Renovar token do Instagram` roda todo dia 1
e grava o token novo no secret sozinho. Se falhar, ele abre uma issue avisando — se ninguém renovar,
as publicações param.

### Limites

A API do Instagram aceita 100 publicações por 24h; a grade usa no máximo 5 por dia. Stories via API
não suportam legenda, figurinhas, música nem enquete — só a imagem.
