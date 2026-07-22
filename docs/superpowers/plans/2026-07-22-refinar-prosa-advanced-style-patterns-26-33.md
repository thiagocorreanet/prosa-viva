# Refinar Prosa Advanced Style Patterns 26–33 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implementar os padrões avançados de estilo e cadência 26–33 e concluir a sequência global 1–33 sem apagar escolhas autorais ou histórico técnico legítimo.

**Architecture:** `skills/refinar-prosa/references/estilo-avancado.md` será a fonte canônica do grupo. `SKILL.md` fará triagem e ligação direta, o README repetirá os nomes, e uma auditoria integrada verificará numeração 1–33, gêneros protegidos e preservação factual.

**Tech Stack:** Markdown, frontmatter YAML, Python 3, expressões regulares, `rg`, validador de Agent Skills e validador de plugins Codex.

## Global Constraints

- As implementações da #3 e da #5 são pré-condições obrigatórias.
- Criar somente `skills/refinar-prosa/references/estilo-avancado.md` e modificar somente `skills/refinar-prosa/SKILL.md` e `README.md` como arquivos do produto.
- O `SKILL.md` deve ligar diretamente `references/estilo-avancado.md`.
- Os padrões devem permanecer numerados exatamente de 26 a 33 e completar a sequência global 1–33.
- Reavaliar hifenização conforme o português; preservar marcas, nomes oficiais, identificadores, código, URLs e citações.
- Não remover recurso retórico isolado sem confirmar conjunto, recorrência, gênero e voz.
- Preservar escolhas intencionais em ensaios, publicidade criativa e ficção.
- Preservar histórico em changelogs, notas de versão, guias de migração e documentos versionados.
- Cada padrão precisa de problema, sinais candidatos, confirmação contextual, falsos positivos, antes, depois e preservação factual, autoral e de gênero.
- Não modificar manifesto, `agents/openai.yaml`, versão ou outros grupos do catálogo.
- Não deixar marcadores incompletos nem metadados específicos do Claude.

## File Structure

| Arquivo | Responsabilidade |
| --- | --- |
| `skills/refinar-prosa/references/estilo-avancado.md` | Fonte canônica dos padrões 26–33. |
| `skills/refinar-prosa/SKILL.md` | Triagem, nomes estáveis e ligação direta. |
| `README.md` | Resumo público sincronizado dos nomes. |

---

### Task 1: Criar a referência canônica dos padrões 26–33

**Files:**
- Create: `skills/refinar-prosa/references/estilo-avancado.md`
- Test: `skills/refinar-prosa/references/estilo-avancado.md`

**Interfaces:**
- Consumes: contrato editorial da #3 e estrutura de catálogo da #5.
- Produces: oito padrões auditáveis e regras de intenção e gênero.

- [ ] **Step 1: Verificar pré-condições e ausência da referência**

Run:

```bash
python3 - <<'PY'
from pathlib import Path

skill = Path("skills/refinar-prosa/SKILL.md").read_text()
required = ["## Contrato editorial", "## Seleção do modo", "references/conteudo.md"]
missing = [item for item in required if item not in skill]
assert not missing, missing
path = Path("skills/refinar-prosa/references/estilo-avancado.md")
assert not path.exists(), path
print("advanced style preconditions: ok")
PY
```

Expected: exit code `0` e saída `advanced style preconditions: ok`.

- [ ] **Step 2: Criar a referência**

Use `apply_patch` para criar
`skills/refinar-prosa/references/estilo-avancado.md` com este conteúdo:

````markdown
# Padrões avançados de estilo e cadência 26–33

Use estes padrões somente depois de confirmar o contrato editorial e o gênero.
Nenhum hífen, frase curta, pergunta, fórmula retórica ou abertura pessoal
isolada comprova um padrão. Considere conjunto, recorrência e voz do autor.

Ensaios, publicidade criativa e ficção admitem recursos retóricos deliberados.
Changelogs, notas de versão e guias de migração podem ser orientados a mudanças.

## 26 — Hifenização imprópria em português

### Problema

Mantém hífens por analogia com o inglês, segmentação visual ou regra incorreta
do português.

### Sinais candidatos

