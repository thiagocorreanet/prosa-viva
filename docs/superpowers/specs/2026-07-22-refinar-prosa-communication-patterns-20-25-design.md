# Padrões de comunicação, preenchimento e hesitação 20–25

## Contexto

Esta especificação detalha o quarto grupo do catálogo editorial do
`refinar-prosa`, relacionado à issue #8 e à épica #1. O grupo cobre seis
padrões que aparecem quando o texto se dirige ao leitor como chatbot, preenche
lacunas com especulação, adota servilismo, acumula palavras sem função, empilha
ressalvas ou encerra com otimismo genérico.

A implementação depende do contrato editorial da #3 e da estrutura de catálogo
iniciada na #5. As decisões de voz da #4 são complementares, mas o grupo precisa
funcionar mesmo sem amostra autoral.

## Decisão de arquitetura

As regras ficarão em `skills/refinar-prosa/references/pt-BR/comunicacao.md`, em
paralelo às famílias anteriores. O `SKILL.md` manterá somente triagem, números,
nomes e ligação direta; o README terá o resumo público.

```text
skills/refinar-prosa/
├── SKILL.md
└── references/
    ├── conteudo.md
    ├── linguagem.md
    ├── formatacao.md
    └── comunicacao.md

README.md
```

## Alternativas consideradas

### Referência contextual por família — escolhida

Permite tratar em conjunto postura comunicativa, preenchimento e confiança sem
misturá-los com gramática ou formatação. O carregamento continua seletivo.

### Lista de frases a remover

Seria fácil de executar, mas confundiria artefatos de chatbot com saudações
legítimas e ressalvas técnicas. Foi rejeitada.

### Regra geral de concisão

Cobriria parte do problema, porém não protegeria incerteza real, atribuição nem
convenções de correspondência. Foi rejeitada.

## Regra transversal de confiança

A edição pode tornar uma incerteza mais clara, mas não pode aumentar nem reduzir
o grau de confiança sustentado pela fonte. Também não pode transformar ausência
de informação em fato, criar fonte, prever atualização ou declarar consenso.

```text
afirmação original
  → evidência e atribuição disponíveis
  → grau de confiança e modalidade
  → função comunicativa no gênero
  → edição mínima sem mudar certeza ou fonte
```

Em textos jurídicos, científicos, médicos, financeiros ou de risco, ressalvas
que delimitam escopo, probabilidade, obrigação ou limitação são conteúdo
protegido. A concisão nunca prevalece sobre cautela material.

## Correspondência e gênero

Saudações, despedidas, agradecimentos e ofertas de ajuda permanecem quando o
texto for e-mail, carta, mensagem de atendimento ou outro gênero em que cumpram
função social. As mesmas fórmulas podem ser removidas de documentação,
descrições de PR, commits ou texto embutido quando forem resíduos de conversa
com o modelo.

## Esquema obrigatório por padrão

Cada padrão em `comunicacao.md` terá problema, sinais candidatos, confirmação
contextual, falsos positivos, exemplo antes/depois e preservação factual e de
confiança. Os detalhes permanecerão somente na referência.

## Padrão 20 — Artefatos de chatbot e ofertas de continuação

### Problema

Mantém no texto final saudações ao solicitante, comentários sobre a tarefa,
ofertas de continuar ou frases como “espero que ajude” sem função no gênero.

### Aplicação contextual

Remover somente quando a frase revelar a interação com o assistente em um texto
que deve ser autônomo. Preservar fórmulas legítimas de correspondência e
atendimento.

### Exemplo de direção

Antes:

```text
A API aceita requisições JSON e retorna o identificador do pedido. Espero que
isso ajude! Se quiser, posso explicar os campos em mais detalhes.
```

Depois:

```text
A API aceita requisições JSON e retorna o identificador do pedido.
```

Permanecem entrada e retorno da API. Saem apenas comentários dirigidos ao
solicitante que não pertencem à documentação.

## Padrão 21 — Avisos de limite de conhecimento e preenchimento especulativo

### Problema

Insere avisos sobre o conhecimento do modelo ou especula sobre mudanças para
compensar a falta de informação na fonte.

### Aplicação contextual

Substituir metacomentários por uma limitação verificável do material disponível,
quando ela for relevante. Não pesquisar, atualizar, inventar fonte ou afirmar
vigência sem autorização e evidência.

