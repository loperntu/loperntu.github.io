#!/usr/bin/env python3
"""
build.py — Convert book.md → geometry_of_grammar.html

Usage:
    python3 build.py                      # defaults: book.md → geometry_of_grammar.html
    python3 build.py mybook.md out.html   # custom paths

Requires: Python 3.8+ (no external dependencies!)

Markdown conventions recognised:
    ---                          YAML front-matter (title, subtitle, date)
    <!-- part: Label -->         Sidebar group heading
    # Chapter N. Title {#id}     Chapter heading  (→ nav link + <article>)
    # Title {.unnumbered}        Unnumbered chapter (Preface, Bibliography…)
    ### Section Title             Section within chapter
    > quote\\n> — Attribution     Blockquote; becomes epigraph if first in chapter
    > *italic sentence*          Example sentence block (if tagged {.example})
    > ... {.deep-dive} or        Deep-dive aside block (optional {.deep-dive: Title})
    $...$  and  $$...$$          LaTeX math (passed through for KaTeX)
    - item / 1. item             Lists
    **bold**  *italic*  `code`   Inline formatting
"""

import re, sys, textwrap
from pathlib import Path

# ─── Paths ───────────────────────────────────────────
SRC      = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("book.md")
OUT      = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("geometry_of_grammar.html")
TEMPLATE = Path("template.html")

# ─── Read inputs ─────────────────────────────────────
md_text  = SRC.read_text(encoding="utf-8")
template = TEMPLATE.read_text(encoding="utf-8")

# ─── Parse YAML front-matter ─────────────────────────
meta = {}
fm_match = re.match(r'^---\n(.*?)\n---\n', md_text, re.DOTALL)
if fm_match:
    lines = fm_match.group(1).splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if stripped.startswith('#') or ':' not in line:
            i += 1
            continue
        k, v = line.split(':', 1)
        key, val = k.strip(), v.strip()
        # Multi-line value: key: "line1\nline2" or key: "line1 (no closing quote, next line continues)
        if (val.startswith('"') or val.startswith("'")) and len(val) > 1 and val[-1] not in '"\'':
            i += 1
            while i < len(lines) and val[-1] not in '"\'':
                val += '\n' + lines[i]
                i += 1
        val = val.strip('"').strip("'")
        if key == 'title' and not val:
            i += 1
            continue
        meta[key] = val
        i += 1
    md_text = md_text[fm_match.end():]

title        = meta.get('title') or 'Untitled'
subtitle     = meta.get('subtitle', '')
author       = meta.get('author', '')
# Allow line breaks in affiliation: use <br> or \n in the value
affiliation  = (meta.get('affiliation', '')
                .replace('\\n', '<br>')
                .replace('\n', '<br>'))
date         = meta.get('date', '')

# ─── Strip HTML comments (except <!-- part: ... -->) ─
md_text = re.sub(r'<!--(?!\s*part:).*?-->', '', md_text, flags=re.DOTALL)

# ─── Inline Markdown → HTML ─────────────────────────
def inline(text):
    """Convert inline markdown to HTML, preserving LaTeX math."""
    # Protect math spans from further processing
    math_spans = []
    def save_math(m):
        math_spans.append(m.group(0))
        return f'\x00MATH{len(math_spans)-1}\x00'
    
    text = re.sub(r'\$\$.*?\$\$', save_math, text, flags=re.DOTALL)
    text = re.sub(r'\$(?!\$).*?\$', save_math, text)
    
    # Inline formatting
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    text = re.sub(r'`(.+?)`', r'<code>\1</code>', text)
    
    # Restore math
    for i, m in enumerate(math_spans):
        text = text.replace(f'\x00MATH{i}\x00', m)
    
    return text

# ─── Split into chapters ─────────────────────────────
# Each chapter starts with "# ..."
chunks = re.split(r'^(?=# )', md_text, flags=re.MULTILINE)
chunks = [c.strip() for c in chunks if c.strip()]

nav_items = []      # list of (type, text, id)  type = 'link' | 'part'
body_parts = []     # list of HTML strings

chapter_counter = 0

