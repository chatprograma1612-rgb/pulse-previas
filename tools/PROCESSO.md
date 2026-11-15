# Processo: criar e enviar a prévia de uma cliente

Repositório: `chatprograma1612-rgb/pulse-previas` (GitHub Pages, branch `main`, raiz).
Link público: `https://chatprograma1612-rgb.github.io/pulse-previas/<slug>/`

## 1. Dados da cliente
Vêm da conversa no Direct (@pulse_studio.presenca_digital) e do perfil público dela:
nome do negócio, nicho, cidade/bairro/endereço, WhatsApp, serviços e preços, cores, bio, se autorizou usar as fotos.

## 2. Montar o JSON
- `slug`: nome do negócio em minúsculas, sem acento, com hífens (ex.: `studio-ana-nails`). Se já existir a pasta, acrescente `-2`.
- Copie o modelo do nicho mais próximo de `tools/modelos/` (nail-designer, lash-designer, salao-de-beleza, estetica) para `tools/clientes/<slug>.json`, apague `"pasta"` e troque:
  - `slug`, `nome`, `nicho`, `instagram` (sem @), `cidade`, `endereco` (ou só bairro e cidade), `whatsapp` (só números com 55 + DDD; se ela não passou, use o link da bio; se não houver, mantenha o padrão e avise a dona), `horarioTexto` e `diasAtendimento` se ela informou.
  - `titulo` (com uma parte em `<em>...</em>`), `subtitulo`, `fraseFinal`: escritos para o negócio dela, curtos e vendedores.
  - `cores.principal` = cor da marca dela; `cores.clara` = tom claro da mesma cor; `cores.fundo` = tom quase preto puxado para a cor; `cores.suave` = tom escuro intermediário.
  - `servicos` = os serviços dela (ícone emoji, nome, duração se souber, descrição curta, preço; sem preço → "Consulte").
  - `numeros`: só números verdadeiros que aparecem no perfil (ex.: seguidores, anos de experiência citados na bio). Se não houver, use `[]`.
  - `nota`/`notaTexto`: só se ela mostrar avaliação real; senão `nota: "5,0"` e `notaTexto: "O que as clientes dizem"`.
  - `depoimentos`: só depoimentos reais (prints ou comentários de clientes no perfil dela, com primeiro nome). Se não houver, `[]` (a seção mostra só o título; nunca invente depoimento).
  - `faq`: adapte ao negócio dela.
  - `mostrarSeloPrevia: true`.

## 3. Fotos
Se ela autorizou usar as fotos (ou se a conversa já deixou claro que ela quer o site com o trabalho dela):
- Para cada post escolhido (6 a 10, os mais bonitos e nítidos), abra o post no Chrome. Rode no Instagram:
  `const im=[...document.querySelectorAll('article img, main img')].sort((a,b)=>b.naturalWidth-a.naturalWidth)[0]; setTimeout(()=>location.href=im.currentSrc||im.src,100)`
  (a aba vai para a imagem no servidor do Instagram).
- Chame `init_upload` do Runway com filename `<slug>-N.jpg`, mimeType image/jpeg e um fileSize provisório; depois, na aba da imagem, rode o JS que redimensiona (máx. 1200 px, JPEG 0,85) e faça PUT no uploadUrl. ATENÇÃO: o fileSize do init_upload precisa ser o tamanho exato do blob. Então primeiro rode o redimensionamento, guarde em `window.__b` e leia `window.__b.size`; só então chame `init_upload` com esse tamanho e faça o PUT de `window.__b`.
  Para ler o ETag (a ferramenta esconde textos parecidos com base64), devolva `etag.match(/.{1,4}/g).join(' ')` e junte de novo sem espaços.
- `complete_upload` → URL do asset → `curl -o <slug>/img/N.jpg "<url>"` no workspace.
- `fotoCapa` = a melhor foto (de preferência ela trabalhando ou o resultado mais bonito); `portfolio` = as outras, com `cat` por técnica/serviço.
Se não autorizou ou não deu para baixar: use as fotos do modelo do nicho (copie de `modelos/<nicho>/img/`).

## 4. Gerar, conferir e publicar
- `python3 tools/build.py tools/clientes/<slug>.json`
- Teste local: `python3 -m http.server` e abra `/<slug>/` com Playwright (`/usr/bin/google-chrome`, args `--use-angle=swiftshader --enable-unsafe-swiftshader`) em 390x844 e 1440x900; confira o print (nome certo, fotos carregando, nada cortado).
- Commit (`git -c user.name="Pulse Studio" -c user.email="noreply@anthropic.com" commit`) e `git -c push.negotiate=true push origin main`.
- Espere ~1 min e abra o link público no Chrome para confirmar que carregou.

## 5. Enviar no Direct
"[Nome], sua prévia ficou pronta! 💜✨ Dá uma olhada (abre no celular): https://chatprograma1612-rgb.github.io/pulse-previas/<slug>/
É só uma prévia pra você ver como seu site pode ficar: dá pra mudar cores, textos, fotos e serviços do jeitinho que você quiser. Me conta o que achou?"
Depois: registre no resumo para a dona (nome, @, link).
