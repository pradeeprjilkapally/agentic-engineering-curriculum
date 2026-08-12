---
title: "Lesson 6.9 · Observability and cost discipline"
---

# Lesson 6.9 · Observability and cost discipline

**Where this gets you:** you'll have a four-axis observability plan and a defensible cost budget for any agentic system you ship into a customer environment.

## The idea

A system you can't watch is a system you can't ship. **Observability** is seeing what your agent actually did. **Cost discipline** is knowing what it cost before someone else tells you. Both are non-negotiable in FDE work.

Agentic systems fail in ways ordinary software doesn't. The model drifts when the vendor updates it. Retrieval misses on a data shape you never saw. A tool call breaks on the customer's config. Catch that before they do — and carry a budget you can defend in a CFO meeting.

**Here's what missing both looks like.** An agent's search tool starts timing out against a customer's slow index. Retry logic does its job: three attempts, full context re-sent each time. Nothing errors. The demo still works. Nobody notices for weeks — until the invoice lands, several times what you quoted. A trace would have shown the retries on day one. A cost dashboard would have shown the slope on day two. Instead the customer found it first, and now the conversation isn't about the fix. It's about your numbers.

**Observability has four axes.**

1. **Per-step trace.** Every step of every agent loop: input, output, latency, cost. Without it, debugging is guessing.
2. **Eval pass rate.** The eval suite from Lesson 4.2, run on every deployment, trend visible over time. A drop is your earliest warning that something broke.
3. **User feedback signal.** Thumbs up / down, "regenerate" clicks, corrections. Capture them, count them. Cheapest user research you'll ever get.
4. **Cost dashboard.** Daily token spend, split by model, by agent, by feature. This is what catches the spike before the bill does.

Tools that work today: Langfuse, OpenLLMetry, Arize, or your own Postgres table. Pick one. Set it up before launch, not after the first incident.

**Cost discipline has four moves.**

1. Set a per-customer monthly budget. Alert at 80 percent. Hard cap or back-pressure at 100 percent.
2. Route easy work to small or local models (Lesson 1.5). Save frontier APIs for the hard cases.
3. Cache aggressively. Identical prompts shouldn't pay twice.
4. Watch tokens-per-active-user. If it climbs while user count is flat, something is looping or retrieving badly.

The pattern: commit to a target cost-per-active-user in your discovery doc (Lesson 6.7). Report against it in your weekly update (Lesson 6.8). Every cost conversation goes better when you brought the number first.

## Your exercise

For your project, sketch the four-axis observability plan and the cost budget. Include the alert threshold and what triggers a model-routing change.

**You're done when** you can defend the plan to a customer's CFO in five minutes.

**Practice proof:** save as `observability.md` and `cost-budget.md` in NOTES.

**Build on it:** build a CLI that wraps your agent, logs every step's tokens and latency to a SQLite table, and prints a per-run cost summary.

## Why this matters

Customers pay for predictability. An agentic system without observability and cost discipline is a science project, not a product. Making it feel like a product is the value you deliver as an FDE. This lesson is half of that.

---

Next: [Lesson 6.10 · Security and compliance for AI products](26-security-and-compliance.html)
