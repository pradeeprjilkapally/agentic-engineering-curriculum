# Job pathways + AISOFT offerings

Use this page to connect training work to job outcomes and AISOFT delivery.

The goal is proof that looks like real work: repos, READMEs, proof commands, review notes, and interview stories. The core skill is briefing, building, reviewing, evaluating, shipping, and explaining the result.

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

Use this sequence:

1. Pick the closest background path, not the fanciest project.
2. Pick one job target and one AISOFT offering match.
3. Choose one small lab that can run locally first.
4. Write the brief before any coding starts.
5. Build the smallest working version.
6. Add one proof command, one test, and one example output.
7. Improve the README until a hiring manager or client can understand the work in two minutes.
8. Write the interview story: what was the user problem, where did the agent help, what did the human review, and how was "done" proven?
9. Only then add the full version: Snowflake, API, dashboard, local model, deployment, or team workflow.

For in-person events, keep the first lab shared: brief, plan, build, review, test, proof. Then split by pathway.

## Pathways

### 1. Data engineering + analytics engineering

**Best fit:** learners who know SQL, pipelines, dbt, Snowflake, ETL, data modeling, or platform work.

**Job targets:** data engineer, analytics engineer, AI data engineer, Snowflake engineer, data platform engineer.

**AISOFT offering match:** AI Platform Design, AI Setup & Enablement, Local/Open Model deployment, AI Product Development.

**Start here:**

