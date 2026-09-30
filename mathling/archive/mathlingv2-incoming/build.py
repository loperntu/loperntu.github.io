#!/usr/bin/env python3
"""
build.py — Convert the bilingual book sources into HTML.

Usage:
    python3 build.py                        # build every language whose source exists
                                            #   book.md    → temp/book.html     (English)
                                            #   book.zh.md → temp/book-zh.html  (繁體中文)
    python3 build.py mybook.md out.html     # custom paths (language: en)
    python3 build.py mybook.md out.html zh  # custom paths, explicit language

Requires: Python 3.8+ (no external dependencies)

Markdown conventions recognised:
    ---                          YAML front-matter (title, subtitle, author, date)
    <!-- part: Label -->         Sidebar group heading
    # Chapter N. Title {#id}     Chapter heading  (→ nav link + <article>)
    # Appendix A. Title {#id}    Appendix heading
    # Title {#id .unnumbered}    Unnumbered chapter (Preface, Bibliography…)
    ### N.M Section Title        Section (gets id="sec-N-M" so EN/ZH anchors match)
    #### Sub-heading             Sub-section
    > quote / > — Attribution    Epigraph (first block, or tagged {.epigraph})
    > ... {.example}             Centered example sentence
    > ... {.deep-dive[: Title]}  Deep-dive box   (multi-paragraph OK)
    > ... {.intuition[: Title]}  Intuition / analogy box (multi-paragraph OK)
    ```lang ... ```              Fenced code (blank lines inside are safe)
    <div|figure|table|section…>  Raw HTML block (kept verbatim; blank lines safe)
    $...$  and  $$...$$          LaTeX math (passed through for KaTeX)
    - item / 1. item             Lists
    **bold** *italic* `code` [text](url)
"""

import re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TEMPLATE = HERE / "template.html"

UI = {
    "en": dict(
        html_lang="en", cover="Cover", chapter="Chapter {n}", appendix="Appendix {x}",
        intuition="Intuition", deep_dive="Deep dive", q_open="\u201c", q_close="\u201d",
        book="Book", nav_aria="Toggle navigation", top_aria="Back to top",
        source="Source", page="book.html",
    ),
    "zh": dict(
        html_lang="zh-Hant", cover="封面", chapter="第 {n} 章", appendix="附錄 {x}",
        intuition="直覺", deep_dive="深入", q_open="「", q_close="」",
        book="本書", nav_aria="切換目錄", top_aria="回到頂端",
        source="原始檔", page="book-zh.html",
    ),
}
DEFAULT_JOBS = [("book.md", "temp/book.html", "en"), ("book.zh.md", "temp/book-zh.html", "zh")]

RAW_TAGS = ("div", "figure", "table", "section", "style", "script", "svg", "details")


# ─── Inline Markdown → HTML ─────────────────────────
def inline(text):
    """Convert inline markdown to HTML, preserving LaTeX math and code spans."""
    saved = []

    def keep(s):
        saved.append(s)
        return f"\x00K{len(saved)-1}\x00"

    text = re.sub(r"\$\$.*?\$\$", lambda m: keep(m.group(0)), text, flags=re.DOTALL)
    text = re.sub(r"(?<!\\)\$(?!\$).+?(?<!\\)\$", lambda m: keep(m.group(0)), text)
    text = re.sub(r"`([^`]+?)`", lambda m: keep("<code>" + m.group(1).replace("&", "&amp;").replace("<", "&lt;") + "</code>"), text)

    text = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", r'<a href="\2">\1</a>', text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text, flags=re.DOTALL)
    text = re.sub(r"(?<![A-Za-z0-9*\\])\*(?![\s*])(.+?)(?<![\s*])\*(?![A-Za-z0-9*])", r"<em>\1</em>", text, flags=re.DOTALL)

    for _ in range(2):  # code spans may contain saved math
        text = re.sub(r"\x00K(\d+)\x00", lambda m: saved[int(m.group(1))], text)
    return text


