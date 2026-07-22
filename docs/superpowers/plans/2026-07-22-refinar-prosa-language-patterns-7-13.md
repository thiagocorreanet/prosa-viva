# Refinar Prosa Language Patterns 7–13 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implementar os padrões de linguagem e gramática 7–13 em uma referência canônica para pt-BR, com roteamento direto no `SKILL.md` e resumo sincronizado no README.

**Architecture:** `skills/refinar-prosa/references/pt-BR/linguagem.md` conterá regras, limites, exemplos e inventários factuais. `SKILL.md` terá apenas o mapa de roteamento, e o README repetirá somente números e nomes; validações estáticas garantirão que a sequência 7–13 permaneça idêntica nos três arquivos.

**Tech Stack:** Markdown, frontmatter YAML, Python 3, expressões regulares, `rg`, validador de Agent Skills e validador de plugins Codex.

## Global Constraints

- As implementações da #3 e da #5 são pré-condições obrigatórias.
- Criar somente `skills/refinar-prosa/references/pt-BR/linguagem.md` e modificar somente `skills/refinar-prosa/SKILL.md` e `README.md` como arquivos do produto.
- A referência é a única fonte canônica de regras, sinais, limites e exemplos.
- O `SKILL.md` deve ligar diretamente `references/pt-BR/linguagem.md`, sem encadeamento intermediário.
- README e `SKILL.md` repetem somente os números e nomes estáveis.
- Os padrões devem permanecer numerados exatamente de 7 a 13 na sequência global.
- Palavra, verbo, pontuação ou construção isolada não comprova um padrão.
- Não transferir automaticamente para pt-BR frequências observadas em inglês.
- Preservar termos técnicos, nomes próprios, citações e escolhas necessárias ao domínio.
- Preservar voz passiva quando o agente for desconhecido, irrelevante, protegido ou quando o foco legítimo for o resultado.
- Distinguir enumerações factuais de três itens de tríades decorativas.
- Cada padrão precisa de problema, sinais candidatos, confirmação contextual, falsos positivos, antes, depois e preservação factual e terminológica.
- O conjunto de exemplos deve cobrir prosa geral e documentação técnica.
- Nenhum exemplo pode fabricar ou omitir fatos protegidos.
- A #4 não é pré-condição; o roteamento deve coexistir com ou sem calibração de voz.
- Não modificar manifesto, `agents/openai.yaml`, versão ou outros grupos do catálogo.
- Não deixar marcadores incompletos nem metadados específicos do Claude.

## File Structure

| Arquivo | Responsabilidade |
| --- | --- |
| `skills/refinar-prosa/references/pt-BR/linguagem.md` | Fonte canônica dos padrões 7–13. |
| `skills/refinar-prosa/SKILL.md` | Triagem, nomes estáveis e ligação direta. |
| `README.md` | Resumo público sincronizado dos nomes. |

---

### Task 1: Criar a referência canônica dos padrões 7–13

**Files:**
- Create: `skills/refinar-prosa/references/pt-BR/linguagem.md`
- Test: `skills/refinar-prosa/references/pt-BR/linguagem.md`

**Interfaces:**
- Consumes: contrato editorial da #3 e estrutura de catálogo da #5.
- Produces: sete padrões completos, numerados e auditáveis, para carregamento seletivo pelo `SKILL.md`.

- [ ] **Step 1: Verificar as pré-condições da #3 e da #5**

Run:

```bash
python3 - <<'PY'
from pathlib import Path

skill = Path("skills/refinar-prosa/SKILL.md").read_text()
required = [
    "## Contrato editorial",
    "## Seleção do modo",
    "## Ciclo interno",
    "references/pt-BR/conteudo.md",
]
missing = [item for item in required if item not in skill]
print("\n".join(missing))
raise SystemExit(bool(missing))
PY
```

Expected: exit code `0` e nenhuma saída. Se falhar, executar primeiro os planos
da #3 e da #5, nessa ordem.

- [ ] **Step 2: Executar a verificação negativa da referência ausente**

Run:

```bash
python3 -c 'from pathlib import Path; p=Path("skills/refinar-prosa/references/pt-BR/linguagem.md"); print("linguagem.md not found") if not p.is_file() else None; raise SystemExit(not p.is_file())'
```

Expected: exit code `1` e saída `linguagem.md not found`.

- [ ] **Step 3: Criar a referência canônica**

Use `apply_patch` para criar `skills/refinar-prosa/references/pt-BR/linguagem.md` com
este conteúdo:

````markdown
# Padrões de linguagem e gramática 7–13

