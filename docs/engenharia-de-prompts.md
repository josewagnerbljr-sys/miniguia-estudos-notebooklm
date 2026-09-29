# Engenharia de Prompts e Cicatrizes

Este documento registra o **raciocínio por trás dos resultados**: hipótese, variações de prompt, resposta, avaliação e correção.

## Método (ciclo HAVAC)

1. **H**ipótese: o que espero obter e por quê.
2. **A**ção: prompt v1 (simples), depois v2/v3 com restrições.
3. **V**erificação: conferir citações clicando nas fontes do NotebookLM.
4. **A**valiação: nota 0 a 3 em fidelidade, completude e utilidade.
5. **C**icatriz: o que deu errado e o ajuste aplicado.

## Rubrica de avaliação

| Nota | Fidelidade às fontes | Completude | Utilidade para estudo |
|---|---|---|---|
| 0 | Contém afirmações sem suporte | Ignora partes do pedido | Inutilizável |
| 1 | Suporte parcial | Cobre metade | Exige muito retrabalho |
| 2 | Suportada, com pequenos deslizes | Cobre quase tudo | Usável com ajustes |
| 3 | Totalmente suportada e citada | Completa | Pronta para revisar |

## Registro de experimentos

> **Como preencher:** execute cada prompt no seu caderno, cole a resposta resumida, avalie e escreva a cicatriz real. Substitua os campos `_preencher_`. As colunas "Hipótese" já estão prontas para guiar o teste.

### E01: Definição do tema

| Campo | Conteúdo |
|---|---|
| Hipótese | Um pedido vago retorna resumo genérico e sem estrutura. |
| Prompt v1 | `Explique RAG.` |
| Prompt v2 | Prompt `resumo-estruturado` da biblioteca (nível iniciante). |
| Resposta obtida | _preencher_ |
| Referências (citações) | _preencher_ |
| Nota v1 / v2 | _preencher_ |
| Cicatriz e ajuste | _preencher_ |

### E02: Comparar Naive versus Advanced RAG

| Campo | Conteúdo |
|---|---|
| Hipótese | Sem pedir tabela e fonte por célula, a IA mistura conceitos. |
| Prompt v1 | `Qual a diferença entre Naive RAG e Advanced RAG?` |
| Prompt v2 | Prompt `comparativo` com a="Naive RAG", b="Advanced RAG". |
| Resposta obtida | _preencher_ |
| Nota v1 / v2 | _preencher_ |
| Cicatriz e ajuste | _preencher_ |

### E03: Contradições entre fontes

| Campo | Conteúdo |
|---|---|
| Hipótese | A IA tende a harmonizar fontes; é preciso pedir divergências explicitamente. |
| Prompt v1 | `As fontes concordam entre si?` |
| Prompt v2 | Prompt `contradicoes` com tema="contexto longo versus recuperação". |
| Resposta obtida | _preencher_ |
| Nota v1 / v2 | _preencher_ |
| Cicatriz e ajuste | _preencher_ |

### E04: Teste anti-alucinação

| Campo | Conteúdo |
|---|---|
| Hipótese | Perguntas sobre algo ausente das fontes revelam se a IA admite não saber. |
| Prompt v1 | Pergunta sobre um framework que **não** está nas fontes. |
| Prompt v2 | Prompt `checagem-citacoes` com uma afirmação falsa proposital. |
| Resposta obtida | _preencher_ |
| Nota v1 / v2 | _preencher_ |
| Cicatriz e ajuste | _preencher_ |

### E05: Glossário

| Campo | Conteúdo |
|---|---|
| Hipótese | Sem limite de palavras e ordem, o glossário fica verboso e desorganizado. |
| Prompt v1 | `Faça um glossário de RAG.` |
| Prompt v2 | Prompt `glossario` com n=25. |
| Resposta obtida | _preencher_ |
| Nota v1 / v2 | _preencher_ |
| Cicatriz e ajuste | _preencher_ |

### E06: Autoavaliação

| Campo | Conteúdo |
|---|---|
| Hipótese | Quiz socrático (uma pergunta por vez) retém mais do que uma lista de perguntas. |
| Prompt v1 | `Me faça perguntas sobre RAG.` |
| Prompt v2 | Prompt `quiz-socratico` com n=8. |
| Resposta obtida | _preencher_ |
| Nota v1 / v2 | _preencher_ |
| Cicatriz e ajuste | _preencher_ |

## Técnicas de prompt que valem testar

- **Delimitar o escopo:** "Usando APENAS as fontes do caderno".
- **Permitir a saída honesta:** "Se não constar nas fontes, diga".
- **Exigir formato:** tabela, passos numerados, limite de palavras.
- **Pedir citação por afirmação** e depois auditar com `checagem-citacoes`.
- **Selecionar fontes** no painel do NotebookLM para isolar o efeito de cada uma.
- **Iterar em duas etapas:** primeiro extrair, depois sintetizar.

## Ferramenta de apoio

```bash
python tools/prompt_lib.py list
python tools/prompt_lib.py render comparativo --var a="Naive RAG" --var b="Advanced RAG"
```
