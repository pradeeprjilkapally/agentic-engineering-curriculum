#!/usr/bin/env python3
"""Assert every lesson matches the shape declared in AGENTS.md.

check_links.py validates links that exist. It cannot see a link — or a section —
that is *absent*. That blind spot let Part 7 ship orphaned from the sidebar, and
let six lessons ship without the `**Build on it:**` line issue #43 requires.

This checks for absence. Run it before opening a PR:

    python3 scripts/check_lesson_shape.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COURSE = ROOT / "course"
SIDEBAR = ROOT / "_layouts" / "docs.html"

# (label, predicate) — every numbered lesson must satisfy all of these.
REQUIRED = [
    ("title `# Lesson N · …`", lambda s: re.search(r"^# Lesson [\w.]+ · ", s, re.M)),
    ("`**Where this gets you:**`", lambda s: re.search(r"^\*\*Where this gets you:\*\*", s, re.M)),
    ("`## The idea`", lambda s: re.search(r"^## The idea\b", s, re.M)),
    ("`## Your exercise`", lambda s: re.search(r"^## Your exercise\b", s, re.M)),
    ("`**You're done when**`", lambda s: re.search(r"^\*\*You['’]re done when\*\*", s, re.M)),
    ("`**Build on it:**` (issue #43)", lambda s: re.search(r"^\*\*Build on it:\*\*", s, re.M)),
    ("`## Why this matters`", lambda s: re.search(r"^## Why this matters\b", s, re.M)),
    ("footer nav", lambda s: re.search(r"^(Previous|Next):", s, re.M)),
]


def lesson_files() -> list[Path]:
    return sorted(p for p in COURSE.glob("*.md") if p.stem[0].isdigit())


def check_shape() -> list[str]:
    problems = []
    for path in lesson_files():
        text = path.read_text(encoding="utf-8")
        for label, ok in REQUIRED:
            if not ok(text):
                problems.append(f"{path.relative_to(ROOT)}: missing {label}")
    return problems


def check_exercise_order() -> list[str]:
    """`Build on it` closes the exercise: it must follow `Practice proof`
    (when present) and precede `## Why this matters`."""
    problems = []
    for path in lesson_files():
        lines = path.read_text(encoding="utf-8").splitlines()
        idx = {}
        for i, line in enumerate(lines):
            for key, prefix in (
                ("done", "**You're done when**"),
                ("proof", "**Practice proof:**"),
                ("build", "**Build on it:**"),
                ("why", "## Why this matters"),
            ):
                if line.startswith(prefix) and key not in idx:
                    idx[key] = i
        rel = path.relative_to(ROOT)
        if "build" not in idx:
            continue  # already reported by check_shape
        if "done" in idx and idx["build"] < idx["done"]:
            problems.append(f"{rel}: `Build on it` precedes `You're done when`")
        if "proof" in idx and idx["build"] < idx["proof"]:
            problems.append(f"{rel}: `Build on it` precedes `Practice proof`")
        if "why" in idx and idx["build"] > idx["why"]:
            problems.append(f"{rel}: `Build on it` falls outside `## Your exercise`")
    return problems


def check_sidebar_covers_lessons() -> list[str]:
    """Every lesson on disk must be reachable from the sidebar rendered on every
    lesson page. Part 7 shipped live and unreachable because nothing checked this."""
    if not SIDEBAR.exists():
        return [f"{SIDEBAR.relative_to(ROOT)}: not found"]
    sidebar = SIDEBAR.read_text(encoding="utf-8")
    missing = [
        f"_layouts/docs.html: no sidebar link to course/{p.stem}.html"
        for p in lesson_files()
        if f"/course/{p.stem}.html" not in sidebar
    ]
    return missing


def main() -> int:
    lessons = lesson_files()
    problems = check_shape() + check_exercise_order() + check_sidebar_covers_lessons()

    print(f"checked {len(lessons)} numbered lessons")
    if problems:
        print(f"shape problems: {len(problems)}")
        for p in problems:
            print(f"  {p}")
        return 1
    print("shape problems: 0")
    return 0


if __name__ == "__main__":
    sys.exit(main())
