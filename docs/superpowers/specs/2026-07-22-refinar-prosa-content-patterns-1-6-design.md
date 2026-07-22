# Padrões de conteúdo 1–6 da skill Refinar Prosa

## Contexto

Esta especificação detalha o primeiro grupo do catálogo editorial do
`refinar-prosa`, relacionado à issue #5 e à épica #1. O grupo cobre seis padrões
de conteúdo adaptados ao português brasileiro, com aplicação contextual,
falsos positivos e exemplos próprios.

O catálogo depende do contrato editorial da #3, porque todo padrão precisa
preservar fatos, qualificações e relações lógicas. A calibração de voz da #4 não
é pré-condição: os dois recursos podem ser implementados em qualquer ordem
depois da #3, desde que suas seções de roteamento coexistam no `SKILL.md`.

## Decisão de arquitetura

Os detalhes dos padrões ficarão em uma referência canônica ligada diretamente
pelo `SKILL.md`:

```text
skills/refinar-prosa/
├── SKILL.md
└── references/
    └── conteudo.md

README.md
```

Responsabilidades:

- `skills/refinar-prosa/references/pt-BR/conteudo.md`: única fonte canônica dos nomes,
  regras, limites, exemplos e inventários factuais dos padrões 1–6.
- `skills/refinar-prosa/SKILL.md`: mapa curto com os seis nomes, famílias de
  sinais e ligação direta para a referência.
- `README.md`: resumo público dos mesmos seis números e nomes, sem copiar regras
  ou exemplos.

A referência será lida quando a revisão encontrar sinais candidatos de
importância inflada, notoriedade, análise superficial, promoção, atribuição vaga
ou fechamento formulaico. O mapa no `SKILL.md` precisa ser suficiente para o
roteamento sem duplicar o catálogo.

## Alternativas consideradas

### Referência única com esquema fixo — escolhida

Mantém o grupo coeso e permite validar automaticamente se os seis padrões têm os
mesmos campos. A ligação direta evita encadeamento profundo e prepara a expansão
do catálogo sem inflar o `SKILL.md`.

### Referência em prosa contínua

Seria agradável para leitura linear, mas dificultaria verificar limites,
exemplos e preservação factual de cada padrão. Foi rejeitada.

### Um arquivo por padrão

Facilitaria alterações isoladas, porém fragmentaria um grupo pequeno em seis
leituras e tornaria o roteamento mais complexo. Foi rejeitada.

## Regra transversal de aplicação

Nenhuma palavra ou expressão isolada comprova um padrão. A skill seguirá esta
sequência:

```text
sinal candidato
  → função no contexto
  → suporte factual ou atribuição
  → informação nova ou apenas aparência de importância
  → edição mínima se o conjunto confirmar o padrão
```

Se houver dúvida, a redação é preservada. Uma expressão recorrente em textos
artificiais pode ser legítima em contexto histórico, técnico, promocional
solicitado, atribuído ou sustentado por evidência.

## Esquema obrigatório por padrão

Cada padrão em `conteudo.md` terá:

1. **Problema:** a distorção editorial que corrige.
2. **Sinais candidatos:** construções e funções discursivas que merecem
   inspeção, sem funcionar como lista proibida.
3. **Confirmação contextual:** evidências necessárias para aplicar o padrão.
4. **Não alterar quando:** usos legítimos e falsos positivos.
5. **Antes:** exemplo original em português brasileiro.
6. **Depois:** revisão mínima, sem fabricação nem omissão factual.
7. **Preservação factual:** inventário explícito do que continuou representado e
   do que foi removido apenas por ser avaliação sem apoio ou preenchimento.

Os nomes e números são estáveis e serão repetidos no mapa do `SKILL.md` e no
resumo do README. Todos os demais detalhes aparecem somente na referência.

## Padrão 1 — Inflação de importância e legado

### Problema

Transforma um acontecimento comum em marco histórico, legado ou mudança
fundamental sem apresentar evidência para essa avaliação.

### Sinais candidatos

