# Lesson 6.2 · The application taxonomy

**Where this gets you:** you'll be able to classify any AI product in the wild onto a three-layer progression in 30 seconds, and you'll know what the next layer of work would look like for any customer engagement.

## The idea

RAG, chatbots, and agentic apps are not three different styles of building. They are a progression. Each layer is a superset of the one before. Knowing where a project sits on the progression tells you what to build next and where the wedge is.

**Layer 1: RAG.** Retrieve documents from a corpus, augment the prompt with the retrieved chunks, generate an answer. Single-shot. No memory of last turn. Examples: internal knowledge Q&A, support search, semantic doc lookup. Most "AI search" products in market are still here.

**Layer 2: Chatbot.** Add conversational memory within a session. The model remembers what you said three turns ago. Usually no memory across sessions. Examples: ChatGPT (consumer mode), support bots, conversational research assistants. The retrieval from Layer 1 is still in there; the session memory is what's new.

**Layer 3: Agentic app.** Add tools and the agent loop. The model doesn't just answer; it acts. It reads files, writes files, calls APIs, makes decisions, persists state across sessions through a brain. Examples: Claude Code, Cursor, and most of what serious customer engagements will be heading toward in 2026 and beyond.

Each layer requires the one before it. You can't skip RAG and go straight to agentic; the retrieval will be flaky. You can't skip chatbot-grade session memory and have a usable agent; users will get frustrated re-explaining context.

Here's the part that matters for FDE work in 2026.

Most enterprise customers have a RAG. They are calling it "our AI" or "our chatbot," and they want it to do more. The wedge for a Forward Deployed Engineer is moving them up the stack without breaking the unit economics they already understand.

The work at each transition:

- **RAG to chatbot.** Add session memory. Build a conversational UI on top of the existing retrieval. Write evals for multi-turn coherence. Almost always a 4-8 week engagement.
- **Chatbot to agentic.** Add tools (MCP servers or direct API integrations). Add a persistent brain that lives across sessions. Add evals for tool use, not just answer quality. Add guardrails for cost and safety. Usually a 3-6 month engagement, sometimes a year.

When a customer asks "can we do agents," they almost always have a RAG. Knowing the gap between where they are and where they want to be is your scoping move.

## Your exercise

Classify your project candidate onto the three layers. Then write two short paragraphs: what the next-layer version of it looks like, and what the work to get there would actually be.

**You're done when** you can classify any AI product you see in the wild onto this taxonomy in under 30 seconds.

**Practice proof:** save your classification and the next-layer write-up in `NOTES.md` under "application taxonomy."

## Why this matters

Customers don't usually know what layer they're on. The scoping conversation is hard because they're describing what they want using the words of a layer they're not yet at. Your value as an FDE starts with naming the layers cleanly, then drawing the bridge from where they are to where they want to be, with realistic costs and timelines for each segment of the bridge.

---

Next: [Lesson 6.3 · Coordinating with agents and humans](19-coordinating-team.html)
