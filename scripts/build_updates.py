#!/usr/bin/env python3
"""Convert the updates/ markdown notes into doragum-themed HTML.

Why this exists
---------------
The supplementary notes are authored as plain Markdown with LaTeX math
(`$...$` inline, `$$...$$` display). The site renders them as standalone pages
sharing css/doragum.css and a vendored KaTeX that renders the math live in the
browser -- no CDN, no pre-rendered math. This script does that conversion so the
Markdown stays the single source of truth.

The one non-trivial step is math protection: a Markdown processor would eat the
underscores and asterisks inside TeX (e.g. `$\\kappa_1 U(t)$`) as emphasis. So we
pull every math span out before Markdown runs and paste it back verbatim after,
leaving the raw `$...$` for KaTeX to render client-side.

Everything else is a fixed template plus a few per-page values (header label,
meta description, ...) read from updates/build-manifest.json. Title, subtitle,
whether the page needs KaTeX, and whether it has footnotes are all inferred from
the content.

Usage
-----
    python scripts/build_updates.py            # build every page in the manifest
    python scripts/build_updates.py --check     # build to memory, diff vs on-disk, exit 1 if stale
    python scripts/build_updates.py <slug|source.md> [...]   # build only these

Requires: markdown (see scripts/requirements.txt). Run inside the venv.
"""

from __future__ import annotations

import argparse
import difflib
import html
import json
import re
import sys
from pathlib import Path

import markdown

REPO_ROOT = Path(__file__).resolve().parent.parent
UPDATES_DIR = REPO_ROOT / "updates"
MANIFEST_PATH = UPDATES_DIR / "build-manifest.json"

# --- defaults a page inherits unless the manifest overrides them ----------------
DEFAULT_LABEL = "SUPPLEMENTARY NOTE"
DEFAULT_NAV_LABEL = "The Paper"
DEFAULT_NAV_HREF = "../index.html"
DEFAULT_FOOTER_NOTE = "A supplementary note to the GUM of DevOps"
SITE_SUFFIX = "The GUM of DevOps"

# --- 7-bit output ---------------------------------------------------------------
# The output files are kept pure ASCII (no byte > 0x7F). Typographic glyphs are
# encoded the 7-bit-safe way: HTML named entities in markup, and a CSS unicode
# escape for the one glyph that lives inside a `content:` string (see build_style).
NAMED_ENTITIES = {
    "—": "&mdash;", "–": "&ndash;", "…": "&hellip;",
    "‘": "&lsquo;", "’": "&rsquo;", "“": "&ldquo;", "”": "&rdquo;",
    "·": "&middot;", "→": "&rarr;", "←": "&larr;",
    " ": "&nbsp;", "−": "&minus;", "×": "&times;",
}


def ascii_harden(s: str) -> str:
    """Replace every non-ASCII char with an HTML entity (named where known)."""
    return "".join(
        ch if ord(ch) < 0x80 else NAMED_ENTITIES.get(ch, f"&#x{ord(ch):04X};")
        for ch in s
    )


# --------------------------------------------------------------------------------
# Math protection: stash math spans behind placeholders Markdown won't touch,
# then restore them verbatim after conversion.
# --------------------------------------------------------------------------------
DISPLAY_RE = re.compile(r"\$\$(.+?)\$\$", re.DOTALL)
# inline $...$ that is not part of a $$ delimiter and has no newline inside
INLINE_RE = re.compile(r"(?<!\$)\$(?!\$)([^\n]+?)(?<!\$)\$(?!\$)")

# A lone block-level tag is preserved verbatim by Python-Markdown (htmlStash),
# so display math survives outside any <p>. Inline uses a pure-alnum token that
# passes through emphasis/smartypants unchanged.
DISPLAY_PH = '<div class="ktx-display-ph" data-i="{i}"></div>'
DISPLAY_PH_RE = re.compile(r'<div class="ktx-display-ph" data-i="(\d+)"></div>')
INLINE_PH = "KTXINLINE{i}KTXEND"
INLINE_PH_RE = re.compile(r"KTXINLINE(\d+)KTXEND")


def protect_math(text: str):
    """Replace math spans with placeholders. Returns (text, display, inline)."""
    display: list[str] = []
    inline: list[str] = []

    def take_display(m: re.Match) -> str:
        display.append(m.group(0))  # keep the $$...$$ delimiters
        return DISPLAY_PH.format(i=len(display) - 1)

    def take_inline(m: re.Match) -> str:
        inline.append(m.group(0))  # keep the $...$ delimiters
        return INLINE_PH.format(i=len(inline) - 1)

    text = DISPLAY_RE.sub(take_display, text)  # display first, so $$ isn't seen as two $
    text = INLINE_RE.sub(take_inline, text)
    return text, display, inline


