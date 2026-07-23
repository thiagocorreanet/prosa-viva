# Distribuição pública e primeira release do Prosa Viva

## Contexto

Esta especificação registra a decisão da issue #16 depois da conclusão do fluxo
local da #21. O repositório já contém um plugin Codex válido na raiz, com
identificador `prosa-viva`, versão `0.1.0` e a skill canônica em
`skills/refinar-prosa/`. Ainda não há licença no checkout, tag, GitHub Release,
marketplace público nem automação de publicação.

A primeira distribuição deve permitir que uma pessoa instale o plugin a partir
do GitHub sem clonar o projeto, montar staging ou editar configurações internas
do Codex.

## Decisão

Transformar o próprio repositório em um marketplace Git de um único plugin. O
marketplace aponta para o plugin na raiz do mesmo repositório por uma fonte
remota `url`, fixada na tag imutável `v0.1.0`.

O fluxo público será:

```text
main validada
  → tag anotada v0.1.0
  → workflow valida tag, manifesto, marketplace e pacote
  → workflow gera ZIP e SHA-256
  → workflow cria a GitHub Release
  → usuário instala pelo marketplace Git
```

Os comandos públicos serão:

```bash
codex plugin marketplace add thiagocorreanet/prosa-viva
codex plugin add prosa-viva@prosa-viva
```

Depois da instalação, o usuário abre uma conversa nova e invoca
`$refinar-prosa`.

## Alternativas consideradas

### Marketplace e plugin no mesmo repositório — escolhida

Mantém uma única fonte do plugin, permite instalação em dois comandos e usa a
capacidade do Codex de carregar um plugin localizado na raiz de uma fonte Git.

### Marketplace em repositório separado

Facilitaria reunir vários plugins, mas introduziria sincronização entre dois
repositórios antes de existir um segundo pacote. Foi rejeitada por enquanto.

### Marketplace apontando para `main`

Evitaria atualizar a referência a cada versão, mas uma instalação deixaria de
ser reproduzível e poderia mudar sem uma nova release. Foi rejeitada.

## Estrutura versionada

Serão adicionados:

```text
.agents/plugins/marketplace.json
.github/workflows/validate.yml
.github/workflows/release.yml
docs/releases/v0.1.0.md
LICENSE
scripts/validate_release.py
tests/test_validate_release.py
```

Também serão atualizados `.codex-plugin/plugin.json` e `README.md`. Não serão
criados MCP, app, hooks, manifestos do Claude nem assets vazios.

## Marketplace Git

`.agents/plugins/marketplace.json` terá nome e identidade `prosa-viva`. Sua
única entrada também se chamará `prosa-viva` e incluirá:

- fonte `url` em `https://github.com/thiagocorreanet/prosa-viva.git`;
- referência `v0.1.0`;
- instalação `AVAILABLE`;
- autenticação `ON_INSTALL`;
- categoria `Productivity`.

A fonte remota aponta para a raiz do repositório; não haverá cópia em
`plugins/prosa-viva`. Em releases futuras, a mudança de versão atualizará em um
mesmo commit o manifesto, a referência do marketplace e as notas da versão.

## Versão e licença

A primeira versão pública será `0.1.0`, publicada como tag anotada `v0.1.0`.
Cachebusters `+codex.local-*` continuam exclusivos do staging de desenvolvimento
e são rejeitados pela validação pública.

O projeto adotará a licença MIT, com copyright de 2026 em nome de Thiago Corrêa.
O campo `license` do manifesto permanecerá `MIT`. O README deixará de dizer que
a licença está indefinida.

## Metadados públicos

O manifesto continuará declarando somente componentes existentes. Autoria,
repositório e website apontarão para `thiagocorreanet/prosa-viva`; o nome de
autor será alinhado a `Thiago Corrêa`.

Não serão declarados ícones, logos, screenshots, política de privacidade ou
termos de serviço nesta release, pois o pacote não coleta dados, não inclui app
ou MCP e esses arquivos não existem. A interface textual atual será preservada
e validada.

## Validador de release

`scripts/validate_release.py` será uma ferramenta Python sem dependências
externas. Ela aceitará `--tag` quando executada durante uma release e verificará:

- manifesto e marketplace são objetos JSON válidos;
- nomes do plugin, marketplace e pasta são `prosa-viva`;
- versão do manifesto é SemVer estrita e não contém cachebuster;
- tag recebida é exatamente `v<versão-do-manifesto>`;
- referência do marketplace é a mesma tag;
- origem Git, autoria, repositório, licença, políticas e categoria são exatos;
- `LICENSE`, `README.md`, skill e configuração do agente existem;
- caminhos declarados permanecem dentro do plugin e apontam para conteúdo real;
- não existem manifestos do Claude, placeholders ou componentes vazios;
- o arquivo de notas `docs/releases/<tag>.md` existe quando há tag.

