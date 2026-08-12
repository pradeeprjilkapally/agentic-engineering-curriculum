# Screenshot provenance

Screenshots in this directory are typeset as SVG (so they stay crisp, searchable,
and diffable), but every line of text in them is transcribed verbatim from a real
session. Nothing here is invented. If you change one, re-run the session and
re-transcribe it — don't hand-edit the output text.

## `verify-install-terminal.svg`

Captured 2026-07-08. Used in Lesson 2.2.

Every line is the real output of these three commands, run on a machine with Claude
Code already installed:

```bash
claude --version   # → 2.1.204 (Claude Code)
which claude       # → <install dir>/claude
claude --help      # → the first four lines of the usage text
```

Two honest notes. The home directory in `which claude` is rewritten to
`/Users/agentics/` so the capture doesn't leak a real username — the path shape is
unchanged. And the `install.sh` line is deliberately **not** shown: running it again
on an already-installed machine would not have produced a truthful first-install
transcript, and inventing one is exactly what this file exists to prevent. The
capture starts where honest capture was possible.

Re-running `claude --version` on a newer release will print a different version. That
is fine — re-transcribe rather than editing the digits.

## `first-session-terminal.svg`

Captured 2026-07-08. Used in Lesson 2.3.

Set up the repo the lesson describes:

```bash
mkdir todo-cli && cd todo-cli
printf 'def greet(name):\n    print("Hello " + name)\n\ngreet("world")\n' > app.py
printf '# todo-cli\n\nA tiny practice project for Lesson 3.\n' > README.md
git init -q && git add -A && git commit -qm initial
```

Run the agent with the lesson's own first-session prompt:

```bash
claude -p 'Find one tiny improvement here, done in under 10 min.
Tell me the file first, then show the diff and how you checked it.' \
  --allowed-tools "Read,Edit,Bash(python3:*),Bash(git diff:*)"
```

Then verify by hand, exactly as the lesson tells the learner to:

```bash
git status --short
git diff
python3 app.py
```

The agent chose to guard the module-level `greet("world")` call behind
`if __name__ == "__main__":` — it noticed the greeting fired on import. It ran the
program *before* editing to establish the baseline, which is the detail the lesson
points at. That behaviour is the agent's own; it was not steered.

Re-running will not always produce the same improvement. If it picks something
different, re-transcribe the SVG to match what actually happened rather than
forcing the old text.
