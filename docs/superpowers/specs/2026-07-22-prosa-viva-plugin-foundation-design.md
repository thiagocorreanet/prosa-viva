# Fundação instalável do plugin Prosa Viva

## Contexto

Esta especificação detalha a fundação mínima instalável do Prosa Viva como
plugin nativo do Codex, relacionada à épica #1. A entrega substitui
funcionalmente os manifestos específicos do Claude usados pelo projeto de
referência, sem copiá-los nem incluí-los no repositório.

O repositório ainda não possui um pacote de plugin. A fundação deve ser pequena,
funcional e compatível com a evolução planejada nas issues #16, #17, #19 e #21.

## Decisões adotadas

- O identificador estável do plugin é `prosa-viva`.
- A versão semântica inicial é `0.1.0`.
- A licença declarada no manifesto é `MIT`; a publicação do arquivo de licença e
  sua revisão jurídica permanecem no escopo de #16.
- A autoria pública é `thiagocorreanet`.
- A única fonte canônica da skill fica em `skills/refinar-prosa/`.
- Não haverá uma segunda cópia de `SKILL.md` na raiz.
- A versão inicial suporta oficialmente apenas português brasileiro.
- A skill pode ser invocada explícita ou implicitamente.
- Esta entrega contém somente componentes reais. MCP, apps, hooks, assets,
  marketplace e referências modulares não serão declarados nem criados.
- A instalação por marketplace e o teste em uma nova sessão permanecem no
  escopo de #21.

## Alternativas consideradas

### Fundação funcional enxuta — escolhida

Cria somente os três arquivos pedidos e inclui um contrato editorial conciso,
mas utilizável. Entrega um plugin validável sem antecipar o catálogo completo de
padrões.

### Esqueleto estritamente estrutural

Criaria manifestos válidos e quase nenhum comportamento editorial. Foi rejeitado
porque ficaria próximo de um placeholder e não demonstraria a função real da
skill.

### Fundação modular antecipada

Criaria desde já arquivos em `references/` para idiomas, contrato e padrões. Foi
rejeitada porque ampliaria o escopo desta fundação e anteciparia decisões das
issues editoriais e de divulgação progressiva.

## Arquitetura

```text
prosa-viva/
├── .codex-plugin/
│   └── plugin.json
└── skills/
    └── refinar-prosa/
        ├── SKILL.md
        └── agents/
            └── openai.yaml
```

### `.codex-plugin/plugin.json`

É o contrato de instalação, descoberta e apresentação do plugin. O manifesto:

- usa `prosa-viva` em `name`;
- usa `0.1.0` em `version`;
- aponta `skills` para `./skills/`;
- contém descrição, autoria, repositório, homepage, licença e palavras-chave;
- contém todos os metadados de interface exigidos pelo validador;
- não declara `id`, pois `name` já é o identificador estável;
- não declara caminhos ou integrações que não existam.

Metadados planejados:

| Campo | Valor ou regra |
| --- | --- |
| `name` | `prosa-viva` |
| `version` | `0.1.0` |
| `description` | `Revisa textos em português brasileiro com clareza, naturalidade e preservação factual.` |
| `author.name` | `thiagocorreanet` |
| `author.url` | `https://github.com/thiagocorreanet` |
| `homepage` | `https://github.com/thiagocorreanet/prosa-viva` |
| `repository` | `https://github.com/thiagocorreanet/prosa-viva` |
| `license` | `MIT` |
| `keywords` | `["escrita", "revisão", "português", "pt-BR", "prosa"]` |
| `skills` | `./skills/` |

O bloco `interface` terá:

- `displayName`: `Prosa Viva`;
- `shortDescription`: `Refina prosa em pt-BR sem perder fatos ou voz`;
- `longDescription`: `Revisa textos em português brasileiro para melhorar
  clareza, concisão, ritmo e naturalidade, preservando fatos, estrutura e voz.`;
- `developerName`: `thiagocorreanet`;
- `category`: `Productivity`;
- `capabilities`: somente `Write`;
- `websiteURL`: o repositório público;
- dois prompts iniciais: `Use $refinar-prosa para revisar este texto em pt-BR
  sem alterar os fatos.` e `Use $refinar-prosa para revisar este arquivo e
  preservar sua estrutura.`.

Serão omitidos email, política de privacidade, termos de serviço, cor de marca,
ícones, logos e screenshots, pois esses valores ou arquivos ainda não existem.

### `skills/refinar-prosa/SKILL.md`

É a única fonte canônica do comportamento editorial. O frontmatter contém:

- `name: refinar-prosa`;
- `description: Use para revisar e reescrever prosa em português brasileiro, em
  texto colado ou arquivos, melhorando clareza e naturalidade sem alterar fatos,
  estrutura protegida ou voz.`

