# Lesson 6.1 · The harness wars

**Where this gets you:** you'll be able to walk into a customer engagement and immediately see where their harness is owned vs rented, and you'll know which moves protect them from lock-in.

## The idea

The model is a commodity. The harness around it is where lock-in happens. As a Forward Deployed Engineer, you build the customer's harness. Not the vendor's.

A harness is the layer that wraps memory, skills, tools, and an agent runtime around a raw model. Today's well-known harnesses include Claude Code, ChatGPT, Cursor, OpenClaw, and several emerging open-source projects. Each one is a credible answer to the question "how do I make this model actually useful for daily work."

But each harness also wants your context inside it. That's where the lock-in lives. If your team's memory, conventions, and accumulated work live inside one vendor's harness, switching vendors costs you all of that. Not just the API spend.

There's a real argument being made in public this year, by a few of the people you should be following (more on that in Lesson 6.4), that the durable position for any AI product is an owned, exportable harness. Memory in markdown files you control. Skills as files in a repo you own. The model rented from whoever has the best price-performance this quarter.

The implication for FDE work is direct. When you go into a customer's stack, you do not build them deeper into your favorite vendor's harness. You build them an owned, exportable harness. The vendor wins or loses on the model layer. Your customer wins by owning the layer above it.

What this looks like in practice:

- Their context lives in markdown in their git repo, not in a vendor's database.
- Their skills are files anyone with access to the repo can read.
- Their tools are MCP servers or local scripts they own and run.
- The model is a config line you can change next quarter without rewriting the system.

The temptation will always be to build directly into a vendor's harness because it's fast. That's the right call for a prototype. The week you hand the system off, the harness becomes the customer's. Owned, exportable, swappable at the model layer. That's the move that makes the work durable.

## Your first exercise

Pick one AI product you've shipped or used heavily. List every place context or memory is rented vs owned. For each rented place, write one line on what would break if that vendor went away tomorrow.

**You're done when** you have an honest portability score for the product and a prioritized list of what to move to "owned" first.

**Practice proof:** save the audit in `NOTES.md` under "harness audit."

## Why this matters

Customer projects almost always start with someone saying "let's just use [vendor's harness] to move fast." Right call for a prototype. Make the "this is prototype, this is production" distinction explicit at kickoff, and the handoff happens cleanly later. Skip that conversation and you end up building work the customer can't take with them, which is a worse outcome for everyone, including you.

---

Next: [Lesson 6.2 · The application taxonomy](18-application-taxonomy.html)
