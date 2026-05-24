# Lesson 15 · Review gates and shipping

> **Part 4 · Scale up** — Lesson 15 of 16

**Where this gets you:** you'll put a real gate in front of your work — and ship the next change with proof, not a feeling.

## The idea

When agents run in parallel, more work arrives faster. That's good. It also means more mediocre work arrives faster. So you need a place where mediocre gets caught before it reaches anyone. That place is the gate.

A gate isn't one check, it's a few, in order. Tests green — the eval suite from Lesson 10. A design check — the no-slop pass and the DESIGN.md from Lessons 12 and 13. And then a human taste call: you look at the result, or at two versions of it, and decide which one is good enough to keep. The agent can run the first two. Only you can make the third.

Then there's shipping, which has its own discipline, and it's a short one. Never claim done without proof.

"Deployed" is not a feeling you get when the command finishes without an error. It's a verification you ran in the same breath — a `curl` against the live URL showing the new content, a screenshot of the change in production, a fresh line in the log. If you can't point at one of those, you didn't ship. You ran a command and hoped.

This sounds strict. It's the single habit that stops you from telling someone "it's live" when it quietly isn't.

## Do it

Before your next change to your project goes out, write the gate down. A practical gate has five checks:

1. The diff is small enough to review.
2. The stated goal matches the actual change.
3. The eval or test passed.
4. The no-slop review found no unresolved issues.
5. The shipping proof is attached.

Run them in that order. Nothing ships that skips a line.

Then, for the deploy itself, decide your proof *before* you run anything. Not after.

## Your exercise

Pick the next change you'll ship to your project. Before you touch the deploy command, write down — actually write it — the exact proof you'll use to confirm it landed. Name the specific `curl` you'll run, or the screenshot you'll take, or the log line you'll grep for.

Then ship it. Run that exact check. Only after the check passes do you get to say the word "done."

**You're done when** you've shipped one change and pointed at concrete proof — a curl, a screenshot, a log line — that it's actually live.

**Practice proof:** run the gate on your project and write the result as `pass`, `fix needed`, or `blocked`, with the evidence.

## Why this matters

The gate is what keeps quality from sliding as your throughput climbs. And "proof before done" is what keeps you honest. The first time you write the proof down and then watch a deploy silently fail, you'll understand why this rule exists — and you won't ever go back to guessing.

---

Previous: [Lesson 14 · Orchestration — parallel agents](14-orchestration-parallel-agents.html) · Next: [Lesson 16 · Where to go next](16-where-to-go-next.html)
