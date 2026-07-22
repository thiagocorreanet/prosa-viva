# Contrato editorial e modos da skill Refinar Prosa

## Contexto

Esta especificação detalha o comportamento central da skill `refinar-prosa`,
relacionado à issue #3 e à épica #1. O contrato deve existir antes do catálogo de
padrões para que todas as revisões compartilhem as mesmas garantias de
preservação, saída e auditoria.

O `SKILL.md` atual já contém princípios mínimos de preservação factual e proteção
de estruturas. A mudança os torna inequívocos, acrescenta os três modos de uso e
formaliza o ciclo interno de revisão.

## Decisão de arquitetura

O comportamento continuará integralmente em
`skills/refinar-prosa/SKILL.md`, a fonte canônica definida para a skill. O arquivo
será organizado em camadas:

1. contrato editorial comum;
2. seleção automática de modo;
3. contrato de entrada, comportamento e saída de cada modo;
4. ciclo interno de revisão;
5. auditoria factual e estilística;
6. conteúdo protegido e limites;
7. tratamento de falhas;
8. exemplos originais.

Esta entrega não cria referências, scripts ou novos componentes. Também não
modifica `.codex-plugin/plugin.json`, `agents/openai.yaml`, `README.md` nem o
catálogo futuro de padrões.

## Alternativas consideradas

### Contrato comum e modos separados — escolhida

Mantém as garantias invariáveis em uma única seção e descreve cada modo com
entrada, comportamento e saída próprios. Evita repetição e permite verificar os
critérios de aceite diretamente.

### Fluxo único com condicionais

Seria menor, mas espalharia condições de arquivo, texto colado e uso embutido
pelo documento. Foi rejeitado porque tornaria a saída de cada modo menos
previsível.

### Referências separadas por modo

Facilitaria uma expansão futura, mas adicionaria arquivos sem necessidade e
anteciparia a estratégia de divulgação progressiva. Foi rejeitado para preservar
a fundação enxuta.

## Contrato editorial comum

O contrato será obrigatório em todos os modos:

- Preservar toda afirmação factual, nome, número, data, citação, fonte,
  atribuição e qualificação relevante.
- Tratar como qualificações protegidas incerteza, negação, condição, ressalva,
  comparação, causalidade, escopo e grau de confiança.
- Preservar a informação e suas relações lógicas sem exigir a mesma estrutura de
  parágrafos. A revisão pode dividir, unir, reordenar ou reescrever parágrafos.
- Manter idioma, intenção, público, gênero textual e grau de formalidade, salvo
  instrução explícita em contrário.
- Aplicar a política linguística vigente: pt-BR é o único idioma oficialmente
  suportado nesta versão; entradas claramente escritas em outro idioma não são
  modificadas.
- Não acrescentar detalhes, exemplos, fontes, experiências, opiniões ou certeza
  para tornar o texto mais convincente.
- Não prometer evasão de detectores de texto gerado por IA.
- Não afirmar que o texto final possui autoria humana.
- Não apresentar a revisão como verificação factual ou revisão técnica,
  jurídica ou acadêmica especializada.
- Não expor cadeia de raciocínio, rascunho ou auditoria interna. Quando uma
  explicação for permitida, descrever somente alterações observáveis.

Preservar informação não significa congelar a forma. Uma reorganização só é
válida quando mantém todas as afirmações e também as relações entre elas.

## Seleção automática de modo

A skill inferirá o modo sem exigir rótulos do usuário, nesta precedência:

1. Se houver caminho ou pedido explícito para editar um arquivo, usar **arquivo**.
2. Se a revisão fizer parte de outra tarefa ou produzir texto pronto para um
   artefato maior, usar **embutido**.
3. Se a solicitação incluir diretamente a prosa a revisar, usar **texto colado**.

A precedência resolve solicitações com sinais combinados. A skill só pede
esclarecimento quando não consegue identificar texto, caminho ou destino.

## Modos

### Texto colado

**Entrada:** prosa incluída diretamente na solicitação, com instruções opcionais
de tom, público ou formato.

**Comportamento:** revisar o texto segundo o contrato comum sem modificar
conteúdo fora do trecho delimitado.

**Saída padrão:** somente a versão final revisada, sem prefácio, justificativa,
rascunho ou relatório de auditoria.

**Saída quando o usuário pedir explicação:** apresentar primeiro a versão final e
depois uma nota curta sobre alterações observáveis. A nota não revela raciocínio
interno.

### Arquivo

**Entrada:** caminho explícito para um arquivo legível e, opcionalmente,
instruções que delimitam trechos ou tom.

**Comportamento:** ler o arquivo, editar somente a prosa solicitada e preservar
todo conteúdo protegido. Não reformatar trechos fora do escopo.

**Saída:** salvar a edição no mesmo arquivo e responder com o caminho alterado e
um resumo curto das mudanças. O resumo descreve categorias de alteração, não a
auditoria interna. Se nenhuma mudança for útil, manter o arquivo intacto e
informar isso.

### Embutido

**Entrada:** prosa ou fatos disponíveis no contexto de uma tarefa maior, com um
destino como descrição de pull request, mensagem de commit, documento ou outro
artefato.

**Comportamento:** produzir a redação final pronta para inserção no destino,
usando somente informações presentes na tarefa.

**Saída:** exclusivamente o texto final. Não acrescentar prefácio, cerca de
código, resumo, justificativa ou auditoria, mesmo quando a revisão ocorrer dentro
de uma tarefa com várias etapas.

