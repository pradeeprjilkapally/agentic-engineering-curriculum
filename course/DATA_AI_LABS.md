# Data + AI practice labs

These labs use small portfolio exercises as a guide for size and shape:

- `llm-data-profiling-tool`
- `snowflake-ai-integration`
- `ai-data-quality-agent`

Those examples are starting points, not boundaries. They show the level: small enough to finish, concrete enough to explain, and real enough to become portfolio proof. The training library expands across roles, domains, and AISOFT offerings.

Each lab is intentionally small. A fresh graduate should be able to build the small version with patience, and an experienced engineer should still find enough realism to practice agentic habits.

Use one lab as your course project, or run several after Lesson 8 as extra practice.

For career positioning, pair this page with [Job pathways + AISOFT offerings](JOB_PATHWAYS_AND_AISOFT_OFFERINGS.md). That guide maps the labs to job targets, interview stories, portfolio proof, and AISOFT's service lines.

## Coverage by work area

| Work area | Labs |
|---|---|
| SDLC + DevOps | Lab 14, Lab 25, Lab 26, Lab 27, Lab 30 |
| Data engineering | Lab 2, Lab 4, Lab 5, Lab 9 |
| Big data + streaming | Lab 16, Lab 17 |
| Analytics + BI | Lab 1, Lab 6, Lab 7 |
| Data quality + governance | Lab 3, Lab 8, Lab 9 |
| Data science | Lab 18, Lab 19 |
| ML + MLOps | Lab 20, Lab 21, Lab 22 |
| AI app engineering | Lab 11, Lab 23, Lab 24 |
| Backend/internal tools | Lab 10, Lab 11, Lab 22 |
| Agentic workflows | Lab 14, Lab 15, Lab 28, Lab 29, Lab 30 |
| Fresh-grad portfolio | Lab 12, Lab 13 |

## Pathways by background

| Pathway | Best for | Start with | Then try |
|---|---|---|---|
| Data engineering | ETL, Snowflake, dbt, pipelines, platform work | Lab 2 · Snowflake AI integration | Lab 4 · Pipeline run explainer, Lab 5 · dbt test generator |
| Big data + streaming | Spark, Kafka, batch/stream jobs, lakehouse work | Lab 16 · Spark job tuning assistant | Lab 17 · Streaming data monitor |
| Data analytics | BI, reporting, SQL, dashboards, business analysis | Lab 1 · LLM data profiling tool | Lab 6 · KPI narrative analyst, Lab 7 · Dashboard QA assistant |
| Data quality + governance | QA, data governance, Collibra-style stewardship, lineage | Lab 3 · AI data quality agent | Lab 8 · PII policy scanner, Lab 9 · Data contract checker |
| Data science | notebooks, experiments, exploratory analysis, stakeholder findings | Lab 18 · Notebook insight reviewer | Lab 19 · Experiment report generator |
| ML + MLOps | model training, evaluation, deployment, monitoring | Lab 20 · Model eval harness | Lab 21 · Feature drift monitor, Lab 22 · ML inference API |
| AI app engineering | RAG, chat apps, tool calling, prompt/version control | Lab 23 · RAG answer evaluator | Lab 24 · Tool-calling assistant |
| SDLC + DevOps | requirements, tickets, CI, tests, releases, incidents | Lab 25 · Story-to-test planner | Lab 26 · CI failure explainer, Lab 27 · Release note generator |
| Agentic workflows | multi-agent work, memory, orchestration, handoff | Lab 28 · Multi-agent task board | Lab 29 · Agent memory curator, Lab 30 · Handoff packet generator |
| Backend/app engineering | APIs, CLIs, internal tools, services | Lab 10 · API log triage agent | Lab 11 · Support ticket routing service |
| Fresh-grad portfolio | New engineers who need concrete GitHub projects | Lab 12 · CSV cleaning assistant | Lab 13 · Resume/project README improver |
| Team lead / manager | Standards, review gates, team adoption | Lab 14 · Agentic PR reviewer | Lab 15 · Team runbook generator |

