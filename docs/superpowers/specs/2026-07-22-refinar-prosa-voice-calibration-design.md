# Calibração de voz e limites de personalidade da skill Refinar Prosa

## Contexto

Esta especificação detalha a calibração de voz da skill `refinar-prosa`,
relacionada à issue #4 e à épica #1. O objetivo é adaptar a revisão ao autor sem
transformar toda prosa em uma voz casual genérica e sem permitir que estilo
introduza informação ausente.

A calibração amplia o contrato editorial planejado na #3. Como as duas mudanças
alteram `skills/refinar-prosa/SKILL.md`, a implementação da #4 deve ocorrer
depois da implementação da #3 para evitar patches concorrentes e preservar uma
única fonte canônica.

## Decisão de arquitetura

A calibração será descrita no próprio `SKILL.md`. Não haverá arquivo de perfil,
memória persistente, referência adicional ou estado entre tarefas.

Durante cada tarefa, a skill construirá internamente um perfil temporário a
partir da amostra do usuário, filtrará esse perfil pelos limites do gênero e o
descartará depois de produzir a resposta. O perfil nunca será tratado como fonte
de fatos para o texto-alvo.

Esta entrega modifica somente `skills/refinar-prosa/SKILL.md`. Manifesto,
`agents/openai.yaml`, README, scripts e catálogo de padrões permanecem fora do
escopo.

## Alternativas consideradas

### Perfil temporário com limites de gênero — escolhida

Extrai sinais observáveis da amostra e aplica somente aqueles compatíveis com o
gênero, os fatos e as instruções. Produz influência reconhecível sem copiar ruído
ou transportar conteúdo da amostra.

### Imitação direta da amostra

Produziria semelhança mais intensa, mas também copiaria erros, exageraria
maneirismos e poderia levar casualidade ou opinião a gêneros incompatíveis. Foi
rejeitada.

### Perfis fixos formal, casual e técnico

Seria previsível, porém reduziria a amostra do usuário a um rótulo genérico e
entregaria pouca adaptação autoral. Os três rótulos serão usados apenas como
casos de exemplo, não como presets.

## Separação entre voz e informação

A amostra e o texto-alvo têm responsabilidades distintas:

- **Amostra:** fornece somente evidências de estilo.
- **Texto-alvo:** fornece fatos, opiniões, experiências, posicionamentos e
  conteúdo que podem aparecer na revisão.
- **Instruções do usuário:** fornecem objetivo, público, gênero, restrições e
  mudanças de tom permitidas.

Nenhum fato, nome, número, data, citação, fonte, opinião, experiência ou primeira
pessoa presente apenas na amostra pode migrar para o texto-alvo. A auditoria
factual da #3 continua valendo depois da calibração.

## Entrada e delimitação

A calibração é ativada quando a solicitação contém uma amostra de voz e um
texto-alvo distinguíveis, por rótulos, blocos separados ou linguagem inequívoca.
Não haverá tamanho mínimo rígido.

- Amostras com vários sinais recorrentes permitem calibração mais forte.
- Amostras curtas ou ambíguas permitem apenas ajustes sustentados por evidência
  clara.
- Se amostra e texto-alvo não puderem ser distinguidos com segurança, a skill
  pede que o usuário os delimite antes de revisar.

A ausência de amostra não é erro. Nesse caso, aplica-se o padrão compatível com
o gênero definido nesta especificação.

## Formação do perfil temporário

A skill observará:

- extensão média e variação das frases;
- alternância entre frases completas, fragmentos e enumerações;
- vocabulário, registro e grau de formalidade;
- pontuação, contrações e uso de parênteses ou apartes;
- aberturas de parágrafo e tipos de transição;
- regionalismos, humor e marcas de posicionamento;
- irregularidades recorrentes que pareçam deliberadas.

