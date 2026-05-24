# Lesson 8 · Ship it

**Where this gets you:** the first version of your project out of your editor and in front of reality — running, deployed, or usable by someone who isn't you.

## The idea

A project that only runs on your machine, in your terminal, while you watch it, isn't shipped. It's a draft. Shipping means it crosses the line into something real — a URL someone can open, a command someone can install, a thing a friend can actually try.

This first version is allowed to be rough. Shipping early isn't about polish. It's about contact with reality, because reality finds the things you missed. The deployed version behaves differently from the local one. The friend uses it in an order you never tested. That feedback is worth more than another hour of solo tweaking.

What "shipped" can look like, depending on your project:

- **A deployed URL** — the page or tool live somewhere, on a free host if that's all it needs.
- **An installable command** — packaged so someone can run it without your dev setup.
- **Something a friend can try** — handed to one other person who can use it start to finish.

Pick whichever fits. The bar is the same: it left your machine, or someone else can run it.

One thing to be honest about: "shipped" means you verified it works. Not "the deploy command finished" — you actually opened the URL, ran the installed command, watched it do the thing. A deploy that didn't really land is worse than no deploy, because now you think it's done. We'll go deep on this discipline in Lesson 15. For now, just hold the line: don't say shipped until you've seen it work where it shipped to.

## Do it

Decide your shipping form — deployed, installable, or handed to a friend. Ask the agent to help: it can set up a deploy to a free host, package the command, or write the short instructions another person would follow.

Then ship it. And then verify it — open the live URL, run the installed command fresh, or watch your friend use it. Confirm with your own eyes that the thing works where it now lives.

Pick the proof that fits:

| Project type | Shipping proof |
|---|---|
| CLI | Command output showing the feature works |
| Web page | Local or deployed URL plus screenshot |
| Library | Test output and usage example |
| Data workflow | Approved run output and row/count/check summary |
| Team repo | PR link and CI/check result |

## Your exercise

Ship the first version of your project.

**You're done when** someone other than you could use it, or you have a link or command — verified working — that proves it runs.

**Practice proof:** paste the URL, command output, screenshot note, or PR link into `NOTES.md`. Do not write "shipped" without proof beside it.

## Why this matters

Shipping is the moment a project stops being yours alone and starts being real. Everything in Part 3 — briefs, evals, the no-slop standard — exists to make what you ship hold up under actual users. You can't practice that on something that never shipped. Get this first version out, rough as it is, and the rest of the course has something true to sharpen.

---

Previous: [Lesson 7 · Build it, step by step](07-build-it-step-by-step.html) · Next: [Lesson 9 · The brief](09-the-brief.html)
