#!/usr/bin/env python3
"""
Gerador automatizado de 3 provas no formato somativo em Markdown e JSON.
Projetado para consumo direto por aplicacoes web (fastsite) e estudo.

Disciplina: Gerencia de Configuracao (IC/UFAM)
Conteudo coberto:
- Git e GitHub (1_git.pdf)
- SmartNotes slides azuis (SemVer, Variaveis de Ambiente, Envalid, ESLint, Prettier)
"""

import json
from pathlib import Path

PROVAS_DATA = [
    {
        "id": "prova_01",
        "titulo": "Simulado Somativo 01 - Preparacao para a Prova de Gerencia de Configuracao",
        "disciplina": "Gerencia de Configuracao",
        "material_referencia": "Aulas e Slides do Prof. David Fernandes de Oliveira (IC/UFAM)",
        "elaboracao": "Simulado Independente de Estudos para a Prova",
        "pontuacao_total": 10.0,
        "instrucoes": "Cada questao contem 5 proposicoes com valores binarios (01, 02, 04, 08, 16). A resposta corresponde a soma exclusiva das proposicoes verdadeiras. Cada questao vale 2,0 pontos.",
        "questoes": [
            {
                "numero": 1,
                "tema": "Git - Arquitetura, Fundamentos e os Tres Estados do Ciclo de Vida",
                "pontos": 2.0,
                "enunciado": "Com relacao a arquitetura dos sistemas de controle de versao e aos conceitos fundamentais de funcionamento do Git, analise as proposicoes a seguir:",
                "proposicoes": [
                    {
                        "valor": 1,
                        "texto": "A execucao do comando git commit -m 'mensagem' consolida as modificacoes diretamente no servidor remoto (como GitHub ou GitLab), sendo desnecessario executar o comando git push para sincronizacao com a equipe.",
                        "correto": False,
                        "justificativa": "O comando git commit opera estritamente no repositorio local. O envio dos commits locais para o servidor remoto exige o comando de rede git push (1_git.pdf)."
                    },
                    {
                        "valor": 2,
                        "texto": "Diferentemente dos Sistemas de Controle de Versao Centralizados (como CVS ou Subversion), nos quais a indisponibilidade do servidor central bloqueia o registro de versoes pelos desenvolvedores, o Git fundamenta-se em uma arquitetura distribuida, onde cada clone local contem uma copia integral do repositorio com todo o seu historico.",
                        "correto": True,
                        "justificativa": "No modelo centralizado, a indisponibilidade do servidor impede qualquer gravacao de historico pela equipe; no Git distribuido, cada cliente possui um repositorio completo e opera de forma autonoma offline (1_git.pdf)."
                    },
                    {
                        "valor": 4,
                        "texto": "O Git estrutura o ciclo de vida dos arquivos em tres estados fundamentais: Working Directory (diretorio de trabalho contendo os arquivos modificados), Staging Area / Index (area de preparacao onde as alteracoes sao selecionadas para o proximo commit) e Repository / .git directory (banco de objetos onde os snapshots confirmados sao gravados de maneira permanente).",
                        "correto": True,
                        "justificativa": "Essa triade constitui o fluxo operacional central do Git, dividindo o ciclo de vida entre edicao local, preparacao de commits e persistencia definitiva no banco de dados do Git (1_git.pdf)."
                    },
                    {
                        "valor": 8,
                        "texto": "A inclusao de um padrao de arquivo no .gitignore remove automaticamente e de forma retroativa os arquivos correspondentes que ja haviam sido comitados no historico do repositorio.",
                        "correto": False,
                        "justificativa": "O .gitignore atua somente sobre arquivos nao rastreados (untracked). Arquivos ja comitados permanecem no historico e precisam ser removidos do indice via git rm --cached (1_git.pdf)."
                    },
                    {
                        "valor": 16,
                        "texto": "O arquivo .gitignore e utilizado para listar padroes de nomes de arquivos e diretorios que nao devem ser rastreados pelo Git (como node_modules/, logs e arquivos de segredos locais), devendo ele proprio ser comitado no repositorio para garantir a padronizacao das exclusoes entre todos os colaboradores.",
                        "correto": True,
                        "justificativa": "O .gitignore define padroes ignorados pelo versionador e deve ser integrado ao repositorio para que toda a equipe adote as mesmas exclusoes de dependencias e credenciais (1_git.pdf e smartnotes.pdf)."
                    }
                ]
            },
            {
                "numero": 2,
                "tema": "Git - Ramificacao (Branches), Ponteiro HEAD e Conflitos de Integracao",
                "pontos": 2.0,
                "enunciado": "Em relacao ao mecanismo de ramificacao, ponteiros de navegacao e resolucao de conflitos de merge no Git, avalie as proposicoes:",
                "proposicoes": [
                    {
                        "valor": 1,
                        "texto": "No Git, uma branch nao e uma duplicacao fisica dos arquivos do projeto no disco, mas sim um ponteiro movel de baixo custo computacional que referencia um commit especifico na arvore historica.",
                        "correto": True,
                        "justificativa": "Uma branch e apenas uma referencia de texto de 41 bytes contendo o hash do commit apontado, permitindo criacao e chaveamento instantaneos (1_git.pdf)."
                    },
                    {
                        "valor": 2,
                        "texto": "O ponteiro HEAD referencia obrigatoriamente um commit hospedado no repositorio remoto origin, sendo tecnicamente impossivel configurar o HEAD para apontar diretamente para um commit local sem vincular a uma branch nominal.",
                        "correto": False,
                        "justificativa": "O HEAD referencia a branch ou commit local ativo. Ao apontar diretamente para um commit (via git switch --detach <commit>), o Git entra no estado de Detached HEAD localmente (1_git.pdf)."
                    },
                    {
                        "valor": 4,
                        "texto": "Quando duas branches realizam alteracoes em arquivos distintos ou em trechos nao sobrepostos do mesmo arquivo, o Git nao consegue unificar as alteracoes de forma automatica, gerando compulsoriamente um conflito de merge.",
                        "correto": False,
                        "justificativa": "O Git unifica alteracoes em arquivos distintos ou regioes distintas do mesmo arquivo de modo automatico via three-way merge, gerando conflito apenas em colisoes na mesma linha (1_git.pdf)."
                    },
                    {
                        "valor": 8,
                        "texto": "A operacao de mesclagem do tipo Fast-Forward ocorre quando a branch de destino nao possui commits divergentes em relacao a branch integrada, permitindo ao Git simplesmente deslocar o ponteiro da branch de destino diretamente para o topo da branch mesclada, sem a criacao de um novo commit de merge.",
                        "correto": True,
                        "justificativa": "Na ausencia de bifurcacao divergente no historico, o Git apenas avanca o ponteiro da branch destino linearmente ate a ponta da branch mesclada (1_git.pdf)."
                    },
                    {
                        "valor": 16,
                        "texto": "Durante a ocorrencia de um conflito de merge, o Git inclui marcadores visuais no arquivo afetado (como <<<<<<< HEAD, ======= e >>>>>>> <branch>), cabendo ao desenvolvedor inspecionar o arquivo, reconciliar o conteudo desejado, remover os delimitadores e executar git add para assinalar a resolucao do conflito.",
                        "correto": True,
                        "justificativa": "Os delimitadores visuais marcam as duas versoes conflitantes. A resolucao manual requer correcao do texto, remocao dos marcadores e adicao ao index via git add (1_git.pdf)."
                    }
                ]
            },
            {
                "numero": 3,
                "tema": "Git - Rebase, Modos de Reset, Reflog e Stash",
                "pontos": 2.0,
                "enunciado": "Sobre tecnicas avancadas de integracao de codigo, modificacao de historico e recuperacao de estados no Git, julgue as proposicoes:",
                "proposicoes": [
                    {
                        "valor": 1,
                        "texto": "O comando git rebase e uma pratica recomendada e segura para ser executada em branches publicas e compartilhadas por varios membros da equipe (como a branch main no servidor remoto), uma vez que nao afeta a rastreabilidade dos colaboradores externos.",
                        "correto": False,
                        "justificativa": "A regra de ouro proibe rebase em branches publicas: alterar hashes de commits ja baixados por outros colaboradores gera graves problemas de divergencia historica (1_git.pdf)."
                    },
                    {
                        "valor": 2,
                        "texto": "Enquanto o git merge preserva a cronologia e a topologia original das ramificacoes gerando commits de integracao (merge commits), o git rebase reaplica linearmente os commits de uma branch sobre o topo de outra, alterando os hashes SHA-1 dos commits movidos e resultando em um historico linear sem bifurcacoes visuais.",
                        "correto": True,
                        "justificativa": "O rebase gera novos commits reaplicados no topo da base, gerando novos hashes e garantindo grafo linear em contraposicao ao historico topologico do merge (1_git.pdf)."
                    },
                    {
                        "valor": 4,
                        "texto": "O comando git reset --soft HEAD~1 desloca o ponteiro da branch corrente de volta para o commit pai imediato, mantendo intactas as alteracoes nos arquivos do projeto e conservando-as preparadas na Staging Area para um novo commit.",
                        "correto": True,
                        "justificativa": "O modo --soft retrocede a ponta da branch sem tocar no indice nem na arvore de trabalho, deixando tudo em staging pronto para commit (1_git.pdf)."
                    },
                    {
                        "valor": 8,
                        "texto": "O utilitario git reflog registra a sequencia cronologica local de todas as alteracoes sofridas pelo ponteiro HEAD, constituindo um mecanismo eficaz para restaurar commits orfaos apos a execucao acidental de um git reset --hard.",
                        "correto": True,
                        "justificativa": "O reflog rastreia toda mudanca de ponteiro local e retem os hashes de commits aparentemente perdidos, permitindo recupera-los com facilidade (1_git.pdf)."
                    },
                    {
                        "valor": 16,
                        "texto": "O comando git stash isola e salva temporariamente em uma pilha de contexto local as alteracoes pendentes no Working Directory e na Staging Area, permitindo que o desenvolvedor alterne de branch com a area de trabalho limpa sem necessidade de realizar commits preliminares ou descartar codigo.",
                        "correto": True,
                        "justificativa": "O stash armazena modificacoes em andamento em uma pilha local, limpando o diretorio de trabalho para alternancia rapida de branches (1_git.pdf)."
                    }
                ]
            },
            {
                "numero": 4,
                "tema": "SmartNotes - Semantic Versioning (SemVer) e Gerenciamento de Dependencias",
                "pontos": 2.0,
                "enunciado": "Considerando a especificacao de Versionamento Semantico (SemVer) e as declaracoes de dependencias gerenciadas no package.json de aplicacoes Node.js, analise as proposicoes:",
                "proposicoes": [
                    {
                        "valor": 1,
                        "texto": "De acordo com o SemVer (MAJOR.MINOR.PATCH), a transicao de versao de 5.2.0 para 6.0.0 comunica formalmente aos consumidores do pacote que modificacoes incompativeis de API (breaking changes) foram introduzidas.",
                        "correto": True,
                        "justificativa": "A elevacao de MAJOR sinaliza quebras de compatibilidade retroativa e mudancas na assinatura publica do software (smartnotes.pdf)."
                    },
                    {
                        "valor": 2,
                        "texto": "Ao especificar a dependencia 'express': '^5.2.1', o operador circunflexo (^) autoriza o comando npm update a instalar atualizacoes dentro da mesma versao MAJOR (permitindo a instalacao automatica de versoes como 5.2.2, 5.3.0 ou 5.5.3), porem bloqueia a instalacao da versao 6.0.0.",
                        "correto": True,
                        "justificativa": "O circunflexo permite atualizacoes de MINOR e PATCH na versao especificada, impedindo a subida para o proximo MAJOR (smartnotes.pdf)."
                    },
                    {
                        "valor": 4,
                        "texto": "No SemVer, a adicao de novas funcionalidades compativeis com as interfaces vigentes exige a atualizacao do digito MINOR, momento no qual o identificador de PATCH e reiniciado em zero (ex.: a versao 5.1.4 evolui para 5.2.0).",
                        "correto": True,
                        "justificativa": "Incrementos MINOR acrescentam funcionalidades retrocompativeis e exigem a reinicializacao do digito PATCH para zero (smartnotes.pdf)."
                    },
                    {
                        "valor": 8,
                        "texto": "Caso uma dependencia esteja declarada sob a sintaxe 'express': '~5.2.1', a execucao do comando npm update permitira a atualizacao para correcoes de bugs como 5.2.3 ou 5.2.9, mas impedira a instalacao da versao 5.3.0.",
                        "correto": True,
                        "justificativa": "O operador ~ trava a versao no nivel minor 5.2, aceitando somente incrementos no digito patch 5.2.x (smartnotes.pdf)."
                    },
                    {
                        "valor": 16,
                        "texto": "A utilizacao do operador til (~) na declaracao 'express': '~5.2.1' confere maior liberdade de atualizacao que o operador circunflexo (^), pois o til autoriza tanto novas versoes MINOR quanto novas versoes MAJOR no comando npm update.",
                        "correto": False,
                        "justificativa": "O til e mais conservador e restrito que o circunflexo; ele permite exclusivamente atualizacoes de PATCH dentro do mesmo MINOR (smartnotes.pdf)."
                    }
                ]
            },
            {
                "numero": 5,
                "tema": "SmartNotes - Variaveis de Ambiente, Envalid e Qualidade de Codigo (ESLint e Prettier)",
                "pontos": 2.0,
                "enunciado": "A respeito de gestao de variaveis de ambiente, validacao de esquemas de configuracao e ferramentas de qualidade de codigo no ecossistema Node.js/TypeScript, julgue as proposicoes:",
                "proposicoes": [
                    {
                        "valor": 1,
                        "texto": "Variaveis de ambiente representam configuracoes de execucao (como credenciais, portas e chaves criptograficas) que devem ser definidas em arquivos locais nao versionados (como .env), os quais devem constar obrigatoriamente no .gitignore, mantendo-se no repositorio um arquivo .env.example para documentar as variaveis requeridas.",
                        "correto": True,
                        "justificativa": "Configuracoes sensiveis residem em .env excluido do Git, enquanto .env.example serve como gabarito publico de variaveis para a equipe (smartnotes.pdf)."
                    },
                    {
                        "valor": 2,
                        "texto": "O ESLint e o Prettier exercem papeis identicos e concorrentes: o ESLint e responsavel exclusivamente pela estilizacao de espacos e quebras de linha visuais, ao passo que o Prettier e a ferramenta encarregada de fazer a analise semantica profunda e deteccao de bugs no codigo-fonte.",
                        "correto": False,
                        "justificativa": "Os papeis sao opostos: o ESLint e um Linter de analise estatica e deteccao de bugs/sintaxe; o Prettier e estritamente um Formatador de codigo visual (smartnotes.pdf)."
                    },
                    {
                        "valor": 4,
                        "texto": "O pacote envalid fornece o metodo cleanEnv, que viabiliza a implementacao de uma validacao estrita em tempo de inicializacao (fail-fast), interrompendo imediatamente o processo com erro descritivo caso o arquivo .env nao forneca as variaveis obrigatorias ou caso os dados nao correspondam aos validadores definidos (como str() ou port()).",
                        "correto": True,
                        "justificativa": "O cleanEnv valida tipagem e presenca de variaveis antes que o servidor suba, lancando excecao caso as regras sejam violadas (smartnotes.pdf)."
                    },
                    {
                        "valor": 8,
                        "texto": "No formato moderno de configuracao modular do ESLint (eslint.config.mjs), as regras individuais podem ser ajustadas explicitamente com tres niveis de severidade padronizados: 'off' (desativa a regra), 'warn' (emite advertencia sem falhar a validacao) e 'error' (emite erro impeditivo de validacao).",
                        "correto": True,
                        "justificativa": "As severidades oficiais no ESLint sao off, warn e error, permitindo dosar o rigor da analise por regra (smartnotes.pdf)."
                    },
                    {
                        "valor": 16,
                        "texto": "No arquivo .prettierrc, diretivas como 'printWidth': 150, 'singleQuote': true, 'semi': true e 'arrowParens': 'avoid' configuram o comportamento do formatador de codigo, o qual pode ser integrado a editores como o VS Code para reformatar os arquivos automaticamente a cada evento de salvamento.",
                        "correto": True,
                        "justificativa": "O .prettierrc padroniza as regras estilisticas e sua extensao no VS Code formata o codigo automaticamente ao salvar (smartnotes.pdf)."
                    }
                ]
            }
        ]
    },
    {
        "id": "prova_02",
        "titulo": "Simulado Somativo 02 - Preparacao para a Prova de Gerencia de Configuracao",
        "disciplina": "Gerencia de Configuracao",
        "material_referencia": "Aulas e Slides do Prof. David Fernandes de Oliveira (IC/UFAM)",
        "elaboracao": "Simulado Independente de Estudos para a Prova",
        "pontuacao_total": 10.0,
        "instrucoes": "Cada questao contem 5 proposicoes com valores binarios (01, 02, 04, 08, 16). A resposta corresponde a soma exclusiva das proposicoes verdadeiras. Cada questao vale 2,0 pontos.",
        "questoes": [
            {
                "numero": 1,
                "tema": "Git - Configuracao de Identidade, Inicializacao e Semantica de Commits",
                "pontos": 2.0,
                "enunciado": "A respeito dos passos iniciais de configuracao de ambiente no Git e boas praticas de criacao de historico, analise as proposicoes:",
                "proposicoes": [
                    {
                        "valor": 1,
                        "texto": "A utilizacao do comando git add . adiciona compulsoriamente todos os arquivos do computador ao commit, ignorando quaisquer regras declaradas no arquivo .gitignore.",
                        "correto": False,
                        "justificativa": "O comando git add . respeita estritamente os filtros definidos no .gitignore, indexando somente arquivos rastreaveis nao ignorados (1_git.pdf)."
                    },
                    {
                        "valor": 2,
                        "texto": "Apos a instalacao do Git, a configuracao de user.name e user.email via comando git config e essencial, pois o Git incorpora essas informacoes como metadados imutaveis de autoria em cada commit gerado.",
                        "correto": True,
                        "justificativa": "O Git vincula permanentemente nome e email a cada commit para assegurar a rastreabilidade e responsabilidade dos autores (1_git.pdf)."
                    },
                    {
                        "valor": 4,
                        "texto": "O comando git init cria um diretorio oculto denominado .git no diretorio raiz do projeto, responsavel por armazenar todos os metadados, configuracoes, objetos blob, arvores e o historico integral de commits.",
                        "correto": True,
                        "justificativa": "O diretorio .git e a base interna do repositorio Git onde reside toda a estrutura do versionamento (1_git.pdf)."
                    },
                    {
                        "valor": 8,
                        "texto": "A mensagem de commit deve deixar claro o proposito da mudanca no historico do codigo (ex.: 'Corrige calculo de juros em faturas vencidas'), sendo mensagens como 'ajustes', 'fix' ou 'funcionou agora' consideradas pouco uteis.",
                        "correto": True,
                        "justificativa": "Mensagens informativas descrevem o que foi feito e por que, facilitando a leitura do git log; mensagens genericas nao ajudam a entender o historico (1_git.pdf, secao Mensagens de Commit)."
                    },
                    {
                        "valor": 16,
                        "texto": "O comando git status e a ferramenta primordial para inspecionar quais arquivos foram modificados no Working Directory, quais estao preparados na Staging Area e quais estao desprovidos de rastreamento (untracked).",
                        "correto": True,
                        "justificativa": "O git status exibe com exatidao o estado das tres areas e arquivos nao monitorados pelo controle de versao (1_git.pdf)."
                    }
                ]
            },
            {
                "numero": 2,
                "tema": "Git - Rastreamento, Analise de Diffs e Visualizacao de Topologia com Git Log",
                "pontos": 2.0,
                "enunciado": "Sobre tecnicas de inspecao de diferencas e historico de commits no Git, julgue as afirmacoes:",
                "proposicoes": [
                    {
                        "valor": 1,
                        "texto": "O comando git diff sem argumentos adicionais exibe as diferencas pontuais entre o Working Directory e a Staging Area, isto e, as alteracoes feitas nos arquivos que ainda nao foram preparadas para commit.",
                        "correto": True,
                        "justificativa": "Por padrao, git diff compara o diretorio de trabalho com o indice; para comparar o indice com o ultimo commit usa-se --staged (1_git.pdf)."
                    },
                    {
                        "valor": 2,
                        "texto": "A execucao de git log --oneline resume cada commit em uma unica linha composta pelo hash abreviado e pelo texto da primeira linha da mensagem de commit.",
                        "correto": True,
                        "justificativa": "A flag --oneline condensa a exibicao para proporcionar uma visualizacao rapida do historico recente (1_git.pdf)."
                    },
                    {
                        "valor": 4,
                        "texto": "O comando git diff --staged e equivalente a git commit --amend, efetuando a substituicao automatica do commit anterior sem necessidade de intervencao do usuario.",
                        "correto": False,
                        "justificativa": "git diff --staged apenas visualiza as alteracoes indexadas no staging em comparacao com o HEAD; nao altera nem cria commits (1_git.pdf)."
                    },
                    {
                        "valor": 8,
                        "texto": "O modificador --graph no comando git log renderiza uma representacao textual em arte ASCII das ramificacoes e juncoes da arvore de commits, permitindo compreender a topologia de branches mescladas.",
                        "correto": True,
                        "justificativa": "O --graph desenha graficamente a convergencia e divergencia de branches e commits de merge (1_git.pdf)."
                    },
                    {
                        "valor": 16,
                        "texto": "Linhas iniciadas com o caractere cerquilha (#) no arquivo .gitignore sao interpretadas como comentarios pelo Git e desconsideradas na definicao dos padroes de exclusao.",
                        "correto": True,
                        "justificativa": "Linhas com '#' no .gitignore sao comentarios explicativos que documentam os motivos de exclusao de pastas e arquivos (1_git.pdf)."
                    }
                ]
            },
            {
                "numero": 3,
                "tema": "Git - Repositorios Remotos, Upstream Tracking, Git Fetch e Git Pull",
                "pontos": 2.0,
                "enunciado": "Em relacao a integracao de repositorios locais com servidores remotos (GitHub/GitLab), avalie as proposicoes:",
                "proposicoes": [
                    {
                        "valor": 1,
                        "texto": "O comando git fetch busca os objetos e referencias do repositorio remoto e os incorpora compulsoriamente a branch local de trabalho, sobrescrevendo quaisquer alteracoes nao salvas do usuario.",
                        "correto": False,
                        "justificativa": "O git fetch apenas baixa dados para o repositorio local atualizando remote-tracking branches (como origin/main); ele nao altera os arquivos do working directory nem a branch local corrente (1_git.pdf)."
                    },
                    {
                        "valor": 2,
                        "texto": "Um repositorio Git requer conexao permanente e estavel com a internet para executar operacoes como git commit, git branch, git log e git reset.",
                        "correto": False,
                        "justificativa": "Sendo distribuido, todas as operacoes de commit, criacao de branches, consulta de log e reset sao puramente locais e offline (1_git.pdf)."
                    },
                    {
                        "valor": 4,
                        "texto": "O comando git clone cria um repositorio local identico ao remoto, configurando automaticamente um vinculo de remote denominado origin e baixando todos os branches e historico existentes.",
                        "correto": True,
                        "justificativa": "O clone copia o repositorio integral e estabelece origin como apelido padrao do endereco remoto (1_git.pdf)."
                    },
                    {
                        "valor": 8,
                        "texto": "O comando git pull e essencialmente uma combinacao logica sequencial de duas operacoes do Git: um git fetch seguido por um git merge da branch rastreada correspondente.",
                        "correto": True,
                        "justificativa": "O git pull sincroniza os metadados remotos (fetch) e imediatamente mescla as alteracoes na branch local ativa (merge) (1_git.pdf)."
                    },
                    {
                        "valor": 16,
                        "texto": "O parametro -u (ou --set-upstream) no comando git push -u origin <branch> estabelece uma ligacao direta de rastreamento entre a branch local e a branch remota, simplificando os proximos comandos para apenas git push ou git pull.",
                        "correto": True,
                        "justificativa": "A flag -u configura a associacao upstream permanente para aquela branch (1_git.pdf)."
                    }
                ]
            },
            {
                "numero": 4,
                "tema": "SmartNotes - Principios 12-Factor, Variaveis de Ambiente e Biblioteca Dotenv",
                "pontos": 2.0,
                "enunciado": "A respeito do armazenamento de configuracoes de aplicacao e do uso do pacote dotenv em projetos Node.js, analise as proposicoes:",
                "proposicoes": [
                    {
                        "valor": 1,
                        "texto": "Uma opcao para definir variaveis de ambiente e utilizar arquivos nao versionados no diretorio raiz da aplicacao, com nomes como .env, .env.development e .env.production, permitindo configuracoes diferentes por ambiente sem alterar o codigo.",
                        "correto": True,
                        "justificativa": "Os slides apresentam exatamente esses nomes de arquivo como exemplos para separar configuracoes por ambiente (smartnotes.pdf, Variaveis de Ambiente)."
                    },
                    {
                        "valor": 2,
                        "texto": "No Node.js, o pacote dotenv e empregado para ler pares chave=valor a partir de um arquivo de texto local (padrao .env) e popula-los automaticamente na variavel global process.env no momento da execucao.",
                        "correto": True,
                        "justificativa": "O metodo dotenv.config() analisa o arquivo .env e injeta as chaves em process.env para acesso programatico (smartnotes.pdf)."
                    },
                    {
                        "valor": 4,
                        "texto": "A adocao de um arquivo versionado chamado .env.example serve como gabarito de configuracao para novos desenvolvedores, listando as variaveis necessarias sem expor valores ou senhas confidenciais.",
                        "correto": True,
                        "justificativa": "O .env.example informa a lista de chaves obrigatorias para que cada membro configure seu proprio .env local (smartnotes.pdf)."
                    },
                    {
                        "valor": 8,
                        "texto": "E recomendavel comitar o arquivo .env de producao no GitHub com o intuito de viabilizar deploys automatizados sem demandar configuracoes adicionais no servidor de hospedagem.",
                        "correto": False,
                        "justificativa": "Arquivos .env contem senhas, segredos e chaves que nunca devem ser expostos em repositorios versionados, devendo constar impreterivelmente no .gitignore (smartnotes.pdf)."
                    },
                    {
                        "valor": 16,
                        "texto": "Caso a variavel PORT nao esteja definida no ambiente ou no arquivo .env, construcoes como const PORT = process.env.PORT || 3000 garantem que a aplicacao adote uma porta padrao alternativa em vez de falhar abruptamente.",
                        "correto": True,
                        "justificativa": "O operador de fallback '||' define um valor alternativo seguro caso a propriedade nao esteja presente em process.env (smartnotes.pdf)."
                    }
                ]
            },
            {
                "numero": 5,
                "tema": "SmartNotes - Linters versus Formatadores, Ecossistema e Integracao com Editores",
                "pontos": 2.0,
                "enunciado": "Sobre a padronizacao de codigo-fonte, ecossistema de linters e integracao com ferramentas de desenvolvimento, julgue as assertivas:",
                "proposicoes": [
                    {
                        "valor": 1,
                        "texto": "Em Python, ferramentas como Ruff ou Pylint atuam como linters de analise de codigo, ao passo que Black ou Ruff Formatter sao utilizados especificamente como formatadores de codigo.",
                        "correto": True,
                        "justificativa": "A listagem comparativa de linguagens define Ruff/Pylint para analise estatica e Black/Ruff Formatter para diagramacao visual automatica (smartnotes.pdf)."
                    },
                    {
                        "valor": 2,
                        "texto": "O utilitario ESLint e restrito estritamente a arquivos JavaScript simples, sendo incapaz de efetuar a verificacao estatica em bases de codigo TypeScript.",
                        "correto": False,
                        "justificativa": "O pacote typescript-eslint permite ao ESLint analisar codigo TypeScript de forma completa, integrando regras recomendadas no eslint.config.mjs (smartnotes.pdf)."
                    },
                    {
                        "valor": 4,
                        "texto": "Em linguagens como Go e Rust, as ferramentas oficiais padroes para formatacao automatica de codigo sao, respectivamente, gofmt e rustfmt.",
                        "correto": True,
                        "justificativa": "Ambos os ecossistemas padronizam a formatacao nativamente atraves de gofmt e rustfmt (smartnotes.pdf)."
                    },
                    {
                        "valor": 8,
                        "texto": "O arquivo .prettierignore serve para instruir o Prettier a nao formatar determinados diretorios e arquivos compilados ou externos, tais como build/, dist/ ou dependencias de terceiros.",
                        "correto": True,
                        "justificativa": "Assim como o .gitignore, o .prettierignore poupa diretorios de saida gerados ou bibliotecas de reformatacoes desnecessarias (smartnotes.pdf)."
                    },
                    {
                        "valor": 16,
                        "texto": "A definicao de scripts no package.json como 'lint': 'eslint src/' e 'format': 'prettier --write src/' permite incorporar facilmente a verificacao e correcao de estilo nas rotinas de integracao continua (CI) da equipe.",
                        "correto": True,
                        "justificativa": "Os scripts encapsulam a chamada aos utilitarios e uniformizam sua execucao em ambientes de desenvolvimento e pipelines de automacao (smartnotes.pdf)."
                    }
                ]
            }
        ]
    },
    {
        "id": "prova_03",
        "titulo": "Simulado Somativo 03 - Preparacao para a Prova de Gerencia de Configuracao",
        "disciplina": "Gerencia de Configuracao",
        "material_referencia": "Aulas e Slides do Prof. David Fernandes de Oliveira (IC/UFAM)",
        "elaboracao": "Simulado Independente de Estudos para a Prova",
        "pontuacao_total": 10.0,
        "instrucoes": "Cada questao contem 5 proposicoes com valores binarios (01, 02, 04, 08, 16). A resposta corresponde a soma exclusiva das proposicoes verdadeiras. Cada questao vale 2,0 pontos.",
        "questoes": [
            {
                "numero": 1,
                "tema": "Git - Desfazimento de Alteracoes e Diferencas entre Modos de Reset",
                "pontos": 2.0,
                "enunciado": "Em relacao as operacoes de cancelamento e desfazimento de mudancas no Git, julgue as assertivas a seguir:",
                "proposicoes": [
                    {
                        "valor": 1,
                        "texto": "O comando git restore <arquivo> descarta as modificacoes nao indexadas de um arquivo no Working Directory, revertendo-o ao estado atualmente registrado na Staging Area ou no ultimo commit.",
                        "correto": True,
                        "justificativa": "O restore restaura o arquivo de trabalho com base no index, descartando edicoes locais nao salvas (1_git.pdf)."
                    },
                    {
                        "valor": 2,
                        "texto": "O comando git restore --staged <arquivo> retira o arquivo indicado da Staging Area (desindexacao), preservando integralmente o conteudo modificado no Working Directory.",
                        "correto": True,
                        "justificativa": "O --staged desfaz apenas o git add: o arquivo volta de staged para modified sem perder o trabalho editado (1_git.pdf, Desfazendo alteracoes)."
                    },
                    {
                        "valor": 4,
                        "texto": "O modo padrao do comando git reset (equivalente a git reset --mixed) move o ponteiro da branch de volta ao commit informado e remove as alteracoes da Staging Area, mantendo as modificacoes no Working Directory.",
                        "correto": True,
                        "justificativa": "O comportamento padrao do reset e o --mixed, que desfaz a preparacao no index mantendo os arquivos no disco para revisao (1_git.pdf)."
                    },
                    {
                        "valor": 8,
                        "texto": "O comando git commit --amend permite incorporar novos arquivos da Staging Area ao ultimo commit realizado ou alterar a mensagem desse commit, sem gerar um commit adicional no historico.",
                        "correto": True,
                        "justificativa": "O --amend retifica o commit mais recente combinando alteracoes pendentes no index com o snapshot imediatamente anterior (1_git.pdf)."
                    },
                    {
                        "valor": 16,
                        "texto": "A execucao de git reset --hard HEAD~1 e uma operacao branda que cria um commit de reversao sem eliminar quaisquer arquivos do disco.",
                        "correto": False,
                        "justificativa": "O reset --hard e uma operacao destrutiva que descarta sumariamente tanto a staging area quanto as edicoes no working directory, sem gerar novo commit (1_git.pdf)."
                    }
                ]
            },
            {
                "numero": 2,
                "tema": "Git - Detached HEAD, Diagnostico de Conflitos e Aborto de Merge",
                "pontos": 2.0,
                "enunciado": "A respeito de situacoes excepcionais de navegacao e resolucao de conflitos no Git, avalie as proposicoes:",
                "proposicoes": [
                    {
                        "valor": 1,
                        "texto": "Quando um conflito de merge acontece, os arquivos conflitantes continuam compativeis para compilacao imediata, pois o compilador ignora nativamente os caracteres <<<<<<< e >>>>>>>.",
                        "correto": False,
                        "justificativa": "Os marcadores geram graves erros sintaticos na linguagem de programacao e impedem a compilacao/execucao do codigo ate serem removidos manualmente (1_git.pdf)."
                    },
                    {
                        "valor": 2,
                        "texto": "No estado de Detached HEAD (obtido, por exemplo, com git switch --detach <commit>), o HEAD aponta diretamente para um commit e nao para uma branch, de modo que commits criados nesse estado nao pertencem automaticamente a nenhuma branch.",
                        "correto": True,
                        "justificativa": "E o alerta do slide de Detached HEAD: e possivel commitar nesse estado, mas os commits nao ficam associados a uma branch; o uso tipico e inspecionar ou testar versoes antigas (1_git.pdf)."
                    },
                    {
                        "valor": 4,
                        "texto": "Caso ocorram conflitos complexos durante uma operacao de integracao e o desenvolvedor opte por desistir do processo, o comando git merge --abort interrompe a mesclagem e restaura o estado exato anterior ao comando de merge.",
                        "correto": True,
                        "justificativa": "O comando git merge --abort limpa os marcadores de conflito e restabelece a branch local ao momento anterior a solicitacao de integracao (1_git.pdf)."
                    },
                    {
                        "valor": 8,
                        "texto": "A expressao HEAD~2 referencia o commit correspondente ao 'avo' do commit atualmente ativo.",
                        "correto": True,
                        "justificativa": "A notacao de til com numero (HEAD~n) navega retroativamente na linhagem de ancestrais primarios (1_git.pdf)."
                    },
                    {
                        "valor": 16,
                        "texto": "O utilitario git stash pop restaura as modificacoes mais recentes salvas na pilha de stash e as remove automaticamente dessa pilha de armazenamento temporario.",
                        "correto": True,
                        "justificativa": "Diferente de git stash apply (que mantem na pilha), o pop aplica o stash e o desempilha imediatamente (1_git.pdf)."
                    }
                ]
            },
            {
                "numero": 3,
                "tema": "Git - Integracao com Rebase versus Three-Way Merge e Regra de Ouro",
                "pontos": 2.0,
                "enunciado": "Comparando as abordagens de integracao de codigo no Git por git merge e git rebase, julgue as assertivas:",
                "proposicoes": [
                    {
                        "valor": 1,
                        "texto": "O git merge e a abordagem preferencial quando se deseja preservar a fidelidade historica e cronologica das bifurcacoes ou quando se esta integrando branches colaborativas de longa duracao.",
                        "correto": True,
                        "justificativa": "O merge preserva o contexto de ramificacao e nao distorce a linha do tempo colaborativa (1_git.pdf)."
                    },
                    {
                        "valor": 2,
                        "texto": "O git rebase e frequentemente utilizado em branches locais de feature antes do merge na main para incorporar atualizacoes recentes da branch base e evitar commits de merge desnecessarios.",
                        "correto": True,
                        "justificativa": "O rebase local lineariza a branch do desenvolvedor, tornando a posterior integracao na base limpa e direta (1_git.pdf)."
                    },
                    {
                        "valor": 4,
                        "texto": "Ao sofrer rebase, os commits originais mantem seus mesmos identificadores de hash SHA-1 inalterados, viabilizando o pareamento perfeito com branches remotas clonadas por terceiros.",
                        "correto": False,
                        "justificativa": "O rebase calcula novos hashes SHA-1 para cada commit reaplicado, destruindo a compatibilidade com colaboradores que tenham os hashes anteriores (1_git.pdf)."
                    },
                    {
                        "valor": 8,
                        "texto": "Um merge commit e necessario quando as duas branches avancaram separadamente, ou seja, quando nao e possivel realizar um fast-forward; esse novo commit integra o historico das duas branches.",
                        "correto": True,
                        "justificativa": "Se as branches divergiram, o Git cria um novo commit de merge unindo as duas linhas; sem divergencia, basta o fast-forward (1_git.pdf, Mesclando Branches)."
                    },
                    {
                        "valor": 16,
                        "texto": "Se um commit for descartado indevidamente por um git reset --hard, o comando git log sem argumentos especiais sera a ferramenta indicada para localiza-lo e resgata-lo.",
                        "correto": False,
                        "justificativa": "O git log apenas percorre commits alcancaveis na arvore atual. Commits orfaos so podem ser localizados via git reflog (1_git.pdf)."
                    }
                ]
            },
            {
                "numero": 4,
                "tema": "SmartNotes - SemVer Estrito e Resolucao de Versoes no Ecossistema NPM",
                "pontos": 2.0,
                "enunciado": "A respeito das convencoes de numeracao de software e especificacao SemVer (Semantic Versioning), avalie as proposicoes:",
                "proposicoes": [
                    {
                        "valor": 1,
                        "texto": "Uma versao SemVer obedece rigidamente ao formato MAJOR.MINOR.PATCH, no qual cada segmento possui significado semantico formal definido pelo impacto da mudanca no sistema.",
                        "correto": True,
                        "justificativa": "A semantica do versionamento divide as modificacoes entre quebras de contrato, adicoes funcionais e correcoes de bugs (smartnotes.pdf)."
                    },
                    {
                        "valor": 2,
                        "texto": "O operador de dependencia ^ (circunflexo) instalado na versao ^5.2.1 autoriza o npm update a instalar uma versao 6.0.0 lancada posteriormente pelos mantenedores da biblioteca.",
                        "correto": False,
                        "justificativa": "O circunflexo bloqueia categoricamente versoes com MAJOR diferente, impedindo que breaking changes sejam instaladas involuntariamente (smartnotes.pdf)."
                    },
                    {
                        "valor": 4,
                        "texto": "A evolucao de 5.1.0 para 5.1.1 representa uma correcao de falha (patch) que nao introduz novas funcionalidades e preserva completa compatibilidade retroativa com versoes anteriores.",
                        "correto": True,
                        "justificativa": "PATCH destina-se exclusivamente a correcoes de bugs estaveis e retrocompativeis (smartnotes.pdf)."
                    },
                    {
                        "valor": 8,
                        "texto": "A declaracao de versao 'express': '5.2.1' (sem prefixos como ^ ou ~) impoe a instalacao estrita e exata da versao 5.2.1, nao sofrendo atualizacoes automaticas via npm update.",
                        "correto": True,
                        "justificativa": "Sem prefixos de intervalo de versao, a dependencia fica fixada (pinned) de maneira deterministica no numero informado (smartnotes.pdf)."
                    },
                    {
                        "valor": 16,
                        "texto": "O operador ~ (til) e mais conservador do que o circunflexo (^), permitindo ao npm instalar apenas novas versoes de correcao de bug (PATCHs), protegendo a aplicacao contra alteracoes de comportamento em funcionalidades novas.",
                        "correto": True,
                        "justificativa": "O til confina o npm update estritamente a correcoes de falhas na mesma versao minor (smartnotes.pdf)."
                    }
                ]
            },
            {
                "numero": 5,
                "tema": "SmartNotes - Validacao com Envalid e Configuracao Flat no ESLint",
                "pontos": 2.0,
                "enunciado": "No contexto da configuracao robusta de servidores Node.js com TypeScript, analise as proposicoes sobre o envalid e o ESLint:",
                "proposicoes": [
                    {
                        "valor": 1,
                        "texto": "A biblioteca envalid impede falhas silenciosas na aplicacao por meio da abordagem fail-fast, garantindo que o servidor nao inicie se configuracoes vitais de conexao ou seguranca estiverem ausentes.",
                        "correto": True,
                        "justificativa": "O envalid aborta a execucao imediatamente no bootstrap caso os requisitos do esquema de variaveis nao sejam cumpridos (smartnotes.pdf)."
                    },
                    {
                        "valor": 2,
                        "texto": "A funcao cleanEnv do envalid aceita validadores de tipo como str() para cadeias de caracteres e port() para portas de rede com limites numericos validos e valores default opcionais.",
                        "correto": True,
                        "justificativa": "Os validadores embutidos asseguram tipos corretos como portas validas e strings obrigatorias ou com valores padrao (smartnotes.pdf)."
                    },
                    {
                        "valor": 4,
                        "texto": "Configurar uma regra no ESLint com o valor 'off' faz com que o linter interrompa a compilacao do projeto emitindo um codigo de erro fatal para o sistema operacional.",
                        "correto": False,
                        "justificativa": "O modificador 'off' desativa inteiramente a regra, fazendo com que o ESLint a ignore sem disparar avisos ou erros (smartnotes.pdf)."
                    },
                    {
                        "valor": 8,
                        "texto": "No novo sistema de configuracao flat do ESLint (arquivo eslint.config.mjs), e possivel definir regras especificas para o compilador TypeScript atraves do pacote typescript-eslint.",
                        "correto": True,
                        "justificativa": "O arquivo modular eslint.config.mjs carrega as recomendacoes de typescript-eslint para aplicar analise estatica ao TypeScript (smartnotes.pdf)."
                    },
                    {
                        "valor": 16,
                        "texto": "A utilizacao da extensao oficial do ESLint ou Prettier no VS Code permite identificar violacoes de regras em tempo real no editor e reformatar o arquivo automaticamente ao pressionar Ctrl+S.",
                        "correto": True,
                        "justificativa": "A integracao no editor proporciona feedback imediato ao desenvolvedor e formatacao automatica ao salvar arquivos (smartnotes.pdf)."
                    }
                ]
            }
        ]
    }
]


