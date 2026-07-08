# Lesson 1.2 · LLMs: just enough to be dangerous

**Where this gets you:** you'll be able to route model decisions on instinct. Frontier API or local. Temperature 0 or 0.8. No transformer paper required.

## The idea

You don't need to train a model to be a great Forward Deployed Engineer. You need five things, known well enough to use on autopilot.

**1. Autoregressive next-token prediction is the whole spine.**
The model has read a lot of text. Given the tokens so far, it predicts the next one. Repeat. Chat, agents, tool calling — all of it is engineering wrapped around that one loop. It's not more mysterious than that.

**2. The context window is your real budget.**
Every token you put in costs money and latency. The model can attend to all of it, but position matters: tokens at the start and end usually carry more weight than tokens buried in the middle. The art is putting the right context in and leaving the wrong context out.

**A real one.** A support bot keeps quoting last year's refund policy. Everyone blames the model. But the prompt is stuffing forty pages of handbook in, and the current policy sits on page 22 — dead center, where attention is thinnest. Nobody touched the model. They cut the prompt to the three paragraphs that mattered and it answered right every time. Most "AI doesn't work" problems are "wrong stuff in context" problems.

**3. Temperature and top-p control creativity.**
Temperature 0 means the model picks the highest-probability next token almost every time. Deterministic, tight. 0.7 means some variety. 1.0 and above means creative, sometimes wrong. Use 0 for code generation, fact extraction, structured output — anything where you want the same answer twice. Use 0.5 to 0.8 for writing, brainstorming, conversation.

**4. Open weights vs closed weights is a real decision, not a religious one.**
Closed (Claude, GPT, Gemini) gives you frontier capability for the least engineering effort, at the cost of API spend, vendor lock, and a privacy boundary at every call. Open (Llama, Qwen, Gemma, DeepSeek, Nemotron) means you host it. You trade dollars for engineering work, but the privacy stays on your machine and the model never changes underneath you. Most production systems run a mix.

**5. Small local models are quietly winning the boring work.**
A 4B to 9B model on a recent GPU answers in under a second. For predictable workloads — classification, routing, extraction, "is this signal or noise" — small and local is often the right answer. Lesson 1.5 goes deeper.

## Your exercise

Pick any prompt. Summarize an article, write a function, draft an email. Run it through the same model at temperature 0, then at 0.8. Read both outputs side by side.

**You're done when** you can name one place in a production system where the temperature-0 output would be correct and the temperature-0.8 output would introduce a bug.

**Practice proof:** save both outputs to `NOTES.md` under "temperature comparison."

**Build on it:** build a CLI that runs the same summarization prompt five times at a given temperature and prints how many outputs are byte-identical.

## Why this matters

Half of agentic engineering is picking the right model and the right settings for the task. The other half is the harness around it. You can't do the second half well without the first half on autopilot. Once these five become reflexes, you'll route work in your head before you ever open a config file.

---

Next: [Lesson 1.3 · What makes an agent](00c-what-makes-an-agent.html)
