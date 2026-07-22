# Refinar Prosa Editorial Contract Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Tornar inequívoco o contrato editorial da skill `refinar-prosa`, com três modos de uso, auditoria contra omissão e fabricação, proteção de conteúdo não textual e exemplos originais em português.

**Architecture:** `skills/refinar-prosa/SKILL.md` continuará sendo a única fonte canônica do comportamento. O arquivo concentrará um contrato comum, seleção automática de modo, entradas e saídas específicas, ciclo interno, auditoria bidirecional, conteúdo protegido, falhas e exemplos; nenhum outro arquivo do produto será alterado.

**Tech Stack:** Markdown, frontmatter YAML, Python 3, `rg`, validador de Agent Skills e validador de plugins Codex.

## Global Constraints

- Modificar somente `skills/refinar-prosa/SKILL.md` como arquivo do produto.
- Manter `name: refinar-prosa` e a descrição atual no frontmatter.
- Manter pt-BR como único idioma oficialmente suportado nesta versão.
- Preservar informação e relações lógicas sem congelar a estrutura de parágrafos.
- Não criar catálogo de padrões, referências, scripts, assets ou integrações.
- Não modificar `.codex-plugin/plugin.json`, `skills/refinar-prosa/agents/openai.yaml` ou `README.md`.
- Não incluir promessas sobre detectores nem afirmações de autoria humana.
- Não expor cadeia de raciocínio, rascunho ou relatório de auditoria na saída.
- Não deixar marcadores incompletos ou metadados específicos do Claude.

## File Structure

| Arquivo | Responsabilidade |
| --- | --- |
| `skills/refinar-prosa/SKILL.md` | Contrato editorial comum, modos, ciclo interno, auditoria, conteúdo protegido, falhas e exemplos. |

---

### Task 1: Implementar o contrato editorial completo

**Files:**
- Modify: `skills/refinar-prosa/SKILL.md`
- Test: `skills/refinar-prosa/SKILL.md`

**Interfaces:**
- Consumes: texto colado, caminho de arquivo ou contexto de uma tarefa maior, com instruções opcionais de público, tom, formalidade e formato.
- Produces: revisão auditada nos modos texto colado, arquivo ou embutido, com a saída exata definida para cada modo.

- [ ] **Step 1: Executar a verificação negativa do contrato atual**

Run:

```bash
python3 -c 'from pathlib import Path; s=Path("skills/refinar-prosa/SKILL.md").read_text(); required=["## Contrato editorial", "## Seleção do modo", "### Texto colado", "### Arquivo", "### Embutido", "## Ciclo interno", "Fonte → rascunho", "Rascunho → fonte", "frontmatter", "links", "tabelas", "código", "comandos", "dados", "detectores", "autoria humana", "cadeia de raciocínio"]; missing=[x for x in required if x not in s]; errors=missing + (["contratos de modo"] if s.count("**Entrada:**") != 3 or s.count("**Comportamento:**") != 3 or s.count("**Saída") < 3 else []) + (["três exemplos"] if s.count("Use $refinar-prosa") < 3 else []); print("\n".join(errors)); raise SystemExit(bool(errors))'
```

Expected: exit code `1`; a saída lista, entre outros itens, `## Contrato editorial`,
`### Embutido`, `Fonte → rascunho` e `três exemplos`.

- [ ] **Step 2: Substituir o conteúdo da skill pelo contrato aprovado**

Use `apply_patch` para substituir integralmente
`skills/refinar-prosa/SKILL.md` por este conteúdo:

````markdown
---
name: refinar-prosa
description: "Use para revisar e reescrever prosa em português brasileiro, em texto colado ou arquivos, melhorando clareza e naturalidade sem alterar fatos, estrutura protegida ou voz."
---

# Refinar prosa

Revise somente a prosa em português brasileiro que o usuário colocar no escopo.
Melhore clareza, concisão, ritmo e naturalidade sem trocar o significado pela
forma.

## Contrato editorial

Este contrato vale em todos os modos:

- Preserve toda afirmação factual, nome, número, data, citação, fonte,
  atribuição e qualificação relevante.
- Trate incerteza, negação, condição, ressalva, comparação, causalidade, escopo e
  grau de confiança como informação protegida.
