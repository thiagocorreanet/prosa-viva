# Refinar Prosa Language Scope Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Tornar pt-BR o único idioma suportado nas versões 0.1.x, definir comportamento conservador por modo e criar fixtures rastreáveis da política linguística.

**Architecture:** A política comportamental ficará no `SKILL.md`; manifesto, agente e README apenas a apresentarão. Fixtures JSON separarão entradas, restrições e expectativas para integração posterior na suíte #15.

**Tech Stack:** Markdown, JSON, YAML, Python 3, validadores locais de Agent Skills e plugins Codex.

## Global Constraints

- Suportar oficialmente apenas português brasileiro em `0.1.x`.
- Não aplicar fallback editorial a idiomas não suportados.
- Identificar idioma somente pela prosa editável, ignorando código, dados, URLs, frontmatter e citações.
- Em documentos mistos, editar somente segmentos claramente pt-BR.
- Texto colado ou arquivo não suportado permanece inalterado e recebe aviso breve.
- Modo embutido não suportado ou ambíguo retorna a entrada exatamente como recebida.
- Não traduzir silenciosamente.
- Futuras localidades usam `references/<locale>/` e avaliações próprias sem duplicar o núcleo.
- Não criar referências vazias, alterar versão ou adicionar componentes ao plugin.

---

### Task 1: Implementar e sincronizar a política linguística

**Files:**
- Modify: `skills/refinar-prosa/SKILL.md`
- Modify: `.codex-plugin/plugin.json`
- Modify: `README.md`
- Test: `skills/refinar-prosa/agents/openai.yaml`

**Interfaces:**
- Consumes: fonte canônica e namespace definidos pela #17.
- Produces: contrato inequívoco por modo e metadados públicos alinhados a pt-BR.

- [ ] **Step 1: Executar a verificação negativa**

```bash
python3 - <<'PY'
from pathlib import Path
s=Path('skills/refinar-prosa/SKILL.md').read_text()
r=Path('README.md').read_text()
missing=[x for x in ['## Política linguística','### Idioma não suportado','### Idioma ambíguo'] if x not in s]
missing += [x for x in ['## Idiomas suportados','modo embutido'] if x not in r]
print('\n'.join(missing))
raise SystemExit(bool(missing))
PY
```

Expected: exit code `1` e os itens ausentes.

- [ ] **Step 2: Adicionar a política ao `SKILL.md`**

Use `apply_patch` para inserir depois de `## Fonte canônica e divulgação progressiva`:

```markdown
## Política linguística

As versões `0.1.x` suportam somente prosa em português brasileiro. Identifique
o idioma pela prosa editável; ignore código, comandos, dados, URLs, frontmatter,
nomes próprios e citações protegidas. Não aplique regras pt-BR a outro idioma e
não use um fallback editorial genérico.

Em documentos mistos, revise apenas segmentos claramente em pt-BR. Preserve
integralmente prosa estrangeira, citações e trechos cuja fronteira linguística
seja incerta. Estrangeirismo técnico ou regionalismo isolado não muda o idioma
do trecho.

### Idioma não suportado

- Texto colado: não reescreva; informe brevemente que esta versão suporta
  somente pt-BR.
- Arquivo: não escreva no arquivo; informe que nenhuma alteração foi realizada.
- Embutido: retorne a entrada exatamente como recebida, sem comentário.

### Idioma ambíguo

- Texto colado: preserve e peça identificação do idioma ou mais contexto.
- Arquivo: não escreva; informe que não foi possível identificar o idioma com
  segurança.
- Embutido: retorne a entrada exatamente como recebida, sem comentário.

Não traduza silenciosamente. Se o pedido combinar tradução e refinamento,
informe no modo conversacional que a tradução precisa ocorrer antes; no modo
embutido, preserve a entrada.
```

- [ ] **Step 3: Restringir as palavras-chave do manifesto**

Use `apply_patch` para substituir:

```json
  "keywords": [
    "escrita",
    "revisão",
    "português",
    "pt-BR",
    "prosa"
  ],
```

