# Lesson 6.11 · The handoff playbook

**Where this gets you:** you'll be able to deliver a handoff package that lets the customer team run the system without you within one sprint of you leaving, which is what separates an FDE from a contractor.

## The idea

Handoff is not the end of the engagement. It is the test of whether you did the rest of the engagement right.

You did the work. The customer team helped. Now they have to run it without you. Skip handoff and the system rots in 90 days; the customer remembers it as your fault. Do handoff right and you get re-engaged and referred.

The handoff package has six parts.

**1. README.md.** What this is in two sentences. How to run it locally. The smoke test that proves it works.

**2. Architecture diagram and `decisions/`.** The why behind the choices. Future engineers will second-guess every decision; `decisions/` pre-empts the rewrites. Include the choices you didn't make and why.

**3. Runbook.** The ten most common operational tasks, step by step. How to bump the model version. How to update the brain. How to recover from a failed deployment. How to read the cost dashboard and act on it.

**4. Eval suite.** Runnable by the customer's CI. With a clear pass/fail threshold and the trend visible in their observability stack.

**5. Observability dashboard.** Lesson 6.9's four-axis plan, wired and live in their environment, not yours.

**6. Training sessions.** Two or three sessions, recorded, with the customer engineers who will own the system after you leave. The sessions are structured: a walkthrough, a hands-on exercise, a Q&A. Don't skip the recordings; the team that operates the system in six months is not necessarily the team you trained.

The discipline that makes this cheap: you start writing the handoff doc on day one of the engagement, not week twelve. Every decision you make goes into `decisions/`. Every operational task you do, you write down in the runbook draft. By the time handoff arrives, the doc is 80 percent done because you've been writing it the whole time.

A second pattern that takes the handoff from "good" to "memorable": leave behind a `future-you.md` file. The five things you wish you had known on day one that the customer team is about to need. Honest, candid, what you'd tell your replacement. Customers value this more than the architecture diagram.

## Your exercise

For your project, draft two artifacts:

- The runbook (ten tasks, step by step).
- The `future-you.md` file (five candid lessons from the engagement).

**You're done when** a competent engineer reading the handoff package can take over the system within a sprint.

**Practice proof:** save both in NOTES as `runbook.md` and `future-you.md`.

## Why this matters

Handoff is what makes Forward Deployed engagements feel great on both sides. The customer team is capable of running the system without you. You get re-engaged, referred, and remembered. Everyone wins.

You finished the course. You walked in as a senior full-stack engineer. You're walking out with the operating system for Forward Deployed work. Ready to apply it on something real.

---

The next step is your first real engagement. The course gave you the operating system. Now go run it on something real, with someone real, and ship.

If you want a day-by-day plan to take this from theory to ready, see **[Two-week FDE ramp](TWO_WEEK_FDE_RAMP.html)** (with a compressed 1-week intensive variant inside for hiring-filter use).

---

Previous: [Lesson 6.10 · Security and compliance](26-security-and-compliance.html) · Next: [Lesson 7.1 · Building on the API](28-building-on-the-api.html)