- prefixo separado de base sem respaldo na grafia portuguesa;
- composto traduzido conserva o hífen do inglês;
- a mesma palavra aparece com grafias diferentes;
- o hífen não pertence a nome oficial nem identificador.

### Confirmação contextual

Aplique somente quando a grafia em português for conhecida no contexto.

### Não alterar quando

- for marca, nome oficial, identificador, código ou URL;
- estiver em citação ou dado protegido;
- o termo de domínio tiver grafia própria;
- a forma correta não puder ser confirmada.

### Antes

```text
Cada micro-serviço registra suas próprias métricas.
```

### Depois

```text
Cada microsserviço registra suas próprias métricas.
```

### Preservação factual, autoral e de gênero

Permanece a arquitetura descrita. Só a grafia é ajustada; um identificador como
`micro-service-id` permaneceria intacto.

## 27 — Fórmulas de autoridade persuasiva

### Problema

Usa “a verdadeira questão” ou “o que realmente importa” para declarar prioridade
sem demonstrá-la.

### Sinais candidatos

- moldura de autoridade antes de um fato;
- prioridade sem comparação;
- exclusão de alternativas sem argumento;
- tom conclusivo mais forte que a evidência.

### Confirmação contextual

Aplique quando a moldura puder sair e a tese continuar completa.

### Não alterar quando

- houver contraste argumentado;
- a frase reproduzir voz ou citação;
- o gênero persuasivo tiver sido solicitado;
- a prioridade estiver sustentada por critério explícito.

### Antes

```text
A verdadeira questão é a latência: os testes registraram 480 ms no fluxo de
pagamento.
```

### Depois

```text
Os testes registraram latência de 480 ms no fluxo de pagamento.
```

### Preservação factual, autoral e de gênero

Permanecem métrica, valor e fluxo. Sai apenas a prioridade sem comparação.

## 28 — Anúncios do percurso textual

### Problema

Anuncia que o texto vai explorar, mergulhar ou percorrer um tema em vez de
começar pela informação.

### Sinais candidatos

- “vamos explorar” antes de instrução curta;
- promessa de percurso que não organiza seções;
- anúncio que repete título ou objetivo;
- convite genérico sem função no gênero.

### Confirmação contextual

Aplique quando o anúncio não orientar estrutura, escopo ou sequência extensa.

### Não alterar quando

- curso ou apresentação precisar de roteiro;
- tutorial longo anunciar etapas úteis;
- o texto delimitar escopo;
- a voz solicitada se dirigir diretamente ao público.

### Antes

```text
Neste guia, vamos explorar como configurar o cache. Primeiro, defina `ttl` como
300 segundos.
```

### Depois

```text
Para configurar o cache, defina `ttl` como 300 segundos.
```

### Preservação factual, autoral e de gênero

Permanecem objetivo, chave e valor. Sai somente o anúncio do percurso.

## 29 — Títulos seguidos de reformulação

### Problema

Repete imediatamente em prosa o conteúdo do título sem acrescentar escopo,
condição ou orientação.

### Sinais candidatos

- primeiro período parafraseia o título;
- a seção começa com “nesta seção veremos”;
- a introdução não contém pré-condição;
- remover a frase não afeta transição nem acessibilidade.

### Confirmação contextual

Aplique quando a reformulação for semanticamente vazia.

### Não alterar quando

- definir objetivo, pré-condição, risco ou contexto;
- apoiar acessibilidade ou navegação;
- introduzir distinção não contida no título;
- o modelo documental exigir resumo.

### Antes

```markdown
## Instalação

Nesta seção, veremos como realizar a instalação. Execute `npm install`.
```

### Depois

```markdown
## Instalação

Execute `npm install`.
```

### Preservação factual, autoral e de gênero

Permanecem título, comando e ordem. Sai apenas a frase que repetia o título.

## 30 — Documentação ancorada na mudança

### Problema

Descreve o estado atual como contraste permanente com uma versão anterior,
mesmo quando o leitor precisa saber como o sistema funciona agora.

### Sinais candidatos

- `agora` aparece em referência atemporal;
- comportamento vigente é definido pelo que deixou de ocorrer;
- versão anterior é citada sem efeito de compatibilidade;
- histórico obscurece a instrução atual.