Sinais recorrentes terão mais peso do que ocorrências isoladas. A skill não deve
inferir um hábito autoral forte a partir de um único travessão, uma única gíria,
uma frase excepcionalmente curta ou qualquer outro indício solitário.

Erros aparentes de ortografia, digitação, regência ou concordância não entram no
perfil. Eles só podem ser reproduzidos quando o usuário pedir explicitamente
imitação também dessas características e isso não prejudicar a compreensão ou
uma restrição superior.

## Ordem de prioridade

Conflitos serão resolvidos nesta ordem:

1. preservação factual, conteúdo protegido e instruções explícitas;
2. limites do gênero, finalidade e público;
3. perfil observado na amostra;
4. heurísticas gerais de clareza e naturalidade.

A amostra prevalece sobre preferências editoriais genéricas. Ela não prevalece
sobre fatos, instruções explícitas nem adequação ao gênero. Quando duas
características da amostra entram em conflito, padrões recorrentes e compatíveis
com o texto-alvo vencem ocorrências isoladas.

## Limites por gênero

### Pessoal, ensaio e opinião

Pode preservar humor, tensão, posicionamento, apartes, irregularidades
deliberadas e ritmo autoral quando essas características forem sustentadas pela
amostra e compatíveis com o texto-alvo. Não pode criar experiências, opiniões ou
reações que existam somente na amostra.

### Profissional e institucional

Pode manter cordialidade, vocabulário e ritmo do autor. Deve conter intimidade,
humor, regionalismo ou fragmentação quando prejudicarem objetivo, público ou
clareza institucional.

### Marketing

Pode adaptar energia, ritmo e vocabulário. Não pode criar benefícios, resultados,
urgência, depoimentos, comparações, garantias ou superlativos que não tenham sido
fornecidos no texto-alvo ou nas instruções.

### Técnico, legal, enciclopédico e de referência

Prioriza neutralidade, precisão e rastreabilidade. Não introduz primeira pessoa,
opinião, humor, regionalismo, experiência ou posicionamento artificial. Pode
aproveitar somente características neutras e compatíveis da amostra, como
concisão, tamanho das frases e preferência por transições diretas.

## Comportamento sem amostra

Sem amostra, a skill identifica gênero, finalidade e público pela solicitação e
pelo texto-alvo. O padrão é:

- claro e direto;
- compatível com o grau de formalidade do gênero;
- neutro quando gênero ou público forem incertos;
- fiel à voz já presente no texto-alvo;
- nunca casual por padrão.

Quando o texto-alvo já apresentar uma voz consistente, essa voz funciona como
evidência local e deve ser preservada sem inventar características adicionais.

## Fluxo interno

A calibração integra o ciclo da #3:

1. separar amostra, texto-alvo e instruções;
2. identificar gênero, finalidade, público e limites aplicáveis;
3. extrair sinais recorrentes da amostra;
4. remover fatos, conteúdo isolado, erros aparentes e sinais incompatíveis;
5. formar o perfil temporário permitido pelo gênero;
6. revisar o texto-alvo segundo o contrato editorial;
7. auditar preservação factual, adequação ao gênero e influência observável da
   amostra;
8. responder segundo o modo texto colado, arquivo ou embutido definido na #3;
9. descartar o perfil temporário.

A resposta não lista o perfil nem a auditoria, salvo quando o usuário pedir uma
descrição das alterações. Mesmo nesse caso, descreve apenas escolhas observáveis,
sem expor raciocínio interno.

## Auditoria de voz

Antes da versão final, a skill confirma:

- nenhuma informação migrou da amostra para o texto-alvo;
- características aplicadas possuem evidência recorrente ou clara;
- gênero, finalidade e público continuam adequados;
- textos técnicos não receberam primeira pessoa nem opinião artificial;
- marketing não recebeu alegações novas;
- a amostra produziu influência observável quando havia sinais seguros;
- sem amostra, o resultado permaneceu claro, direto e compatível com o gênero;
- erros isolados não foram copiados sem pedido explícito.

