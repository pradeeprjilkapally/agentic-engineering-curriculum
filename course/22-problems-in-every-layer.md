# Lesson 6.6 · The problems in every layer

**Where this gets you:** you'll have a one-page failure-mode inventory for any agentic system — the single best document to put in the first PR of a new engagement.

## The idea

LLMs hallucinate. Agents cascade-fail. Harnesses lock you in. Second brains rot. Teams pay a coordination tax. Solo founders burn out.

The bug is almost never in the layer you're looking at.

Most engineers debug where the symptom shows. Forward Deployed Engineers debug where the cause lives. Those are rarely the same layer, and knowing that is most of the job.

**A real one.** A support bot starts citing a refund policy the company doesn't have. Everyone blames the model — it's making things up. It isn't. Retrieval returned nothing for that question (application layer), because the harness silently truncated the policy doc to fit the context window (harness layer), because someone swapped in a cheaper small-context model last sprint to cut the bill (model layer). Three layers, one symptom. Tighten the prompt and you'll spend a week watching it come back. Name all three and you fix it in a morning.

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

Read the table twice and one thing should bother you: every mitigation in that third column is its own small project. Evals are a project. The no-slop review pass is a project. The intel-watch is a project. You can spend an entire engagement hardening one layer — and sometimes that's exactly the right call, as long as you said so out loud on day one.

## Your exercise

For your project, write down the most likely failure mode at each layer that applies. Next to each, write the one-line mitigation you'd ship before launch.

Skip the layers that don't apply. A CLI with no retrieval has no application-layer retrieval miss. Don't pad it.

**You're done when** you have a one-page failure-mode-and-mitigation doc for your project — the document you'd want to see in the first PR of any FDE engagement, including your own.

**Practice proof:** save it in `NOTES.md` as `failures.md`.

**Build on it:** write a CLI that reads `failures.md` and fails the build if any layer you marked "applies" has no mitigation line — a lint pass for your own inventory.

## Why this matters

Looking across layers is what makes you valuable. The common story: you ship, it works for a week, something strange appears, and three days go into debugging the wrong layer. The FDEs customers ask for by name are the ones who wrote the failure modes down before launch and shipped the mitigations before anyone had to ask.

The inventory is the deliverable. Carry it into the next lessons, where you'll scope the engagement, talk to non-engineers, watch cost and behavior in production, and hand the system off cleanly.

---

Previous: [Lesson 6.5 · The team shape](21-team-shape.html) · Next: [Lesson 6.7 · Discovery and scoping the engagement](23-discovery-and-scoping.html)
