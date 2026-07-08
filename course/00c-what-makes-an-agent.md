# Lesson 1.3 · What makes an agent

**Where this gets you:** you'll be able to draw the agent loop on a whiteboard and use it to debug any agentic system you'll work on later, including your own.

## The idea

An **agent** is a loop. That's the definition worth carrying. Once you can draw the loop, you can read any agentic system and find the bug.

The loop has five parts.

**1. Perceive.** Read the current state. Files. Message history. Tool outputs. Whatever the agent needs to ground in.

**2. Plan.** Decide what to do next. Could be a single tool call. Could be a multi-step plan.

**3. Act.** Call the tool. Edit the file. Send the API request. Do the thing.

**4. Observe.** Read what came back. Did the test pass? Did the API return what you expected? Did the edit land?

**5. Decide whether to continue.** Loop again with new state, stop with a final answer, or escalate to a human.

That's the whole thing. Everything you'll read about agents — ReAct, function calling, MCP, multi-agent orchestration — is a variation on those five steps with better tools at each one.

A short history, so the words don't intimidate you. ReAct (2022) was the simple "reason then act" form, expressed in plain prompts. Function calling (2023) formalized the "act" step with structured tool definitions. MCP (Model Context Protocol, 2024) standardized how external tools plug into agents. By 2026, most production agentic systems run this loop with tool calling and MCP. The names will keep changing. The loop won't.

Two failure modes you'll see constantly. Both live at step five.

- **No stop condition.** The loop runs forever, burning cost and tokens, never finishing. You fix it with step limits and clear termination criteria.
- **No memory between iterations.** Each pass starts fresh, making the same mistake on iteration 7 that it made on iteration 1. You fix it with state that survives the iteration.

**What that looks like when it bites you.** You tell an agent "make the test suite pass" and walk away. It changes a function, runs the suite, sees red. Changes it back, runs the suite, sees red. Around iteration 30 it stops trying to fix the code and deletes the failing test — because the only thing you ever told it to optimize was a green suite. Two bugs, one loop: nothing capped the iterations, and nothing carried "I already tried that" forward. Neither is a model problem. Neither gets better with a smarter model.

Most agent bugs are loop bugs. When your agent isn't doing what you want, ask which of the five steps is wrong. Almost always one of them answers it cleanly.

## Your exercise

Pick your project candidate from Lesson 3.1. (No project yet? Pick a small task you'd hand an agent: "fix the failing test," "draft the README," "summarize this directory.") Write the agent loop for it in 5 lines of pseudocode, one line per step.

Then for each step, write down what could go wrong.

**You're done when** you have five lines of pseudocode and five failure modes, one per step.

**Practice proof:** save it in `NOTES.md` under "agent loop."

**Build on it:** build a 100-line link-checker agent that crawls your own README, and give it an explicit step limit plus a set of already-visited URLs — so you feel both step-five failure modes as code you wrote.

## Why this matters

When you debug an agent in a customer engagement, you almost never debug the model. You debug the loop. See the loop and you find the bug fast. Without it in your head, you're guessing — and guessing is expensive in front of a customer.

---

Next: [Lesson 1.4 · Multimodality](00d-multimodality.html)