Each lab has a **small version** that avoids paid services and credentials. Do that first. The full version can add Snowflake, LLM APIs, deployment, or alerts after the core behavior works locally.

## Quick chooser

If someone says:

- "I know SQL but not much Python" — start with Lab 6.
- "I work in Snowflake" — start with Lab 2.
- "I do data quality or governance" — start with Lab 3 or Lab 8.
- "I work with Spark, Kafka, or lakehouse jobs" — start with Lab 16 or Lab 17.
- "I do data science or notebooks" — start with Lab 18.
- "I train or deploy models" — start with Lab 20 or Lab 22.
- "I am building RAG or AI apps" — start with Lab 23 or Lab 24.
- "I work across SDLC, CI, releases, or incidents" — start with Lab 25, Lab 26, or Lab 27.
- "I want agentic workflow practice" — start with Lab 28 or Lab 30.
- "I am a fresh graduate" — start with Lab 12.
- "I build APIs" — start with Lab 10.
- "I manage a team adopting AI" — start with Lab 14 or Lab 15.

## Lab 1 · LLM data profiling tool

**Goal:** Given table metadata and a few sample rows, produce a data dictionary and suggested validation rules.

**Who it is for:** data analysts, data engineers, QA analysts, fresh graduates who know Python basics.

**Small version:** Use a local CSV instead of Snowflake.

**Full version:** Connect to Snowflake and profile a real table.

### Suggested structure

```text
llm-data-profiling-tool/
├── main.py
├── data/
│   └── customer_transactions.csv
├── profiler/
│   ├── schema_extractor.py
│   └── sample_reader.py
├── llm/
│   ├── prompt_templates.py
│   └── profiler_client.py
├── output/
│   ├── dictionary_writer.py
│   └── rule_exporter.py
└── tests/
    └── test_rule_exporter.py
```

### Step-by-step

1. Create a tiny CSV with 8-10 rows and obvious issues: nulls, invalid dates, negative amounts, duplicate IDs.
2. Ask the agent to inspect the CSV and propose a project plan.
3. Build `sample_reader.py` to load rows and infer basic types.
4. Build `schema_extractor.py` to summarize columns, null rates, examples, and suspicious values.
5. Write one prompt template that asks an LLM to explain business meaning and propose validation rules.
6. Add an offline mode that returns deterministic sample rules without calling an LLM.
7. Export a Markdown data dictionary.
8. Export validation rules as YAML or JSON.
9. Add a test for one rule export.
10. Run the tool and save the generated output.

### Practice proof

```bash
python main.py --csv data/customer_transactions.csv --output output/profile.md
python main.py --csv data/customer_transactions.csv --rules output/rules.yaml
```

Done means:

- the Markdown dictionary exists,
- the rules file exists,
- at least one test passes,
- the output flags at least one real issue in the sample data.

## Lab 2 · Snowflake AI integration

**Goal:** Run a query, summarize results, classify text rows, or narrate a trend.

**Who it is for:** data engineers, analytics engineers, Snowflake users, experienced engineers learning governed AI workflows.

**Small version:** Use local CSV fixtures.

**Full version:** Use Snowflake with approved credentials.

### Suggested structure

```text
snowflake-ai-integration/
├── main.py
├── config/
│   └── config.example.yaml
├── connectors/
│   ├── local_client.py
│   └── snowflake_client.py
├── pipelines/
│   ├── insight_generator.py
│   ├── classifier.py
│   └── trend_narrator.py
├── prompts/
│   └── prompt_templates.py
└── tests/
    └── test_classifier.py
```

### Step-by-step

1. Start with local CSV mode so the project works without credentials.
2. Add a CLI with three commands: `insight`, `classify`, and `trend`.
3. Implement `insight` against a local CSV: summarize row count, columns, and notable values.
4. Implement `classify`: assign each text row to one of the supplied labels.
5. Implement `trend`: group a date/value series and narrate direction.
6. Add prompt templates for the LLM version.
7. Add Snowflake connection code behind a config flag.
8. Add dry-run mode that prints the query and planned action before running it.
9. Add one test for label validation or trend calculation.
10. Write a README with safe credential setup.

