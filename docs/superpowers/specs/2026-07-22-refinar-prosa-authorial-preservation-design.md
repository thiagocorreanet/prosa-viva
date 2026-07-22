# Proteção contra falsos positivos e preservação autoral

## Contexto

Esta especificação cobre a issue #10 e a épica #1. Seu objetivo é impedir que o
`refinar-prosa` trate correção, formalidade ou um recurso isolado como evidência
de texto artificial e achate sinais legítimos de autoria.

A implementação depende do contrato editorial da #3. Ela complementa todos os
padrões 1–33 e deve ser aplicada antes de qualquer correção do catálogo. As
fixtures criadas aqui serão a semente de sobre-edição da suíte ampla da #15.

## Decisão de arquitetura

```text
skills/refinar-prosa/
├── SKILL.md
└── references/
    └── preservacao-autoral.md

evals/fixtures/sobre-edicao/
├── inputs.json
├── constraints.json
└── expectations.json
```

Responsabilidades:

- `SKILL.md`: invariantes curtas e sempre visíveis — conjunto de sinais,
  falsos positivos, sinais autorais e auditoria de perda de voz.
- `references/preservacao-autoral.md`: critérios completos, casos limítrofes e
  procedimento de decisão. A skill o lerá antes de aplicar o catálogo 1–33.
- `inputs.json`: textos, modo e gênero, sem expectativas misturadas.
- `constraints.json`: substrings e estruturas protegidas, além do limite de
  alteração permitido.
- `expectations.json`: resultado comportamental e justificativa de cada caso.

A separação das três dimensões segue a estratégia da #15 e permite que um runner
futuro avalie invariantes sem exigir uma redação final única.

## Alternativas consideradas

### Regra curta no `SKILL.md` e referência detalhada — escolhida

Mantém a proteção ativa em toda revisão e evita inflar o arquivo principal com
casos extensos. A ligação direta impede encadeamento profundo.

### Apenas uma referência opcional

Poderia não ser carregada antes da detecção e, portanto, não impedir o falso
positivo. Foi rejeitada.

### Fixtures com saída exata

Seriam frágeis diante de várias revisões igualmente válidas. Foram rejeitadas
em favor de invariantes, intensidade máxima de mudança e resultado esperado.

## Regra de conjunto de sinais

Nenhuma palavra, sinal de pontuação, estrutura ou ausência isolada autoriza
reescrita agressiva. Um padrão só é aplicado quando vários indícios convergem e
o contexto confirma que a construção prejudica clareza, precisão, adequação ao
gênero ou voz solicitada.

```text
sinal isolado
  → preservar e continuar leitura

conjunto de sinais
  → verificar função, gênero, voz e fatos
  → aplicar edição mínima somente se o padrão for confirmado
```

Na dúvida, preservar. A ausência de citações não é licença para acrescentar
fontes nem tratar o texto como não confiável.

## Falsos positivos que não contam isoladamente

- gramática correta e estilo consistente;
- mistura de registros;
- vocabulário formal, técnico ou acadêmico;
- transições comuns;
- aspas curvas ou travessões;
- uma frase curta de ênfase;
- ausência de citações;
- formatação complexa;
- termos observados dentro de citações, títulos, código ou exemplos.

Trechos protegidos não participam da detecção como se fossem voz do autor.
Termos usados metalinguisticamente, como um exemplo da expressão “fundamental”,
continuam intactos.

## Sinais autorais a preservar

- detalhe específico e incomum que esteja na fonte;
- sentimento misto, ambivalência ou tensão não resolvida;
- referência cultural situada;
- escolha editorial defensável, ainda que incomum;
- variação natural entre frases e parágrafos curtos e longos;
- aparte, autocorreção, hesitação significativa ou regionalismo.

Esses sinais não precisam ser “melhorados” para atingir uniformidade. Só serão
editados se o usuário pedir normalização ou se houver problema claro que possa
ser corrigido sem apagar a função autoral.

## Procedimento de decisão

1. Marcar conteúdo factual e estrutural protegido.
2. Identificar gênero, idioma, público, formalidade e amostra de voz.
3. Separar sinais isolados de conjuntos contextualmente coerentes.
4. Verificar se o trecho é citação, título, código, exemplo ou metalinguagem.
5. Identificar sinais autorais que a uniformização poderia apagar.
6. Fazer a menor edição útil ou não alterar.
7. Comparar a versão final à fonte e procurar perda de voz, além de fabricação e
   omissão.

## Auditoria de perda de voz

Além da auditoria factual, a skill pergunta:

- detalhes específicos ficaram mais genéricos?
- ambivalência virou conclusão limpa ou positiva?
- referência cultural foi neutralizada?
- variação natural virou cadência uniforme?
- aparte, autocorreção ou regionalismo defensável desapareceu?
- um único sinal desencadeou mudanças em volta dele?

Se qualquer resposta for positiva sem instrução do usuário, a versão deve ser
recuada até a menor edição segura.

## Fixtures de sobre-edição

O conjunto inicial terá casos originais em pt-BR para:

1. um travessão isolado em ensaio;
2. aspas curvas em prosa natural;
3. vocabulário formal em texto jurídico;
4. mistura funcional de registro em mensagem interna;
5. uma frase curta enfática;
6. Markdown complexo com tabela, link e código;
7. expressão do catálogo dentro de citação e exemplo metalinguístico;
8. detalhe específico incomum;
9. sentimentos mistos e tensão não resolvida;
10. referência cultural, aparte, autocorreção e regionalismo.

Cada ID aparecerá exatamente uma vez nos três arquivos JSON. Restrições terão
`preserve_exact`, `protected_structures` e `max_change_ratio`; expectativas terão
`expected_change` igual a `none` ou `minimal` e uma justificativa. O limite é um
sinal de regressão para o runner da #15, não uma métrica de autoria.

## Validação

A implementação verificará que:

- o `SKILL.md` contém as seções `Conjunto de sinais`, `Falsos positivos`,
  `Sinais autorais a preservar` e `Auditoria de perda de voz`;
- a referência é ligada diretamente e exigida antes do catálogo;
- todos os falsos positivos e sinais autorais do escopo estão representados;
- os três arquivos JSON são válidos, têm os mesmos IDs e separam entrada,
  restrições e expectativas;
- citações e exemplos metalinguísticos têm restrições explícitas;
- casos de sinal único esperam nenhuma ou mínima alteração;
- não há saída final única nem promessa sobre detecção de autoria.

## Fora de escopo

- implementar o runner completo da #15;
- definir pesos ou classificador probabilístico de autoria;
- exigir imutabilidade absoluta de toda escolha incomum;
- ampliar idiomas suportados;
- alterar manifesto, versão, agentes ou catálogo numerado.
