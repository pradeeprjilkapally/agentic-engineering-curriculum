# Beginner prep: Git, terminal, and language basics

Use this page if you are a fresh graduate, switching stacks, or new to working in a repo with a coding agent.

The goal is not to become expert before starting. The goal is to know enough Git, terminal, and language basics that you can follow what the agent is doing, review its diff, run the project, and ask better questions.

## What you need before Milestone 1

You are ready for the CLI milestone when you can do these without guessing:

| Skill | You should be able to | Why it matters with agents |
|---|---|---|
| Terminal | `cd` into a project, list files, run one command | The agent works inside your project folder |
| Git status | Run `git status --short` | You need to know what changed |
| Git diff | Run `git diff` and read changed lines | Agent review happens in the diff |
| Git commit | Stage and commit a small change | You need clean checkpoints |
| Language basics | Read a function, variable, import, and error message | You need to judge whether the agent's edit makes sense |
| Project commands | Run the app or tests | Done needs proof |

## Git quick path

Start with the official resources:

- [Install Git](https://git-scm.com/downloads)
- [Pro Git book](https://git-scm.com/book/en/v2)
- [GitHub: About Git](https://docs.github.com/en/get-started/using-git/about-git)

Practice this in a small repo:

```bash
# see where you are
pwd

# see files
ls

# check Git state
git status --short

# create a small branch for practice
git switch -c practice/first-agent-change

# after making a tiny edit, inspect it
git diff

# save the checkpoint
git add .
git commit -m "docs: practice first agent change"

# see recent commits
git log --oneline -5
```

Fresh graduate rule: do not accept an agent change until you have run `git status --short` and `git diff`.

## Terminal basics

You do not need to memorize the terminal. You need the small set you will use every day:

```bash
# move around
pwd
ls
cd path/to/project

# make folders and files for artifacts
mkdir -p artifacts
touch artifacts/notes.md

# read files
cat README.md

# search text in the repo
rg "TODO"

# run common project checks
npm test
pytest
make test
```

If a command fails, do not hide it. Copy the command, the error, and what you tried into your notes. That becomes useful context for the agent and for a mentor.

## Pick one language lane

Pick the lane closest to your project. You can add more later.

| Lane | Learn first | Official references |
|---|---|---|
| Web app | HTML, CSS, JavaScript, then TypeScript | [MDN HTML](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content), [MDN JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide), [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html) |
| Data or automation | Python, virtual environments, files, CSVs | [Python Tutorial](https://docs.python.org/3/tutorial/), [Python venv](https://docs.python.org/3/library/venv.html) |
| Analytics or data engineering | SQL, tables, joins, filters, grouping | [PostgreSQL Tutorial](https://www.postgresql.org/docs/current/tutorial.html) |
| CLI and scripts | Shell commands, files, pipes, exit codes | [Bash Manual](https://www.gnu.org/software/bash/manual/bash.html) |

Do not try to learn every language before starting. Choose one lane, build one tiny thing, and let the course teach the agent workflow around it.

## Tiny project choices

Good first projects for fresh graduates:

- A one-command CLI that reads a file and prints a summary.
- A small HTML page with one form and one validation rule.
- A Python script that cleans one CSV.
- A README improvement with verified setup commands.
- A tiny bug fix in a class or portfolio project.

Avoid projects with auth, payments, databases, deployment, and a new framework all at once. That is too many new things in one room.

## How to use an agent while learning

Use the agent as a guide, but keep ownership with you.

Good prompts:

```text
Explain this file to me at a beginner level. Do not change it.
```

```text
Before editing, tell me what command proves this change works.
```

```text
Show me the smallest possible change and the exact diff I should review.
```

```text
I am new to this language. After the change, explain the syntax you used.
```

Bad prompts:

- "Build the whole app."
- "Fix everything."
- "Make it production ready."
- "Just do it."

Those prompts hide the learning and make review impossible.

## Centralize what you learn

Every time the agent or a mentor teaches you something reusable, put it somewhere the next session can read.

Use `AGENTS.md` or `CLAUDE.md`:

```bash
cat >> AGENTS.md <<'EOF'

## Beginner notes

- Run `npm test` before saying frontend work is done.
- Use `src/components/` for shared UI.
- Do not edit generated files in `dist/`.
- If a command fails, paste the exact error into the handoff note.
EOF
```

This is how the course compounds. One learner finds a missing command, updates the shared instructions, and everyone after them starts with less confusion.

## Ready checkpoint

Before moving to [Milestone 1](MILESTONE_PATH.html#milestone-1-get-comfortable-in-the-cli), you should have:

- Git installed.
- One small repo you can safely change.
- One language lane picked.
- A command that runs the project or a tiny script.
- A habit of checking `git status --short` and `git diff`.
- A place for notes, usually `artifacts/` plus `AGENTS.md` or `CLAUDE.md`.