### Practice proof

```bash
python main.py insight --csv data/kpi_daily.csv --context "Daily KPIs"
python main.py classify --csv data/support_tickets.csv --text-field description --labels billing technical account
python main.py trend --csv data/orders.csv --date-col order_date --value-col revenue --metric "Daily Revenue"
```

Done means:

- all three commands run on local fixtures,
- Snowflake credentials are never committed,
- the tool has dry-run mode,
- at least one behavior has a test.

## Lab 3 · AI data quality agent

**Goal:** Detect data quality issues, classify impact, and generate a human-readable scorecard.

**Who it is for:** QA analysts, data quality analysts, data engineers, governance teams.

**Small version:** Run checks on a local CSV.

**Full version:** Add Snowflake and alert routing.

### Suggested structure

```text
ai-data-quality-agent/
├── main.py
├── config/
│   └── config.example.yaml
├── profiler/
│   ├── schema_validator.py
│   ├── statistical_checks.py
│   └── lineage_mapper.py
├── agent/
│   ├── impact_classifier.py
│   └── prompt_templates.py
├── output/
│   ├── scorecard_generator.py
│   └── alert_router.py
└── tests/
    └── test_statistical_checks.py
```

### Step-by-step

1. Create a CSV with expected schema and a second CSV with broken rows.
2. Build schema checks: missing column, new column, wrong type.
3. Build statistical checks: null spike, duplicate IDs, out-of-range values.
4. Build an issue object with `name`, `severity`, `evidence`, and `suggested_owner`.
5. Add an impact classifier: Low, Medium, High.
6. Generate a Markdown scorecard.
7. Add alert routing as a stub that writes to `output/alerts.json`.
8. Add one test for each check family.
9. Ask the agent to run a no-slop pass.
10. Ship the result as a repo with sample output.

### Practice proof

```bash
python main.py --csv data/orders_bad.csv --expected-schema data/orders_schema.yaml --out output/scorecard.md
```

Done means:

- the scorecard lists each detected issue,
- every issue includes evidence,
- at least one high-impact issue is classified correctly,
- the test suite catches a broken check.

## Lab 4 · Pipeline run explainer

**Pathway:** Data engineering

**Goal:** Turn raw pipeline logs into a readable incident summary with failed step, likely cause, and next action.

**Small version:** Use sample log files in `data/logs/`.

**Full version:** Pull logs from Airflow, Dagster, dbt Cloud, GitHub Actions, or Snowflake task history.

### Suggested structure

```text
pipeline-run-explainer/
├── main.py
├── data/logs/
├── parser/
│   └── log_parser.py
├── analyzer/
│   ├── failure_classifier.py
│   └── summary_writer.py
└── tests/
    └── test_log_parser.py
```

### Step-by-step

1. Collect three fake logs: success, SQL failure, timeout.
2. Parse timestamps, step names, status, and error blocks.
3. Classify failures into `sql_error`, `dependency_down`, `timeout`, or `unknown`.
4. Generate a Markdown incident summary.
5. Add a `--since` or `--run-id` option.
6. Add one test for log parsing.

### Practice proof

```bash
python main.py --log data/logs/failed_sql.log --out output/incident.md
```

Done means the incident summary names the failed step, evidence, likely cause, and next action.

## Lab 5 · dbt test generator

**Pathway:** Data engineering

**Goal:** Read a dbt model SQL file and propose useful `schema.yml` tests.

**Small version:** Parse local `.sql` files.

**Full version:** Inspect a dbt project and write candidate tests into a review file.

### Step-by-step

1. Add two sample dbt model SQL files.
2. Extract selected columns and simple transformations.
3. Infer candidate tests: `not_null`, `unique`, `accepted_values`, relationships.
4. Write proposed YAML to `output/proposed_schema.yml`.
5. Add a review note explaining why each test was proposed.
6. Add one test for YAML generation.

