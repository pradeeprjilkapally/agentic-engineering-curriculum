# Agentic Engineering

A hands-on course for engineers who want to move from first agent session to shipped work they can review, prove, and hand off.

Pick one small, real project. Carry it through the lessons. Finish with a shipped slice and the habits that go with it.

**Read it as a site:** [aisoftllc.github.io/agentic-engineering-curriculum](https://aisoftllc.github.io/agentic-engineering-curriculum/)

**Prefer a room:** [Agentic Engineering Day](https://aisoft.us/workshop). The in-person workshop version.

## Start here

Pick the entry point that fits you.

- Fresh graduate or new to Git? → **[Beginner prep](course/BEGINNER_PREP.html)**. Git, terminal, and language basics before the CLI.
- New to AI? → **[Lesson 1.1: the AI map](course/00a-the-ai-map.html)**. 30 minutes to a clean mental model.
- Want the guided route? → **[Milestone path](course/MILESTONE_PATH.html)**. Step by step from orientation to handoff.
- Comfortable with the AI stack? → **[Lesson 2.1: what is agentic engineering](course/01-what-is-agentic-engineering.html)**. Start building.
- Want the full path? → **[The course index](curriculum.html)**.
- Have two focused weeks? → **[Two-week FDE ramp](course/TWO_WEEK_FDE_RAMP.html)**. A day-by-day structured plan toward Forward Deployed Engineer work.

32 lessons across 6 parts. Take them at the pace that works for you. A few evenings a week is fine.

## Who it's for

Engineers who can write code and want agents to become how they work. The widest sweet spot is **senior full-stack engineers from any background** (mobile, infra, frontend, backend, data, platform). You've shipped real software. The course meets you wherever you are with agents.

Fresh graduates can follow it too. Keep the project tiny and read every diff.

Claude Code is the main path. Codex CLI, Gemini CLI, and Snowflake Coco are covered as variants.

## More

- **[Course index](curriculum.html)** : the full lesson list.
- **[Milestone path](course/MILESTONE_PATH.html)** : the learner route with proof checkpoints.
- **[Beginner prep](course/BEGINNER_PREP.html)** : Git, terminal, and language basics for fresh graduates.
- **[Practice run guide](course/PRACTICE_RUN.html)** : how to run it for different audiences.
- **[Teaching guide](course/TEACHING_AGENTIC_ENGINEERING.html)** : instructor notes, external references, and room formats.
- **[CLI variants](course/CLI_VARIANTS.html)** : Claude Code, Codex, Gemini, Coco.
- **[30 practice labs](course/DATA_AI_LABS.html)** : SDLC, data, ML, AI apps, agentic workflows.
- **[Job pathways](course/JOB_PATHWAYS_AND_AISOFT_OFFERINGS.html)** : how labs map to roles and AISOFT offerings.

## Checks

Before pushing curriculum edits, run:

```bash
python3 scripts/check_links.py         # links that exist resolve
python3 scripts/check_lesson_shape.py  # every lesson has its required sections
python3 scripts/check_pages_build.py   # links still resolve after Jekyll builds
```

`check_links.py` checks local Markdown and HTML links, including generated `.html` pages and heading anchors. `check_pages_build.py` catches what it cannot see: a page with no YAML front matter is never rendered to `.html` by Jekyll, so the link resolves in the repo and 404s on the published site.

---

Maintained by [Ravinder Jilkapally](https://www.linkedin.com/in/jravinder/) · [AISOFT](https://aisoft.us) · [Free 30-min mentoring](https://aisoft.us/contact)