Sem `--tag`, o validador usa a versão do manifesto para conferir a referência e
as notas esperadas. Isso permite executar a mesma política em desenvolvimento e
na automação.

## Testes

`tests/test_validate_release.py` criará pacotes temporários e cobrirá pelo menos:

- pacote público válido;
- divergência entre tag e versão;
- referência de marketplace divergente;
- cachebuster em versão pública;
- licença ausente ou incompatível;
- placeholder e manifesto do Claude;
- componente ou caminho declarado sem arquivo correspondente.

A suíte existente continuará cobrindo staging, documentação local e arquitetura
da skill.

## Workflow de validação

`.github/workflows/validate.yml` rodará em pull requests e pushes para `main`,
com permissão somente de leitura. Usará versões oficiais de
`actions/checkout` e `actions/setup-python` fixadas por SHA completo e executará:

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate_skill_architecture.py
python3 scripts/validate_release.py
```

O workflow não cria tags, releases ou arquivos no repositório.

## Workflow de release

`.github/workflows/release.yml` será acionado apenas por tags compatíveis com
`v*.*.*`. A permissão `contents: write` ficará limitada ao job de publicação.

O job fará checkout da tag, configurará Python, repetirá toda a validação e
executará `scripts/validate_release.py --tag "$GITHUB_REF_NAME"`. Somente depois
disso criará:

```text
prosa-viva-v0.1.0.zip
prosa-viva-v0.1.0.zip.sha256
```

O ZIP conterá apenas `.codex-plugin/`, `skills/`, `README.md` e `LICENSE`, sob
uma pasta superior `prosa-viva/`. Documentação interna, testes, evals, GitHub
Actions e caches não farão parte do asset.

A release será criada com `gh release create`, `--verify-tag`, título
`Prosa Viva v0.1.0` e notas de `docs/releases/v0.1.0.md`. Nenhuma Action de
terceiros será usada para publicar.

## Notas da v0.1.0

As notas serão originais, em português, e registrarão:

- revisão de prosa em pt-BR;
- preservação factual e de conteúdo protegido;
- modos de texto colado, arquivo e embutido;
- instalação como plugin e como skill;
- suporte oficial somente a pt-BR na série `0.1.x`;
- ausência de promessa sobre detectores, autoria humana ou verificação factual;
- natureza inicial da versão e canais de feedback.

## README público

A instalação pública substituirá o fluxo local como orientação principal. O
README separará:

1. instalação do plugin via marketplace Git;
2. atualização e remoção públicas;
3. instalação independente da skill;
4. desenvolvimento local com staging e cachebuster.

Também exibirá status `v0.1.0`, licença MIT e link para a release. Nenhum comando
específico do Claude será citado.

## Publicação inicial

Depois que os arquivos forem enviados para `main`:

1. aguardar o workflow de validação concluir com sucesso;
2. criar a tag anotada `v0.1.0` no commit validado;
3. enviar somente essa tag;
4. aguardar o workflow de release;
5. confirmar release, ZIP e checksum no GitHub;
6. adicionar o marketplace Git em um ambiente limpo;
7. instalar `prosa-viva@prosa-viva`;
8. abrir uma sessão efêmera nova e invocar `$refinar-prosa`;
9. fechar a issue #16 somente se todas as verificações passarem.

## Falhas e recuperação

- Validação em `main` falha: não criar a tag.
- Workflow da tag falha: preservar a tag e os logs; corrigir em uma versão de
  patch, sem mover ou recriar a tag pública.
- Release já existe: `gh release create` falha, evitando sobrescrita silenciosa.
- Instalação pública falha: manter a issue aberta e não recomendar o fluxo no
  README como verificado.
- Asset diverge do checkout: falhar antes de criar a release.

Tags e releases publicadas são tratadas como imutáveis. Não haverá force-push de
tag nem edição manual do cache do Codex.

## Segurança

Os workflows usarão apenas `GITHUB_TOKEN`, com a menor permissão necessária. As
Actions oficiais serão fixadas por SHA completo. O empacotamento não executará
código do plugin nem instalará dependências externas. Segredos adicionais não
serão necessários.

## Fora de escopo

- submissão ao diretório público curado da OpenAI;
- marketplace com vários plugins;
- publicação em npm;
- assinatura criptográfica do asset;
- app, MCP, hook ou autenticação externa;
- identidade visual que dependa de assets ainda inexistentes.