### Practice proof

```bash
python main.py --model models/fct_orders.sql --out output/proposed_schema.yml
```

Done means the generated YAML is valid and every proposed test has a reason.

## Lab 6 · KPI narrative analyst

**Pathway:** Data analytics

**Goal:** Turn a weekly KPI CSV into a plain-English business summary.

**Small version:** Use local CSVs.

**Full version:** Connect to a BI export or Snowflake query.

### Step-by-step

1. Create a KPI CSV with date, metric, segment, value.
2. Compute week-over-week change.
3. Flag biggest movers.
4. Generate a short executive summary.
5. Generate a second analyst note with caveats.
6. Add a test for percent-change calculation.

### Practice proof

```bash
python main.py --csv data/weekly_kpis.csv --metric revenue --out output/kpi_summary.md
```

Done means the summary includes top movement, segment, numeric evidence, and caveat.

## Lab 7 · Dashboard QA assistant

**Pathway:** Data analytics

**Goal:** Compare dashboard numbers against source extracts and flag mismatches.

**Small version:** Compare two CSVs: `source.csv` and `dashboard.csv`.

**Full version:** Connect to BI export, semantic layer, or warehouse query.

### Step-by-step

1. Create source and dashboard CSVs with matching metric names.
2. Join by metric/date/segment.
3. Compute absolute and percentage difference.
4. Flag mismatches above tolerance.
5. Generate a QA report.
6. Add a test for tolerance behavior.

### Practice proof

```bash
python main.py --source data/source.csv --dashboard data/dashboard.csv --tolerance 0.01 --out output/dashboard_qa.md
```

Done means the report separates pass, warning, and fail metrics.

## Lab 8 · PII policy scanner

**Pathway:** Data quality + governance

**Goal:** Scan column names and sample values for possible PII, then generate a stewardship review file.

**Small version:** Use CSV headers and sample rows.

**Full version:** Connect to Snowflake information schema or a catalog export.

### Step-by-step

1. Create a CSV with fields like email, phone, customer_name, notes.
2. Add pattern checks for email, phone, SSN-like values.
3. Add name-based checks for sensitive columns.
4. Classify risk as Low, Medium, High.
5. Generate a stewardship review Markdown file.
6. Add allowlist/false-positive config.

### Practice proof

```bash
python main.py --csv data/customers.csv --out output/pii_review.md
```

Done means every flagged field has evidence and a suggested handling policy.

## Lab 9 · Data contract checker

**Pathway:** Data quality + governance

**Goal:** Compare an incoming file/table against a declared contract.

**Small version:** YAML contract plus CSV file.

**Full version:** Validate warehouse tables before pipeline runs.

### Step-by-step

1. Write a YAML contract: columns, types, required fields, allowed values.
2. Load an incoming CSV.
3. Check missing columns, extra columns, nulls, and invalid values.
4. Produce a pass/fail report.
5. Add an exit code: `0` for pass, non-zero for fail.
6. Add tests for one passing and one failing file.

### Practice proof

```bash
python main.py --contract contracts/orders.yaml --csv data/orders_incoming.csv
```

Done means the checker can block a bad file before it reaches a pipeline.

## Lab 10 · API log triage agent

**Pathway:** Backend/app engineering

**Goal:** Summarize API logs and group failures by endpoint, status code, and likely cause.

**Small version:** Use local JSONL logs.

**Full version:** Pull logs from CloudWatch, Datadog, GCP Logging, or app files.

### Step-by-step

1. Create sample JSONL logs with status, route, latency, message.
2. Group errors by route and status.
3. Detect latency spikes.
4. Generate a triage report.
5. Add a suggested owner field based on route prefix.
6. Add one test for grouping.

### Practice proof

```bash
python main.py --logs data/api_logs.jsonl --out output/triage.md
```

Done means the report names top failing routes and gives evidence.

## Lab 11 · Support ticket routing service

**Pathway:** Backend/app engineering

**Goal:** Classify support tickets and route them to the right queue.

**Small version:** CLI reads CSV and writes routed CSV.

