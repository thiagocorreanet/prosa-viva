---
name: refinar-prosa
description: "Use para revisar e reescrever prosa em português brasileiro, em texto colado ou arquivos, melhorando clareza e naturalidade sem alterar fatos, estrutura protegida ou voz."
---

# Refinar prosa

Revise somente a prosa em português brasileiro que o usuário colocar no escopo.
Melhore clareza, concisão, ritmo e naturalidade sem trocar o significado pela
forma.

## Fluxo

1. Confirme que há texto ou um arquivo legível para revisar.
2. Identifique se a prosa está em português brasileiro.
3. Preserve fatos, nomes, números, datas, citações, ressalvas e grau de certeza.
4. Preserve a voz, o registro e as escolhas incomuns que sejam intencionais.
5. Edite somente o necessário; mantenha o original quando não houver melhoria
   útil.
6. Compare a revisão com a fonte e remova qualquer informação acrescentada.
7. Entregue somente o texto revisado, salvo quando o usuário pedir explicações.

## Conteúdo protegido

Ao editar arquivos, preserve frontmatter, links, tabelas, blocos de código e
outros trechos não textuais. Não altere citações nem passagens em outro idioma.

Em documentos mistos, revise apenas a prosa em português brasileiro. Se o texto
estiver claramente em outro idioma, não o modifique; informe brevemente que esta
versão suporta somente pt-BR.

## Limites

- Não invente fatos, fontes, exemplos, experiências ou opiniões.
- Não transforme incerteza em certeza.
- Não prometa detecção de texto gerado por IA.
- Não apresente a revisão como verificação factual ou revisão técnica,
  jurídica ou acadêmica especializada.
- Se a entrada estiver ausente, o arquivo não puder ser lido ou as instruções
  impedirem uma revisão segura, explique o problema antes de editar.

## Exemplos de uso

```text
Use $refinar-prosa para revisar o texto abaixo sem alterar os fatos.

[texto em português brasileiro]
```

```text
Use $refinar-prosa para revisar docs/guia.md e preservar sua estrutura.
```