- Preserve a informação e suas relações lógicas, não a estrutura de parágrafos.
  Divida, una, reordene ou reescreva parágrafos somente quando isso não causar
  omissão nem mudança de sentido.
- Mantenha idioma, intenção, público, gênero textual e grau de formalidade,
  salvo instrução explícita em contrário.
- Não acrescente detalhes, exemplos, fontes, experiências, opiniões ou certeza
  para tornar o texto mais convincente.
- Edite somente o necessário e mantenha o original quando não houver melhoria
  útil.

Pt-BR é o único idioma oficialmente suportado nesta versão. Se a entrada estiver
claramente em outro idioma, não a modifique; informe brevemente esse limite.

## Seleção do modo

Escolha o modo automaticamente, nesta ordem:

1. Se houver caminho ou pedido explícito para editar um arquivo, use **arquivo**.
2. Se a revisão fizer parte de outra tarefa ou produzir texto pronto para um
   artefato maior, use **embutido**.
3. Se a solicitação incluir diretamente a prosa, use **texto colado**.

Só peça esclarecimento quando não conseguir identificar texto, caminho ou
destino.

## Modos

### Texto colado

**Entrada:** prosa incluída diretamente na solicitação, com instruções opcionais
de tom, público ou formato.

**Comportamento:** revise somente o trecho fornecido segundo o contrato
editorial.

**Saída padrão:** devolva apenas a versão final, sem prefácio, justificativa,
rascunho ou relatório de auditoria.

Se o usuário pedir explicação, apresente primeiro a versão final e depois uma
nota curta sobre alterações observáveis. Não exponha raciocínio interno.

### Arquivo

**Entrada:** caminho explícito para um arquivo legível e, opcionalmente,
instruções que delimitem trechos, público ou tom.

**Comportamento:** leia o arquivo, edite somente a prosa solicitada e não
reformate conteúdo fora do escopo.

**Saída:** salve a edição no mesmo arquivo e responda com o caminho alterado e um
resumo curto das mudanças. Se nenhuma mudança for útil, mantenha o arquivo
intacto e informe isso.

### Embutido

**Entrada:** prosa ou fatos disponíveis no contexto de uma tarefa maior, com
destino como descrição de pull request, mensagem de commit, documento ou outro
artefato.

**Comportamento:** produza redação pronta para inserção no destino, usando
somente informações presentes na tarefa.

**Saída:** retorne exclusivamente o texto final. Não acrescente prefácio, cerca
de código, resumo, justificativa ou auditoria.

## Ciclo interno

Execute o ciclo sem expô-lo na resposta:

1. **Leitura:** identifique modo, fonte, destino, intenção, público, formalidade,
   afirmações, qualificações e conteúdo protegido.
2. **Rascunho:** revise somente o necessário, com liberdade estrutural e sem
   adicionar conteúdo.
3. **Auditoria factual:** compare fonte e rascunho nas duas direções para
   detectar omissão e fabricação.
4. **Auditoria estilística:** confira idioma, intenção, público, formalidade,
   voz, instruções do usuário e conteúdo protegido.
5. **Versão final:** corrija divergências e produza exatamente a saída exigida
   pelo modo.

## Auditoria

### Auditoria factual

- **Fonte → rascunho:** confirme que cada afirmação, qualificação e relação
  lógica da fonte continua representada.
- **Rascunho → fonte:** confirme que cada detalhe factual da revisão possui
  apoio explícito na fonte ou nas instruções do usuário.
- Confira literalmente nomes, números, datas, citações e fontes.
- Corrija qualquer fabricação, omissão ou mudança de condição, causalidade,
  incerteza ou escopo antes da versão final.

### Auditoria estilística

- Confirme idioma, intenção, público, gênero e formalidade.
- Respeite instruções explícitas do usuário.
- Preserve a voz e escolhas legítimas sem uniformizar o texto.
- Confirme que conteúdo protegido permaneceu intacto.

## Conteúdo protegido em arquivos

Não modifique, salvo quando o usuário incluir explicitamente prosa interna no
escopo e a alteração puder preservar estrutura e significado:

- frontmatter e outros metadados estruturados;
- destinos e sintaxe de links;
- estrutura e dados de tabelas;
- blocos e trechos de código;
- comandos, flags, caminhos e argumentos;
- dados, identificadores e valores estruturados;
- citações literais e trechos em outro idioma;
- conteúdo fora do escopo indicado.

## Limites

- Não prometa evasão de detectores de texto gerado por IA.
- Não afirme que o resultado possui autoria humana.
- Não apresente a revisão como verificação factual ou revisão técnica,
  jurídica ou acadêmica especializada.
- Não transforme incerteza legítima em certeza.
- Não exponha cadeia de raciocínio, rascunho ou auditoria interna.

## Falhas e casos-limite

- Sem entrada identificável: peça texto, caminho ou destino.
- Arquivo ausente ou ilegível: não edite nada e informe o caminho problemático.
- Instrução estilística incompatível com preservação factual: preserve fatos e
  qualificações; só peça esclarecimento quando não houver interpretação segura.
- Estrutura protegida inseparável da alteração pedida: preserve o trecho e
  explique a limitação no resumo do modo arquivo.
- Texto já adequado: devolva o original nos modos texto colado e embutido; no
  modo arquivo, não escreva o arquivo e informe a ausência de mudança útil.

## Exemplos

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
````

- [ ] **Step 3: Executar a verificação positiva do contrato**

Run:

```bash
python3 -c 'from pathlib import Path; s=Path("skills/refinar-prosa/SKILL.md").read_text(); required=["## Contrato editorial", "## Seleção do modo", "### Texto colado", "### Arquivo", "### Embutido", "## Ciclo interno", "Fonte → rascunho", "Rascunho → fonte", "frontmatter", "links", "tabelas", "código", "comandos", "dados", "detectores", "autoria humana", "cadeia de raciocínio"]; missing=[x for x in required if x not in s]; errors=missing + (["contratos de modo"] if s.count("**Entrada:**") != 3 or s.count("**Comportamento:**") != 3 or s.count("**Saída") < 3 else []) + (["três exemplos"] if s.count("Use $refinar-prosa") < 3 else []); print("\n".join(errors)); raise SystemExit(bool(errors))'
```

Expected: exit code `0` e nenhuma saída.

- [ ] **Step 4: Validar a skill e o pacote**

Run:

```bash
python3 /home/thiago-botelho/.config/orca/codex-accounts/9ae230c7-073c-4dc6-85bc-436aca338b5d/home/skills/.system/skill-creator/scripts/quick_validate.py skills/refinar-prosa
```

Expected: exit code `0` e saída `Skill is valid!`.

Run:

```bash
python3 /home/thiago-botelho/.config/orca/codex-accounts/9ae230c7-073c-4dc6-85bc-436aca338b5d/home/skills/.system/plugin-creator/scripts/validate_plugin.py .
```

Expected: exit code `0` e saída iniciada por `Plugin validation passed:`.

- [ ] **Step 5: Verificar o escopo e a higiene da mudança**

Run:

```bash
git diff --name-only HEAD
```

Expected exatamente:

```text
skills/refinar-prosa/SKILL.md
```

Run:

```bash
rg -n 'TBD|\[TODO:|Claude' skills/refinar-prosa/SKILL.md
```

Expected: exit code `1` e nenhuma saída.

Run:

```bash
git diff --check
```

Expected: exit code `0` e nenhuma saída.

- [ ] **Step 6: Revisar o diff contra os critérios de aceite**

Run:

```bash
git diff -- skills/refinar-prosa/SKILL.md
```

Expected: o diff contém contrato comum, seleção automática, três modos com
entrada/comportamento/saída, ciclo interno, auditoria bidirecional, conteúdo
protegido, limites, falhas e três exemplos; nenhum outro arquivo aparece.

- [ ] **Step 7: Commitar o contrato editorial**

```bash
git add skills/refinar-prosa/SKILL.md
git commit -m "feat: define editorial contract"
```

Expected: commit criado contendo somente `skills/refinar-prosa/SKILL.md`.

- [ ] **Step 8: Confirmar o estado final**

Run:

```bash
git status --short --branch
```

Expected: árvore de trabalho limpa e `main` à frente de `origin/main` pelos
commits da especificação, do plano e da implementação.
