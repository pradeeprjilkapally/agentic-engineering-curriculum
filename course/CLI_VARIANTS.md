# CLI variants

Use one tool for the whole course if you can. Switching tools every lesson makes the learning noisy. The habits are the same; the commands and permission model differ.

## Pick a track

| Track | Start command | Best fit | What to watch |
|---|---|---|---|
| Claude Code | `claude` | Primary course path, strongest fit for planning, editing, and repo work | Plan mode and permission prompts |
| Codex CLI | `codex` | OpenAI users, review-heavy code work, test-driven loops | Approval mode, sandbox rules, command output |
| Gemini CLI | `gemini` | Google users, large-context exploration, multimodal-adjacent work | Workspace context and command permissions |
| Snowflake Coco | your org's Coco entry point | Enterprise data and Snowflake-centered teams | Data boundaries, workspace access, governance |

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

Do not accept output because it sounds confident. Accept it because you can point to proof: a diff you read, a test you ran, a page you opened, a command output you understand, or a reviewer note you wrote yourself.