for chunk in chunks:
    lines = chunk.split('\n')
    
    # ─── Check for part comment before this chunk ────
    # (handled inline below)
    
    # ─── Parse heading line ──────────────────────────
    heading_line = lines[0]
    heading_match = re.match(r'^#\s+(.+?)(?:\s*\{([^}]*)\})?\s*$', heading_line)
    if not heading_match:
        continue  # skip non-chapter content
    
    raw_title = heading_match.group(1).strip()
    attrs = heading_match.group(2) or ''
    
    # Extract id
    id_match = re.search(r'#(\S+)', attrs)
    unnumbered = '.unnumbered' in attrs
    bib_class = 'bib-section' if 'bibliography' in raw_title.lower() else ''
    
    # Parse "Chapter N. Title" pattern
    ch_match = re.match(r'Chapter\s+(\d+)\.\s*(.*)', raw_title)
    if ch_match:
        ch_num = int(ch_match.group(1))
        ch_title = ch_match.group(2).strip()
        ch_id = id_match.group(1) if id_match else f'ch{ch_num}'
        label = f'Chapter {ch_num}'
        nav_text = f'<span class="ch-num">{ch_num}</span> {ch_title}'
    else:
        ch_num = None
        ch_title = raw_title
        ch_id = id_match.group(1) if id_match else re.sub(r'\W+', '-', raw_title.lower()).strip('-')
        label = raw_title if unnumbered else ''
        if 'Appendix' in raw_title:
            label = 'Appendix A'
            ch_title = re.sub(r'^Appendix\s+\w+\.\s*', '', raw_title)
        nav_text = ch_title
    
    # ─── Check for part labels in surrounding text ───
    # Look for <!-- part: ... --> in the content before this chunk
    part_idx = md_text.find(chunk)
    if part_idx > 0:
        preceding = md_text[max(0, part_idx - 200):part_idx]
        part_match = re.search(r'<!--\s*part:\s*(.+?)\s*-->', preceding)
        if part_match:
            nav_items.append(('part', part_match.group(1)))
    
    # Add nav link
    nav_items.append(('link', nav_text, ch_id))
    
    # ─── Process body content ────────────────────────
    content_lines = lines[1:]
    content = '\n'.join(content_lines).strip()
    
    # Process blocks
    html_blocks = []
    
    # Split content into paragraphs / blocks
    # We process: blockquotes, headings (###), display math, lists, paragraphs
    
    blocks = re.split(r'\n{2,}', content)
    
    is_first_block = True
    in_list = False
    
    for block in blocks:
        block = block.strip()
        if not block:
            continue
        
        # ─── Display math block (standalone $$...$$) ─
        if block.startswith('$$') and block.endswith('$$'):
            html_blocks.append(block)  # KaTeX auto-render handles this
            is_first_block = False
            continue
        
        # ─── Blockquote (epigraph or example) ────────
        if block.startswith('>'):
            bq_lines = []
            tag_line = ''
            for bl in block.split('\n'):
                if bl.strip().startswith('{.'):
                    tag_line = bl.strip()
                elif bl.startswith('>'):
                    bq_lines.append(re.sub(r'^>\s?', '', bl))
                else:
                    bq_lines.append(bl)
            
            bq_text = '\n'.join(bq_lines).strip()
            is_example = '{.example}' in tag_line
            is_deep_dive = '{.deep-dive' in tag_line
            is_epigraph = '{.epigraph}' in tag_line or (is_first_block and not is_example and not is_deep_dive)
            
            if is_example:
                html_blocks.append(
                    f'<div class="example-block"><p>{inline(bq_text)}</p></div>'
                )
            elif is_deep_dive:
                # Optional title: {.deep-dive} or {.deep-dive: Title}
                dd_title = ''
                dd_title_match = re.search(r'\{\.deep-dive(?:\s*:\s*([^}]+))?\}', tag_line)
                if dd_title_match and dd_title_match.group(1):
                    dd_title = dd_title_match.group(1).strip()
                paras = [p.strip() for p in bq_text.split('\n\n') if p.strip()]
                body_html = '\n'.join(f'  <p>{inline(p)}</p>' for p in paras)
                if dd_title:
                    html_blocks.append(
                        f'<div class="deep-dive">\n'
                        f'  <div class="deep-dive-title">{inline(dd_title)}</div>\n'
                        f'  {body_html}\n'
                        f'</div>'
                    )
                else:
                    html_blocks.append(
                        f'<div class="deep-dive">\n{body_html}\n</div>'
                    )
            elif is_epigraph:
                # Split quote from attribution
                attr_match = re.search(r'\n\s*—\s*(.+)$', bq_text)
                if attr_match:
                    quote = bq_text[:attr_match.start()].strip()
                    attribution = attr_match.group(1).strip()
                    html_blocks.append(
                        f'<div class="epigraph">\n'
                        f'  <p>"{inline(quote)}"</p>\n'
                        f'  <div class="attribution">— {inline(attribution)}</div>\n'
                        f'</div>'
                    )
                else:
                    html_blocks.append(
                        f'<div class="epigraph"><p>{inline(bq_text)}</p></div>'
                    )
            else:
                html_blocks.append(f'<blockquote><p>{inline(bq_text)}</p></blockquote>')
            is_first_block = False
            continue
        
        # ─── Section heading (###) ───────────────────
        h3_match = re.match(r'^###\s+(.+)', block)
        if h3_match:
            sec_title = h3_match.group(1).strip()
            # Check for "N.M" pattern
            num_match = re.match(r'^(\d+\.\d+)\s+(.*)', sec_title)
            if num_match:
                sec_num = num_match.group(1)
                sec_rest = num_match.group(2)
                html_blocks.append(
                    f'<h3><span class="section-num">{sec_num}</span> {inline(sec_rest)}</h3>'
                )
            else:
                html_blocks.append(f'<h3>{inline(sec_title)}</h3>')
            is_first_block = False
            continue
        
        # ─── Unordered list ──────────────────────────
        if re.match(r'^[-*]\s', block):
            items = re.split(r'\n[-*]\s', '\n' + block)
            items = [it.strip() for it in items if it.strip()]
            li_html = '\n'.join(f'  <li>{inline(it)}</li>' for it in items)
            html_blocks.append(f'<ul>\n{li_html}\n</ul>')
            is_first_block = False
            continue
        
        # ─── Ordered list ────────────────────────────
        if re.match(r'^\d+\.\s', block):
            items = re.split(r'\n\d+\.\s', '\n' + block)
            items = [it.strip() for it in items if it.strip()]
            li_html = '\n'.join(f'  <li>{inline(it)}</li>' for it in items)
            html_blocks.append(f'<ol>\n{li_html}\n</ol>')
            is_first_block = False
            continue
        
        # ─── Image (Markdown ![](url) or ![alt](url)) ─
        img_match = re.match(r'^!\[([^\]]*)\]\(([^)]+)\)\s*$', block.strip())
        if img_match:
            alt_text = img_match.group(1).strip()
            src = img_match.group(2).strip()
            html_blocks.append(
                f'<figure class="book-figure">\n'
                f'  <img src="{src}" alt="{alt_text}" loading="lazy">\n'
                f'</figure>'
            )
            is_first_block = False
            continue
        
        # ─── Regular paragraph ───────────────────────
        html_blocks.append(f'<p>{inline(block)}</p>')
        is_first_block = False
    
    # ─── Assemble chapter HTML ───────────────────────
    extra_class = f' {bib_class}' if bib_class else ''
    chapter_html = f'<article class="chapter{extra_class}" id="{ch_id}">\n'
    if label:
        chapter_html += f'  <div class="chapter-label">{label}</div>\n'
    chapter_html += f'  <h2 class="chapter-title">{inline(ch_title)}</h2>\n'
    chapter_html += '\n'.join(html_blocks)
    chapter_html += '\n</article>\n'
    
    body_parts.append(chapter_html)


