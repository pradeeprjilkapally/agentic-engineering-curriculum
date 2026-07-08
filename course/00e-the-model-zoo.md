# Lesson 1.5 · The model zoo

**Where this gets you:** you'll be able to look at any task in a customer system and route it to the right model tier with one line of reasoning.

## The idea

Three tiers are worth knowing.

**1. Closed frontier.** Claude (Opus/Sonnet/Haiku), GPT-class models, Gemini. Highest capability, least engineering effort. You pay in API spend, vendor lock at the call site, and a privacy boundary you have to negotiate with the customer's compliance team.

**2. Open weights.** Llama, Qwen, Gemma, DeepSeek, Nemotron, Moondream, Parakeet. You host them. Capability per parameter is usually lower than the frontier, so you trade dollars for engineering work. What you get back: privacy stays on your machine, the model never changes underneath you, and per-query cost approaches zero at scale.

**3. Specialty.** Voice models (Parakeet, Voxtral). Video models (LTX, Sora-class). Embedding models (OpenAI ada, Voyage, Cohere). Don't reach for a generalist when a specialty model is 10x better at the one task you need.

Now the decision. Look at any task in a customer system and answer: which tier?

- **Sensitive data → local.** Customer NPII, regulated industry, contracts that say data doesn't leave their environment.
- **Predictable, high-volume workload → fine-tune local.** Classification, extraction, routing. The boring repetitive work. A small local model trained on your customer's distribution beats a frontier model in cost, latency, and often accuracy.
- **Hard reasoning → frontier.** Code generation, novel synthesis, anything where a 1% capability gap shows up in the output.
- **Latency-critical → local plus cache.** Sub-second targets, voice, gaming — anything where the round trip to a frontier API is too slow.
- **Cost-critical at scale → hybrid.** Frontier for the hard cases, local for the rest. Route on confidence: if the small model is sure, ship its answer; if not, escalate.

**What this looks like on a real system.** An insurer wants claim documents read. One pipeline, three calls. First, sort each file into one of nine claim types — millions of documents, a fixed set of labels, and a fine-tuned small open-weight model does it locally for pennies. Second, pull the fields out of the ones the classifier flagged as unusual — still local, still cheap. Third, the handful that don't fit anything: draft an adjuster note explaining why. That one goes to the frontier, because it's the only step where reasoning quality changes the answer. Route the whole pipeline to the frontier and you blow the budget on the classifier. Route it all local and you ship bad adjuster notes.

One licensing note. Open-weight licensing is finally getting standardized. OpenMDW (Open Model + Data + Weights), endorsed by NVIDIA for Nemotron releases in 2026, is the first credible attempt at an open-source license written for AI artifacts. When you see OpenMDW on a model card, that's a strong signal of genuine portability and redistributable weights. Watch for it.

## Training and adapting small models

You won't pretrain a model from scratch. Nobody on a customer engagement does. But adapting a small open-weight model to a customer's work is one of the highest-leverage moves you have. Four levers, in the order you should reach for them.

**1. Prompt and context first.** Try a better prompt and better retrieval before you train anything. Most "we need to fine-tune" requests are really "we put the wrong stuff in context" requests (Lesson 1.2). Training is what you do when prompting plateaus, not before.

**2. Fine-tuning (LoRA / QLoRA).** Take an open model (Llama, Qwen, Gemma) and train a small adapter on a few hundred to a few thousand examples of the customer's task. **LoRA** trains a tiny set of extra weights instead of the whole model, so it's cheap, fast, and runs on one GPU. QLoRA quantizes the base model to fit in even less memory. This is the workhorse: when a customer has labeled examples of their task, a fine-tuned 8B model often beats a frontier API on cost, latency, and accuracy for that task. Tooling worth knowing: Hugging Face PEFT, Axolotl, Unsloth.

**3. Distillation.** Use a frontier model as a teacher to generate training data, then train a small student model to reproduce it. The student gets most of the teacher's quality on a narrow task for a fraction of the cost. Two flavors: classic output distillation, where you train the small model on the big model's answers, and the Pi pattern, where the frontier model writes the procedures (skills) and the small local model executes them. The Pi pattern is often the better deal, because the knowledge stays in inspectable markdown instead of baked into weights you can't read. See [Tom Tunguz on the Pi agent and skill distillation](https://tomtunguz.com/the-pi-agent-skill-distillation/).

**4. Embeddings, separately.** Retrieval (RAG) runs on embedding models, not chat models. They're small, cheap, and you rarely train them. Pick a good open one (BGE, Nomic, Voyage) or a hosted one, and spend your training budget on the task model instead.

The FDE judgment call: training is a commitment. A fine-tuned model is one you now own, host, version, and re-train when the data drifts. That's real ongoing work. Reach for it when the task is high-volume, stable, and private enough that a frontier API doesn't fit (Lesson 6.10). For everything else, prompt and route. When you do train, the cheapest path is almost always a LoRA adapter on a small open model, held to the same eval suite you'd use for anything else (Lesson 4.2).

## Your exercise

For your project candidate, list every place you call (or will call) a model. For each one, assign it to a tier (frontier / open-weights / specialty) and write one line on why.

**You're done when** you have a routing table. Even if every cell says "frontier today," you know what would move it.

**Practice proof:** save the table in `NOTES.md` under "model routing."

**Build on it:** build a two-tier router that answers confident requests with a local model, escalates the rest to a frontier API, and logs which tier handled what.

## Why this matters

**Model routing** is half your cost, half your latency, and all of your privacy story. Get it right and the project ships to enterprise. Get it wrong and you ship a budget overrun, or a privacy review you can't pass. The customers paying for FDE work care more about routing than about which frontier model is smartest this week.

---

You've finished Part 1. The foundations are in. Now you put your hands on the workflow.

Next: [Lesson 2.1 · What is agentic engineering?](01-what-is-agentic-engineering.html)
