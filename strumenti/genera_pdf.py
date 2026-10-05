#!/usr/bin/env python3
"""Genera un PDF A4 impaginato da uno o più file Markdown del repository.

Uso:
  python3 strumenti/genera_pdf.py manuale   # manuale completo -> pdf/Superapprendimento_manuale_completo.pdf
  python3 strumenti/genera_pdf.py guida     # guida del docente di tango -> pdf/Guida_operativa_docente_tango.pdf

Richiede: pacchetto Python `markdown` e Node.js con `playwright` (Chromium).
"""
import html
import os
import re
import subprocess
import sys

import markdown

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DOCS = {
    "manuale": {
        "title": "Superapprendimento",
        "subtitle": "Metodo fondato sulla Desuggestopedia di Georgi Lozanov<br>Manuale completo",
        "out": "pdf/Superapprendimento_manuale_completo.pdf",
        "files": [
            "README.md",
            "metodo/00-convenzioni.md",
            "metodo/01-fondamenti-e-principi.md",
            "metodo/02-ciclo-didattico.md",
            "metodo/03a-catalogo-strumenti-stato-suggestione-voce.md",
            "metodo/03b-catalogo-strumenti-corpo-memoria-integrazioni.md",
            "metodo/04-musica.md",
            "metodo/05-il-docente.md",
            "metodo/06-sicurezza-ed-etica.md",
            "metodo/07-modulo-sperimentale.md",
            "applicazioni/tango.md",
            "applicazioni/qigong-liu-zi-jue.md",
            "applicazioni/formazione-insegnanti.md",
            "applicazioni/corso-universitario.md",
            "DECISIONI.md",
            "metodo/REVISIONE.md",
        ],
        "toc_depth": 2,
    },
    "guida": {
        "title": "Guida operativa del docente",
        "subtitle": "Superapprendimento nel tango argentino",
        "out": "pdf/Guida_operativa_docente_tango.pdf",
        "files": ["guide/guida-operativa-docente-tango.md"],
        "toc_depth": 2,
    },
}

CSS = """
@page { size: A4; margin: 22mm 18mm 20mm 18mm; }
html { font-family: 'Noto Serif', 'DejaVu Serif', Georgia, serif; font-size: 10.5pt; line-height: 1.5; color: #1c1917; }
body { margin: 0; }
h1, h2, h3, h4 { font-family: 'Noto Sans', 'DejaVu Sans', Arial, sans-serif; color: #1f3a2e; line-height: 1.25; break-after: avoid; }
h1 { font-size: 20pt; margin: 0 0 10pt; border-bottom: 2px solid #1f3a2e; padding-bottom: 4pt; }
h2 { font-size: 14pt; margin: 18pt 0 6pt; }
h3 { font-size: 12pt; margin: 14pt 0 4pt; }
h4 { font-size: 10.5pt; margin: 10pt 0 3pt; }
p, li { orphans: 3; widows: 3; }
a { color: #1f3a2e; text-decoration: none; }
table { border-collapse: collapse; width: 100%; margin: 8pt 0; font-size: 9pt; break-inside: auto; }
tr { break-inside: avoid; }
th, td { border: 1px solid #d6d3d1; padding: 3pt 5pt; vertical-align: top; text-align: left; }
th { background: #f5f5f4; font-family: 'Noto Sans', 'DejaVu Sans', sans-serif; }
blockquote { margin: 8pt 0; padding: 6pt 10pt; background: #f7f5ef; border-left: 3px solid #b8a37a; break-inside: avoid; }
code { font-family: 'DejaVu Sans Mono', monospace; font-size: 9pt; }
hr { border: none; border-top: 1px solid #d6d3d1; margin: 12pt 0; }
.doc { break-before: page; }
.cover { height: 240mm; display: flex; flex-direction: column; justify-content: center; text-align: center; }
.cover h1 { border: none; font-size: 30pt; }
.cover .sub { font-family: 'Noto Sans', sans-serif; font-size: 13pt; color: #44403c; line-height: 1.6; }
.cover .meta { margin-top: 30pt; font-size: 10pt; color: #78716c; }
.toc { break-before: page; }
.toc h1 { font-size: 18pt; }
.toc ul { list-style: none; padding-left: 0; }
.toc li { margin: 2pt 0; }
.toc li.l2 { padding-left: 14pt; font-size: 9.5pt; color: #44403c; }
.toc li.l1 { margin-top: 6pt; font-weight: bold; }
.src { font-size: 8pt; color: #a8a29e; margin-bottom: 4pt; font-family: 'Noto Sans', sans-serif; }
"""


def slug(text):
    s = re.sub(r"<[^>]+>", "", text)
    s = re.sub(r"[^\w\s-]", "", s.lower(), flags=re.UNICODE)
    return re.sub(r"[\s_]+", "-", s).strip("-") or "sezione"


def build(key):
    cfg = DOCS[key]
    sections, toc = [], []
    used = set()
    file_ids = {f: "doc-" + slug(f) for f in cfg["files"]}
    for f in cfg["files"]:
        path = os.path.join(ROOT, f)
        if not os.path.exists(path):
            print("manca:", f)
            continue
        text = open(path, encoding="utf-8").read()
        body = markdown.markdown(text, extensions=["tables", "sane_lists", "fenced_code", "attr_list"])

        def add_ids(m):
            level, content = int(m.group(1)), m.group(2)
            base = slug(content)
            hid, n = base, 2
            while hid in used:
                hid, n = f"{base}-{n}", n + 1
            used.add(hid)
            if level <= cfg["toc_depth"]:
                toc.append((level, re.sub(r"<[^>]+>", "", content), hid))
            return f'<h{level} id="{hid}">{content}</h{level}>'

        body = re.sub(r"<h([1-4])>(.*?)</h\1>", add_ids, body, flags=re.S)

        # link tra file del repository -> ancore interne del PDF
        def fix_link(m):
            href = m.group(1)
            target = os.path.normpath(os.path.join(os.path.dirname(f), href.split("#")[0]))
            return f'href="#{file_ids[target]}"' if target in file_ids else m.group(0)

        body = re.sub(r'href="([^"#:]+\.md[^"]*)"', fix_link, body)
        sections.append(f'<section class="doc" id="{file_ids[f]}"><div class="src">{html.escape(f)}</div>{body}</section>')

    toc_html = "".join(f'<li class="l{lvl}"><a href="#{hid}">{html.escape(t)}</a></li>' for lvl, t, hid in toc)
    page = f"""<!doctype html><html lang="it"><head><meta charset="utf-8"><title>{cfg['title']}</title><style>{CSS}</style></head>
<body><div class="cover"><h1>{cfg['title']}</h1><div class="sub">{cfg['subtitle']}</div>
<div class="meta">Repository andrea76b/superapprendimento</div></div>
<nav class="toc"><h1>Indice</h1><ul>{toc_html}</ul></nav>
{''.join(sections)}</body></html>"""
    out_pdf = os.path.join(ROOT, cfg["out"])
    os.makedirs(os.path.dirname(out_pdf), exist_ok=True)
    out_html = out_pdf[:-4] + ".html"
    open(out_html, "w", encoding="utf-8").write(page)
    subprocess.run(["node", os.path.join(ROOT, "strumenti", "stampa_pdf.js"), out_html, out_pdf], check=True)
    os.remove(out_html)
    print("scritto:", cfg["out"])


if __name__ == "__main__":
    for k in sys.argv[1:] or ["manuale", "guida"]:
        build(k)
