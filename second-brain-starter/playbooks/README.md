# Playbooks

Step-by-step procedures for things you do repeatedly. The point: derive the procedure **once**, then reuse it — instead of re-explaining it to an agent every time.

## What belongs here

- Deploys and releases
- Incident / rollback procedures
- Environment setup
- Recurring multi-step tasks (data refreshes, report generation, audits)

## What does not

- One-off task detail → that's a brief
- Slow-changing project truth → that's `CLAUDE.md`
- Facts and decisions → that's `memory/`

## Format

Each playbook: **Trigger** (when it applies) · **Steps** (numbered, concrete) · **Definition of done** · **Anti-patterns** (the ways it goes wrong).

See [`deploy-verification.md`](deploy-verification.html) for the shape.

## Make them discoverable

Reference your playbooks from `CLAUDE.md` so the agent knows they exist and pulls the right one when a task matches.