**Full version:** Add a small FastAPI endpoint.

### Step-by-step

1. Create a ticket CSV with subject, description, customer tier.
2. Define route labels: billing, technical, account, bug, feature.
3. Build deterministic keyword routing first.
4. Add optional LLM routing behind a flag.
5. Write output CSV with label and confidence.
6. Add a test for at least three ticket examples.

### Practice proof

```bash
python main.py --tickets data/tickets.csv --out output/routed_tickets.csv
```

Done means every ticket has a route, reason, and confidence.

## Lab 12 · CSV cleaning assistant

**Pathway:** Fresh-grad portfolio

**Goal:** Build a friendly CLI that cleans a messy CSV and writes a cleaned file plus report.

**Small version:** Local CSV only.

**Full version:** Add a simple web UI.

### Step-by-step

1. Create a messy CSV: extra spaces, mixed casing, bad dates, duplicate rows.
2. Trim strings and normalize column names.
3. Parse dates and report failed rows.
4. Remove duplicates.
5. Write `clean.csv` and `cleaning_report.md`.
6. Add one test for duplicate removal.

### Practice proof

```bash
python main.py --csv data/messy_customers.csv --out output/clean_customers.csv --report output/cleaning_report.md
```

Done means the cleaned file and report are both created.

## Lab 13 · Resume/project README improver

**Pathway:** Fresh-grad portfolio

**Goal:** Turn a rough project README into a stronger portfolio README with setup, demo, screenshots, and proof.

**Small version:** Markdown in, Markdown out.

**Full version:** Add GitHub repo inspection.

### Step-by-step

1. Create a rough README.
2. Parse existing headings.
3. Detect missing sections: setup, usage, proof, limitations.
4. Generate an improved README draft.
5. Add a checklist of what still needs human input.
6. Add one test for missing-section detection.

### Practice proof

```bash
python main.py --readme README_rough.md --out README_improved.md
```

Done means the improved README is clearer but does not invent fake claims.

## Lab 14 · Agentic PR reviewer

**Pathway:** Team lead / manager

**Goal:** Review a diff against team standards and produce actionable findings.

**Small version:** Read a saved `.diff` file.

**Full version:** Pull PR diff from GitHub.

### Step-by-step

1. Create or save a small diff file.
2. Define review categories: bug risk, missing tests, scope creep, unclear naming.
3. Parse changed files.
4. Produce review findings with file, line, severity, and suggestion.
5. Add a no-findings path.
6. Add one test for detecting TODO/fake done.

### Practice proof

```bash
python main.py --diff data/sample.diff --out output/review.md
```

Done means findings are specific, grounded, and not generic advice.

## Lab 15 · Team runbook generator

**Pathway:** Team lead / manager

**Goal:** Convert scattered notes into a repeatable runbook for a recurring engineering task.

**Small version:** Local notes folder.

**Full version:** Pull from wiki/docs and create a PR.

### Step-by-step

1. Create three messy notes about deploy, rollback, and verification.
2. Extract steps, commands, owners, and warnings.
3. Generate a clean runbook.
4. Add a verification checklist.
5. Add a "when to stop and ask" section.
6. Add one test that required sections exist.

### Practice proof

```bash
python main.py --notes data/deploy_notes/ --out output/deploy_runbook.md
```

Done means the runbook is usable by someone who did not write the notes.

## Lab 16 · Spark job tuning assistant

**Pathway:** Big data + streaming

**Goal:** Read Spark job metrics and explain likely bottlenecks, skew, shuffle cost, and tuning options.

**Small version:** Use sample Spark event summaries as JSON.

**Full version:** Parse Spark event logs or Databricks job exports.

### Step-by-step

1. Create three sample job summaries: healthy, skewed join, excessive shuffle.
2. Parse stage duration, input rows, shuffle read/write, spill, and task skew.
3. Detect likely bottlenecks with deterministic rules first.
4. Generate a tuning report with evidence and safe next experiments.
5. Add a confidence field and "needs human review" flag.
6. Add one test for skew detection.

