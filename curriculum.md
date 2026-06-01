# Agentic Engineering

A hands-on course for engineers who can write code and want coding agents to become how they work.

Pick one small, real project. Carry it through the lessons. Finish with a shipped slice, proof commands, and the habits behind the work.

For teams, AISOFT runs **Agentic Engineering Day** as the in-person version: shared lab, live review, and a first-week rollout plan.

## How the course works

- **32 lessons, 6 parts.** Short to read, longer to do. Take them in order if you're new to agents; jump around if you already are.
- **One project, the whole way through.** You pick it in Lesson 5. Every lesson after that puts the new skill to work on *your* project. The project compounds; the lessons make sense because they land on it.
- **Every lesson ends with an exercise** and a plain "you're done when." Reading without doing won't move you, but the doing is the satisfying part. That's where the skill actually appears.
- **We teach Claude Code first, then translate.** Codex CLI, Gemini CLI, and Snowflake Coco get variant notes where the workflow changes. See [CLI variants](course/CLI_VARIANTS.html).
- **Where this leads.** If you want to take this all the way to Forward Deployed Engineer work (embedded with a customer, shipping agentic systems into their stack, handing them off cleanly), the [Two-week FDE ramp](course/TWO_WEEK_FDE_RAMP.html) is a structured day-by-day plan. FDE is a destination, not a prerequisite for starting.

## Who can follow it

This is beginner-first, not beginner-only.

| Learner | How to run it |
|---|---|
| Fresh graduate | Keep the project tiny, do every exercise, and read every diff out loud before accepting it. |
| Experienced engineer | Move faster through setup, but do not skip planning, evals, review gates, or shipping proof. |
| Team lead | Run the course on one real team workflow, then turn the artifacts into team standards. |
| Live cohort | Use the shared lab first, then apply the same habit to each learner's project. |

For facilitation, use the [practice run guide](course/PRACTICE_RUN.html).

For concrete projects, use the [Data + AI practice labs](course/DATA_AI_LABS.html): 30 exercises across SDLC, data engineering, big data, analytics, governance, data science, ML/MLOps, AI apps, backend, fresh-grad portfolio, team lead adoption, and agentic workflows.

For job-focused learners, use [Job pathways + AISOFT offerings](course/JOB_PATHWAYS_AND_AISOFT_OFFERINGS.html). It maps pathways to roles, portfolio proof, interview stories, and AISOFT service lines.

For page, slide, handout, or workshop copy, use the [AISOFT Agentic Engineering brand system](course/BRAND_SYSTEM.html).

## The path

### Part 0 · Foundations
*The conceptual stack you walk in with, so the workflow lessons land cleanly. Senior full-stack engineers from any background can skim quickly; nothing here assumes prior AI work.*

- 0.1 [The AI map](course/00a-the-ai-map.html)
- 0.2 [LLMs: just enough to be dangerous](course/00b-llms-just-enough.html)
- 0.3 [What makes an agent](course/00c-what-makes-an-agent.html)
- 0.4 [Multimodality](course/00d-multimodality.html)
- 0.5 [The model zoo](course/00e-the-model-zoo.html)

### Part 1 · Get set up
*From nothing installed to your first agent session.*

1. [What is agentic engineering?](course/01-what-is-agentic-engineering.html)
2. [Install your tool](course/02-install-your-tool.html)
3. Your first session
4. Staying in control

### Part 2 · Build something real
*Pick a project and take it all the way to shipped.*

5. Pick your first project
6. Plan before you build
7. Build it, step by step
8. Ship it

### Part 3 · The core concepts
*The discipline that makes agent work hold up under real users.*

9. The brief
10. Evals
11. Context and the second brain
12. The no-slop standard
13. Design discipline

### Part 4 · Scale up
*From one agent to a way of working.*

14. Orchestration
15. Review gates and shipping
16. Where to go next

### Part 5 · Operating in the real world
*The envelope you walk out with. The six lessons that turn a working agent engineer into a Forward Deployed Engineer.*

- 17. [The harness wars](course/17-the-harness-wars.html)
- 18. [The application taxonomy](course/18-application-taxonomy.html)
- 19. [Coordinating with agents and humans](course/19-coordinating-team.html)
- 20. [Staying current: the intel-watch pattern](course/20-staying-current-intel-watch.html)
- 21. [The team shape](course/21-team-shape.html)
- 22. [The problems in every layer](course/22-problems-in-every-layer.html)
- 23. [Discovery and scoping the engagement](course/23-discovery-and-scoping.html)
- 24. [Communicating to non-engineers](course/24-communicating-to-non-engineers.html)
- 25. [Observability and cost discipline](course/25-observability-and-cost.html)
- 26. [Security and compliance for AI products](course/26-security-and-compliance.html)
- 27. [The handoff playbook](course/27-the-handoff-playbook.html)

## What you'll walk away with

- A real project, built, shipped, and yours. Not a tutorial toy.
- The scaffolding installed on it and actually used: a `CLAUDE.md` (or `AGENTS.md`), a `DESIGN.md`, an eval suite, a no-slop review pass, a `HANDOFF.md`, and a `decisions/` log.
- The habits: a brief before code, evals before you call it done, parallel work when the pieces are independent, and proof before you say "shipped."
- A tool-agnostic workflow you can run in Claude Code, Codex CLI, Gemini CLI, or Snowflake Coco.
- A working personal intel-watch so you stay current on the people whose signal matters, without doom-scrolling.
- The operating mode of a Forward Deployed Engineer: walking into a customer's stack, scoping, building, shipping with proof, and handing off cleanly.

## The artifacts

Three forkable starters back the course. You install each one during its lesson:

- [`no-slop-skill/`](no-slop-skill/): a review pass the agent runs against its own output (Lesson 12).
- [`templates/DESIGN.md`](templates/DESIGN.html): a design-quality spec for anything with a surface (Lesson 13).
- [`second-brain-starter/`](second-brain-starter/): a `CLAUDE.md` skeleton and memory structure (Lesson 11).

---

Maintained by [Ravinder Jilkapally](https://www.linkedin.com/in/jravinder/) · [AISOFT](https://aisoft.us) · Mentoring: [book a free 30-min session](https://aisoft.us/contact)
