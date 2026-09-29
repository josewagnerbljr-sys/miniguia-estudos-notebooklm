# Glossário

| Termo | Definição | Fonte |
|---|---|---|
| RAG | Geração aumentada por recuperação: o modelo responde usando trechos buscados numa base externa. | F1 |
| Memória paramétrica | Conhecimento armazenado nos pesos do modelo. | F1 |
| Memória não paramétrica | Conhecimento externo consultável (índice de documentos). | F1 |
| Chunk | Fragmento de documento indexado e recuperado como unidade. | F2 |
| Embedding | Vetor numérico que representa o significado de um texto. | F2 |
| Índice vetorial | Estrutura que busca vetores por similaridade (ex.: pgvector, ChromaDB). | F2 |
| Top-k | Quantidade de trechos mais similares devolvidos pela busca. | F2 |
| Busca densa | Recuperação por similaridade de embeddings. | F2 |
| Busca lexical (BM25) | Recuperação por correspondência de termos. | F2 |
| Busca híbrida | Combinação de busca lexical e densa. | F2 |
| Reranking | Reordenação dos candidatos por um modelo mais preciso. | F2 |
| Reescrita de consulta | Reformular a pergunta para melhorar a recuperação. | F2 |
| Naive RAG | Pipeline simples: indexar, recuperar, gerar. | F2 |
| Advanced RAG | RAG com otimizações antes e depois da recuperação. | F2 |
| Modular RAG | Arquitetura com módulos combináveis e roteamento. | F2 |
| Alucinação | Resposta fluente porém não sustentada por fatos ou fontes. | F1, F4 |
| Grounding (ancoragem) | Fundamentar a resposta em evidências recuperadas. | F4 |
| Faithfulness | Grau em que a resposta é sustentada pelo contexto. | F4 |
| Answer relevancy | Grau em que a resposta atende à pergunta. | F4 |
| Context precision | Proporção de contexto útil nas melhores posições. | F4 |
| Context recall | Cobertura do que era necessário no contexto recuperado. | F4 |
| Lost in the Middle | Queda de desempenho quando o dado relevante fica no meio do contexto longo. | F3 |
| Janela de contexto | Limite de tokens que o modelo processa de uma vez. | F3 |
| Self-RAG | Modelo que decide quando recuperar e critica suas próprias saídas. | F5 |
| Token de reflexão | Marcador especial que sinaliza necessidade de busca ou avaliação de suporte. | F5 |
| Citação | Referência que liga cada afirmação ao trecho de origem. | NotebookLM |

> Termos e atribuições de fonte devem ser conferidos no NotebookLM após o upload.
