---
title: "Second-Brain Starter"
permalink: /second-brain-starter/
---

# Second-Brain Starter

Every repeated explanation is leverage leaking. Write stable context once, in a form the agent picks up **automatically**.

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

Do not put fast-changing task detail here; that belongs in the brief.

## How to build yours

Build it by **subtraction from repetition**: when you explain something for the second time, write it into the right tier instead of explaining it again.

## Adapt for your tools

This skeleton uses `CLAUDE.md` (Claude Code's convention). The idea is tool-agnostic — Cursor rules, a `CONVENTIONS.md`, an `AGENTS.md`, whatever your agent reads automatically. The filename doesn't matter. The discipline of writing context down once does.
