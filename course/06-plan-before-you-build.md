# Lesson 3.2 · Plan before you build

**Where this gets you:** a written, approved plan for the first slice of your project. One you've read hard and pushed back on, before a single file gets edited.

## The idea

The fastest way to waste an hour with an agent is to let it build before you've seen the plan. When the approach is wrong, you're untangling instead of reviewing.

**Plan Mode** fixes that. The agent reads your files and runs read-only commands, then hands you a written plan. It changes nothing until you approve. No edits, no surprises. You get to argue with the approach while it's still just words.

**What that looks like.** You ask for CSV import. The plan comes back: add `pandas`, write a new `importers/` package, refactor the existing file reader to use it. All reasonable-sounding. But you know the app already parses CSVs in `io/reader.py` with the standard library, and you know `pandas` is 60MB you don't want in the container. Two sentences of pushback — *no new dependency, extend `io/reader.py`* — and the plan comes back correct. Approve the first version instead, and you're reverting a refactor and a dependency two days later, after they've grown callers.

In Claude Code, cycle to it with **Shift+Tab**. Tap it until the prompt shows you're in plan mode.

For other tools:

| Tool | Planning move |
|---|---|
| Claude Code | Use Plan Mode before edits. |
| Codex CLI | Ask for a plan first and do not approve edits until you agree with it. |
| Gemini CLI | Ask it to inspect and propose a plan before changing files. |
| Coco | Require a written plan that names data, permissions, and governed actions before execution. |

The workflow is short:

1. **Enter plan mode** and describe the goal. The first slice of your project, not the whole thing.
2. **Read the plan critically.** Right files? Right approach? Did it miss a step, or invent one you don't need?
3. **Push back.** Tell it what's wrong. It revises.
4. **Approve** only when you actually believe the plan.
5. It builds.

A wrong plan is cheap. Wrong code is not.

## Do it

Open your project and enter plan mode (Shift+Tab). Describe the first slice — the smallest meaningful piece of your definition of done. Not "build the whole app." Something like "add the command that parses the input file."

Read what comes back the way you'd read a coworker's design doc. Look for the wrong file, the missing step, the heavier-than-needed approach. Find at least one thing and send a correction. Let it revise. Repeat until the plan is one you'd defend.

## Your exercise

Get a plan, in plan mode, for the first slice of your project. Read it hard. Send at least one correction. Even if the plan looks decent, find the thing that could be tighter.

**You're done when** you have an approved plan you actually believe in. Not one you rubber-stamped to move on.

**Practice proof:** commit or save the approved plan in `NOTES.md`. Include the correction you made to the agent's first plan.

**Build on it:** build a `plan-diff` CLI that saves each plan mode plan to a timestamped file in `plans/` and prints a diff against the previous one, so you can see exactly what your pushback changed.

## Why this matters

Planning first is the habit that separates directing an agent from gambling with one. It moves your judgment to the front, where corrections are cheap. Every later lesson — building, evals, shipping — gets easier when the work started from a plan you understood. Skip it and you'll spend the course cleaning up after confident wrong turns.

---

Previous: [Lesson 3.1 · Pick your first project](05-pick-your-first-project.html) · Next: [Lesson 3.3 · Build it, step by step](07-build-it-step-by-step.html)