# ─── Protect fenced code + raw HTML blocks from paragraph splitting ──
def protect_blocks(content):
    lines = content.split("\n")
    out, saved, i = [], [], 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("```"):
            lang = line[3:].strip()
            j = i + 1
            while j < len(lines) and not lines[j].startswith("```"):
                j += 1
            code = "\n".join(lines[i + 1:j]).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            cls = f' class="language-{lang}"' if lang else ""
            saved.append(f"<pre><code{cls}>{code}</code></pre>")
            out += ["", f"\x00B{len(saved)-1}\x00", ""]
            i = j + 1
            continue
        m = re.match(r"^<(%s)\b" % "|".join(RAW_TAGS), line)
        if m:
            tag, depth, j = m.group(1), 0, i
            while j < len(lines):
                depth += len(re.findall(r"<%s\b" % tag, lines[j])) - len(re.findall(r"</%s>" % tag, lines[j]))
                if depth <= 0:
                    break
                j += 1
            block = "\n".join(lines[i:j + 1])
            if tag == "table":
                block = f'<div class="tbl-wrap">{block}</div>'
            saved.append(block)
            out += ["", f"\x00B{len(saved)-1}\x00", ""]
            i = j + 1
            continue
        out.append(line)
        i += 1
    return "\n".join(out), saved


def render_list(block, ordered):
    pat = r"\n\s*\d+\.\s" if ordered else r"\n\s*[-*•]\s"
    items = [it.strip() for it in re.split(pat, "\n" + block) if it.strip()]
    tag = "ol" if ordered else "ul"
    lis = "\n".join("  <li>" + inline(re.sub(r"\s*\n\s*", " ", it)) + "</li>" for it in items)
    return f"<{tag}>\n{lis}\n</{tag}>"


def render_blocks(content, ui, saved, first_is_epigraph=False):
    html_blocks = []
    blocks = [b.strip() for b in re.split(r"\n\s*\n", content) if b.strip()]
    for idx, block in enumerate(blocks):
        m = re.fullmatch(r"\x00B(\d+)\x00", block)
        if m:
            html_blocks.append(saved[int(m.group(1))])
            continue

        img = re.match(r"^!\[([^\]]*)\]\(([^)]+)\)\s*$", block)
        if img:
            alt, src = img.group(1), img.group(2)
            cap = f"<figcaption>{inline(alt)}</figcaption>" if alt else ""
            html_blocks.append(f'<figure class="fig"><img src="{src}" alt="{alt}" loading="lazy">{cap}</figure>')
            continue

        if block.startswith("$$") and block.endswith("$$"):
            html_blocks.append(block)
            continue

        if block.startswith(">"):
            html_blocks.append(render_quote(block, ui, saved, first_is_epigraph and idx == 0))
            continue

        h = re.match(r"^(#{3,4})\s+(.+)$", block)
        if h and "\n" not in block:
            level, title = len(h.group(1)), h.group(2).strip()
            if level == 4:
                html_blocks.append(f"<h4>{inline(title)}</h4>")
                continue
            num = re.match(r"^(\d+\.\d+)\s+(.*)", title)
            if num:
                sid = "sec-" + num.group(1).replace(".", "-")
                html_blocks.append(f'<h3 id="{sid}"><span class="section-num">{num.group(1)}</span> {inline(num.group(2))}</h3>')
            else:
                html_blocks.append(f"<h3>{inline(title)}</h3>")
            continue

        if re.match(r"^[-*•]\s", block):
            html_blocks.append(render_list(block, False))
            continue
        if re.match(r"^\d+\.\s", block):
            html_blocks.append(render_list(block, True))
            continue

        html_blocks.append(f"<p>{inline(block)}</p>")
    return "\n".join(html_blocks)


def render_quote(block, ui, saved, is_first):
    tag_line, body = "", []
    for bl in block.split("\n"):
        s = bl.strip()
        if s.startswith("{.") and s.endswith("}"):
            tag_line = s
        else:
            body.append(re.sub(r"^>\s?", "", bl))
    text = "\n".join(body).strip()
    tm = re.match(r"\{\.([\w-]+)(?::\s*(.+?))?\}", tag_line)
    kind = tm.group(1) if tm else ("epigraph" if is_first else "quote")
    title = tm.group(2) if tm and tm.group(2) else ""

    if kind in ("deep-dive", "intuition"):
        label = title or (ui["intuition"] if kind == "intuition" else ui["deep_dive"])
        inner = render_blocks(text, ui, saved)
        return f'<div class="{kind}"><div class="box-label">{inline(label)}</div>\n{inner}\n</div>'
    if kind == "example":
        return f'<div class="example-block"><p>{inline(text)}</p></div>'
    if kind == "epigraph":
        am = re.search(r"\n\s*[—–]\s*(.+)$", text)
        quote, attribution = (text[:am.start()], am.group(1).strip()) if am else (text, "")
        quote = quote.strip().strip('"\u201c\u201d\u300c\u300d').strip()
        out = f'<div class="epigraph">\n  <p>{ui["q_open"]}{inline(quote)}{ui["q_close"]}</p>\n'
        if attribution:
            out += f'  <div class="attribution">— {inline(attribution)}</div>\n'
        return out + "</div>"
    return f"<blockquote>{render_blocks(text, ui, saved)}</blockquote>"


