# Job pathways + AISOFT offerings

This guide connects the training to job outcomes and to the actual work AISOFT sells.

The promise is not "finish a bootcamp, get a job." The promise is better and more honest: build proof that looks like real work. Every learner should leave with GitHub repos, READMEs, proof commands, review notes, and interview stories that map to the kind of work companies now need.

AISOFT's own positioning is the model: small teams can ship serious AI products when they use agents well. The skill is not just prompting. It is briefing, building, reviewing, evaluating, shipping, and explaining the result.

## The training ladder

| Stage | Learner outcome | AISOFT offering it supports |
|---|---|---|
| Open curriculum | Learn the agentic engineering loop and ship one small project | Community education, mentoring, hiring pipeline |
| Data + AI labs | Build portfolio proof in a domain path | AI setup, AI product development, data AI enablement |
| Agentic Engineering Day | Practice the workflow live with review in the room | In-person enablement workshop |
| Team rollout | Turn briefs, evals, review gates, and context files into team standards | AI setup + enablement, platform design |
| Build sprint | Apply agents to a real backlog, workflow, data product, or internal tool | AI product development, full-stack engineering |
| Architecture/advisory | Decide what should run in cloud, warehouse, edge, or local model form | AI platform design, local LLMs, edge AI, startup advisory |

## How to use this in training

Use this sequence for every learner or event:

1. Pick the closest background path, not the fanciest project.
2. Pick one job target and one AISOFT offering match.
3. Choose one small lab that can run locally first.
4. Write the brief before any coding starts.
5. Build the smallest working version.
6. Add one proof command, one test, and one example output.
7. Improve the README until a hiring manager or client can understand the work in two minutes.
8. Write the interview story: what was the user problem, where did the agent help, what did the human review, and how was "done" proven?
9. Only then add the full version: Snowflake, API, dashboard, local model, deployment, or team workflow.

For in-person events, keep the first lab shared. The room should see one complete pass: brief, plan, build, review, test, ship proof. After that, split by pathway.

## Pathways

### 1. Data engineering + analytics engineering

**Best fit:** learners who know SQL, pipelines, dbt, Snowflake, ETL, data modeling, or platform work.

**Job targets:** data engineer, analytics engineer, AI data engineer, Snowflake engineer, data platform engineer.

**AISOFT offering match:** AI Platform Design, AI Setup & Enablement, Local/Open Model deployment, AI Product Development.

**Start here:**

