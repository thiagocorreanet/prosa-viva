# Padrões de linguagem e gramática 7–13 da skill Refinar Prosa

## Contexto

Esta especificação detalha o segundo grupo do catálogo editorial do
`refinar-prosa`, relacionado à issue #6 e à épica #1. O grupo cobre sete
padrões de linguagem e gramática adaptados ao português brasileiro, com
aplicação contextual, falsos positivos e exemplos próprios.

A implementação depende do contrato editorial da #3 e da estrutura inicial do
catálogo definida na #5. A calibração de voz da #4 não é pré-condição: seus
critérios são complementares e podem ser integrados antes ou depois deste
grupo, desde que o roteamento no `SKILL.md` permaneça coeso.

## Decisão de arquitetura

Os detalhes dos padrões ficarão em uma referência canônica própria, paralela à
referência dos padrões 1–6:

```text
skills/refinar-prosa/
├── SKILL.md
└── references/
    ├── conteudo.md
    └── linguagem.md

README.md
```

Responsabilidades:

- `skills/refinar-prosa/references/pt-BR/linguagem.md`: única fonte canônica dos
  nomes, regras, limites e exemplos dos padrões 7–13.
- `skills/refinar-prosa/SKILL.md`: mapa curto com números, nomes, famílias de
  sinais e ligação direta para a referência.
- `README.md`: resumo público dos mesmos números e nomes, sem copiar regras ou
  exemplos.

A referência será lida quando a revisão encontrar recorrência lexical sem
função, substituição artificial de verbos simples, paralelismos negativos,
tríades decorativas, variação lexical que prejudica a precisão, intervalos sem
escala real ou ocultação desnecessária do agente.

## Alternativas consideradas

### Uma referência por família — escolhida

Mantém o grupo 7–13 coeso, permite validar um esquema uniforme e evita que o
`SKILL.md` cresça com detalhes. Também preserva a numeração global do catálogo
sem misturar regras de conteúdo e de linguagem no mesmo arquivo.

### Acrescentar tudo a `conteudo.md`

Simplificaria o número de arquivos, mas confundiria famílias editoriais
distintas e faria uma leitura sobre linguagem carregar regras de conteúdo sem
necessidade. Foi rejeitada.

### Uma lista de substituições proibidas

Seria simples de aplicar, mas produziria falsos positivos e transferiria para o
português frequências observadas em outros idiomas. Foi rejeitada.

## Regra transversal de aplicação

Palavra, verbo, pontuação ou construção isolada não comprova um padrão. A skill
seguirá esta sequência:

```text
sinal candidato
  → função sintática e discursiva no contexto
  → precisão factual e terminológica
  → efeito sobre clareza, naturalidade e atribuição
  → edição mínima se o conjunto confirmar o padrão
```

Na dúvida, o trecho é preservado. Frequências associadas à escrita artificial
em inglês não serão tratadas como evidência automática em português. Termos
técnicos, nomes próprios, citações e escolhas necessárias ao domínio não serão
substituídos apenas para variar ou simplificar o vocabulário.

## Esquema obrigatório por padrão

Cada padrão em `linguagem.md` terá:

1. **Problema:** a distorção editorial que corrige.
2. **Sinais candidatos:** construções e funções que merecem inspeção, sem
   funcionar como lista proibida.
3. **Confirmação contextual:** evidências necessárias para aplicar o padrão.
4. **Não alterar quando:** usos legítimos e falsos positivos.
5. **Antes:** exemplo original em português brasileiro.
6. **Depois:** revisão mínima, sem fabricação nem omissão factual.
7. **Preservação factual e terminológica:** inventário do que permaneceu e da
   razão de qualquer remoção ou repetição deliberada.

Os exemplos do grupo alternarão prosa geral e documentação técnica. O conjunto
terá exemplos técnicos suficientes para testar preservação de termos de domínio
e exemplos gerais suficientes para testar cadência natural.

## Padrão 7 — Vocabulário recorrente sem função

### Problema

Repete adjetivos, advérbios ou fórmulas de forma perceptível, sem que a repetição
organize conceitos ou preserve um termo necessário.

### Aplicação contextual

Revisar apenas quando a recorrência não tiver função técnica, retórica ou de
coesão e produzir monotonia ou aparência formulaica. A repetição de um termo de
domínio deve ser preferida a sinônimos imprecisos.

### Exemplo de direção

Antes:

```text
O plano propõe uma abordagem robusta, uma rotina robusta de revisão e um
processo robusto de aprovação.
```

Depois:

```text
O plano define a abordagem, a rotina de revisão e o processo de aprovação.
```

Permanecem os três componentes. Sai apenas o adjetivo repetido, que não tinha
critério ou comparação; nenhum atributo novo é acrescentado.

## Padrão 8 — Substituição artificial de verbos simples

### Problema

Evita `ser`, `estar` ou `ter` por meio de perífrases e nominalizações que tornam
a frase menos direta sem aumentar a precisão.

### Aplicação contextual

Simplificar somente quando o verbo mais elaborado não expressar relação técnica
própria. Verbos específicos, como `implementar`, `persistir` ou `autenticar`,
continuam quando descrevem uma operação real.

### Exemplo de direção

Antes:

```text
A configuração apresenta como característica a presença de duas chaves
obrigatórias.
```

Depois:

```text
A configuração tem duas chaves obrigatórias.
```

Permanecem quantidade, obrigatoriedade e objeto. A perífrase é simplificada sem
alterar a terminologia técnica.

