---
title: "Lesson 2.4 · Staying in control"
---

# Lesson 2.4 · Staying in control

**Where this gets you:** you'll know the permission modes, how to read a diff before you accept it, and how to redirect the agent when it's wrong.

## The idea

By default, the agent asks before it edits a file or runs a command. That pause is where you stay the reviewer.

There are four **permission modes**, and you cycle through them with **Shift+Tab**:

- **Default**. Asks every time, before every edit and every command. Slower, and exactly right while you're learning. Start here.
- **Accept-edits**. Auto-accepts file edits, so the agent keeps moving. Faster, but now you're reviewing after the fact instead of before.
- **Plan mode**. Read-only. The agent looks but changes nothing; it proposes a plan and waits for your go-ahead. Lesson 3.2 covers it properly. For now, just know it exists.
- **Bypass**. Skips every prompt. The agent edits and runs whatever it wants. Only for a throwaway or isolated environment: a scratch container, a repo you'd be fine deleting. Anywhere real, bypass means a command you'd never have approved runs before you see it. Don't.

No mode removes your job. In Default you review before. In Accept-edits you review after. In bypass, bring your own guardrails.

**Reading a diff** is the skill underneath all of this. Don't skim the green. Read the removed lines and the added lines together. What's actually different? Does it touch only what you asked? Any file you didn't expect?

**Why the removed lines matter.** Someone asks the agent to strip unused imports, and it's a boring task, so they're in Accept-edits. It deletes twenty imports across the repo. Nineteen were dead. The twentieth was `import logging_config` at the top of `main.py` — nothing referenced it by name, but importing it was what installed the log handlers. Nothing failed. Tests passed. It shipped. Two weeks later there's an outage and the logs for it are empty. The added lines said nothing; the removed line was the whole story.

If a line looks wrong, **reject it** and say why: "that breaks the null case. Handle empty input too." The agent takes the correction and tries again. Rejecting isn't failure; it's the loop working.

## Do it

In a repo you know, start `claude` in Default mode. Give it a small task. At each prompt, actually read the diff before you approve. Out loud if it helps.

Then press **Shift+Tab** to reach Accept-edits and give it a similar task. Notice it doesn't stop. You're reading changes as they land instead of before.

## Your exercise

Do two small tasks in a repo you know. The first in **Default mode**: approve each step and read every diff before you accept it. The second, something similar, in **Accept-edits**: let the edits land, then review them together at the end.

**You're done when** you've used at least two modes and can say plainly when you'd pick each one.

**Build on it:** write a `review-diff` shell script that runs `git diff` and prints only the removed lines, grouped by file, so you can check what an Accept-edits run quietly deleted before you commit.

## Why this matters

As the tasks get bigger, the temptation is to stop reading and just accept. The modes exist so you can move faster *on purpose*. Not so you can stop reviewing. Learn the trade-off now and you'll speed up where it's safe and slow down where it counts — instead of finding out which was which after something breaks.

---

Previous: [Lesson 2.3 · Your first session](03-your-first-session.html) · Next: [Lesson 3.1 · Pick your first project](05-pick-your-first-project.html)
