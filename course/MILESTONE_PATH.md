# Milestone path

Use this page as the learner route through the curriculum. The lessons are the source material. The milestones tell you what you should be able to do before moving on.

You do not need to feel ready before you start. Keep the first project small, work in public artifacts, and let proof decide when a milestone is complete.

## The path at a glance

| Milestone | You are learning to | Lessons | Proof before moving on |
|---|---|---|---|
| 0. Get oriented | Learn the few AI concepts you need before touching the CLI | 1.1 to 1.5 | A one-page orientation note you can use while choosing tools and models |
| 1. Take the first turn | Install a coding agent and run a controlled first session | 2.1 to 2.4 | Tool installed, first session log captured, permissions understood |
| 2. Pick a real slice | Choose a project small enough to finish and real enough to matter | 3.1 | One-page project brief with a done check |
| 3. Build with control | Plan, build, review, and ship one slice | 3.2 to 3.4 | A shipped or runnable slice with proof |
| 4. Make quality repeatable | Add briefs, evals, context, review, and design standards | 4.1 to 4.5 | `brief.md`, eval, context file, review pass, and design note |
| 5. Scale the workflow | Coordinate parallel work and review gates | 5.1 to 5.3 | Parallel-agent plan, review gate, and next roadmap |
| 6. Operate in the real world | Handle discovery, teams, cost, security, and handoff | 6.1 to 6.11 | Handoff package another engineer can run |

## Milestone 0: Get oriented

Purpose: remove the fog before the hands-on work starts.

You are not trying to become an AI researcher here. You are learning enough to understand what the agent is doing, what kind of model or tool fits the job, and what risks to watch before you let it edit a repo.

