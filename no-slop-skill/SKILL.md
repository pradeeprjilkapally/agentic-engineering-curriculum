---
name: no-slop
description: Review pass that catches slop before it ships — dead code, unhandled errors, duplication, vague names, untested edges, comments that restate code. Run against your own output before handing work back. Use after generating or editing any non-trivial code.
---

# No-Slop Review

Slop is a list. This skill runs that list as a review pass.

Run it against code you just wrote or edited **before** you call the work done.

## How to run it

1. Identify every file you created or changed in this task.
2. For each one, walk the [checklist](no-slop-checklist.html) top to bottom.
3. For every hit: fix it, or write one line on why it's a deliberate exception.
4. Only then is the work eligible for the review gate.

Do not report the work as done while any checklist item is an unexplained hit.

## The checklist (summary)

Full version with examples: [`no-slop-checklist.md`](no-slop-checklist.html).

- **Dead code** — unused vars, imports, functions, branches. Delete it.
- **Unhandled errors** — every fallible call has a real failure path, not a swallowed exception.
- **Duplication** — copy-pasted blocks. Three strikes → extract.
- **Vague names** — `data`, `handle`, `temp`, `doStuff`. Name the thing.
- **Untested edges** — empty, null, max, concurrent, the unhappy path.
- **Restating comments** — `// increment i`. Delete. Keep only comments that explain *why*.
- **Inconsistent with the file** — match the surrounding code's idioms, not your defaults.
- **Scope creep** — anything not in the brief. Flag it; don't smuggle it.
- **Fake done** — `TODO`, stubbed returns, hardcoded values pretending to be real.
- **Unverified claims** — "this works" / "deployed" with no proof in the same turn.

## Why this exists

Agentic engineering is a multiplier. Without a no-slop pass, it multiplies inattention. Run it every time.

## Customizing

The checklist is a baseline. Add the slop patterns specific to your stack and the ones you personally keep shipping.
