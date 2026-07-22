# Refinar Prosa Formatting Patterns 14–19 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implementar os padrões de formatação e estilo visual 14–19 em uma referência canônica, preservando estrutura e seguindo as convenções observadas no documento.

**Architecture:** `skills/refinar-prosa/references/formatacao.md` concentrará regras contextuais e exemplos. `SKILL.md` fará triagem e ligação direta, enquanto o README repetirá apenas números e nomes; verificações estáticas protegerão Markdown e a sequência global do catálogo.

**Tech Stack:** Markdown, frontmatter YAML, Python 3, expressões regulares, `rg`, validador de Agent Skills e validador de plugins Codex.

## Global Constraints

- As implementações da #3 e da #5 são pré-condições obrigatórias.
- Criar somente `skills/refinar-prosa/references/formatacao.md` e modificar somente `skills/refinar-prosa/SKILL.md` e `README.md` como arquivos do produto.
- A referência é a única fonte canônica de regras, limites e exemplos dos padrões 14–19.
- O `SKILL.md` deve ligar diretamente `references/formatacao.md`.
- Os padrões devem permanecer numerados exatamente de 14 a 19 na sequência global.
- Seguir, nesta ordem: instrução explícita, convenção do documento, amostra do autor, convenção do gênero/idioma e preferência padrão da skill.
- Não banir pontuação, negrito, listas, capitalização, emojis ou aspas de forma absoluta.
- Preservar frontmatter, links, tabelas, código, comandos, dados e sintaxe Markdown funcional.
- Preservar listas quando facilitarem consulta, comparação ou execução.
- Preservar nomes próprios, siglas, grafias oficiais e conteúdo protegido entre aspas.
- Cada padrão precisa de problema, sinais candidatos, confirmação contextual, falsos positivos, antes, depois e preservação estrutural e semântica.
- Não modificar manifesto, `agents/openai.yaml`, versão ou outros grupos do catálogo.
- Não deixar marcadores incompletos nem metadados específicos do Claude.

## File Structure

| Arquivo | Responsabilidade |
| --- | --- |
| `skills/refinar-prosa/references/formatacao.md` | Fonte canônica dos padrões 14–19 e do contrato visual. |
| `skills/refinar-prosa/SKILL.md` | Triagem, nomes estáveis e ligação direta. |
| `README.md` | Resumo público sincronizado dos nomes. |

---

### Task 1: Criar a referência canônica dos padrões 14–19

**Files:**
- Create: `skills/refinar-prosa/references/formatacao.md`
- Test: `skills/refinar-prosa/references/formatacao.md`

**Interfaces:**
- Consumes: contrato editorial da #3 e estrutura de catálogo da #5.
- Produces: seis padrões completos e um contrato de preservação estrutural para o roteamento da Task 2.

- [ ] **Step 1: Verificar pré-condições e ausência da nova referência**

Run:

```bash
python3 - <<'PY'
from pathlib import Path

skill = Path("skills/refinar-prosa/SKILL.md").read_text()
required = ["## Contrato editorial", "## Seleção do modo", "references/conteudo.md"]
missing = [item for item in required if item not in skill]
assert not missing, missing
path = Path("skills/refinar-prosa/references/formatacao.md")
assert not path.exists(), path
print("formatting preconditions: ok")
PY
```

Expected: exit code `0` e saída `formatting preconditions: ok`.

- [ ] **Step 2: Criar a referência**

Use `apply_patch` para criar `skills/refinar-prosa/references/formatacao.md` com
este conteúdo:

````markdown
# Padrões de formatação e estilo visual 14–19

Use estes padrões somente depois de confirmar o contrato editorial do
`refinar-prosa`. Nenhum sinal visual isolado justifica reformatar o texto.

## Hierarquia de decisão

Siga, nesta ordem:

1. instrução explícita do usuário;
2. convenção consistente do documento;
3. amostra de voz do autor;
4. convenção do gênero e do idioma;
5. preferência editorial padrão da skill.

## Proteção estrutural

Em edições de arquivo, preserve frontmatter e delimitadores, destinos de links,
tabelas, cercas e conteúdo de código, comandos, opções, nomes de arquivo, dados
e sintaxe Markdown funcional. Preserve listas que facilitem consulta, comparação
ou execução. Edite somente a prosa quando estrutura, destino e semântica
protegida continuarem intactos.

## 14 — Travessões formulaicos ou excessivos

### Problema

Usa travessões em sequência como molde automático para apartes, conclusões ou
explicações que poderiam seguir a pontuação e a cadência do documento.

