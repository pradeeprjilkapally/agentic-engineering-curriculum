# Lesson 6.11 · The handoff playbook

**Where this gets you:** you'll deliver a handoff package that lets the customer team run the system without you within one sprint of you leaving. That's what separates an FDE from a contractor.

## The idea

**Handoff** isn't the end of the engagement. It's the test of whether you did the rest of the engagement right.

You did the work. The customer team helped. Now they have to run it without you. Skip handoff and the system rots in 90 days, and the customer remembers it as your fault. Do it right and you get re-engaged and referred.

**What that looks like when it goes wrong.** Three months after you leave, costs triple overnight. The on-call engineer has never seen the pipeline. There's no runbook, so she guesses: pins the model back to the version in the old commit message. Costs drop. So does accuracy, quietly, because that older model never passed your eval suite — which nobody is running, because it lives in your laptop's CI config. Six weeks later the team is rewriting the retrieval layer from scratch, since no one wrote down why it was chunked that way. You never hear about any of it. You just don't get called again.

The handoff package has six parts.

**1. README.md.** What this is in two sentences. How to run it locally. The smoke test that proves it works.

**2. Architecture diagram and `decisions/`.** The why behind the choices. Future engineers will second-guess every one of them; `decisions/` pre-empts the rewrites. Include the choices you didn't make, and why.

**3. Runbook.** The ten most common operational tasks, step by step. How to bump the model version. How to update the brain. How to recover from a failed deployment. How to read the cost dashboard and act on it.

**4. Eval suite.** Runnable by the customer's CI, with a clear pass/fail threshold and the trend visible in their observability stack.

**5. Observability dashboard.** Lesson 6.9's four-axis plan, wired and live in their environment, not yours.

**6. Training sessions.** Two or three recorded sessions with the customer engineers who'll own the system. Structure each one: a walkthrough, a hands-on exercise, a Q&A. Don't skip the recordings. The team operating this in six months isn't necessarily the team you trained.

What makes all this cheap is when you write it. Start the handoff doc on day one, not week twelve. Every decision goes into `decisions/` as you make it. Every operational task you do, you write down in the runbook draft. By handoff, the doc is 80 percent done because you've been writing it all along.

One more pattern takes a handoff from good to memorable: leave behind a `future-you.md`. The five things you wish you'd known on day one that the customer team is about to need. Candid, what you'd tell your replacement. Customers value this more than the architecture diagram.

## Your exercise

For your project, draft two artifacts:

- The runbook (ten tasks, step by step).
- The `future-you.md` file (five candid lessons from the engagement).

**You're done when** a competent engineer reading the handoff package can take over the system within a sprint.

**Practice proof:** save both in NOTES as `runbook.md` and `future-you.md`.

**Build on it:** build a CLI that scans a repo for the six handoff artifacts and prints a readiness scorecard — missing runbook, stale `decisions/`, no eval threshold.

## Why this matters

Handoff is what makes a Forward Deployed engagement feel great on both sides. The customer team can run the system without you. You get re-engaged, referred, remembered.

You finished the course. You walked in as a senior full-stack engineer. You're walking out with the operating system for Forward Deployed work.

---

The next step is your first real engagement. The course gave you the operating system. Now go run it on something real, with someone real, and ship.

If you want a day-by-day plan to take this from theory to ready, see **[Two-week FDE ramp](TWO_WEEK_FDE_RAMP.html)** (with a compressed 1-week intensive variant inside for hiring-filter use).

---

Previous: [Lesson 6.10 · Security and compliance](26-security-and-compliance.html) · Next: [Lesson 7.1 · Building on the API](28-building-on-the-api.html)