- “desempenha um papel fundamental” sem explicar o papel;
- “marca um momento crucial” sem consequência demonstrada;
- “representa um divisor de águas” sem comparação anterior e posterior;
- “deixa um legado duradouro” sem efeito identificado;
- escalada de importância que pode ser retirada sem perder o acontecimento.

### Confirmação contextual

Aplicar somente quando a importância for uma avaliação genérica, sem dados,
fonte, atribuição ou consequência concreta, e o trecho factual permanecer
completo sem ela.

### Não alterar quando

- impacto histórico é o próprio objeto do texto;
- há dados, comparação temporal ou fonte que sustentem o impacto;
- a avaliação está atribuída a uma pessoa ou documento relevante;
- “fundamental” ou equivalente descreve uma dependência técnica real.

### Exemplo

Antes:

```text
A biblioteca passou a abrir aos sábados, um marco fundamental em sua trajetória.
```

Depois:

```text
A biblioteca passou a abrir aos sábados.
```

### Preservação factual

Permanece o fato de que a biblioteca passou a abrir aos sábados. Sai apenas a
avaliação não sustentada de que a mudança foi um marco fundamental; nenhuma
data, causa, alcance ou efeito é acrescentado.

## Padrão 2 — Notoriedade e cobertura sem contexto

### Problema

Usa enumeração de veículos, aparições ou reconhecimento para insinuar ampla
relevância sem explicar a relação dessa cobertura com o assunto.

### Sinais candidatos

- “ganhou ampla notoriedade” seguido de lista de canais;
- “recebeu extensa cobertura” sem medida ou consequência;
- enumeração de jornais, podcasts, eventos ou plataformas como prova automática
  de importância;
- repetição de aparições sem contexto de data, alcance ou recepção.

### Confirmação contextual

Aplicar quando a cobertura informada for factual, mas a conclusão sobre
notoriedade, prestígio ou impacto não tiver apoio. Preservar as menções concretas
e remover apenas a inferência exagerada.

### Não alterar quando

- recepção pública ou história da cobertura são o tema;
- veículos, datas ou alcance são necessários para verificar uma afirmação;
- a cobertura demonstra consequência concreta documentada;
- a enumeração está em uma seção bibliográfica ou de imprensa apropriada.

### Exemplo

Antes:

```text
A iniciativa ganhou ampla notoriedade e foi mencionada por jornais locais e
podcasts da região.
```

Depois:

```text
Jornais locais e podcasts da região mencionaram a iniciativa.
```

### Preservação factual

Permanecem a existência das menções e os dois tipos de veículo. Sai somente a
conclusão não quantificada de “ampla notoriedade”; não são inventados alcance,
datas, nomes de veículos ou efeitos da cobertura.

## Padrão 3 — Análise superficial acoplada

### Problema

Anexa ao fato uma interpretação genérica, muitas vezes por gerúndio, que atribui
virtude, significado ou intenção sem acrescentar evidência.

### Sinais candidatos

- “evidenciando” seguido de qualidade abstrata;
- “demonstrando compromisso” sem ação adicional;
- “reforçando a importância” sem argumento;
- “destacando seu papel” como comentário automático;
- gerúndio que apenas elogia ou interpreta a oração anterior.

### Confirmação contextual

Aplicar quando a oração acoplada não descreve consequência verificável, ação
simultânea ou conteúdo explícito, e apenas converte o fato anterior em julgamento
positivo.

### Não alterar quando

- o gerúndio expressa resultado concreto: “A chuva alagou a pista,
  interrompendo o trânsito por duas horas”;
- há relação temporal, causal ou operacional necessária;
- a análise está atribuída e é relevante ao argumento;
- retirar a oração eliminaria informação verificável.

### Exemplo

Antes:

```text
O conselho publicou as atas no portal, demonstrando compromisso com a
transparência.
```

Depois:

```text
O conselho publicou as atas no portal.
```

### Preservação factual

Permanecem agente, ação, objeto e local de publicação. Sai a interpretação não
sustentada sobre compromisso; não se afirma quem consultou as atas nem qual foi
o efeito da publicação.