Use estes padrões somente depois de confirmar o contrato editorial do
`refinar-prosa`. Palavra, verbo, pontuação ou construção isolada não comprova um
padrão.

Para cada candidato:

1. identifique sua função sintática e discursiva no contexto;
2. verifique a precisão factual e terminológica;
3. avalie o efeito sobre clareza, naturalidade e atribuição;
4. faça a menor edição que resolva o padrão;
5. preserve o trecho em caso de dúvida.

Não transfira automaticamente para o português brasileiro frequências
observadas em inglês. Preserve termos técnicos, nomes próprios, citações e
escolhas necessárias ao domínio.

## 7 — Vocabulário recorrente sem função

### Problema

Repete adjetivos, advérbios ou fórmulas de forma perceptível, sem que a repetição
organize conceitos ou preserve um termo necessário.

### Sinais candidatos

- o mesmo adjetivo genérico qualifica objetos distintos em sequência;
- fórmulas de transição reaparecem sem orientar a leitura;
- a recorrência pode ser removida sem alterar o conteúdo;
- a escolha parece traduzida de uma frequência típica do inglês.

### Confirmação contextual

Aplique somente quando a recorrência não tiver função técnica, retórica ou de
coesão e produzir monotonia ou aparência formulaica.

### Não alterar quando

- a repetição identificar um conceito ou componente técnico;
- a coesão depender do mesmo termo;
- houver paralelismo retórico intencional;
- o autor usar a recorrência como marca de voz defensável.

### Antes

```text
O plano propõe uma abordagem robusta, uma rotina robusta de revisão e um
processo robusto de aprovação.
```

### Depois

```text
O plano define a abordagem, a rotina de revisão e o processo de aprovação.
```

### Preservação factual e terminológica

Permanecem abordagem, rotina de revisão e processo de aprovação. Sai apenas o
adjetivo repetido, sem critério ou comparação; nenhum atributo é acrescentado.

## 8 — Substituição artificial de verbos simples

### Problema

Evita `ser`, `estar` ou `ter` por meio de perífrases e nominalizações que tornam
a frase menos direta sem aumentar a precisão.

### Sinais candidatos

- “apresenta como característica a presença de” no lugar de `tem`;
- “encontra-se em estado de” no lugar de `está`;
- verbo genérico acompanhado de substantivo abstrato;
- construção mais longa que expressa a mesma relação simples.

### Confirmação contextual

Aplique quando o verbo mais elaborado não expressar relação técnica própria nem
qualificação relevante.

### Não alterar quando

- o verbo nomear uma operação real, como `persistir` ou `autenticar`;
- a construção distinguir estado temporário de propriedade permanente;
- o gênero exigir formulação jurídica ou normativa precisa;
- a simplificação mudar escopo, tempo ou modalidade.

### Antes

```text
A configuração apresenta como característica a presença de duas chaves
obrigatórias.
```

### Depois

```text
A configuração tem duas chaves obrigatórias.
```

### Preservação factual e terminológica

Permanecem quantidade, obrigatoriedade e objeto. A perífrase é simplificada sem
alterar a terminologia técnica.

## 9 — Paralelismo negativo acrescentado

### Problema

Usa estruturas como “não apenas”, “não deixa de” ou uma negação final para dar
ênfase artificial a afirmações que poderiam ser diretas.

### Sinais candidatos

- “não apenas X, como também Y” sem contraste necessário;
- “não deixa de” usado apenas para intensificar;
- negação acrescentada ao fim sem corrigir expectativa anterior;
- dupla moldura negativa envolvendo fatos positivos.

### Confirmação contextual

Aplique quando as negações não delimitarem contraste, exceção, concessão ou
correção real.

### Não alterar quando

- a oposição for necessária ao argumento;
- a negação corrigir interpretação provável;
- houver contraste entre expectativa e resultado;
- a formulação preservar alcance lógico relevante.

### Antes

```text
A atualização não apenas reduz o tempo de inicialização, como também não deixa
de simplificar a configuração.
```

### Depois

```text
A atualização reduz o tempo de inicialização e simplifica a configuração.
```

### Preservação factual e terminológica

Permanecem os dois efeitos atribuídos à atualização. Saem apenas as negações
usadas como moldura enfática.

## 10 — Tríades decorativas

### Problema

Agrupa ideias em três para produzir ritmo ou autoridade, mesmo quando os itens
são redundantes, vagos ou não correspondem à estrutura real do assunto.

### Sinais candidatos

