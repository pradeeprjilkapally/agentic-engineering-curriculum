# Lesson 20 · Staying current — the intel-watch pattern

**Where this gets you:** you'll have a working personal intel-watch — a pipeline that scans the people whose signal matters to you, filters for what matters to your projects, and surfaces it to you while you sleep. No more doom-scrolling.

## The idea

You will not stay current by doom-scrolling. You will stay current by wiring a small pipeline: a trusted-voices feed, a local model that judges relevance, an alerting channel, and a brain page that updates while you sleep.

The pattern has four parts.

**1. Trusted voices list.** Pick 20 to 40 people on X whose signal actually matters for the projects you care about. Researchers, builders, VCs adjacent to your stack. Add their handles to a config file. Then pick 5 to 15 blogs whose RSS feeds matter and add those too. The point is to curate aggressively. The wide internet is noise; this small list is signal.

**2. Scanner.** A small script that runs on a schedule (every 3 to 6 hours is enough). It pulls recent posts from your voices, strips the obvious noise (replies, retweets you don't care about, low-engagement posts), and hands the survivors to step 3.

**3. Local judge.** A local small model (Gemma 9B, Llama 8B, Qwen 4B — your pick based on hardware) reads each post with a short prompt: "Is this a signal for any of these projects: X, Y, Z? If yes, return what kind of signal and which project. If no, skip." Local because it's fast, free, and the privacy stays on your machine.

**4. Routing and alerting.** For each signal the judge keeps: append a row to that project's brain page under a section like `## Industry signals`, with the date, source, and a one-line summary. Send a notification (Telegram, Slack DM, whatever you use) so you know something landed.

The result: you wake up to a brain page that captured what mattered overnight, with a quiet alert when something genuinely big moves. You read the brain page over coffee, not Twitter.

Why this works:

- Trusted voices filter the noise for you. You're not scanning the whole internet; you're scanning a curated set of people who have already filtered it once.
- The local model judge keeps cost at zero and privacy on your machine.
- The brain page makes the signal queryable later. Months from now you can ask "what did this person say about memory in May?" and get a grounded answer with the source.

The pipeline doesn't have to be sophisticated. The first version is one config file, one script, one launchd entry. You can ship it in an afternoon.

## Your first exercise

Pick 10 people on X whose signal matters for the projects you care about. Pick 3 projects you're tracking. Write the judge prompt in plain language (you'll wire it to a model later). Sketch the four-part pipeline in your notes — even before you write any code.

**You're done when** you can describe the pipeline end-to-end to another engineer and they could go build it.

**Practice proof:** save the list of voices, the project list, and the judge prompt in `NOTES.md` under "intel-watch sketch."

## Why this matters

The edge a Forward Deployed Engineer has over a generalist engineer is being three days ahead of the field, not three weeks. Three days = personal intel watch. Three weeks = LinkedIn. You want to be at three days, and you want it to cost you almost no time per day to maintain.

---

Next: [Lesson 21 · The team shape](21-team-shape.html)
