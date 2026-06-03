# Teaching agentic engineering

Use this guide when you are mentoring one person, running a workshop, reviewing a candidate, or helping a team adopt agentic engineering.

The goal is simple: help the learner turn a real problem into agent-directed work they can scope, review, prove, and hand off.

## Start here

| Situation | Use this path | What good looks like |
|---|---|---|
| One person needs help today | 30-minute mentoring | One small slice briefed, planned, and assigned with a proof command |
| A team is new to agents | 90-minute team session | Everyone sees the same loop, then applies it to a tiny repo task |
| In-person workshop | 1-day workshop | Learners finish one shared lab and one personal slice with proof |
| New hire or FDE ramp | 2-week ramp | One real project shipped with a handoff package |
| Candidate assessment | 5-day artifact review | The candidate shows how they scope, steer, review, and prove work |

If the room is mixed, start smaller than you think. A good first exercise is one file, one command, one fixture, or one failing test.

## The loop you are teaching

Teach the same loop every time. The tool can change. The behavior should not.

| Step | Instructor question | Artifact |
|---|---|---|
| Problem | What is the smallest useful slice? | One-sentence scope |
| Brief | What should the agent know before it starts? | Goal, constraints, inputs, outputs, done check |
| Plan | What files, tests, data, or risks matter? | Reviewable plan |
| Build | What should the agent do first? | Small diff |
| Review | What changed, and would you keep it? | Diff notes |
| Proof | What command, log, screenshot, eval, or deployed URL proves it? | Captured evidence |
| Handoff | What should the next person do? | Decision note and next slice |

## Ready-to-run agendas

### 30-minute mentoring

Use this when one learner is stuck or trying the workflow for the first time.

| Time | Do this |
|---|---|
| 0 to 5 | Pick one tiny slice from their real project |
| 5 to 10 | Write the brief and done check together |
| 10 to 18 | Let the agent inspect and propose a plan |
| 18 to 25 | Review the plan or first diff out loud |
| 25 to 30 | Write the proof command and next instruction |

### 90-minute team session

Use this when a team needs a shared baseline.

| Time | Do this |
|---|---|
| 0 to 10 | Explain the loop using one real slice |
| 10 to 25 | Demo brief, plan, permissions, and proof on a shared lab |
| 25 to 45 | Learners run the same lab in pairs |
| 45 to 65 | Stop for diff review and proof capture |
| 65 to 80 | Each pair writes a next-slice instruction |
| 80 to 90 | Agree on team conventions for `AGENTS.md`, review gates, and proof |

### 1-day in-person workshop

Use this when people are coming from different backgrounds. Keep the morning shared. Make the afternoon role-specific.

| Time | Do this |
|---|---|
| 0:00 to 0:30 | Set up tools, repo, and the workshop command rhythm |
| 0:30 to 1:15 | Shared lab: brief, plan, permissions, first diff |
| 1:15 to 2:00 | Diff review, proof, and handoff note |
| 2:00 to 3:00 | Role paths: app engineering, data engineering, analytics, ML, AI product, leadership |
| 3:00 to 4:15 | Personal slice or role-specific lab |
| 4:15 to 5:00 | Review artifacts in pairs |
| 5:00 to 5:30 | Final walkthrough: proof, risk, decision, next slice |

## Shared lab default

Use [Data + AI practice labs](DATA_AI_LABS.html) when the learner does not bring a project.

| Learner group | Start with |
|---|---|
| Mixed or beginner room | Lab 12: CSV cleaning assistant |
| Data engineering | Lab 4: dbt style model agent |
| Data analytics | Lab 1: LLM data profiling review |
| Big data | Lab 9: Spark log summarizer |
| ML or MLOps | Lab 20: feature drift monitor |
| AI product | Lab 23: RAG evaluator |
| Software engineering | Lab 14: PR reviewer |
| Leaders or CTOs | Lab 30: agentic operating model |

Start every workshop with the same local shape:

```bash
mkdir agentic-lab
cd agentic-lab
git init
mkdir -p data lab-artifacts
```

Then ask the learner to create one file before using the agent:

```bash
cat > lab-artifacts/brief.md <<'EOF'
# Brief

Goal:
Constraints:
Inputs:
Output:
Done check:
Risk to review:
EOF
```

## What learners submit

Every learner should finish with a small artifact package:

- `brief.md`: goal, constraints, inputs, outputs, done check, and risk.
- `plan.md`: the plan they approved or changed.
- `proof.md`: command output, screenshot notes, eval result, logs, or deployed URL.
- `decision.md`: what changed, what was rejected, and why.
- `next.md`: the next smallest slice another person could run.