- [Lab 2 · Snowflake AI integration](DATA_AI_LABS.md#lab-2-snowflake-ai-integration)
- [Lab 4 · Pipeline run explainer](DATA_AI_LABS.md#lab-4-pipeline-run-explainer)
- [Lab 5 · dbt test generator](DATA_AI_LABS.md#lab-5-dbt-test-generator)
- [Lab 9 · Data contract checker](DATA_AI_LABS.md#lab-9-data-contract-checker)

**Portfolio proof:**

- A repo that can run locally without credentials.
- A Snowflake or warehouse adapter behind config.
- Dry-run mode for safe queries.
- A generated data dictionary, validation rule, lineage note, or failed-run explanation.
- Tests for at least one deterministic transformation.

**Interview story:**

"I used an agent like a teammate, not autocomplete. I wrote the brief, made the data contract explicit, built the local version first, added tests, then connected it to Snowflake behind a safe configuration."

### 2. Data analytics + BI

**Best fit:** learners from reporting, SQL analysis, business analysis, dashboards, KPI tracking, operations, or finance analytics.

**Job targets:** data analyst, BI analyst, analytics engineer, AI analyst, product analyst.

**AISOFT offering match:** AI Setup & Enablement, AI Product Development, internal tools, decision support workflows.

**Start here:**

- [Lab 1 · LLM data profiling tool](DATA_AI_LABS.md#lab-1-llm-data-profiling-tool)
- [Lab 6 · KPI narrative analyst](DATA_AI_LABS.md#lab-6-kpi-narrative-analyst)
- [Lab 7 · Dashboard QA assistant](DATA_AI_LABS.md#lab-7-dashboard-qa-assistant)
- [Lab 12 · CSV cleaning assistant](DATA_AI_LABS.md#lab-12-csv-cleaning-assistant)

**Portfolio proof:**

- Before/after sample data.
- A KPI narrative with source numbers included.
- Dashboard QA checks that catch at least three real issues.
- A README that explains how a business user would use the output.

**Interview story:**

"I did not just ask an LLM to summarize data. I made the source checks visible, kept the numbers traceable, and generated a narrative a stakeholder could review."

### 3. Data quality, governance, and responsible AI

**Best fit:** learners from QA, data governance, Collibra-style stewardship, metadata, compliance, lineage, PII, audit, or operations controls.

**Job targets:** data quality analyst, data governance analyst, AI governance analyst, data steward, risk/control analyst.

**AISOFT offering match:** AI Platform Design, Local LLMs, AI Setup & Enablement, governance-aware product development.

**Start here:**

- [Lab 3 · AI data quality agent](DATA_AI_LABS.md#lab-3-ai-data-quality-agent)
- [Lab 8 · PII policy scanner](DATA_AI_LABS.md#lab-8-pii-policy-scanner)
- [Lab 9 · Data contract checker](DATA_AI_LABS.md#lab-9-data-contract-checker)
- [Lesson 10 · Evals](10-evals-defining-done.md)

**Portfolio proof:**

- A policy file the tool reads.
- Sample data with seeded quality and PII issues.
- A report that separates deterministic findings from model-assisted notes.
- A review checklist for false positives and false negatives.

**Interview story:**

"I treated the model as an assistant inside a governed workflow. The policy was explicit, deterministic checks came first, and model output was reviewed before anything was called done."

### 4. Backend, API, and internal tool engineering

**Best fit:** learners who build APIs, CLIs, automations, web apps, service integrations, or internal tools.

**Job targets:** backend engineer, AI app engineer, internal tools engineer, platform engineer, full-stack engineer.

**AISOFT offering match:** Full-Stack Engineering, AI Product Development, Agentic Engineering, Startup Advisory.

**Start here:**

- [Lab 10 · API log triage agent](DATA_AI_LABS.md#lab-10-api-log-triage-agent)
- [Lab 11 · Support ticket routing service](DATA_AI_LABS.md#lab-11-support-ticket-routing-service)
- [Lab 14 · Agentic PR reviewer](DATA_AI_LABS.md#lab-14-agentic-pr-reviewer)
- [Lesson 15 · Review gates and shipping](15-review-gates-and-shipping.md)

**Portfolio proof:**

- A CLI or API with clear inputs and outputs.
- Tests around routing, classification, or triage logic.
- A review gate that prevents low-confidence output from being treated as final.
- A deployment or run command someone else can execute.

**Interview story:**

"I used agents to accelerate implementation, but I controlled the contract. The service has tests, confidence thresholds, logs, and a clear handoff path when the model is unsure."

### 5. Fresh graduate portfolio path

**Best fit:** new graduates, career switchers, interns, and learners with light coding experience.

**Job targets:** junior data analyst, junior Python developer, AI support engineer, automation analyst, junior QA analyst.

**AISOFT offering match:** mentoring, open curriculum, workshop entry path, AI enablement readiness.

**Start here:**

- [Lab 12 · CSV cleaning assistant](DATA_AI_LABS.md#lab-12-csv-cleaning-assistant)
- [Lab 13 · Resume/project README improver](DATA_AI_LABS.md#lab-13-resumeproject-readme-improver)
- [Lab 1 · LLM data profiling tool](DATA_AI_LABS.md#lab-1-llm-data-profiling-tool)
- [Practice run guide](PRACTICE_RUN.md)

**Portfolio proof:**

- One tiny repo that runs.
- A clean README with setup, command, example input, and example output.
- Screenshots or copied terminal output showing the tool works.
- A short "what I learned" section that explains the agentic workflow.

**Interview story:**

"I kept the scope small and finished it. I wrote a brief, let the agent help, reviewed the diff, tested it, and can explain every file."

### 6. Team lead, manager, and CTO path

**Best fit:** leads who need adoption plans, standards, review gates, training plans, and real team rollout.

**Job targets:** lead engineer, engineering manager, AI transformation lead, staff engineer, startup CTO.

**AISOFT offering match:** Agentic Engineering Day, AI Setup & Enablement, Startup Advisory, AI Platform Design.

**Start here:**

- [Lab 14 · Agentic PR reviewer](DATA_AI_LABS.md#lab-14-agentic-pr-reviewer)
- [Lab 15 · Team runbook generator](DATA_AI_LABS.md#lab-15-team-runbook-generator)
- [Lesson 14 · Orchestration](14-orchestration-parallel-agents.md)
- [Lesson 16 · Where to go next](16-where-to-go-next.md)

**Portfolio proof:**

- A team `AGENTS.md` or `CLAUDE.md`.
- A review checklist.
- A rollout plan for one team workflow.
- A before/after measure: cycle time, review quality, defect rate, support time, or onboarding time.

**Interview story:**

"I did not just tell people to use AI. I defined where agents fit, what they are allowed to change, how we review, and how we know the workflow is producing better work."

### 7. Edge AI and local LLM path

**Best fit:** learners interested in private AI, low-latency inference, small models, Jetson/GB10/Mac deployments, or cost-controlled AI systems.

**Job targets:** edge AI engineer, local AI engineer, MLOps engineer, AI platform engineer, applied AI engineer.

**AISOFT offering match:** Edge AI, Local & Open Models, AI Platform Design.

**Start here:**

- [Lab 2 · Snowflake AI integration](DATA_AI_LABS.md#lab-2-snowflake-ai-integration), using local fixtures first.
- [Lab 3 · AI data quality agent](DATA_AI_LABS.md#lab-3-ai-data-quality-agent), with offline mode.
- [Lab 10 · API log triage agent](DATA_AI_LABS.md#lab-10-api-log-triage-agent), with a local model adapter.
- [CLI variants](CLI_VARIANTS.md), especially tool choice and environment differences.

**Portfolio proof:**

- A model adapter interface with cloud and local implementations.
- Offline or deterministic fallback behavior.
- Latency and cost notes in the README.
- A clear reason why local inference is useful for this use case.

**Interview story:**

"I separated the product behavior from the model provider. That let me run the small version locally, compare tradeoffs, and decide when cloud, warehouse, or edge inference made sense."

## Offer-to-lab map

| AISOFT offering | Training focus | Best labs |
|---|---|---|
| AI Product Development | Build usable AI features with specs, evals, review gates, and shipped proof | Labs 6, 10, 11, 14 |
| Edge AI / Local & Open Models | Separate model adapters, measure latency, keep data private where needed | Labs 2, 3, 10 |
| AI Platform Design | Data contracts, orchestration, deployment boundaries, governance | Labs 2, 5, 8, 9, 15 |
| AI Setup & Enablement | Train teams to brief, review, test, and ship with agents | Labs 1, 12, 14, 15 |
| Full-Stack Engineering | Turn AI workflows into tools users can run | Labs 10, 11, 13 |
| Startup Advisory | Decide what to build first, what to defer, and how to prove traction | Labs 6, 11, 15 |

## What every learner should leave with

Every path should produce the same base evidence:

1. A GitHub repo with a clear README.
2. A one-paragraph brief that explains the user, goal, constraints, and done condition.
3. A local run command.
4. At least one automated test or deterministic check.
5. Example input and output.
6. A short note on where an agent helped and where the human reviewed.
7. A short interview story that connects the project to a real job or AISOFT-style delivery.

That is the standard. Not "I used AI." Proof.
