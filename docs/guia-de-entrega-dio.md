# Guia de entrega na DIO (passo a passo)

## 1. Criar o repositório e enviar o projeto

```bash
cd miniguia-estudos-notebooklm
git init -b main
git add .
git commit -m "feat: miniguia de estudos RAG com NotebookLM"
git remote add origin https://github.com/josewagnerbljr-sys/miniguia-estudos-notebooklm.git
git push -u origin main
```

Crie antes o repositório vazio no GitHub (sem README inicial), com o nome `miniguia-estudos-notebooklm`.

## 2. Preencher a parte que só você pode fazer

1. Criar o caderno no NotebookLM e subir as 5 fontes de `sources/fontes.yaml`.
2. Executar os experimentos E01 a E06 e preencher `docs/engenharia-de-prompts.md` com respostas, citações, notas e cicatrizes **reais**.
3. Conferir o glossário e o miniguia clicando nas citações.
4. Se o compartilhamento estiver disponível, colocar o link do caderno no README.

## 3. Validar localmente

```bash
pip install -r requirements.txt
python tools/validate_repo.py
```

## 4. Entregar

1. Copie a URL principal do repositório.
2. Na página do desafio na DIO, clique em entregar.
3. Cole o link e escreva uma descrição curta (modelo abaixo).

**Modelo de descrição:** "Caderno temático no NotebookLM sobre RAG (Retrieval-Augmented Generation), com 5 fontes abertas, biblioteca de prompts versionada e validada por CI, registro de experimentos com troubleshooting, glossário de 26 termos e miniguia de estudo com resumos e checklist de revisão."
