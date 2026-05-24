# Lesson 6 · Plan before you build

> **Part 2 · Build something real** — Lesson 6 of 16

**Where this gets you:** a written, approved plan for the first slice of your project — one you've read hard and pushed back on, before a single file gets edited.

## The idea

The fastest way to waste an hour with an agent is to let it start building before you've seen its plan. It picks an approach, commits to it, writes the code — and only then do you notice it went the wrong direction. Now you're untangling instead of reviewing.

Plan Mode fixes that. It's a mode where the agent reads your files and runs read-only commands, then hands you a written plan — and changes nothing until you approve it. No edits, no surprises. You get to argue with the approach while it's still just words.

In Claude Code, cycle to it with **Shift+Tab** — tap it until the prompt shows you're in plan mode.

For other tools:

| Tool | Planning move |
|---|---|
| Claude Code | Use Plan Mode before edits. |
| Codex CLI | Ask for a plan first and do not approve edits until you agree with it. |
| Gemini CLI | Ask it to inspect and propose a plan before changing files. |
| Coco | Require a written plan that names data, permissions, and governed actions before execution. |

The workflow is short:

1. **Enter plan mode** and describe the goal — the first slice of your project, not the whole thing.
2. **Read the plan critically.** Does it touch the right files? Is the approach the one you'd choose? Did it miss something, or invent a step you don't need?
3. **Push back.** Tell it what's wrong. "Don't add a new dependency for this." "Wrong file — that logic lives in X." It revises.
4. **Approve** only when you actually believe the plan.
5. It builds.

The point isn't speed. It's catching a bad approach before it costs you. A wrong plan is ten seconds to fix. Wrong code is an hour.

## Do it

Open your project and enter plan mode (Shift+Tab). Describe the first slice — the smallest meaningful piece of your definition of done. Not "build the whole app." Something like "add the command that parses the input file."

Read the plan it gives back the way you'd read a coworker's design doc. Look for the wrong file, the missing step, the heavier-than-needed approach. Find at least one thing and send a correction. Let it revise. Repeat until the plan is one you'd defend.

## Your exercise

Get a plan, in plan mode, for the first slice of your project. Read it hard. Send at least one correction — even if the plan looks decent, find the thing that could be tighter.

**You're done when** you have an approved plan you actually believe in — not one you rubber-stamped to move on.

**Practice proof:** commit or save the approved plan in `NOTES.md`. Include the correction you made to the agent's first plan.

## Why this matters

Planning first is the single habit that separates directing an agent from gambling with one. It moves your judgment to the front, where corrections are cheap. Every later lesson — building, evals, shipping — gets easier when the work started from a plan you understood. Skip it and you'll spend the course cleaning up after confident wrong turns.

---

Previous: [Lesson 5 · Pick your first project](05-pick-your-first-project.md) · Next: [Lesson 7 · Build it, step by step](07-build-it-step-by-step.md)
