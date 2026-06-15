# Agentic Engineering Curriculum. Agent instructions

Instructions for any coding agent (Claude Code, Codex, Gemini CLI) working in this
repo. `CLAUDE.md` is a symlink to this file. One source of truth, both tools.

## What this is

A hands-on, beginner-first course on agentic engineering, plus a static landing
site and three forkable artifacts. Published via GitHub Pages at
aisoftllc.github.io/agentic-engineering-curriculum.

## Layout

- `course/`. The 32 lessons, `NN-slug.md`, across 6 parts, plus guides for labs, CLI variants, teaching, pathways, and the two-week ramp.
- `curriculum.md`. The course index / table of contents.
- `index.html` + `assets/style.css`. The landing site (GitHub Pages serves this).
- `no-slop-skill/`, `templates/DESIGN.md`, `second-brain-starter/`. The forkable
  artifacts the course installs. Lessons 4.3, 4.4, and 4.5 depend on them; don't break them.
- `README.md`. Repo overview.

## Lesson format

Every lesson follows the same shape. Match it exactly when editing or adding one:

1. `# Lesson N · Title`
2. `> **Part X · Part name**. Lesson N of 32`
3. `**Where this gets you:** <one sentence>`
4. `## The idea`. Plain explanation
5. `## Do it`. Concrete steps (only when there are real commands)
6. `## Your exercise`. Ends with a bold `**You're done when** …` line
7. `## Why this matters`. One short paragraph
8. footer: `Previous: [link] · Next: [link]`

The course threads ONE learner project (picked in Lesson 5) through every later
exercise. Keep that thread intact.

## Voice

Conversational, plain, second person, contractions. Warm but no hype, no aphorisms,
short paragraphs. It should read like a person mentoring you. Not a manifesto and
not API documentation.

## Git

Feature branch + PR. Don't push to `main` directly. Merging to `main` republishes
the GitHub Pages site.

## Verification

Before opening a PR for curriculum or navigation changes, run:

```bash
python3 scripts/check_links.py
```

The checker validates local Markdown and HTML links, including GitHub Pages `.html`
targets and heading anchors.
