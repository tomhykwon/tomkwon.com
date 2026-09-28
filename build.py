"""Assemble the site: wraps each page in pages/ with the shared header + sidebar.

Edit content in _src/*.html, then run:  python3 build.py
"""
from pathlib import Path

ROOT = Path(__file__).parent
CV = "https://drive.google.com/file/d/1g3-t7GjXTxpQe8bLHAco3GwJsJYnV0Ms/view?usp=sharing"

PAGES = [
    # file, nav label, <title>
    ("index.html", "Home", "Tom Kwon · UCL School of Management"),
    ("research.html", "Research", "Research · Tom Kwon"),
    ("teaching.html", "Teaching", "Teaching · Tom Kwon"),
]

ICON = {
    "mail": '<path d="M3 5h18v14H3z"/><path d="m3 6 9 7 9-7"/>',
    "school": '<path d="M3 10 12 4l9 6"/><path d="M5 10v8M9.5 10v8M14.5 10v8M19 10v8M3 20h18"/>',
    "scholar": '<path d="M2 9l10-5 10 5-10 5z"/><path d="M6 11v5c3 2.5 9 2.5 12 0v-5"/>',
    "file": '<path d="M6 3h8l4 4v14H6z"/><path d="M14 3v4h4M9 12h6M9 16h6"/>',
    "pin": '<path d="M12 21s-6-5.5-6-11a6 6 0 0 1 12 0c0 5.5-6 11-6 11z"/><circle cx="12" cy="10" r="2"/>',
}


def icon(name):
    return (f'<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" '
            f'stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round">{ICON[name]}</svg>')


SIDEBAR = f"""<aside class="sidebar">
      <img class="portrait" src="assets/tom-kwon.jpg" alt="Portrait of Tom Kwon" width="220" height="242">
      <p class="sb-name">Tom Kwon</p>
      <p class="sb-role"><em>Assistant Professor</em><br>Strategy &amp; Entrepreneurship<br>UCL School of Management</p>
      <ul class="sb-links">
        <li>{icon("pin")}<span>London, UK</span></li>
        <li>{icon("mail")}<a href="mailto:tom.kwon@ucl.ac.uk">tom.kwon@ucl.ac.uk</a></li>
        <li>{icon("school")}<a href="https://www.mgmt.ucl.ac.uk/people/tomkwon">UCL profile</a></li>
        <li>{icon("scholar")}<a href="https://scholar.google.com/citations?user=ItulQVQAAAAJ&amp;hl=en">Google Scholar</a></li>
        <li>{icon("file")}<a href="{CV}">Curriculum vitae</a></li>
      </ul>
      <a class="sb-logo" href="https://www.mgmt.ucl.ac.uk/"><img src="assets/ucl-som-logo.png" alt="UCL School of Management" width="120" height="40"></a>
    </aside>"""


def nav(active):
    items = [(f, label) for f, label, _ in PAGES] + [(CV, "CV")]
    cls = ' class="active"'
    return "\n".join(
        f'      <a href="{href}"{cls if label == active else ""}>{label}</a>'
        for href, label in items)


TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="Tom Kwon is an Assistant Professor of Strategy &amp; Entrepreneurship at UCL School of Management, studying technology management and industry emergence.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&family=Source+Sans+3:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">
<link rel="icon" href="assets/favicon-32.png" sizes="32x32" type="image/png">
<link rel="icon" href="assets/favicon-64.png" sizes="64x64" type="image/png">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<link rel="stylesheet" href="style.css">
</head>
<body>

<header class="site-header">
  <div class="shell header-inner">
    <a class="site-name" href="index.html">Tom Kwon</a>
    <nav>
{nav}
    </nav>
  </div>
</header>

<div class="shell layout">
    {sidebar}

    <main>
{body}
    </main>
</div>

<footer class="shell site-footer">
  <p>© 2026 Tom Kwon</p>
</footer>

</body>
</html>
"""

for fname, label, title in PAGES:
    body = (ROOT / "_src" / fname).read_text().rstrip()
    html = TEMPLATE.format(title=title, nav=nav(label), sidebar=SIDEBAR, body=body)
    (ROOT / fname).write_text(html)
    print("built", fname)
