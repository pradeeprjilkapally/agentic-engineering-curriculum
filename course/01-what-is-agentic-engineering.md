# Lesson 2.1 · What is agentic engineering?

**Where this gets you:** you'll be able to say plainly what a coding agent is, how it's different from the AI you've already used, and why "agentic engineering" is a real skill and not a buzzword.

## The idea

If you've used AI to write code, it was probably autocomplete — it finishes your line and you keep typing — or a chat window you paste errors into. Useful, but you're still doing the work, keystroke by keystroke.

An agent is different. You hand it a goal — "add a logout button," "figure out why this test keeps failing" — and it goes and works. It reads your files, makes a plan, edits code, runs it, sees what broke, tries again. One sentence from you can turn into fifteen minutes of finished work. Your job moves: you're judging the result now, not typing every line.

That's the shift: stop operating a tool, start directing one.

![A team leaning over charts and notes, pointing and deciding together — the shift from typing to directing and judging the work.](../assets/photos/directing-work.jpg)

*Your job starts looking less like typing and more like this: pointing, deciding, judging what came back.*

There are two ways people direct an agent.

The first is the one most people drift into. Type a prompt, glance at what comes back, looks fine, move on. No plan, no definition of "done" except that it ran once. Call it **vibe coding**. It's quick, it's genuinely fine for experiments and learning, and it falls apart the moment real users touch the thing.

The second is **agentic engineering**. You write the agent a real brief. You decide up front how you'll know it worked. You hold the output to a standard and ship it with proof. Same agent, same model as the person vibe coding next to you — but the work that comes out is not close.

**What that gap looks like in practice.** Two engineers get the same ticket: "add password reset." The vibe coder types "add password reset to my app," gets code that looks right, and ships it — no test for the expired-token case, no rate limit, tokens logged in plaintext. It works in the demo and breaks in week two. The agentic engineer writes three lines first — *reset link expires in 30 min, one active token per user, never log the token* — has the agent build to that, and checks each against a test before shipping. Same tool, same afternoon. One of them gets paged at 2am.

This course teaches the second way: not prompt tricks, habits.

You do not need years of experience to learn this. Fresh graduates can follow the course by keeping the project small and reading every diff carefully. Experienced engineers can move faster, but the standard is the same: you are responsible for the brief, the review, and the proof.

## Your exercise

You will build something real through this course, so start looking now.

Write down three small things you could build or fix. Next to each, add one line for what it does and one line for how you'd know it works.

Good candidates: a one-command CLI, a small page, an internal tool, a bug fix, or the script you keep meaning to write.

**You're done when** you have three candidates written down. You'll pick one in Lesson 3.1.

**Practice proof:** save the three candidates somewhere durable, like `NOTES.md`. For each one, include the check that would prove it works.

## Why this matters

Every lesson after this hands you a new skill and asks you to use it on a real project. Do that on a throwaway toy and it stays trivia you'll forget by Friday. Do it on something you actually care about and it turns into how you work. So pick real candidates. The whole course compounds on that one choice.

---

Next: [Lesson 2.2 · Install your tool](02-install-your-tool.html)
