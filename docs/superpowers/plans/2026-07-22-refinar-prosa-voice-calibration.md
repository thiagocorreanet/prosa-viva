# Refinar Prosa Voice Calibration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Adicionar calibração temporária de voz ao `refinar-prosa`, com influência observável da amostra, limites por gênero e separação rígida entre estilo e informação factual.

**Architecture:** A calibração será acrescentada ao `skills/refinar-prosa/SKILL.md` depois que o contrato da #3 estiver implementado. O perfil será derivado e descartado dentro de cada tarefa; não haverá arquivo de perfil, memória persistente ou novo componente.

**Tech Stack:** Markdown, frontmatter YAML, Python 3, `rg`, validador de Agent Skills e validador de plugins Codex.

## Global Constraints

- A implementação da #3 é pré-condição obrigatória e deve estar presente no `SKILL.md` antes desta mudança.
- Modificar somente `skills/refinar-prosa/SKILL.md` como arquivo do produto.
- Manter `skills/refinar-prosa/SKILL.md` como única fonte canônica.
- Não criar perfil persistente, referência, script, asset ou integração.
- Não modificar `.codex-plugin/plugin.json`, `skills/refinar-prosa/agents/openai.yaml` ou `README.md`.
- A amostra fornece estilo; o texto-alvo fornece fatos, opiniões e experiências.
- Preservação factual, instruções explícitas e limites do gênero têm prioridade sobre imitação.
- Pt-BR continua sendo o único idioma oficialmente suportado nesta versão.
- Erros isolados não são copiados sem pedido explícito.
- Textos técnicos não recebem primeira pessoa, opinião ou experiência artificial.
- Marketing não recebe alegações, resultados ou urgência não fornecidos.
- Não deixar marcadores incompletos nem metadados específicos do Claude.

## File Structure

| Arquivo | Responsabilidade |
| --- | --- |
| `skills/refinar-prosa/SKILL.md` | Contrato da #3 mais perfil temporário de voz, prioridades, limites por gênero, auditoria e exemplos. |

---

### Task 1: Acrescentar calibração de voz ao contrato editorial

**Files:**
- Modify: `skills/refinar-prosa/SKILL.md`
- Test: `skills/refinar-prosa/SKILL.md`

**Interfaces:**
- Consumes: o contrato implementado da #3, uma amostra de voz opcional, texto-alvo e instruções de gênero, público e finalidade.
- Produces: revisão no modo definido pela #3, influenciada apenas por sinais estilísticos seguros e compatíveis com o gênero.

- [ ] **Step 1: Verificar a pré-condição da #3**

Run:

```bash
python3 -c 'from pathlib import Path; s=Path("skills/refinar-prosa/SKILL.md").read_text(); required=["## Contrato editorial", "## Seleção do modo", "### Texto colado", "### Arquivo", "### Embutido", "## Ciclo interno", "Fonte → rascunho", "Rascunho → fonte"]; missing=[x for x in required if x not in s]; print("\n".join(missing)); raise SystemExit(bool(missing))'
```

Expected antes de iniciar a #4: exit code `0` e nenhuma saída. Se houver qualquer
item na saída, pare e execute primeiro o plano
`docs/superpowers/plans/2026-07-22-refinar-prosa-editorial-contract.md`.

- [ ] **Step 2: Executar a verificação negativa da calibração**

Run:

```bash
python3 -c 'from pathlib import Path; s=Path("skills/refinar-prosa/SKILL.md").read_text(); required=["## Calibração de voz", "### Formação do perfil temporário", "### Ordem de prioridade", "### Limites por gênero", "### Comportamento sem amostra", "### Auditoria de voz", "### Voz formal", "### Voz casual", "### Voz técnica"]; missing=[x for x in required if x not in s]; print("\n".join(missing)); raise SystemExit(bool(missing))'
```

Expected: exit code `1`; a saída lista todas as seções de calibração ainda
ausentes.

- [ ] **Step 3: Inserir o contrato de calibração e seus exemplos**

Use `apply_patch` com este patch exato:

````diff
*** Begin Patch
*** Update File: skills/refinar-prosa/SKILL.md
@@
 - Confirme idioma, intenção, público, gênero e formalidade.
 - Respeite instruções explícitas do usuário.
 - Preserve a voz e escolhas legítimas sem uniformizar o texto.
 - Confirme que conteúdo protegido permaneceu intacto.
 
