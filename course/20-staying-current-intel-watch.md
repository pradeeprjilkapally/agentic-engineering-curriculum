---
title: "Lesson 6.4 · Staying current: the intel-watch pattern"
---

# Lesson 6.4 · Staying current: the intel-watch pattern

**Where this gets you:** you'll have a working personal **intel watch**. A pipeline that scans the people whose signal matters to you, filters for what matters to your projects, and surfaces it while you sleep. No more doom-scrolling.

## The idea

Doom-scrolling won't keep you current. A small pipeline will: a trusted-voices feed, a local model that judges relevance, an alert channel, and a brain page that updates overnight.

**What being late costs.** A maintainer posts that the SDK your project depends on is deprecating its streaming API, with a six-week window. You don't follow that maintainer, so you miss it. Five weeks later you're mid-demo when the calls start failing, and you spend the weekend migrating under pressure. The post was public the whole time. One line in a config file would have put it in front of you the next morning.

The pattern has four parts.

**1. Trusted voices list.** Pick 20 to 40 people on X whose signal actually matters for your projects. Researchers, builders, VCs adjacent to your stack. Put their handles in a config file. Add 5 to 15 blogs by RSS. Curate aggressively. The wide internet is noise; this small list is signal.

**2. Scanner.** A script on a schedule (every 3 to 6 hours is enough). It pulls recent posts from your voices, strips the obvious noise (replies, retweets, low-engagement posts), and hands the survivors to step 3.

**3. Local judge.** A local small model (Gemma 9B, Llama 8B, Qwen 4B. Your pick based on hardware) reads each post with a short prompt: "Is this a signal for any of these projects: X, Y, Z? If yes, return what kind of signal and which project. If no, skip." Local because it's fast, free, and the data stays on your machine.

**4. Routing and alerting.** For each signal the judge keeps, append a row to that project's brain page under `## Industry signals` with the date, source, and a one-line summary. Send a notification (Telegram, Slack DM, whatever you use) so you know something landed.

You wake up to a page that captured what mattered overnight, and a quiet alert when something big moves. You read that page over coffee, not Twitter.

Why it works:

- Your voices already filtered the internet once. You're scanning their output, not the firehose.
- The local judge keeps cost at zero and your data on your machine.
- The brain page stays queryable. Months later you can ask "what did this person say about memory in May?" and get a grounded answer with the source.

Nothing here is sophisticated. Version one is a config file, a script, and a launchd entry. Ship it in an afternoon.

## Your exercise

Pick 10 people on X whose signal matters for your project. Pick 3 projects you're tracking. Write the judge prompt in plain language (you'll wire it to a model later). Sketch the four-part pipeline in your notes, before you write any code.

**You're done when** you can describe the pipeline end-to-end to another engineer and they could go build it.

**Practice proof:** save the list of voices, the project list, and the judge prompt in `NOTES.md` under "intel-watch sketch."

**Build on it:** build a deprecation watcher — a cron job that reads your project's dependency list, scans each library's GitHub releases for breaking-change notes, and emails you a weekly digest.

## Why this matters

The edge a Forward Deployed Engineer has over a generalist is being three days ahead of the field, not three weeks. Three days is a personal intel watch. Three weeks is LinkedIn. You want three days, and you want it to cost you almost nothing per day to maintain.

---

Next: [Lesson 6.5 · The team shape](21-team-shape.html)
