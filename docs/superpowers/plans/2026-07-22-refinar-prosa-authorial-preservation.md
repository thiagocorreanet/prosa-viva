# Refinar Prosa Authorial Preservation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Impedir reescritas agressivas por sinal isolado, preservar marcas autorais e criar fixtures iniciais de sobre-edição baseadas em invariantes.

**Architecture:** O `SKILL.md` receberá invariantes sempre visíveis e ligação obrigatória para `references/preservacao-autoral.md` antes do catálogo. Fixtures JSON separarão entradas, restrições e expectativas, preparando a expansão pela #15 sem impor uma única saída textual.

**Tech Stack:** Markdown, JSON, Python 3, `rg`, validador de Agent Skills e validador de plugins Codex.

## Global Constraints

- A implementação da #3 é pré-condição obrigatória.
- Criar `skills/refinar-prosa/references/preservacao-autoral.md` e `evals/fixtures/sobre-edicao/{inputs,constraints,expectations}.json`.
- Modificar somente `skills/refinar-prosa/SKILL.md` além dos arquivos criados.
- Nenhum sinal isolado autoriza reescrita agressiva.
- Citações, títulos, código, exemplos e metalinguagem não participam da detecção como voz do autor.
- Preservar detalhes incomuns, ambivalência, referências situadas, escolhas defensáveis, variação natural, apartes, autocorreções e regionalismos.
- Auditar perda de voz além de fabricação e omissão.
- Fixtures devem separar entrada, restrições e expectativas e não exigir saída exata.
- Não implementar o runner completo da #15.
- Não modificar manifesto, versão, agentes, README ou catálogo numerado.
- Não deixar marcadores incompletos nem metadados específicos do Claude.

---

### Task 1: Criar a referência e ativar as proteções no `SKILL.md`

**Files:**
- Create: `skills/refinar-prosa/references/preservacao-autoral.md`
- Modify: `skills/refinar-prosa/SKILL.md`
- Test: `skills/refinar-prosa/SKILL.md`

**Interfaces:**
- Consumes: contrato editorial e ciclo da #3.
- Produces: guardrails obrigatórios antes do catálogo 1–33 e auditoria de perda de voz.

- [ ] **Step 1: Verificar a pré-condição e executar teste negativo**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
s = Path("skills/refinar-prosa/SKILL.md").read_text()
for item in ["## Contrato editorial", "## Ciclo interno"]:
    assert item in s, item
for item in ["## Conjunto de sinais", "## Falsos positivos", "## Sinais autorais a preservar", "## Auditoria de perda de voz", "references/preservacao-autoral.md"]:
    assert item not in s, item
print("authorial protection missing as expected")
PY
```

Expected: exit code `0` e saída `authorial protection missing as expected`.

- [ ] **Step 2: Criar `references/preservacao-autoral.md`**

Use `apply_patch` com este conteúdo:

```markdown
# Preservação autoral e falsos positivos

Leia esta referência antes de aplicar qualquer padrão do catálogo 1–33.

## Regra de conjunto

Nenhuma palavra, pontuação, estrutura ou ausência isolada autoriza reescrita
agressiva. Confirme vários indícios coerentes no contexto, sua função, o gênero
e a voz. Na dúvida, preserve.

## Não considerar isoladamente

- gramática correta e estilo consistente;
- mistura de registros;
- vocabulário formal, técnico ou acadêmico;
- transições comuns;
- aspas curvas ou travessões;
- uma frase curta de ênfase;
- ausência de citações;
- formatação complexa;
- termos dentro de citações, títulos, código ou exemplos.

Trechos protegidos e usos metalinguísticos não são evidência da voz do autor. A
ausência de citações não autoriza acrescentar fontes.

## Preservar

- detalhe específico e incomum presente na fonte;
- sentimentos mistos, ambivalência e tensão não resolvida;
- referência cultural situada;
- escolha editorial defensável;
- variação natural de extensão;
- aparte, autocorreção, hesitação significativa e regionalismo.