### Confirmação contextual

Aplique em documentação de referência quando o contraste não for necessário à
compatibilidade, ao risco ou à compreensão.

### Não alterar quando

- for changelog, nota de versão ou guia de migração;
- o documento for versionado e o histórico importar;
- houver risco de compatibilidade;
- a comparação explicar decisão atual.

### Antes

```text
Agora, o endpoint `/pedidos` exige o cabeçalho `X-Conta`, ao contrário da versão
anterior.
```

### Depois

```text
O endpoint `/pedidos` exige o cabeçalho `X-Conta`.
```

### Preservação factual, autoral e de gênero

Permanecem endpoint, requisito e cabeçalho. Sai o contraste porque o trecho
descreve estado atual, não migração.

## 31 — Sequências curtas de dramatização artificial

### Problema

Divide uma afirmação em frases mínimas para simular tensão ou impacto sem função
autoral ou informativa.

### Sinais candidatos

- fragmentos consecutivos de uma ou duas palavras;
- pontuação cria suspense sem alterar o sentido;
- a cadência dramática destoa do documento;
- a sequência pode ser reunida sem perda.

### Confirmação contextual

Aplique quando houver recorrência formulaica incompatível com gênero e voz.

### Não alterar quando

- for uma frase curta enfática isolada;
- publicidade criativa, ensaio ou ficção pedir a cadência;
- a fragmentação representar fala ou pensamento;
- a amostra autoral confirmar o recurso.

### Antes

```text
O deploy falhou. De novo. Sem aviso.
```

### Depois

```text
O deploy voltou a falhar sem aviso.
```

### Preservação factual, autoral e de gênero

Permanecem falha, recorrência e ausência de aviso. Só a fragmentação é
condensada.

## 32 — Fórmulas aforísticas no lugar de precisão

### Problema

Usa oposição ou máxima memorável para substituir uma relação que poderia ser
declarada com precisão.

### Sinais candidatos

- “não é sobre X, é sobre Y” como fórmula pronta;
- máxima encerra discussão sem critério;
- paralelismo substitui escopo;
- frase memorável não acrescenta informação.

### Confirmação contextual

Aplique quando a fórmula contiver relação recuperável e não for escolha autoral
ou do gênero.

### Não alterar quando

- for aforismo autoral, slogan solicitado ou citação;
- ensaio, publicidade ou ficção usar o recurso deliberadamente;
- a forma condensar uma tese já argumentada;
- a cadência fizer parte da amostra.

### Antes

```text
Não é sobre velocidade. É sobre confiança.
```

### Depois

```text
A prioridade é a confiança, não a velocidade.
```

### Preservação factual, autoral e de gênero

Permanece a prioridade relativa. Não são inventadas métrica nem justificativa.

## 33 — Aberturas de falsa espontaneidade

### Problema

Começa com confissão, franqueza ou surpresa simulada que não pertence à voz do
autor nem acrescenta experiência situada.

### Sinais candidatos

- “vou ser sincero” antes de fato neutro;
- “confesso que” sem experiência real;
- surpresa genérica destacável;
- intimidade que destoa do gênero.

### Confirmação contextual

Aplique quando a abertura for fórmula removível e não informação sobre a
perspectiva do autor.

### Não alterar quando

- houver relato pessoal real;
- for autocorreção, hesitação ou regionalismo autoral;
- gênero pessoal ou criativo pedir a abertura;
- a experiência situada importar ao argumento.

### Antes

```text
Vou ser sincero: a configuração exige duas chaves obrigatórias.
```

### Depois

```text
A configuração exige duas chaves obrigatórias.
```

### Preservação factual, autoral e de gênero

Permanecem quantidade, obrigatoriedade e objeto. Sai apenas a alegação genérica
de franqueza.

## Auditoria do grupo

Antes de entregar a versão final, confirme:

- grafias técnicas e identificadores protegidos permanecem intactos;
- nenhum recurso retórico isolado motivou edição automática;
- exemplos autorais, criativos e ficcionais conservam cadência deliberada;
- changelogs, migrações e documentos versionados mantêm histórico útil;
- cada fórmula removida deu lugar à informação disponível, sem fabricação.
````

