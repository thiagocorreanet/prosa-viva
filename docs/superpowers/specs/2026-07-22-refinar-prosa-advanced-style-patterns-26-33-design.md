# Padrões avançados de estilo e cadência 26–33

## Contexto

Esta especificação detalha o quinto grupo do catálogo editorial do
`refinar-prosa`, relacionado à issue #9 e à épica #1. O grupo encerra a
sequência 1–33 com oito padrões sobre ortografia, autoridade retórica,
metadiscurso, documentação orientada a mudanças, dramatização, aforismos e
aberturas de falsa espontaneidade.

A implementação depende do contrato editorial da #3 e da estrutura de catálogo
iniciada na #5. A calibração de voz da #4 é especialmente útil para distinguir
cadência autoral de fórmula, mas não é pré-condição técnica.

## Decisão de arquitetura

As regras ficarão em `skills/refinar-prosa/references/estilo-avancado.md`. O
`SKILL.md` fará triagem e ligação direta, e o README manterá apenas números e
nomes.

```text
skills/refinar-prosa/
├── SKILL.md
└── references/
    ├── conteudo.md
    ├── linguagem.md
    ├── formatacao.md
    ├── comunicacao.md
    └── estilo-avancado.md

README.md
```

## Alternativas consideradas

### Referência contextual por família — escolhida

Mantém juntos os padrões que dependem fortemente de gênero, cadência e intenção
retórica. Também permite uma auditoria única da sequência completa 1–33.

### Corretor ortográfico e estilístico rígido

Poderia automatizar hifenização e frases curtas, mas apagaria usos intencionais
em ensaios, publicidade criativa e ficção. Foi rejeitado.

### Dividir documentação técnica e prosa geral

Separaria o padrão 30 dos demais, porém duplicaria regras de voz e contexto. O
esquema por padrão já permite declarar gêneros protegidos. Foi rejeitada.

## Regra transversal de intenção

Nenhum recurso isolado — hífen, frase curta, pergunta, fórmula retórica ou
abertura pessoal — comprova artificialidade. A skill considera conjunto,
recorrência, gênero e amostra autoral.

```text
sinal candidato
  → convenção do português e do documento
  → função factual, estrutural ou retórica
  → gênero e voz do autor
  → edição mínima somente se a fórmula substituir precisão
```

Ensaios, publicidade criativa e ficção admitem maior densidade de recursos
retóricos. Changelogs e guias de migração podem ser explicitamente orientados a
mudanças. Documentação de estado atual deve priorizar o comportamento vigente,
sem apagar contexto histórico necessário de documentos versionados.

## Esquema obrigatório por padrão

Cada padrão em `estilo-avancado.md` terá problema, sinais candidatos,
confirmação contextual, falsos positivos, exemplo antes/depois e preservação
factual, autoral e de gênero.

## Padrão 26 — Hifenização imprópria em português

### Problema

Mantém hífens por analogia com o inglês, por segmentação visual ou por regra
incorreta do português, sobretudo em compostos e prefixos.

### Aplicação contextual

Corrigir apenas formas cuja grafia em português seja conhecida no contexto.
Preservar nomes oficiais, marcas, identificadores, código, URLs, citações e
termos de domínio cuja grafia não possa ser confirmada. Não transformar a skill
em corretor ortográfico geral.

### Exemplo de direção

Antes:

```text
Cada micro-serviço registra suas próprias métricas.
```

Depois:

```text
Cada microsserviço registra suas próprias métricas.
```

Permanece a arquitetura descrita. Só a grafia é ajustada segundo a formação em
português; identificadores como `micro-service-id` continuariam intactos.

## Padrão 27 — Fórmulas de autoridade persuasiva

### Problema

Usa expressões como “a verdadeira questão” ou “o que realmente importa” para
declarar prioridade sem demonstrá-la.

### Aplicação contextual

Substituir a moldura pela tese ou pelo critério disponível. Manter quando a
frase introduzir contraste argumentado, reproduzir voz autoral ou cumprir função
persuasiva solicitada.

### Exemplo de direção

Antes:

```text
A verdadeira questão é a latência: os testes registraram 480 ms no fluxo de
pagamento.
```

Depois:

```text
Os testes registraram latência de 480 ms no fluxo de pagamento.
```

Permanecem métrica, valor e fluxo. Sai apenas a declaração de prioridade sem
comparação.

## Padrão 28 — Anúncios do percurso textual

### Problema

Anuncia que o texto vai explorar, mergulhar, descobrir ou percorrer um tema em
vez de começar pela informação.

### Aplicação contextual

Remover quando o anúncio não orientar uma estrutura extensa. Preservar roteiros
úteis em cursos, apresentações, tutoriais longos e documentos que precisam
explicitar escopo ou sequência.

### Exemplo de direção

Antes:

