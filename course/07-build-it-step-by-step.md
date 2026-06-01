# Lesson 7 · Build it, step by step

**Where this gets you:** the first real slice of your project actually built and running. One meaningful piece, done and working.

## The idea

You have an approved plan. Now execute it in slices.

Avoid the mega-prompt. If you hand over the whole plan at once, the agent drifts and you end up reviewing a pile you cannot reason about.

Build one piece small enough to review in a few minutes. Then:

- **Review it.** Read the diff. Does it do what you asked, and only that?
- **Run it.** Don't take "it works" on faith. Run the code, see the output.
- **Course-correct.** If it's off, say so now, before the next slice stacks on top.
- **Commit.** When a slice is good, commit it. Small commits are your undo button. When something later goes sideways, you have a clean point to fall back to.

Keep asks scoped. "Add the parser" is reviewable. "Add the parser, validation, error handling, and tests" is four slices pretending to be one.

When a slice goes sideways, stop. Return to the last good commit. Re-plan that slice.

## Do it

Take the first slice from your approved plan. Ask the agent to build just that piece.

Use this wording if you are unsure:

```text
Build only step 1 from the approved plan. Before editing, restate what files you expect to touch. After editing, show me the diff and how you verified it.
```

Claude Code, Codex CLI, Gemini CLI, and Coco can all run this loop. The important part is not the command; it is the slice size.

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

If it's right, commit it with a short message. If it's wrong, correct the agent and let it revise. Or, if it's badly off, reset to your last commit and re-plan the slice. Either way, end with one piece that genuinely works.

## Your exercise

Build the first real slice of your project. Get one meaningful piece working. Reviewed, run, and committed.

**You're done when** one real piece of your project runs, and you've seen it run, not just been told it does.

**Practice proof:** write down the slice name, files changed, verification command, and what you will ask for next.

## Why this matters

Small slices are how you stay the engineer instead of the spectator. You review what you can actually review, you catch drift early, and every commit is a safe point to return to. This is the rhythm (slice, review, run, commit) that the rest of your project gets built on. Get comfortable with it now.

---

Previous: [Lesson 6 · Plan before you build](06-plan-before-you-build.html) · Next: [Lesson 8 · Ship it](08-ship-it.html)
