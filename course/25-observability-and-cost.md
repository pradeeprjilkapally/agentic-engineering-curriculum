# Lesson 6.9 · Observability and cost discipline

**Where this gets you:** you'll have a four-axis observability plan and a defensible cost budget for any agentic system you ship into a customer environment.

## The idea

An agentic system you cannot observe is an agentic system you cannot ship. Cost is the second axis. Both are non-negotiable for FDE work.

Production agentic systems fail in ways traditional systems don't. The model drifts as the vendor updates it. The retrieval misses on a data shape you didn't anticipate. A tool call goes wrong on the customer's specific config. You need to see all of this before the customer notices, and you need a budget you can defend in a CFO meeting.

**Observability has four axes.**

1. **Per-step trace.** Every step of every agent loop, with input, output, latency, and cost. Without this, debugging is a guess.
2. **Eval pass rate.** The eval suite you wrote in Lesson 4.2, run on every deployment, with the trend visible over time. A drop is a leading indicator something broke.
3. **User feedback signal.** Thumbs up / down, "regenerate" clicks, explicit corrections. Capture them. Count them. They're the cheapest user research you'll ever get.
4. **Cost dashboard.** Daily token spend broken down by model, by agent, by customer-facing feature. The dimension that catches the cost spike before the bill does.

Tools that work today: Langfuse, OpenLLMetry, Arize, or your own table in Postgres. Pick one. Set it up before launch, not after the first incident.

**Cost discipline has four moves.**

1. Set a per-customer monthly budget. Automatic alert at 80 percent. Hard cap or back-pressure at 100 percent.
2. Route easy work to small or local models (Lesson 1.5). Reserve frontier APIs for the genuinely hard cases.
3. Cache aggressively. Identical prompts should not pay twice.
4. Watch tokens-per-active-user as the early-warning metric. If it climbs while user count is flat, something is looping or retrieving badly.

The pattern: in your discovery doc (Lesson 6.7), commit to a target cost-per-active-user. In your weekly update (Lesson 6.8), report against it. Every customer conversation about cost is easier when you brought the number first.

## Your exercise

For your project, sketch the four-axis observability plan and the cost budget. Include the alert threshold and what triggers a model-routing change.

**You're done when** you can defend the plan to a customer's CFO in five minutes.

**Practice proof:** save as `observability.md` and `cost-budget.md` in NOTES.

## Why this matters

Customers pay for predictability. An agentic system without observability and cost discipline is a science project, not a product. As an FDE, the value you deliver is making the system feel like a product. This lesson is half of that.

---

Next: [Lesson 6.10 · Security and compliance for AI products](26-security-and-compliance.html)