def restore_math(html_text: str, display: list[str], inline: list[str]) -> str:
    html_text = DISPLAY_PH_RE.sub(lambda m: display[int(m.group(1))], html_text)
    html_text = INLINE_PH_RE.sub(lambda m: inline[int(m.group(1))], html_text)
    return html_text


# --------------------------------------------------------------------------------
# Markdown -> content HTML
# --------------------------------------------------------------------------------
def render_body(md_text: str) -> str:
    # Author writes " -- " intending an em dash; smartypants would make it an en
    # dash, so convert here (spaced form never occurs inside the code diagrams).
    md_text = md_text.replace(" -- ", " — ")

    body, display, inline = protect_math(md_text)

    md = markdown.Markdown(
        extensions=["extra", "sane_lists", "smarty", "toc"],
        extension_configs={
            "smarty": {"smart_dashes": False},  # we handle dashes above
            "toc": {"permalink": False},
        },
        output_format="html5",
    )
    body = md.convert(body)
    body = restore_math(body, display, inline)

    # Promote the italic dek right under the H1 to the paper subtitle style.
    body = re.sub(
        r"(<h1[^>]*>.*?</h1>\s*)<p><em>(.*?)</em></p>",
        r'\1<p class="paper-subtitle">\2</p>',
        body,
        count=1,
        flags=re.DOTALL,
    )
    return body


# --------------------------------------------------------------------------------
# Page assembly
# --------------------------------------------------------------------------------
def first_h1_text(md_text: str) -> str:
    for line in md_text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    raise ValueError("markdown has no level-1 heading for the title")


def build_style(label: str, has_math: bool, has_footnotes: bool) -> str:
    parts = [
        "  /* Page-specific overrides on top of the shared GUT documentation theme. */",
        "  .readme-page .github-markdown-content h1:first-of-type::before {",
        # CSS unicode escape for the middle dot (U+00B7); HTML entities are not
        # honored inside a `content:` string, and we keep the file 7-bit. The
        # escape consumes one trailing whitespace as its terminator, so two
        # spaces are needed to render a visible space after the dot.
        f'    content: "THE GUM OF DEVOPS \\0000B7  {label}";',
        "  }",
        "",
        "  /* Italic dek beneath the title. Mirrors the landing page's paper subtitle. */",
        "  .readme-page .github-markdown-content .paper-subtitle {",
        "    margin: 0 0 1.8rem;",
        "    color: var(--text-dim);",
        "    font-style: italic;",
        "    font-size: 1.05rem;",
        "  }",
    ]
    if has_math:
        parts += [
            "",
            "  /* Display math (dollar-dollar delimiters) renders to .katex-display. Give it",
            "     breathing room and let very wide equations scroll horizontally on their own",
            "     rather than overflowing the page. */",
            "  .readme-page .github-markdown-content .katex-display {",
            "    margin: 1.6rem 0;",
            "    overflow-x: auto;",
            "    overflow-y: hidden;",
            "  }",
            "",
            "  /* Size math to match the surrounding text rather than KaTeX's default 1.21em. */",
            "  .readme-page .github-markdown-content .katex {",
            "    font-size: 1.11em;",
            "  }",
        ]
    parts += [
        "",
        "  /* Fenced code blocks. The shared theme styles inline <code> but leaves",
        "     <pre> to the page; give the chain/ledger listings a bordered, monospaced",
        "     card that scrolls on its own rather than overflowing the reading column. */",
        "  .readme-page .github-markdown-content pre {",
        "    margin: 1.4rem 0;",
        "    padding: 0.9rem 1.1rem;",
        "    border: 1px solid var(--border);",
        "    border-radius: 3px;",
        "    background: var(--surface);",
        "    overflow-x: auto;",
        "    line-height: 1.55;",
        "  }",
        "",
        "  /* Reset the inline-code chrome inside a block so we don't double-border. */",
        "  .readme-page .github-markdown-content pre code {",
        "    padding: 0;",
        "    border: 0;",
        "    border-radius: 0;",
        "    background: none;",
        "    font-size: 0.86em;",
        "  }",
        "",
        "  /* Footer mirrors the landing page's: a horizontal meta / links bar driven",
        "     by the shared unscoped footer/.footer-meta/.paper-links rules, with the",
        "     content-scoped link colors restored. */",
        "  .readme-page .github-markdown-content footer {",
        "    margin-top: 3rem;",
        "    padding-left: 0;",
        "    padding-right: 0;",
        "  }",
        "",
        "  .readme-page .github-markdown-content .footer-meta a,",
        "  .readme-page .github-markdown-content .paper-links a {",
        "    color: var(--accent-dim);",
        "    text-decoration: none;",
        "  }",
        "",
        "  .readme-page .github-markdown-content .paper-links .paper-link-primary {",
        "    color: var(--accent);",
        "    font-weight: 500;",
        "  }",
        "",
        "  .readme-page .github-markdown-content .footer-meta a:hover,",
        "  .readme-page .github-markdown-content .paper-links a:hover {",
        "    color: var(--accent);",
        "  }",
        "",
        "  .readme-nav-actions {",
        "    display: flex;",
        "    flex: 0 0 auto;",
        "    gap: 0.5rem;",
        "  }",
    ]
    if has_footnotes:
        parts += [
            "",
            "  /* Footnotes (Python-Markdown emits a .footnote block). Small-print notes",
            "     above the footer, separated by a rule. */",
            "  .readme-page .github-markdown-content .footnote,",
            "  .readme-page .github-markdown-content .footnotes {",
            "    margin-top: 2.6rem;",
            "    padding-top: 1rem;",
            "    border-top: 1px solid var(--border);",
            "    font-size: 0.85rem;",
            "    color: var(--text-dim);",
            "  }",
            "  .readme-page .github-markdown-content .footnote hr,",
            "  .readme-page .github-markdown-content .footnotes hr {",
            "    display: none;",
            "  }",
            "  .readme-page .github-markdown-content .footnote ol {",
            "    margin: 0;",
            "    padding-left: 1.2rem;",
            "  }",
            "  .readme-page .github-markdown-content .footnote li {",
            "    margin: 0.3rem 0;",
            "  }",
        ]
    return "\n".join(parts)


