# Lesson 14 · Orchestration — parallel agents

> **Part 4 · Scale up** — Lesson 14 of 16

**Where this gets you:** you'll take a multi-part task and run its independent pieces as parallel agents instead of one serial chain — and see where the real difficulty moves.

## The idea

Once your briefs are tight, your evals catch regressions, and your second brain feeds the agent good context, something interesting happens. The thing slowing you down stops being how fast the agent writes code. One agent is already faster than you. The bottleneck becomes orchestration — how many separate streams of work you can keep coherent at the same time.

Here's the move. When a task splits into N pieces that don't depend on each other, you don't do them one after another. You spawn N agents, one per piece, and let them run side by side. Three independent things take as long as the slowest one, not the sum of all three.

Subagents do something similar for the messy side work. You send a subagent off to "find every place we call the old API" or "summarize what these twelve files do." It burns through a pile of reading, comes back with a short answer, and your main session never gets clogged with the noise.

A two-person team running parallel agents on three streams will out-ship a five-person team running serial on one. That's not a clever trick. It's just arithmetic once each individual stream is reliable.

## Do it

Take a task on your project with several parts. Ask first: which pieces are *genuinely* independent? Two streams are independent only if neither needs the other's output. If piece B reads a file piece A creates, they're not parallel — they're a chain.

Parallel does not have to mean two different products. It can be:

| Stream A | Stream B |
|---|---|
| Implementation | Tests |
| Frontend copy/layout | Backend/API change |
| Bug investigation | Documentation update |
| Data validation | UI polish |

Then launch them together. In Claude Code, describe the parts and ask it to run them as parallel agents, or hand discrete chunks to subagents. The key is launching them in one go, not babysitting one before starting the next.

## Your exercise

Find a multi-part task on your project. A few unrelated bug fixes. Three small features. A refactor plus its tests plus its docs.

Split it honestly into independent pieces. Run those as parallel agents or subagents. Then watch what's actually hard — it won't be the speed. It'll be keeping the streams coherent: making sure two agents don't edit the same file, that their briefs don't contradict, that the merged result still hangs together.

**You're done when** you've run at least two genuinely independent pieces of one task in parallel, and can name the part that was hard to keep coherent.

**Practice proof:** write the two stream names, their owners/sessions, their files, and the merge order.

## Why this matters

Speed was never the real skill. Any agent is fast. The skill is being the person who can hold three streams in their head, give each a clean brief, and stitch the results back into one thing that works. That's what scales — and it's the difference between using an agent and running a small fleet of them.

---

Previous: [Lesson 13 · Design discipline](13-design-discipline.md) · Next: [Lesson 15 · Review gates and shipping](15-review-gates-and-shipping.md)
