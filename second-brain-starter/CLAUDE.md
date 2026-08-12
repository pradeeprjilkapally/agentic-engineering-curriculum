---
title: "CLAUDE.md — [Project Name]"
---

# CLAUDE.md — [Project Name]

> This is the always-loaded context skeleton. Fill every section with real specifics; delete the prompts in brackets. Keep it tight — this is read every session, so every line should earn its place. When something here goes stale, fix it the same day.
>
> Delete this blockquote when you fork.

## What this project is

[One paragraph. What it does, who it's for, what stage it's at. The thing a new agent needs to not be confused.]

## Stack

- **Language / runtime:** [...]
- **Framework:** [...]
- **Data:** [...]
- **Deploy target:** [...]
- **Key dependencies and why:** [...]

## How the code is organized

[The map. Where things live, what the top-level directories are for, where NOT to put things. Point at the 3–5 files that matter most.]

## Conventions

The idioms an agent must match instead of using its defaults:

- **Naming:** [...]
- **Error handling:** [...]
- **Tests:** [where, what framework, what "tested" means here]
- **Comments:** [your bar — almost certainly "why, not what"]
- **Imports / structure:** [...]

## Standards — non-negotiable

- Run the **no-slop** review pass before reporting any non-trivial change done.
- For anything with a surface, follow **`DESIGN.md`**.
- **Never claim done without proof.** "Deployed" / "works" / "passing" requires verification in the same turn — a test run, a curl, a screenshot, a log line.
- Report outcomes faithfully — failing tests get reported as failing, with output.

## Git & shipping

- [Branch strategy — e.g. never push to main, feature branches + PRs]
- [How deploys happen, and how to verify one landed]
- [What "done" means — the review gate for this project]

## How to work with me

- [Parallelism default — e.g. independent pieces get parallel agents, not a serial chain]
- [Tone / response style you want]
- [What to ask about vs. decide autonomously]
- [Things that have bitten us before — see `memory/`]

## Pointers

- Playbooks: [`playbooks/`](playbooks/) — procedures for repeated work
- Memory: [`memory/`](memory/) — durable facts, decisions, scars
- Design: `DESIGN.md`
