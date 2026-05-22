# Lesson 4 · Staying in control

> **Part 1 · Get set up** — Lesson 4 of 16

**Where this gets you:** you'll know the permission modes, how to read a diff before you accept it, and how to redirect the agent when it's wrong.

## The idea

By default, the agent asks before it touches anything. Before it edits a file or runs a command, it stops and shows you what it's about to do. You approve, or you don't. That pause is the whole point — it's where you stay the reviewer.

There are four modes, and you cycle through them with **Shift+Tab**:

- **Default** — asks every time, before every edit and every command. Slower, and exactly right while you're learning. Start here.
- **Accept-edits** — auto-accepts file edits, so the agent keeps moving without stopping at each one. Faster, but you're now reviewing after the fact instead of before.
- **Plan mode** — read-only. The agent looks but changes nothing; it proposes a plan and waits for your go-ahead. We cover this properly in Lesson 6 — for now just know the name and that it exists.
- **Bypass** — skips every prompt. The agent edits and runs whatever it wants, no pause. Only use this in a throwaway or isolated environment — a scratch container, a repo you'd be fine deleting. In anything real, bypass means a command you'd never have approved runs before you see it. Don't.

No mode removes your job. In Default you review before; in Accept-edits you review after; in bypass there's no built-in pause at all, so you'd better have your own. You stay the reviewer regardless.

**Reading a diff** is the skill underneath all of this. When the agent shows a change, don't skim the green. Read the removed lines and the added lines together — what's actually different? Does it touch only what you asked? Any file you didn't expect? If a line looks wrong, **reject it** and say why: "that breaks the null case — handle empty input too." The agent takes the correction and tries again. Rejecting isn't failure; it's the loop working.

## Do it

In a repo you know, start `claude` in Default mode. Give it a small task. At each prompt, actually read the diff before you approve — out loud if it helps.

Then press **Shift+Tab** to reach Accept-edits and give it a similar task. Notice it doesn't stop — you're reading changes as they land instead of before.

## Your exercise

Do two small tasks in a repo you know. The first in **Default mode** — approve each step and read every diff before you accept it. The second, something similar, in **Accept-edits** — let the edits land, then review them together at the end.

**You're done when** you've used at least two modes and can say plainly when you'd pick each one.

## Why this matters

As the tasks get bigger, the temptation is to stop reading and just accept. The modes exist so you can move faster *on purpose* — not so you can stop reviewing. Knowing the trade-off now means you'll speed up where it's safe and slow down where it counts, instead of finding out which was which after something breaks.

---

Previous: [Lesson 3 · Your first session](03-your-first-session.md) · Next: [Lesson 5 · Pick your first project](05-pick-your-first-project.md)
