---
title: "Lesson 6.8 · Communicating to non-engineers"
---

# Lesson 6.8 · Communicating to non-engineers

**Where this gets you:** you'll have a weekly written update template and a monthly executive demo template. So the engagement stays sponsored, funded, and trusted while you ship.

## The idea

Technical work that's well communicated travels much further than technical work that's just shipped. The FDEs who get re-engaged built this habit early.

FDE work has three audiences, each with a different need.

**Engineers you're embedded with.** They live in the repo. They want PR comments, technical writeups, demos with running code. They see your work daily.

**The engineering manager or VP.** They want a weekly written update, five minutes to read. Three short paragraphs: what shipped, what's next, what's blocked. They'll defend your engagement to their leadership using the words you wrote.

**The executive sponsor who pays the bill.** They want a monthly demo, fifteen minutes, no code on screen. Charts, numbers, screenshots, outcomes. They decide whether to renew based on this.

The discipline that makes it cheap: write the weekly Friday afternoon, ship it Friday evening. Same template every week. The monthly demo is four weeklies stitched together with charts.

Two patterns win every time.

**Lead with the metric.** Not "last week we worked on the retrieval layer." Instead: "last week the eval pass rate moved from 71 percent to 83 percent. Here's what changed and what it cost." Numbers anchor the conversation. Words drift.

**Close with the ask.** Not "let me know if you have questions." Instead: "to hit our June target, I need access to the prod read replica by Wednesday. Can you confirm by Monday?" Every update creates one specific request. That's how the engagement keeps moving.

Here's what the gap costs. Two FDEs, same six-month engagement, same quality of code. One sends the Friday note; when the sponsor's budget review lands in month four, the VP already has four months of "pass rate 71 → 83, latency halved" in her inbox and forwards it. The other has a beautiful repo nobody outside the team has ever seen. Her sponsor asks, honestly, what the contractor has been doing. She has to answer that question in a meeting she didn't schedule, with slides she built overnight. Only one of these engagements gets renewed, and it isn't the better code.

The weekly update template:

```
Subject: [Project] week of <date>

What shipped: (1 short paragraph, lead with the metric)
What's next: (1 short paragraph, named milestones)
What's blocked: (1 short paragraph, with the specific ask)

Demo / artifacts: link or short video.
```

The monthly demo agenda:

1. The number that matters this month (60 seconds).
2. What shipped against the discovery doc (5 minutes).
3. Live demo of the customer-facing feature (5 minutes).
4. Risks and asks (3 minutes).
5. What's next month (2 minutes).

## Your exercise

Write your weekly update template and your monthly demo agenda. Apply both to a real or hypothetical engagement and produce one weekly update.

**You're done when** you have the template, the agenda, and one example update written.

**Practice proof:** save them in NOTES as `weekly-template.md`, `monthly-demo-agenda.md`, and `weekly-example.md`.

**Build on it:** write a script that reads your week's merged PRs from the GitHub API and drafts the "what shipped" paragraph, metric first.

## Why this matters

The technical work is half the job. The other half is keeping the engagement sponsored. The FDE who communicates cleanly keeps the budget. The one who hides in the repo gets cut at the next quarterly review, no matter how good the code is.

---

Next: [Lesson 6.9 · Observability and cost discipline](25-observability-and-cost.html)