That package matters more than a perfect final product. It shows whether the learner can direct the work.

## The five instructor moves

### 1. Start with the smallest real thing

Do not let the learner begin with a platform rewrite. Pick one command, one route, one report, one broken test, one data fixture, or one support workflow. The work needs to be real enough to matter and small enough to finish.

### 2. Make the learner say the done check first

Before the agent edits files, ask:

- What output should exist?
- What command proves it?
- What failure would make you reject the result?
- What risk needs human review?

If the learner cannot answer, help them shrink the slice.

### 3. Stop at the diff

The most important classroom moment is not the prompt. It is the diff. Ask the learner to explain:

- what changed,
- why it changed,
- what they would keep,
- what they would reject,
- what proof exists.

If they cannot explain the diff, they do not own the work yet.

### 4. Teach tool choice as translation

Use Claude Code as the main path because the course examples are written that way. Then translate the habit:

- Claude Code: plan mode, CLAUDE.md, permissions, subagents.
- Codex CLI: AGENTS.md, approval modes, local command review, code review agent.
- Gemini CLI: large-context exploration, file tools, shell tools, web fetch, memory, trusted folders.
- Coco: governed data workspace, approved data actions, enterprise evidence.

The habit is stable. The command surface changes.

### 5. Finish with a handoff artifact

Every workshop or cohort should end with a small package:

- brief,
- plan,
- diff,
- proof command output,
- eval or test,
- decision note,
- next-slice instruction.

That is the smallest version of FDE behavior.

## Instructor checklist

Before the session:

- Pick the shared lab or learner project.
- Prepare one local fixture so nobody is blocked by credentials.
- Decide the primary CLI and one fallback CLI.
- Write the proof command on the board.
- Open the relevant course page and lab page.

During the session:

- Keep slices small.
- Make learners read diffs.
- Reject vague "it works" claims.
- Ask for command output, screenshots, logs, or test results.
- Capture the next instruction before moving on.

After the session:

- Ask each learner to commit the artifact package.
- Have them write one paragraph on what the agent got wrong.
- Have them write the next slice as a brief.
- For teams, turn the best artifact into `AGENTS.md`, `HANDOFF.md`, or a team playbook.

## Reference layer

Use these as instructor anchors, not as extra reading homework.

| Reference | Teaching takeaway | Where it appears in this course |
|---|---|---|
| [Claude Code best practices](https://code.claude.com/docs/en/best-practices) | Give the agent a way to verify its work. Explore first, plan, then code. Manage context deliberately. | Lessons 3.2, 3.3, 4.2, 4.3, 5.2 |
| [Anthropic: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) | Start simple. Use workflows when the path is known, agents when the path is open-ended. Add complexity only when it improves outcomes. | Lessons 1.3, 6.2, 6.6 |
| [Anthropic: Writing effective tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents) | Tools need clear definitions, careful context, and evaluation-driven iteration. | Lessons 4.1, 4.2, 6.3, 6.10 |
| [OpenAI Codex CLI docs](https://developers.openai.com/codex/cli) | Codex can read, change, and run code locally. The learner must understand approvals, sandboxing, and review before accepting changes. | Lessons 2.2, 2.4, CLI variants |
| [Gemini CLI docs](https://google-gemini.github.io/gemini-cli/docs/) | Gemini CLI brings model, file, shell, web, memory, and MCP-style tools into a terminal workflow. Teach the same review loop, with tool-specific permissions. | Lessons 2.2, 4.3, CLI variants |

## Common failure modes

| Failure | What it looks like | Instructor move |
|---|---|---|
| Tool demo drift | Learner asks which model is best for everything | Bring it back to the slice, done check, and proof |
| Prompt theater | Learner keeps rewriting prompts without inspecting output | Stop and read the diff |
| Scope inflation | The project grows during the session | Cut to one local fixture and one command |
| Blind acceptance | Learner accepts changes because the agent sounds confident | Ask them to explain the diff and run proof |
| Context overload | The agent reads too much and loses the thread | Create a short project note and restart from the brief |
| No handoff | The work runs only in the learner's head | Write the decision and next step before ending |

## What good sounds like

Use this language in the room:

- "Show me the command that proves it."
- "What did the agent change?"
- "What would make you reject this?"
- "What is the next smallest slice?"
- "Where will future-you read this decision?"
- "Which part is workflow, which part is agent?"

That language is the curriculum.
