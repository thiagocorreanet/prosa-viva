# Escopo linguístico da primeira versão do Prosa Viva

## Contexto

Esta especificação registra a decisão da issue #19, relacionada à épica #1. O
catálogo, os exemplos e a pesquisa planejada para a primeira versão são voltados
ao português brasileiro. Oferecer revisão completa em outros idiomas sem regras
e avaliações próprias criaria uma promessa que o projeto não consegue validar.

A arquitetura canônica definida na #17 separa o núcleo editorial das referências
localizadas. Esta decisão usa essa separação para tornar a versão inicial
estritamente pt-BR e preparar futuras localidades sem duplicar o contrato de
preservação.

## Decisão

As versões `0.1.x` suportarão oficialmente apenas prosa em português brasileiro.
O Prosa Viva não fará revisão parcial ou “genérica” de outro idioma como fallback.

```text
entrada
  → identificar o idioma da prosa editável
  → pt-BR claro: revisar
  → documento misto: revisar somente segmentos pt-BR
  → idioma não suportado: preservar integralmente
  → idioma ambíguo: preservar até haver confirmação
```

Essa política se aplica à invocação explícita e implícita, nos modos texto
colado, arquivo e embutido.

## Alternativas consideradas

### Português brasileiro apenas — escolhida

Mantém a promessa alinhada às 33 regras, à pesquisa e às avaliações. Evita
aplicar convenções portuguesas a outro idioma e reduz o risco de apagar voz com
heurísticas não testadas.

### Núcleo geral com fallback em outros idiomas

Pareceria útil, mas “regras gerais” como concisão, pontuação e naturalidade
também dependem de idioma e gênero. Sem catálogo e fixtures próprios, o fallback
seria difícil de distinguir de suporte incompleto. Foi rejeitado para a v1.

### Português brasileiro e inglês na v1

Exigiria pesquisa, exemplos, falsos positivos e avaliações independentes para
inglês, praticamente duplicando o escopo antes de validar o produto em pt-BR.
Foi rejeitado para a v1.

## Identificação do idioma

A skill identifica o idioma pela prosa editável colocada no escopo, não por
nomes de variáveis, código, URLs, frontmatter, comandos, dados, títulos de obras
ou citações protegidas.

Sinais considerados em conjunto:

- vocabulário e morfologia predominantes;
- estrutura sintática dos períodos;
- convenções ortográficas observáveis;
- instrução explícita do usuário;
- contexto do documento, quando a amostra isolada for curta.

Não haverá classificador externo, porcentagem de confiança ou chamada de rede.
A identificação é uma triagem conservadora para decidir se é seguro editar. Um
termo estrangeiro, estrangeirismo técnico ou nome próprio não muda sozinho o
idioma do trecho.

## Português brasileiro claro

Quando a prosa estiver claramente em pt-BR, a skill executa o contrato editorial
completo, incluindo os padrões localizados em `references/pt-BR/`.

Variação regional, registro formal, ortografia anterior preservada em citação e
vocabulário técnico não transformam o texto em idioma não suportado. A skill não
exige português padronizado para reconhecer pt-BR.

## Documentos mistos

Em documentos com mais de um idioma:

- revisar somente segmentos de prosa claramente em pt-BR;
- preservar passagens estrangeiras integralmente;
- preservar citações em qualquer idioma;
- preservar código, comandos, dados, links e frontmatter;
- não traduzir transições para conectar trechos;
- não uniformizar aspas, capitalização ou pontuação estrangeira segundo regras
  portuguesas.

Se a fronteira entre segmentos não for segura, o trecho ambíguo permanece
inalterado. A edição do restante do documento pode prosseguir quando os segmentos
pt-BR forem inequívocos e independentes.

## Idioma claramente não suportado

### Texto colado

Não reescrever. Responder brevemente que esta versão do `$refinar-prosa` suporta
somente português brasileiro e que o texto foi preservado.

### Arquivo

Não modificar o arquivo. Informar que nenhuma alteração foi realizada porque a
prosa em escopo não está em pt-BR.

### Embutido

Retornar o texto original sem alterações e sem comentário adicional. Isso
mantém o contrato de “somente texto final” para descrições de PR, commits e
outras composições automáticas.

## Idioma ambíguo

Idioma é ambíguo quando a prosa editável é curta demais, contém apenas termos
compartilhados ou mistura idiomas sem fronteiras confiáveis.

### Texto colado

Não editar. Informar brevemente que não foi possível confirmar pt-BR e pedir que
o usuário identifique o idioma ou forneça mais contexto.

### Arquivo

Não modificar. Resumir que a edição foi interrompida porque o idioma da prosa
não pôde ser identificado com segurança.

### Embutido

Retornar a entrada integralmente inalterada, sem explicação.

## Pedidos de tradução

