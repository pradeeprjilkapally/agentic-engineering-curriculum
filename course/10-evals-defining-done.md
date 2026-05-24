# Lesson 10 · Evals — defining done

**Where this gets you:** you'll write the test before the code — so "done" is something the agent can check itself, not something you eyeball after the fact.

## The idea

In Lesson 9 the brief had a done-check line. An eval is that line, made executable. It's the test — automated where possible — that goes green or red and tells you, without your judgment in the loop, whether the work is finished.

Here's the uncomfortable part. If you can't describe "working" precisely enough to test it, you're not ready to hand off. Whatever the agent gives you back, you'll have no firm ground to reject it on — so you'll accept slop, and the slop is yours. You authored it in advance, the moment you handed off a fuzzy goal.

So write the eval first. Before any code. This isn't bureaucracy — it's the same discipline as test-driven development, and it works for the same reason: writing the test forces you to decide what "correct" actually means while you still have the freedom to think clearly about it. Do it after, and the code quietly defines "done" for you.

One catch. The agent is done when the eval is green **and** it passes a taste check. The eval catches what you specified. It can't catch what you forgot to specify — clumsy UX, a confusing name, a slow path. Green eval, then your eyes. Both, every time.

And use real test data. An eval that runs against fixtures you hand-picked to pass is an eval that lies. Feed it the empty input, the malformed row, the thing that was actually down last Tuesday. A test that can't fail isn't protecting you.

## Do it

Take the brief you wrote in Lesson 9. Before writing a line of implementation:

1. Turn the done-check into a real test — a unit test, an integration test, a script that exits non-zero on failure. Whatever your project can run.
2. Use real-shaped data. Include at least one unhappy case: empty, null, malformed, or the dependency being down.
3. Run it. Watch it fail — it should, there's no code yet. A test that passes before the feature exists is testing nothing.
4. Hand off the **brief and the eval together.** The eval is now the agent's definition of done.

Use the eval shape that fits your project:

| Project | First eval |
|---|---|
| CLI | Given this input, command prints this output and exits successfully |
| Web app | This page/action renders the expected state |
| API | This request returns the expected status and body |
| Data workflow | This query/run returns expected counts or validation checks |
| Agent workflow | Given this task, the agent must produce this artifact and pass this check |

Example eval commands:

```bash
# CLI project
python -m your_cli sample-input.csv --out /tmp/output.csv
diff tests/expected-output.csv /tmp/output.csv

# JavaScript app or package
npm test

# Python app or data workflow
pytest

# API check
curl -sS http://localhost:3000/health
curl -sS -X POST http://localhost:3000/api/example \
  -H "content-type: application/json" \
  -d '{"input":"sample"}'
```

## Your exercise

Run two handoffs of the same change. First: brief plus eval, as above. Second (or just recall a past one): brief with no eval, "looks right" as the bar.

Compare. How many rounds did each take? Which result did you actually trust?

**You're done when** you've shipped a change where the eval was written before the code, it failed first and passed last, and you can state the difference the eval made versus the no-eval handoff.

**Practice proof:** save the eval name, command, expected pass/fail behavior, and output.

## Why this matters

From here on you'll hand work to agents you're not watching — sometimes several at once. An eval is what lets you do that safely. It's the difference between "I think this works" and "this is green, and I checked it." One of those scales. The other doesn't.

---

Previous: [Lesson 9 · The brief](09-the-brief.html) · Next: [Lesson 11 · Context and the second brain](11-context-and-the-second-brain.html)