- três avaliações abstratas depois de uma descrição factual;
- lista estendida ou reduzida para terminar com três itens;
- trio de sinônimos sem distinção funcional;
- três títulos ou etapas sem correspondência com o processo real.

### Confirmação contextual

Aplique apenas quando a quantidade de itens for determinada pela fórmula, não
pelos fatos ou pela organização útil do texto.

### Não alterar quando

- houver exatamente três requisitos, etapas, arquivos ou resultados;
- a lista facilitar consulta ou execução;
- cada item tiver função distinta;
- a repetição ternária for uma escolha retórica intencional.

### Antes

```text
O guia explica instalação, configuração e solução de problemas, oferecendo
clareza, completude e transformação.
```

### Depois

```text
O guia explica instalação, configuração e solução de problemas.
```

### Preservação factual e terminológica

Permanece a enumeração factual dos três conteúdos. Sai somente a segunda
tríade, formada por avaliações sem apoio.

## 11 — Variação lexical desnecessária

### Problema

Troca o mesmo referente por sinônimos elegantes para evitar repetição e cria
ambiguidade ou perda de precisão.

### Sinais candidatos

- um componente técnico recebe nomes diferentes no mesmo trecho;
- sinônimo mais amplo substitui um termo de domínio;
- a variação sugere entidades distintas onde existe uma só;
- pronomes e perífrases dificultam identificar o referente.

### Confirmação contextual

Aplique quando os termos apontarem para o mesmo referente e a variação não
acrescentar distinção útil.

### Não alterar quando

- os termos nomearem entidades ou níveis distintos;
- a variação evitar ambiguidade real;
- o domínio reconhecer os termos como equivalentes estáveis;
- a escolha fizer parte de citação, nome próprio ou interface.

### Antes

```text
O servidor recebe a requisição. Esse serviço valida o token. A plataforma grava
o resultado no log. Nos três casos, trata-se do mesmo servidor.
```

### Depois

```text
O servidor recebe a requisição, valida o token e grava o resultado no log.
```

### Preservação factual e terminológica

Permanecem o componente, as três operações e seus objetos. `Token` e `log`
permanecem como termos técnicos; os sinônimos imprecisos são removidos.

## 12 — Intervalos falsos

### Problema

Usa “de X a Y” para ligar categorias que não formam escala, percurso ou
intervalo verificável.

### Sinais candidatos

- extremos sem dimensão comum identificável;
- par de tópicos apresentado como percurso completo;
- intervalo sem valores ou estados intermediários pertinentes;
- amplitude sugerida apenas para engrandecer o escopo.

### Confirmação contextual

Aplique quando os extremos forem apenas itens relacionados e não houver escala,
percurso ou abrangência defensável entre eles.

### Não alterar quando

- o intervalo for numérico, temporal ou geográfico;
- houver estados intermediários reconhecíveis;
- a construção descrever transformação ou percurso real;
- o domínio definir a escala empregada.

### Antes

```text
O encontro abordou temas que foram da segurança à criatividade.
```

### Depois

```text
O encontro abordou segurança e criatividade.
```

### Preservação factual e terminológica

Permanecem os dois temas. Sai apenas a sugestão de escala; nenhum tema
intermediário é inventado.

## 13 — Agente oculto sem necessidade

### Problema

Usa voz passiva ou fragmentos sem sujeito para esconder um agente relevante que
o próprio contexto já identifica.

### Sinais candidatos

- passiva logo depois de o agente ser nomeado;
- sequência de ações sem sujeito apesar de responsabilidade relevante;
- fragmento que impede saber quem tomou a decisão;
- alternância entre ativa e passiva sem mudança legítima de foco.

### Confirmação contextual

Aplique somente quando o agente estiver disponível na fonte e importar para
responsabilidade ou compreensão.

### Não alterar quando

- o agente for desconhecido ou irrelevante;
- a identidade precisar ser protegida;
- o foco legítimo for processo ou resultado;
- a convenção técnica ou científica preferir a passiva;
- explicitar o agente exigir inferência.

### Antes

```text
A equipe de infraestrutura revisou o ambiente. Em seguida, foi removido o
acesso ao banco e alterada a política de backup.
```

### Depois

```text
A equipe de infraestrutura revisou o ambiente, removeu o acesso ao banco e
alterou a política de backup.
```

### Preservação factual e terminológica

Permanecem agente, sequência, ações e objetos. O agente não é inferido: já
estava identificado no contexto.

## Auditoria do grupo

Antes de entregar a versão final, confirme:

