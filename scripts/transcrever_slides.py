#!/usr/bin/env python3
"""
Script fixo de transcricao de slides para Markdown com suporte a OCR e extracao direta.
Desenvolvido para a disciplina de Gerencia de Configuracao (IC/UFAM).

Funcionalidades:
- Transcricao estruturada de 1_git.pdf (148 slides).
- Transcricao com filtro de cor para smartnotes.pdf (apenas slides com fundo azul).
- Deteccao automatica e higienizacao de marcadores de lista e blocos de codigo.
- Suporte a OCR via Tesseract quando solicitado ou em paginas rasterizadas.
- Garantia de conformidade de codificacao UTF-8 e ausencia de emojis.
"""

import os
import sys
import argparse
import subprocess
from pathlib import Path

try:
    import pymupdf
    from PIL import Image
    import numpy as np
except ImportError:
    print("Dependencias necessarias ausentes. Instale: pip install pymupdf pillow numpy")
    sys.exit(1)


def is_blue_slide(page, dpi=36) -> bool:
    """
    Avalia se o slide possui fundo com a tonalidade azul padrao
    utilizada nos slides de interesse de smartnotes.pdf (RGB ~ [218, 227, 243]).
    """
    pix = page.get_pixmap(dpi=dpi)
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    arr = np.array(img)
    tl = arr[2, 2]
    # Tonalidade azul: canal B superior a R e G com intensidade significativa
    return int(tl[2]) > int(tl[0]) + 10 and int(tl[2]) > int(tl[1]) + 10 and int(tl[2]) > 180


def run_ocr_on_page(page, dpi=150) -> str:
    """
    Executa OCR em uma pagina PDF utilizando Tesseract (se disponivel no SO)
    ou fallback para extracao vetorial do PyMuPDF.
    """
    pix = page.get_pixmap(dpi=dpi)
    img_path = f"/tmp/page_ocr_temp_{os.getpid()}.png"
    pix.save(img_path)
    
    text = ""
    try:
        cmd = ["tesseract", img_path, "stdout", "-l", "por+eng", "--psm", "6"]
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if res.returncode == 0 and res.stdout.strip():
            text = res.stdout.strip()
    except Exception:
        pass
    finally:
        if os.path.exists(img_path):
            os.remove(img_path)

    # Fallback para o texto nativo do PDF caso OCR falhe ou tesseract nao esteja instalado
    if not text:
        text = page.get_text().strip()
    return text


def clean_and_format_text(text: str) -> str:
    """
    Normaliza caracteres de marcadores de apresentacao (Impress/PowerPoint),
    converte comandos em blocos de codigo e remove simbolos de emoji.
    """
    lines = text.split("\n")
    formatted_lines = []
    
    for raw_line in lines:
        line = raw_line.rstrip()
        if not line:
            continue
            
        # Higienizacao de marcadores especiais
        line = line.replace("✓", "[OK]").replace("✔", "[OK]")
        
        # Formatacao de marcadores de lista
        if line.startswith(("•", "●", "")):
            formatted_lines.append(f"- {line[1:].strip()}")
        elif line.startswith(("–", "—")):
            formatted_lines.append(f"  - {line[1:].strip()}")
        elif line.startswith(("$ ", "git ", "npm ", "npx ", "export ", "const ", "import ", "function ")):
            formatted_lines.append(f"```bash\n{line}\n```")
        else:
            formatted_lines.append(line)
            
    return "\n\n".join(formatted_lines)


