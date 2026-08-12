---
title: "Lesson 4.4 · The no-slop standard"
---

# Lesson 4.4 · The no-slop standard

**Where this gets you:** you'll install a review pass the agent runs against its own output. So quality is enforced by an artifact, not by you remembering to look hard.

## The idea

"Pay more attention" is not a system. Encode quality into something the agent reads and runs every time.

**Slop** is a list: dead code, swallowed errors, copy-paste, vague names, untested edges, comments that restate the line above. If you can check it, the agent can check it.

**What slop looks like when it bites.** You ask for a retry wrapper around a payment call. What comes back reads fine — a loop, a sleep, a `try` block. But the `except` swallows the error and returns `None`, and the test only asserts the function doesn't raise. It passes. You skim, you ship. Three weeks later the card processor starts timing out, every charge quietly returns `None`, and nobody notices until month-end reconciliation comes up short. The bug wasn't hidden. It was on line four, and it's item two on the checklist.

That's what the no-slop skill is for. This repo ships it: [`no-slop-skill/`](../no-slop-skill/SKILL.html). After the agent writes or edits non-trivial code, it walks a checklist against its own output **before** handing the work back. Every hit gets fixed, or gets one line saying why it's a deliberate exception. Nothing reaches your review gate until the checklist is clean.

The checklist ([`no-slop-checklist.md`](../no-slop-skill/no-slop-checklist.html)) has ten sections: dead code, unhandled errors, duplication, naming, untested edges, comments, consistency with the codebase, scope, fake done (TODOs and stubbed returns), and verified-not-claimed. Each item is concrete enough to be unarguable.

This is attention as an artifact.

## Do it

1. Install the skill. Copy `no-slop-skill/` into your project (Claude Code reads skills from `.claude/skills/`; check your tool's convention).
2. From `CLAUDE.md`, make it non-negotiable. The starter already has the line: *run the no-slop review pass before reporting any non-trivial change done.*
3. Run it on a recent change to your project. Have the agent walk the full checklist against it.

If your tool doesn't support skills, use the checklist anyway. Paste it into your review prompt and make the agent run through it before handing work back.

## Your exercise

Run the no-slop pass on your project's most recent real changes. Count what it catches. Every hit. Be honest; some of those are yours.

Then customize the checklist. The shipped version is a baseline. Add the slop patterns specific to your stack, and the ones *you* keep shipping. A checklist you didn't tune is one you won't trust enough to run.

**You're done when** the no-slop skill or checklist is installed, referenced from your project instructions, has run against real changes with the catch count written down, and the checklist has at least two items you added.

**Practice proof:** run the review pass on one recent change and record one fix-or-justify note.

**Build on it:** build a `slopcheck` CLI that takes a git diff, runs your checklist against it with one agent call, and prints each hit as `file:line — rule`.

## Why this matters

Agentic engineering is a multiplier. Without a no-slop pass it multiplies inattention — mediocre code, fast, running and passing the wrong tests. The checklist is cheap. Skipping it is expensive. This is the standard that makes the speed worth having.

---

Previous: [Lesson 4.3 · Context and the second brain](11-context-and-the-second-brain.html) · Next: [Lesson 4.5 · Design discipline](13-design-discipline.html)
