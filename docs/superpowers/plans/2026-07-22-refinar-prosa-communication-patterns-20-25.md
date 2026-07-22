# Refinar Prosa Communication Patterns 20–25 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implementar os padrões de comunicação, preenchimento e hesitação 20–25 sem apagar correspondência legítima, incerteza real ou cautela material.

**Architecture:** `skills/refinar-prosa/references/comunicacao.md` será a fonte canônica do grupo. `SKILL.md` fará triagem e ligação direta, o README repetirá apenas os nomes, e testes estáticos verificarão confiança, atribuição, gêneros protegidos e sequência global.

**Tech Stack:** Markdown, frontmatter YAML, Python 3, expressões regulares, `rg`, validador de Agent Skills e validador de plugins Codex.

## Global Constraints

- As implementações da #3 e da #5 são pré-condições obrigatórias.
- Criar somente `skills/refinar-prosa/references/comunicacao.md` e modificar somente `skills/refinar-prosa/SKILL.md` e `README.md` como arquivos do produto.
- A referência é a única fonte canônica dos padrões 20–25.
- O `SKILL.md` deve ligar diretamente `references/comunicacao.md`.
- Os padrões devem permanecer numerados exatamente de 20 a 25.
- Preservar incerteza, escopo, modalidade, atribuição e cautela material.
- Não inventar fonte, consenso, vigência, atualização, fato ou certeza.
- Não remover saudações, despedidas, agradecimentos ou ofertas legítimas de correspondência e atendimento.
- Em texto embutido, retornar somente o texto final solicitado.
- Conclusões permanecem quando sintetizam fatos, decisões, riscos ou próximos passos.
- Cada padrão precisa de problema, sinais candidatos, confirmação contextual, falsos positivos, antes, depois e preservação factual e de confiança.
- Não modificar manifesto, `agents/openai.yaml`, versão ou outros grupos do catálogo.
- Não deixar marcadores incompletos nem metadados específicos do Claude.

## File Structure

| Arquivo | Responsabilidade |
| --- | --- |
| `skills/refinar-prosa/references/comunicacao.md` | Fonte canônica dos padrões 20–25 e da regra de confiança. |
| `skills/refinar-prosa/SKILL.md` | Triagem, nomes estáveis e ligação direta. |
| `README.md` | Resumo público sincronizado dos nomes. |

---

### Task 1: Criar a referência canônica dos padrões 20–25

**Files:**
- Create: `skills/refinar-prosa/references/comunicacao.md`
- Test: `skills/refinar-prosa/references/comunicacao.md`

**Interfaces:**
- Consumes: contrato editorial da #3 e estrutura de catálogo da #5.
- Produces: seis padrões auditáveis e regras de confiança e gênero para a Task 2.

- [ ] **Step 1: Verificar pré-condições e ausência da referência**

Run:

```bash
python3 - <<'PY'
from pathlib import Path

skill = Path("skills/refinar-prosa/SKILL.md").read_text()
required = ["## Contrato editorial", "## Seleção do modo", "references/conteudo.md"]
missing = [item for item in required if item not in skill]
assert not missing, missing
path = Path("skills/refinar-prosa/references/comunicacao.md")
assert not path.exists(), path
print("communication preconditions: ok")
PY
```

Expected: exit code `0` e saída `communication preconditions: ok`.

- [ ] **Step 2: Criar a referência**

Use `apply_patch` para criar `skills/refinar-prosa/references/comunicacao.md`
com este conteúdo:

````markdown
# Padrões de comunicação, preenchimento e hesitação 20–25

Use estes padrões somente depois de confirmar o contrato editorial do
`refinar-prosa` e identificar o gênero do texto.

## Confiança e atribuição

A edição pode tornar uma incerteza mais clara, mas não pode aumentar nem reduzir
o grau de confiança sustentado pela fonte. Não transforme ausência de
informação em fato nem crie fonte, consenso, vigência ou atualização.

Em textos jurídicos, científicos, médicos, financeiros ou de risco, preserve
ressalvas que delimitam escopo, probabilidade, obrigação ou limitação.

## Correspondência e gênero

Preserve saudações, despedidas, agradecimentos e ofertas de ajuda quando o texto
for e-mail, carta, atendimento ou outro gênero em que cumpram função social.
Remova resíduos de conversa com o modelo apenas quando o texto final precisar
ser autônomo.

## 20 — Artefatos de chatbot e ofertas de continuação

### Problema

Mantém no texto final saudações ao solicitante, comentários sobre a tarefa,
ofertas de continuar ou frases como “espero que ajude” sem função no gênero.

