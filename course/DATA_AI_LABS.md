# Data + AI practice labs

These labs are modeled after small portfolio exercises like:

- `llm-data-profiling-tool`
- `snowflake-ai-integration`
- `ai-data-quality-agent`

They are intentionally small. Each one can be built by a fresh graduate with patience, and each one is still realistic enough for an experienced data engineer to practice agentic habits.

Use one lab as your course project, or run all three after Lesson 8 as extra practice.

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

For live workshops, use Lab 1 as the shared room exercise. It has the shortest path from zero to visible output.