- [ ] **Step 3: Validar estrutura, nomes e gêneros protegidos**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
import re

text = Path("skills/refinar-prosa/references/estilo-avancado.md").read_text()
expected = [
    (26, "Hifenização imprópria em português"),
    (27, "Fórmulas de autoridade persuasiva"),
    (28, "Anúncios do percurso textual"),
    (29, "Títulos seguidos de reformulação"),
    (30, "Documentação ancorada na mudança"),
    (31, "Sequências curtas de dramatização artificial"),
    (32, "Fórmulas aforísticas no lugar de precisão"),
    (33, "Aberturas de falsa espontaneidade"),
]
found = [(int(n), name) for n, name in re.findall(r"^## (\d+) — (.+)$", text, re.M)]
assert found == expected, found
sections = re.split(r"^## \d+ — .+$", text, flags=re.M)[1:]
required = ["### Problema", "### Sinais candidatos", "### Confirmação contextual", "### Não alterar quando", "### Antes", "### Depois", "### Preservação factual, autoral e de gênero"]
for number, section in zip(range(26, 34), sections):
    missing = [heading for heading in required if heading not in section]
    assert not missing, (number, missing)
for item in ["publicidade criativa e ficção", "Changelogs", "identificador", "frase curta enfática isolada"]:
    assert item in text, item
print("advanced style reference: ok")
PY
```

Expected: exit code `0` e saída `advanced style reference: ok`.

- [ ] **Step 4: Commitar a referência**

```bash
git add skills/refinar-prosa/references/estilo-avancado.md
git commit -m "feat: add advanced style patterns 26-33"
```

### Task 2: Integrar roteamento e catálogo público

**Files:**
- Modify: `skills/refinar-prosa/SKILL.md`
- Modify: `README.md`
- Test: `skills/refinar-prosa/SKILL.md`
- Test: `README.md`

**Interfaces:**
- Consumes: nomes estáveis e referência da Task 1.
- Produces: triagem e resumo público sincronizados, completando 1–33.

- [ ] **Step 1: Executar a verificação negativa de roteamento**

Run:

```bash
python3 - <<'PY'
from pathlib import Path

skill = Path("skills/refinar-prosa/SKILL.md").read_text()
readme = Path("README.md").read_text()
missing = [f"SKILL.md: {n}" for n in range(26, 34) if f"{n} —" not in skill]
missing += [f"README.md: {n}" for n in range(26, 34) if f"{n} —" not in readme]
if "references/estilo-avancado.md" not in skill:
    missing.append("SKILL.md: references/estilo-avancado.md")
print("\n".join(missing))
raise SystemExit(not missing)
PY
```

Expected: exit code `1` e linhas referentes aos itens ausentes.

- [ ] **Step 2: Adicionar o mapa ao `SKILL.md`**

Use `apply_patch` para acrescentar junto aos grupos anteriores:

```markdown
### Estilo avançado e cadência — padrões 26–33

26 — Hifenização imprópria em português
27 — Fórmulas de autoridade persuasiva
28 — Anúncios do percurso textual
29 — Títulos seguidos de reformulação
30 — Documentação ancorada na mudança
31 — Sequências curtas de dramatização artificial
32 — Fórmulas aforísticas no lugar de precisão
33 — Aberturas de falsa espontaneidade

Se a leitura encontrar hifenização duvidosa, autoridade formulaica,
metadiscurso, repetição de título, documentação presa ao histórico,
dramatização fragmentada, aforismo impreciso ou falsa espontaneidade, leia
[`references/estilo-avancado.md`](references/estilo-avancado.md) antes do
rascunho.
```

- [ ] **Step 3: Adicionar o resumo ao README**

Use `apply_patch` para acrescentar ao catálogo público:

```markdown
### Estilo avançado e cadência

