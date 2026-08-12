---
title: "Lesson 6.1 · The harness wars"
---

# Lesson 6.1 · The harness wars

**Where this gets you:** you'll walk into a customer engagement and see immediately which parts of their setup they own and which they're renting — and know which moves protect them from lock-in.

## The idea

The model is a commodity. The layer around it is where lock-in happens.

That layer is the **harness**: memory, skills, tools, and an agent runtime wrapped around a raw model. Claude Code, ChatGPT, Cursor, OpenClaw, and a handful of open-source projects are all harnesses. Each is a credible answer to "how do I make this model useful for daily work."

Each one also wants your context inside it. That's where the lock-in lives. If your team's memory, conventions, and accumulated work sit in a vendor's harness, switching vendors costs you all of it. Not just the API bill.

**What that costs, concretely.** A team spends eight months in a vendor's assistant. Every convention, every "we tried that, here's why it failed," every reviewed decision lives in threads inside that product. A cheaper, better model ships elsewhere. Moving means exporting a JSON blob of chat logs that no new tool can read as memory, and rebuilding eight months of institutional knowledge from scratch. So they don't move. The switching cost was never the API spend — it was everything they'd taught the thing. A second team kept the same eight months in markdown in their repo. Their migration was a config line.

There's a real argument being made in public this year, by a few of the people you should be following (more on that in Lesson 6.4): the durable position for any AI product is an owned, exportable harness. Memory in markdown files you control. Skills as files in a repo you own. The model rented from whoever has the best price-performance this quarter.

The implication for FDE work is direct. You don't build customers deeper into your favorite vendor's harness. You build them one they own. The vendor competes at the model layer. Your customer owns the layer above it.

In practice:

- Their context lives in markdown in their git repo, not a vendor's database.
- Their skills are files anyone with repo access can read.
- Their tools are MCP servers or local scripts they own and run.
- The model is a config line you can change next quarter without rewriting the system.

Building straight into a vendor's harness is fast, and that's the right call for a prototype. But the week you hand the system off, the harness becomes the customer's. Owned, exportable, swappable at the model layer. That's what makes the work durable.

## Your exercise

Pick one AI product you've shipped or used heavily. List every place context or memory is rented rather than owned. For each rented place, write one line on what breaks if that vendor disappears tomorrow.

**You're done when** you have an honest portability score for the product and a prioritized list of what to move to "owned" first.

**Practice proof:** save the audit in `NOTES.md` under "harness audit."

**Build on it:** Write a CLI that exports one vendor's chat history into dated markdown files in a git repo, so your memory outlives the vendor.

## Why this matters

Customer projects almost always start with "let's just use [vendor's harness] to move fast." Right call for a prototype. Say out loud at kickoff which parts are prototype and which are production, and the handoff goes cleanly later. Skip that conversation and you build work the customer can't take with them — a worse outcome for everyone, including you.

---

Next: [Lesson 6.2 · The application taxonomy](18-application-taxonomy.html)
