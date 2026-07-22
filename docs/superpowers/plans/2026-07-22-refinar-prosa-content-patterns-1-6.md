# Refinar Prosa Content Patterns 1–6 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implementar os padrões de conteúdo 1–6 em uma referência canônica para pt-BR, com roteamento direto no `SKILL.md` e resumo sincronizado no README.

**Architecture:** `skills/refinar-prosa/references/pt-BR/conteudo.md` conterá regras, limites, exemplos e inventários factuais. `SKILL.md` terá apenas o mapa de roteamento, e o README repetirá somente números e nomes; validações estáticas garantirão que as três sequências permaneçam idênticas.

**Tech Stack:** Markdown, frontmatter YAML, Python 3, expressões regulares, `rg`, validador de Agent Skills e validador de plugins Codex.

## Global Constraints

- A implementação da #3 é pré-condição obrigatória.
- Criar somente `skills/refinar-prosa/references/pt-BR/conteudo.md` e modificar somente `skills/refinar-prosa/SKILL.md` e `README.md` como arquivos do produto.
- A referência é a única fonte canônica de regras, sinais, limites e exemplos.
- O `SKILL.md` deve ligar diretamente `references/pt-BR/conteudo.md`, sem encadeamento intermediário.
- README e `SKILL.md` repetem somente os números e nomes estáveis.
- Os padrões devem permanecer numerados exatamente de 1 a 6.
- Nenhuma palavra ou expressão isolada comprova um padrão.
- Cada padrão precisa de problema, sinais candidatos, confirmação contextual, falsos positivos, antes, depois e preservação factual.
- Nenhum exemplo pode fabricar ou omitir fatos protegidos.
- A #4 não é pré-condição; o roteamento deve coexistir com ou sem calibração de voz.
- Não modificar manifesto, `agents/openai.yaml`, versão ou outros grupos do catálogo.
- Não deixar marcadores incompletos nem metadados específicos do Claude.

## File Structure

| Arquivo | Responsabilidade |
| --- | --- |
| `skills/refinar-prosa/references/pt-BR/conteudo.md` | Fonte canônica dos padrões 1–6. |
| `skills/refinar-prosa/SKILL.md` | Triagem, nomes estáveis e ligação direta. |
| `README.md` | Resumo público sincronizado dos nomes. |

---

### Task 1: Criar a referência canônica dos padrões 1–6

**Files:**
- Create: `skills/refinar-prosa/references/pt-BR/conteudo.md`
- Test: `skills/refinar-prosa/references/pt-BR/conteudo.md`

**Interfaces:**
- Consumes: contrato editorial implementado pela #3 e candidatos contextuais identificados pelo `SKILL.md`.
- Produces: seis padrões completos, numerados e auditáveis, aplicados em conjunto quando a referência for carregada.

- [ ] **Step 1: Verificar a pré-condição da #3**

Run:

```bash
python3 -c 'from pathlib import Path; s=Path("skills/refinar-prosa/SKILL.md").read_text(); required=["## Contrato editorial", "## Seleção do modo", "## Ciclo interno", "Fonte → rascunho", "Rascunho → fonte"]; missing=[x for x in required if x not in s]; print("\n".join(missing)); raise SystemExit(bool(missing))'
```

Expected: exit code `0` e nenhuma saída. Se falhar, execute primeiro
`docs/superpowers/plans/2026-07-22-refinar-prosa-editorial-contract.md`.

- [ ] **Step 2: Executar a verificação negativa da referência ausente**

Run:

```bash
python3 -c 'from pathlib import Path; p=Path("skills/refinar-prosa/references/pt-BR/conteudo.md"); print("conteudo.md not found") if not p.is_file() else None; raise SystemExit(not p.is_file())'
```

Expected: exit code `1` e saída `conteudo.md not found`.

- [ ] **Step 3: Criar a referência canônica**

Use `apply_patch` para criar
`skills/refinar-prosa/references/pt-BR/conteudo.md` com este conteúdo:

````markdown
# Padrões de conteúdo 1–6

Use estes padrões somente depois de confirmar o contrato editorial do
`refinar-prosa`. Nenhuma palavra ou expressão isolada comprova um padrão.

Para cada candidato:

1. identifique sua função no contexto;
2. verifique suporte factual ou atribuição;
3. determine se acrescenta informação ou apenas aparência de importância;
4. faça a menor edição que resolva o padrão;
5. preserve o trecho em caso de dúvida.

## 1 — Inflação de importância e legado

### Problema

Transforma um acontecimento comum em marco histórico, legado ou mudança
fundamental sem evidência para essa avaliação.

### Sinais candidatos

- “desempenha um papel fundamental” sem explicar o papel;
- “marca um momento crucial” sem consequência demonstrada;
- “representa um divisor de águas” sem comparação anterior e posterior;
- “deixa um legado duradouro” sem efeito identificado.

### Confirmação contextual

Aplique somente quando a importância for uma avaliação genérica, sem dados,
fonte, atribuição ou consequência concreta, e o acontecimento permanecer
completo sem ela.

### Não alterar quando

- impacto histórico for o objeto do texto;
- dados, comparação temporal ou fonte sustentarem o impacto;
- a avaliação estiver atribuída;
- “fundamental” descrever dependência técnica real.

### Antes

```text
A biblioteca passou a abrir aos sábados, um marco fundamental em sua trajetória.
```

### Depois

```text
A biblioteca passou a abrir aos sábados.
```

### Preservação factual

Permanece o fato de que a biblioteca passou a abrir aos sábados. Sai apenas a
avaliação não sustentada de marco fundamental; nenhuma data, causa ou efeito é
acrescentado.

## 2 — Notoriedade e cobertura sem contexto

### Problema

Usa enumeração de veículos ou aparições para insinuar ampla relevância sem
explicar a relação da cobertura com o assunto.

### Sinais candidatos

- “ganhou ampla notoriedade” seguido de canais;
- “recebeu extensa cobertura” sem medida ou consequência;
- lista de jornais, podcasts ou eventos como prova automática de importância;
- aparições sem contexto de data, alcance ou recepção.

### Confirmação contextual

Aplique quando a cobertura for factual, mas a conclusão sobre notoriedade,
prestígio ou impacto não tiver apoio. Preserve as menções concretas.

### Não alterar quando

- recepção pública ou história da cobertura forem o tema;
- veículos, datas ou alcance verificarem uma afirmação;
- a cobertura tiver consequência documentada;
- a enumeração estiver em seção bibliográfica ou de imprensa apropriada.

### Antes

```text
A iniciativa ganhou ampla notoriedade e foi mencionada por jornais locais e
podcasts da região.
```

### Depois

```text
Jornais locais e podcasts da região mencionaram a iniciativa.
```

### Preservação factual

Permanecem as menções e os dois tipos de veículo. Sai somente a conclusão não
quantificada de ampla notoriedade; não são inventados alcance, datas ou efeitos.

## 3 — Análise superficial acoplada

### Problema

Anexa ao fato uma interpretação genérica, muitas vezes por gerúndio, que atribui
virtude, significado ou intenção sem evidência.

### Sinais candidatos

- “evidenciando” seguido de qualidade abstrata;
- “demonstrando compromisso” sem ação adicional;
- “reforçando a importância” sem argumento;
- “destacando seu papel” como comentário automático.

### Confirmação contextual

Aplique quando a oração não descrever consequência verificável, ação simultânea
ou conteúdo explícito, e apenas converter o fato anterior em julgamento.

### Não alterar quando

- o gerúndio expressar resultado concreto, como interrupção por duas horas;
- houver relação temporal, causal ou operacional necessária;
- a análise estiver atribuída;
- retirar a oração eliminar informação verificável.

### Antes

```text
O conselho publicou as atas no portal, demonstrando compromisso com a
transparência.
```

### Depois

```text
O conselho publicou as atas no portal.
```

### Preservação factual

