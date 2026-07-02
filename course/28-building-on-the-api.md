# Lesson 7.1 · Building on the API

**Where this gets you:** you'll be able to call any major model API directly from code, wire tool use (function calling), handle streaming output, and make sensible decisions about tokens and cost -- all without a CLI in the loop.

## The idea

The CLI tools (Claude Code, Codex CLI, Gemini CLI) are great for development. At some point you need to embed a model call inside a product: a backend route, a batch job, a serverless function. That's when you talk to the API directly.

Every major provider wraps the same conceptual shape: you send a list of messages, the model responds. The differences are in naming, auth headers, and a few structural details. Once you know one, the others take an afternoon.

**The message array.** Every API call is a list of turns. Each turn has a role (`user`, `assistant`, and often `system`) and content. Anthropic calls this endpoint `POST /v1/messages`. OpenAI calls it `POST /v1/chat/completions` (older) or the newer `POST /v1/responses`. Gemini calls it `generateContent`. Snowflake Cortex exposes it as the SQL function `SNOWFLAKE.CORTEX.COMPLETE`. Same idea everywhere.

```python
# Anthropic
import anthropic
client = anthropic.Anthropic()
response = client.messages.create(
    model="claude-opus-4-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Summarize this contract: ..."}]
)
print(response.content[0].text)

# OpenAI
from openai import OpenAI
client = OpenAI()
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Summarize this contract: ..."}]
)
print(response.choices[0].message.content)

# Gemini
import google.generativeai as genai
model = genai.GenerativeModel("gemini-2.0-flash")
response = model.generate_content("Summarize this contract: ...")
print(response.text)

# Snowflake Cortex (SQL, inside a Snowflake session)
-- SELECT SNOWFLAKE.CORTEX.COMPLETE('mistral-large', 'Summarize this contract: ...')
```

**Streaming.** For anything the user watches in real time, request a stream. Without streaming, the whole response buffers server-side and arrives at once -- which feels slow for long outputs. Streaming is one parameter change on every platform (`stream=True` for OpenAI, `stream=True` for Anthropic; Gemini uses `generate_content_async` with `stream=True`). The trade-off: you lose easy access to total token counts until the stream closes, so log the final usage chunk.

**Structured output and JSON mode.** If you're extracting data (entities, classification labels, structured reports), asking the model to "respond in JSON" in the prompt is not enough. Use the platform's structured-output guarantee instead.

- Anthropic: pass a `tool` definition with a JSON schema and tell the model to call it. The response will be a tool-use block with the parsed object.
- OpenAI: `response_format={"type": "json_schema", "json_schema": {...}}` on the Chat Completions API, or use the Structured Outputs feature on the Responses API.
- Gemini: `response_mime_type="application/json"` plus a `response_schema`.
- Snowflake Cortex: extract with `TRY_PARSE_JSON()` on the response string; no native schema enforcement as of mid-2025, so you validate downstream.

Structured output matters because JSON-mode-without-a-schema still lets the model hallucinate field names. A schema catches that at the protocol level.

**Tool use (function calling).** This is how agents get real work done at the API layer. You declare one or more tools -- each is a name, description, and a JSON schema for its parameters. The model decides when to call one, returns a `tool_use` block instead of a text answer, you execute the function in your code, and you send the result back as a `tool_result` message. Repeat until the model returns a plain text response.

```python
# Anthropic -- abbreviated
tools = [{
    "name": "lookup_invoice",
    "description": "Return invoice data for a given invoice_id.",
    "input_schema": {
        "type": "object",
        "properties": {"invoice_id": {"type": "string"}},
        "required": ["invoice_id"]
    }
}]
response = client.messages.create(
    model="claude-opus-4-5", max_tokens=1024,
    tools=tools,
    messages=[{"role": "user", "content": "What's the status of invoice INV-9912?"}]
)
# If response.stop_reason == "tool_use", pull the tool_use block, run your function, loop.
```

OpenAI's shape is nearly identical: `tools=[{"type": "function", "function": {...}}]` and `finish_reason == "tool_calls"`. Gemini uses `tools=[genai.protos.Tool(...)]` and checks `response.candidates[0].finish_reason`.

**Tokens and cost.** Token counts drive your costs. The API returns input and output token counts in every response; log them. A few rules that hold across platforms:

- System prompts cost tokens every call. Keep them tight, or use prompt caching (Anthropic and OpenAI both have it; check current docs for the exact parameter).
- Output tokens are usually 3-5x the cost of input tokens. If you're summarizing a long doc, compress the input rather than letting the model output a long summary.
- Set `max_tokens` explicitly. An uncapped call can return a very long response, very expensively.

**Error handling and retries.** APIs rate-limit, go over capacity, and time out. Every production caller needs at minimum: exponential backoff on `429` (rate limit) and `529`/`503` (overloaded), a circuit breaker if you're hitting the API in a tight loop, and a timeout. Anthropic returns `anthropic.RateLimitError`; OpenAI returns `openai.RateLimitError`; Gemini throws `google.api_core.exceptions.ResourceExhausted`. Use `tenacity` or a similar retry library so you don't reinvent this.

The mistake most teams make is shipping API calls without retries in the first version, because "it works in testing." It will fail in production under real load.

## Your exercise

Pick one real capability your project needs (summarization, extraction, classification, or a look-up that requires tool use). Write a Python script that calls the model API directly -- no CLI wrapper -- with at least one tool defined. If your project is read-only or not yet code-heavy, write the script against a toy dataset.

Your script should: build the message array explicitly, handle the tool-use loop (send result back, get final response), print the token counts from the response, and have at least one retry on `429`.

**You're done when** the script runs end-to-end and prints the tool result plus token counts.

**Practice proof:** save the script (or a snippet of it) in `NOTES.md` under "API tool use," and note which platform you used and what the per-call token cost looked like.

## Why this matters

Every agent you build for a customer will eventually need to run without a human-facing CLI. Knowing the raw API means you can embed model calls anywhere: a Lambda function, a Postgres trigger via an external function, a Slack bot handler. You're not dependent on a specific developer tool being installed.

Tool use at the API layer is also where the real reliability work happens. The CLI tools abstract the loop away. When you own the loop in code, you control retries, timeouts, fallbacks, and logging -- which is what a production system actually needs.

And pricing fluency matters in customer conversations. When a customer asks "how much will this cost to run at scale," you need to be able to do the math in the room, not promise to follow up.

---

Next: [Lesson 7.2 · Programmatic agents (the SDKs)](29-programmatic-agents-sdks.html)
