#!/usr/bin/env python3
"""Build nss: join src/*.css into dist/nss.css and minify it into dist/nss.min.css.

    python build.py          build
    python build.py --check  build, then verify the rules nss promises (fails CI if broken)
"""

from __future__ import annotations

import gzip
import re
import sys
from pathlib import Path

VERSION = "3.0.0"
ROOT = Path(__file__).parent
SRC, DIST, THEMES = ROOT / "src", ROOT / "dist", ROOT / "themes"
BANNER = f"/*! nss {VERSION} · classless CSS · no JavaScript · MIT · https://gitlab.com/niharokz/nss */\n"
SIZE_BUDGET = 8 * 1024  # gzipped bytes of nss.min.css: what a visitor actually downloads


def minify(css: str) -> str:
    """A small, safe minifier. Selectors and declarations are handled separately, so
    spaces that matter (descendant selectors, calc() operators, media queries) survive."""
    strings: list[str] = []

    def stash(m: re.Match) -> str:
        strings.append(m.group(0))
        return f"\x00{len(strings) - 1}\x00"

    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    css = re.sub(r'"(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\'', stash, css)
    css = re.sub(r"\s+", " ", css)

    def chunk(m: re.Match) -> str:
        text, brace = m.group(1).strip(), m.group(2)
        if brace == "{":  # a selector list or an at-rule prelude
            if text.startswith("@"):
                text = re.sub(r"\s*([:,])\s*", r"\1", text)
            else:
                text = re.sub(r"\s*([>~+,])\s*", r"\1", text)
        else:  # declarations
            decls = []
            for d in text.split(";"):
                prop, colon, value = d.partition(":")
                if colon:
                    value = re.sub(r"\s*,\s*", ",", value.strip())
                    decls.append(prop.strip() + ":" + value)
                elif d.strip():
                    decls.append(d.strip())
            text = ";".join(decls)
        return text + brace

    body = re.sub(r"([^{}]*)([{}])", chunk, css)
    body = re.sub(r"\x00(\d+)\x00", lambda m: strings[int(m.group(1))], body)
    return BANNER.strip() + "\n" + body.strip() + "\n"


def build() -> tuple[str, str]:
    files = sorted(SRC.glob("*.css"))
    css = BANNER + "\n".join(f.read_text(encoding="utf-8").rstrip() + "\n" for f in files)
    DIST.mkdir(exist_ok=True)
    (DIST / "nss.css").write_text(css, encoding="utf-8")
    mini = minify(css)
    (DIST / "nss.min.css").write_text(mini, encoding="utf-8")
    for theme in sorted(THEMES.glob("*.css")):
        (DIST / f"nss-{theme.stem}.min.css").write_text(minify(theme.read_text(encoding="utf-8")), encoding="utf-8")
    # nss 1.x/2.x were linked from the repo root; keep those URLs working.
    (ROOT / "nss.css").write_text(css, encoding="utf-8")
    (ROOT / "nss.min.css").write_text(mini, encoding="utf-8")
    return css, mini


def selectors(css: str) -> list[str]:
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    css = re.sub(r'"(?:\\.|[^"\\])*"', '""', css)
    found = []
    for match in re.finditer(r"([^{}]+)\{", css):
        sel = match.group(1).strip()
        if sel.startswith("@") or re.fullmatch(r"(from|to|\d+%)(\s*,\s*(from|to|\d+%))*", sel):
            continue
        found.append(sel)
    return found


def check(css: str, mini: str) -> list[str]:
    problems = []
    if css.count("{") != css.count("}"):
        problems.append("unbalanced braces in dist/nss.css")
    if mini.count("{") != mini.count("}"):
        problems.append("unbalanced braces in dist/nss.min.css")
    for sel in selectors(css):
        cleaned = re.sub(r"\[[^\]]*\]", "", sel)            # attribute selectors checked below
        cleaned = re.sub(r"\(\s*[\d.]+\s*\)", "", cleaned)
        if re.search(r"(^|[\s>+~(,])\.[A-Za-z_-]", cleaned):
            problems.append(f"class selector (nss is classless): {sel[:80]}")
        for attr in re.findall(r"\[([\w-]+)", sel):
            if attr == "class" or attr.startswith("data-"):
                problems.append(f"styling hook attribute [{attr}] (nss is classless): {sel[:80]}")
    if re.search(r"\bjavascript:|<script", css, re.I):
        problems.append("JavaScript found in CSS")
    zipped = len(gzip.compress(mini.encode(), 9))
    if zipped > SIZE_BUDGET:
        problems.append(f"nss.min.css is {zipped} bytes gzipped, over the {SIZE_BUDGET} byte budget")
    return problems


if __name__ == "__main__":
    css, mini = build()
    print(f"dist/nss.css      {len(css.encode()):>6} bytes")
    print(f"dist/nss.min.css  {len(mini.encode()):>6} bytes ({len(gzip.compress(mini.encode(), 9))} gzipped)")
    if "--check" in sys.argv:
        problems = check(css, mini)
        for p in problems:
            print("✗", p)
        if problems:
            sys.exit(1)
        print("✓ classless, balanced, within size budget")