def assemble(page: dict, md_text: str) -> str:
    title = page.get("title") or first_h1_text(md_text)
    label = page.get("label", DEFAULT_LABEL)
    nav_label = page.get("nav_label", DEFAULT_NAV_LABEL)
    nav_href = page.get("nav_href", DEFAULT_NAV_HREF)
    footer_note = page.get("footer_note", DEFAULT_FOOTER_NOTE)

    body = render_body(md_text)
    has_math = "$" in md_text
    has_footnotes = 'class="footnote' in body
    description = page.get("description") or _fallback_description(body)

    head = [
        "<!doctype html>",
        '<html lang="en">',
        "<head>",
        '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        f'<meta name="description" content="{html.escape(description, quote=True)}">',
        f"<title>{html.escape(title)} — {SITE_SUFFIX}</title>",
    ]
    if has_math:
        head += [
            "<!-- Math is authored as LaTeX (dollar-dollar for display, single-dollar for",
            "     inline) and rendered live by a vendored KaTeX — no CDN, no build step.",
            "     See the scripts just before the closing body tag. -->",
            '<link rel="stylesheet" href="../DORA/GUT/vendor/katex/katex.min.css">',
        ]
    head += ['<link rel="stylesheet" href="../css/doragum.css">']
    if has_math:
        head.append("<script>document.documentElement.classList.add('math-loading');</script>")
    head += ["<style>", build_style(label, has_math, has_footnotes), "</style>", "</head>"]

    shell = [
        '<body class="readme-page post-page">',
        '<a class="skip-link" href="#note-content">Skip to content</a>',
        '<nav class="readme-nav" aria-label="Site">',
        '    <div class="readme-nav-brand" aria-label="The GUM of DevOps">',
        '        <span class="readme-nav-mark" aria-hidden="true"><a style="color: inherit; text-decoration: none;" href="https://blehg.paperclipmaximizer.ai/GUM_of_Devops/">GUM</a></span>',
        '        <span><a style="color: inherit; text-decoration: none;" href="https://blehg.paperclipmaximizer.ai/GUM_of_Devops/">The Grand Unified Model of DevOps</a></span>',
        "    </div>",
        '    <div class="readme-nav-actions">',
        f'        <a class="readme-nav-action" href="{nav_href}">{html.escape(nav_label)}</a>',
        "    </div>",
        "</nav>",
        "<main",
        '            class="github-markdown-body"',
        '            data-color-mode="auto"',
        '            data-light-theme="light"',
        '            data-dark-theme="dark"',
        "        >",
        '            <div class="github-markdown-content" id="note-content">',
        body,
        "",
        "        <footer>",
        '            <div class="footer-meta">',
        "                <span>Scott VanRavenswaay</span>",
        '                <a href="mailto:scottvr@paperclipmaximizer.ai">scottvr@paperclipmaximizer.ai</a>',
        f"                <span>{html.escape(footer_note)}</span>",
        "            </div>",
        '            <nav class="paper-links" aria-label="Project resources">',
        '                <a class="paper-link-primary" href="../index.html">Paper</a>',
        '                <a href="../DORA/GUT/GUT.html">Tool</a>',
        '                <a href="https://github.com/scottvr/GUM_of_Devops/" target="_blank" rel="noopener noreferrer">Repository</a>',
        "            </nav>",
        "        </footer>",
        "</div>",
        "        </main>",
    ]

    scripts = []
    if has_math:
        scripts = [
            "<!-- Vendored KaTeX (0.16.11) + auto-render: turns the LaTeX in the content",
            "     into math in the browser. No CDN dependency; fonts load from ../DORA/GUT/",
            "     vendor/katex/fonts via the stylesheet above. -->",
            '<script defer src="../DORA/GUT/vendor/katex/katex.min.js"></script>',
            '<script defer src="../DORA/GUT/vendor/katex/contrib/auto-render.min.js"></script>',
            "<script>",
            "  (function () {",
            "    function reveal() { document.documentElement.classList.remove('math-loading'); }",
            "    document.addEventListener('DOMContentLoaded', function () {",
            "      if (typeof renderMathInElement === 'function') {",
            "        renderMathInElement(document.getElementById('note-content'), {",
            "          delimiters: [",
            "            { left: '$$', right: '$$', display: true },",
            "            { left: '$', right: '$', display: false },",
            "            { left: '\\\\(', right: '\\\\)', display: false }",
            "          ],",
            "          throwOnError: false",
            "        });",
            "      }",
            "      reveal();",
            "    });",
            "    // Failsafe: never leave the content hidden if a script fails to load.",
            "    setTimeout(reveal, 2000);",
            "  })();",
            "</script>",
        ]
    tail = ["</body>", "</html>"]

    # The style block's one non-ASCII glyph is already a CSS escape, so hardening
    # the whole document to 7-bit only touches HTML text/attributes.
    return ascii_harden("\n".join(head + shell + scripts + tail)) + "\n"


