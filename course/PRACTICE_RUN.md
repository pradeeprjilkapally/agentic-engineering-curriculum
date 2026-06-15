# Practice run

Run the course through artifacts. Each lesson should leave something concrete in a repo: a file, command, diff, test, proof note, or shipped slice.

## The bar

The bar is useful independence. A learner finishes the course when they can take a small real problem, brief it, run an agent, review the diff, prove the result, and leave a handoff another engineer can continue from.

For the full Forward Deployed Engineer path, use the [Two-week FDE ramp](TWO_WEEK_FDE_RAMP.html). For hiring or intensive coaching, use the 5-day variant with a Friday artifact walkthrough.

Teach toward visible behavior, not tool fluency. The learner should be able to explain the brief, plan, diff, proof, risk, decision, and next slice in plain English.

## Learner tracks

| Learner | Start here | Project size | Support needed |
|---|---|---|---|
| Fresh graduate | [Beginner prep](BEGINNER_PREP.html), Part 1 thoroughly, then Lessons 2.1 to 2.4 slowly, with a tiny app or CLI | 1 page, 1 command, or 1 bug fix | More review, smaller slices, more explanation of diffs |
| Experienced engineer new to agents | Skim Part 1, do Lessons 2.1 to 2.4 quickly, then focus on planning, gates, and all of Part 6 | A real backlog item or small internal tool | Pushback on scope and proof |
| Senior engineer aiming for FDE | The [Two-week FDE ramp](TWO_WEEK_FDE_RAMP.html). One real project, all 32 lessons, the Day-10 acceptance test | A real customer-style project | Daily check-in, Day-10 peer review |
| Team lead | Do the whole path on one team repo. Adopt Part 6 conventions for the team | One team-owned improvement | Standards, review gates, rollout plan, AGENTS.md/HANDOFF.md/decisions/ adopted across team repos |
| Workshop cohort | Shared lab first, personal project second | Shared lab during the day | Live correction and peer review |
| Hiring filter (candidate cohort) | The 1-week intensive variant of the [Two-week FDE ramp](TWO_WEEK_FDE_RAMP.html), as a second-round filter | A project the candidate picks Monday | Daily check-in. Friday artifact review informs the decision. Treat as second-round, not first. |

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
| Part 2 | Tool installed, first session run, permissions understood |
| Part 3 | Project chosen, plan approved, first slice built, first version shipped |
| Part 4 | Brief, eval, context, review pass, and design standard installed |
| Part 5 | Parallel-agent plan, review gate, proof checklist, next roadmap |
| Part 6 | Discovery note, team conventions, security model, cost/observability note, handoff package |

## Artifact rubric

Use this when reviewing a learner, candidate, or cohort artifact.

| Area | Pass | Not yet |
|---|---|---|
| Brief | Goal, constraints, inputs, outputs, and done check are written before build | Prompt is vague or only describes intent |
| Plan | Plan is scoped to one slice and names files, tests, and risks | Plan tries to solve the whole product |
| Agent use | Learner redirects the agent and can explain why | Learner accepts whatever the agent returns |
| Review | Diff is read and explained in plain English | Diff is merged because tests happened to pass |
| Proof | Command output, screenshot, test, fixture, log, or deployed URL is captured | "It works on my machine" with no evidence |
| Context | `AGENTS.md`, `CLAUDE.md`, `HANDOFF.md`, or decision note exists | Context lives only in chat history |
| Handoff | Another engineer can run the next step | The learner must be in the room for progress |

## Instructor loop

For live cohorts, run every exercise with the same loop:

1. Demo the habit on a shared lab.
2. Give learners a small task.
3. Let them run the agent.
4. Stop for diff review.
5. Ask what proof exists.
6. Have them write the next instruction.

The teaching moment is usually the review after the agent does something plausible but incomplete.

For a deeper instructor reference, use [Teaching agentic engineering](TEACHING_AGENTIC_ENGINEERING.html).

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

## Review questions

Ask these after every exercise:

- What problem did you ask the agent to solve?
- What did you constrain?
- What did the agent change?
- What proof did you run?
- What is still risky?
- What will future-you need to know?
