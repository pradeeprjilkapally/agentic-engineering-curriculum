#!/usr/bin/env python3
"""Assert every internal link will still resolve once Jekyll has built the site.

`check_links.py` checks that a link's *source* exists: `course/x.html` is fine as
long as `course/x.md` is on disk. That is not the same question GitHub Pages asks.

Jekyll only renders a file into `.html` if it carries YAML front matter. From the
Jekyll docs: "A static file is a file that does not contain any front matter."
Static files are copied verbatim — `x.md` stays `x.md`, and `x.html` is never
produced. So a repo can pass `check_links.py` cleanly and still 404 on every page.

That is exactly what happened here: 49 targets, 287 links, every lesson dead.

This checks the build-time question:

    python3 scripts/check_pages_build.py

Every internal `.html` link must resolve to a real `.html` file, or to a `.md`
source that carries front matter. Every directory-style link must resolve to an
index. Exit 0 when the built site would serve every link, 1 otherwise.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

LINK = re.compile(r'(?:\]\(|href=["\'])([^)"\'#\s]+)(?:#[^)"\']*)?')
EXTERNAL = ("http://", "https://", "mailto:", "//", "javascript:", "{{", "#")
IGNORED_PARTS = {".git", ".jekyll-cache", "_site", "node_modules", ".claude"}
SCANNED_SUFFIXES = {".md", ".html"}


def has_front_matter(path: Path) -> bool:
    """Jekyll renders a file only when it opens with a YAML front matter block."""
    try:
        with path.open("r", encoding="utf-8") as handle:
            return handle.readline().rstrip("\n") == "---"
    except OSError:
        return False


def front_matter(path: Path) -> str:
    """The raw front matter block, or '' when the file has none."""
    if not has_front_matter(path):
        return ""
    text = path.read_text(encoding="utf-8")
    end = text.find("\n---", 4)
    return text[4:end] if end != -1 else ""


def scanned_files() -> list[Path]:
    return sorted(
        p for p in ROOT.rglob("*")
        if p.suffix in SCANNED_SUFFIXES
        and not any(part in IGNORED_PARTS for part in p.relative_to(ROOT).parts)
    )


def directory_index_ok(target: Path) -> bool:
    """A directory URL needs an index page Jekyll will actually emit."""
    for name in ("index.html", "index.md"):
        candidate = target / name
        if candidate.exists() and (name.endswith(".html") or has_front_matter(candidate)):
            return True
    readme = target / "README.md"
    if readme.exists() and "permalink:" in front_matter(readme):
        return True
    return False


def check() -> list[str]:
    problems: list[str] = []
    for source in scanned_files():
        try:
            text = source.read_text(encoding="utf-8")
        except OSError:
            continue
        rel_source = source.relative_to(ROOT)

        for match in LINK.finditer(text):
            raw = match.group(1)
            if raw.startswith(EXTERNAL):
                continue

            target = (source.parent / raw).resolve()
            try:
                rel_target = target.relative_to(ROOT)
            except ValueError:
                continue  # points outside the repo; not ours to serve

            if raw.endswith(".html"):
                if target.exists():
                    continue  # a real .html file is copied as-is
                md = ROOT / rel_target.with_suffix(".md")
                if not md.exists():
                    problems.append(f"{rel_source}: -> {rel_target} (no source file)")
                elif not has_front_matter(md):
                    problems.append(
                        f"{rel_source}: -> {rel_target} "
                        f"({rel_target.with_suffix('.md')} has no front matter, "
                        f"so Jekyll never emits it)"
                    )
            elif raw.endswith("/") or target.is_dir():
                if target.is_dir() and not directory_index_ok(target):
                    problems.append(f"{rel_source}: -> {rel_target}/ (no index page)")
    return problems


def main() -> int:
    files = scanned_files()
    problems = sorted(set(check()))

    print(f"checked {len(files)} Markdown/HTML files")
    if problems:
        print(f"links that would 404 on the built site: {len(problems)}")
        for problem in problems:
            print(f"  {problem}")
        return 1
    print("links that would 404 on the built site: 0")
    return 0


if __name__ == "__main__":
    sys.exit(main())