If you already know LLMs, agents, RAG, context windows, open weights, and multimodal models, skim this milestone and move to [Milestone 1](#milestone-1-take-the-first-turn). If those terms are fuzzy, spend 30 to 60 minutes here. It will make the rest of the course much easier.

Read:

- [The AI map](00a-the-ai-map.html)
- [LLMs: just enough to be dangerous](00b-llms-just-enough.html)
- [What makes an agent](00c-what-makes-an-agent.html)
- [Multimodality](00d-multimodality.html)
- [The model zoo](00e-the-model-zoo.html)

Do this:

```bash
mkdir -p agentic-course/artifacts
cd agentic-course
cat > artifacts/00-orientation.md <<'EOF'
# Orientation

What is an LLM?
What makes a workflow agentic?
What should stay in context?
When would I use a frontier model?
When would I use a local or open-weight model?
What is one risk I need to watch?
EOF
```

You are ready to move on when you can explain the answers without copying the lesson text.

## Milestone 1: Take the first turn

Now put your hands on the tool. Claude Code is the main path in the course. Use [CLI variants](CLI_VARIANTS.html) if your room is using Codex CLI, Gemini CLI, or Coco.

Read:

- [What is agentic engineering?](01-what-is-agentic-engineering.html)
- [Install your tool](02-install-your-tool.html)
- [Your first session](03-your-first-session.html)
- [Staying in control](04-staying-in-control.html)

Do this in a repo you can safely change:

```bash
git status --short

# start your selected tool
claude
# or: codex
# or: gemini
```

Ask the agent to inspect the project and summarize how to run it. Do not ask it to make a large change yet.

Capture:

- What command starts the project.
- What command tests it.
- What files look important.
- What permission mode you used.
- What you would not let the agent change without review.

You are ready to move on when you can stop the agent, inspect the diff, and decide whether to keep or reject the work.

## Milestone 2: Pick a real slice

This is where the course becomes yours. Pick one project you care about enough to finish, but small enough that the first version can be boring.

Good first slices:

- Add one command to a CLI.
- Fix one bug and add one regression test.
- Build one small internal utility.
- Clean one dataset and write one validation check.
- Add one route, one screen, or one report.

Write the brief before you build:

```bash
cat > artifacts/01-project-brief.md <<'EOF'
# Project brief

Problem:
Smallest useful slice:
Inputs:
Output:
Done check:
Proof command:
Risk to review:
What I will not change in this slice:
EOF
```

Use [Data + AI practice labs](DATA_AI_LABS.html) if you do not have a project yet. Start with Lab 12 for a mixed or beginner room.

You are ready to move on when the project fits on one page and the done check is not a feeling.

## Milestone 3: Build with control

This is the first real build loop: plan, edit, review, prove, ship.

Read:

- [Plan before you build](06-plan-before-you-build.html)
- [Build it, step by step](07-build-it-step-by-step.html)
- [Ship it](08-ship-it.html)

Run the loop:

```bash
git status --short

# after the agent proposes or makes a slice
git diff

# run the proof for your project
npm test
# or: pytest
# or: make test
# or: your project-specific check
```

Capture:

- The plan you approved.
- The diff you accepted.
- The proof command output.
- One thing you rejected or changed.
- The next smallest slice.

You are ready to move on when another person can read your proof and understand what shipped.

## Milestone 4: Make quality repeatable

Agentic work gets useful when quality is not based on memory or luck. This milestone adds the standards.

Read:

- [The brief](09-the-brief.html)
- [Evals](10-evals-defining-done.html)
- [Context and the second brain](11-context-and-the-second-brain.html)
- [The no-slop standard](12-the-no-slop-standard.html)
- [Design discipline](13-design-discipline.html)

Install the working artifacts:

```bash
mkdir -p decisions
touch AGENTS.md HANDOFF.md artifacts/eval.md artifacts/review.md artifacts/design-note.md
```

If you use Claude Code, `CLAUDE.md` can sit next to or instead of `AGENTS.md`. If you use Codex, keep `AGENTS.md` as the main instruction file.

Capture:

- A better brief for the next slice.
- At least one eval or test.
- A project context file the agent can read.
- A no-slop review note.
- A design note if the work has a user-facing surface.

You are ready to move on when a fresh agent session can read the project context and give back a useful summary.

## Milestone 5: Scale the workflow

Now you are no longer asking one agent for one answer. You are coordinating work.

Read:

- [Orchestration](14-orchestration-parallel-agents.html)
- [Review gates](15-review-gates-and-shipping.html)
- [Where to go next](16-where-to-go-next.html)

Try one parallel plan:

```bash
cat > artifacts/parallel-plan.md <<'EOF'
# Parallel plan

Goal:
Workstream A:
Workstream B:
Shared files:
Review gate:
Merge order:
Proof:
EOF
```

You are ready to move on when you can split work without losing review control.

## Milestone 6: Operate in the real world

This is the customer, team, and production layer. You are learning how to make agentic work survive outside your laptop.

Read:

- [The harness wars](17-the-harness-wars.html)
- [The application taxonomy](18-application-taxonomy.html)
- [Coordinating with agents and humans](19-coordinating-team.html)
- [Staying current: the intel-watch pattern](20-staying-current-intel-watch.html)
- [The team shape](21-team-shape.html)
- [The problems in every layer](22-problems-in-every-layer.html)
- [Discovery and scoping the engagement](23-discovery-and-scoping.html)
- [Communicating to non-engineers](24-communicating-to-non-engineers.html)
- [Observability and cost discipline](25-observability-and-cost.html)
- [Security and compliance for AI products](26-security-and-compliance.html)
- [The handoff playbook](27-the-handoff-playbook.html)

Build the final package:

```bash
mkdir -p decisions runbook
touch HANDOFF.md runbook/operate.md runbook/security.md runbook/cost.md
```

Your final walkthrough should answer:

- What problem did you solve?
- What did the agent do?
- What did you review?
- What proof exists?
- What risks remain?
- What would the next engineer do tomorrow?

You are done with the full path when someone else can clone the repo, read the handoff, run the proof, and continue the next slice without you sitting next to them.

## Pick your pathway

Once the core loop is clear, choose the practice path that matches the learner.

| Pathway | Use these labs | Portfolio proof |
|---|---|---|
| Fresh graduate | Lab 12, then Lab 14, then one tiny app slice | Clear brief, readable diff, test output, reflection note |
| Data engineering | Labs 2, 3, 4, 7, 9 | Pipeline checks, dbt tests, Spark notes, data contracts |
| Analytics | Labs 1, 8, 19 | KPI narrative, dashboard QA, metric proof |
| Big data | Labs 7, 9, 18 | Partition notes, log summarizer, monitoring output |
| ML or MLOps | Labs 20, 21, 22 | Drift check, model card, eval harness |
| AI apps | Labs 23, 24, 27 | RAG eval, tool-call tests, agent memory notes |
| Software engineering | Labs 14, 15, 25, 26 | PR review, release note, story-to-test, API contract |
| Team lead or CTO | Labs 28, 29, 30 | Rollout plan, adoption dashboard, operating model |

Use [Job pathways + AISOFT offerings](JOB_PATHWAYS_AND_AISOFT_OFFERINGS.html) when you want to translate the work into role readiness, portfolio stories, or team enablement.

## How to use this with a mentor

Bring three things to every review:

- Your current artifact folder.
- The latest diff.
- The proof command or evidence.

The review is simple:

1. Show the brief.
2. Explain what the agent did.
3. Walk the diff.
4. Run or show proof.
5. Name the risk.
6. Write the next slice.

That is the whole course in miniature.