26 — Hifenização imprópria em português
27 — Fórmulas de autoridade persuasiva
28 — Anúncios do percurso textual
29 — Títulos seguidos de reformulação
30 — Documentação ancorada na mudança
31 — Sequências curtas de dramatização artificial
32 — Fórmulas aforísticas no lugar de precisão
33 — Aberturas de falsa espontaneidade
```

- [ ] **Step 4: Validar nomes e ligação direta**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
import re

expected = [
    (26, "Hifenização imprópria em português"),
    (27, "Fórmulas de autoridade persuasiva"),
    (28, "Anúncios do percurso textual"),
    (29, "Títulos seguidos de reformulação"),
    (30, "Documentação ancorada na mudança"),
    (31, "Sequências curtas de dramatização artificial"),
    (32, "Fórmulas aforísticas no lugar de precisão"),
    (33, "Aberturas de falsa espontaneidade"),
]
reference = Path("skills/refinar-prosa/references/estilo-avancado.md").read_text()
skill = Path("skills/refinar-prosa/SKILL.md").read_text()
readme = Path("README.md").read_text()
assert [(int(n), name) for n, name in re.findall(r"^## (\d+) — (.+)$", reference, re.M)] == expected
for number, name in expected:
    needle = f"{number} — {name}"
    assert skill.count(needle) == 1, ("SKILL.md", needle)
    assert readme.count(needle) == 1, ("README.md", needle)
assert "[references/estilo-avancado.md](references/estilo-avancado.md)" in skill
print("advanced style routing: ok")
PY
```

Expected: exit code `0` e saída `advanced style routing: ok`.

- [ ] **Step 5: Commitar roteamento e README**

```bash
git add skills/refinar-prosa/SKILL.md README.md
git commit -m "docs: complete pattern catalog routing"
```

### Task 3: Executar auditoria integrada do catálogo 1–33

**Files:**
- Test: `.codex-plugin/plugin.json`
- Test: `skills/refinar-prosa/SKILL.md`
- Test: `skills/refinar-prosa/references/*.md`
- Test: `README.md`

**Interfaces:**
- Consumes: todas as famílias do catálogo e o roteamento das Tasks 1–2.
- Produces: evidência de sequência completa e plugin válido.

- [ ] **Step 1: Auditar sequência global, exemplos e proteções**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
import re

paths = [
    "skills/refinar-prosa/references/conteudo.md",
    "skills/refinar-prosa/references/linguagem.md",
    "skills/refinar-prosa/references/formatacao.md",
    "skills/refinar-prosa/references/comunicacao.md",
    "skills/refinar-prosa/references/estilo-avancado.md",
]
text = "\n".join(Path(path).read_text() for path in paths)
numbers = [int(n) for n in re.findall(r"^## (\d+) —", text, re.M)]
assert numbers == list(range(1, 34)), numbers
advanced = Path(paths[-1]).read_text()
assert advanced.count("### Antes") == 8
assert advanced.count("### Depois") == 8
for protected in ["publicidade criativa e ficção", "Changelogs", "notas de versão", "guias de migração", "frase curta enfática isolada"]:
    assert protected in advanced, protected
print("catalog 1-33: ok")
PY
```

Expected: exit code `0` e saída `catalog 1-33: ok`.

- [ ] **Step 2: Executar validadores e higiene**

Run:

```bash
python3 /home/thiago-botelho/.config/orca/codex-accounts/9ae230c7-073c-4dc6-85bc-436aca338b5d/home/skills/.system/skill-creator/scripts/quick_validate.py skills/refinar-prosa
```

Expected: exit code `0` e mensagem de skill válida.

Run o validador de plugins Codex identificado na implementação da #2. Expected:
exit code `0`, manifesto e skill aceitos.

Run:

```bash
rg -n -i 'claude|\.claude-plugin|marketplace\.json|placeholder|\[preencher\]' .codex-plugin skills README.md
git diff --check
git status --short
```

Expected: `rg` com exit code `1` e nenhuma saída; `git diff --check` sem saída;
nenhum arquivo inesperado no status.

- [ ] **Step 3: Commitar eventual correção estritamente necessária**

Se e somente se a validação exigir correção nos três arquivos em escopo:

```bash
git add skills/refinar-prosa/references/estilo-avancado.md skills/refinar-prosa/SKILL.md README.md
git commit -m "fix: validate complete pattern catalog"
```

Caso não haja correção, não criar commit vazio.
