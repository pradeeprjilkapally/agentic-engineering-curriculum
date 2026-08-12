---
title: "Lesson 3.4 · Ship it"
---

# Lesson 3.4 · Ship it

**Where this gets you:** the first version of your project out of your editor and in front of reality. Running, deployed, or usable by someone who isn't you.

## The idea

A project that only runs on your machine is a draft. **Shipping** means a URL someone can open, a command someone can install, or a thing someone else can try.

The first version can be rough. Shipping early is contact with reality — how it behaves deployed, what people actually click, feedback you can't get alone.

What "shipped" can look like, depending on your project:

- **A deployed URL**. The page or tool live somewhere, on a free host if that's all it needs.
- **An installable command**. Packaged so someone can run it without your dev setup.
- **Something a friend can try**. Handed to one other person who can use it start to finish.

Pick whichever fits. The bar's the same: it left your machine, or someone else can run it.

And "shipped" means verified. The deploy prints a green checkmark and a URL, you paste it in Slack, done. Except the build never picked up your local `.env`, so the API key in production is a placeholder and every request 500s. The deploy succeeded. The site is broken. Nobody finds out until someone opens the link — better that someone is you, thirty seconds after deploying, than the person you were trying to impress.

So open the URL. Run the installed command. Watch someone use it. Don't say shipped until you've seen it work where it lives.

## Do it

Decide your shipping form: deployed, installable, or handed to a friend. Ask the agent to help. It can set up a deploy to a free host, package the command, or write the short instructions another person would follow.

Then ship it. Then verify it. Open the live URL, run the installed command fresh, or watch your friend use it. Confirm with your own eyes that it works where it lives.

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

**You're done when** someone other than you could use it, or you have a link or command, verified working, that proves it runs.

**Practice proof:** paste the URL, command output, screenshot note, or PR link into `NOTES.md`. Do not write "shipped" without proof beside it.

**Build on it:** build `shipcheck`, a one-command tool that requests a URL and fails unless it returns 200 and contains a string you specify.

## Why this matters

Shipping is the moment a project stops being yours alone and starts being real. Everything in Part 4 — briefs, evals, the no-slop standard — exists to make what you ship hold up under actual users. You can't practice that on something that never left your laptop. Get this first version out, rough as it is, and the rest of the course has something true to sharpen.

---

Previous: [Lesson 3.3 · Build it, step by step](07-build-it-step-by-step.html) · Next: [Lesson 4.1 · The brief](09-the-brief.html)
