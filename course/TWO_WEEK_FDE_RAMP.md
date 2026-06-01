# Two-week FDE ramp

> A 10-day, ~80-hour structured path through all 32 lessons, designed for the case where you've blocked off real time and want to come out the other end ready to do Forward Deployed work. Use it for new-hire onboarding, your own focused ramp, or a candidate sprint. A compressed 5-day intensive variant for hiring-filter use is described at the end.

> The ramp is one way to use the curriculum. The other ways work too: a few evenings a week, a weekend project arc, the in-person workshop. Pick what fits.

## The premise

You ship code for a living. You may not have built with agents at depth, and that's fine. The foundations (Part 1) take less than a day and the workflow lessons land cleanly on top of any senior engineering background.

By end of day Friday in week two, you'll have shipped one real project end-to-end with agentic discipline AND installed the FDE-specific habits at real depth, not as sketches.

Two weeks instead of one because the Part 6 artifacts (security model, runbook, observability wiring, intel-watch live) get more honest when they have time to breathe.

## Week 1: Foundations, build, discipline (~40 hrs)

### Day 1: Foundations + setup (~8 hrs)

**Morning, ~4 hrs.** Lessons 1.1 to 1.5 (the AI map, LLMs just enough, what makes an agent, multimodality, the model zoo). Skim if you're AI-fluent; do every exercise if not.

**Afternoon, ~4 hrs.** Lessons 2.1 to 2.2 (what is agentic engineering, install your tool).

**End-of-day artifact:** `NOTES.md` with the Part 1 exercises completed and your first agent session log.

### Day 2: Take control + pick the project (~8 hrs)

Lessons 2.3 to 3.1 (your first session, staying in control, pick your first project). The project must be small enough to ship a slice this week and big enough to harden next week.

**End-of-day artifact:** project chosen, agent-loop sketch applied, project candidate file in `NOTES.md`.

### Day 3: Build something real (~8 hrs)

Lessons 3.2 to 3.4 (plan before build, build step by step, ship). Take the project to a shipped slice with a passing test by end of day.

**End-of-day artifact:** a shipped slice of the real project in git, with at least one passing test.

### Day 4: Brief and evals (~8 hrs)

Lessons 4.1 to 4.3 (the brief, evals defining done, context and the second brain). Apply each to the project.

**End-of-day artifact:** `CLAUDE.md`, an `evals/` directory with at least 5 evals, the brief document for the project.

### Day 5: Standards + week 1 retro (~8 hrs)

Lessons 4.4 to 4.5 (the no-slop standard, design discipline). Install both. End the week with a self-retro: what worked, what didn't, what to fix Monday.

**End-of-day artifact:** no-slop review pass wired, `DESIGN.md`, week-1 retro notes.

## Week 2: Scale, operate, hand off (~40 hrs)

### Day 6: Scale up (~8 hrs)

Lessons 5.1 to 5.3 (orchestration, review gates, where to go next). Run a piece of the project as parallel agents. Wire a real review gate.

**End-of-day artifact:** parallel orchestration applied to one part of the project, review gate live in CI or local pre-commit.

### Day 7: Harness fundamentals (~8 hrs)

Lessons 6.1 to 6.3 (harness wars, application taxonomy, coordinating with agents and humans). Audit the project's harness ownership. Add `AGENTS.md`, `HANDOFF.md`, `decisions/`. Populate with real content from your project, not placeholders.

**End-of-day artifact:** harness audit, `AGENTS.md`, `HANDOFF.md`, `decisions/0001-stack-choice.md`, `decisions/0002-model-routing.md`.

### Day 8: Staying current and reading the room (~8 hrs)

Lessons 6.4 to 6.6 (intel-watch, team shape, problems in every layer). Actually wire the intel-watch. Not a sketch. Get one alert firing on a real signal by end of day.

**End-of-day artifact:** working intel-watch with 5 voices + 3 projects, one real alert received and triaged, failure-mode-and-mitigation doc for the project.

### Day 9: The customer side (~8 hrs)