### Sinais candidatos

- várias frases consecutivas terminam em inciso com travessão;
- o travessão separa complemento curto sem contraste ou aparte;
- a mesma pausa reaparece independentemente da relação lógica;
- a pontuação chama mais atenção que a informação.

### Confirmação contextual

Aplique quando a recorrência for mecânica e não corresponder à voz do autor nem
à convenção do documento.

### Não alterar quando

- o travessão marcar diálogo;
- houver inciso, interrupção ou contraste legítimo;
- a amostra do autor usar essa cadência intencionalmente;
- a publicação exigir a convenção.

### Antes

```text
O relatório foi entregue — dentro do prazo. A equipe respondeu — sem atraso. O
cliente aprovou — sem ressalvas.
```

### Depois

```text
O relatório foi entregue dentro do prazo. A equipe respondeu sem atraso, e o
cliente aprovou sem ressalvas.
```

### Preservação estrutural e semântica

Permanecem prazo, resposta e aprovação. Saem apenas pausas repetidas sem função;
travessões legítimos em outros trechos permanecem.

## 15 — Negrito mecânico

### Problema

Marca palavras ou rótulos em negrito de forma repetitiva, sem hierarquia
informativa ou necessidade de consulta.

### Sinais candidatos

- quase todo substantivo recebe destaque;
- cada item começa com rótulo em negrito sem função de consulta;
- a ênfase não distingue prioridade;
- a marcação compete com títulos e avisos reais.

### Confirmação contextual

Aplique quando retirar a marcação melhorar a hierarquia sem apagar ênfase
intencional.

### Não alterar quando

- o negrito identificar termo definido, alerta ou ação principal;
- houver convenção consistente no documento;
- a marcação apoiar leitura rápida de conteúdo extenso;
- o usuário pedir o destaque.

### Antes

```markdown
O comando exige uma **chave** e retorna uma **resposta** em formato **JSON**.
```

### Depois

```markdown
O comando exige uma chave e retorna uma resposta em formato JSON.
```

### Preservação estrutural e semântica

Permanecem requisito, retorno e formato. Só a marcação sem função é removida;
`JSON` não é substituído.

## 16 — Listas verticais com cabeçalhos repetitivos

### Problema

Fragmenta uma sequência curta em lista cujos itens repetem rótulos e produzem
mais estrutura do que informação.

### Sinais candidatos

- lista curta de frases que formariam um período claro;
- todos os itens têm cabeçalhos mecânicos em negrito;
- não há ordem, comparação nem necessidade de consulta;
- a fragmentação interrompe a cadência.

### Confirmação contextual

Aplique quando a lista não tiver função operacional ou de referência e a prosa
preservar todas as relações.

### Não alterar quando

- os itens forem passos, requisitos, opções ou inventário;
- a ordem tiver valor;
- o leitor precisar comparar ou localizar itens;
- a lista fizer parte de uma interface ou modelo.

### Antes

```markdown
- **Prazo:** a inscrição termina na sexta-feira.
- **Canal:** o envio ocorre pelo portal.
- **Retorno:** a confirmação chega por e-mail.
```

### Depois

```markdown
A inscrição termina na sexta-feira, o envio ocorre pelo portal e a confirmação
chega por e-mail.
```

### Preservação estrutural e semântica

Permanecem prazo, canal e retorno. A conversão só ocorre porque os itens formam
uma frase curta, não uma sequência operacional.

## 17 — Capitalização inadequada de títulos

### Problema

Aplica maiúsculas a palavras significativas de títulos por influência do inglês
ou alterna convenções sem motivo no mesmo documento.

### Sinais candidatos

- substantivos, verbos e adjetivos comuns começam com maiúscula;
- títulos equivalentes usam convenções diferentes;
- preposições variam sem regra editorial;
- a capitalização não corresponde ao idioma do documento.

### Confirmação contextual

Aplique somente depois de identificar a convenção predominante. Na ausência
dela, prefira em português maiúscula inicial.

### Não alterar quando

- nome próprio, sigla ou grafia oficial exigir maiúscula;
- o guia editorial determinar title case;
- o trecho reproduzir título de obra ou interface;
- a amostra do autor estabelecer outra convenção consistente.

### Antes

```markdown
## Como Configurar o Banco de Dados no Amazon RDS
```

### Depois

```markdown
## Como configurar o banco de dados no Amazon RDS
```

### Preservação estrutural e semântica

Permanecem nível, assunto e nome oficial `Amazon RDS`. Só a capitalização
incompatível com a convenção em português é ajustada.