por:

```json
  "keywords": [
    "escrita",
    "revisão",
    "pt-BR",
    "prosa"
  ],
```

- [ ] **Step 4: Documentar os idiomas no README**

Use `apply_patch` para inserir depois de `## Arquitetura da skill`:

```markdown
## Idiomas suportados

A série `0.1.x` suporta oficialmente apenas português brasileiro. Textos em
outro idioma não recebem uma revisão parcial ou genérica.

- Em texto colado, a entrada é preservada e o limite é informado brevemente.
- Em arquivo, nenhuma escrita é realizada.
- No modo embutido, a entrada é devolvida exatamente como recebida.
- Em documentos mistos, somente segmentos claramente pt-BR são revisados;
  citações, código e prosa estrangeira permanecem intactos.

Se o idioma for ambíguo, os modos conversacionais pedem contexto sem editar; o
modo embutido preserva a entrada. Tradução não faz parte de `$refinar-prosa`.

Uma futura localidade terá referências, pesquisa, exemplos e avaliações próprias
em `references/<locale>/`; contrato editorial e proteção factual continuarão no
núcleo comum.
```

- [ ] **Step 5: Validar sincronização e commit**

```bash
python3 - <<'PY'
from pathlib import Path
import json, yaml
s=Path('skills/refinar-prosa/SKILL.md').read_text()
r=Path('README.md').read_text()
m=json.loads(Path('.codex-plugin/plugin.json').read_text())
a=yaml.safe_load(Path('skills/refinar-prosa/agents/openai.yaml').read_text())
for x in ['## Política linguística','### Idioma não suportado','### Idioma ambíguo','Não traduza silenciosamente']:
    assert x in s, x
for x in ['## Idiomas suportados','modo embutido','references/<locale>/']:
    assert x in r, x
assert 'pt-BR' in m['keywords'] and 'português' not in m['keywords']
assert 'pt-BR' in m['description'] or 'português brasileiro' in m['description']
assert 'pt-BR' in a['interface']['short_description']
print('language policy metadata: ok')
PY
git add skills/refinar-prosa/SKILL.md .codex-plugin/plugin.json README.md
git commit -m "feat: define pt-BR language policy"
```

### Task 2: Criar fixtures da política linguística

**Files:**
- Create: `evals/fixtures/politica-linguistica/inputs.json`
- Create: `evals/fixtures/politica-linguistica/constraints.json`
- Create: `evals/fixtures/politica-linguistica/expectations.json`

**Interfaces:**
- Consumes: comportamento por modo da Task 1.
- Produces: sete casos alinhados por `id`, sem saída textual única.

- [ ] **Step 1: Confirmar ausência e criar `inputs.json`**

Expected antes da criação: `test ! -e evals/fixtures/politica-linguistica/inputs.json` retorna `0`.

```json
{
  "schema_version": 1,
  "cases": [
    {"id":"ptbr-general","mode":"pasted","genre":"general","input":"A reunião acontece na terça-feira e começa às 9h."},
    {"id":"ptbr-regional-technical","mode":"pasted","genre":"internal","input":"O deploy ficou redondo, mas esse trem ainda exige um token."},
    {"id":"mixed-document","mode":"file","genre":"documentation","input":"A API retorna 200.\n\n> This sentence is quoted.\n\n```js\nreturn 'ok'\n```"},
    {"id":"english-pasted","mode":"pasted","genre":"general","input":"The meeting starts at nine on Tuesday."},
    {"id":"spanish-file","mode":"file","genre":"documentation","input":"La reunión comienza a las nueve del martes."},
    {"id":"ambiguous-embedded","mode":"embedded","genre":"pr-description","input":"Status API OK."},
    {"id":"translation-request","mode":"pasted","genre":"general","input":"Translate and refine: The meeting starts at nine."}
  ]
}
```

- [ ] **Step 2: Criar `constraints.json`**

