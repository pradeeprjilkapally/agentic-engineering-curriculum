# Second-Brain Starter

An agent is only as good as the context you can hand it. Every time you re-explain your architecture, your conventions, your past decisions — that's leverage leaking.

The fix: write it down once, in a form the agent picks up **automatically**. That's a second brain. This folder is a starting skeleton.

## What's in here

| File | What it holds |
|------|--------------|
| [`CLAUDE.md`](CLAUDE.html) | The always-loaded context — stack, conventions, standards, how to work with you. The agent reads this every session. |
| [`playbooks/`](playbooks/) | Step-by-step procedures for things you do repeatedly — deploys, releases, incident response. Reusable, not re-derived. |
| [`memory/`](memory/) | Durable facts that accumulate over time — decisions, scars, what worked and what didn't. |

## The principle

There are three tiers of context, by how often it changes:

1. **`CLAUDE.md`** — slow-changing truth about the project and how you work. Loaded every time.
2. **`playbooks/`** — procedures. Pulled in when the task matches.
3. **`memory/`** — facts that accrue. One file per fact; an index so the agent can find them.

Don't put fast-changing task detail in any of these — that's what the brief is for. The second brain is the *stable* layer underneath the briefs.

## How to build yours

Don't try to write it all at once — you'll write fiction. Build it by **subtraction from repetition**: for one week, every time you explain something to an agent that you've explained before, stop and write it into the right tier instead of explaining it again.

Month one, you're documenting. Month three, every task starts with the agent already knowing your stack, your standards, and your scars. That compounding is the real 10x — and it's the part you own. The model is the same for everyone; the second brain is not.

## Adapt for your tools

This skeleton uses `CLAUDE.md` (Claude Code's convention). The idea is tool-agnostic — Cursor rules, a `CONVENTIONS.md`, an `AGENTS.md`, whatever your agent reads automatically. The filename doesn't matter. The discipline of writing context down once does.