### Sinais candidatos

- “espero que isso ajude” depois do conteúdo;
- “se quiser, posso continuar” em documento autônomo;
- comentário sobre ter produzido ou revisado o texto;
- saudação genérica em descrição de PR, commit ou documentação.

### Confirmação contextual

Aplique quando a frase revelar a interação com o assistente e não cumprir função
social ou operacional no gênero.

### Não alterar quando

- o texto for e-mail, carta ou mensagem de atendimento;
- a oferta de ajuda for uma ação real do remetente;
- a saudação ou despedida fizer parte da voz solicitada;
- o trecho citado estiver sendo analisado.

### Antes

```text
A API aceita requisições JSON e retorna o identificador do pedido. Espero que
isso ajude! Se quiser, posso explicar os campos em mais detalhes.
```

### Depois

```text
A API aceita requisições JSON e retorna o identificador do pedido.
```

### Preservação factual e de confiança

Permanecem entrada e retorno da API. Saem apenas comentários ao solicitante que
não pertencem à documentação.

## 21 — Avisos de limite de conhecimento e preenchimento especulativo

### Problema

Insere avisos sobre o conhecimento do modelo ou especula sobre mudanças para
compensar a falta de informação na fonte.

### Sinais candidatos

- menção à data-limite de conhecimento do modelo;
- “pode ter mudado” sem relação com a fonte;
- previsão sobre vigência ou estado atual sem evidência;
- preenchimento de lacuna com hipótese não solicitada.

### Confirmação contextual

Aplique quando o metacomentário puder ser substituído por uma limitação
verificável do material disponível ou removido sem perder cautela.

### Não alterar quando

- a data de consulta for informação metodológica real;
- o texto precisar declarar limitação temporal de uma pesquisa;
- a hipótese estiver atribuída e fizer parte da análise;
- o usuário solicitar pesquisa atual, que deve ser feita e citada separadamente.

### Antes

```text
O regulamento foi publicado em 2022. Como meu conhecimento pode estar
desatualizado, talvez ele ainda esteja vigente.
```

### Depois

```text
O regulamento foi publicado em 2022; o texto fornecido não informa se ele
continua vigente.
```

### Preservação factual e de confiança

Permanecem data, publicação e incerteza sobre vigência. A limitação passa a se
referir à fonte; nenhuma atualização é inventada.

## 22 — Tom adulador ou servil

### Problema

Acrescenta elogios automáticos, concordância excessiva ou deferência que desvia
do conteúdo e pode simular validação factual.

### Sinais candidatos

- “excelente pergunta” sem função social;
- “você está absolutamente certo” antes da evidência;
- elogio genérico à ideia ou ao usuário;
- concordância mais ampla que os fatos apresentados.

### Confirmação contextual

Aplique quando a cortesia não pertencer ao gênero e puder ser removida sem
alterar o relacionamento ou o conteúdo.

### Não alterar quando

- houver reconhecimento específico e verdadeiro;
- o gênero exigir hospitalidade ou acolhimento;
- a voz de marca solicitar calor humano;
- a frase fizer parte de correspondência legítima.

### Antes

```text
Excelente observação — você está absolutamente certo. A opção B usa menos
memória nos testes apresentados.
```

### Depois

```text
Nos testes apresentados, a opção B usa menos memória.
```

### Preservação factual e de confiança

Permanece a comparação limitada aos testes. Saem elogio e concordância absoluta,
que poderiam ampliar a conclusão.

## 23 — Preenchimento sem função

### Problema

Usa prefácios, transições ou comentários genéricos que atrasam uma afirmação sem
delimitar contexto, relação lógica ou cautela.

### Sinais candidatos

- “é importante observar que” sem ênfase necessária;
- “de modo geral” sem exceção ou escopo;
- introdução que repete o título;
- frase que pode sair sem alterar conteúdo ou ligação.

### Confirmação contextual

Aplique quando o material não mudar sentido, ênfase necessária, relação lógica
ou grau de confiança.

### Não alterar quando

- a transição explicitar contraste, causa ou sequência;
- o enquadramento delimitar escopo;
- a repetição apoiar acessibilidade ou instrução;
- a ênfase tiver função no gênero.

### Antes

```text
É importante observar que, de modo geral, a reunião começa às 9h.
```

### Depois

```text
A reunião começa às 9h.
```

### Preservação factual e de confiança

Permanece o horário. Saem prefácios que não qualificavam a afirmação.

