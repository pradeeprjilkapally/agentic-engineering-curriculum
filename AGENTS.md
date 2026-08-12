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
6. `## Your exercise`. Closes with these lines, in this order:
   - `**You're done when** …` (bold, required)
   - `**Practice proof:** …` (what to record in `NOTES.md`, where the lesson has one)
   - `**Build on it:** …` (one sentence, under ~30 words: a concrete thing the learner
     could build that exercises this lesson. Required — see issue #43.)
7. `## Why this matters`. One short paragraph
8. footer: `Previous: [link] · Next: [link]`

Item 2 is aspirational: most lessons don't currently carry the `> **Part X**` line. Don't
add it to one lesson in isolation — it's a repo-wide fix or nothing.

## Imagery

Diagrams are hand-authored SVGs in `assets/diagrams/`, matching the palette and type of
`agent-loop.svg` and `ai-map-layers.svg`. Keep all text inside the `viewBox` (rotated
labels running off-canvas has been a bug twice) and put arrowheads on arrows. Photos go in
`assets/photos/` with an entry in `CREDITS.md` naming the license.

**Never fabricate a terminal screenshot.** Anything depicting a real session must be a
verbatim transcription of a real run, recorded in `assets/screenshots/PROVENANCE.md` with
the commands needed to reproduce it. Typesetting real output as SVG is fine; inventing the
output is not. A course that teaches "ship it with proof" cannot illustrate itself with
fake proof.

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

Before opening a PR for curriculum or navigation changes, run both:

```bash
python3 scripts/check_links.py         # links that exist resolve
python3 scripts/check_lesson_shape.py  # required sections aren't missing
python3 scripts/check_pages_build.py   # links still resolve after Jekyll builds
```

`check_links.py` validates local Markdown and HTML links, including GitHub Pages
`.html` targets and heading anchors. It can only see links that are *there*.

`check_lesson_shape.py` checks for **absence** — the blind spot that let Part 7 ship
live but unreachable from the sidebar, and let six lessons ship without the
`**Build on it:**` line. It asserts every numbered lesson has each required section,
that `Build on it` closes the exercise (after `Practice proof`, before
`## Why this matters`), and that every lesson on disk is linked from the sidebar in
`_layouts/docs.html`.

A green `check_links.py` does not mean the lesson is well-formed. Run all three.

`check_pages_build.py` checks the question the other two do not ask: will the link
still work *after Jekyll builds the site*. Jekyll only renders a file to `.html` if
it carries YAML front matter — "a static file is a file that does not contain any
front matter", and static files are copied verbatim. A `.md` page with no front
matter is never emitted as `.html`, so `check_links.py` goes green while every
published link 404s. That is not hypothetical: 49 targets across 287 links shipped
dead this way.

**Every `.md` that is linked as `.html` needs front matter.** A `title:` is enough —
`_config.yml` supplies `layout: docs` to anything that is a page. A directory-style
link needs an index: either an `index.html`/`index.md`, or a `README.md` with an
explicit `permalink:` ending in `/`.
