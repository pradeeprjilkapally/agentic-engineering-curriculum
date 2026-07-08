# Screenshot provenance

Screenshots in this directory are typeset as SVG (so they stay crisp, searchable,
and diffable), but every line of text in them is transcribed verbatim from a real
session. Nothing here is invented. If you change one, re-run the session and
re-transcribe it — don't hand-edit the output text.

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