## 24 — Empilhamento de ressalvas

### Problema

Acumula marcadores de possibilidade ou cautela que expressam o mesmo grau de
incerteza e tornam a frase evasiva.

### Sinais candidatos

- `talvez`, `pode` e `possivelmente` na mesma oração;
- vários verbos modais com o mesmo alcance;
- ressalvas repetidas sem dimensões distintas;
- cautela verbal que encobre a afirmação principal.

### Confirmação contextual

Aplique quando os marcadores forem semanticamente redundantes e uma forma mais
curta preservar o mesmo grau de confiança.

### Não alterar quando

- cada ressalva delimitar dimensão diferente;
- amostra, método, escopo e risco exigirem cautelas próprias;
- norma jurídica ou científica exigir a formulação;
- condensar aumentar a certeza.

### Antes

```text
Os resultados talvez possam possivelmente indicar uma redução de falhas.
```

### Depois

```text
Os resultados podem indicar uma redução de falhas.
```

### Preservação factual e de confiança

Permanece a possibilidade, sem convertê-la em certeza. Saem apenas marcadores
redundantes do mesmo grau de hesitação.

## 25 — Conclusões positivas genéricas

### Problema

Encerra com “futuro promissor”, “passo importante” ou otimismo equivalente sem
fato, decisão ou próximo passo que sustente a conclusão.

### Sinais candidatos

- último período acrescenta apenas avaliação positiva;
- a conclusão repete abstrações sem sintetizar fatos;
- promessa de progresso não identifica ação ou responsável;
- o texto fica completo antes do fechamento.

### Confirmação contextual

Aplique quando a conclusão não contiver informação, decisão, risco ou próximo
passo sustentado.

### Não alterar quando

- sintetizar fatos ou argumento;
- registrar decisão, risco ou ação seguinte;
- a avaliação estiver atribuída ou apoiada;
- o gênero pedir chamada à ação legítima.

### Antes

```text
A migração termina em 15 de agosto. Com isso, a organização caminha para um
futuro cada vez mais promissor.
```

### Depois

```text
A migração termina em 15 de agosto.
```

### Preservação factual e de confiança

Permanecem evento e data. Sai a projeção positiva sem suporte; nenhum benefício
é inferido.

## Auditoria do grupo

Antes de entregar a versão final, confirme:

- nenhuma saudação ou despedida legítima foi removida;
- incerteza, escopo e cautela material permanecem;
- nenhuma fonte, vigência, consenso ou certeza foi inventada;
- toda conclusão mantida contém fato, decisão, risco ou próximo passo;
- texto embutido contém somente o resultado solicitado.
````

- [ ] **Step 3: Validar estrutura e proteções**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
import re

text = Path("skills/refinar-prosa/references/comunicacao.md").read_text()
expected = [
    (20, "Artefatos de chatbot e ofertas de continuação"),
    (21, "Avisos de limite de conhecimento e preenchimento especulativo"),
    (22, "Tom adulador ou servil"),
    (23, "Preenchimento sem função"),
    (24, "Empilhamento de ressalvas"),
    (25, "Conclusões positivas genéricas"),
]
found = [(int(n), name) for n, name in re.findall(r"^## (\d+) — (.+)$", text, re.M)]
assert found == expected, found
sections = re.split(r"^## \d+ — .+$", text, flags=re.M)[1:]
required = ["### Problema", "### Sinais candidatos", "### Confirmação contextual", "### Não alterar quando", "### Antes", "### Depois", "### Preservação factual e de confiança"]
for number, section in zip(range(20, 26), sections):
    missing = [heading for heading in required if heading not in section]
    assert not missing, (number, missing)
for item in ["Não transforme ausência de", "jurídicos, científicos", "Preserve saudações", "sem convertê-la em certeza"]:
    assert item in text, item
print("communication reference: ok")
PY
```

Expected: exit code `0` e saída `communication reference: ok`.

- [ ] **Step 4: Commitar a referência**

```bash
git add skills/refinar-prosa/references/comunicacao.md
git commit -m "feat: add communication patterns 20-25"
```

### Task 2: Integrar roteamento e catálogo público

**Files:**
- Modify: `skills/refinar-prosa/SKILL.md`
- Modify: `README.md`
- Test: `skills/refinar-prosa/SKILL.md`
- Test: `README.md`

**Interfaces:**
- Consumes: os nomes estáveis e a referência da Task 1.
- Produces: triagem e resumo público sincronizados.

- [ ] **Step 1: Executar a verificação negativa de roteamento**

Run:

```bash
python3 - <<'PY'
from pathlib import Path