- nenhum termo técnico ou nome próprio foi substituído;
- nenhuma oposição, escala ou agente foi inventado ou apagado;
- nenhuma enumeração factual foi confundida com tríade decorativa;
- nenhuma proibição absoluta foi aplicada por palavra isolada;
- idioma, intenção, público e grau de formalidade foram mantidos.
````

- [ ] **Step 4: Validar estrutura e conteúdo da referência**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
import re

text = Path("skills/refinar-prosa/references/pt-BR/linguagem.md").read_text()
expected = [
    (7, "Vocabulário recorrente sem função"),
    (8, "Substituição artificial de verbos simples"),
    (9, "Paralelismo negativo acrescentado"),
    (10, "Tríades decorativas"),
    (11, "Variação lexical desnecessária"),
    (12, "Intervalos falsos"),
    (13, "Agente oculto sem necessidade"),
]
found = [(int(n), name) for n, name in re.findall(r"^## (\d+) — (.+)$", text, re.M)]
assert found == expected, found
sections = re.split(r"^## \d+ — .+$", text, flags=re.M)[1:]
required = [
    "### Problema",
    "### Sinais candidatos",
    "### Confirmação contextual",
    "### Não alterar quando",
    "### Antes",
    "### Depois",
    "### Preservação factual e terminológica",
]
for number, section in zip(range(7, 14), sections):
    missing = [heading for heading in required if heading not in section]
    assert not missing, (number, missing)
assert "português brasileiro" in text
assert "termos técnicos" in text
assert "agente for desconhecido ou irrelevante" in text
assert "exatamente três requisitos" in text
print("language reference: ok")
PY
```

Expected: exit code `0` e saída `language reference: ok`.

- [ ] **Step 5: Commitar a referência**

```bash
git add skills/refinar-prosa/references/pt-BR/linguagem.md
git commit -m "feat: add language patterns 7-13"
```

### Task 2: Integrar roteamento e documentação pública

**Files:**
- Modify: `skills/refinar-prosa/SKILL.md`
- Modify: `README.md`
- Test: `skills/refinar-prosa/SKILL.md`
- Test: `README.md`

**Interfaces:**
- Consumes: os sete nomes estáveis e `references/pt-BR/linguagem.md` da Task 1.
- Produces: triagem da skill e catálogo público sincronizados com a referência.

- [ ] **Step 1: Executar a verificação negativa de roteamento**

Run:

```bash
python3 - <<'PY'
from pathlib import Path

skill = Path("skills/refinar-prosa/SKILL.md").read_text()
readme = Path("README.md").read_text()
missing = []
for path, text in [("SKILL.md", skill), ("README.md", readme)]:
    for number in range(7, 14):
        if f"{number} —" not in text:
            missing.append(f"{path}: {number}")
if "references/pt-BR/linguagem.md" not in skill:
    missing.append("SKILL.md: references/pt-BR/linguagem.md")
print("\n".join(missing))
raise SystemExit(not missing)
PY
```

Expected: exit code `1` e linhas referentes aos itens ainda ausentes.

- [ ] **Step 2: Adicionar o mapa ao `SKILL.md`**

Use `apply_patch` para acrescentar, junto ao mapa de padrões 1–6, esta seção:

```markdown
### Linguagem e gramática — padrões 7–13

7 — Vocabulário recorrente sem função
8 — Substituição artificial de verbos simples
9 — Paralelismo negativo acrescentado
10 — Tríades decorativas
11 — Variação lexical desnecessária
12 — Intervalos falsos
13 — Agente oculto sem necessidade

Se a leitura encontrar recorrência lexical sem função, substituição artificial
de verbos simples, paralelismo negativo, tríade decorativa, variação lexical que
reduz precisão, intervalo sem escala real ou agente relevante oculto, leia
[`references/pt-BR/linguagem.md`](references/pt-BR/linguagem.md) antes do rascunho.
```

- [ ] **Step 3: Adicionar o resumo ao README**

Use `apply_patch` para acrescentar, junto ao catálogo público 1–6, este bloco:

```markdown
### Linguagem e gramática