### Exemplo de direção

Antes:

```text
O regulamento foi publicado em 2022. Como meu conhecimento pode estar
desatualizado, talvez ele ainda esteja vigente.
```

Depois:

```text
O regulamento foi publicado em 2022; o texto fornecido não informa se ele
continua vigente.
```

Permanecem data, publicação e incerteza sobre vigência. A limitação passa a se
referir à fonte; nenhuma atualização ou conclusão é inventada.

## Padrão 22 — Tom adulador ou servil

### Problema

Acrescenta elogios automáticos, concordância excessiva ou deferência que desvia
do conteúdo e pode simular validação factual.

### Aplicação contextual

Remover elogios sem função e apresentar a avaliação com base observável.
Preservar cortesia adequada ao gênero, reconhecimento específico e linguagem de
hospitalidade solicitada.

### Exemplo de direção

Antes:

```text
Excelente observação — você está absolutamente certo. A opção B usa menos
memória nos testes apresentados.
```

Depois:

```text
Nos testes apresentados, a opção B usa menos memória.
```

Permanece a comparação limitada aos testes. Saem elogio e concordância absoluta,
que poderiam ampliar indevidamente a conclusão.

## Padrão 23 — Preenchimento sem função

### Problema

Usa prefácios, transições ou comentários genéricos que atrasam uma afirmação sem
delimitar contexto, relação lógica ou cautela.

### Aplicação contextual

Remover somente o material que não muda sentido, ênfase necessária ou ligação
entre ideias. Transições reais e enquadramentos necessários permanecem.

### Exemplo de direção

Antes:

```text
É importante observar que, de modo geral, a reunião começa às 9h.
```

Depois:

```text
A reunião começa às 9h.
```

Permanece o horário. Saem apenas prefácios que não qualificavam a afirmação.

## Padrão 24 — Empilhamento de ressalvas

### Problema

Acumula marcadores de possibilidade ou cautela que expressam o mesmo grau de
incerteza e tornam a frase evasiva.

### Aplicação contextual

Condensar marcadores redundantes em uma formulação que preserve exatamente a
confiança disponível. Manter ressalvas independentes sobre amostra, método,
escopo, risco ou obrigação.

### Exemplo de direção

Antes:

```text
Os resultados talvez possam possivelmente indicar uma redução de falhas.
```

Depois:

```text
Os resultados podem indicar uma redução de falhas.
```

Permanece a possibilidade, sem convertê-la em certeza. Saem somente marcadores
redundantes do mesmo grau de hesitação.

## Padrão 25 — Conclusões positivas genéricas

### Problema

Encerra com “futuro promissor”, “passo importante” ou otimismo equivalente sem
fato, decisão ou próximo passo que sustente a conclusão.

### Aplicação contextual

Remover o fechamento quando ele apenas repete uma avaliação positiva. Preservar
conclusões que sintetizem fatos, registrem decisões, riscos ou próximos passos.

### Exemplo de direção

Antes:

```text
A migração termina em 15 de agosto. Com isso, a organização caminha para um
futuro cada vez mais promissor.
```

Depois:

```text
A migração termina em 15 de agosto.
```

Permanecem evento e data. Sai a projeção positiva sem suporte; nenhum benefício
é inferido.

## Integração e auditoria

Na leitura, a skill identifica gênero e grau de confiança antes de classificar
um sinal. Na auditoria final, confirma:

- que nenhuma saudação ou despedida legítima foi removida;
- que incerteza, escopo e cautela material permanecem;
- que nenhuma fonte, vigência, consenso ou certeza foi inventada;
- que a conclusão retida contém fato, decisão, risco ou próximo passo;
- que o texto embutido contém somente o resultado solicitado.

## Sincronização e validação

A implementação validará sequência 20–25, nomes idênticos, campos obrigatórios,
ligação direta, exemplos antes/depois, proteção da confiança e distinção entre
artefato de chatbot e correspondência legítima. Também executará os validadores
da skill e do plugin e a auditoria contra placeholders e metadados de Claude.

## Fora de escopo

- pesquisa de fatos atuais ou inclusão de novas fontes;
- alteração do grau de certeza sustentado pela entrada;
- remoção automática de toda saudação, ressalva ou conclusão;
- implementação dos padrões 26–33;
- alteração do manifesto, versão ou componentes do plugin.
