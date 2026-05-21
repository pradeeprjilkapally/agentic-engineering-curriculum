# Lesson 2 · Install your tool

> **Part 1 · Get set up** — Lesson 2 of 16

**By the end of this lesson** Claude Code is installed, authenticated, and you've had your first exchange with it on a real repo.

## The idea

Agentic engineering happens in an agent that lives in your terminal and can touch your real files. This course uses **Claude Code** as the main tool. Codex CLI (OpenAI) and Gemini CLI (Google) work the same way at the level that matters — pick one and the habits transfer. We'll note the differences where they count.

You install it once, log in once, and from then on you start it with a single command inside any project folder.

## Do it

**1. Install Claude Code.**

macOS / Linux / WSL:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Windows (PowerShell):

```powershell
irm https://claude.ai/install.ps1 | iex
```

On a Mac you can also use Homebrew: `brew install --cask claude-code`.

**2. Start it.** Open a terminal, `cd` into a code project you already have, and run:

```bash
claude
```

**3. Log in.** The first run asks you to authenticate. Use your Claude subscription, or an API key from [console.anthropic.com](https://console.anthropic.com) — either works.

**4. Say hello.** Once it's running, type a plain question:

```
what does this project do?
```

Claude reads the project and answers. That's your first agent session.

> **Other tools:** Codex CLI — install from OpenAI's developer site, run `codex`. Gemini CLI — install and run `gemini`. Both prompt for login on first run, the same way.

## The exercise

Install the tool, then point it at a **real repository you know well** — not an empty folder.

Ask it two things:

1. *"What does this project do?"*
2. *"Where would I add a new [something small — a route, a command, a config option]?"*

Read both answers closely. You know this repo — judge whether the agent got it right.

**Done when:** Claude Code is installed and authenticated, and you've had a two-question exchange about a real repo.

## Why it matters

You'll spend the rest of this course in this tool. Installing it and proving it can read a real codebase — today, on something you can fact-check — means every later lesson starts from "it works" instead of "does it work?"

---

Previous: [Lesson 1 · What is agentic engineering?](01-what-is-agentic-engineering.md) · Next: Lesson 3 · Your first session — the core loop
