# Troubleshooting: dificuldades comuns e correções

> Seção de referência com problemas frequentes ao trabalhar com cadernos de fontes. Registre as **suas** ocorrências reais em `docs/engenharia-de-prompts.md`.

| Problema | Como identificar | Correção |
|---|---|---|
| Resposta genérica | Sem citações, texto "de manual" | Restringir a "APENAS as fontes"; selecionar fontes específicas |
| Citação que não sustenta a frase | Clicar na citação e o trecho não confirma | Rodar `checagem-citacoes`; pedir o trecho literal de apoio |
| Fontes harmonizadas demais | IA diz que todas concordam | Prompt `contradicoes`; perguntar por metodologia e época |
| PDF com texto ruim | Trechos truncados ou ilegíveis (colunas, fórmulas) | Preferir a versão HTML do artigo ou colar o texto limpo |
| Resposta longa demais | Excesso de texto | Impor limite (ex.: 150 palavras) e formato |
| Perda de informação no meio | Detalhes do meio do material ignorados | Perguntas mais específicas; dividir em tópicos; selecionar 1 fonte por vez |
| Termo em inglês sem tradução | Glossário misto | Pedir "termo em inglês (tradução) — definição" |
| Resposta desatualizada | Fonte antiga | Adicionar fonte recente e declarar a data na pergunta |

## Checklist antes de confiar numa resposta

1. Há citação em cada afirmação importante?
2. Abri pelo menos uma citação e ela sustenta a frase?
3. Testei uma pergunta cuja resposta **não** está nas fontes?
4. Comparei com outra fonte ou com a versão original do artigo?
