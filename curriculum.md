# Agentic Engineering — the course

A hands-on course for engineers who can already write code, and want coding agents to become how they work — not a thing they reach for now and then.

The catch: you won't learn this by reading it. You learn it by building. Early on you'll pick one small, real project, and carry it through every lesson — bolting on one new skill each time. Finish the course and you've got a real, shipped thing, plus the habits that made it good.

If you want the live version, AISOFT runs **Agentic Engineering Day** as an in-person workshop: one shared lab, live review, and a first-week rollout plan. Start here for the self-paced path; use the workshop when your team needs the room.

## How the course works

- **16 lessons, 4 parts.** Short to read, longer to do. Take them in order — each one stands on the last.
- **One project, the whole way through.** You pick it in Lesson 5. Every lesson after that puts the new skill to work on *your* project.
- **Every lesson ends with an exercise** and a plain "you're done when." The exercise is the actual lesson — reading without doing won't move you.
- **We teach Claude Code first, then translate.** Codex CLI, Gemini CLI, and Snowflake Coco get variant notes where the workflow changes. See [CLI variants](course/CLI_VARIANTS.md).

## Who can follow it

This is beginner-first, not beginner-only.

| Learner | How to run it |
|---|---|
| Fresh graduate | Keep the project tiny, do every exercise, and read every diff out loud before accepting it. |
| Experienced engineer | Move faster through setup, but do not skip planning, evals, review gates, or shipping proof. |
| Team lead | Run the course on one real team workflow, then turn the artifacts into team standards. |
| Live cohort | Use the shared lab first, then apply the same habit to each learner's project. |

For facilitation, use the [practice run guide](course/PRACTICE_RUN.md).

## The path

### Part 1 · Get set up
*From nothing installed to your first agent session.*

1. [What is agentic engineering?](course/01-what-is-agentic-engineering.md)
2. [Install your tool](course/02-install-your-tool.md)
3. Your first session — the core loop
4. Staying in control — review and permissions

### Part 2 · Build something real
*Pick a project and take it all the way to shipped.*

5. Pick your first project
6. Plan before you build
7. Build it, step by step
8. Ship it

### Part 3 · The core concepts
*The discipline that makes agent work hold up under real users.*

9. The brief — a contract, not a description
10. Evals — defining "done"
11. Context and the second brain
12. The no-slop standard
13. Design discipline

### Part 4 · Scale up
*From one agent to a way of working.*

14. Orchestration — parallel agents
15. Review gates and shipping
16. Where to go next

## What you'll walk away with

- A real project — built, shipped, and yours. Not a tutorial toy.
- The scaffolding installed on it and actually used: a `CLAUDE.md`, a `DESIGN.md`, an eval suite, a no-slop review pass.
- The habits: a brief before code, evals before you call it done, parallel work when the pieces are independent, and proof before you say "shipped."
- A tool-agnostic workflow you can run in Claude Code, Codex CLI, Gemini CLI, or Snowflake Coco.

## The artifacts

Three forkable starters back the course. You install each one during its lesson:

- [`no-slop-skill/`](no-slop-skill/) — a review pass the agent runs against its own output (Lesson 12).
- [`templates/DESIGN.md`](templates/DESIGN.md) — a design-quality spec for anything with a surface (Lesson 13).
- [`second-brain-starter/`](second-brain-starter/) — a `CLAUDE.md` skeleton and memory structure (Lesson 11).

---

Maintained by [Ravinder Jilkapally](https://www.linkedin.com/in/jravinder/) · [AISOFT](https://aisoft.us) · Mentoring: [book a free 30-min session](https://aisoft.us/contact)
