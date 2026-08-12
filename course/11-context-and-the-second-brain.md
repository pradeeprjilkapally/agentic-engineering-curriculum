---
title: "Lesson 4.3 · Context and the second brain"
---

# Lesson 4.3 · Context and the second brain

**Where this gets you:** your project will have a `CLAUDE.md` the agent reads automatically every session. So you stop re-explaining the same things and the agent starts each task already knowing your stack.

## The idea

Every session you re-explain the same things. Your stack. Your commands. Your repo rules. Your deploy path. That's leverage leaking.

The fix is a **second brain**: stable context in a file the agent loads on its own. In Claude Code that file is `CLAUDE.md` at the project root. Codex and Gemini have their own conventions. The habit is the same.

**Here's what it saves you.** A team's migrations have to run before the deploy, or the app boots against a schema that isn't there. Everyone knows. Nobody wrote it down. So every session the agent proposes deploy-then-migrate, and every session someone catches it in review — until the Friday nobody does, and the site is down for eleven minutes. One line in `CLAUDE.md` — *migrations run before deploy, always* — and the agent never suggests it again. Not on any branch, not for the new hire either.

Three commands matter:

- **`/init`**. Point it at your project and it reads the code and generates a starting `CLAUDE.md`. A solid first draft, not a finished one.
- **`/memory`**. View and edit your `CLAUDE.md` from inside a session, the moment you spot something missing.
- **Auto-memory**. Durable facts the agent records as you work, so a decision made today is still known next week.

Slow-changing truth, underneath fast-changing briefs.

## Do it

Start with the instruction file for your tool:

| Tool | File or place to start |
|---|---|
| Claude Code | `CLAUDE.md` |
| Codex CLI | `AGENTS.md` |
| Gemini CLI | repo instructions or `GEMINI.md` if your team uses one |
| Coco | approved project/team guidance in the governed workspace |

Using several tools? Keep `AGENTS.md` as the tool-neutral source and symlink or copy from it.

This repo ships a starter: [`second-brain-starter/`](../second-brain-starter/). Three tiers:

- **`CLAUDE.md`**. The always-loaded skeleton: what the project is, stack, code layout, conventions, non-negotiable standards, how to work with you.
- **`playbooks/`**. Step-by-step procedures for repeated work — deploys, releases — pulled in when a task matches.
- **`memory/`**. Durable facts, one per file: decisions, and *scars*. The expensive things that broke, and the lesson.

Run `/init` or fork `second-brain-starter/`. Fill in real facts. Delete every bracket.

## Your exercise

Get a real `CLAUDE.md` onto your project. Run `/init` or fork the starter, fill it in, delete every bracket.

Then run this rule for one full work session: every time you catch yourself explaining something to the agent you've explained before, stop. Write it into the second brain instead — `CLAUDE.md`, a playbook, or a memory file — and move on.

**You're done when** your project has a filled-in instruction file with no brackets left, and that one session produced at least three things written into the second brain instead of re-explained.

**Practice proof:** start a fresh session and ask the agent to summarize the repo rules. Fix the instruction file if it misses anything important.

**Build on it:** add a `memory/scars.md` and, every time something breaks, append two lines — what broke, what you'll do differently — so next month's agent inherits this month's expensive lessons.

## Why this matters

The model is the same for everyone. Your second brain is not. Month one you're documenting. Month three every task starts with the agent already knowing your stack, your standards, and your scars. That compounding is the real 10x — and it's the part you own.

---

Previous: [Lesson 4.2 · Evals. Defining done](10-evals-defining-done.html) · Next: [Lesson 4.4 · The no-slop standard](12-the-no-slop-standard.html)