## Ciclo interno

O ciclo é obrigatório e permanece oculto na resposta:

1. **Leitura:** identificar modo, fonte, destino, intenção, público, formalidade,
   afirmações, qualificações e conteúdo protegido.
2. **Rascunho:** revisar somente o necessário, com liberdade estrutural e sem
   adicionar conteúdo.
3. **Auditoria factual:** comparar fonte e rascunho nas duas direções para
   detectar omissão e fabricação.
4. **Auditoria estilística:** conferir idioma, intenção, público, formalidade,
   voz, instruções do usuário e integridade do conteúdo protegido.
5. **Versão final:** corrigir divergências encontradas e produzir exatamente a
   saída exigida pelo modo.

## Auditoria factual e estilística

A auditoria factual será bidirecional:

- **Fonte → rascunho:** cada afirmação, qualificação e relação lógica da fonte
  continua representada na revisão.
- **Rascunho → fonte:** cada detalhe factual da revisão possui apoio explícito na
  fonte ou nas instruções do usuário.

Também será necessário conferir literalmente nomes, números, datas, citações e
fontes. A auditoria deve detectar tanto fabricação quanto omissão, inclusive
quando uma frase aparentemente mais simples altera condição, causalidade,
incerteza ou escopo.

A auditoria estilística confirma que a revisão:

- mantém idioma, intenção, público, gênero e formalidade;
- respeita instruções explícitas do usuário;
- preserva a voz sem uniformizar escolhas legítimas;
- não força mudanças em texto já adequado;
- não alterou conteúdo protegido.

## Conteúdo protegido em arquivos

Em modo arquivo, a skill não modifica:

- frontmatter e outros metadados estruturados;
- destinos e sintaxe de links;
- estrutura e dados de tabelas;
- blocos e trechos de código;
- comandos, flags, caminhos e argumentos;
- dados, identificadores e valores estruturados;
- citações literais e trechos em outro idioma;
- qualquer conteúdo fora do escopo indicado pelo usuário.

Texto visível de links e células de tabela só pode ser revisado quando o usuário
o incluir explicitamente no escopo e a alteração não modificar seu significado
ou sua estrutura.

## Tratamento de falhas

- Sem entrada identificável: pedir texto, caminho ou destino.
- Arquivo ausente ou ilegível: não editar nada e informar o caminho problemático.
- Idioma não suportado: não modificar a entrada e informar brevemente o limite.
- Instrução estilística incompatível com preservação factual: preservar fatos e
  qualificações; pedir esclarecimento apenas quando não houver interpretação
  segura.
- Estrutura protegida inseparável da alteração pedida: preservar o trecho e
  explicar a limitação no resumo do modo arquivo.
- Texto já adequado: devolver o original nos modos texto colado e embutido; no
  modo arquivo, não escrever o arquivo e informar a ausência de mudança útil.

## Exemplos originais

### Texto colado

Entrada:

```text
Use $refinar-prosa para revisar o aviso abaixo.

A manutenção do portal ocorrerá em 14 de agosto, das 22h às 23h. Durante esse
período, o envio de formulários ficará indisponível, mas a consulta de protocolos
continuará funcionando.
```

Saída:

```text
Em 14 de agosto, o portal passará por manutenção das 22h às 23h. Nesse intervalo,
não será possível enviar formulários; a consulta de protocolos continuará
disponível.
```

O exemplo preserva data, horário, indisponibilidade e exceção sem explicar a
auditoria.

### Arquivo

Entrada:

```text
Use $refinar-prosa para revisar docs/comunicado.md. Preserve o frontmatter, o
link de suporte e o bloco com o comando de atualização.
```

Saída após uma edição bem-sucedida:

```text
Revisei docs/comunicado.md. Enxuguei a prosa e preservei o frontmatter, o link de
suporte e o comando de atualização.
```

O arquivo é o artefato principal; a resposta contém somente o caminho e o resumo
curto exigido pelo modo.

### Embutido

Entrada:

```text
Use $refinar-prosa para transformar estas notas na descrição final da PR.
Retorne apenas o texto pronto: adiciona filtro por status; corrige paginação;
inclui testes para os dois comportamentos.
```

Saída:

```text
Adiciona filtro por status e corrige a paginação da listagem. Inclui testes para
os dois comportamentos.
```

O exemplo não inclui prefácio nem resumo separado.

## Validação

A implementação deve executar:

1. `quick_validate.py` contra `skills/refinar-prosa/`.
2. `validate_plugin.py` contra a raiz do repositório.
3. Uma verificação estática dos títulos e contratos dos três modos.
4. Uma verificação da presença da auditoria bidirecional contra omissão e
   fabricação.
5. Uma verificação das estruturas protegidas e das proibições sobre detectores e
   autoria humana.
6. Uma verificação de um exemplo original para cada modo.
7. Uma busca por placeholders e metadados específicos do Claude.
8. `git diff --check`.

## Critérios de aceite verificáveis

- Texto colado, arquivo e embutido possuem entrada, comportamento e saída
  explícitos.
- A seleção automática usa a precedência arquivo → embutido → texto colado.
- A auditoria compara fonte e rascunho nas duas direções.
- Frontmatter, links, tabelas, código, comandos e dados estão explicitamente
  protegidos.
- A resposta padrão não contém rascunho, cadeia de raciocínio ou relatório de
  auditoria.
- Há um exemplo original em português para cada modo.
- Somente `skills/refinar-prosa/SKILL.md` é alterado na implementação.
