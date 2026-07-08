# Lesson 4.5 · Design discipline

**Where this gets you:** your project will have a `DESIGN.md` the agent reads on every task with a surface. So screens, APIs, and docs come out consistent instead of being a fresh roll of the dice each time.

## The idea

If your project has a surface — UI, API, CLI, docs — it has a design. If the standard lives only in your head, the agent guesses. Ten guesses later you have ten dialects of the same product.

Here's what that looks like. You ask for a settings page on Monday and get `#3b82f6` buttons with 18px padding. On Thursday you ask for a billing page in a fresh session and get `#2563eb` buttons with 20px padding. Both are fine alone. Side by side they're two products. Every future screen then inherits whichever the agent read first, and the cleanup is a week of find-and-replace across files nobody wrote by hand.

Fix it the way you fixed slop: move the standard into an artifact the agent reads. For design, that artifact is **`DESIGN.md`**.

`DESIGN.md` pins down what the agent would otherwise invent. Color tokens (named, not loose hex), the type scale, the spacing scale, layout rules, component rules, and **voice** — how the product talks in copy, errors, and empty states. The rule it enforces: if a color or size is needed and no token fits, that's a flag to discuss. Not a license to invent.

This repo ships a template, [`templates/DESIGN.md`](../templates/DESIGN.html). It covers what the product is and the one feeling it should produce, voice, color tokens, type, layout and spacing, components, motion, an accessibility floor, and an anti-patterns list. The slop list, design edition: generic AI gradients, off-scale spacing, invented colors, emoji standing in for real copy.

## Do it

1. Fork `templates/DESIGN.md` to your project root.
2. Fill every section with real specifics. Real hex values in the token table, your actual spacing scale, your actual voice. Delete every bracket and the top blockquote.
3. Reference it from `CLAUDE.md` so the agent reads it on every task that touches a surface. The starter `CLAUDE.md` already has the line and a `DESIGN.md` pointer.

Be concrete. "Calm, fast, trustworthy" beats "modern and clean."

## Your exercise

Fill in `DESIGN.md` for your project and wire it into `CLAUDE.md`.

Then run the comparison. Pick one component — a card, a form, an error state. Generate it once with `DESIGN.md` in context. Generate it again in a session where the agent can't see it. Put them side by side.

**You're done when** your project has a filled-in `DESIGN.md` referenced from `CLAUDE.md`, and you've generated the same component with and without it and can name what the spec changed.

**Build on it:** Build a small CLI that reads your `DESIGN.md` token table and flags any hex value in your codebase that isn't a named token.

## Why this matters

The difference between "looks generated" and "looks intentional" is almost never talent. It's whether the standard was written down. `DESIGN.md` is how a project built largely by agents still looks like one product, made on purpose. Without it, speed just gets you to inconsistent faster.

---

Previous: [Lesson 4.4 · The no-slop standard](12-the-no-slop-standard.html) · Next: [Lesson 5.1 · Orchestration. Parallel agents](14-orchestration-parallel-agents.html)