Permanecem agente, ação, objeto e local. Sai a interpretação não sustentada
sobre compromisso; não se inventa efeito da publicação.

## 4 — Promoção indevida

### Problema

Substitui descrição por publicidade, com superlativos, adjetivos absolutos ou
promessas que não são necessárias ao gênero nem sustentadas.

### Sinais candidatos

- “revolucionário”, “incomparável” ou “imperdível” sem comparação;
- “experiência única” sem característica identificada;
- promessa de resultado sem dado ou condição;
- adjetivos promocionais em texto informativo.

### Confirmação contextual

Aplique quando a linguagem não for citação, requisito de voz de marca nem
alegação apoiada, e puder ser substituída pelas capacidades fornecidas.

### Não alterar quando

- o usuário pedir texto publicitário e fornecer as alegações;
- a expressão fizer parte de slogan ou citação;
- uma comparação tiver métrica e referência;
- o tom promocional for objeto de análise.

### Antes

```text
O aplicativo oferece uma experiência revolucionária e incomparável, com busca
por título e filtro por autor.
```

### Depois

```text
O aplicativo permite buscar por título e filtrar por autor.
```

### Preservação factual

Permanecem busca por título e filtro por autor. Saem adjetivos sem apoio; não são
acrescentadas velocidade, precisão ou comparação com concorrentes.

## 5 — Atribuição vaga e evasiva

### Problema

Apresenta afirmação apoiada em fonte indefinida ou quantificador vago,
dificultando avaliar autoria, alcance e certeza.

### Sinais candidatos

- “especialistas afirmam” sem identificação disponível;
- “alguns dizem”, “muitos consideram” ou “é amplamente reconhecido”;
- voz passiva que apaga agente relevante;
- categoria vaga no lugar de fonte específica.

### Confirmação contextual

Aplique quando a fonte não puder ser identificada no texto ou contexto e a
vagueza esconder limitação relevante. Nunca transforme atribuição vaga em
afirmação direta.

### Não alterar quando

- anonimato proteger pessoas ou fontes;
- a atribuição resumir consenso documentado;
- identidade for irrelevante e o quantificador, preciso;
- o gênero exigir confidencialidade;
- a fonte aparecer em trecho próximo.

### Antes

```text
Segundo especialistas, o novo horário reduziu a espera.
```

### Depois

```text
Segundo especialistas não identificados no texto, o novo horário reduziu a
espera.
```

### Preservação factual

Permanecem a atribuição e a afirmação sobre redução da espera. A revisão torna
explícita a ausência observável de identificação; não inventa nomes, dados,
período ou intensidade.

## 6 — Desafios e futuro formulaicos

### Problema

Cria seções de desafios, perspectivas ou futuro preenchidas por frases
genéricas, mesmo quando há apenas um próximo passo concreto.

### Sinais candidatos

- título “Desafios e perspectivas futuras” sem desafios nomeados;
- “em meio aos desafios” sem obstáculo específico;
- “abre caminho para novas possibilidades” sem ação;
- “o futuro parece promissor” sem previsão sustentada.

### Confirmação contextual

Aplique quando a seção misturar preenchimento abstrato com poucos fatos. Mantenha
riscos, decisões, datas, responsáveis e próximos passos.

### Não alterar quando

- desafios, riscos ou cenários forem específicos;
- perspectivas tiverem fonte, plano ou projeção;
- a seção organizar ações futuras reais;
- o gênero exigir análise de riscos.

### Antes

```text
Apesar dos desafios, o projeto segue avançando e abre caminho para novas
possibilidades. O próximo encontro será em 12 de outubro para definir o
cronograma.
```

### Depois

```text
O próximo encontro será em 12 de outubro para definir o cronograma.
```

### Preservação factual

Permanecem data e finalidade do encontro. Saem referências não especificadas a
desafios, avanço e possibilidades; não são inventados participantes ou prazos.
````

- [ ] **Step 4: Validar estrutura, exemplos e inventários**

Run:

```bash
python3 -c 'from pathlib import Path; import re; s=Path("skills/refinar-prosa/references/pt-BR/conteudo.md").read_text(); nums=re.findall(r"^## ([1-6]) — ", s, re.M); fields=["### Problema", "### Sinais candidatos", "### Confirmação contextual", "### Não alterar quando", "### Antes", "### Depois", "### Preservação factual"]; assert nums==list("123456"), nums; assert all(s.count(x)==6 for x in fields), {x:s.count(x) for x in fields}; assert "Nenhuma palavra ou expressão isolada comprova um padrão" in s; print("content patterns valid")'
```

Expected: exit code `0` e saída `content patterns valid`.

- [ ] **Step 5: Executar a auditoria estática dos exemplos**

Run:

```bash
python3 -c 'from pathlib import Path; s=Path("skills/refinar-prosa/references/pt-BR/conteudo.md").read_text(); required=["biblioteca passou a abrir aos sábados", "Jornais locais e podcasts", "conselho publicou as atas", "buscar por título e filtrar por autor", "especialistas não identificados no texto", "12 de outubro para definir o cronograma"]; missing=[x for x in required if x not in s]; print("\n".join(missing)); raise SystemExit(bool(missing))'
```

Expected: exit code `0` e nenhuma saída. Depois, compare manualmente cada par
“Antes/Depois” com sua seção “Preservação factual”; nenhuma seção pode depender
de fato ausente no “Antes”.

- [ ] **Step 6: Commitar a referência canônica**

```bash
git add skills/refinar-prosa/references/pt-BR/conteudo.md
git commit -m "feat: add content patterns 1-6"
```

Expected: commit criado contendo somente `references/pt-BR/conteudo.md`.

---

### Task 2: Ligar a referência e sincronizar o README

**Files:**
- Modify: `skills/refinar-prosa/SKILL.md`
- Modify: `README.md`
- Test: `skills/refinar-prosa/SKILL.md`, `skills/refinar-prosa/references/pt-BR/conteudo.md`, `README.md`

**Interfaces:**
- Consumes: os seis títulos estáveis da referência criada na Task 1.
- Produces: roteamento contextual na skill e resumo público com sequência idêntica.

- [ ] **Step 1: Executar a verificação negativa de sincronização**

Run:

```bash
python3 -c 'from pathlib import Path; names=["Inflação de importância e legado", "Notoriedade e cobertura sem contexto", "Análise superficial acoplada", "Promoção indevida", "Atribuição vaga e evasiva", "Desafios e futuro formulaicos"]; texts=[Path("skills/refinar-prosa/SKILL.md").read_text(), Path("README.md").read_text()]; missing=[f"{i}. {name}" for text in texts for i,name in enumerate(names,1) if f"{i}. {name}" not in text]; print("\n".join(missing)); raise SystemExit(bool(missing))'
```

Expected: exit code `1`; a saída lista os nomes ausentes do `SKILL.md` e do
README.

- [ ] **Step 2: Adicionar o mapa e a ligação direta ao SKILL.md**

Use `apply_patch` com este patch:

```diff
*** Begin Patch
*** Update File: skills/refinar-prosa/SKILL.md
@@
-## Conteúdo protegido em arquivos
+## Catálogo editorial
+
+Faça uma triagem contextual por estas famílias:
+
+1. Inflação de importância e legado.
+2. Notoriedade e cobertura sem contexto.
+3. Análise superficial acoplada.
+4. Promoção indevida.
+5. Atribuição vaga e evasiva.
+6. Desafios e futuro formulaicos.
+
+Se houver ao menos um sinal candidato, leia integralmente
+[os padrões de conteúdo 1–6](references/pt-BR/conteudo.md). Aplique somente padrões
+confirmados pela função do trecho, pelo contexto e pela ausência de suporte
+factual. Uma expressão isolada nunca basta. Preserve o original em caso de
+dúvida e audite cada edição pelo contrato factual.
+
+## Conteúdo protegido em arquivos
*** End Patch
```