# ─── Build navigation HTML ───────────────────────────
nav_html_parts = ['    <a class="nav-link" href="#cover">Cover</a>']
for item in nav_items:
    if item[0] == 'part':
        nav_html_parts.append(f'    <div class="nav-part-label">{item[1]}</div>')
    else:
        _, text, anchor = item
        nav_html_parts.append(f'    <a class="nav-link" href="#{anchor}">{text}</a>')

nav_html = '\n'.join(nav_html_parts)

# ─── Fill template ───────────────────────────────────
body_html = '\n\n'.join(body_parts)

# Ensure title is never empty (e.g. if front-matter was misparsed)
if not title or not title.strip():
    title = 'Untitled'

output = template
output = output.replace('{{NAV}}', nav_html)
output = output.replace('{{BODY}}', body_html)
# Replace meta placeholders last so they apply to the full document
output = output.replace('{{TITLE}}', title)
output = output.replace('{{SUBTITLE}}', subtitle)
output = output.replace('{{AUTHOR}}', author)
output = output.replace('{{AFFILIATION}}', affiliation)
output = output.replace('{{DATE}}', date)

OUT.write_text(output, encoding='utf-8')
print(f"✓ Built {OUT}  ({len(body_parts)} chapters, {len(nav_items)} nav items)")
print(f"  Source:   {SRC}")
print(f"  Template: {TEMPLATE}")
print(f"  Output:   {OUT}")
