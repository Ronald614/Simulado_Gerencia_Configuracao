# AGENT.md - Documentacao Tecnica do Sistema e Pipeline do Agente

Este documento descreve a arquitetura, as decisoes tecnicas, os scripts de automacao e as diretrizes de engenharia implementadas pelo agente no projeto de preparacao para a disciplina de Gerencia de Configuracao (IC/UFAM).

---

## 1. Visao Geral e Escopo

O objetivo do sistema e extrair, processar e estruturar o conteudo programatico de apresentacoes em PDF, transcrevendo-os fielmente para Markdown e gerando simulados avaliativos no formato somativo. A aplicacao e acompanhada por uma interface web moderna, reativa e sem necessidade de build, pronta para deploy na Vercel e compartilhamento por endpoints diretos.

### Delimitacao do Conteudo dos Slides
- **`slides/1_git.pdf` (148 paginas)**: Transcrito integralmente. Abrange fundamentos de controle de versao distribuido, ciclo de vida dos arquivos (Working Directory, Staging Area, Repository), manipulacao de branches, o ponteiro `HEAD`, fast-forward merge versus merge commit, resolucao de conflitos, rebase linear, desfazimento com modos de `git reset` (`--soft`, `--mixed`, `--hard`), rastreamento local via `git reflog` e isolamento temporario com `git stash`.
- **`slides/smartnotes.pdf` (175 paginas totais)**: Conforme diretriz estrita do projeto, foram isolados e transcritos **exclusivamente os 35 slides de fundo azul** (identificados no espaco de cores RGB por `[218, 227, 243]`). O conteudo filtrado abrange:
  - Slides 22 a 25: Semantic Versioning (SemVer), regras de incremento de MAJOR, MINOR e PATCH, e operadores de controle de dependencia no `package.json` (`^` versus `~`).
  - Slides 32 a 44: Variaveis de ambiente, principios de Twelve-Factor App, bibliotecas `dotenv` e `envalid`, validacao em tempo de inicializacao (*fail-fast*) via `cleanEnv`, alem de isolamento com `.env.example` e `.gitignore`.
  - Slides 45 a 62: Linters versus Formatadores de codigo, ecossistema comparado entre linguagens, configuracao modular flat (`eslint.config.mjs`) com severidades (`off`, `warn`, `error`), diretivas do `.prettierrc`, extensoes do VS Code e scripts de automacao no `package.json`.
- **`slides/docker.pdf` (47 paginas)**: Descartado e cancelado por orientacao do usuario (nao faz parte do escopo da prova).

---

## 2. Decisoes de Autoria e Disclaimer

Por solicitacao formal, todos os simulados registram explicitamente que:
- **Natureza:** Trata-se de **Simulados Independentes de Estudos** desenvolvidos colaborativamente por estudantes para preparacao da turma.
- **Material de Referencia:** Baseado nos slides e aulas ministradas pelo docente titular da disciplina, Prof. David Fernandes de Oliveira (Instituto de Computacao - IC/UFAM).
- **Finalidade:** Fixacao tecnica de conceitos e treinamento pratico em questoes somativas.

---

## 3. Estrutura do Repositorio

```text
site_estudos/
├── .venv/                         # Ambiente virtual gerenciado via uv (Python 3.14)
├── slides/                        # PDFs originais fornecidos (1_git.pdf, docker.pdf, smartnotes.pdf)
├── transcricoes/                  # Transcricoes higienizadas para leitura e estudo
│   ├── 1_git.md                   # Transcricao completa de Git e GitHub
│   └── smartnotes.md              # Transcricao seletiva dos 35 slides azuis de SmartNotes
├── scripts/                       # Scripts deterministas de automacao
│   ├── transcrever_slides.py      # Extracao vetorial e OCR com filtro de cor azul
│   ├── validar_questoes.py        # Validador de consistencia matematica e integridade
│   └── gerar_provas.py            # Compilador das 3 avaliacoes para Markdown e JSON
├── artefatos/                     # Terceira pasta com os entregaveis oficiais
│   ├── prova_01.md / .json        # Simulado Somativo 01
│   ├── prova_02.md / .json        # Simulado Somativo 02
│   ├── prova_03.md / .json        # Simulado Somativo 03
│   ├── provas.json                # Banco consolidado de todas as questoes
│   └── questoes_somativas.md      # Caderno original de estudo
├── public/                        # Frontend Web pronto para a Vercel
│   ├── index.html                 # Single Page Application reativa com Vue 3, Tailwind e DaisyUI
│   ├── style.css                  # Estilos complementares
│   ├── app.js                     # Logica do cliente (mantido para compatibilidade estatica)
│   └── provas.json                # Base estatica consumida pelo cliente Vue
├── api/                           # Funcoes Serverless da Vercel
│   └── provas.js                  # Endpoint de API REST JSON (/api/provas)
├── vercel.json                    # Configuracao de roteamento e rewrites SPA
├── requirements.txt               # Dependencias congeladas do Python
└── AGENT.md                       # Documentacao tecnica do agente
```

