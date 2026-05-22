# Lesson 7 · Build it, step by step

> **Part 2 · Build something real** — Lesson 7 of 16

**Where this gets you:** the first real slice of your project actually built and running — one meaningful piece, done and working.

## The idea

You have an approved plan. Now you execute it — and the way you execute is the lesson.

The temptation is the mega-prompt: hand the agent the whole plan, walk away, come back to a finished project. It almost never works. The agent drifts, you can't tell where it went wrong, and reviewing a thousand lines at once is its own job. You end up trusting code you never really read.

Build in slices instead. Take one piece of the plan — small enough that you can review it in a few minutes. Let the agent build just that. Then:

- **Review it.** Read the diff. Does it do what you asked, and only that?
- **Run it.** Don't take "it works" on faith. Run the code, see the output.
- **Course-correct.** If it's off, say so now, before the next slice stacks on top.
- **Commit.** When a slice is good, commit it. Small commits are your undo button — when something later goes sideways, you have a clean point to fall back to.

Keep your asks scoped. "Add the parser" is reviewable. "Add the parser, the validation, the error handling, and the tests" is four slices pretending to be one.

When it goes sideways — and sometimes it will — don't try to patch your way out. Stop. Back up to your last good commit. Re-plan that slice. A clean restart on one slice beats debugging a tangle the agent half-built.

## Do it

Take the first slice from your approved plan. Ask the agent to build just that piece. When it's done, read the diff, run the code, and confirm the piece does what the plan said.

If it's right, commit it with a short message. If it's wrong, correct the agent and let it revise — or, if it's badly off, reset to your last commit and re-plan the slice. Either way, end with one piece that genuinely works.

## Your exercise

Build the first real slice of your project. Get one meaningful piece working — reviewed, run, and committed.

**You're done when** one real piece of your project runs — and you've seen it run, not just been told it does.

## Why this matters

Small slices are how you stay the engineer instead of the spectator. You review what you can actually review, you catch drift early, and every commit is a safe point to return to. This is the rhythm — slice, review, run, commit — that the rest of your project gets built on. Get comfortable with it now.

---

Previous: [Lesson 6 · Plan before you build](06-plan-before-you-build.md) · Next: [Lesson 8 · Ship it](08-ship-it.md)
