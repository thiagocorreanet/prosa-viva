# Padrões de formatação e estilo visual 14–19 da skill Refinar Prosa

## Contexto

Esta especificação detalha o terceiro grupo do catálogo editorial do
`refinar-prosa`, relacionado à issue #7 e à épica #1. O grupo cobre seis
padrões de formatação e estilo visual em português brasileiro sem converter
preferências editoriais em proibições absolutas.

A implementação depende do contrato editorial da #3 e da estrutura de catálogo
iniciada na #5. A calibração de voz da #4 é complementar, mas não obrigatória.

## Decisão de arquitetura

As regras ficarão em uma referência própria:

```text
skills/refinar-prosa/
├── SKILL.md
└── references/
    ├── conteudo.md
    ├── linguagem.md
    └── formatacao.md

README.md
```

Responsabilidades:

- `skills/refinar-prosa/references/formatacao.md`: fonte canônica dos padrões
  14–19, seus limites, exemplos e regras de preservação estrutural.
- `skills/refinar-prosa/SKILL.md`: mapa de números e nomes, sinais para triagem
  e ligação direta para a referência.
- `README.md`: resumo público com números e nomes estáveis.

O arquivo será carregado quando houver repetição formulaica de travessões,
negrito mecânico, listas verticais que dificultem a leitura, capitalização de
títulos incompatível com o documento, emojis meramente decorativos ou aspas
inconsistentes com a convenção observada.

## Alternativas consideradas

### Referência contextual por família — escolhida

Separa estilo visual de linguagem e permite declarar uma regra transversal de
preservação de Markdown. Também mantém a leitura seletiva e a numeração global.

### Normalizador rígido de estilo

Aplicaria uma convenção única de travessão, títulos, aspas e listas. Foi
rejeitado porque a amostra do autor e as convenções do documento têm precedência.

### Regras no contrato editorial

Garantiria ampla visibilidade, mas inflaria a seção central com decisões que só
se aplicam quando existem sinais visuais. Foi rejeitada.

## Hierarquia de decisão

Antes de aplicar qualquer padrão, a skill seguirá esta prioridade:

```text
instrução explícita do usuário
  → convenção consistente do documento
  → amostra de voz do autor
  → convenção do gênero e do idioma
  → preferência editorial padrão da skill
```

Nenhum sinal isolado justifica reformatar o texto. Travessões, negrito, listas,
maiúsculas, emojis e aspas podem ser escolhas legítimas. A revisão só ocorre
quando a repetição é mecânica, a função é decorativa ou a inconsistência
prejudica a leitura.

## Contrato de preservação estrutural

Em edições de arquivo, permanecem intactos:

- frontmatter e delimitadores;
- destinos de links e referências;
- tabelas, cercas e conteúdo de código;
- comandos, opções, nomes de arquivo e dados;
- sintaxe Markdown necessária à estrutura;
- listas que facilitam consulta ou execução.

A skill pode editar somente a prosa dentro de títulos, itens, legendas ou texto
de links quando isso não muda estrutura, destino ou semântica protegida. Nunca
deve converter automaticamente tabela em prosa, lista operacional em parágrafo
ou código em texto corrido.

## Esquema obrigatório por padrão

Cada padrão em `formatacao.md` terá problema, sinais candidatos, confirmação
contextual, falsos positivos, exemplo antes/depois e preservação estrutural e
semântica. Números e nomes serão repetidos no `SKILL.md` e no README; os demais
detalhes existirão somente na referência.

## Padrão 14 — Travessões formulaicos ou excessivos

### Problema

Usa travessões em sequência como molde automático para apartes, conclusões ou
explicações que poderiam seguir a pontuação e a cadência do documento.

### Aplicação contextual

Revisar apenas quando a recorrência chamar mais atenção que as relações entre
as ideias. Manter travessões isolados, diálogos, incisos expressivos e a
convenção consistente do autor.

### Exemplo de direção

Antes:

```text
O relatório foi entregue — dentro do prazo. A equipe respondeu — sem atraso. O
cliente aprovou — sem ressalvas.
```

Depois:

```text
O relatório foi entregue dentro do prazo. A equipe respondeu sem atraso, e o
cliente aprovou sem ressalvas.
```

Permanecem prazo, resposta e aprovação. Saem apenas as pausas repetidas sem
função; um travessão legítimo em outro trecho não seria removido por associação.

## Padrão 15 — Negrito mecânico

### Problema

Marca palavras ou rótulos em negrito de forma repetitiva, sem hierarquia
informativa ou necessidade de consulta.

### Aplicação contextual

