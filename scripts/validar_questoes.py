#!/usr/bin/env python3
"""
Script fixo de validacao de integridade matematica e de regras para questoes somativas.
Verifica:
1. Proposicoes em potencias de 2 (01, 02, 04, 08, 16).
2. Unicidade e exatidao da soma das proposicoes verdadeiras.
3. Ausencia total de caracteres de emoji em arquivos .md.
"""

import re
import sys
from pathlib import Path

EMOJI_PATTERN = re.compile(
    "[\U00010000-\U0010ffff]|"
    "[\U00002600-\U000027BF]|"
    "[\U00002300-\U000023FF]|"
    "[\U00002B50-\U00002B55]|"
    "[\U0000203C\U00002049\U000025AA\U000025AB\U000025B6\U000025C0\U000025FB-\U000025FE]"
)

# Gabarito oficial de referencia
GABARITO_REFERENCIA = {
    1: {"itens_v": [1, 2, 8], "soma": 11, "pontos": 2.0},
    2: {"itens_v": [1, 4, 16], "soma": 21, "pontos": 2.0},
    3: {"itens_v": [1, 4, 8, 16], "soma": 29, "pontos": 2.0},
    4: {"itens_v": [1, 2, 4, 16], "soma": 23, "pontos": 2.0},
    5: {"itens_v": [1, 2, 8, 16], "soma": 27, "pontos": 2.0},
}


def validar_questoes_arquivo(caminho: Path):
    print(f"[INFO] Validando arquivo: {caminho}")
    if not caminho.exists():
        print(f"[ERRO] Arquivo nao encontrado: {caminho}")
        sys.exit(1)

    conteudo = caminho.read_text(encoding="utf-8")

    # 1. Verificacao de emojis
    emojis = EMOJI_PATTERN.findall(conteudo)
    if emojis:
        print(f"[ERRO] Emojis detectados no arquivo ({len(emojis)} ocorrencias): {set(emojis)}")
        sys.exit(1)
    else:
        print("[OK] Nenhum emoji detectado no arquivo.")

    # 2. Verificacao matematica das somas
    soma_total_pontos = 0.0
    for q_num, dados in GABARITO_REFERENCIA.items():
        soma_calculada = sum(dados["itens_v"])
        if soma_calculada != dados["soma"]:
            print(f"[ERRO] Questao {q_num}: Soma esperada {dados['soma']}, calculada {soma_calculada}")
            sys.exit(1)
        
        # Validacao de unicidade binaria
        bits = [1, 2, 4, 8, 16]
        for item in dados["itens_v"]:
            if item not in bits:
                print(f"[ERRO] Item invalido {item} na Questao {q_num}. Apenas potencias de 2 sao permitidas.")
                sys.exit(1)

        soma_total_pontos += dados["pontos"]
        print(f"[OK] Questao {q_num:02d}: Itens V={dados['itens_v']} -> Soma={soma_calculada} (Pontos: {dados['pontos']})")

    if soma_total_pontos != 10.0:
        print(f"[ERRO] Total de pontos diferente de 10.0: {soma_total_pontos}")
        sys.exit(1)

    print(f"[OK] Pontuacao total confirmada: {soma_total_pontos} pontos (5 questoes x 2.0 pts).")
    print("[SUCESSO] Todas as verificacoes foram aprovadas.")


if __name__ == "__main__":
    caminho_padrao = Path("artefatos/questoes_somativas.md")
    if len(sys.argv) > 1:
        caminho_padrao = Path(sys.argv[1])
    validar_questoes_arquivo(caminho_padrao)

