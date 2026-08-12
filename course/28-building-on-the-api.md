---
title: "Lesson 7.1 · Building on the API"
---

# Lesson 7.1 · Building on the API

**Where this gets you:** you'll be able to call any major model API directly from code, wire tool use (function calling), handle streaming output, and make sensible decisions about tokens and cost -- all without a CLI in the loop.

## The idea

The CLI tools (Claude Code, Codex CLI, Gemini CLI) are great while you're building. But eventually the model call has to live inside the product: a backend route, a batch job, a serverless function. No human at a terminal. That's when you talk to the API directly.

Every provider wraps the same shape: you send a list of messages, the model responds. What differs is naming, auth headers, and a few structural details. Learn one and the others take an afternoon.

**The message array.** Every API call is a list of turns. Each turn has a role (`user`, `assistant`, and often `system`) and content. Anthropic calls this endpoint `POST /v1/messages`. OpenAI calls it `POST /v1/chat/completions` (older) or the newer `POST /v1/responses`. Gemini calls it `generateContent` (older) or the newer Interactions API. Snowflake Cortex exposes it as the SQL function `SNOWFLAKE.CORTEX.COMPLETE`. Same idea everywhere.

```python
# Anthropic
import anthropic
client = anthropic.Anthropic()
response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Summarize this contract: ..."}]
)
print(response.content[0].text)

# OpenAI
from openai import OpenAI
client = OpenAI()
response = client.chat.completions.create(
    model="gpt-5.5",
    messages=[{"role": "user", "content": "Summarize this contract: ..."}]
)
print(response.choices[0].message.content)

# Gemini
from google import genai
client = genai.Client()
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Summarize this contract: ..."
)
print(interaction.output_text)

# Snowflake Cortex (SQL, inside a Snowflake session)
-- SELECT SNOWFLAKE.CORTEX.COMPLETE('mistral-large', 'Summarize this contract: ...')
```

**Streaming.** If a user is watching the output appear, request a stream. Without it the whole response buffers server-side and lands at once, which feels slow for long answers. Streaming is one parameter change on every platform (`stream=True` for OpenAI, for Anthropic, and for Gemini's `interactions.create`). The trade-off: you can't read total token counts until the stream closes, so log the final usage chunk.

**Structured output and JSON mode.** If you're extracting data (entities, classification labels, structured reports), asking the model to "respond in JSON" in the prompt is not enough. Use the platform's structured-output guarantee instead.

- Anthropic: pass a `tool` definition with a JSON schema and tell the model to call it. The response will be a tool-use block with the parsed object.
- OpenAI: `response_format={"type": "json_schema", "json_schema": {...}}` on the Chat Completions API, or use the Structured Outputs feature on the Responses API.
- Gemini: `response_mime_type="application/json"` plus a `response_schema`.
- Snowflake Cortex: extract with `TRY_PARSE_JSON()` on the response string; no native schema enforcement at the time of writing, so you validate downstream.

This matters because JSON mode without a schema still lets the model invent field names. A schema catches that at the protocol level.

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
    model="claude-opus-4-8", max_tokens=1024,
    tools=tools,
    messages=[{"role": "user", "content": "What's the status of invoice INV-9912?"}]
)
# If response.stop_reason == "tool_use", pull the tool_use block, run your function, loop.
```

OpenAI's shape is nearly identical: `tools=[{"type": "function", "function": {...}}]` and `finish_reason == "tool_calls"`. Gemini passes `tools=[...]` to `interactions.create` and returns a `function_call` block in `interaction.outputs` with `interaction.status == "requires_action"`.

**Tokens and cost.** Token counts drive your costs. Every response returns input and output token counts. Log them. Three rules hold across platforms:

- System prompts cost tokens on every call. Keep them tight, or use prompt caching (Anthropic and OpenAI both have it; check current docs for the exact parameter).
- Output tokens are usually 3-5x the cost of input tokens. If you're summarizing a long doc, compress the input rather than letting the model output a long summary.
- Set `max_tokens` explicitly. An uncapped call can return a very long response, very expensively.

**Error handling and retries.** APIs rate-limit, go over capacity, and time out. Every production caller needs, at minimum: exponential backoff on `429` (rate limit) and `529`/`503` (overloaded), a circuit breaker if you're calling in a tight loop, and a timeout. Anthropic returns `anthropic.RateLimitError`; OpenAI returns `openai.RateLimitError`; Gemini raises `google.genai.errors.APIError` (inspect the status code to spot a 429). Use `tenacity` or a similar retry library so you don't reinvent this.

**What "it works in testing" costs you.** Picture a nightly job that classifies the day's support tickets. Ten tickets on your laptop, clean run, ship it. In production it fires 4,000 calls in a burst, the provider starts returning `429`, and the loop has no backoff -- so a third of the tickets get an exception instead of a label. Nothing crashes. The job exits zero, the dashboard shows a smaller-than-usual day, and nobody notices for a week. Six lines of `tenacity` would have made those calls wait and succeed. That's the whole difference between a script and a service.

## Your exercise

Pick one real capability your project needs (summarization, extraction, classification, or a look-up that requires tool use). Write a Python script that calls the model API directly -- no CLI wrapper -- with at least one tool defined. If your project is read-only or not yet code-heavy, write the script against a toy dataset.

Your script should: build the message array explicitly, handle the tool-use loop (send result back, get final response), print the token counts from the response, and have at least one retry on `429`.

**You're done when** the script runs end-to-end and prints the tool result plus token counts.

**Practice proof:** save the script (or a snippet of it) in `NOTES.md` under "API tool use," and note which platform you used and what the per-call token cost looked like.

**Build on it:** wrap the script in a small HTTP endpoint so your project can call it over the network instead of the shell.

## Why this matters

Every agent you build for a customer eventually has to run without a human-facing CLI. Knowing the raw API means you can put a model call anywhere: a Lambda function, a Postgres external-function trigger, a Slack bot handler. Nothing has to be installed on anyone's machine.

Tool use at the API layer is also where the reliability work lives. The CLI tools hide the loop from you. Own the loop in code and you control retries, timeouts, fallbacks, and logging -- which is what a production system actually is.

Pricing fluency matters too. When a customer asks what this costs at scale, you want to do the math in the room, not promise to follow up.

---

Previous: [Lesson 6.11 · The handoff playbook](27-the-handoff-playbook.html) · Next: [Lesson 7.2 · Programmatic agents (the SDKs)](29-programmatic-agents-sdks.html)