Esses sinais só são normalizados por instrução do usuário ou quando um problema
claro puder ser corrigido sem apagar sua função.

## Procedimento

1. Marque conteúdo factual e estrutural protegido.
2. Identifique gênero, público, formalidade e amostra de voz.
3. Separe sinal isolado de conjunto coerente.
4. Exclua citações, títulos, código, exemplos e metalinguagem da detecção.
5. Identifique marcas autorais que a uniformização apagaria.
6. Faça a menor edição útil ou não altere.
7. Audite fabricação, omissão e perda de voz.

## Auditoria de perda de voz

Verifique se detalhes ficaram genéricos, ambivalência virou certeza ou otimismo,
referência cultural foi neutralizada, cadência ficou uniforme, aparte,
autocorreção ou regionalismo desapareceu, ou um sinal isolado provocou mudanças
ao redor. Se isso ocorrer sem pedido explícito, recue até a menor edição segura.
```

- [ ] **Step 3: Adicionar seções obrigatórias ao `SKILL.md`**

Use `apply_patch` para inserir antes do roteamento do catálogo:

```markdown
## Conjunto de sinais

Nenhuma palavra, pontuação, estrutura ou ausência isolada autoriza reescrita
agressiva. Confirme um conjunto coerente no contexto e faça a menor edição útil.
Na dúvida, preserve. Antes de aplicar o catálogo, leia
[`references/preservacao-autoral.md`](references/preservacao-autoral.md).

## Falsos positivos

Não trate isoladamente como problema: gramática correta, estilo consistente,
mistura de registros, vocabulário formal, transições comuns, aspas curvas,
travessões, uma frase curta, ausência de citações ou formatação complexa. Ignore
para detecção termos dentro de citações, títulos, código e exemplos.

## Sinais autorais a preservar

Preserve detalhes específicos, sentimentos mistos, tensão não resolvida,
referências culturais situadas, escolhas editoriais defensáveis, variação
natural de extensão, apartes, autocorreções e regionalismos.
```

E acrescentar à auditoria existente:

```markdown
## Auditoria de perda de voz

Compare fonte e versão final. Reverta mudanças que tornem detalhes genéricos,
resolvam ambivalência, neutralizem referências culturais, uniformizem a
cadência ou apaguem apartes, autocorreções e regionalismos sem pedido explícito.
```

- [ ] **Step 4: Validar cobertura e ligação direta**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
s = Path("skills/refinar-prosa/SKILL.md").read_text()
r = Path("skills/refinar-prosa/references/preservacao-autoral.md").read_text()
for heading in ["## Conjunto de sinais", "## Falsos positivos", "## Sinais autorais a preservar", "## Auditoria de perda de voz"]:
    assert heading in s, heading
assert "[references/preservacao-autoral.md](references/preservacao-autoral.md)" in s
for item in ["mistura de registros", "ausência de citações", "citações, títulos, código", "sentimentos mistos", "referências culturais", "autocorreções", "regionalismos"]:
    assert item in s + r, item
print("authorial guardrails: ok")
PY
```

Expected: exit code `0` e saída `authorial guardrails: ok`.

- [ ] **Step 5: Commitar guardrails**

```bash
git add skills/refinar-prosa/SKILL.md skills/refinar-prosa/references/preservacao-autoral.md
git commit -m "feat: protect authorial signals"
```

### Task 2: Criar fixtures separadas de sobre-edição

**Files:**
- Create: `evals/fixtures/sobre-edicao/inputs.json`
- Create: `evals/fixtures/sobre-edicao/constraints.json`
- Create: `evals/fixtures/sobre-edicao/expectations.json`
- Test: `evals/fixtures/sobre-edicao/*.json`

**Interfaces:**
- Consumes: categorias da Task 1.
- Produces: dez casos alinhados por `id`, prontos para o runner da #15.

- [ ] **Step 1: Criar entradas**

Use `apply_patch` para criar `inputs.json`:

```json
{
  "schema_version": 1,
  "cases": [
    {"id":"single-em-dash","mode":"pasted","genre":"essay","input":"A decisão — ainda desconfortável — ficou para segunda-feira."},
    {"id":"curly-quotes","mode":"pasted","genre":"general","input":"Ela chamou o acordo de “provisório” e manteve essa palavra na ata."},
    {"id":"formal-legal","mode":"pasted","genre":"legal","input":"A parte requerente deverá comprovar a tempestividade do recurso."},
    {"id":"mixed-register","mode":"pasted","genre":"internal-message","input":"A implantação foi concluída; agora falta conferir se ficou tudo redondo."},
    {"id":"single-short-sentence","mode":"embedded","genre":"pr-description","input":"A migração preserva os dados existentes. Sem exceções."},
    {"id":"complex-markdown","mode":"file","genre":"documentation","input":"---\ntitle: Guia\n---\n\n| Campo | Valor |\n| --- | --- |\n| `ttl` | 300 |\n\nVeja [a API](https://example.com/api)."},
    {"id":"quoted-metalanguage","mode":"pasted","genre":"analysis","input":"Neste exemplo, “papel fundamental” é a expressão analisada; não uma avaliação do projeto."},
    {"id":"unusual-detail","mode":"pasted","genre":"personal-essay","input":"Guardei o bilhete azul no terceiro volume da enciclopédia, entre as páginas 214 e 215."},
    {"id":"mixed-feelings","mode":"pasted","genre":"personal-essay","input":"Fiquei aliviada com a mudança e, ao mesmo tempo, senti falta da rotina antiga. Ainda não sei o que prevalece."},
    {"id":"situated-regionalism","mode":"pasted","genre":"personal-essay","input":"No fim da tarde, parei no mercadinho da esquina — quer dizer, no que restou dele — e pedi um cafezinho. Trem esquisito, sô."}
  ]
}
```

- [ ] **Step 2: Criar restrições verificáveis**

Use `apply_patch` para criar `constraints.json`:

```json
{
  "schema_version": 1,
  "cases": [
    {"id":"single-em-dash","preserve_exact":["segunda-feira","desconfortável"],"protected_structures":[],"max_change_ratio":0.10},
    {"id":"curly-quotes","preserve_exact":["“provisório”","ata"],"protected_structures":["curly_quotes"],"max_change_ratio":0.05},
    {"id":"formal-legal","preserve_exact":["parte requerente","tempestividade do recurso"],"protected_structures":[],"max_change_ratio":0.05},
    {"id":"mixed-register","preserve_exact":["implantação foi concluída","ficou tudo redondo"],"protected_structures":[],"max_change_ratio":0.10},
    {"id":"single-short-sentence","preserve_exact":["dados existentes","Sem exceções."],"protected_structures":[],"max_change_ratio":0.05},
    {"id":"complex-markdown","preserve_exact":["title: Guia","`ttl`","300","https://example.com/api"],"protected_structures":["frontmatter","table","inline_code","link_destination"],"max_change_ratio":0.05},
    {"id":"quoted-metalanguage","preserve_exact":["“papel fundamental”","expressão analisada"],"protected_structures":["quotation","metalinguistic_example"],"max_change_ratio":0.05},
    {"id":"unusual-detail","preserve_exact":["bilhete azul","terceiro volume","214","215"],"protected_structures":[],"max_change_ratio":0.05},
    {"id":"mixed-feelings","preserve_exact":["aliviada","senti falta","Ainda não sei"],"protected_structures":[],"max_change_ratio":0.10},
    {"id":"situated-regionalism","preserve_exact":["mercadinho da esquina","quer dizer","cafezinho","Trem esquisito, sô."],"protected_structures":[],"max_change_ratio":0.10}
  ]
}
```

- [ ] **Step 3: Criar expectativas comportamentais**

Use `apply_patch` para criar `expectations.json`:

```json
{
  "schema_version": 1,
  "cases": [
    {"id":"single-em-dash","expected_change":"none_or_minimal","reason":"Um travessão isolado não confirma padrão."},
    {"id":"curly-quotes","expected_change":"none","reason":"Aspas curvas consistentes são escolha tipográfica válida."},
    {"id":"formal-legal","expected_change":"none_or_minimal","reason":"Vocabulário formal é adequado ao gênero jurídico."},
    {"id":"mixed-register","expected_change":"none_or_minimal","reason":"A mistura de registro cumpre função em mensagem interna."},
    {"id":"single-short-sentence","expected_change":"none","reason":"Uma frase curta isolada pode ser ênfase legítima."},
    {"id":"complex-markdown","expected_change":"none","reason":"Estruturas e dados Markdown estão protegidos."},
    {"id":"quoted-metalanguage","expected_change":"none","reason":"A expressão aparece em citação metalinguística."},
    {"id":"unusual-detail","expected_change":"none_or_minimal","reason":"Detalhes específicos e incomuns preservam voz e fatos."},
    {"id":"mixed-feelings","expected_change":"none_or_minimal","reason":"Ambivalência e tensão não resolvida não devem ser limpas."},
    {"id":"situated-regionalism","expected_change":"none_or_minimal","reason":"Referência situada, aparte, autocorreção e regionalismo são autorais."}
  ]
}
```

- [ ] **Step 4: Validar JSON, IDs e separação**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
import json

root = Path("evals/fixtures/sobre-edicao")
docs = {p.stem: json.loads(p.read_text()) for p in root.glob("*.json")}
assert set(docs) == {"inputs", "constraints", "expectations"}
ids = {name: [c["id"] for c in doc["cases"]] for name, doc in docs.items()}
assert len(set(map(tuple, ids.values()))) == 1, ids
assert len(ids["inputs"]) == 10
assert all(c["expected_change"] in {"none", "none_or_minimal"} for c in docs["expectations"]["cases"])
assert all(0 <= c["max_change_ratio"] <= 0.10 for c in docs["constraints"]["cases"])
assert all("input" not in c for c in docs["constraints"]["cases"])
assert all("preserve_exact" not in c for c in docs["expectations"]["cases"])
print("over-editing fixtures: ok")
PY
```

Expected: exit code `0` e saída `over-editing fixtures: ok`.

- [ ] **Step 5: Commitar fixtures**

```bash
git add evals/fixtures/sobre-edicao
git commit -m "test: add over-editing fixtures"
```

### Task 3: Executar auditoria integrada

**Files:**
- Test: `skills/refinar-prosa/SKILL.md`
- Test: `skills/refinar-prosa/references/preservacao-autoral.md`
- Test: `evals/fixtures/sobre-edicao/*.json`
- Test: `.codex-plugin/plugin.json`

**Interfaces:**
- Consumes: guardrails e fixtures das Tasks 1–2.
- Produces: evidência de cobertura e validade estrutural.

- [ ] **Step 1: Executar validações da skill e do plugin**

Run:

```bash
python3 /home/thiago-botelho/.config/orca/codex-accounts/9ae230c7-073c-4dc6-85bc-436aca338b5d/home/skills/.system/skill-creator/scripts/quick_validate.py skills/refinar-prosa
```

Expected: exit code `0` e mensagem de skill válida. Depois, execute o validador
de plugins Codex identificado na #2; expected: exit code `0`.

- [ ] **Step 2: Verificar higiene e diff**

Run:

```bash
rg -n -i 'claude|\.claude-plugin|marketplace\.json|placeholder|\[preencher\]' .codex-plugin skills evals
git diff --check
git status --short
```

Expected: `rg` com exit code `1`, `git diff --check` sem saída e nenhum arquivo
inesperado no status.

- [ ] **Step 3: Commitar eventual correção estritamente necessária**

Se a validação exigir correção apenas nos arquivos em escopo:

```bash
git add skills/refinar-prosa/SKILL.md skills/refinar-prosa/references/preservacao-autoral.md evals/fixtures/sobre-edicao
git commit -m "fix: validate authorial preservation"
```

Caso não haja correção, não criar commit vazio.
