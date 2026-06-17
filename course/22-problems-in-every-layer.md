# Lesson 6.6 · The problems in every layer

**Where this gets you:** you'll have a one-page failure-mode inventory for any agentic system, which is the single best document to put in the first PR of any new engagement.

## The idea

LLMs hallucinate. Agents cascade-fail. Harnesses lock you in. Second brains rot. Teams coordination-tax. Solo founders burn out. The bug is never in the layer you're looking at.

The discipline that separates a senior engineer from a senior Forward Deployed Engineer is looking across layers when something breaks. Most engineers debug at the layer where the symptom shows. FDEs debug at the layer where the cause lives. They're almost never the same layer.

Here's the inventory you'll carry into every engagement.

| Layer | Failure mode | Mitigation |
|---|---|---|
| LLM | Hallucination, context overflow, cost spike | Evals before merge, structured output, smaller models when you can |
| Agent | Cascade failure, infinite loop, off-task drift | Step limits, per-step observability, no-slop review pass |
| Harness | Vendor lock-in, memory rent, surprise pricing | Owned brain, exports that actually work, swappable model layer |
| Application (RAG / chatbot / agentic) | Retrieval miss, persona drift, tool misuse | Eval suite, golden tests, manual review on the first 20 cases |
| Second brain | Rot, contradiction, corruption | Nightly distillation, provenance on every claim, backup discipline |
| Team coordination | Handoff loss, agent collisions, decision drift | AGENTS.md, HANDOFF.md, decisions/, branch hygiene |
| Solo workflow | Burnout, no review, hidden mistakes | Telegram heartbeats, weekly retro, a mentor outside the engagement |
| Staying current | Doom-scroll, miss the wave | Intel-watch, trusted voices, scheduled review |

A concrete pattern to internalize: when a customer-visible problem appears, the symptom is almost always at a different layer from the cause. A hallucinated answer might trace back to a retrieval miss (application layer), which traces to a misconfigured harness, which traces to a wrong model choice for that retrieval step. You cannot fix one of these without naming the others. The team that names all three first wins the debug.

A second concrete pattern: every layer's mitigation is itself a small project. Evals are a project. The no-slop review pass is a project. The intel-watch is a project. You can spend a whole engagement just hardening one layer, and sometimes that's exactly the right move.

## Your first exercise

For your project candidate, write down the most likely failure mode at each applicable layer. For each, write the one-line mitigation you would ship before launch.

**You're done when** you have a one-page failure-mode-and-mitigation doc for your project. It is the document you would want to see in the first PR of any FDE engagement, including your own.

**Practice proof:** save it in `NOTES.md` as `failures.md`.

## Why this matters

The discipline of looking across layers is what makes you valuable. Most engineers ship to a customer and the system works for the first week, then a strange behavior appears, and they spend three days debugging at the wrong layer. The FDEs the customers ask for again are the ones who name the failure modes up front and ship mitigations before anyone has to ask for them.

The inventory is the deliverable. Carry it into the next lessons, where you'll learn how to scope the engagement, talk to non-engineers, watch cost and behavior in production, and hand the system off cleanly.

---

Previous: [Lesson 6.5 · The team shape](21-team-shape.html) · Next: [Lesson 6.7 · Discovery and scoping the engagement](23-discovery-and-scoping.html)
