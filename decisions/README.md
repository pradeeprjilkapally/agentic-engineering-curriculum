# Decisions

Architecture Decision Records (ADRs) — one file per change, filename
`YYYY-MM-DD-HHMM-<slug>.md`, newest by name.

## When a record is created
- **MCP servers** (tools connected to the app) added or removed: the
  `tooling_decision.py` hook detects the change against `.claude/.mcp_snapshot.json`
  and writes the record's factual skeleton automatically; the agent fills in
  Why / Impact / Alternatives.
- **Other external tools or infra** (CI, containers, IaC, launchd, deps, cloud
  config): the hook nudges the agent to author a record by hand, since only the
  agent has the rationale.

## Record shape
`# <title>` → `## What changed` → `## Why` → `## Impact` → `## Alternatives considered`.

`.claude/.mcp_snapshot.json` is the auto-managed MCP baseline (created on first
session) — do not edit it by hand. `.mcp_snapshot.json` and `memory.md` may hold
local context; gitignore them per repo if that context should stay off the remote.
