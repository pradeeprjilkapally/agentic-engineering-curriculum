# Agentic Engineering Curriculum — agent instructions

Instructions for any coding agent (Claude Code, Codex, Gemini CLI) working in this
repo. `CLAUDE.md` is a symlink to this file — one source of truth, both tools.

## What this is

A hands-on, beginner-first course on agentic engineering, plus a static landing
site and three forkable artifacts. Published via GitHub Pages at
aisoftllc.github.io/agentic-engineering-curriculum.

## Layout

- `course/` — the 16 lessons, `NN-slug.md`, in order, across 4 parts.
- `curriculum.md` — the course index / table of contents.
- `index.html` + `assets/style.css` — the landing site (GitHub Pages serves this).
- `no-slop-skill/`, `templates/DESIGN.md`, `second-brain-starter/` — the forkable
  artifacts the course installs. Lessons 11–13 depend on them; don't break them.
- `README.md` — repo overview.

## Lesson format

Every lesson follows the same shape — match it exactly when editing or adding one:

1. `# Lesson N · Title`
2. `> **Part X · Part name** — Lesson N of 16`
3. `**Where this gets you:** <one sentence>`
4. `## The idea` — plain explanation
5. `## Do it` — concrete steps (only when there are real commands)
6. `## Your exercise` — ends with a bold `**You're done when** …` line
7. `## Why this matters` — one short paragraph
8. footer: `Previous: [link] · Next: [link]`

The course threads ONE learner project (picked in Lesson 5) through every later
exercise. Keep that thread intact.

## Voice

Conversational, plain, second person, contractions. Warm but no hype, no aphorisms,
short paragraphs. It should read like a person mentoring you — not a manifesto and
not API documentation.

## Git

Feature branch + PR. Don't push to `main` directly. Merging to `main` republishes
the GitHub Pages site.
