#!/usr/bin/env python3
"""Check local Markdown and HTML links for GitHub Pages output."""

from __future__ import annotations

import argparse
import re
import sys
import urllib.parse
from pathlib import Path


MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
HTML_HREF = re.compile(r"""href=["']([^"']+)["']""")
HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$", re.MULTILINE)

IGNORED_PARTS = {".git", ".jekyll-cache", "_site", "node_modules"}
LOCAL_SUFFIXES = {".md", ".html"}


def slugify_heading(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"[`*_\[\]()]", "", text)
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def should_skip(path: Path) -> bool:
    return any(part in IGNORED_PARTS for part in path.parts)


def iter_content_files(root: Path) -> list[Path]:
    return sorted(
        path
        for path in root.rglob("*")
        if path.suffix in LOCAL_SUFFIXES and not should_skip(path)
    )


def extract_links(text: str) -> list[tuple[int, str]]:
    links: list[tuple[int, str]] = []
    links.extend((match.start(), match.group(1).strip()) for match in MARKDOWN_LINK.finditer(text))
    links.extend((match.start(), match.group(1).strip()) for match in HTML_HREF.finditer(text))
    return links


def extract_anchors(path: Path) -> set[str]:
    text = path.read_text(errors="ignore")
    return {slugify_heading(match.group(2)) for match in HEADING.finditer(text)}


def candidate_targets(source: Path, raw_target: str) -> list[Path]:
    target = (source.parent / raw_target).resolve() if raw_target else source.resolve()
    candidates = [target]

    if target.suffix == ".html":
        candidates.append(target.with_suffix(".md"))
    elif target.suffix == ".md":
        candidates.append(target.with_suffix(".html"))

    if target.is_dir():
        candidates.extend([target / "index.html", target / "README.md"])

    return candidates


def is_ignored_url(url: str) -> bool:
    return (
        not url
        or url.startswith(("http://", "https://", "mailto:", "tel:", "{{"))
        or "{%" in url
        or "{{" in url
    )


def check_links(root: Path) -> list[str]:
    files = iter_content_files(root)
    anchors = {path.resolve(): extract_anchors(path) for path in files}
    problems: list[str] = []

    for source in files:
        text = source.read_text(errors="ignore")
        for position, url in extract_links(text):
            if is_ignored_url(url):
                continue

            raw_target, _, fragment = url.partition("#")
            raw_target = raw_target.split("?", 1)[0]
            if raw_target.startswith("/"):
                continue

            existing = next((path for path in candidate_targets(source, raw_target) if path.exists()), None)
            line = text.count("\n", 0, position) + 1

            if existing is None:
                problems.append(f"{source.relative_to(root)}:{line} {url} -> missing file")
                continue

            if not fragment:
                continue

            fragment = urllib.parse.unquote(fragment)
            existing_anchors = anchors.get(existing.resolve(), set())
            if existing.suffix in LOCAL_SUFFIXES and existing_anchors and fragment not in existing_anchors:
                problems.append(f"{source.relative_to(root)}:{line} {url} -> missing anchor")

    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description="Check local Markdown and HTML links.")
    parser.add_argument("--root", default=".", help="Repository root to scan.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    problems = check_links(root)

    print(f"checked {len(iter_content_files(root))} Markdown/HTML files")
    if problems:
        print(f"missing links or anchors: {len(problems)}")
        for problem in problems:
            print(problem)
        return 1

    print("missing links or anchors: 0")
    return 0


if __name__ == "__main__":
    sys.exit(main())