def calcular_soma_questao(questao):
    return sum(p["valor"] for p in questao["proposicoes"] if p["correto"])

def gerar_markdown_prova(prova_data):
    md = []
    md.append(f"# {prova_data['titulo']}\n")
    md.append(f"**Disciplina:** {prova_data['disciplina']}  ")
    md.append(f"**Material de Referencia:** {prova_data['material_referencia']}  ")
    md.append(f"**Elaboracao:** {prova_data['elaboracao']}  ")
    md.append(f"**Pontuacao Total:** {prova_data['pontuacao_total']} pontos  ")
    md.append(f"**Formato:** Questoes de Verdadeiro (V) ou Falso (F) no Formato Somativo\n")
    md.append("---\n")
    md.append("## Instrucoes\n")
    md.append(f"{prova_data['instrucoes']}\n")
    md.append("---\n")
    md.append("## Questoes\n")

    for q in prova_data["questoes"]:
        md.append(f"### Questao {q['numero']:02d} (Valor: {q['pontos']:.1f} pontos)")
        md.append(f"**Tema:** {q['tema']}\n")
        md.append(f"{q['enunciado']}\n")
        for p in q["proposicoes"]:
            md.append(f"- **({p['valor']:02d})** {p['texto']}")
        md.append(f"\n**SOMA DA QUESTAO {q['numero']:02d}:** [ ______ ]\n")
        md.append("---\n")

    md.append("## Folha de Gabarito e Justificativas Tecnicas\n")
    md.append("### Resumo das Respostas Corretas\n")
    md.append("| Questao | Proposicoes Verdadeiras | Calculo da Soma Unica | Resposta Final (Soma) | Pontos |")
    md.append("| :---: | :---: | :---: | :---: | :---: |")

    for q in prova_data["questoes"]:
        itens_v = [f"({p['valor']:02d})" for p in q["proposicoes"] if p["correto"]]
        soma = calcular_soma_questao(q)
        calc_str = " + ".join([f"{p['valor']:02d}" for p in q["proposicoes"] if p["correto"]])
        md.append(f"| **Questao {q['numero']:02d}** | {', '.join(itens_v)} | {calc_str} | **{soma}** | {q['pontos']:.1f} |")

    md.append(f"| **TOTAL** | - | - | - | **{prova_data['pontuacao_total']:.1f}** |\n")
    md.append("---\n")
    md.append("### Resolucao Detalhada Item por Item\n")

    for q in prova_data["questoes"]:
        soma = calcular_soma_questao(q)
        md.append(f"#### Questao {q['numero']:02d} - Soma: {soma}")
        for p in q["proposicoes"]:
            status = "VERDADEIRA" if p["correto"] else "FALSA"
            md.append(f"- **({p['valor']:02d}) [{status}]**: {p['justificativa']}")
        md.append("")

    return "\n".join(md)

