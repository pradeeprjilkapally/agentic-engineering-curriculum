# Lesson 2.2 · Install your tool

**Where this gets you:** the tool installed, you logged in, and a first real exchange with it. About ten minutes of work.

## The idea

Everything in this course happens inside a terminal agent that can touch your actual files. We use **Claude Code** as the main path. Codex CLI, Gemini CLI, and Coco follow the same habits with different commands and permission models.

You install it once and log in once. After that, you start it by typing one word inside any project.

## Do it

**Choose your track.** Stay on one for the course unless you have a reason to switch.

| Track | Use when | Start command |
|---|---|---|
| Claude Code | You want the main course path | `claude` |
| Codex CLI | You want the OpenAI CLI path | `codex` |
| Gemini CLI | You want the Google CLI path | `gemini` |
| Snowflake Coco | Your team works inside Snowflake or a governed enterprise workspace | your approved Coco entry point |

The rest of this lesson uses Claude Code as the example.

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

Keep this quick-start block handy during the workshop:

```bash
# move into a project you already understand
cd path/to/your-project

# start the primary course tool
claude

# first orientation prompt to paste into the agent
what does this project do?
```

**Log in.** The first run walks you through signing in.

**Say something.** When it's ready, just ask it a plain question:

```
what does this project do?
```

It reads the project and answers from the code. That's a real agent session.

> **Using something else?** Codex CLI: install from OpenAI's developer site, run `codex`. Gemini CLI: install it, run `gemini`. Coco: use your organization's approved setup path. The habit is the same: start in the repo, sign in, ask it to orient on code you know.

For the full translation table, keep [CLI variants](CLI_VARIANTS.html) open while you work.

## Your exercise

Point the tool at a repo you know, not an empty folder. If you are a fresh graduate without a repo yet, use a tiny class app, portfolio project, or sample CLI with fewer than ten files.

Ask it two things:

1. What does this project do?
2. Where would I add a new [something small. A route, a command, a config option]?

Use this exact starter if you want the low-friction path:

```text
What does this project do?

Then answer this: where would I add a small route, command, or config option?
Read the repo first. If you are unsure, say what you checked and what you still need.
```

Read the answers like a reviewer. You know this code. Did it get it right?

**You're done when** the tool is installed, you're logged in, and you've had that two-question back-and-forth on a real repo.

**Practice proof:** paste the tool name, repo name, and the two answers into a `NOTES.md` file. Mark anything the agent got wrong.

## Why this matters

You're going to live in this tool for the rest of the course. Getting it working today, and watching it actually understand code you know, means every lesson after this starts from "this works" instead of "wait, is it broken?"

---

Previous: [Lesson 2.1 · What is agentic engineering?](01-what-is-agentic-engineering.html) · Next: [Lesson 2.3 · Your first session](03-your-first-session.html)
