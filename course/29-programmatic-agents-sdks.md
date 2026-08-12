---
title: "Lesson 7.2 · Programmatic agents (the SDKs)"
---

# Lesson 7.2 · Programmatic agents (the SDKs)

**Where this gets you:** you'll know when to stop using a CLI and write an agent in code instead, and you'll be able to sketch the minimal loop using the Claude Agent SDK, OpenAI Agents SDK, or the equivalent pattern on Gemini.

## The idea

Claude Code is a development tool. It isn't a product. The moment you want an agent running in a cron job, inside an API endpoint, or making decisions while users are asleep, you need code, not a CLI session.

**Here's the wall you hit.** You've built a triage agent in Claude Code. It reads a support ticket, checks the billing database, and drafts a reply. It's great. Ops asks for it on every ticket, and there are 400 a day. So someone wires the CLI into a shell script. Then a ticket contains a backtick and the shell eats it. Nothing retries the calls that time out. Nobody can answer "what did it cost yesterday" or "which ticket made it loop nine times," because there are no logs — only a terminal that scrolled away. None of that is a model problem. It's the problem of not owning the loop.

The shift is smaller than it sounds. An **agent** is a loop: call the model, check if it wants a tool, run the tool, send the result back, repeat until done. The CLI runs that loop interactively. The SDKs let you run it headlessly, controlling every step.

**The agent loop, spelled out.**

```
1. Build the initial messages (system prompt + user task)
2. Call the model
3. If the response is "use a tool":
   a. Parse the tool name and arguments
   b. Run the tool in your code
   c. Append the tool result to messages
   d. Go to step 2
4. If the response is a final answer, return it
```

That's the whole loop. Every agent SDK is opinionated scaffolding around it — tool registration, streaming, error handling, tracing, memory hooks, guardrails. You could write it yourself against the raw API (Lesson 7.1). The SDK saves you from rewriting the same 80 lines in every project.

**Anthropic's two surfaces.** These are easy to confuse. The `anthropic` Python package is the API SDK; inside it, `client.beta.messages.tool_runner` drives the tool-call loop for you and is the recommended default. The **Claude Agent SDK** (`claude-agent-sdk`) is a *different* package — Claude Code as a library, with built-in file, bash, and search tools. Both leave hosting to you. You can also wire tools as external servers over the Model Context Protocol instead of registering them inline (see Lesson 7.3).

Write the loop by hand once anyway, as below. Not because you'll ship it — you'll usually reach for the tool runner — but because owning it once is what makes the abstraction legible when it misbehaves.

```python
import anthropic

client = anthropic.Anthropic()

def run_agent(task: str, tools: list, tool_runner: callable) -> str:
    messages = [{"role": "user", "content": task}]
    while True:
        response = client.messages.create(
            model="claude-opus-4-8",
            max_tokens=4096,
            tools=tools,
            messages=messages,
        )
        if response.stop_reason == "end_turn":
            return response.content[0].text
        # Handle tool calls
        tool_results = []
        for block in response.content:
            if block.type == "tool_use":
                result = tool_runner(block.name, block.input)
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": str(result),
                })
        messages.append({"role": "assistant", "content": response.content})
        messages.append({"role": "user", "content": tool_results})
```

**The OpenAI Agents SDK.** OpenAI's `openai-agents` package wraps the loop with decorator-style tool registration and a `Runner` that handles looping, streaming, and handoffs between agents.

```python
from agents import Agent, Runner, function_tool

@function_tool
def lookup_invoice(invoice_id: str) -> str:
    """Return status for the given invoice."""
    return fetch_from_db(invoice_id)  # your code here

agent = Agent(
    name="BillingAgent",
    instructions="You help users understand their invoices.",
    tools=[lookup_invoice],
)

result = Runner.run_sync(agent, "What's the status of INV-9912?")
print(result.final_output)
```

The SDK handles retries, tracing (to the OpenAI dashboard if you opt in), and multi-agent handoffs. It's more opinionated than the Anthropic approach — faster to start with, less flexible when you need to control the loop.

**Gemini's approach.** Google's `google-adk` (Agent Development Kit) follows the same pattern: define tools as Python functions with docstrings, register them with an `Agent`, call `agent.run(query)`. The ADK moves fast, so check the current `google-adk` docs before wiring production code. The loop underneath is identical.

**Snowflake Cortex.** For teams already inside Snowflake, Cortex Analyst and Cortex Search let you build agents as stored procedures or external functions that call `SNOWFLAKE.CORTEX.COMPLETE` in a loop. The loop is SQL plus Python glue rather than a dedicated SDK. Beyond simple multi-turn SQL agents, most teams reach for a Python SDK and call Cortex from there.

**When is the CLI enough?**

Stay on the CLI while you're developing and iterating, when you want to watch the intermediate steps, and when the person running it is a developer typing into a terminal.

Move to an SDK when there's no human in the loop, when you're embedding the agent in a product (API, scheduler, CI pipeline), when you need custom retry and fallback logic, when you want structured tracing, or when you're running thousands of calls a day and someone has to answer for the bill.

**Memory and guardrails.** Two things the loop alone won't give you.

**Memory** is anything that survives between runs: a database row, a file, a vector store. No SDK manages long-term memory for you. You wire it — read from storage at the top of the loop, write back at the end. That's the right split. The agent doesn't decide where facts live. You do.

**Guardrails** run alongside the model call: input filters that block topics before they reach the model, output filters that catch policy violations before the user sees them, and cost caps that abort when tokens or calls cross a threshold. Wrap them around the loop from the start. Retrofitting guardrails into a live system is miserable.

## Your exercise

Pick one repeated task in your project that runs without a human typing in a terminal: a nightly report, a webhook handler, a batch classifier, a monitoring job. Sketch or build a minimal programmatic agent for it.

A sketch is fine if you're not at the code stage yet. Write the tool list (name plus what it does), the system prompt, and the loop in pseudocode. If you have a working API call from Lesson 7.1, extend it into a full loop instead.

**You're done when** you have either running code that completes the loop at least once, or a documented sketch detailed enough that a second engineer could implement it in an afternoon.

**Practice proof:** save the code or sketch in `NOTES.md` under "programmatic agent," and note which SDK you chose and why (or why you chose not to use one yet).

**Build on it:** add a cost cap that aborts the loop after N model calls, then log what each run actually cost.

## Why this matters

The gap between demo and product is almost always the gap between running in a CLI session and running in code, headlessly, at scale. Every serious customer engagement gets there eventually. Writing the loop and wiring it into a real system is what separates an FDE who can prototype from one who can ship.

SDKs also expose the seams the CLI hides. Own the loop and you see where errors happen, which tool calls are slow, where costs spike. That's what you need to tune a production agent. A black-box CLI session gives you none of it.

And multi-agent coordination — one agent delegating to another — only exists in code. The CLI runs one agent. Product-grade systems chain many.

---

Previous: [Lesson 7.1 · Building on the API](28-building-on-the-api.html) · Next: [Lesson 7.3 · Tool protocols: MCP and connectors](30-tool-protocols-mcp.html)
