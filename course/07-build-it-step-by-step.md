# Lesson 3.3 · Build it, step by step

**Where this gets you:** the first real slice of your project actually built and running. One meaningful piece, done and working.

## The idea

You have an approved plan. Now execute it in **slices** — one piece small enough to review in a few minutes.

Skip the mega-prompt. Hand over the whole plan at once and the agent drifts, and you're left reviewing a pile you can't reason about.

Here's what that looks like. You paste all six plan steps in. Twenty minutes later there are 900 lines across eleven files. It runs. You skim it, it looks plausible, you commit. Two days on, a test fails, and you find the agent quietly rewrote your date parser in step 3 because step 5 was easier that way. You never asked for that. It was in the diff — but nobody reads a 900-line diff line by line. Six slices would have caught it in step 3, in the thirty seconds it takes to read forty lines.

For each slice:

- **Review it.** Read the diff. Does it do what you asked, and only that?
- **Run it.** Don't take "it works" on faith. Run the code, see the output.
- **Course-correct.** If it's off, say so now, before the next slice stacks on top.
- **Commit.** Small commits are your undo button. When something goes sideways later, you have a clean point to fall back to.

Keep asks scoped. "Add the parser" is reviewable. "Add the parser, validation, error handling, and tests" is four slices pretending to be one.

When a slice goes wrong, stop. Return to the last good commit. Re-plan that slice.

## Do it

Take the first slice from your approved plan. Ask the agent to build just that piece.

Use this wording if you're unsure:

```text
Build only step 1 from the approved plan. Before editing, restate what files you expect to touch. After editing, show me the diff and how you verified it.
```

Claude Code, Codex CLI, Gemini CLI, and Coco all run this loop. What matters isn't the command. It's the slice size.

When it's done, read the diff, run the code, and confirm the piece does what the plan said.

Use this review-and-commit block for every slice:

```bash
# inspect what changed
git status --short
git diff

# run the smallest meaningful verification
npm test
# or
pytest
# or
make test

# commit only after you have read the diff and seen the check pass
git add .
git commit -m "feat: complete first project slice"
```

If it's right, commit it with a short message. If it's wrong, correct the agent and let it revise. If it's badly off, reset to your last commit and re-plan the slice. Either way, end with one piece that genuinely works.

## Your exercise

Build the first real slice of your project. One meaningful piece: reviewed, run, and committed.

**You're done when** one real piece of your project runs, and you've seen it run, not just been told it does.

**Practice proof:** write down the slice name, files changed, verification command, and what you will ask for next.

**Build on it:** build a `git slice` script that refuses to commit when the diff exceeds 150 lines, and runs your tests first.

## Why this matters

Small slices are how you stay the engineer instead of the spectator. You review what you can actually review, you catch drift early, and every commit is a safe point to return to. Slice, review, run, commit. That rhythm is what the rest of your project gets built on.

---

Previous: [Lesson 3.2 · Plan before you build](06-plan-before-you-build.html) · Next: [Lesson 3.4 · Ship it](08-ship-it.html)