```text
Neste guia, vamos explorar como configurar o cache. Primeiro, defina `ttl` como
300 segundos.
```

Depois:

```text
Para configurar o cache, defina `ttl` como 300 segundos.
```

Permanecem objetivo, chave e valor. Sai somente o anúncio do percurso.

## Padrão 29 — Títulos seguidos de reformulação

### Problema

Repete imediatamente em prosa o conteúdo já expresso por um título, sem
acrescentar escopo, condição ou orientação.

### Aplicação contextual

Remover a reformulação somente quando for semanticamente vazia. Preservar
introduções que definam objetivo, pré-condição, risco ou contexto acessível.

### Exemplo de direção

Antes:

```markdown
## Instalação

Nesta seção, veremos como realizar a instalação. Execute `npm install`.
```

Depois:

```markdown
## Instalação

Execute `npm install`.
```

Permanecem título, comando e ordem. Sai apenas a frase que repetia o título.

## Padrão 30 — Documentação ancorada na mudança

### Problema

Descreve o estado atual como contraste permanente com uma versão anterior,
mesmo quando o leitor precisa saber apenas como o sistema funciona agora.

### Aplicação contextual

Reescrever documentação de referência pelo comportamento vigente. Preservar
histórico em changelogs, notas de versão, guias de migração e documentos
versionados; manter comparação quando ela explicar compatibilidade ou risco.

### Exemplo de direção

Antes:

```text
Agora, o endpoint `/pedidos` exige o cabeçalho `X-Conta`, ao contrário da versão
anterior.
```

Depois:

```text
O endpoint `/pedidos` exige o cabeçalho `X-Conta`.
```

Permanecem endpoint, requisito e cabeçalho. Sai o contraste histórico porque o
trecho é documentação do estado atual, não guia de migração.

## Padrão 31 — Sequências curtas de dramatização artificial

### Problema

Divide uma afirmação em várias frases mínimas para simular tensão ou impacto sem
função autoral ou informativa.

### Aplicação contextual

Reunir somente sequências recorrentes cuja fragmentação não corresponda à voz
nem ao gênero. Uma frase curta enfática isolada permanece; publicidade criativa,
ensaio e ficção admitem cadência dramática intencional.

### Exemplo de direção

Antes:

```text
O deploy falhou. De novo. Sem aviso.
```

Depois:

```text
O deploy voltou a falhar sem aviso.
```

Permanecem falha, recorrência e ausência de aviso. Só a fragmentação formulaica
é condensada.

## Padrão 32 — Fórmulas aforísticas no lugar de precisão

### Problema

Usa oposição ou máxima memorável para substituir uma relação que poderia ser
declarada com escopo e precisão.

### Aplicação contextual

Converter quando a fórmula contiver uma prioridade ou relação recuperável.
Preservar aforismos autorais, slogans solicitados, citações e recursos
deliberados em ensaio, publicidade ou ficção.

### Exemplo de direção

Antes:

```text
Não é sobre velocidade. É sobre confiança.
```

Depois:

```text
A prioridade é a confiança, não a velocidade.
```

Permanece a prioridade relativa expressa pela fonte. A revisão não inventa
métrica nem justificativa.

## Padrão 33 — Aberturas de falsa espontaneidade

### Problema

Começa com confissão, franqueza ou surpresa simulada que não pertence à voz do
autor nem acrescenta experiência situada.

### Aplicação contextual

Remover apenas quando a abertura for uma fórmula genérica destacável. Preservar
relatos pessoais reais, auto-correções, hesitações autorais e aberturas
intencionais em gêneros pessoais ou criativos.

### Exemplo de direção

Antes:

```text
Vou ser sincero: a configuração exige duas chaves obrigatórias.
```

Depois:

```text
A configuração exige duas chaves obrigatórias.
```

Permanecem quantidade, obrigatoriedade e objeto. Sai apenas a alegação genérica
de franqueza.

## Integração e auditoria

Na auditoria final, a skill confirma:

- grafias técnicas e identificadores protegidos permaneceram intactos;
- nenhum recurso retórico isolado motivou edição automática;
- exemplos autorais, criativos e ficcionais conservaram a cadência deliberada;
- changelogs, migrações e documentos versionados mantiveram histórico útil;
- cada fórmula removida deu lugar à informação já disponível, sem fabricação;
- a sequência das referências do catálogo forma exatamente 1–33.

## Sincronização e validação

A implementação validará sequência 26–33, nomes idênticos, campos obrigatórios,
ligação direta, exemplos próprios, convenções do português e os gêneros
protegidos. Uma verificação integrada confirmará a numeração 1–33.

## Fora de escopo

- corretor ortográfico completo;
- atualização automática de documentação histórica;
- proibição global de frases curtas ou recursos retóricos;
- detecção de autoria por frequência;
- alteração do manifesto, versão ou componentes do plugin.
