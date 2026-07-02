# Lesson 7.2 · Programmatic agents (the SDKs)

**Where this gets you:** you'll know when to stop using a CLI and write an agent in code instead, and you'll be able to sketch the minimal loop using the Claude Agent SDK, OpenAI Agents SDK, or the equivalent pattern on Gemini.

## The idea

Claude Code is a development tool. It is not a product. The moment you want an agent running in a cron job, inside an API endpoint, embedded in a mobile backend, or making decisions while users are sleeping -- you need code, not a CLI session.

The shift is smaller than it sounds. An agent is a loop: call the model, check if it wants to use a tool, run the tool, send the result back, repeat until done. The CLI tools run this loop interactively. The SDKs let you run it headlessly, with your own control over every step.

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

That is the whole loop. Every agent SDK is opinionated scaffolding around this pattern. They add: tool registration, streaming, error handling, tracing, memory hooks, and guardrails. You could write the loop yourself against the raw API (Lesson 7.1); the SDK saves you from rewriting the same 80 lines across every project.

**The Claude Agent SDK.** Anthropic's SDK (`anthropic` Python package) gives you the raw API primitives. For the higher-level agent loop, the relevant class is `client.beta.messages.stream` combined with tool-use handling. As of 2025-2026, Anthropic's recommended pattern is to manage the loop explicitly (it's a few dozen lines), or use the Model Context Protocol (MCP) to wire tools as external servers rather than inline functions (see Lesson 7.3). Check the current Anthropic docs for `tool_use` and streaming -- the specifics evolve quickly.

```python
import anthropic

client = anthropic.Anthropic()

def run_agent(task: str, tools: list, tool_runner: callable) -> str:
    messages = [{"role": "user", "content": task}]
    while True:
        response = client.messages.create(
            model="claude-opus-4-5",
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

**The OpenAI Agents SDK.** OpenAI's `openai-agents` package wraps this loop with decorator-style tool registration and a `Runner` that handles the loop, streaming, and handoffs between agents.

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

The SDK handles retries, tracing (to the OpenAI dashboard if you opt in), and multi-agent handoffs. It is more opinionated than the Anthropic approach -- which makes it faster to get started, and less flexible when you need to control the loop.

**Gemini's approach.** Google's `google-adk` (Agent Development Kit) follows a similar pattern: you define tools as Python functions with docstrings, register them with an `Agent`, and call `agent.run(query)`. As of mid-2025 the ADK is in active development; check the current `google-adk` docs before wiring production code. The conceptual loop is identical to the above.

**Snowflake Cortex.** For teams already inside Snowflake, Cortex Analyst and Cortex Search let you build agents as stored procedures or external functions that call `SNOWFLAKE.CORTEX.COMPLETE` in a loop. The agent loop is SQL + Python glue rather than a dedicated SDK. For anything beyond simple multi-turn SQL agents, most teams reach for a Python SDK and call Cortex from there.

**When is the CLI enough?**

The CLI is the right tool when: you're developing and iterating, the task is interactive (you want to see intermediate steps), the user is a developer who has the CLI installed, and the agent runs once per human request in a terminal.

Move to an SDK when: the agent needs to run without a human in the loop, you're embedding it in a product (API, scheduler, CI pipeline), you need custom retry/fallback logic, you want structured tracing and logs, or you need to run thousands of calls per day with cost controls.

**Memory and guardrails.** Two things the loop alone doesn't give you.

Memory is anything that persists across agent runs: a database row, a file, a vector store. The SDKs do not manage long-term memory for you. You wire it: read from storage at the start of the loop, write back at the end. This is the right abstraction -- the agent doesn't decide where facts live, you do.

Guardrails are checks that run alongside the model call: input filters (block certain topics before they reach the model), output filters (catch policy violations before the response goes to the user), and cost caps (abort if token count or call count exceeds a threshold). Add these as wrappers around your loop, not as afterthoughts. Retrofitting guardrails into a running production system is painful.

## Your exercise

Pick one repeated task in your project that runs without a human typing in a terminal: a nightly report, a webhook handler, a batch classifier, a monitoring job. Sketch or build a minimal programmatic agent for it.

"Sketch" is acceptable if you're not yet at the code stage: write the tool list (name + what it does), the system prompt, and the loop logic in pseudocode. But if you have a working API call from Lesson 7.1, extend it into a full loop.

**You're done when** you have either running code that completes the loop at least once, or a documented sketch detailed enough that a second engineer could implement it in an afternoon.

**Practice proof:** save the code or sketch in `NOTES.md` under "programmatic agent," and note which SDK you chose and why (or why you chose not to use one yet).

## Why this matters

The gap between "demo" and "product" is almost always the gap between "running in a CLI session" and "running in code, headlessly, at scale." Every serious customer engagement will eventually need the latter. Knowing how to write the loop and wire it into a real system is the skill that separates an FDE who can prototype from one who can ship.

The SDKs also expose the seams that the CLI hides. When you own the loop, you see where errors actually happen, which tool calls are slow, and where costs spike. That visibility is what you need to tune a production agent -- not a black-box CLI session.

Finally, multi-agent coordination (one agent delegating to another) is only possible in code. The CLI runs one agent. Product-grade systems chain many.

---

Previous: [Lesson 7.1 · Building on the API](28-building-on-the-api.html) · Next: [Lesson 7.3 · Tool protocols: MCP and connectors](30-tool-protocols-mcp.html)
