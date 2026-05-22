# Lesson 11 · Context and the second brain

> **Part 3 · The core concepts** — Lesson 11 of 16

**Where this gets you:** your project will have a `CLAUDE.md` the agent reads automatically every session — so you stop re-explaining the same things and the agent starts each task already knowing your stack.

## The idea

By now you've noticed it. Every session, you re-explain the same things: this is a Next.js app, we never push to main, tests live here, don't reinvent the date helper. The agent doesn't remember between sessions. So you type it again. That's leverage leaking — work you redo because the context didn't persist.

An agent is only as good as the context you can hand it. The fix isn't a longer prompt. It's writing the stable stuff down once, in a file the agent picks up on its own. That file is `CLAUDE.md`, and it lives at the root of your project. Claude Code loads it at the start of every session — no prompt needed. (Codex and Gemini have their own conventions; the idea is identical, only the filename changes.)

Three commands matter:

- **`/init`** — point it at your project and it reads the code and generates a starting `CLAUDE.md`. A solid first draft, not a finished one.
- **`/memory`** — view and edit your `CLAUDE.md` from inside a session, the moment you spot something missing.
- **Auto-memory** — durable facts the agent records as you work, so a decision made today is still known next week.

This is your second brain: the stable layer of context underneath every brief. The brief is fast-changing, per-task. The second brain is slow-changing truth about the project and how you work.

## Do it

This repo ships a starter — [`second-brain-starter/`](../second-brain-starter/). It has three tiers:

- **`CLAUDE.md`** — the always-loaded skeleton: what the project is, stack, code layout, conventions, non-negotiable standards, how to work with you.
- **`playbooks/`** — step-by-step procedures for repeated work (deploys, releases), pulled in when a task matches.
- **`memory/`** — durable facts, one per file: decisions, and *scars* — the expensive things that broke and the lesson.

Either run `/init` to generate a first draft, or fork `second-brain-starter/` and fill in the bracketed prompts. Don't write fiction — only put down what's actually true.

## Your exercise

Get a real `CLAUDE.md` onto your project. Run `/init` or fork the starter, then fill it in with real specifics about your project — delete every bracket.

Then, for one full work session, run this rule: every time you explain something to the agent that you've explained before, stop. Don't explain it. Put it in the second brain instead — `CLAUDE.md`, a playbook, or a memory file — and move on.

**You're done when** your project has a filled-in `CLAUDE.md` with no brackets left, and your one session produced at least three things written into the second brain instead of re-explained.

## Why this matters

The model is the same for everyone. Your second brain is not. Month one you're documenting; month three every task starts with the agent already knowing your stack, your standards, and your scars. That compounding is the real 10x — and it's the part you own.

---

Previous: [Lesson 10 · Evals — defining done](10-evals-defining-done.md) · Next: [Lesson 12 · The no-slop standard](12-the-no-slop-standard.md)