Lessons 6.7 to 6.9 (discovery + scoping, communicating to non-engineers, observability + cost). Write a realistic discovery doc for the project as if it were a customer engagement. Wire actual observability. At least one of the four axes live. Set a cost budget with an alert.

**End-of-day artifact:** `discovery.md`, weekly update template + one written example, one observability axis live, cost budget + alert.

### Day 10: Security, handoff, acceptance review (~8 hrs)

**Morning, ~4 hrs.** Lessons 6.10 to 6.11 (security and compliance, the handoff playbook). Write the security model. Draft the runbook and `future-you.md`.

**Afternoon, ~4 hrs.** End-of-week-two acceptance review with a peer or mentor. Walk through every artifact. Defend each one. Identify what would still need to happen for a real customer engagement next quarter.

**End-of-day artifact:** security model, runbook, `future-you.md`, peer review notes.

## End of Week 2: what you'll have built

By Friday at 5pm of week two, here's the artifact inventory you'll have on disk, ready to walk through with a peer or mentor in a relaxed 30-minute review:

- [ ] One real project shipped end-to-end with a passing test.
- [ ] `CLAUDE.md` (or `AGENTS.md`), `DESIGN.md`, `evals/` (5+ evals), no-slop review pass installed.
- [ ] `AGENTS.md`, `HANDOFF.md`, `decisions/` (at least 2 decisions) populated.
- [ ] Harness audit (`harness-audit.md`).
- [ ] Application classification (`application-taxonomy.md`).
- [ ] Personal intel-watch wired and live, at least one real alert received.
- [ ] Failure-mode-and-mitigation doc (`failures.md`).
- [ ] Discovery doc (`discovery.md`). One-page scope for a hypothetical or real engagement.
- [ ] Weekly update template (`weekly-template.md`) + one written example.
- [ ] Observability with at least one axis live + cost budget with alert.
- [ ] Security model (`security-model.md`).
- [ ] Runbook (`runbook.md`) and `future-you.md`.
- [ ] Peer review notes from the Day 10 walkthrough.

If you're using this as a hiring or onboarding milestone, a second-pass review of this list with a senior FDE is the natural conversation. If you're using it for your own growth, the list is your checkpoint. What you can point to, defend, and reuse on the next project.

## What two weeks gives you, and what it doesn't

Two weeks gives you a real, working operating system with depth. You'll be able to walk into your first FDE engagement with the habits, the templates, and the conventions already installed.

What two weeks doesn't give you (and nothing short of doing the work will) is the lived experience of a real customer team, the judgment that comes from shipping two or three engagements, and a network of trusted vendors and tools you've battle-tested in production. That's the next chapter, and it builds naturally on this one.

## Intensive 1-week variant (for hiring filters)

If you need a compressed hiring-filter cohort, you can run all 32 lessons in five days instead of ten. Each day takes a block from week 1 plus a block from week 2.

The 1-week intensive is a stress test of pattern matching and discipline. Artifacts will be rougher; the acceptance review will read more like a sketch review.

Recommendation: use the 2-week ramp as the default for **new-hire onboarding**, and use the 1-week intensive as a **second-round hiring filter** after a strong first-round technical interview. The 1-week version is not strong enough to make a first-round hiring decision on its own.

## Notes for facilitators

If you're running this as a hiring filter:

- Daily 30-minute check-ins land better over 2 weeks than 1.
- The Day-10 acceptance test is the actual hiring decision. Block 90 minutes for the review.
- A candidate who finishes nine of the thirteen checklist items at depth is in the hireable range with a normal post-hire ramp. Below nine usually means longer onboarding or a slightly different role fit. Not a failure.

If you're running this as your own onboarding:

- Schedule it. Don't try to fit it around customer work. Ramps work; squeezed ramps don't.
- Tell your team you're doing this. Public commitment lifts the completion rate.
- Pick a real project on Day 2. The whole ramp compounds on that choice.

---

The course is the operating system. This is the proper install procedure.

Back to [the course index](./curriculum.html).
