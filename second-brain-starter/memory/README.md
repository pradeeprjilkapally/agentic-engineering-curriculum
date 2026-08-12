---
title: "Memory"
permalink: /second-brain-starter/memory/
---

# Memory

Durable facts that accumulate over time — decisions, scars, what worked and what didn't. The layer that makes month-three you faster than month-one you.

## The model

**One fact per file.** A file is cheap. A file that tries to hold five facts gets stale in five ways.

Each file, short, with a little frontmatter so it's findable:

```markdown
---
name: short-kebab-slug
description: one-line summary — used to decide if this is relevant to recall
type: decision | scar | reference | convention
---

The fact. If it's a decision or a scar, follow with **Why** and **How to apply**.
Link related memories with [[their-slug]].
```

## Types

- **`decision`** — a choice made and the reasoning, so it isn't relitigated. ("We use X over Y because…")
- **`scar`** — something that broke, why, and the lesson. The expensive ones. ("Deploy looked done but wasn't because…")
- **`reference`** — a pointer to an external resource (dashboard, doc, ticket).
- **`convention`** — a settled pattern, if it's too specific for `CLAUDE.md`.

## The index

Keep a `MEMORY.md` index with one line per memory, for example `- title: memory-slug - hook`. That's what an agent scans to decide what to pull. The individual files are the content; the index is the table of contents.

## Hygiene

- Before adding a fact, check if a file already covers it — update, don't duplicate.
- A memory that turns out wrong gets deleted, not left to mislead.
- Don't store what the repo already records — code structure, git history, things in `CLAUDE.md`. Store what was *non-obvious*.
- Memories reflect what was true when written. If one names a file or flag, the agent verifies it still exists before acting on it.

## Start empty

This folder ships empty on purpose. It fills as real work happens. The first scar you write down is the moment the second brain starts paying you back.
