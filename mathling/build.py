#!/usr/bin/env python3
"""
build.py — Convert book.md → temp/book.html

Usage:
    python3 build.py                      # defaults: book.md → temp/book.html
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
    $...$  and  $$...$$          LaTeX math (passed through for KaTeX)
    - item / 1. item             Lists
    **bold**  *italic*  `code`   Inline formatting
"""

import re, sys, textwrap
from pathlib import Path

# ─── Paths ───────────────────────────────────────────
SRC      = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("book.md")
OUT      = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("temp/book.html")
TEMPLATE = Path("template.html")

# ─── Read inputs ─────────────────────────────────────
md_text  = SRC.read_text(encoding="utf-8")
template = TEMPLATE.read_text(encoding="utf-8")

# ─── Parse YAML front-matter ─────────────────────────
meta = {}
fm_match = re.match(r'^---\n(.*?)\n---\n', md_text, re.DOTALL)
if fm_match:
    for line in fm_match.group(1).splitlines():
        if ':' in line:
            k, v = line.split(':', 1)
            meta[k.strip()] = v.strip().strip('"').strip("'")
    md_text = md_text[fm_match.end():]

title    = meta.get('title', 'Untitled')
subtitle = meta.get('subtitle', '')
date     = meta.get('date', '')
author   = meta.get('author', '')

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
        
        # ─── Raw HTML block (starts with <) ──────────
        if block.startswith('<div') or block.startswith('<section') or block.startswith('<style') or block.startswith('<script'):
            html_blocks.append(block)
            is_first_block = False
            continue
        
        # ─── Fenced code block (```...```) ───────────
        if block.startswith('```'):
            lang_match = re.match(r'^```(\w*)\n', block)
            lang = lang_match.group(1) if lang_match else ''
            code_content = re.sub(r'^```\w*\n', '', block)
            code_content = re.sub(r'\n```$', '', code_content)
            code_content = code_content.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            html_blocks.append(f'<pre><code>{code_content}</code></pre>')
            is_first_block = False
            continue
        
        # ─── Image ![alt](url) ───────────────────────
        img_match = re.match(r'^!\[([^\]]*)\]\(([^)]+)\)\s*$', block)
        if img_match:
            alt = img_match.group(1)
            src = img_match.group(2)
            html_blocks.append(f'<img src="{src}" alt="{alt}" loading="lazy">')
            is_first_block = False
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
            is_example = '{.example' in tag_line
            is_epigraph = '{.epigraph}' in tag_line or (is_first_block and not is_example and '{.deep-dive}' not in tag_line)
            is_deep_dive = '{.deep-dive}' in tag_line
            
            if is_deep_dive:
                html_blocks.append(
                    f'<div class="deep-dive">{inline(bq_text)}</div>'
                )
            elif is_example:
                html_blocks.append(
                    f'<div class="example-block"><p>{inline(bq_text)}</p></div>'
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

output = template
output = output.replace('{{TITLE}}', title)
output = output.replace('{{SUBTITLE}}', subtitle)
output = output.replace('{{AUTHOR}}', author)
output = output.replace('{{DATE}}', date)
output = output.replace('{{NAV}}', nav_html)
output = output.replace('{{BODY}}', body_html)

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(output, encoding='utf-8')
print(f"✓ Built {OUT}  ({len(body_parts)} chapters, {len(nav_items)} nav items)")
print(f"  Source:   {SRC}")
print(f"  Template: {TEMPLATE}")
print(f"  Output:   {OUT}")