7 — Vocabulário recorrente sem função
8 — Substituição artificial de verbos simples
9 — Paralelismo negativo acrescentado
10 — Tríades decorativas
11 — Variação lexical desnecessária
12 — Intervalos falsos
13 — Agente oculto sem necessidade
```

- [ ] **Step 4: Validar sequência, nomes e ligação direta**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
import re

expected = [
    (7, "Vocabulário recorrente sem função"),
    (8, "Substituição artificial de verbos simples"),
    (9, "Paralelismo negativo acrescentado"),
    (10, "Tríades decorativas"),
    (11, "Variação lexical desnecessária"),
    (12, "Intervalos falsos"),
    (13, "Agente oculto sem necessidade"),
]
reference = Path("skills/refinar-prosa/references/pt-BR/linguagem.md").read_text()
skill = Path("skills/refinar-prosa/SKILL.md").read_text()
readme = Path("README.md").read_text()
assert [(int(n), name) for n, name in re.findall(r"^## (\d+) — (.+)$", reference, re.M)] == expected
for number, name in expected:
    needle = f"{number} — {name}"
    assert skill.count(needle) == 1, ("SKILL.md", needle, skill.count(needle))
    assert readme.count(needle) == 1, ("README.md", needle, readme.count(needle))
assert "[references/pt-BR/linguagem.md](references/pt-BR/linguagem.md)" in skill
print("language routing: ok")
PY
```

Expected: exit code `0` e saída `language routing: ok`.

- [ ] **Step 5: Commitar roteamento e README**

```bash
git add skills/refinar-prosa/SKILL.md README.md
git commit -m "docs: route language patterns"
```

### Task 3: Executar a auditoria integrada

**Files:**
- Test: `.codex-plugin/plugin.json`
- Test: `skills/refinar-prosa/SKILL.md`
- Test: `skills/refinar-prosa/references/pt-BR/conteudo.md`
- Test: `skills/refinar-prosa/references/pt-BR/linguagem.md`
- Test: `README.md`

**Interfaces:**
- Consumes: referência e roteamento das Tasks 1–2.
- Produces: evidência de que o catálogo 1–13 é íntegro e o plugin continua válido.

- [ ] **Step 1: Auditar numeração global e cobertura dos exemplos**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
import re

content = Path("skills/refinar-prosa/references/pt-BR/conteudo.md").read_text()
language = Path("skills/refinar-prosa/references/pt-BR/linguagem.md").read_text()
numbers = [int(n) for n in re.findall(r"^## (\d+) —", content + "\n" + language, re.M)]
assert numbers == list(range(1, 14)), numbers
assert language.count("### Antes") == 7
assert language.count("### Depois") == 7
assert language.count("### Não alterar quando") == 7
for term in ["configuração", "servidor", "token", "log", "equipe de infraestrutura"]:
    assert term in language, term
print("catalog 1-13: ok")
PY
```

Expected: exit code `0` e saída `catalog 1-13: ok`.

- [ ] **Step 2: Auditar falsos positivos, fabricação e termos protegidos**

Run:

```bash
python3 - <<'PY'
from pathlib import Path

text = Path("skills/refinar-prosa/references/pt-BR/linguagem.md").read_text()
required = [
    "Palavra, verbo, pontuação ou construção isolada não comprova um padrão",
    "Não transfira automaticamente",
    "Preserve termos técnicos, nomes próprios, citações",
    "exatamente três requisitos, etapas, arquivos ou resultados",
    "o agente for desconhecido ou irrelevante",
    "O agente não é inferido",
]
missing = [item for item in required if item not in text]
assert not missing, missing
for forbidden in ["sempre remova", "nunca use ser", "lista proibida", "detectores de IA"]:
    assert forbidden.casefold() not in text.casefold(), forbidden
print("false-positive audit: ok")
PY
```

Expected: exit code `0` e saída `false-positive audit: ok`.

- [ ] **Step 3: Executar validadores estruturais**

Run:

```bash
python3 /home/thiago-botelho/.config/orca/codex-accounts/9ae230c7-073c-4dc6-85bc-436aca338b5d/home/skills/.system/skill-creator/scripts/quick_validate.py skills/refinar-prosa
```

Expected: exit code `0` e mensagem de skill válida.

Run o validador de plugins Codex identificado na implementação da #2. Expected:
exit code `0`, manifesto e skill aceitos.

- [ ] **Step 4: Verificar higiene do pacote e diff**

Run:

```bash
rg -n -i 'claude|\.claude-plugin|marketplace\.json|placeholder|\[preencher\]' .codex-plugin skills README.md
```

Expected: exit code `1` e nenhuma saída.

Run:

```bash
git diff --check
git status --short
```

Expected: `git diff --check` sem saída e nenhum arquivo inesperado no status.

- [ ] **Step 5: Commitar eventual ajuste estritamente necessário à validação**

Se e somente se os passos anteriores exigirem correção nos três arquivos em
escopo:

```bash
git add skills/refinar-prosa/references/pt-BR/linguagem.md skills/refinar-prosa/SKILL.md README.md
git commit -m "fix: validate language pattern catalog"
```

Caso não haja correção, não criar commit vazio.
