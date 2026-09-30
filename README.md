# wally-posts

Artes e legendas dos posts do Instagram [@wally_financeiro](https://instagram.com/wally_financeiro), de 05/10/2026 a 01/10/2027 (seg, qua e sex).

- `posts/` — as imagens (1080×1350) que o Metricool publica. **Não apague nem renomeie**: os posts agendados apontam para esses links.
- `posts.json` — data, template, arte e legenda de cada post.
- `tools/` — conteúdo (`q1.py` a `q4.py`) e o gerador das artes (`build.py`, `render.py`).

Para mudar um post: edite o `q*.py`, rode `python3 tools/build.py && python3 tools/render.py <id>` e converta o PNG em `posts/<id>.jpg`.
