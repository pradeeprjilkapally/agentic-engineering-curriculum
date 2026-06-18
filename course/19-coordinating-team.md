# Lesson 6.3 · Coordinating with agents and humans

**Where this gets you:** you'll have a small set of file conventions that let multiple agents and multiple humans work on the same project without collisions, and you'll be able to set them up on a new repo in 20 minutes.

## The idea

Solo parallel orchestration was Lesson 5.1. This is the team version. When more than one agent or more than one human work on the same project, coordination becomes a tax. The job is to reduce the tax with conventions that survive a session ending.

The files you want in every agentic project:

**AGENTS.md**. What an agent should know about this repo on a cold start. The stack, the conventions, where the secrets live, what NOT to touch. Anyone (or any agent) reading this should be able to be useful within ten minutes.

**HANDOFF.md**. What the last session did, what's still pending, where the gotchas are. Append-only across sessions. Every session reads it before it starts and updates it before it ends.

**decisions/**. One file per real architectural or scope decision, with the why and the date. Append-only, never edited. Think ADRs (Architecture Decision Records), but extended to product scope and not just architecture.

**LOG.md**. What changed today, who changed it (human or agent), links to the diff. Short and chronological.

**CLAUDE.md**. Usually just a symlink to AGENTS.md so Claude Code picks it up automatically. Other tools (Codex CLI, Gemini CLI) read AGENTS.md directly.

The GitHub primitives you'll lean on for cross-session coordination:

- **Issues with labels** as the queue: `ready-for-agent`, `needs-human`, `blocked`, etc.
- **PR comments** as the review surface for humans and agents both.
- **Commit trailers** like `Co-authored-by:` to attribute work to specific agents or humans clearly.

The discipline that makes all of this work: every session, agent or human, reads HANDOFF.md before it starts and updates it before it ends. Every real decision lands in decisions/. Every change gets a LOG.md entry. The rule is "the project's state lives in the files, not in anyone's head."

Why this matters for FDE work specifically: you'll often work with a customer team that has multiple humans, plus your agents, plus their agents. Without these conventions, the work collapses into chaos in the first month. With them, four people and six agents can ship more than ten people on a traditional team would.

## Your exercise

Take your project candidate. Add AGENTS.md, HANDOFF.md, and decisions/0001-stack-choice.md. Make AGENTS.md actually useful. Stack, conventions, where secrets live, what not to touch.

Then start a fresh Claude Code session and ask the agent to read those files and report back what it understood about the project. Compare its summary to what you'd want a new teammate to know on day one.

**You're done when** a cold agent can pick up your project and start contributing without you in the chat.

**Practice proof:** save the cold agent's report in `NOTES.md` under "cold start test."

## Why this matters

Once you can hand off your project to a future version of yourself (or a customer engineer next quarter), every Friday becomes a clean stopping point instead of a held breath. As an FDE you'll be handing projects off constantly: at the end of every engagement, every sprint, every Friday afternoon. The conventions in this lesson are what make those handoffs cheap and quietly satisfying instead of stressful.

---

Next: [Lesson 6.4 · Staying current: the intel-watch pattern](20-staying-current-intel-watch.html)