def main():
    artefatos_dir = Path("artefatos")
    artefatos_dir.mkdir(parents=True, exist_ok=True)

    todas_as_provas_json = []

    for p in PROVAS_DATA:
        # Calcular somas em cada questao para o json
        p_enriched = json.loads(json.dumps(p))
        for q in p_enriched["questoes"]:
            q["soma_correta"] = calcular_soma_questao(q)
            q["proposicoes_verdadeiras"] = [prop["valor"] for prop in q["proposicoes"] if prop["correto"]]

        todas_as_provas_json.append(p_enriched)

        # Salvar JSON individual da prova
        json_path = artefatos_dir / f"{p['id']}.json"
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(p_enriched, f, indent=2, ensure_ascii=False)
        print(f"[OK] Gerado: {json_path}")

        # Salvar Markdown individual da prova
        md_content = gerar_markdown_prova(p)
        md_path = artefatos_dir / f"{p['id']}.md"
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(md_content)
        print(f"[OK] Gerado: {md_path}")

    # Salvar JSON unificado de todas as provas para consumo no fastsite
    consolidated_path = artefatos_dir / "provas.json"
    with open(consolidated_path, "w", encoding="utf-8") as f:
        json.dump({"provas": todas_as_provas_json}, f, indent=2, ensure_ascii=False)
    print(f"[OK] Gerado arquivo consolidado: {consolidated_path}")

    # Salvar copia para o diretorio public
    public_dir = Path("public")
    if public_dir.exists():
        public_json_path = public_dir / "provas.json"
        with open(public_json_path, "w", encoding="utf-8") as f:
            json.dump({"provas": todas_as_provas_json}, f, indent=2, ensure_ascii=False)
        print(f"[OK] Gerado arquivo publico: {public_json_path}")

if __name__ == "__main__":
    main()