### Practice proof

```bash
python main.py --metrics data/spark_job_skew.json --out output/spark_tuning.md
```

Done means the report names the bottleneck, cites metrics, and proposes one safe experiment.

## Lab 17 · Streaming data monitor

**Pathway:** Big data + streaming

**Goal:** Detect lag, schema changes, and bad event spikes in a simulated stream.

**Small version:** Read timestamped JSONL events from a local folder.

**Full version:** Connect to Kafka, Kinesis, Pub/Sub, or Snowflake streams.

### Step-by-step

1. Create JSONL files for normal events, delayed events, and schema drift.
2. Track event time versus processing time.
3. Detect missing required fields and new unexpected fields.
4. Generate an alert summary with severity and evidence.
5. Add a replay command for the affected time window.
6. Add tests for lag and schema drift.

### Practice proof

```bash
python main.py --events data/stream/ --contract contracts/events.yaml --out output/stream_monitor.md
```

Done means lag, schema drift, and bad event spikes are separated in the report.

## Lab 18 · Notebook insight reviewer

**Pathway:** Data science

**Goal:** Review a notebook export for unclear assumptions, weak charts, missing caveats, and unsupported conclusions.

**Small version:** Read a Markdown or `.ipynb` export.

**Full version:** Inspect a notebook, generated figures, and source data profile.

### Step-by-step

1. Create a small notebook export with a chart, conclusion, and caveat.
2. Parse headings, code cells, chart captions, and markdown conclusions.
3. Check whether each conclusion has numeric evidence nearby.
4. Flag missing caveats, unclear filters, and chart-label issues.
5. Generate a review report.
6. Add one test for unsupported conclusion detection.

### Practice proof

```bash
python main.py --notebook notebooks/customer_churn.md --out output/notebook_review.md
```

Done means the review separates evidence issues from style suggestions.

## Lab 19 · Experiment report generator

**Pathway:** Data science

**Goal:** Turn experiment metrics into a stakeholder-ready report with winner, tradeoffs, and next experiment.

**Small version:** Use local CSV metrics from A/B or model experiments.

**Full version:** Pull from MLflow, W&B, Optuna, or warehouse tables.

### Step-by-step

1. Create an experiment CSV with variant, metric, segment, and confidence columns.
2. Compute winner by primary metric.
3. Identify segments where the winner is weaker.
4. Generate a short report with decision, risks, and next experiment.
5. Add a "not enough evidence" path.
6. Add tests for winner and no-winner cases.

### Practice proof

```bash
python main.py --metrics data/experiment_results.csv --primary conversion_rate --out output/experiment_report.md
```

Done means the report makes a decision only when the evidence supports it.

## Lab 20 · Model eval harness

**Pathway:** ML + MLOps

**Goal:** Build a repeatable eval harness for a classifier, extractor, or LLM response task.

**Small version:** Evaluate canned predictions against a labeled CSV.

**Full version:** Run a model or LLM client and write versioned eval results.

### Step-by-step

1. Create a labeled dataset with input, expected output, and difficulty.
2. Write exact-match and rubric-style scoring functions.
3. Add per-category metrics.
4. Save results with model name, prompt version, and timestamp.
5. Generate an eval summary with failure examples.
6. Add tests for scoring behavior.

### Practice proof

```bash
python main.py --cases data/eval_cases.csv --predictions data/predictions.csv --out output/eval_report.md
```

Done means the eval can compare two model or prompt versions without changing code.

## Lab 21 · Feature drift monitor

**Pathway:** ML + MLOps

**Goal:** Compare training and production feature distributions and flag drift.

**Small version:** Compare two CSV snapshots.

**Full version:** Read from feature store, warehouse, or model monitoring export.

### Step-by-step

1. Create training and production feature CSVs.
2. Compute null rate, mean/median, category frequency, and range changes.
3. Flag features above drift thresholds.
4. Generate a model-owner report with severity and suggested action.
5. Add config for thresholds.
6. Add tests for numeric and categorical drift.