skill = Path("skills/refinar-prosa/SKILL.md").read_text()
readme = Path("README.md").read_text()
missing = [f"SKILL.md: {n}" for n in range(20, 26) if f"{n} —" not in skill]
missing += [f"README.md: {n}" for n in range(20, 26) if f"{n} —" not in readme]
if "references/comunicacao.md" not in skill:
    missing.append("SKILL.md: references/comunicacao.md")
print("\n".join(missing))
raise SystemExit(not missing)
PY
```

Expected: exit code `1` e linhas referentes aos itens ausentes.

- [ ] **Step 2: Adicionar o mapa ao `SKILL.md`**

Use `apply_patch` para acrescentar junto aos grupos anteriores:

```markdown
### Comunicação, preenchimento e hesitação — padrões 20–25

20 — Artefatos de chatbot e ofertas de continuação
21 — Avisos de limite de conhecimento e preenchimento especulativo
22 — Tom adulador ou servil
23 — Preenchimento sem função
24 — Empilhamento de ressalvas
25 — Conclusões positivas genéricas

Se a leitura encontrar resíduo de chatbot, especulação sobre informação
ausente, servilismo, preenchimento, ressalvas redundantes ou conclusão positiva
sem suporte, leia
[`references/comunicacao.md`](references/comunicacao.md) antes do rascunho.
```

- [ ] **Step 3: Adicionar o resumo ao README**

Use `apply_patch` para acrescentar ao catálogo público:

```markdown
### Comunicação, preenchimento e hesitação

20 — Artefatos de chatbot e ofertas de continuação
21 — Avisos de limite de conhecimento e preenchimento especulativo
22 — Tom adulador ou servil
23 — Preenchimento sem função
24 — Empilhamento de ressalvas
25 — Conclusões positivas genéricas
```

- [ ] **Step 4: Validar nomes e ligação direta**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
import re

expected = [
    (20, "Artefatos de chatbot e ofertas de continuação"),
    (21, "Avisos de limite de conhecimento e preenchimento especulativo"),
    (22, "Tom adulador ou servil"),
    (23, "Preenchimento sem função"),
    (24, "Empilhamento de ressalvas"),
    (25, "Conclusões positivas genéricas"),
]
reference = Path("skills/refinar-prosa/references/comunicacao.md").read_text()
skill = Path("skills/refinar-prosa/SKILL.md").read_text()
readme = Path("README.md").read_text()
assert [(int(n), name) for n, name in re.findall(r"^## (\d+) — (.+)$", reference, re.M)] == expected
for number, name in expected:
    needle = f"{number} — {name}"
    assert skill.count(needle) == 1, ("SKILL.md", needle)
    assert readme.count(needle) == 1, ("README.md", needle)
assert "[references/comunicacao.md](references/comunicacao.md)" in skill
print("communication routing: ok")
PY
```

Expected: exit code `0` e saída `communication routing: ok`.

- [ ] **Step 5: Commitar roteamento e README**

```bash
git add skills/refinar-prosa/SKILL.md README.md
git commit -m "docs: route communication patterns"
```

### Task 3: Executar auditoria integrada do catálogo 1–25

**Files:**
- Test: `.codex-plugin/plugin.json`
- Test: `skills/refinar-prosa/SKILL.md`
- Test: `skills/refinar-prosa/references/*.md`
- Test: `README.md`

**Interfaces:**
- Consumes: referência e roteamento das Tasks 1–2 e grupos anteriores.
- Produces: evidência de catálogo contínuo, confiança protegida e plugin válido.

- [ ] **Step 1: Auditar sequência global e confiança**

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
]
text = "\n".join(Path(path).read_text() for path in paths)
numbers = [int(n) for n in re.findall(r"^## (\d+) —", text, re.M)]
assert numbers == list(range(1, 26)), numbers
communication = Path(paths[-1]).read_text()
assert communication.count("### Antes") == 6
assert communication.count("### Depois") == 6
for protected in ["Preserve saudações", "grau de confiança", "jurídicos, científicos", "nenhuma fonte, vigência, consenso ou certeza"]:
    assert protected in communication, protected
print("catalog 1-25: ok")
PY
```

Expected: exit code `0` e saída `catalog 1-25: ok`.

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
git add skills/refinar-prosa/references/comunicacao.md skills/refinar-prosa/SKILL.md README.md
git commit -m "fix: validate communication pattern catalog"
```

Caso não haja correção, não criar commit vazio.
