# Pulse Studio · Prévias de sites

Prévias gratuitas enviadas às clientes no Instagram da Pulse Studio.
Link de cada prévia: `https://chatprograma1612-rgb.github.io/pulse-previas/<slug>/`

## Como criar uma prévia
1. Crie `tools/clientes/<slug>.json` copiando um modelo de `tools/modelos/` (mesmo nicho).
2. Coloque as fotos em `<slug>/img/` e aponte `fotoCapa` e `portfolio[].foto` para `img/...`.
3. Rode `python3 tools/build.py tools/clientes/<slug>.json` e publique (commit + push na `main`).

Modelos de demonstração: `modelos/nail-designer`, `modelos/lash-designer`, `modelos/salao-de-beleza`, `modelos/estetica`.
Depoimentos e notas marcados "(exemplo)" devem ser removidos ou trocados pelos reais.