## Falhas e casos-limite

- **Amostra e alvo indistinguíveis:** pedir delimitação antes da revisão.
- **Amostra curta:** usar somente sinais claros e manter o restante conservador.
- **Amostra contraditória:** preferir padrões recorrentes e não misturar registros
  incompatíveis.
- **Pedido de voz conflitante com o gênero:** seguir a instrução quando segura,
  sem fabricar fatos, experiências ou posicionamentos.
- **Gênero incerto:** usar neutralidade clara e direta.
- **Nenhuma característica segura:** revisar sem calibração forte.
- **Amostra contém fatos ou experiências atraentes:** ignorar esse conteúdo e
  aproveitar somente evidências de estilo.

## Exemplos originais

### Voz formal

Amostra:

```text
Encaminho a versão consolidada do relatório. As alterações concentram-se nos
critérios de acesso e entram em vigor em 3 de setembro.
```

Texto-alvo:

```text
precisamos avisar que o cadastro fecha sexta às 18h e reabre segunda às 9h
```

Saída calibrada:

```text
O cadastro será encerrado na sexta-feira, às 18h, e reaberto na segunda-feira,
às 9h.
```

O resultado aproveita formalidade e construção direta sem importar os fatos do
relatório usado como amostra.

### Voz casual

Amostra:

```text
Fui conferir e, olha, era mais simples do que parecia. Duas mudanças, cinco
minutos e pronto.
```

Texto-alvo:

```text
Eu reorganizei a estante durante a manhã. Encontrei os livros que estavam
guardados em duas caixas.
```

Saída calibrada:

```text
Reorganizei a estante de manhã e, olha, encontrei os livros. Estavam guardados
em duas caixas.
```

O aparte, as frases curtas e a contração são compatíveis com um relato pessoal;
nenhum fato da amostra foi transferido.

### Voz técnica

Amostra:

```text
Fui mexer nisso e, sinceramente, a solução antiga já tinha passado da hora.
Troquei tudo e ficou bem melhor.
```

Texto-alvo:

```text
A migração substitui o endpoint v1 pelo v2. O v1 será desativado em 30 de
novembro. Clientes devem atualizar a variável API_VERSION.
```

Saída calibrada:

```text
A migração substitui o endpoint v1 pelo v2. O v1 será desativado em 30 de
novembro. Antes dessa data, os clientes devem atualizar a variável API_VERSION.
```

O resultado aproveita concisão e ritmo, mas rejeita primeira pessoa, opinião e
casualidade incompatíveis com uma nota técnica.

## Validação

A implementação deve executar:

1. uma verificação estática da separação entre amostra e texto-alvo;
2. uma verificação da ordem de prioridade;
3. uma verificação das dimensões do perfil temporário;
4. uma verificação do comportamento com e sem amostra;
5. uma verificação dos limites para conteúdo pessoal, marketing e material
   técnico, legal ou de referência;
6. uma verificação da proibição de primeira pessoa e opinião artificiais em
   conteúdo técnico;
7. uma verificação dos exemplos formal, casual e técnico;
8. `quick_validate.py` contra a skill;
9. `validate_plugin.py` contra a raiz do pacote;
10. busca por placeholders e metadados específicos do Claude;
11. `git diff --check`.

## Critérios de aceite verificáveis

- Voz e informação factual possuem fontes e responsabilidades distintas.
- Uma amostra com sinais seguros influencia o resultado de maneira observável.
- Sem amostra, o padrão é claro, direto e compatível com o gênero.
- Textos técnicos não recebem primeira pessoa nem opinião artificiais.
- Marketing não recebe alegações novas.
- Erros isolados não são copiados sem pedido explícito.
- Há casos originais de voz formal, casual e técnica.
- A implementação modifica somente `skills/refinar-prosa/SKILL.md` e acontece
  depois da implementação planejada da #3.
