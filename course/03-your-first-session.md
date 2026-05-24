# Lesson 3 · Your first session

**Where this gets you:** you'll take one small task end-to-end with an agent and understand the loop it runs — the thing every later lesson builds on.

## The idea

An agent session isn't one prompt and one answer. It's a loop, and once you've seen it run a few times you'll spot it every time.

You give it a goal. Then it goes around: **gather context** — read the files it needs to understand the task. **Act** — make an edit, run a command. **Check** — look at what happened, run the test, read the error. Then it loops: gather, act, check, gather, act, check — until the goal is met or it gets stuck and asks you.

You watch this happen in your terminal. It tells you what it's reading, what it's about to change, what the command printed. Read that as it goes. It's not noise — it's the agent thinking out loud, and it's where you catch a wrong turn early.

When it does turn wrong, you don't restart. Hit **Esc** to interrupt — it stops where it is. Then just type the correction in plain words: "no, the config lives in `settings/`, not the root" or "skip the tests for now, just make the change." It picks up from there with the new information. You're steering mid-drive, not crashing and re-parking.

One more thing that matters more than it sounds: **small asks beat one giant prompt.** A tight task — "rename this function and update its callers" — gives the agent a clear target and gives you a result you can actually check. A huge one — "refactor the whole module" — gives it room to wander and gives you a pile of changes you can't reason about. Scope down. You can always ask for the next piece.

## Do it

Open a repo you know and start your tool:

```bash
claude
```

Codex CLI users run `codex`. Gemini CLI users run `gemini`. Coco users open the approved workspace for the repo or data product.

Pick something genuinely small — a typo in a string, a renamed variable, one new log line.

Give it the goal in one sentence. Then watch. Don't touch anything. Read each step as it scrolls by — what file it opened, what it changed, what it ran.

Here is a safe first-session prompt:

```text
Find one tiny improvement in this repo that can be completed in under ten minutes.
Before editing, tell me the exact file you plan to touch and why.
After editing, show me the diff and the command or manual check you used.
```

If it heads somewhere wrong, hit **Esc** and type what you meant. Let it finish.

## Your exercise

In a repo you know well, give the agent one small, real task — something you could have done yourself in a few minutes.

Watch the whole loop run without jumping in unless it goes wrong. When it's done, read **every change it made** — open the diff, read each line, make sure you'd have signed off on it yourself.

Use these commands after the agent finishes:

```bash
# see every changed file
git status --short

# read the actual patch before accepting it
git diff

# run the smallest relevant check for your project
npm test
# or
pytest
# or
make test
```

**You're done when** you've taken one small task end-to-end and can describe the gather → act → check loop in your own words.

**Practice proof:** save the prompt you gave, the diff it produced, and the command or manual check you used to verify it. Fresh graduates should ask a human or teammate to review this first diff if possible.

## Why this matters

Everything later in this course is this loop, scaled up — bigger tasks, more of them, several at once. If the loop is clear to you on something small, the hard stuff later is just more of a thing you already understand. If it's a blur now, it stays a blur.

---

Previous: [Lesson 2 · Install your tool](02-install-your-tool.html) · Next: [Lesson 4 · Staying in control](04-staying-in-control.html)
