# Lesson 0.1 · The AI map: four layers on one page

**Where this gets you:** you'll be able to put the right layer name on any AI conversation you walk into, so you stop arguing about the wrong thing.

## The idea

Almost every confusing conversation in AI right now is one layer mistaken for another. Pin down the four layers and most of the noise drops away.

Top down:

1. **Application.** What the user sees. A chatbot. A search box that uses RAG. An agentic app that goes off and does things on the user's behalf. This is where most product talk lives.
2. **Harness.** The layer that wraps memory, skills, tools, and an agent runtime around the model. Examples: Claude Code, ChatGPT, Cursor, Codex CLI. The harness is where switching cost lives. Lesson 17 goes deep here.
3. **Agent.** The loop. Perceive, plan, act, observe, decide whether to continue. With memory across iterations and a stop condition. Lesson 0.3 goes deep.
4. **Model.** The LLM or multimodal model. Claude, GPT, Gemini, Gemma, Qwen, DeepSeek. Lesson 0.2 and Lesson 0.5 go here.

Now, why does it matter to keep them separate? Here's where the real value shows up. When someone says "Claude is better than GPT," they mean the model layer. When they say "Cursor is better than Claude Code," they mean the harness. When they say "your agent needs better memory," they mean the agent and harness together. The conversation goes nowhere if everyone's pointing at different layers and using the same words.

A common one you'll hear from customers: "we need a better LLM." Nine times out of ten the LLM is fine. What they need is a better harness. Better memory, better tools, better evals. Naming the layer saves a quarter of arguing.

## Your first exercise

Pick a product you use every day. ChatGPT, Cursor, Notion AI, GitHub Copilot, something you built. Write one sentence at each of the four layers, naming the choice that product made at that layer.

**You're done when** you have four sentences and they don't blur into each other. Each one is about a different thing.

**Practice proof:** save it in `NOTES.md` under "AI map." You'll reuse this exact frame in Lesson 17.

## Why this matters

Every confusing conversation you'll have for the next year as an FDE will dissolve the moment you put the right layer on it. This is the first tool you'll reach for in customer meetings, on Twitter, in your own debugging. Get the layer right and the rest of the conversation becomes easy.

---

Next: [Lesson 0.2 · LLMs. Just enough to be dangerous](00b-llms-just-enough.html)
