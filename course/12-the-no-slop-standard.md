# Lesson 12 · The no-slop standard

**Where this gets you:** you'll install a review pass the agent runs against its own output — so quality is enforced by an artifact, not by you remembering to look hard.

## The idea

"Pay more attention" is not a system. Encode quality into something the agent reads and runs every time.

Slop is a list: dead code, swallowed errors, copy-paste, vague names, untested edges, comments that restate the line above. If you can check it, the agent can check it.

That's what the no-slop skill is. This repo ships it — [`no-slop-skill/`](../no-slop-skill/). It's a review pass: after the agent generates or edits non-trivial code, it walks a checklist against its own output **before** handing the work back to you. Every hit gets fixed, or gets one line explaining why it's a deliberate exception. The work isn't eligible for your review gate until the checklist is clean.

The checklist itself ([`no-slop-checklist.md`](../no-slop-skill/no-slop-checklist.html)) has ten sections: dead code, unhandled errors, duplication, naming, untested edges, comments, consistency with the codebase, scope, fake done (TODOs and stubbed returns), and verified-not-claimed. Each item is concrete enough to be unarguable.

This is attention as an artifact.

## Do it

1. Install the skill — copy `no-slop-skill/` into your project (Claude Code reads skills from `.claude/skills/`; check your tool's convention).
2. From `CLAUDE.md`, make it non-negotiable — the starter already has the line: *run the no-slop review pass before reporting any non-trivial change done.*
3. Run it on a recent change to your project — code you already shipped or just wrote. Have the agent walk the full checklist against it.

If your tool does not support skills, still use the checklist. Paste it into your review prompt or project instructions and require the agent to run through it before handing work back.

## Your exercise

Run the no-slop pass on your project's most recent real changes. Count what it catches — every hit. Be honest; some of those are yours.

Then customize the checklist. The shipped version is a baseline. Add the slop patterns specific to your stack, and the ones *you* personally keep shipping. A checklist you didn't tune is one you won't trust enough to run.

**You're done when** the no-slop skill or checklist is installed, referenced from your project instructions, has run against real changes with the catch count written down, and the checklist has at least two items you added.

**Practice proof:** run the review pass on one recent change and record one fix-or-justify note.

## Why this matters

Agentic engineering is a multiplier. Without a no-slop pass it multiplies inattention — you get mediocre code, fast, that runs and passes the wrong tests. The checklist is cheap. Skipping it is expensive. This is the standard that makes the speed worth having.

---

Previous: [Lesson 11 · Context and the second brain](11-context-and-the-second-brain.html) · Next: [Lesson 13 · Design discipline](13-design-discipline.html)
