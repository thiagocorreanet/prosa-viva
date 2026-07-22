# Fonte canônica e divulgação progressiva da skill Refinar Prosa

## Contexto

Esta especificação registra a decisão arquitetural da issue #17, relacionada à
épica #1. O Prosa Viva precisa funcionar como plugin nativo do Codex e também
permitir instalação isolada da skill sem manter duas cópias do comportamento.

O catálogo editorial terá 33 padrões, exemplos e falsos positivos. Concentrar
todo esse conteúdo no `SKILL.md` aumentaria o contexto inicial e dificultaria a
manutenção. Duplicar a skill na raiz criaria risco de divergência entre a
instalação do plugin e a instalação independente.

## Decisão

O conjunto canônico será exclusivamente `skills/refinar-prosa/`:

```text
skills/refinar-prosa/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    ├── preservacao-autoral.md
    └── pt-BR/
        ├── conteudo.md
        ├── linguagem.md
        ├── formatacao.md
        ├── comunicacao.md
        └── estilo-avancado.md
```

Não haverá `SKILL.md` na raiz do repositório, cópia de compatibilidade, arquivo
gerado ou etapa de release que replique manualmente as instruções.

O manifesto do plugin continuará apontando para `./skills/`. A instalação
independente localizará a mesma pasta `skills/refinar-prosa/`, por descoberta do
repositório ou por seleção explícita da skill. Se uma ferramenta de instalação
não descobrir a estrutura aninhada, o fluxo deverá apontar para essa subpasta;
nunca criará uma segunda fonte na raiz.

## Alternativas consideradas

### Única skill canônica com referências por localidade — escolhida

Mantém o contrato editorial em um só lugar, reduz o contexto inicial, permite
instalação pelo plugin ou isoladamente e prepara novos idiomas sem duplicar o
núcleo.

### `SKILL.md` canônico na raiz com cópia dentro do plugin

Facilitaria algumas ferramentas genéricas de instalação, mas exigiria geração
ou sincronização e permitiria que plugin e skill isolada tivessem comportamentos
diferentes. Foi rejeitada.

### Catálogo completo dentro do `SKILL.md`

Eliminaria referências, porém carregaria todos os padrões e exemplos mesmo em
revisões simples. Também tornaria o arquivo central mais difícil de auditar. Foi
rejeitada.

## Responsabilidades dos arquivos

### `SKILL.md`

É a única entrada comportamental. Contém:

- frontmatter de descoberta;
- contrato editorial e política linguística;
- seleção dos modos texto colado, arquivo e embutido;
- ciclo leitura → rascunho → auditoria → versão final;
- resumo obrigatório de preservação factual, estrutural e autoral;
- mapa dos cinco grupos do catálogo;
- critérios para carregar cada referência diretamente;
- contrato de saída e condições de interrupção segura.

Não contém exemplos extensos nem a implementação completa dos 33 padrões.

### `agents/openai.yaml`

Contém somente apresentação e política de invocação. Nome, descrição curta e
prompt padrão podem resumir a skill, mas não definem regras editoriais. Nenhum
comportamento existe apenas nesse arquivo.

### `references/preservacao-autoral.md`

Contém falsos positivos, sinais autorais, regra de conjunto e auditoria de perda
de voz. O `SKILL.md` mantém os invariantes mínimos sempre visíveis e liga
diretamente essa referência. Antes de aplicar qualquer grupo numerado do
catálogo, a skill lê esta referência.

### `references/pt-BR/*.md`

Cada arquivo contém uma família do catálogo em português brasileiro:

| Arquivo | Padrões | Quando carregar |
| --- | ---: | --- |
| `conteudo.md` | 1–6 | importância, notoriedade, análise superficial, promoção, atribuição vaga ou fechamento formulaico |
| `linguagem.md` | 7–13 | recorrência lexical, verbos artificiais, paralelismo negativo, tríades, variação lexical, intervalos ou agente oculto |
| `formatacao.md` | 14–19 | travessões, negrito, listas, títulos, emojis ou aspas |
| `comunicacao.md` | 20–25 | resíduos de chatbot, especulação, servilismo, preenchimento, ressalvas ou conclusão genérica |
| `estilo-avancado.md` | 26–33 | hifenização, autoridade retórica, metadiscurso, documentação histórica, dramatização, aforismo ou falsa espontaneidade |

Os arquivos de referência não possuem frontmatter de skill e não são instalados
ou invocados independentemente.

## Regra de ligação direta

Toda referência necessária aparece como link direto no `SKILL.md`. Referências
não apontam para outras referências como requisito de execução.

```text
SKILL.md
  ├── references/preservacao-autoral.md
  ├── references/pt-BR/conteudo.md
  ├── references/pt-BR/linguagem.md
  ├── references/pt-BR/formatacao.md
  ├── references/pt-BR/comunicacao.md
  └── references/pt-BR/estilo-avancado.md
```

Uma revisão carrega somente os grupos cujos sinais candidatos aparecerem. Se
mais de um grupo for relevante, todos os grupos necessários podem ser lidos;
correção e preservação têm precedência sobre uma limitação artificial de
quantidade de arquivos.

## Orçamento de contexto e manutenção