- [Lab 2 · Snowflake AI integration](DATA_AI_LABS.html#lab-2-snowflake-ai-integration)
- [Lab 4 · Pipeline run explainer](DATA_AI_LABS.html#lab-4-pipeline-run-explainer)
- [Lab 5 · dbt test generator](DATA_AI_LABS.html#lab-5-dbt-test-generator)
- [Lab 9 · Data contract checker](DATA_AI_LABS.html#lab-9-data-contract-checker)
- [Lab 16 · Spark job tuning assistant](DATA_AI_LABS.html#lab-16-spark-job-tuning-assistant)
- [Lab 17 · Streaming data monitor](DATA_AI_LABS.html#lab-17-streaming-data-monitor)

**Portfolio proof:**

- A repo that can run locally without credentials.
- A Snowflake or warehouse adapter behind config.
- Dry-run mode for safe queries.
- A generated data dictionary, validation rule, lineage note, or failed-run explanation.
- Tests for at least one deterministic transformation.

**Interview story:**

"I used an agent like a teammate, not autocomplete. I wrote the brief, made the data contract explicit, built the local version first, added tests, then connected it to Snowflake behind a safe configuration."

### 2. Big data + streaming

**Best fit:** learners working with Spark, Kafka, Databricks, lakehouse jobs, streaming pipelines, or high-volume batch processing.

**Job targets:** big data engineer, streaming data engineer, data platform engineer, lakehouse engineer.

**AISOFT offering match:** AI Platform Design, Edge AI, Local & Open Models, AI Setup & Enablement.

**Start here:**

- [Lab 16 · Spark job tuning assistant](DATA_AI_LABS.html#lab-16-spark-job-tuning-assistant)
- [Lab 17 · Streaming data monitor](DATA_AI_LABS.html#lab-17-streaming-data-monitor)
- [Lab 4 · Pipeline run explainer](DATA_AI_LABS.html#lab-4-pipeline-run-explainer)

**Portfolio proof:**

- Sample job metrics or event files.
- A report that cites bottlenecks or lag with evidence.
- Threshold config and replay/reproduce command.
- Tests for skew, schema drift, or lag behavior.

**Interview story:**

"I made large-scale data work reviewable. The tool reads job or stream evidence, explains what changed, and proposes safe next experiments instead of guessing."

### 3. Data analytics + BI

**Best fit:** learners from reporting, SQL analysis, business analysis, dashboards, KPI tracking, operations, or finance analytics.

**Job targets:** data analyst, BI analyst, analytics engineer, AI analyst, product analyst.

**AISOFT offering match:** AI Setup & Enablement, AI Product Development, internal tools, decision support workflows.

**Start here:**

- [Lab 1 · LLM data profiling tool](DATA_AI_LABS.html#lab-1-llm-data-profiling-tool)
- [Lab 6 · KPI narrative analyst](DATA_AI_LABS.html#lab-6-kpi-narrative-analyst)
- [Lab 7 · Dashboard QA assistant](DATA_AI_LABS.html#lab-7-dashboard-qa-assistant)
- [Lab 12 · CSV cleaning assistant](DATA_AI_LABS.html#lab-12-csv-cleaning-assistant)

**Portfolio proof:**

- Before/after sample data.
- A KPI narrative with source numbers included.
- Dashboard QA checks that catch at least three real issues.
- A README that explains how a business user would use the output.

**Interview story:**

"I did not just ask an LLM to summarize data. I made the source checks visible, kept the numbers traceable, and generated a narrative a stakeholder could review."

### 4. Data quality, governance, and responsible AI

**Best fit:** learners from QA, data governance, Collibra-style stewardship, metadata, compliance, lineage, PII, audit, or operations controls.

**Job targets:** data quality analyst, data governance analyst, AI governance analyst, data steward, risk/control analyst.

**AISOFT offering match:** AI Platform Design, Local LLMs, AI Setup & Enablement, governance-aware product development.

**Start here:**

- [Lab 3 · AI data quality agent](DATA_AI_LABS.html#lab-3-ai-data-quality-agent)
- [Lab 8 · PII policy scanner](DATA_AI_LABS.html#lab-8-pii-policy-scanner)
- [Lab 9 · Data contract checker](DATA_AI_LABS.html#lab-9-data-contract-checker)
- [Lesson 10 · Evals](10-evals-defining-done.html)

**Portfolio proof:**

- A policy file the tool reads.
- Sample data with seeded quality and PII issues.
- A report that separates deterministic findings from model-assisted notes.
- A review checklist for false positives and false negatives.

**Interview story:**

"I treated the model as an assistant inside a governed workflow. The policy was explicit, deterministic checks came first, and model output was reviewed before anything was called done."

### 5. Data science + experimentation

**Best fit:** learners from notebooks, exploratory analysis, experimentation, product analytics, applied statistics, or research workflows.

**Job targets:** data scientist, product data scientist, experimentation analyst, decision scientist.

**AISOFT offering match:** AI Product Development, AI Setup & Enablement, Startup Advisory.

**Start here:**

- [Lab 18 · Notebook insight reviewer](DATA_AI_LABS.html#lab-18-notebook-insight-reviewer)
- [Lab 19 · Experiment report generator](DATA_AI_LABS.html#lab-19-experiment-report-generator)
- [Lab 6 · KPI narrative analyst](DATA_AI_LABS.html#lab-6-kpi-narrative-analyst)

**Portfolio proof:**

- A notebook or experiment input with generated review.
- Numeric evidence tied to each conclusion.
- A report with caveats and a no-decision path when evidence is weak.
- Tests for winner/no-winner or unsupported conclusion logic.

**Interview story:**

"I used agents to improve the analysis process, not to invent conclusions. The tool checks evidence, caveats, and decision quality before a stakeholder sees the result."

### 6. ML + MLOps

**Best fit:** learners training models, evaluating prompts/models, deploying inference APIs, or monitoring production features.

**Job targets:** machine learning engineer, MLOps engineer, AI engineer, model platform engineer.

**AISOFT offering match:** AI Product Development, Local & Open Models, Edge AI, AI Platform Design.

**Start here:**

- [Lab 20 · Model eval harness](DATA_AI_LABS.html#lab-20-model-eval-harness)
- [Lab 21 · Feature drift monitor](DATA_AI_LABS.html#lab-21-feature-drift-monitor)
- [Lab 22 · ML inference API](DATA_AI_LABS.html#lab-22-ml-inference-api)

**Portfolio proof:**

- Versioned eval results.
- Feature drift report with thresholds.
- API contract with validation and tests.
- README that explains model/version tradeoffs.

**Interview story:**

"I treated model behavior as something to test and monitor. The work has evals, versioned results, drift checks, and an API contract instead of a model notebook alone."

### 7. AI app engineering

**Best fit:** learners building RAG, chat products, copilots, tool-calling workflows, or AI-backed internal tools.

**Job targets:** AI application engineer, RAG engineer, full-stack AI engineer, product engineer.

**AISOFT offering match:** AI Product Development, Full-Stack Engineering, Agentic Engineering, Local & Open Models.

**Start here:**

- [Lab 23 · RAG answer evaluator](DATA_AI_LABS.html#lab-23-rag-answer-evaluator)
- [Lab 24 · Tool-calling assistant](DATA_AI_LABS.html#lab-24-tool-calling-assistant)
- [Lab 11 · Support ticket routing service](DATA_AI_LABS.html#lab-11-support-ticket-routing-service)

**Portfolio proof:**

- Retrieval and answer quality evaluation.
- Tool schemas and audit trail.
- Refusal/unsupported request behavior.
- Tests for routing, citations, or groundedness.

**Interview story:**

"I built the AI feature with product controls: retrieval checks, tool-call logs, argument validation, and a clear path when the assistant should not act."

### 8. SDLC + DevOps

**Best fit:** learners working across requirements, tickets, tests, CI, release notes, incident summaries, or engineering operations.

**Job targets:** software engineer, DevOps engineer, QA automation engineer, release engineer, platform engineer.

**AISOFT offering match:** Agentic Engineering, AI Setup & Enablement, Full-Stack Engineering.

**Start here:**

- [Lab 25 · Story-to-test planner](DATA_AI_LABS.html#lab-25-story-to-test-planner)
- [Lab 26 · CI failure explainer](DATA_AI_LABS.html#lab-26-ci-failure-explainer)
- [Lab 27 · Release note generator](DATA_AI_LABS.html#lab-27-release-note-generator)
- [Lab 14 · Agentic PR reviewer](DATA_AI_LABS.html#lab-14-agentic-pr-reviewer)

**Portfolio proof:**

- Acceptance criteria and test plans generated from stories.
- CI summaries that include reproduce commands.
- Release notes with risk and verification sections.
- Tests for parser and grouping behavior.

**Interview story:**

"I applied agents across the software delivery lifecycle: clarifying stories, planning tests, explaining CI failures, reviewing PRs, and producing release notes with verification."

### 9. Backend, API, and internal tool engineering

**Best fit:** learners who build APIs, CLIs, automations, web apps, service integrations, or internal tools.

**Job targets:** backend engineer, AI app engineer, internal tools engineer, platform engineer, full-stack engineer.

**AISOFT offering match:** Full-Stack Engineering, AI Product Development, Agentic Engineering, Startup Advisory.

**Start here:**

- [Lab 10 · API log triage agent](DATA_AI_LABS.html#lab-10-api-log-triage-agent)
- [Lab 11 · Support ticket routing service](DATA_AI_LABS.html#lab-11-support-ticket-routing-service)
- [Lab 14 · Agentic PR reviewer](DATA_AI_LABS.html#lab-14-agentic-pr-reviewer)
- [Lesson 15 · Review gates and shipping](15-review-gates-and-shipping.html)

**Portfolio proof:**

- A CLI or API with clear inputs and outputs.
- Tests around routing, classification, or triage logic.
- A review gate that prevents low-confidence output from being treated as final.
- A deployment or run command someone else can execute.

**Interview story:**

"I used agents to accelerate implementation, but I controlled the contract. The service has tests, confidence thresholds, logs, and a clear handoff path when the model is unsure."

### 10. Agentic workflow engineering

**Best fit:** learners coordinating multi-agent work, creating memory/context files, and handing work between people and agents.

**Job targets:** agentic engineer, staff engineer, platform engineer, AI workflow engineer, technical lead.

**AISOFT offering match:** Agentic Engineering Day, AI Setup & Enablement, Startup Advisory, AI Platform Design.

**Start here:**

- [Lab 28 · Multi-agent task board](DATA_AI_LABS.html#lab-28-multi-agent-task-board)
- [Lab 29 · Agent memory curator](DATA_AI_LABS.html#lab-29-agent-memory-curator)
- [Lab 30 · Handoff packet generator](DATA_AI_LABS.html#lab-30-handoff-packet-generator)
- [Lesson 14 · Orchestration](14-orchestration-parallel-agents.html)

**Portfolio proof:**

- Agent-sized task board with dependencies and proof gates.
- Project memory files.
- Handoff packet with status, verification, risks, and next actions.
- A README explaining how the workflow prevents drift.

**Interview story:**

"I can coordinate agent work without losing control. The system splits tasks, preserves context, records proof, and makes handoff clear."

### 11. Fresh graduate portfolio path

**Best fit:** new graduates, career switchers, interns, and learners with light coding experience.

**Job targets:** junior data analyst, junior Python developer, AI support engineer, automation analyst, junior QA analyst.

**AISOFT offering match:** mentoring, open curriculum, workshop entry path, AI enablement readiness.

**Start here:**

- [Lab 12 · CSV cleaning assistant](DATA_AI_LABS.html#lab-12-csv-cleaning-assistant)
- [Lab 13 · Resume/project README improver](DATA_AI_LABS.html#lab-13-resumeproject-readme-improver)
- [Lab 1 · LLM data profiling tool](DATA_AI_LABS.html#lab-1-llm-data-profiling-tool)
- [Practice run guide](PRACTICE_RUN.html)

**Portfolio proof:**

- One tiny repo that runs.
- A clean README with setup, command, example input, and example output.
- Screenshots or copied terminal output showing the tool works.
- A short "what I learned" section that explains the agentic workflow.

**Interview story:**

"I kept the scope small and finished it. I wrote a brief, let the agent help, reviewed the diff, tested it, and can explain every file."

### 12. Team lead, manager, and CTO path

**Best fit:** leads who need adoption plans, standards, review gates, training plans, and real team rollout.

**Job targets:** lead engineer, engineering manager, AI transformation lead, staff engineer, startup CTO.

**AISOFT offering match:** Agentic Engineering Day, AI Setup & Enablement, Startup Advisory, AI Platform Design.

**Start here:**

- [Lab 14 · Agentic PR reviewer](DATA_AI_LABS.html#lab-14-agentic-pr-reviewer)
- [Lab 15 · Team runbook generator](DATA_AI_LABS.html#lab-15-team-runbook-generator)
- [Lab 28 · Multi-agent task board](DATA_AI_LABS.html#lab-28-multi-agent-task-board)
- [Lab 30 · Handoff packet generator](DATA_AI_LABS.html#lab-30-handoff-packet-generator)
- [Lesson 14 · Orchestration](14-orchestration-parallel-agents.html)
- [Lesson 16 · Where to go next](16-where-to-go-next.html)

**Portfolio proof:**

- A team `AGENTS.md` or `CLAUDE.md`.
- A review checklist.
- A rollout plan for one team workflow.
- A before/after measure: cycle time, review quality, defect rate, support time, or onboarding time.

**Interview story:**

"I did not just tell people to use AI. I defined where agents fit, what they are allowed to change, how we review, and how we know the workflow is producing better work."

### 13. Edge AI and local LLM path

**Best fit:** learners interested in private AI, low-latency inference, small models, Jetson/GB10/Mac deployments, or cost-controlled AI systems.

**Job targets:** edge AI engineer, local AI engineer, MLOps engineer, AI platform engineer, applied AI engineer.

**AISOFT offering match:** Edge AI, Local & Open Models, AI Platform Design.

**Start here:**

- [Lab 2 · Snowflake AI integration](DATA_AI_LABS.html#lab-2-snowflake-ai-integration), using local fixtures first.
- [Lab 3 · AI data quality agent](DATA_AI_LABS.html#lab-3-ai-data-quality-agent), with offline mode.
- [Lab 10 · API log triage agent](DATA_AI_LABS.html#lab-10-api-log-triage-agent), with a local model adapter.
- [Lab 22 · ML inference API](DATA_AI_LABS.html#lab-22-ml-inference-api), with local model serving.
- [Lab 24 · Tool-calling assistant](DATA_AI_LABS.html#lab-24-tool-calling-assistant), with local tools first.
- [CLI variants](CLI_VARIANTS.html), especially tool choice and environment differences.

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
| AI Product Development | Build usable AI features with specs, evals, review gates, and shipped proof | Labs 6, 10, 11, 20, 23, 24 |
| Edge AI / Local & Open Models | Separate model adapters, measure latency, keep data private where needed | Labs 2, 3, 10, 22, 24 |
| AI Platform Design | Data contracts, orchestration, deployment boundaries, governance | Labs 2, 5, 8, 9, 16, 17, 21, 28 |
| AI Setup & Enablement | Train teams to brief, review, test, and ship with agents | Labs 1, 12, 14, 15, 25, 26, 30 |
| Full-Stack Engineering | Turn AI workflows into tools users can run | Labs 10, 11, 13, 22, 23, 24 |
| Startup Advisory | Decide what to build first, what to defer, and how to prove traction | Labs 6, 11, 15, 19, 27, 28 |

## What every learner should leave with

Every path should produce the same base evidence:

1. A GitHub repo with a clear README.
2. A one-paragraph brief that explains the user, goal, constraints, and done condition.
3. A local run command.
4. At least one automated test or deterministic check.
5. Example input and output.
6. A short note on where an agent helped and where the human reviewed.
7. A short interview story that connects the project to a real job or AISOFT-style delivery.

That is the standard: proof, not "I used AI."