def _fallback_description(body: str) -> str:
    """Meta description of last resort: first paragraph's text, trimmed."""
    m = re.search(r"<p(?: class=\"paper-subtitle\")?>(.*?)</p>", body, re.DOTALL)
    if not m:
        return SITE_SUFFIX
    text = re.sub(r"<[^>]+>", "", m.group(1))
    text = re.sub(r"\s+", " ", text).strip()
    return (text[:197] + "...") if len(text) > 200 else text


# --------------------------------------------------------------------------------
# Driver
# --------------------------------------------------------------------------------
def load_manifest() -> list[dict]:
    data = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    return data["pages"]


def output_path(page: dict) -> Path:
    return UPDATES_DIR / (page.get("output") or Path(page["source"]).with_suffix(".html").name)


def build_page(page: dict) -> tuple[Path, str]:
    md_text = (UPDATES_DIR / page["source"]).read_text(encoding="utf-8")
    return output_path(page), assemble(page, md_text)


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Build doragum-themed HTML from updates/ markdown.")
    ap.add_argument("targets", nargs="*", help="Only build these (source .md name or output slug).")
    ap.add_argument("--check", action="store_true", help="Fail if any output is stale (no writes).")
    ap.add_argument("--list-outputs", action="store_true", help="Print each output path and exit.")
    args = ap.parse_args(argv)

    pages = load_manifest()
    if args.list_outputs:
        for page in pages:
            print(output_path(page).relative_to(REPO_ROOT))
        return 0

    if args.targets:
        wanted = set(args.targets)
        pages = [
            p for p in pages
            if p["source"] in wanted
            or output_path(p).name in wanted
            or Path(p["source"]).stem in wanted
        ]
        if not pages:
            print(f"no manifest pages matched: {', '.join(args.targets)}", file=sys.stderr)
            return 2

    stale = False
    for page in pages:
        out, rendered = build_page(page)
        if args.check:
            current = out.read_text(encoding="utf-8") if out.exists() else ""
            if current != rendered:
                stale = True
                print(f"STALE: {out.relative_to(REPO_ROOT)}")
                diff = difflib.unified_diff(
                    current.splitlines(), rendered.splitlines(),
                    fromfile=f"{out.name} (on disk)", tofile=f"{out.name} (rebuilt)", lineterm="",
                )
                print("\n".join(list(diff)[:40]))
            else:
                print(f"ok:    {out.relative_to(REPO_ROOT)}")
        else:
            out.write_text(rendered, encoding="utf-8")
            print(f"wrote: {out.relative_to(REPO_ROOT)}")

    return 1 if (args.check and stale) else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
