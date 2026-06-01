# Lesson 4.3 · Context and the second brain

**Where this gets you:** your project will have a `CLAUDE.md` the agent reads automatically every session. So you stop re-explaining the same things and the agent starts each task already knowing your stack.

## The idea

Every session, you re-explain the same things: stack, commands, repo rules, helpers, deploy path. That is leverage leaking.

The fix is stable context in a file the agent loads on its own. In Claude Code, that file is `CLAUDE.md` at the project root. Codex and Gemini have their own conventions; the habit is the same.

Three commands matter:

- **`/init`**. Point it at your project and it reads the code and generates a starting `CLAUDE.md`. A solid first draft, not a finished one.
- **`/memory`**. View and edit your `CLAUDE.md` from inside a session, the moment you spot something missing.
- **Auto-memory**. Durable facts the agent records as you work, so a decision made today is still known next week.

This is your second brain: slow-changing truth underneath fast-changing briefs.

## Do it

Start with the instruction file for your tool:

| Tool | File or place to start |
|---|---|
| Claude Code | `CLAUDE.md` |
| Codex CLI | `AGENTS.md` |
| Gemini CLI | repo instructions or `GEMINI.md` if your team uses one |
| Coco | approved project/team guidance in the governed workspace |

If your team uses several tools, keep `AGENTS.md` as the tool-neutral source and symlink or copy from it when needed.

This repo ships a starter. [`second-brain-starter/`](./second-brain-starter/). It has three tiers:

- **`CLAUDE.md`**. The always-loaded skeleton: what the project is, stack, code layout, conventions, non-negotiable standards, how to work with you.
- **`playbooks/`**. Step-by-step procedures for repeated work (deploys, releases), pulled in when a task matches.
- **`memory/`**. Durable facts, one per file: decisions, and *scars*. The expensive things that broke and the lesson.

Run `/init` or fork `second-brain-starter/`. Fill in real facts. Delete every bracket.

## Your exercise

Get a real `CLAUDE.md` onto your project. Run `/init` or fork the starter, then fill it in with real specifics about your project. Delete every bracket.

Then, for one full work session, run this rule: every time you explain something to the agent that you've explained before, stop. Don't explain it. Put it in the second brain instead. `CLAUDE.md`, a playbook, or a memory file. And move on.

**You're done when** your project has a filled-in instruction file with no brackets left, and your one session produced at least three things written into the second brain instead of re-explained.

**Practice proof:** start a fresh session and ask the agent to summarize the repo rules. Fix the instruction file if it misses anything important.

## Why this matters

The model is the same for everyone. Your second brain is not. Month one you're documenting; month three every task starts with the agent already knowing your stack, your standards, and your scars. That compounding is the real 10x. And it's the part you own.

---

Previous: [Lesson 4.2 · Evals. Defining done](10-evals-defining-done.html) · Next: [Lesson 4.4 · The no-slop standard](12-the-no-slop-standard.html)
