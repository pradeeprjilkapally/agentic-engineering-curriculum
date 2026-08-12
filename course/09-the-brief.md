---
title: "Lesson 4.1 · The brief"
---

# Lesson 4.1 · The brief

**Where this gets you:** you'll write a brief instead of a vague ask, and start reviewing whether the brief was right instead of babysitting every choice the agent makes.

## The idea

In Part 3 you built and shipped something. The prompts that went badly weren't badly worded. They were under-specified. You said "add search" and the agent guessed at ten things you never said. Some guesses were fine. You found out which by reading the diff.

A **brief** fixes that. A brief is a contract, not a description. A description says what you want in a sentence. A contract states the goal, the constraints, the inputs, the outputs, and the check that defines "done." That last one is the part people skip. Write all five and there's nothing left to guess.

**Here's the gap.** You ask for search on your orders page. The agent matches on order ID, case-sensitively, with no limit. Typing `hoff` finds nothing; an empty box returns every row you have. The diff looks reasonable, because nothing in it contradicts anything you said. You said nothing. Now write one line first — *searching `hoff` finds `Hoffman`, an empty query returns no rows* — and the same agent, on the same afternoon, builds the thing you meant.

A brief costs thirty seconds. In exchange the agent gets its context and you get something concrete to review against.

It also moves your job. Without a brief you review implementation choices — should it be a dropdown or a list? — decisions you never made and now have to second-guess. With a brief you review one thing: was the brief right? That's the only question worth your attention.

## Do it

Use this six-line template:

```
Goal:         the one outcome, in a sentence.
Constraints:  what it must (and must not) do. Stack, perf, style, security.
Inputs:       what the agent starts with. Files, data, an API, an example.
Outputs:      what exists when it's finished. Files, endpoints, behavior.
Done-check:   the concrete test that proves it works.
Out-of-scope: what NOT to touch, so it doesn't wander.
```

The done-check is the load-bearing line. "It works" is not a done-check. "Running `npm test` passes, and `/search?q=foo` returns matching rows" is.

## Your exercise

Pick the next real change to your project — the feature or fix you'd make anyway. Write a brief for it using the six lines above. Then hand it off and let the agent run.

When it comes back wrong, and the first one usually does, don't fix the code. Find the bug in the brief. Which line was vague, missing, or wrong? Fix that line and hand it off again.

**You're done when** you've shipped one change driven entirely by a written brief, and you can name the line of the brief that caused the first wrong attempt.

**Build on it:** a `brief` CLI that scaffolds the six-line template into `briefs/NNN-slug.md`, prefilled with your repo's test command as the done-check.

## Why this matters

Every lesson left in this course assumes you can hand an agent a clean spec. The brief is that skill. Get it solid now and the rest — evals, parallel agents, review gates — bolt onto it. Skip it and you're back to guessing prompts and hoping.

---

Previous: [Lesson 3.4 · Ship it](08-ship-it.html) · Next: [Lesson 4.2 · Evals. Defining done](10-evals-defining-done.html)