Os limites serão verificáveis por linhas físicas:

- `SKILL.md`: no máximo 250 linhas;
- cada referência: no máximo 400 linhas;
- conjunto das seis referências: no máximo 2.000 linhas;
- `agents/openai.yaml`: no máximo 40 linhas.

O limite do conjunto é uma salvaguarda de manutenção, não uma instrução para
carregar todos os arquivos. O fluxo normal carrega o `SKILL.md`, a referência de
preservação antes do catálogo e somente os grupos relevantes.

Se um arquivo ultrapassar seu limite, a solução deve ser condensar exemplos ou
reorganizar o próprio grupo. Não é permitido criar encadeamento de referências,
duplicar regras ou esconder instruções indispensáveis fora do diretório
canônico.

## Instalação como plugin

O plugin usa a raiz atual do repositório:

```text
.codex-plugin/plugin.json
skills/refinar-prosa/SKILL.md
```

O campo `skills` do manifesto permanece `./skills/`. O validador de plugins deve
confirmar que o caminho existe e que a skill é descoberta. A instalação por
marketplace pertence à #21 e não altera a fonte canônica.

## Instalação somente como skill

A instalação isolada usa o mesmo diretório
`skills/refinar-prosa/`. A implementação da #17 verificará primeiro a descoberta
local com:

```bash
npx skills add . --list
```

Se a versão disponível da ferramenta suportar seleção por nome, o fluxo usará
`refinar-prosa`. Se a descoberta pela raiz não for suportada, o comando
documentado apontará diretamente para `./skills/refinar-prosa`. O teste decidirá
qual sintaxe é válida; uma cópia na raiz não será aceita como contorno.

A #11 só publicará o comando exato depois desse teste. A instalação isolada não
inclui o manifesto do plugin nem `agents/openai.yaml` como contratos separados;
o comportamento continua integralmente definido pelo mesmo `SKILL.md` e suas
referências.

## Impacto nos designs e planos existentes

Os documentos das issues #5–#10 atualmente usam caminhos planos, como
`references/conteudo.md`. Antes de executar esses planos, a implementação da #17
deve atualizar todas as referências de grupos para o namespace `pt-BR`:

```text
references/conteudo.md
→ references/pt-BR/conteudo.md
```

O mesmo vale para `linguagem.md`, `formatacao.md`, `comunicacao.md` e
`estilo-avancado.md`. `preservacao-autoral.md` permanece fora do namespace por
ser parte do núcleo editorial, não uma regra exclusiva de localização.

Essa atualização será mecânica nos designs e planos ainda não executados. Não
será criada uma fase de compatibilidade com os caminhos antigos.

## Fluxo de descoberta

### Plugin

```text
plugin.json
  → ./skills/
  → refinar-prosa/SKILL.md
  → contrato central
  → preservação autoral
  → referências pt-BR relevantes
```

### Skill independente

```text
instalador de skills
  → skills/refinar-prosa/
  → SKILL.md
  → o mesmo contrato e as mesmas referências
```

Os dois fluxos convergem antes de qualquer regra editorial. Não existe camada de
adaptação comportamental específica do plugin.

## Falhas e comportamento seguro

- Referência ligada mas ausente: a validação falha; a versão não deve ser
  distribuída.
- Referência acima do orçamento: a validação falha; o conteúdo deve ser
  condensado antes do merge.
- Instalador independente não descobre a raiz: usar a subpasta canônica se a
  ferramenta aceitar caminho local; não duplicar a skill.
- Ferramenta não suporta instalação da subpasta: documentar instalação isolada
  como indisponível nessa ferramenta/versão até existir um fluxo verificável.
- Divergência entre apresentação e comportamento: o `SKILL.md` prevalece, e os
  metadados devem ser corrigidos.

## Validação

A implementação deverá verificar:

1. existe exatamente um `SKILL.md` do produto;
2. não existe `SKILL.md` na raiz;
3. o manifesto aponta para `./skills/`;
4. todos os seis links do `SKILL.md` existem e são relativos;
5. nenhuma referência exige leitura encadeada de outra;
6. os limites de linhas são respeitados;
7. os planos #5–#10 usam caminhos `references/pt-BR/`;
8. o validador de Agent Skills aceita `skills/refinar-prosa/`;
9. o validador de plugins aceita a raiz;
10. `npx skills add . --list`, quando suportado, encontra `refinar-prosa`;
11. a instalação isolada não cria ou depende de uma segunda cópia.

## Relação com as próximas issues

- #19 formaliza pt-BR como único idioma da v1 e o comportamento para entradas
  não suportadas, usando o namespace definido aqui.
- #21 cria o ciclo de marketplace, cachebuster, reinstalação e teste sem alterar
  a fonte canônica.
- #11 documenta os dois caminhos somente depois de #17, #19 e #21 terem sido
  implementados e verificados.

## Fora de escopo

- implementar agora os padrões 1–33;
- adicionar inglês ou outro catálogo;
- criar marketplace ou cachebuster;
- publicar comandos de instalação ainda não testados;
- adicionar MCP, app, hook, asset ou segundo plugin;
- manter compatibilidade com caminhos de referência ainda não implementados.