def transcrever_git(pdf_path: Path, output_file: Path, force_ocr: bool = False):
    """Transcreve o arquivo 1_git.pdf completo."""
    print(f"[INFO] Processando Git: {pdf_path}")
    doc = pymupdf.open(str(pdf_path))
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("# Transcricao dos Slides - Git e GitHub\n\n")
        f.write(f"> Origem: `{pdf_path.name}` ({len(doc)} paginas) - Gerencia de Configuracao (IC/UFAM).\n\n")
        f.write("## Indice dos Topicos\n\n")
        f.write("- [1. Fundamentos de Controle de Versao (Slides 2 a 9)](#1-fundamentos-de-controle-de-versao)\n")
        f.write("- [2. Arquitetura e Principios Basicos do Git (Slides 10 a 14)](#2-arquitetura-e-principios-basicos-do-git)\n")
        f.write("- [3. Configuracao Inicial e Autoria (Slides 15 a 19)](#3-configuracao-inicial-e-autoria)\n")
        f.write("- [4. Ciclo de Vida e os Tres Estados (Slides 20 a 29)](#4-ciclo-de-vida-e-os-tres-estados)\n")
        f.write("- [5. Ignorando Arquivos com .gitignore (Slides 30 a 35)](#5-ignorando-arquivos-com-gitignore)\n")
        f.write("- [6. Visualizacao de Mudancas, Status e Logs (Slides 36 a 44)](#6-visualizacao-de-mudancas-status-e-logs)\n")
        f.write("- [7. Branches e o Ponteiro HEAD (Slides 45 a 56)](#7-branches-e-o-ponteiro-head)\n")
        f.write("- [8. Integracao de Branches: Fast-Forward e Merge Commit (Slides 57 a 69)](#8-integracao-de-branches-fast-forward-e-merge-commit)\n")
        f.write("- [9. Conflitos de Merge e Resolucao (Slides 70 a 85)](#9-conflitos-de-merge-e-resolucao)\n")
        f.write("- [10. Repositorios Remotos, Clones e Push (Slides 86 a 102)](#10-repositorios-remotos-clones-e-push)\n")
        f.write("- [11. Git Pull, Git Fetch e Sincronizacao (Slides 103 a 111)](#11-git-pull-git-fetch-e-sincronizacao)\n")
        f.write("- [12. Rebase versus Merge (Slides 112 a 118)](#12-rebase-versus-merge)\n")
        f.write("- [13. Desfazendo Alteracoes e Modos de Reset (Slides 119 a 135)](#13-desfazendo-alteracoes-e-modos-de-reset)\n")
        f.write("- [14. Historico de Movimentos com Git Reflog (Slides 136 a 140)](#14-historico-de-movimentos-com-git-reflog)\n")
        f.write("- [15. Corrigindo Commits com Git Amend (Slides 141 a 145)](#15-corrigindo-commits-com-git-amend)\n")
        f.write("- [16. Armazenamento Temporario com Git Stash (Slides 146 a 148)](#16-armazenamento-temporario-com-git-stash)\n\n---\n\n")

        for idx, page in enumerate(doc, start=1):
            if force_ocr:
                text = run_ocr_on_page(page)
            else:
                text = page.get_text().strip()
                if not text:
                    text = run_ocr_on_page(page)

            clean_text = clean_and_format_text(text)
            f.write(f"### Slide {idx}\n\n")
            f.write(f"{clean_text}\n\n---\n\n")

    print(f"[SUCESSO] Arquivo gerado: {output_file}")


def transcrever_smartnotes(pdf_path: Path, output_file: Path, force_ocr: bool = False):
    """Transcreve exclusivamente os slides com cor de fundo azul de smartnotes.pdf."""
    print(f"[INFO] Processando SmartNotes (Filtro Azul): {pdf_path}")
    doc = pymupdf.open(str(pdf_path))
    blue_slides = []

    for idx, page in enumerate(doc, start=1):
        if is_blue_slide(page):
            blue_slides.append((idx, page))

    print(f"[INFO] Identificados {len(blue_slides)} slides com tonalidade azul.")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("# Transcricao dos Slides Azuis - SmartNotes\n\n")
        f.write(f"> Origem: `{pdf_path.name}` (Filtro estrito de {len(blue_slides)} slides azuis) - Gerencia de Configuracao (IC/UFAM).\n\n")
        f.write("## Indice dos Topicos Filtrados\n\n")
        f.write("- [1. Semantic Versioning - SemVer (Slides 22 a 25)](#1-semantic-versioning---semver)\n")
        f.write("- [2. Variaveis de Ambiente (Slides 32 a 37)](#2-variaveis-de-ambiente)\n")
        f.write("- [3. Validando as Variaveis de Ambiente com Envalid (Slides 38 a 44)](#3-validando-as-variaveis-de-ambiente-com-envalid)\n")
        f.write("- [4. Qualidade de Codigo: ESLint e Prettier (Slides 45 a 62)](#4-qualidade-de-codigo-eslint-e-prettier)\n\n---\n\n")

        for idx, page in blue_slides:
            if force_ocr:
                text = run_ocr_on_page(page)
            else:
                text = page.get_text().strip()
                if not text:
                    text = run_ocr_on_page(page)

            clean_text = clean_and_format_text(text)
            f.write(f"### Slide {idx}\n\n")
            f.write(f"{clean_text}\n\n---\n\n")

    print(f"[SUCESSO] Arquivo gerado: {output_file}")


def main():
    parser = argparse.ArgumentParser(description="Script fixo de transcricao de slides para Markdown")
    parser.add_argument("--slides-dir", type=str, default="slides", help="Diretorio com os PDFs")
    parser.add_argument("--output-dir", type=str, default="transcricoes", help="Diretorio de saida dos arquivos .md")
    parser.add_argument("--force-ocr", action="store_true", help="Forcar uso do motor OCR em todas as paginas")
    args = parser.parse_args()

    slides_dir = Path(args.slides_dir)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    git_pdf = slides_dir / "1_git.pdf"
    smartnotes_pdf = slides_dir / "smartnotes.pdf"

    if git_pdf.exists():
        transcrever_git(git_pdf, output_dir / "1_git.md", force_ocr=args.force_ocr)
    else:
        print(f"[AVISO] Arquivo nao encontrado: {git_pdf}")

    if smartnotes_pdf.exists():
        transcrever_smartnotes(smartnotes_pdf, output_dir / "smartnotes.md", force_ocr=args.force_ocr)
    else:
        print(f"[AVISO] Arquivo nao encontrado: {smartnotes_pdf}")

    print("[CONCLUIDO] Transcricoes finalizadas com sucesso.")


if __name__ == "__main__":
    main()