+## Calibração de voz
+
+Quando houver amostra e texto-alvo distinguíveis, trate-os como fontes
+separadas:
+
+- **Amostra:** fornece somente evidências de estilo.
+- **Texto-alvo:** fornece fatos, opiniões, experiências e conteúdo que podem
+  aparecer na revisão.
+- **Instruções:** fornecem objetivo, público, gênero e restrições.
+
+Nunca transfira para o texto-alvo fato, nome, número, data, citação, fonte,
+opinião, experiência ou primeira pessoa presente somente na amostra. O perfil de
+voz existe apenas durante a tarefa e deve ser descartado depois da resposta.
+
+### Formação do perfil temporário
+
+Observe:
+
+- extensão e variação das frases;
+- alternância entre frases completas, fragmentos e enumerações;
+- vocabulário, registro e grau de formalidade;
+- pontuação, contrações, parênteses e apartes;
+- aberturas de parágrafo e transições;
+- regionalismos, humor e marcas de posicionamento;
+- irregularidades recorrentes que pareçam deliberadas.
+
+Dê mais peso a sinais recorrentes do que a ocorrências isoladas. Não deduza um
+hábito forte a partir de uma única gíria, pontuação ou frase excepcional.
+Amostras curtas permitem somente ajustes sustentados por evidência clara.
+
+Não copie erros aparentes de ortografia, digitação, regência ou concordância,
+salvo quando o usuário pedir explicitamente também essas características e a
+imitação não violar uma restrição superior.
+
+### Ordem de prioridade
+
+Resolva conflitos nesta ordem:
+
+1. preservação factual, conteúdo protegido e instruções explícitas;
+2. limites do gênero, finalidade e público;
+3. perfil observado na amostra;
+4. heurísticas gerais de clareza e naturalidade.
+
+A amostra prevalece sobre preferências editoriais genéricas, mas nunca sobre
+fatos, instruções explícitas ou adequação ao gênero.
+
+### Limites por gênero
+
+- **Pessoal, ensaio e opinião:** preserve humor, tensão, posicionamento, apartes
+  e ritmo quando sustentados pela amostra e pelo texto-alvo. Não crie
+  experiências ou opiniões.
+- **Profissional e institucional:** preserve cordialidade, vocabulário e ritmo,
+  mas contenha intimidade, humor ou regionalismo que prejudiquem a finalidade.
+- **Marketing:** adapte energia e vocabulário sem criar benefícios, resultados,
+  urgência, depoimentos, comparações, garantias ou superlativos.
+- **Técnico, legal, enciclopédico e de referência:** priorize neutralidade e
+  precisão. Não introduza primeira pessoa, opinião, humor, regionalismo,
+  experiência ou posicionamento artificial.
+
+### Comportamento sem amostra
+
+Sem amostra, identifique gênero, finalidade e público pela solicitação e pelo
+texto-alvo. Use um padrão claro, direto e compatível com a formalidade do gênero.
+Quando houver dúvida, seja neutro; nunca torne o texto casual por padrão.
+
+Se o texto-alvo já tiver voz consistente, preserve-a como evidência local sem
+inventar características adicionais.
+
+### Fluxo de calibração
+
+1. Separe amostra, texto-alvo e instruções.
+2. Identifique gênero, finalidade, público e limites.
+3. Extraia sinais recorrentes da amostra.
+4. Remova fatos, conteúdo isolado, erros aparentes e sinais incompatíveis.
+5. Forme o perfil temporário permitido pelo gênero.
+6. Revise o texto-alvo segundo o contrato editorial.
+7. Audite fatos, gênero e influência observável da amostra.
+8. Responda segundo o modo selecionado.
+9. Descarte o perfil temporário.
+
+### Auditoria de voz
+
+Antes da versão final, confirme:
+
+- nenhuma informação migrou da amostra para o texto-alvo;
+- características aplicadas possuem evidência recorrente ou clara;
+- gênero, finalidade e público continuam adequados;
+- textos técnicos não receberam primeira pessoa nem opinião artificial;
+- marketing não recebeu alegações novas;
+- a amostra influenciou o resultado quando havia sinais seguros;
+- sem amostra, o resultado permaneceu claro e compatível com o gênero;
+- erros isolados não foram copiados sem pedido explícito.
+
+Se amostra e texto-alvo forem indistinguíveis, peça delimitação. Se a amostra
+for curta, contraditória ou não tiver características seguras, aplique somente
+sinais claros e mantenha o restante conservador.
+
 ## Conteúdo protegido em arquivos