### Practice proof

```bash
python main.py --train data/train_features.csv --prod data/prod_features.csv --out output/drift_report.md
```

Done means drift findings include evidence and avoid claiming model impact without proof.

## Lab 22 · ML inference API

**Pathway:** ML + MLOps

**Goal:** Wrap a simple model behind an API with validation, logging, and a testable prediction contract.

**Small version:** FastAPI app with a fake or scikit-learn model.

**Full version:** Add Docker, model version metadata, and deployment checks.

### Step-by-step

1. Define request and response schemas.
2. Add input validation and clear error messages.
3. Load a model artifact or deterministic stub.
4. Return prediction, confidence, and model version.
5. Log request metadata without sensitive fields.
6. Add API tests for success and validation failure.

### Practice proof

```bash
uvicorn app.main:app --reload
pytest
```

Done means the API has a stable contract and tests protect it.

## Lab 23 · RAG answer evaluator

**Pathway:** AI app engineering

**Goal:** Evaluate retrieved context and answer quality for a small RAG system.

**Small version:** Use local Markdown docs and canned answers.

**Full version:** Connect to a vector database and run live retrieval.

### Step-by-step

1. Create five small documents and ten questions.
2. Store expected source document IDs for each question.
3. Evaluate retrieval hit rate.
4. Score answers for groundedness and citation coverage.
5. Generate a failure report with examples.
6. Add tests for citation extraction.

### Practice proof

```bash
python main.py --questions data/questions.csv --answers data/answers.csv --out output/rag_eval.md
```

Done means the report separates retrieval failures from answer-generation failures.

## Lab 24 · Tool-calling assistant

**Pathway:** AI app engineering

**Goal:** Build an assistant that chooses between safe tools and records why each tool was called.

**Small version:** Local tools for calculator, CSV lookup, and note search.

**Full version:** Add authenticated business tools behind explicit approval.

### Step-by-step

1. Define three local tool schemas.
2. Create user requests that require zero, one, and multiple tools.
3. Add a router that selects the tool and validates arguments.
4. Log tool call, reason, result, and user-visible summary.
5. Add a refusal path for unsupported or risky requests.
6. Add tests for routing and argument validation.

### Practice proof

```bash
python main.py --request "Look up customer C-100 and summarize open balance"
```

Done means the assistant uses tools only when needed and leaves an audit trail.

## Lab 25 · Story-to-test planner

**Pathway:** SDLC + DevOps

**Goal:** Turn a product story into acceptance criteria and test cases before implementation.

**Small version:** Markdown story in, test plan out.

**Full version:** Pull tickets from Jira, Linear, GitHub Issues, or Azure DevOps.

### Step-by-step

1. Write three sample stories: clear, vague, and risky.
2. Extract user, goal, constraints, and missing information.
3. Generate acceptance criteria.
4. Generate unit, integration, and manual test ideas.
5. Add a "questions before build" section.
6. Add tests for missing-information detection.

### Practice proof

```bash
python main.py --story data/story.md --out output/test_plan.md
```

Done means vague stories produce questions instead of invented requirements.

## Lab 26 · CI failure explainer

**Pathway:** SDLC + DevOps

**Goal:** Summarize CI logs into failure cause, affected test, likely owner, and next command.

**Small version:** Use saved GitHub Actions logs.

**Full version:** Pull logs from GitHub Actions, GitLab CI, Jenkins, or Buildkite.

### Step-by-step

1. Save logs for lint failure, test failure, dependency failure, and timeout.
2. Parse command, exit code, failing file, and error block.
3. Classify failure type.
4. Generate a concise fix summary.
5. Add next command to reproduce locally.
6. Add tests for log parsing.

### Practice proof

```bash
python main.py --log data/ci_failed_test.log --out output/ci_summary.md
```

Done means a developer can reproduce the failure from the summary.

## Lab 27 · Release note generator

**Pathway:** SDLC + DevOps

**Goal:** Turn commits, PR titles, or issue notes into release notes with risk and verification sections.

