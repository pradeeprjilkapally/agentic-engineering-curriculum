# Lesson 7.3 · Tool protocols: MCP and connectors

**Where this gets you:** you'll understand what the Model Context Protocol is and why it exists, be able to connect an agent to a real tool or data source via MCP, and know how the major platforms handle tool connectivity so you can speak to this in any customer conversation.

## The idea

Every agent needs to reach outside itself: query a database, call an internal API, read a file, post to Slack, look something up in a CRM. The naive approach is to write each integration by hand -- a Python function per tool, hardcoded into the agent. That works for one agent with three tools. It falls apart at ten agents with thirty tools, because every agent reimplements the same integrations, and every integration change requires touching every agent that uses it.

The Model Context Protocol (MCP) is the open standard that solves this. Anthropic published the spec and open-sourced it in late 2024. OpenAI adopted it in early 2025. Google and others followed. It is now the closest thing to a universal tool connector in the agentic ecosystem.

**What MCP actually is.** MCP defines a protocol between two processes: a client (the agent or the host that runs the agent) and a server (the process that exposes tools, data, or prompts). The client discovers what tools the server has, calls them over a standard JSON-RPC wire format, and gets results back. The server can run locally (a subprocess) or remotely (an HTTP endpoint). The agent doesn't know or care how the tool is implemented -- it just calls it by name with the declared parameters.

Think of it as a USB standard for agent tools. Before USB, every peripheral needed its own driver and connector. After USB, you plug in any device and it works. MCP is that for model tools.

**The three things an MCP server can expose:**

- **Tools** -- functions the model can call (equivalent to function calling in the raw API, but decoupled from the agent code).
- **Resources** -- files, database rows, or documents the model can read (surfaced as contextual data rather than function calls).
- **Prompts** -- reusable prompt templates the model can invoke by name.

Most practical MCP servers expose tools. Resources are useful for document-heavy workflows.

**Building a minimal MCP server.** The `mcp` Python SDK (from Anthropic) is the reference implementation. A server is a small Python file:

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("invoice-tools")

@mcp.tool()
def lookup_invoice(invoice_id: str) -> dict:
    """Return status and amount for the given invoice ID."""
    # your real implementation here
    return {"invoice_id": invoice_id, "status": "paid", "amount": 1200.00}

if __name__ == "__main__":
    mcp.run()
```

That's the whole server. `FastMCP` handles the protocol, the capability negotiation, and the JSON-RPC transport. Your job is to write the tool functions.

To connect Claude Code to this server, add it to your `.claude/settings.json`:

```json
{
  "mcpServers": {
    "invoice-tools": {
      "command": "python",
      "args": ["path/to/invoice_server.py"]
    }
  }
}
```

Now any Claude Code session in that project has `lookup_invoice` available as a tool, without touching the agent code.

**Using MCP from a programmatic agent.** In Python code, the Anthropic SDK lets you call MCP servers directly:

```python
# abbreviated -- check current anthropic docs for the exact async client usage
async with client.beta.messages.with_mcp_server(...) as session:
    # tools from the MCP server are automatically available in messages.create
    ...
```

The OpenAI Agents SDK has native MCP support too:

```python
from agents.mcp import MCPServer, MCPServerStdio

server = MCPServerStdio(params={"command": "python", "args": ["invoice_server.py"]})
agent = Agent(name="BillingAgent", mcp_servers=[server], ...)
```

The pattern is the same: declare the server, and the SDK handles discovery and routing.

**How the platforms handle this.**

| Platform | MCP support | Notes |
|---|---|---|
| Claude Code / Anthropic SDK | Native, first-class | Originated the spec; `mcp` SDK is the reference implementation |
| OpenAI Agents SDK | Adopted MCP in 2025 | `MCPServer` class, works with any MCP-compliant server |
| Gemini / Google ADK | MCP-compatible tooling via Extensions | Check current ADK docs; the ecosystem is moving fast |
| Snowflake Cortex | External functions + partner connectors | No native MCP client at the time of writing; tools are wired as SQL external functions or Python UDFs |

For Snowflake, the practical approach is: build an MCP server that wraps your tools, then call it from a Python layer that also calls Cortex. The Cortex SQL layer stays clean; the MCP server handles the integrations.

**Why a protocol beats bespoke integrations.** Before MCP, an FDE building an agent for a customer would write tool integrations inline: a Slack function, a Salesforce function, a custom DB function, all hardcoded. If the customer wanted a second agent, they'd copy and paste. If a tool changed its API, they'd patch every agent.

With MCP, the tools live in servers. Agents are clients. You build the Salesforce MCP server once, and every agent in the organization can use it. When Salesforce changes their API, you patch one server. You can also compose: an agent that needs both Slack and Salesforce just connects to both servers, no new code required.

The ecosystem of pre-built MCP servers is growing quickly (Anthropic's MCP server directory, and community registries). Before writing a custom integration, check if an MCP server already exists for that tool.

**Sharp edges.** MCP servers are processes. They can crash, time out, or return malformed responses. Your agent should handle `tool_result` errors gracefully -- log them, retry if appropriate, and surface a useful error message rather than silently failing. Also: secrets. MCP servers that connect to external services need credentials; don't hardcode them in the server file. Use environment variables, and document the required env vars clearly.

## Your exercise

Connect your agent to one real tool or data source via MCP. Options in increasing order of effort:

1. **Use an existing MCP server.** Find an MCP server that's already written for a tool you need (GitHub, Slack, a database), add it to your Claude Code config, and demonstrate it working in a session.
2. **Build a minimal MCP server.** Write a `FastMCP` server with one or two tools that your project actually needs (a DB lookup, a file reader, a metrics query). Connect it to Claude Code and run a real task through it.
3. **Wire it to a programmatic agent.** Take the agent from Lesson 7.2 and replace one inline tool function with an MCP server call.

**You're done when** an agent in your project calls at least one tool through an MCP server and returns a real result.

**Practice proof:** save a screenshot or terminal output of the tool call in action in `NOTES.md` under "MCP integration," and note which server you used or built.

## Why this matters

MCP changes the scoping conversation with enterprise customers. Instead of "we'll build a custom integration for each system," the answer becomes "we'll build MCP servers for each system and all your agents share them." That is a fundamentally different project shape -- one that scales and one that doesn't.

Customers who already have an Anthropic deployment will be running MCP. OpenAI customers are increasingly running it too. Knowing how to build, debug, and connect MCP servers is becoming a baseline skill for agentic engineering work in 2026, not a specialization.

And the protocol being open means the investment is durable. A Salesforce MCP server you build for a Claude deployment today works with OpenAI and Gemini tomorrow. That's the right story to tell in any multi-vendor enterprise environment.

---

Previous: [Lesson 7.2 · Programmatic agents (the SDKs)](29-programmatic-agents-sdks.html)