## 18 — Emojis decorativos

### Problema

Acrescenta emojis a títulos ou itens sem função informativa, afetiva ou de marca
solicitada.

### Sinais candidatos

- cada título recebe um símbolo diferente;
- o emoji não codifica status nem significado;
- a decoração contrasta com o grau de formalidade;
- retirar o símbolo não muda a leitura.

### Confirmação contextual

Aplique quando os símbolos forem ornamentos repetitivos sem função observável
ou instruída.

### Não alterar quando

- integrarem a voz do autor ou a comunicação informal solicitada;
- representarem status, escala ou legenda;
- fizerem parte de interface, citação ou nome;
- o guia de marca os exigir.

### Antes

```markdown
## 🚀 Instalação

## ✨ Configuração
```

### Depois

```markdown
## Instalação

## Configuração
```

### Preservação estrutural e semântica

Permanecem títulos, hierarquia e ordem. Saem apenas os símbolos decorativos.

## 19 — Convenção de aspas inconsistente

### Problema

Alterna aspas retas, curvas, simples ou outra convenção sem função e contra o
padrão predominante do documento.

### Sinais candidatos

- o mesmo nível de citação usa sinais diferentes;
- aspas mudam no meio de uma seção sem aninhamento;
- prosa e exemplos têm convenções misturadas por acidente;
- a inconsistência dificulta reconhecer os limites da citação.

### Confirmação contextual

Aplique somente à prosa editável e conforme a convenção predominante.

### Não alterar quando

- as aspas estiverem em código, comando ou dado;
- houver aninhamento de citações;
- estilo editorial ou formato exigir outra marcação;
- o sinal fizer parte do conteúdo citado.

### Antes

```text
O documento chama a primeira etapa de “triagem” e a segunda de "revisão".
```

### Depois

```text
O documento chama a primeira etapa de “triagem” e a segunda de “revisão”.
```

### Preservação estrutural e semântica

Permanecem os nomes das etapas. A segunda marcação acompanha a convenção já
estabelecida; o conteúdo entre aspas não muda.

## Auditoria do grupo

Antes de entregar a versão final, confirme:

- frontmatter, links, tabelas, código, comandos e dados continuam intactos;
- nenhuma lista útil foi convertida em prosa;
- nomes próprios e grafias oficiais preservam capitalização;
- a pontuação segue a amostra ou o documento, não uma regra universal;
- símbolos e destaques mantidos têm função observável ou instruída.
````

- [ ] **Step 3: Validar estrutura, campos e proteções**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
import re

text = Path("skills/refinar-prosa/references/formatacao.md").read_text()
expected = [
    (14, "Travessões formulaicos ou excessivos"),
    (15, "Negrito mecânico"),
    (16, "Listas verticais com cabeçalhos repetitivos"),
    (17, "Capitalização inadequada de títulos"),
    (18, "Emojis decorativos"),
    (19, "Convenção de aspas inconsistente"),
]
found = [(int(n), name) for n, name in re.findall(r"^## (\d+) — (.+)$", text, re.M)]
assert found == expected, found
sections = re.split(r"^## \d+ — .+$", text, flags=re.M)[1:]
required = ["### Problema", "### Sinais candidatos", "### Confirmação contextual", "### Não alterar quando", "### Antes", "### Depois", "### Preservação estrutural e semântica"]
for number, section in zip(range(14, 20), sections):
    missing = [heading for heading in required if heading not in section]
    assert not missing, (number, missing)
for item in ["frontmatter", "destinos de links", "conteúdo de código", "Preserve listas"]:
    assert item in text, item
print("formatting reference: ok")
PY
```

Expected: exit code `0` e saída `formatting reference: ok`.

- [ ] **Step 4: Commitar a referência**

```bash
git add skills/refinar-prosa/references/formatacao.md
git commit -m "feat: add formatting patterns 14-19"
```

### Task 2: Integrar roteamento e catálogo público

**Files:**
- Modify: `skills/refinar-prosa/SKILL.md`
- Modify: `README.md`
- Test: `skills/refinar-prosa/SKILL.md`
- Test: `README.md`

**Interfaces:**
- Consumes: os nomes estáveis e a referência da Task 1.
- Produces: mapa de triagem e resumo público sincronizados.

- [ ] **Step 1: Executar a verificação negativa de roteamento**

Run:

```bash
python3 - <<'PY'
from pathlib import Path

