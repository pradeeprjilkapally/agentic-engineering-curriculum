# Lesson 6.3 · Coordinating with agents and humans

**Where this gets you:** you'll have a small set of file conventions that let multiple agents and multiple humans work on the same project without collisions, and you'll be able to set them up on a new repo in 20 minutes.

## The idea

Lesson 5.1 was you, running agents in parallel. This is the team version. Once more than one person or more than one agent touches the same project, coordination becomes a tax. Your job is to make that tax small with conventions that outlive any single session.

Here's what the tax feels like when you don't pay it. Tuesday, you tell an agent to switch the project from SQLite to Postgres. It works. Thursday, a teammate opens a fresh session, sees an unfamiliar connection string, assumes the agent hallucinated it, and reverts to SQLite. Friday, your agent — cold, no memory of Tuesday — reads the code, decides SQLite won't hold, and migrates to Postgres again. Nobody was wrong. The decision just never lived anywhere except in a chat window that closed. A three-line file in `decisions/` would have ended it.

![A team standing around a whiteboard, working a problem out together.](../assets/photos/coordinating-team.jpg)

*The decisions made in a room like this are worth nothing to next week's agent unless somebody writes them down.*

So: the files you want in every agentic project.

**AGENTS.md**. What an agent needs to know on a cold start. The stack, the conventions, where secrets live, what not to touch. Anyone reading it — human or agent — should be useful within ten minutes.

**HANDOFF.md**. What the last session did, what's pending, where the gotchas are. Append-only. Read at the start of every session, updated at the end.

**decisions/**. One file per real architectural or scope decision, with the why and the date. Append-only, never edited. Think ADRs (Architecture Decision Records), extended to product scope, not just architecture.

**LOG.md**. What changed today, who changed it (human or agent), a link to the diff. Short and chronological.

**CLAUDE.md**. Usually a symlink to AGENTS.md, so Claude Code picks it up automatically. Codex CLI and Gemini CLI read AGENTS.md directly.

Then the GitHub primitives you'll lean on across sessions:

- **Issues with labels** as the queue: `ready-for-agent`, `needs-human`, `blocked`.
- **PR comments** as the review surface, for humans and agents both.
- **Commit trailers** like `Co-authored-by:` to attribute work clearly.

The discipline underneath all of it is one rule: **the project's state lives in the files, not in anyone's head.** Every session reads HANDOFF.md before it starts and updates it before it ends. Every real decision lands in `decisions/`. Every change gets a LOG.md line.

This matters doubly in FDE work. You'll be on a customer team with several humans, your agents, and their agents. Without conventions, that collapses in the first month. With them, four people and six agents outship a traditional team of ten.

## Your exercise

Take your project candidate. Add AGENTS.md, HANDOFF.md, and `decisions/0001-stack-choice.md`. Make AGENTS.md actually useful. Stack, conventions, where secrets live, what not to touch.

Then start a fresh Claude Code session, ask the agent to read those files, and have it report what it understood. Compare that summary to what you'd want a new teammate to know on day one.

**You're done when** a cold agent can pick up your project and start contributing without you in the chat.

**Practice proof:** save the cold agent's report in `NOTES.md` under "cold start test."

**Build on it:** write a `handoff` CLI that reads your repo's last ten commits and open PRs, then drafts the HANDOFF.md update for you to edit and commit.

## Why this matters

Once you can hand your project to a future version of yourself — or to a customer engineer next quarter — every Friday becomes a clean stopping point instead of a held breath. As an FDE you'll hand projects off constantly: end of engagement, end of sprint, end of week. These conventions are what make those handoffs cheap.

---

Next: [Lesson 6.4 · Staying current: the intel-watch pattern](20-staying-current-intel-watch.html)