Tradução não faz parte do `$refinar-prosa`. Se o usuário pedir tradução e
refinamento, a skill não deve traduzir silenciosamente nem tratar o texto de
origem como pt-BR. Em modo conversacional, informa o limite e sugere que o texto
seja traduzido antes da revisão. Em modo embutido, preserva a entrada.

Uma tradução fornecida pelo próprio usuário pode ser revisada normalmente se o
resultado estiver claramente em pt-BR.

## Componentes e responsabilidades

### `skills/refinar-prosa/SKILL.md`

Contém a política completa de triagem, o comportamento por modo e a proibição de
fallback. É a fonte comportamental.

### `skills/refinar-prosa/references/pt-BR/`

Contém apenas regras e exemplos validados para português brasileiro. Nenhuma
referência desse namespace é aplicada a passagem estrangeira.

### `.codex-plugin/plugin.json`

Descrição, palavras-chave e prompts devem declarar pt-BR sem sugerir suporte
genérico a “português” ou inglês.

### `skills/refinar-prosa/agents/openai.yaml`

Descrição curta e prompt padrão devem permanecer alinhados ao suporte exclusivo
a pt-BR. Não contém regra comportamental diferente do `SKILL.md`.

### `README.md`

Documenta idiomas suportados, comportamento previsível para entradas não
suportadas, política de futuras localidades e exemplos dos três modos.

## Fixtures da política linguística

A implementação criará dados de avaliação em:

```text
evals/fixtures/politica-linguistica/
├── inputs.json
├── constraints.json
└── expectations.json
```

As três dimensões permanecem separadas para integração posterior na #15.

Casos mínimos:

1. prosa geral em pt-BR, revisável;
2. pt-BR com regionalismo e estrangeirismo técnico, revisável sem normalizar a
   voz;
3. documento misto com prosa pt-BR, citação inglesa e código;
4. texto colado claramente em inglês, inalterado com aviso;
5. arquivo claramente em espanhol, inalterado e sem escrita;
6. entrada ambígua em modo embutido, devolvida exatamente como recebida;
7. pedido de tradução seguido de refinamento, sem tradução silenciosa.

As restrições verificam substrings protegidas, estruturas, ausência de escrita e
igualdade exata quando aplicável. As expectativas registram ação, tipo de saída
e justificativa sem impor uma redação única para avisos conversacionais.

## Arquitetura para futuras localidades

Uma nova localidade só será oficialmente suportada quando tiver:

- identificador BCP 47 próprio, como `en` ou `es`;
- referências dentro de `references/<locale>/`;
- pesquisa linguística e falsos positivos próprios;
- exemplos originais nesse idioma;
- cobertura na suíte da #15;
- manifesto, prompts e README atualizados na mesma release.

O contrato editorial, os três modos, a preservação factual e a proteção de
estrutura permanecem no `SKILL.md` e não são duplicados por localidade. Não será
criado um segundo plugin apenas para adicionar idioma.

## Auditoria

Antes da saída final, a skill confirma:

- que somente prosa pt-BR foi editada;
- que trechos estrangeiros e ambíguos permanecem intactos;
- que nenhum padrão tipográfico português foi aplicado fora de pt-BR;
- que nenhum pedido de tradução foi executado implicitamente;
- que o modo embutido não acrescentou aviso ao texto preservado;
- que arquivo não suportado não recebeu escrita parcial.

## Validação

A implementação verificará:

1. manifesto, `SKILL.md`, `openai.yaml` e README declaram pt-BR como único
   idioma suportado na v1;
2. não há promessa de revisão em inglês ou fallback genérico;
3. os três modos têm comportamento definido para idioma não suportado e
   ambíguo;
4. documentos mistos protegem citações, código e prosa estrangeira;
5. fixtures separam entradas, restrições e expectativas e cobrem os sete casos;
6. a arquitetura aceita futura pasta de localidade sem duplicar o núcleo;
7. os validadores arquitetural, de skill e de plugin continuam passando.

## Relação com outras issues

- #17 fornece a fonte canônica e o namespace `references/pt-BR/`.
- #3 implementa o contrato editorial e deve incorporar esta política ao definir
  entrada e saída dos três modos.
- #5–#10 implementam somente exemplos e regras pt-BR.
- #15 consumirá as fixtures criadas aqui e ampliará a cobertura comportamental.
- #21 não altera o idioma; apenas testa instalação e atualização.
- #11 documenta esta política depois de #19 e #21 estarem verificadas.

## Fora de escopo

- revisar, traduzir ou avaliar inglês, espanhol ou outro idioma;
- usar serviço externo de detecção de idioma;
- atribuir porcentagem de confiança linguística;
- criar catálogo vazio para futura localidade;
- alterar versão ou adicionar componentes ao plugin;
- implementar o runner completo da suíte #15.