O corpo define um fluxo mínimo e funcional:

1. Confirmar que existe texto ou arquivo legível para revisar.
2. Identificar se a prosa está em português brasileiro.
3. Preservar fatos, nomes, números, datas, citações, ressalvas e grau de certeza.
4. Em arquivos, proteger frontmatter, links, tabelas e blocos de código.
5. Melhorar clareza, concisão, ritmo e naturalidade sem uniformizar a voz.
6. Não inventar informações nem alterar texto que já esteja adequado.
7. Auditar a revisão contra a fonte antes de responder.
8. Entregar somente o texto revisado, exceto quando o usuário pedir explicações.

O arquivo inclui exemplos curtos de texto colado e edição de arquivo, ambos com
`$refinar-prosa`. Calibração detalhada de voz, catálogo de padrões e referências
progressivas ficam fora desta entrega.

### `skills/refinar-prosa/agents/openai.yaml`

Controla a apresentação e a invocação da skill no Codex:

```yaml
interface:
  display_name: "Refinar Prosa"
  short_description: "Revise prosa em pt-BR sem perder fatos ou voz"
  default_prompt: "Use $refinar-prosa para revisar o texto abaixo em português brasileiro, preservando fatos, estrutura e voz."

policy:
  allow_implicit_invocation: true
```

`Prosa Viva` identifica o plugin; `Refinar Prosa` identifica a ação oferecida
pela skill. Não haverá dependências ou assets declarados.

## Fluxo de execução

```text
Codex lê plugin.json
  → descobre ./skills/
  → carrega refinar-prosa
  → apresenta os metadados de openai.yaml
  → invoca a skill explícita ou implicitamente
  → SKILL.md orienta revisão e auditoria
  → entrega texto revisado ou edita o arquivo solicitado
```

Não há estado persistente, serviço externo ou fluxo de dados adicional. A skill
opera somente sobre a entrada ou os arquivos que o usuário colocou no escopo.

## Idiomas e comportamento previsível

- Português brasileiro é o único idioma oficialmente suportado em `0.1.0`.
- Textos claramente escritos em outro idioma não são modificados; a skill
  informa brevemente que o idioma ainda não é suportado.
- Em documentos mistos, apenas a prosa em pt-BR é revisada. Código, citações e
  trechos estrangeiros são preservados.
- A skill não promete detecção de IA, verificação factual nem revisão técnica,
  jurídica ou acadêmica especializada.

## Tratamento de falhas

- Sem texto ou caminho: solicitar a entrada necessária.
- Arquivo inexistente ou ilegível: informar o caminho problemático sem alterar
  outros arquivos.
- Idioma não suportado: informar o limite da versão sem modificar a entrada.
- Instruções conflitantes: priorizar preservação factual e pedir esclarecimento
  somente quando não houver interpretação segura.
- Risco de alterar estrutura protegida: preservar o trecho em vez de improvisar.
- Nenhuma melhoria necessária: devolver o original ou informar que não há
  mudança útil.

## Validação

A implementação deve executar:

1. O validador de plugins fornecido pela skill `plugin-creator` contra a raiz do
   repositório.
2. O validador de Agent Skills contra `skills/refinar-prosa/`.
3. Validação sintática de JSON e YAML.
4. Verificação de que todos os caminhos relativos permanecem dentro do pacote e
   apontam para conteúdo existente.
5. Busca por placeholders, referências a Claude e declarações de componentes
   ausentes.
6. `git diff --check`.

O teste de instalação por marketplace e a confirmação em uma nova sessão do
Codex não fazem parte desta entrega e serão cobertos por #21.

## Critérios de aceite verificáveis

- A raiz do pacote e o campo `name` usam `prosa-viva`.
- `skills` resolve de `./skills/` para a pasta real de skills.
- O frontmatter de `SKILL.md` possui `name` e `description` não vazios.
- `openai.yaml` possui nome de apresentação, descrição curta e prompt padrão com
  menção literal a `$refinar-prosa`.
- O validador de plugins aceita o pacote.
- Não existem placeholders nem metadados específicos do Claude.
- O manifesto não declara MCP, apps, hooks ou assets.

## Impacto nas dependências

- #17: registra `skills/refinar-prosa/` como fonte canônica e proíbe duplicação
  na raiz para esta versão.
- #19: registra pt-BR como único idioma oficialmente suportado em `0.1.0` e
  define a resposta para idiomas não suportados.
- #16: define para esta versão `0.1.0`, MIT, autoria e metadados públicos reais;
  licença publicada, identidade visual e requisitos adicionais de distribuição
  continuam nessa issue.
- #21: permanece responsável pelo marketplace, instalação, reinstalação e teste
  em nova sessão.
