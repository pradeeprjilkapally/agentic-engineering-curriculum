# Practice run

Run the course through artifacts. Each lesson should leave something concrete in a repo: a file, command, diff, test, proof note, or shipped slice.

## Learner tracks

| Learner | Start here | Project size | Support needed |
|---|---|---|---|
| Fresh graduate | Lessons 1-4 slowly, with a tiny app or CLI | 1 page, 1 command, or 1 bug fix | More review, smaller slices, more explanation of diffs |
| Experienced engineer new to agents | Lessons 1-4 quickly, then focus on planning and gates | A real backlog item or small internal tool | Pushback on scope and proof |
| Team lead | Do the whole path on one team repo | One team-owned improvement | Standards, review gates, rollout plan |
| Workshop cohort | Shared lab first, personal project second | Shared lab during the day | Live correction and peer review |

## The project rule

The project must be:

- **Small enough** to finish during the course.
- **Real enough** that the learner cares whether it works.
- **Checkable enough** that done is not a feeling.

Good examples:

- Add one command to an existing CLI.
- Fix one bug in a small app.
- Add one route and one test.
- Build a one-page utility.
- Create a small internal dashboard from static data.

Bad first projects:

- Rebuild the company platform.
- Learn agents while also learning a new framework.
- Build an app with auth, payments, database, deployment, and analytics.
- Anything where "done" cannot be tested.

## Every lesson produces proof

| Part | Proof |
|---|---|
| Part 1 | Tool installed, first session run, permissions understood |
| Part 2 | Project chosen, plan approved, first slice built, first version shipped |
| Part 3 | Brief, eval, context, review pass, and design standard installed |
| Part 4 | Parallel-agent plan, review gate, proof checklist, next roadmap |

## Instructor loop

For live cohorts, run every exercise with the same loop:

1. Demo the habit on a shared lab.
2. Give learners a small task.
3. Let them run the agent.
4. Stop for diff review.
5. Ask what proof exists.
6. Have them write the next instruction.

The teaching moment is usually the review after the agent does something plausible but incomplete.

## Shared workshop command block

Use this block when the room needs one rhythm:

```bash
# start in the learner's repo
cd path/to/project

# start the selected tool
claude
# or: codex
# or: gemini

# after the agent finishes a slice
git status --short
git diff

# run the project check
npm test
# or: pytest
# or: make test

# only after review and proof
git add .
git commit -m "feat: complete workshop slice"
```