## Padrão 4 — Promoção indevida

### Problema

Substitui descrição por publicidade, com superlativos, adjetivos absolutos ou
promessas que não são necessárias ao gênero nem sustentadas pelo texto.

### Sinais candidatos

- “revolucionário”, “incomparável” ou “imperdível” sem comparação;
- “experiência única” sem característica identificada;
- promessa de resultado sem dado ou condição;
- adjetivos promocionais em texto técnico, enciclopédico ou informativo;
- repetição de benefícios abstratos em lugar de funções concretas.

### Confirmação contextual

Aplicar quando a linguagem promocional não é citação, requisito de voz de marca
nem alegação apoiada, e pode ser substituída pelas capacidades efetivamente
fornecidas.

### Não alterar quando

- o usuário pediu texto publicitário e forneceu as alegações;
- a expressão faz parte de slogan ou citação preservada;
- uma comparação é apoiada por métrica e referência;
- o tom promocional é objeto de análise, não voz do texto.

### Exemplo

Antes:

```text
O aplicativo oferece uma experiência revolucionária e incomparável, com busca
por título e filtro por autor.
```

Depois:

```text
O aplicativo permite buscar por título e filtrar por autor.
```

### Preservação factual

Permanecem as duas capacidades: busca por título e filtro por autor. Saem os
adjetivos promocionais sem apoio; não são acrescentadas velocidade, precisão,
facilidade de uso ou comparação com concorrentes.

## Padrão 5 — Atribuição vaga e evasiva

### Problema

Apresenta uma afirmação apoiada em fonte indefinida ou em quantificadores vagos,
dificultando avaliar autoria, alcance e grau de certeza.

### Sinais candidatos

- “especialistas afirmam” sem identificação disponível;
- “alguns dizem”, “muitos consideram” ou “é amplamente reconhecido”;
- voz passiva que apaga o agente relevante;
- atribuição genérica usada para fortalecer uma conclusão;
- troca de fonte específica por categoria vaga.

### Confirmação contextual

Aplicar quando a fonte não puder ser identificada no texto ou contexto e a
vagueza estiver escondendo uma limitação relevante. Nunca transformar atribuição
vaga em afirmação direta.

### Não alterar quando

- anonimato protege pessoas ou fontes;
- a atribuição resume consenso documentado já apresentado;
- a identidade é irrelevante e o quantificador é preciso o suficiente;
- o gênero exige confidencialidade ou agregação;
- a fonte aparece claramente em trecho próximo.

### Exemplo

Antes:

```text
Segundo especialistas, o novo horário reduziu a espera.
```

Depois:

```text
Segundo especialistas não identificados no texto, o novo horário reduziu a
espera.
```

### Preservação factual

Permanecem a atribuição a especialistas e a afirmação sobre redução da espera.
A revisão torna explícita a limitação observável de que o texto não identifica
as fontes; não inventa nomes, dados, causa, período ou intensidade da redução.

## Padrão 6 — Desafios e futuro formulaicos

### Problema

Cria seções previsíveis de “desafios”, “perspectivas” ou “futuro” preenchidas
por frases genéricas, mesmo quando há apenas um próximo passo concreto.

### Sinais candidatos

- título “Desafios e perspectivas futuras” sem desafios nomeados;
- “em meio aos desafios” sem obstáculo específico;
- “abre caminho para novas possibilidades” sem ação ou decisão;
- “o futuro parece promissor” sem previsão sustentada;
- fechamento otimista que repete o tema e adia a conclusão.

### Confirmação contextual

Aplicar quando a seção mistura preenchimento abstrato com poucos fatos concretos.
Manter riscos, decisões, datas, responsáveis e próximos passos; remover apenas
frases sem conteúdo verificável.

### Não alterar quando

- desafios, riscos ou cenários são específicos;
- perspectivas estão apoiadas por fonte, plano ou projeção identificada;
- a seção organiza ações futuras reais;
- o gênero exige análise de riscos ou planejamento.

### Exemplo

Antes:

```text
Apesar dos desafios, o projeto segue avançando e abre caminho para novas
possibilidades. O próximo encontro será em 12 de outubro para definir o
cronograma.
```

Depois:

```text
O próximo encontro será em 12 de outubro para definir o cronograma.
```

### Preservação factual

Permanecem data e finalidade do encontro. Saem referências não especificadas a
desafios, avanço e possibilidades; não são inventados participantes, decisões,
prazos ou conteúdo do cronograma.

## Roteamento no SKILL.md

O `SKILL.md` terá uma seção curta com os seis números e nomes e uma ligação
direta para `references/pt-BR/conteudo.md`. A instrução será:

- fazer uma triagem contextual pelas seis famílias;
- ler a referência inteira quando houver ao menos um sinal candidato;
- aplicar somente padrões confirmados pelo contexto;
- usar o contrato factual da #3 para auditar cada edição;
- preservar o trecho em caso de dúvida.

O mapa não copiará expressões, falsos positivos ou exemplos da referência.

## Resumo no README

Depois da tabela de grupos do catálogo, o README terá uma subseção “Padrões de
conteúdo (1–6)” com uma lista numerada dos seis nomes estáveis:

1. Inflação de importância e legado.
2. Notoriedade e cobertura sem contexto.
3. Análise superficial acoplada.
4. Promoção indevida.
5. Atribuição vaga e evasiva.
6. Desafios e futuro formulaicos.

O README não conterá sinais, limites ou exemplos. A referência canônica poderá
ser ligada para leitores que desejarem detalhes.

## Sincronização

A validação extrairá números e nomes de três locais:

- títulos `## N — Nome` de `references/pt-BR/conteudo.md`;
- lista numerada do mapa no `SKILL.md`;
- lista numerada da subseção no README.

As três sequências devem ser idênticas e conter exatamente os números 1 a 6.
Somente a referência pode conter os campos detalhados e os pares “Antes” e
“Depois”.

## Falhas e casos-limite

- Sinal isolado sem confirmação contextual: não editar por causa do padrão.
- Avaliação apoiada por fonte ou dados: preservar a avaliação e sua atribuição.
- Gerúndio com consequência concreta: preservar a relação.
- Linguagem promocional solicitada: manter somente alegações fornecidas.
- Atribuição vaga irresolúvel: explicitar a limitação sem inventar fonte.
- Seção de futuro com ações concretas: preservar as ações e remover somente
  preenchimento confirmado.
- Dois padrões no mesmo trecho: aplicar a menor edição que resolva ambos sem
  apagar informação.
- Dúvida sobre perda factual: manter o original.

## Validação

A implementação deve executar:

1. pré-condição que confirme o contrato da #3 no `SKILL.md`;
2. verificação da sequência e dos nomes 1–6 nos três arquivos;
3. verificação dos sete campos obrigatórios por padrão;
4. contagem de seis pares “Antes” e “Depois”;
5. contagem de seis seções de preservação factual;
6. verificação de pelo menos um falso positivo concreto por padrão;
7. busca por linguagem que transforme sinais em palavras proibidas;
8. auditoria manual dos exemplos contra fabricação e omissão;
9. confirmação da ligação direta no `SKILL.md`;
10. confirmação de que README e `SKILL.md` não duplicam exemplos;
11. `quick_validate.py` contra a skill;
12. `validate_plugin.py` contra a raiz do pacote;
13. busca por placeholders e metadados específicos do Claude;
14. `git diff --check`.

## Critérios de aceite verificáveis

- A referência contém exatamente os padrões numerados de 1 a 6.
- Todos os padrões seguem o mesmo esquema e têm exemplos próprios em pt-BR.
- Nenhum “depois” inventa fatos; cada padrão inclui inventário factual.
- Termos isolados são sinais candidatos, nunca prova suficiente.
- O `SKILL.md` liga diretamente a referência e define roteamento contextual.
- O README resume os mesmos seis números e nomes sem duplicar o catálogo.
- A implementação modifica somente `SKILL.md`, `references/pt-BR/conteudo.md` e
  `README.md`, depois da implementação da #3.
