"""Gera uma prévia: python3 tools/build.py tools/clientes/<slug>.json
O JSON tem o CONFIG do site + "slug" (pasta/URL) e, opcionalmente, "pasta" (padrão: raiz).
Fotos: caminhos relativos à pasta da prévia (ex.: "img/1.jpg")."""
import json, html, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
T = open(os.path.join(ROOT, 'tools/template.html')).read()
DEF = dict(cidade="", endereco="", horarioTexto="Terça a sábado, 9h às 19h", diasAtendimento=[2,3,4,5,6],
  horarios=["09:00","10:30","13:00","14:30","16:00","17:30"], nota="5,0", notaTexto="Avaliações das clientes",
  mostrarSeloPrevia=True, numeros=[], depoimentos=[], faq=[], portfolio=[], instagram="", whatsapp="5521999999999",
  fraseFinal="Garanta seu horário <em>agora</em>")

def build(cfg):
    c = dict(DEF); c.update(cfg)
    slug = c.pop('slug'); pasta = c.pop('pasta', '')
    out = os.path.join(ROOT, pasta, slug); os.makedirs(out, exist_ok=True)
    depth = len([p for p in (pasta + '/' + slug).split('/') if p])
    title = f"{c['nome']} · {c['nicho']}" + (f" em {c['cidade']}" if c['cidade'] else '')
    s = (T.replace('__BASE__', '../' * depth)
          .replace('__CONFIG__', json.dumps(c, ensure_ascii=False, indent=1))
          .replace('__TITLE__', html.escape(title)).replace('__DESC__', html.escape(c.get('subtitulo', ''))))
    open(os.path.join(out, 'index.html'), 'w').write(s)
    return os.path.join(pasta, slug)

if __name__ == '__main__':
    for f in sys.argv[1:]:
        print('ok', build(json.load(open(f))))