def build(src, out, lang):
    ui = UI[lang]
    md = src.read_text(encoding="utf-8")
    template = TEMPLATE.read_text(encoding="utf-8")

    meta = {}
    fm = re.match(r"^---\n(.*?)\n---\n", md, re.DOTALL)
    if fm:
        for line in fm.group(1).splitlines():
            if ":" in line and not line.startswith(" "):
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip().strip('"').strip("'")
        md = md[fm.end():]

    md = re.sub(r"<!--(?!\s*part:).*?-->", "", md, flags=re.DOTALL)
    md, saved = protect_blocks(md)

    parts = re.split(r"^(<!--\s*part:.*?-->|# .*)$", md, flags=re.MULTILINE)
    nav = [f'    <a class="nav-link" href="#cover">{ui["cover"]}</a>']
    body = []
    i = 1
    while i < len(parts):
        sep, content = parts[i], parts[i + 1] if i + 1 < len(parts) else ""
        i += 2
        pm = re.match(r"<!--\s*part:\s*(.+?)\s*-->", sep)
        if pm:
            nav.append(f'    <div class="nav-part-label">{pm.group(1)}</div>')
            continue
        hm = re.match(r"^#\s+(.+?)(?:\s*\{([^}]*)\})?\s*$", sep)
        if not hm:
            continue
        raw_title, attrs = hm.group(1).strip(), hm.group(2) or ""
        idm = re.search(r"#([\w-]+)", attrs)
        unnumbered = ".unnumbered" in attrs

        ch = re.match(r"Chapter\s+(\d+)\.\s*(.*)", raw_title)
        ap = re.match(r"Appendix\s+(\w+)\.\s*(.*)", raw_title)
        if ch:
            n, title = ch.group(1), ch.group(2).strip()
            cid = idm.group(1) if idm else f"ch{n}"
            label = ui["chapter"].format(n=n)
            nav_text = f'<span class="ch-num">{n}</span> {inline(title)}'
        elif ap:
            x, title = ap.group(1), ap.group(2).strip()
            cid = idm.group(1) if idm else f"appendix-{x.lower()}"
            label = ui["appendix"].format(x=x)
            nav_text = inline(title)
        else:
            title = raw_title
            cid = idm.group(1) if idm else re.sub(r"\W+", "-", raw_title.lower()).strip("-")
            label = raw_title if unnumbered else ""
            nav_text = inline(title)
        nav.append(f'    <a class="nav-link" href="#{cid}">{nav_text}</a>')

        is_bib = "bibliography" in cid.lower() or "bibliography" in raw_title.lower()
        cls = "chapter bib-section" if is_bib else "chapter"
        html = f'<article class="{cls}" id="{cid}">\n'
        if label:
            html += f'  <div class="chapter-label">{label}</div>\n'
        html += f'  <h2 class="chapter-title">{inline(title)}</h2>\n'
        html += render_blocks(content.strip(), ui, saved, first_is_epigraph=True)
        html += "\n</article>\n"
        body.append(html)

    fills = {
        "TITLE": meta.get("title", "Untitled"), "SUBTITLE": meta.get("subtitle", ""),
        "AUTHOR": meta.get("author", ""), "DATE": meta.get("date", ""),
        "NAV": "\n".join(nav), "BODY": "\n\n".join(body),
        "HTML_LANG": ui["html_lang"], "LANG": lang,
        "UI_BOOK": ui["book"], "UI_NAV_ARIA": ui["nav_aria"], "UI_TOP_ARIA": ui["top_aria"],
        "UI_SOURCE": ui["source"], "SRC_NAME": src.name,
        "EN_CURRENT": "current" if lang == "en" else "", "ZH_CURRENT": "current" if lang == "zh" else "",
        "EN_PAGE": UI["en"]["page"], "ZH_PAGE": UI["zh"]["page"],
    }
    output = template
    for k, v in fills.items():
        output = output.replace("{{" + k + "}}", v)

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(output, encoding="utf-8")
    print(f"✓ [{lang}] {src.name} → {out}  ({len(body)} chapters)")


if __name__ == "__main__":
    if len(sys.argv) > 2:
        build(Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3] if len(sys.argv) > 3 else "en")
    else:
        for s, o, lang in DEFAULT_JOBS:
            src = HERE / s
            if src.exists():
                build(src, HERE / o, lang)
            else:
                print(f"· skipped {s} (not found)")