---

## 4. Ambiente Virtual com `uv`

O projeto adota o gerenciador `uv` em substituicao ao ecossistema legado do `pip` tradicional:
- **Criacao do ambiente:**
  ```bash
  uv venv .venv
  ```
- **Instalacao das dependencias do pipeline:**
  ```bash
  uv pip install --python .venv/bin/python pymupdf pillow numpy
  ```
- **Execucao dos scripts atraves do ambiente isolado:**
  ```bash
  .venv/bin/python scripts/transcrever_slides.py
  .venv/bin/python scripts/validar_questoes.py
  .venv/bin/python scripts/gerar_provas.py
  ```

---

## 5. Algoritmo das Questoes Somativas

Cada questao segue a convencao formal do formato somativo:
1. Cada item recebe uma potencia de base 2: `(01), (02), (04), (08), (16)`.
2. A resposta valida de cada questao e **estritamente a soma das proposicoes verdadeiras**.
3. Pela propriedade de unicidade da representacao em numeracao binaria, cada combinacao de itens verdadeiros possui um somatorio unico no intervalo de 0 a 31.
4. Cada questao possui valor atribuido de 2,0 pontos, totalizando 10,0 pontos por simulado.

### Resumo dos Gabaritos Unicos das 3 Provas

| Prova | Q1 | Q2 | Q3 | Q4 | Q5 | Pontuacao Total |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Simulado 01** | Soma: 11 | Soma: 21 | Soma: 29 | Soma: 23 | Soma: 27 | 10,0 pontos |
| **Simulado 02** | Soma: 23 | Soma: 23 | Soma: 13 | Soma: 27 | Soma: 23 | 10,0 pontos |
| **Simulado 03** | Soma: 23 | Soma: 27 | Soma: 19 | Soma: 23 | Soma: 23 | 10,0 pontos |

---

## 6. Arquitetura do Frontend Web (Vercel Ready)

Para proporcionar uma aplicacao leve, sem etapa de compilacao (`zero-build`) e com visual sofisticado, foram combinadas tres tecnologias via CDN:
- **Vue 3 (Standalone CDN):** Gerencia o estado reativo dos checkboxes, o somatorio instantaneo, a alternancia de rotas e o feedback explicativo.
- **Tailwind CSS + DaisyUI (via CDN):** Fornece componentes pre-estilizados prontos (Navbar, Tabs, Badges, Cards, Checkboxes, Stats, Alerts) com suporte a modo escuro nativo (`data-theme="dark"`).
- **Roteamento Vercel (`vercel.json`):**
  - `/` -> Hub central de navegacao e regras.
  - `/prova1` -> Simulado Somativo 01 interativo.
  - `/prova2` -> Simulado Somativo 02 interativo.
  - `/prova3` -> Simulado Somativo 03 interativo.
  - `/api/provas` -> Retorno dos dados em JSON para consumo programmatico.

---

## 7. Instrucoes para Deploy na Vercel e GitHub

### Deploy na Vercel
1. Instale a Vercel CLI (ou conecte o repositorio via painel em vercel.com):
   ```bash
   npx vercel
   ```
2. A configuracao presente no `vercel.json` roteia automaticamente as chamadas sem necessidade de build steps adicionais.

### Versionamento no GitHub
```bash
git init
git add .
git commit -m "feat: plataforma de simulados somativos de gerencia de configuracao"
git branch -M main
git remote add origin <URL_DO_REPOSITORIO>
git push -u origin main
```

---

## 8. Diretrizes Globais Observadas

- **Ausencia Total de Emojis:** Todos os arquivos de codigo, scripts, documentacoes em Markdown, interfaces HTML e respostas foram estritamente validados contra caracteres de emojis.
- **Rigor Tecnico e Terminologia:** Preservacao formal de termos tecnicos universais em ingles (*pipeline*, *commit*, *staging*, *working directory*, *fast-forward*, *rebase*, *detached HEAD*, *linter*, *formatter*, *fail-fast*, *breaking changes*).
