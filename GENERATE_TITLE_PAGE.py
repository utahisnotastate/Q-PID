"""
[SYSTEM: ACADEMIC_FACTORY_TITLE_PAGE]
[TARGET: MIT_LEONARDO_JOURNAL]
[OBJECTIVE: GENERATE NON-BLIND TITLE PAGE]
"""
import os
import subprocess
import sys
import requests
import zipfile

# ==========================================
# 0. SETUP
# ==========================================
TECTONIC_URL = "https://github.com/tectonic-typesetting/tectonic/releases/download/tectonic%400.14.1/tectonic-0.14.1-x86_64-pc-windows-msvc.zip"


def ensure_compiler():
    if os.path.exists("tectonic.exe"): return
    print("[SYSTEM] Downloading Compiler...")
    try:
        r = requests.get(TECTONIC_URL, stream=True)
        with open("tectonic.zip", 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): f.write(chunk)
        with zipfile.ZipFile("tectonic.zip", 'r') as z:
            z.extractall(".")
        os.remove("tectonic.zip")
    except Exception as e:
        print(f"[ERROR] {e}")
        sys.exit(1)


def sanitize(text):
    text = text.replace("&", " and ").replace("%", "\\%")
    text = text.replace("“", '"').replace("”", '"').replace("’", "'")
    return text


# ==========================================
# 1. CONTENT
# ==========================================
TITLE = "Tangible Algorithmics: Physicalizing Abstract Mathematical Dynamics via Diegetic USB Artifacts"
AUTHOR = "Utah Hans"
AFFILIATION = "Department of Unorthodox Engineering, Future Institute"
EMAIL = "utah@utahcreates.com"

ABSTRACT = sanitize(r"""
As algorithmic complexity increases, the gap between user understanding and software function widens. This "Black Box" problem is particularly acute in fields like Chaos Theory, Neural Differential Equations, and Entropic Security, where mathematical abstraction alienates the user from the underlying dynamics. This paper proposes a framework for "Tangible Algorithmics," utilizing a suite of modular USB artifacts designed to physicalize these concepts. Four case studies are presented: (1) The Q-PID, a modular Liquid Neural Network node; (2) The Isochron Key, a crystal-embedded interface for visualizing deterministic chaos; (3) The Aspect Interface, a screen-embedded tool for subliminal cognitive reinforcement; and (4) The Mnemonic Key, a haptic bio-logger. By coupling executable code with weight-calibrated physical totems, the author argues that users achieve a deeper "Material Anchoring" of complex computational states. Preliminary trials suggest this multi-modal approach significantly improves conceptual retention compared to purely digital interfaces.
""")


# ==========================================
# 2. GENERATOR
# ==========================================
def generate_title_page():
    latex = r"""
\documentclass[12pt, letterpaper]{article}
\usepackage[utf8]{inputenc}
\usepackage[margin=1in]{geometry}
\usepackage{setspace}

\begin{document}

\vspace*{2cm}

\begin{center}
    \textbf{\Large """ + TITLE + r"""}

    \vspace{2cm}

    \textbf{""" + AUTHOR + r"""} \\
    \vspace{0.5cm}
    \textit{""" + AFFILIATION + r"""} \\
    \texttt{""" + EMAIL + r"""}

    \vspace{3cm}
\end{center}

\noindent \textbf{Abstract:} \\
""" + ABSTRACT + r"""

\vfill
\noindent \textit{Corresponding Author: """ + AUTHOR + r"""}

\end{document}
    """

    with open("Title_Page.tex", "w", encoding="utf-8") as f:
        f.write(latex)


def compile_pdf():
    ensure_compiler()
    print("[SYSTEM] Compiling Title Page...")
    subprocess.run(["tectonic.exe", "Title_Page.tex"])

    if os.path.exists("Title_Page.pdf"):
        print("-" * 40)
        print("[VICTORY] Title_Page.pdf generated.")
        print("-" * 40)
    else:
        print("[ERROR] PDF generation failed.")


if __name__ == "__main__":
    generate_title_page()
    compile_pdf()
