# Teaching agentic engineering

This page is for instructors, mentors, team leads, and reviewers running the curriculum with a person or room. It keeps the teaching model clear so the course does not drift into a tool demo.

## The teaching promise

The learner should leave able to run this loop on real work:

1. Understand the problem and choose the smallest useful slice.
2. Write a brief with constraints, inputs, outputs, and a done check.
3. Let an agent explore, plan, and build in reviewable steps.
4. Verify with proof the learner can explain.
5. Capture the decision, handoff, and next slice.

The point is not to memorize one CLI. The point is to learn how to direct agentic work safely across Claude Code, Codex CLI, Gemini CLI, Coco, or whatever the team standardizes next.

## What the external references agree on

Use these as instructor anchors, not as extra reading homework.

| Reference | Teaching takeaway | Where it appears in this course |
|---|---|---|
| [Claude Code best practices](https://code.claude.com/docs/en/best-practices) | Give the agent a way to verify its work. Explore first, plan, then code. Manage context deliberately. | Lessons 3.2, 3.3, 4.2, 4.3, 5.2 |
| [Anthropic: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) | Start simple. Use workflows when the path is known, agents when the path is open-ended. Add complexity only when it improves outcomes. | Lessons 1.3, 6.2, 6.6 |
| [Anthropic: Writing effective tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents) | Tools need clear definitions, careful context, and evaluation-driven iteration. | Lessons 4.1, 4.2, 6.3, 6.10 |
| [OpenAI Codex CLI docs](https://developers.openai.com/codex/cli) | Codex can read, change, and run code locally. The learner must understand approvals, sandboxing, and review before accepting changes. | Lessons 2.2, 2.4, CLI variants |
| [Gemini CLI docs](https://google-gemini.github.io/gemini-cli/docs/) | Gemini CLI brings model, file, shell, web, memory, and MCP-style tools into a terminal workflow. Teach the same review loop, with tool-specific permissions. | Lessons 2.2, 4.3, CLI variants |

## The five instructor moves

### 1. Start with the smallest real thing

Do not let the learner begin with a platform rewrite. Pick one command, one route, one report, one broken test, one data fixture, or one support workflow. The work needs to be real enough to matter and small enough to finish.

Use [Data + AI practice labs](DATA_AI_LABS.html) when the learner does not bring a project.

### 2. Make the learner say the done check first

Before the agent edits files, ask:

- What output should exist?
- What command proves it?
- What failure would make you reject the result?
- What risk needs human review?

If the learner cannot answer, they are not ready to run the agent yet. Help them shrink the slice.

### 3. Stop at the diff

The most important classroom moment is not the prompt. It is the diff. Ask the learner to explain:

- what changed,
- why it changed,
- what they would keep,
- what they would reject,
- what proof exists.

If they cannot explain the diff, they do not own the work.

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

## Room formats

| Format | Best use | Structure |
|---|---|---|
| 30-minute mentoring | unblock one learner | choose slice, write brief, review plan, assign proof |
| 90-minute team session | introduce the method | shared demo, learner slice, diff review, team standard |
| 1-day workshop | install the workflow | morning control and briefs, afternoon evals, context, review gates, handoff |
| 2-week ramp | FDE readiness | all 32 lessons, one real project, Day-10 walkthrough |
| Hiring filter | second-round signal | 5-day intensive, daily proof, Friday artifact review |

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