**Small version:** Read a local changelog input file.

**Full version:** Pull merged PRs from GitHub and draft a release PR.

### Step-by-step

1. Create sample PR titles and commit messages.
2. Group changes by feature, fix, internal, and docs.
3. Identify migration or rollout notes.
4. Generate user-facing and internal release notes.
5. Add verification evidence placeholders.
6. Add tests for grouping behavior.

### Practice proof

```bash
python main.py --changes data/merged_prs.md --out output/release_notes.md
```

Done means the notes are useful without overstating what shipped.

## Lab 28 · Multi-agent task board

**Pathway:** Agentic workflows

**Goal:** Break a project into agent-sized tasks with dependencies, owners, and review gates.

**Small version:** Markdown brief in, task board out.

**Full version:** Create GitHub issues or Linear tickets with labels.

### Step-by-step

1. Write a project brief with three independent workstreams.
2. Extract deliverables, dependencies, and risks.
3. Split work into tasks suitable for parallel agents.
4. Add review gate and proof requirement for each task.
5. Generate a Markdown board.
6. Add a validation check for missing proof.

### Practice proof

```bash
python main.py --brief data/project_brief.md --out output/task_board.md
```

Done means tasks can be claimed independently without losing the overall goal.

## Lab 29 · Agent memory curator

**Pathway:** Agentic workflows

**Goal:** Convert scattered project notes into concise agent memory files.

**Small version:** Local notes folder to `AGENTS.md` plus topic files.

**Full version:** Pull from docs, issues, and previous handoffs.

### Step-by-step

1. Create messy notes about architecture, commands, decisions, and open questions.
2. Extract durable facts from temporary chatter.
3. Write `AGENTS.md` with commands, standards, and boundaries.
4. Write separate notes for architecture and deployment.
5. Add a stale-fact warning section.
6. Add a check that required sections exist.

### Practice proof

```bash
python main.py --notes data/project_notes/ --out output/memory/
```

Done means a new agent can start work without re-discovering basic project facts.

## Lab 30 · Handoff packet generator

**Pathway:** Agentic workflows

**Goal:** Create a handoff packet from git status, recent commits, open tasks, and verification notes.

**Small version:** Read local text fixtures.

**Full version:** Inspect a real repo and open PR.

### Step-by-step

1. Create fixtures for git status, commit log, TODOs, and test output.
2. Summarize what changed.
3. Separate done, in progress, blocked, and next actions.
4. Include verification commands and results.
5. Add risks and files touched.
6. Add tests for section completeness.

### Practice proof

```bash
python main.py --repo-fixture data/repo_state/ --out output/handoff.md
```

Done means another person or agent can continue without guessing the state.

## How to use these with the 16 lessons

| Course point | What to do with a lab |
|---|---|
| Lesson 1 | Pick two lab candidates and write done checks. |
| Lesson 5 | Choose one lab and cut scope to the small version. |
| Lesson 6 | Ask for a plan for the first slice only. |
| Lesson 7 | Build one module at a time. |
| Lesson 8 | Ship local proof: command output, sample files, README. |
| Lesson 10 | Add tests/checks for the critical behavior. |
| Lesson 11 | Add project instructions and safe credential rules. |
| Lesson 12 | Run no-slop against generated code. |
| Lesson 15 | Attach proof before saying shipped. |

## Instructor notes

For fresh graduates, start with local CSV mode. Snowflake and LLM credentials add too many failure modes for the first pass.

For experienced engineers, keep the same lab but raise the bar:

- config validation,
- dry-run mode,
- tests,
- structured output,
- credential safety,
- README with reproducible commands.

For live workshops, choose the shared room exercise by audience:

- mixed or beginner cohort: Lab 1 or Lab 12,
- engineering leaders: Lab 14, Lab 25, or Lab 30,
- data platform cohort: Lab 4, Lab 9, or Lab 16,
- AI product cohort: Lab 20, Lab 23, or Lab 24.

Use the smallest version first. The room should see one complete pass from brief to proof before splitting into deeper pathway work.