- [ ] **Step 3: Adicionar o resumo sincronizado ao README**

Use `apply_patch` com este patch:

```diff
*** Begin Patch
*** Update File: README.md
@@
 | Comunicação | resíduos de chatbot, bajulação, preenchimento e hesitação |
 | Cadência | frases de efeito, dramatização, aforismos e falsas espontaneidades |

+### Padrões de conteúdo (1–6)
+
+1. Inflação de importância e legado.
+2. Notoriedade e cobertura sem contexto.
+3. Análise superficial acoplada.
+4. Promoção indevida.
+5. Atribuição vaga e evasiva.
+6. Desafios e futuro formulaicos.
+
+Os detalhes, limites e exemplos ficam na
+[referência canônica](skills/refinar-prosa/references/pt-BR/conteudo.md).
+
 Os padrões não serão uma tradução mecânica de regras inglesas. A
*** End Patch
```

- [ ] **Step 4: Validar sequência e nomes nos três arquivos**

Run:

```bash
python3 -c 'from pathlib import Path; import re; names=["Inflação de importância e legado", "Notoriedade e cobertura sem contexto", "Análise superficial acoplada", "Promoção indevida", "Atribuição vaga e evasiva", "Desafios e futuro formulaicos"]; ref=Path("skills/refinar-prosa/references/pt-BR/conteudo.md").read_text(); skill=Path("skills/refinar-prosa/SKILL.md").read_text(); readme=Path("README.md").read_text(); assert [n for _,n in re.findall(r"^## ([1-6]) — (.+)$",ref,re.M)]==names; assert all(f"{i}. {n}." in skill for i,n in enumerate(names,1)); assert all(f"{i}. {n}." in readme for i,n in enumerate(names,1)); assert "(references/pt-BR/conteudo.md)" in skill; print("catalog synchronization valid")'
```

Expected: exit code `0` e saída `catalog synchronization valid`.

- [ ] **Step 5: Confirmar que exemplos não foram duplicados**

Run:

```bash
rg -n '^### Antes$|^### Depois$|^### Preservação factual$' skills/refinar-prosa/SKILL.md README.md
```

Expected: exit code `1` e nenhuma saída.

- [ ] **Step 6: Validar a skill e o pacote**

Run:

```bash
python3 /home/thiago-botelho/.config/orca/codex-accounts/9ae230c7-073c-4dc6-85bc-436aca338b5d/home/skills/.system/skill-creator/scripts/quick_validate.py skills/refinar-prosa
```

Expected: `Skill is valid!`.

Run:

```bash
python3 /home/thiago-botelho/.config/orca/codex-accounts/9ae230c7-073c-4dc6-85bc-436aca338b5d/home/skills/.system/plugin-creator/scripts/validate_plugin.py .
```

Expected: `Plugin validation passed:` seguido da raiz do repositório.

- [ ] **Step 7: Verificar escopo e higiene**

Run:

```bash
git diff --name-only HEAD
```

Expected exatamente, em qualquer ordem:

```text
README.md
skills/refinar-prosa/SKILL.md
```

Run:

```bash
rg -n 'TBD|\[TODO:|Claude' skills/refinar-prosa/SKILL.md skills/refinar-prosa/references/pt-BR/conteudo.md README.md
```

Expected: exit code `1` e nenhuma saída.

Run:

```bash
git diff --check
```

Expected: exit code `0` e nenhuma saída.

- [ ] **Step 8: Revisar e commitar roteamento e resumo**

Run:

```bash
git diff -- skills/refinar-prosa/SKILL.md README.md
```

Expected: somente o mapa com ligação direta e o resumo público, ambos com os
mesmos seis números e nomes.

Commit:

```bash
git add skills/refinar-prosa/SKILL.md README.md
git commit -m "docs: route content pattern catalog"
```

- [ ] **Step 9: Confirmar o estado final**

Run:

```bash
git status --short --branch
```

Expected: árvore limpa e `main` à frente de `origin/main` pelos commits de
especificação, plano e implementação.