Reduzir somente quando quase todo item recebe destaque automático e o negrito
deixa de comunicar prioridade. Manter ênfase intencional, termos definidos,
avisos e convenções existentes.

### Exemplo de direção

Antes:

```markdown
O comando exige uma **chave** e retorna uma **resposta** em formato **JSON**.
```

Depois:

```markdown
O comando exige uma chave e retorna uma resposta em formato JSON.
```

Permanecem requisito, retorno e formato. Só a marcação sem função é removida;
`JSON` não é substituído.

## Padrão 16 — Listas verticais com cabeçalhos repetitivos

### Problema

Fragmenta uma sequência curta em lista cujos itens repetem rótulos em negrito e
produzem mais estrutura do que informação.

### Aplicação contextual

Converter em prosa apenas quando ordem, consulta, comparação e execução não
dependem da lista. Preservar listas de passos, requisitos, opções, inventários e
itens que o leitor precisa localizar rapidamente.

### Exemplo de direção

Antes:

```markdown
- **Prazo:** a inscrição termina na sexta-feira.
- **Canal:** o envio ocorre pelo portal.
- **Retorno:** a confirmação chega por e-mail.
```

Depois:

```markdown
A inscrição termina na sexta-feira, o envio ocorre pelo portal e a confirmação
chega por e-mail.
```

Permanecem prazo, canal e retorno. A conversão só é adequada porque os três
itens formam uma frase curta, não uma sequência operacional.

## Padrão 17 — Capitalização inadequada de títulos

### Problema

Aplica maiúsculas a palavras significativas de títulos por influência do inglês
ou alterna convenções sem motivo dentro do mesmo documento.

### Aplicação contextual

Seguir a convenção consistente do documento. Na ausência dela, preferir em
português maiúscula inicial e preservar nomes próprios, siglas e grafia oficial.

### Exemplo de direção

Antes:

```markdown
## Como Configurar o Banco de Dados no Amazon RDS
```

Depois:

```markdown
## Como configurar o banco de dados no Amazon RDS
```

Permanecem nível do título, assunto e nome oficial `Amazon RDS`. Só a
capitalização incompatível com a convenção em português é ajustada.

## Padrão 18 — Emojis decorativos

### Problema

Acrescenta emojis a títulos ou itens sem função informativa, afetiva ou de marca
solicitada.

### Aplicação contextual

Remover somente quando os símbolos forem ornamentos repetitivos. Manter quando
integrarem a voz do autor, a comunicação informal solicitada, uma legenda,
status, escala ou convenção de interface.

### Exemplo de direção

Antes:

```markdown
## 🚀 Instalação

## ✨ Configuração
```

Depois:

```markdown
## Instalação

## Configuração
```

Permanecem títulos, hierarquia e ordem. Saem apenas os símbolos decorativos.

## Padrão 19 — Convenção de aspas inconsistente

### Problema

Alterna aspas retas, curvas, simples ou outra convenção sem função e contra o
padrão predominante do documento.

### Aplicação contextual

Harmonizar somente a prosa editável com a convenção observada. Preservar aspas
em código, comandos, dados, citações com aninhamento e estilos exigidos pelo
formato ou pela publicação.

### Exemplo de direção

Antes:

```text
O documento chama a primeira etapa de “triagem” e a segunda de "revisão".
```

Depois:

```text
O documento chama a primeira etapa de “triagem” e a segunda de “revisão”.
```

Permanecem os nomes das etapas. A segunda marcação acompanha a convenção já
estabelecida; nenhum conteúdo entre aspas é alterado.

## Integração no fluxo da skill

Na leitura, a skill primeiro identifica a convenção predominante e distingue
estrutura funcional de decoração. Antes da versão final, a auditoria confirma:

- que Markdown, links, tabelas, código, comandos e dados continuam intactos;
- que nenhuma lista útil foi convertida em prosa;
- que nomes próprios e grafias oficiais preservam capitalização;
- que a pontuação segue a amostra ou o documento, não uma regra universal;
- que símbolos e destaques mantidos têm função observável ou instruída.

## Sincronização e validação

A implementação validará:

- sequência global 14–19 sem lacunas em `formatacao.md`, `SKILL.md` e README;
- nomes estáveis idênticos nos três arquivos;
- todos os campos obrigatórios em cada padrão;
- ligação direta do `SKILL.md` para a referência;
- exemplos com Markdown protegido e convenção contextual;
- ausência de proibições absolutas, placeholders e metadados de Claude.

## Fora de escopo

- formatador automático de Markdown;
- adoção obrigatória de um estilo tipográfico único;
- reestruturação de tabelas, código ou listas operacionais;
- implementação dos padrões 20–33;
- alteração de manifesto, versão ou componentes do plugin.
