# Lesson 0.2 · LLMs: just enough to be dangerous

**Where this gets you:** you'll be able to make routing decisions about models. When to use a frontier API, when to run something locally, when to crank temperature, when to keep it at zero. Without needing to read another transformer paper.

## The idea

You don't need to train a model to be a great Forward Deployed Engineer. You need to know five things well enough to use them on autopilot.

**1. Autoregressive next-token prediction is the whole spine.**
The model has read a lot of text. Given the tokens so far, it predicts the next one. Repeat. Everything else. Chat, agents, tool calling. Is engineering around this single loop. That's it. Don't let anyone tell you it's more mysterious than that.

**2. The context window is your real budget.**
Every token you put in costs money and latency. The model can attend to all of it, but recency wins; tokens at the end of the prompt usually carry more weight than tokens at the start. The art is putting the right context in and leaving the wrong context out. Most "AI doesn't work" problems are actually "wrong stuff in context" problems.

**3. Temperature and top-p control creativity.**
Temperature 0 means the model picks the highest-probability next token almost every time. Outputs are deterministic and tight. Temperature 0.7 means some variety. Temperature 1.0 and above means creative. And sometimes wrong. Use 0 for code generation, fact extraction, structured output, anything where you want the same answer twice. Use 0.5 to 0.8 for writing, brainstorming, conversation.

**4. Open weights vs closed weights is a real decision, not a religious one.**
Closed (Claude, GPT, Gemini) gives you the frontier capability with the least engineering effort, at the cost of API spend, vendor lock, and a privacy boundary at every API call. Open (Llama, Qwen, Gemma, DeepSeek, Nemotron) means you host it; you trade dollars for engineering work, but the privacy stays on your machine and the model never changes underneath you. Most production systems will run a mix.

**5. Small local models on real hardware are quietly winning for boring work.**
A 4B to 9B model on a recent GPU runs at sub-second per query. For predictable workloads. Classification, routing, extraction, "is this signal or noise". Small local models are often the right answer. Lesson 0.5 goes deeper.

## Your first exercise

Pick any prompt. Summarize an article, write a function, draft an email. Run it through the same model at temperature 0 and then at temperature 0.8. Read both outputs side by side.

**You're done when** you can name one place in a production system where the temperature-0 output would be correct and the temperature-0.8 output would introduce a bug.

**Practice proof:** save both outputs to `NOTES.md` under "temperature comparison."

## Why this matters

Half of agentic engineering is just picking the right model and the right settings for the task at hand. The other half is the harness around it. You can't do the second half well without the first half on autopilot. Once these five become reflexes, you'll route work in your head before you ever open a config file.

---

Next: [Lesson 0.3 · What makes an agent](00c-what-makes-an-agent.html)
