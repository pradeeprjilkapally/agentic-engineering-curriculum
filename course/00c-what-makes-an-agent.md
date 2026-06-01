# Lesson 1.3 · What makes an agent

**Where this gets you:** you'll be able to draw the agent loop on a whiteboard and use it to debug any agentic system you'll work on later, including your own.

## The idea

The simplest useful definition: an agent is a loop. Once you can draw the loop, you can read any agentic system and find the bug. That's the whole game.

The loop has five parts.

**1. Perceive.** Read the current state. Files. Message history. Tool outputs. Whatever the agent needs to ground in.

**2. Plan.** Decide what to do next. Could be a single tool call. Could be a multi-step plan to execute.

**3. Act.** Call the tool. Edit the file. Send the API request. Do the thing.

**4. Observe.** Read what came back. Did the test pass? Did the API return what you expected? Did the file edit land?

**5. Decide whether to continue.** Loop again with new state, or stop with a final answer, or escalate to a human.

That's the whole thing. Everything you'll read about agents (ReAct, function calling, MCP, multi-agent orchestration) is a variation on those five steps with better tools at each step.

A short history, so the words don't intimidate you: ReAct (2022) was the simple "reason then act" form of the loop, expressed in plain prompts. Function calling (2023) formalized the "act" step with structured tool definitions. MCP (Model Context Protocol, 2024) standardized how external tools plug into agents. By 2026, most production agentic systems use this loop with tool calling and MCP. The names will keep changing. The loop won't.

Two failure modes you'll see all the time, both at the "decide whether to continue" step:

- **No stop condition.** The loop runs forever, burning cost and tokens, never finishing. You debug this with step limits and clear termination criteria.
- **No memory between iterations.** Each pass starts fresh, making the same mistake on iteration 7 that it made on iteration 1. You debug this with state that survives the iteration.

The point of seeing the loop clearly is that you can now debug it. Most agent bugs are loop bugs. If your agent isn't doing what you want, ask: which step of the loop is wrong? Almost always one of the five answers it cleanly.

## Your first exercise

Pick your project candidate from Lesson 2.1 (if you don't have one yet, pick a small task you'd give an agent: "fix the failing test," "draft the README," "summarize this directory"). Write the agent loop for it in 5 lines of pseudocode, one line per step.

Then for each step, write down what could go wrong.

**You're done when** you have five lines of pseudocode and five failure modes, one per step.

**Practice proof:** save it in `NOTES.md` under "agent loop."

## Why this matters

When you debug an agent in a customer engagement, you almost never debug the model. You debug the loop. Once you can see the loop, you can find the bug fast. Without it in your head, you're guessing, and guessing is expensive in front of a customer.

---

Next: [Lesson 1.4 · Multimodality](00d-multimodality.html)
