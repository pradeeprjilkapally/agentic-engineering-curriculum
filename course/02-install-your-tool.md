# Lesson 2 · Install your tool

> **Part 1 · Get set up** — Lesson 2 of 16

**Where this gets you:** the tool installed, you logged in, and a first real exchange with it — about ten minutes of work.

## The idea

Everything in this course happens inside an agent that lives in your terminal and can touch your actual files. We use **Claude Code** as the main tool here. If you'd rather use Codex CLI (OpenAI) or Gemini CLI (Google), go ahead — at the level this course works at, they're the same thing, and we'll point out the few spots where they differ.

You install it once and log in once. After that, you start it by typing one word inside any project.

## Do it

**Install it.**

macOS, Linux, or WSL:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Windows (PowerShell):

```powershell
irm https://claude.ai/install.ps1 | iex
```

On a Mac, `brew install --cask claude-code` works too.

**Start it.** Open a terminal, `cd` into a project you already have on your machine, and run:

```bash
claude
```

**Log in.** The first run walks you through signing in — your Claude subscription, or an API key from [console.anthropic.com](https://console.anthropic.com). Either is fine.

**Say something.** When it's ready, just ask it a plain question:

```
what does this project do?
```

It reads the project and tells you. That's a real agent session — you're already doing it.

> **Using something else?** Codex CLI: install from OpenAI's developer site, run `codex`. Gemini CLI: install it, run `gemini`. Both sign you in on first run the same way.

## Your exercise

Point the tool at a repo you know well — not an empty folder. Somewhere you'd catch a wrong answer.

Ask it two things:

1. What does this project do?
2. Where would I add a new [something small — a route, a command, a config option]?

Read the answers like a reviewer. You know this code. Did it get it right?

**You're done when** the tool is installed, you're logged in, and you've had that two-question back-and-forth on a real repo.

## Why this matters

You're going to live in this tool for the rest of the course. Getting it working today — and watching it actually understand code you know — means every lesson after this starts from "this works" instead of "wait, is it broken?"

---

Previous: [Lesson 1 · What is agentic engineering?](01-what-is-agentic-engineering.md) · Next: Lesson 3 · Your first session