## Padrão 9 — Paralelismo negativo acrescentado

### Problema

Usa estruturas como “não apenas”, “não deixa de” ou uma negação final para dar
ênfase artificial a duas afirmações que poderiam ser diretas.

### Aplicação contextual

Remover o paralelismo somente quando as negações não delimitarem contraste,
exceção ou correção real. Manter quando a oposição for necessária ao argumento.

### Exemplo de direção

Antes:

```text
A atualização não apenas reduz o tempo de inicialização, como também não deixa
de simplificar a configuração.
```

Depois:

```text
A atualização reduz o tempo de inicialização e simplifica a configuração.
```

Permanecem os dois efeitos atribuídos à atualização. Saem apenas as negações
usadas como moldura enfática.

## Padrão 10 — Tríades decorativas

### Problema

Agrupa ideias em três para produzir ritmo ou autoridade, mesmo quando os itens
são redundantes, vagos ou não correspondem à estrutura real do assunto.

### Aplicação contextual

Editar apenas a tríade decorativa. Enumerações reais de três requisitos, etapas,
arquivos ou resultados são preservadas, assim como listas cuja extensão é
determinada pelos fatos.

### Exemplo de direção

Antes:

```text
O guia explica instalação, configuração e solução de problemas, oferecendo
clareza, completude e transformação.
```

Depois:

```text
O guia explica instalação, configuração e solução de problemas.
```

Permanece a enumeração factual de três conteúdos. Sai somente a segunda tríade,
formada por avaliações sem apoio.

## Padrão 11 — Variação lexical desnecessária

### Problema

Troca o mesmo referente por sinônimos elegantes para evitar repetição e, com
isso, cria ambiguidade ou perda de precisão.

### Aplicação contextual

Repetir deliberadamente o nome técnico quando a identidade do componente for
relevante. Variar o vocabulário continua legítimo quando os termos nomeiam
coisas distintas ou melhoram a leitura sem alterar o referente.

### Exemplo de direção

Antes:

```text
O servidor recebe a requisição. Esse serviço valida o token. A plataforma grava
o resultado no log. Nos três casos, trata-se do mesmo servidor.
```

Depois:

```text
O servidor recebe a requisição, valida o token e grava o resultado no log.
```

Permanecem o componente único, as três operações e seus objetos. Os sinônimos
imprecisos são removidos; `token` e `log` permanecem como termos técnicos.

## Padrão 12 — Intervalos falsos

### Problema

Usa “de X a Y” para ligar categorias que não formam escala, percurso ou
intervalo verificável.

### Aplicação contextual

Converter em enumeração ou relação explícita somente quando os extremos não
tiverem posições intermediárias pertinentes. Preservar intervalos numéricos,
temporais, geográficos e conceituais defensáveis.

### Exemplo de direção

Antes:

```text
O encontro abordou temas que foram da segurança à criatividade.
```

Depois:

```text
O encontro abordou segurança e criatividade.
```

Permanecem os dois temas. Sai apenas a sugestão de uma escala entre eles;
nenhum tema intermediário é inventado.

## Padrão 13 — Agente oculto sem necessidade

### Problema

Usa voz passiva ou fragmentos sem sujeito para esconder um agente relevante que
o próprio contexto já identifica.

### Aplicação contextual

Explicitar o agente somente quando ele estiver disponível na fonte e importar
para responsabilidade ou compreensão. Preservar a passiva quando o agente for
desconhecido, irrelevante, deliberadamente protegido ou quando o foco legítimo
for o resultado.

### Exemplo de direção

Antes:

```text
A equipe de infraestrutura revisou o ambiente. Em seguida, foi removido o
acesso ao banco e alterada a política de backup.
```

Depois:

```text
A equipe de infraestrutura revisou o ambiente, removeu o acesso ao banco e
alterou a política de backup.
```

Permanecem agente, sequência, ações e objetos. O agente não é inferido: já
estava identificado no contexto.

## Integração no fluxo da skill

Durante a leitura, a skill identifica sinais candidatos e carrega
`references/pt-BR/linguagem.md` somente quando algum deles for relevante. Durante a
auditoria factual e estilística, verifica também:

- se algum termo técnico ou nome próprio foi substituído;
- se uma oposição, escala ou agente foi inventado ou apagado;
- se uma enumeração factual foi confundida com tríade decorativa;
- se a edição aplicou uma proibição absoluta baseada em palavra isolada;
- se a cadência melhorou sem mudar idioma, intenção, público ou formalidade.

## Sincronização e validação

A implementação terá verificações estáticas para garantir que:

- a sequência global 7–13 apareça sem lacunas em `linguagem.md`, `SKILL.md` e
  README;
- os nomes estáveis sejam idênticos nos três arquivos;
- cada padrão contenha todos os campos obrigatórios;
- a referência esteja ligada diretamente pelo `SKILL.md`;
- os exemplos cubram prosa geral e documentação técnica;
- não haja proibições absolutas, placeholders ou metadados de Claude.

O validador de Agent Skills e o validador de plugins do Codex serão executados
depois das verificações específicas do catálogo.

## Fora de escopo

- implementar os padrões 14–33;
- criar dicionário global de palavras proibidas;
- introduzir heurísticas quantitativas importadas do inglês;
- alterar manifesto, `agents/openai.yaml`, versão ou componentes do plugin;
- criar testes de detecção probabilística de autoria.