skill = Path("skills/refinar-prosa/SKILL.md").read_text()
readme = Path("README.md").read_text()
missing = [f"SKILL.md: {n}" for n in range(14, 20) if f"{n} —" not in skill]
missing += [f"README.md: {n}" for n in range(14, 20) if f"{n} —" not in readme]
if "references/formatacao.md" not in skill:
    missing.append("SKILL.md: references/formatacao.md")
print("\n".join(missing))
raise SystemExit(not missing)
PY
```

Expected: exit code `1` e linhas referentes aos itens ausentes.

- [ ] **Step 2: Adicionar o mapa ao `SKILL.md`**

Use `apply_patch` para acrescentar junto aos grupos anteriores:

```markdown
### Formatação e estilo visual — padrões 14–19

14 — Travessões formulaicos ou excessivos
15 — Negrito mecânico
16 — Listas verticais com cabeçalhos repetitivos
17 — Capitalização inadequada de títulos
18 — Emojis decorativos
19 — Convenção de aspas inconsistente

Se a leitura encontrar repetição formulaica de travessões, negrito mecânico,
lista vertical sem função, capitalização incompatível, emoji decorativo ou
aspas inconsistentes, leia
[`references/formatacao.md`](references/formatacao.md) antes do rascunho.
```

- [ ] **Step 3: Adicionar o resumo ao README**

Use `apply_patch` para acrescentar ao catálogo público:

```markdown
### Formatação e estilo visual

14 — Travessões formulaicos ou excessivos
15 — Negrito mecânico
16 — Listas verticais com cabeçalhos repetitivos
17 — Capitalização inadequada de títulos
18 — Emojis decorativos
19 — Convenção de aspas inconsistente
```

- [ ] **Step 4: Validar sequência, nomes e ligação direta**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
import re

expected = [
    (14, "Travessões formulaicos ou excessivos"),
    (15, "Negrito mecânico"),
    (16, "Listas verticais com cabeçalhos repetitivos"),
    (17, "Capitalização inadequada de títulos"),
    (18, "Emojis decorativos"),
    (19, "Convenção de aspas inconsistente"),
]
reference = Path("skills/refinar-prosa/references/formatacao.md").read_text()
skill = Path("skills/refinar-prosa/SKILL.md").read_text()
readme = Path("README.md").read_text()
assert [(int(n), name) for n, name in re.findall(r"^## (\d+) — (.+)$", reference, re.M)] == expected
for number, name in expected:
    needle = f"{number} — {name}"
    assert skill.count(needle) == 1, ("SKILL.md", needle)
    assert readme.count(needle) == 1, ("README.md", needle)
assert "[references/formatacao.md](references/formatacao.md)" in skill
print("formatting routing: ok")
PY
```

Expected: exit code `0` e saída `formatting routing: ok`.

- [ ] **Step 5: Commitar roteamento e README**

```bash
git add skills/refinar-prosa/SKILL.md README.md
git commit -m "docs: route formatting patterns"
```

### Task 3: Executar auditoria integrada do catálogo 1–19

**Files:**
- Test: `.codex-plugin/plugin.json`
- Test: `skills/refinar-prosa/SKILL.md`
- Test: `skills/refinar-prosa/references/conteudo.md`
- Test: `skills/refinar-prosa/references/linguagem.md`
- Test: `skills/refinar-prosa/references/formatacao.md`
- Test: `README.md`

**Interfaces:**
- Consumes: referência e roteamento das Tasks 1–2 e grupos anteriores.
- Produces: evidência de catálogo contínuo e plugin válido.

- [ ] **Step 1: Auditar numeração global e contrato estrutural**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
import re

paths = [
    "skills/refinar-prosa/references/conteudo.md",
    "skills/refinar-prosa/references/linguagem.md",
    "skills/refinar-prosa/references/formatacao.md",
]
text = "\n".join(Path(path).read_text() for path in paths)
numbers = [int(n) for n in re.findall(r"^## (\d+) —", text, re.M)]
assert numbers == list(range(1, 20)), numbers
formatting = Path(paths[-1]).read_text()
assert formatting.count("### Antes") == 6
assert formatting.count("### Depois") == 6
for protected in ["frontmatter", "destinos de links", "tabelas", "conteúdo de código", "comandos", "dados"]:
    assert protected in formatting, protected
print("catalog 1-19: ok")
PY
```

Expected: exit code `0` e saída `catalog 1-19: ok`.

- [ ] **Step 2: Executar validadores estruturais e higiene**

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
git add skills/refinar-prosa/references/formatacao.md skills/refinar-prosa/SKILL.md README.md
git commit -m "fix: validate formatting pattern catalog"
```

Caso não haja correção, não criar commit vazio.