@@
 - Texto já adequado: devolva o original nos modos texto colado e embutido; no
   modo arquivo, não escreva o arquivo e informe a ausência de mudança útil.
 
+## Exemplos de calibração
+
+### Voz formal
+
+Amostra:
+
+```text
+Encaminho a versão consolidada do relatório. As alterações concentram-se nos
+critérios de acesso e entram em vigor em 3 de setembro.
+```
+
+Texto-alvo:
+
+```text
+precisamos avisar que o cadastro fecha sexta às 18h e reabre segunda às 9h
+```
+
+Saída calibrada:
+
+```text
+O cadastro será encerrado na sexta-feira, às 18h, e reaberto na segunda-feira,
+às 9h.
+```
+
+### Voz casual
+
+Amostra:
+
+```text
+Fui conferir e, olha, era mais simples do que parecia. Duas mudanças, cinco
+minutos e pronto.
+```
+
+Texto-alvo:
+
+```text
+Eu reorganizei a estante durante a manhã. Encontrei os livros que estavam
+guardados em duas caixas.
+```
+
+Saída calibrada:
+
+```text
+Reorganizei a estante de manhã e, olha, encontrei os livros. Estavam guardados
+em duas caixas.
+```
+
+### Voz técnica
+
+Amostra:
+
+```text
+Fui mexer nisso e, sinceramente, a solução antiga já tinha passado da hora.
+Troquei tudo e ficou bem melhor.
+```
+
+Texto-alvo:
+
+```text
+A migração substitui o endpoint v1 pelo v2. O v1 será desativado em 30 de
+novembro. Clientes devem atualizar a variável API_VERSION.
+```
+
+Saída calibrada:
+
+```text
+A migração substitui o endpoint v1 pelo v2. O v1 será desativado em 30 de
+novembro. Antes dessa data, os clientes devem atualizar a variável API_VERSION.
+```
+
 ## Exemplos
*** End Patch
````

- [ ] **Step 4: Executar a verificação positiva da calibração**

Run:

```bash
python3 -c 'from pathlib import Path; s=Path("skills/refinar-prosa/SKILL.md").read_text(); required=["## Calibração de voz", "### Formação do perfil temporário", "### Ordem de prioridade", "### Limites por gênero", "### Comportamento sem amostra", "### Auditoria de voz", "### Voz formal", "### Voz casual", "### Voz técnica", "Amostra:", "Texto-alvo:", "Saída calibrada:"]; missing=[x for x in required if x not in s]; errors=missing + (["três casos calibrados"] if s.count("Saída calibrada:") != 3 else []); print("\n".join(errors)); raise SystemExit(bool(errors))'
```

Expected: exit code `0` e nenhuma saída.

- [ ] **Step 5: Verificar separação, prioridades e limites**

Run:

```bash
python3 -c 'from pathlib import Path; s=Path("skills/refinar-prosa/SKILL.md").read_text(); required=["Amostra:** fornece somente evidências de estilo", "Texto-alvo:** fornece fatos", "preservação factual, conteúdo protegido e instruções explícitas", "perfil observado na amostra", "nunca torne o texto casual por padrão", "Não introduza primeira pessoa", "marketing não recebeu alegações novas", "erros isolados não foram copiados"]; missing=[x for x in required if x not in s]; print("\n".join(missing)); raise SystemExit(bool(missing))'
```

Expected: exit code `0` e nenhuma saída.

- [ ] **Step 6: Validar a skill e o pacote**

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

- [ ] **Step 7: Verificar escopo e higiene da mudança**

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

- [ ] **Step 8: Revisar o diff contra a especificação**

Run:

```bash
git diff -- skills/refinar-prosa/SKILL.md
```

Expected: o diff contém perfil temporário, separação entre amostra e alvo, ordem
de prioridade, limites por gênero, comportamento sem amostra, auditoria de voz e
três exemplos; nenhum outro arquivo aparece.

- [ ] **Step 9: Commitar a calibração de voz**

```bash
git add skills/refinar-prosa/SKILL.md
git commit -m "feat: add voice calibration"
```

Expected: commit criado contendo somente `skills/refinar-prosa/SKILL.md`.

- [ ] **Step 10: Confirmar o estado final**

Run:

```bash
git status --short --branch
```

Expected: árvore de trabalho limpa e `main` à frente de `origin/main` pelos
commits de especificação, plano e implementação.