```json
{
  "schema_version": 1,
  "cases": [
    {"id":"ptbr-general","preserve_exact":["terça-feira","9h"],"must_not_write":false,"exact_output":false},
    {"id":"ptbr-regional-technical","preserve_exact":["redondo","esse trem","token"],"must_not_write":false,"exact_output":false},
    {"id":"mixed-document","preserve_exact":["> This sentence is quoted.","```js\nreturn 'ok'\n```"],"must_not_write":false,"exact_output":false},
    {"id":"english-pasted","preserve_exact":["The meeting starts at nine on Tuesday."],"must_not_write":false,"exact_output":false},
    {"id":"spanish-file","preserve_exact":["La reunión comienza a las nueve del martes."],"must_not_write":true,"exact_output":true},
    {"id":"ambiguous-embedded","preserve_exact":["Status API OK."],"must_not_write":false,"exact_output":true},
    {"id":"translation-request","preserve_exact":["The meeting starts at nine."],"must_not_write":false,"exact_output":false}
  ]
}
```

- [ ] **Step 3: Criar `expectations.json`**

```json
{
  "schema_version": 1,
  "cases": [
    {"id":"ptbr-general","action":"review","output":"revised_text","reason":"Prosa claramente pt-BR."},
    {"id":"ptbr-regional-technical","action":"review_minimally","output":"revised_text","reason":"Regionalismo e termo técnico não mudam o idioma."},
    {"id":"mixed-document","action":"review_ptbr_only","output":"edited_file_summary","reason":"Citação inglesa e código são protegidos."},
    {"id":"english-pasted","action":"preserve_with_notice","output":"notice","reason":"Inglês não é suportado na v1."},
    {"id":"spanish-file","action":"do_not_write","output":"unchanged_file_summary","reason":"Arquivo fora de pt-BR."},
    {"id":"ambiguous-embedded","action":"preserve_exactly","output":"input_only","reason":"Modo embutido não acrescenta aviso."},
    {"id":"translation-request","action":"preserve_with_notice","output":"notice","reason":"Tradução está fora do escopo."}
  ]
}
```

- [ ] **Step 4: Validar e commitar fixtures**

```bash
python3 - <<'PY'
from pathlib import Path
import json
root=Path('evals/fixtures/politica-linguistica')
docs={p.stem:json.loads(p.read_text()) for p in root.glob('*.json')}
assert set(docs)=={'inputs','constraints','expectations'}
ids={k:[x['id'] for x in v['cases']] for k,v in docs.items()}
assert len(set(map(tuple,ids.values())))==1 and len(ids['inputs'])==7
assert next(x for x in docs['constraints']['cases'] if x['id']=='spanish-file')['must_not_write']
assert next(x for x in docs['expectations']['cases'] if x['id']=='ambiguous-embedded')['output']=='input_only'
print('language policy fixtures: 7/7 ok')
PY
git add evals/fixtures/politica-linguistica
git commit -m "test: add language policy fixtures"
```

### Task 3: Executar validação integrada

**Files:**
- Test: `.codex-plugin/plugin.json`
- Test: `skills/refinar-prosa/`
- Test: `README.md`
- Test: `evals/fixtures/politica-linguistica/*.json`

**Interfaces:**
- Consumes: Tasks 1–2.
- Produces: evidência de política sincronizada e pacote válido.

- [ ] **Step 1: Executar validadores**

```bash
python3 scripts/validate_skill_architecture.py
python3 /home/thiago-botelho/.config/orca/codex-accounts/9ae230c7-073c-4dc6-85bc-436aca338b5d/home/skills/.system/skill-creator/scripts/quick_validate.py skills/refinar-prosa
python3 /home/thiago-botelho/.config/orca/codex-accounts/9ae230c7-073c-4dc6-85bc-436aca338b5d/home/skills/.system/plugin-creator/scripts/validate_plugin.py .
```

Expected: os três comandos com exit code `0`.

- [ ] **Step 2: Verificar higiene e estado**

```bash
git diff --check
git status --short --branch
```

Expected: diff sem erros e árvore limpa.
