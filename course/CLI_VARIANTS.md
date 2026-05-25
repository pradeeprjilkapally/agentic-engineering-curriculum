# CLI variants

Use one tool for the course if you can. Switching tools every lesson adds noise. The habits are the same; commands and permission models differ.

## Pick a track

| Track | Start command | Best fit | What to watch |
|---|---|---|---|
| Claude Code | `claude` | Primary course path, strongest fit for planning, editing, and repo work | Plan mode and permission prompts |
| Codex CLI | `codex` | OpenAI users, review-heavy code work, test-driven loops | Approval mode, sandbox rules, command output |
| Gemini CLI | `gemini` | Google users, large-context exploration, multimodal-adjacent work | Workspace context and command permissions |
| Snowflake Coco | your org's Coco entry point | Enterprise data and Snowflake-centered teams | Data boundaries, workspace access, governance |

## Start commands

Use one of these in the root of the project you are working on:

```bash
# Claude Code track
cd path/to/your-project
claude

# Codex CLI track
cd path/to/your-project
codex

# Gemini CLI track
cd path/to/your-project
gemini
```

Coco learners should open the approved workspace for the repo, Snowflake object, or data product. The command is whatever your organization has standardized.

## Translation table

| Course habit | Claude Code | Codex CLI | Gemini CLI | Coco |
|---|---|---|---|---|
| Start a session | `claude` in the repo | `codex` in the repo | `gemini` in the repo | open Coco in the approved workspace |
| Ask for orientation | `what does this project do?` | same prompt | same prompt | same prompt, scoped to allowed data |
| Plan before edits | Shift+Tab into Plan Mode | ask for a plan and do not approve edits yet | ask for a plan before edits | require a written plan before execution |
| Approve file edits | Review the proposed edit/tool call | Review file patch and command approvals | Review edit/tool permissions | Review governed action |
| Interrupt | Esc | interrupt/stop in the CLI | interrupt/stop in the CLI | stop the run/session |
| Verify | run tests, inspect diff | run tests, inspect diff | run tests, inspect diff | run approved checks and logs |
| Record memory | `CLAUDE.md`, playbooks, memory files | `AGENTS.md`, repo instructions, memory files | repo instructions, memory files | approved workspace docs |

## One rule across every tool

Accept output only when you can point to proof: a diff you read, a test you ran, a page you opened, command output you understand, or a reviewer note you wrote.

```bash
# proof commands you will use constantly
git status --short
git diff
npm test
pytest
curl -sI https://your-live-url.example
```
