# Lesson 9 · The brief

**Where this gets you:** you'll write a brief instead of a vague ask — and start reviewing whether the brief was right instead of babysitting every choice the agent makes.

## The idea

In Part 2 you built and shipped something. Along the way you probably noticed a pattern: the prompts that went badly weren't badly worded, they were under-specified. You said "add search" and the agent guessed at ten things you never said. Some guesses were fine. Some weren't. You found out by reviewing the diff.

A brief fixes that. A brief is a contract, not a description. A description says what you want in a sentence. A contract states the goal, the constraints, the inputs, the outputs, and — this is the part people skip — the check that defines "done." When all five are written down, there's nothing left to guess.

A brief costs about thirty seconds. In exchange, the agent gets the context it needs and you get something concrete to review against.

And it moves your job. Without a brief, you review implementation choices — "should it be a dropdown or a list?" — decisions you never made and now have to second-guess. With a brief, you review one thing: was the brief right? That's a better question, and it's the only one worth your attention.

## Do it

Use this six-line template:

```
Goal:         the one outcome, in a sentence.
Constraints:  what it must (and must not) do — stack, perf, style, security.
Inputs:       what the agent starts with — files, data, an API, an example.
Outputs:      what exists when it's finished — files, endpoints, behavior.
Done-check:   the concrete test that proves it works.
Out-of-scope: what NOT to touch, so it doesn't wander.
```

The done-check is the load-bearing line. "It works" is not a done-check. "Running `npm test` passes, and `/search?q=foo` returns matching rows" is.

## Your exercise

Pick the next real change to your project — the next feature or fix you'd make anyway. Write a brief for it using the six lines above. Then hand it off and let the agent run.

When it comes back wrong — and the first one usually does — don't fix the code yet. Find the bug in the **brief**. Which line was vague, missing, or wrong? Fix that line, hand it off again.

**You're done when** you've shipped one change driven entirely by a written brief, and you can name the line of the brief that caused the first wrong attempt.

## Why this matters

Every lesson left in this course assumes you can hand an agent a clean spec. The brief is that skill. Get it solid now and the rest — evals, parallel agents, review gates — all bolt onto it. Skip it, and you're back to guessing prompts and hoping.

---

Previous: [Lesson 8 · Ship it](08-ship-it.html) · Next: [Lesson 10 · Evals — defining done](10-evals-defining-done.html)
