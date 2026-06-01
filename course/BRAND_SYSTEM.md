# AISOFT Agentic Engineering brand system

Working brand system for the curriculum, workshop, and job-pathways material.

Direction: **Stitch-style documentation**. Calm, precise, useful, built around people doing real work.

## Positioning

**AISOFT helps teams ship useful AI work with agentic engineering.**

| Signal | What it should communicate |
|---|---|
| Practical | Learners leave with repos, commands, diffs, checks, and proof. |
| Practical judgment | The material teaches review, gates, and delivery discipline. |
| In-person ready | The workshop should feel like a room where people build, review, and improve together. |

## Brand idea

**Clear work, visible proof.**

The work spans agents, data, SDLC, MLOps, AI apps, workflows, and leadership adoption. The brand should make it feel clear, teachable, and executable.

Use language that sounds like:

- "Here is the next step."
- "Here is the proof."
- "Here is what good looks like."
- "Here is how to recover when the agent drifts."

Avoid language that sounds like:

- "Unlock the future."
- "Revolutionize your workflow."
- "Magic AI productivity."
- "One guide to master everything."

## Visual System

### Palette

Use the blue/slate system for the curriculum.

| Token | Value | Use |
|---|---:|---|
| Primary | `#004ac6` | Links, active states, small emphasis |
| Primary strong | `#003996` | Hover and primary action states |
| Primary soft | `#dbe8ff` | Very light emphasis backgrounds |
| Surface | `#f7f9fb` | Page background outside docs surfaces |
| Surface low | `#f1f5f9` | Subtle panels and code backgrounds |
| Border | `#d9e2ef` | Dividers, tables, inputs, nav boundaries |
| Text | `#0f172a` | Primary text |
| Muted text | `#565e74` | Supporting copy |

Do not bring back the old warm curriculum palette. The logo can remain; the curriculum visual language is blue/slate.

### Typography

| Use | Font | Treatment |
|---|---|---|
| Headings | Geist | Strong, direct, no decorative tracking except small labels |
| Body | Inter | 16px baseline, generous line height |
| Code | JetBrains Mono / ui-monospace | Small, readable, copyable |

Headings should be plain and literal.

Good:

```text
Lesson 3.3 · Build it, step by step
Data + AI practice labs
Job pathways + AISOFT offerings
```

Avoid:

```text
Unlocking the Agentic Future
Your AI Transformation Starts Here
The Complete AI Playbook
```

### Layout

Use a documentation layout by default:

- left navigation,
- content column,
- optional right-side table of contents,
- minimal top navigation,
- no decorative hero section on lesson pages.

The page should open on the material. Brand shows through restraint, consistency, and useful structure.

### Components

| Component | Rule |
|---|---|
| Sidebar links | Flat text links with a blue left active border. No pill cards. |
| Code blocks | Border-led, light background, copy button, no heavy shadow. |
| Tables | Simple borders, compact rows, no marketing-card treatment. |
| Callouts | Use only when the learner needs a warning, decision, proof rule, or engineering judgment tip. |
| Buttons | Use sparingly. Prefer links in docs; reserve buttons for actual actions. |

## Documentation Patterns

### Engineering Judgment Tip

Use this when the learner needs judgment.

> **Engineering Judgment Tip**
>
> Optimize for readability over brevity. In agentic systems, the bottleneck is usually the human's ability to review, debug, and recover from the agent's choices.

### Stitched Progress

Use a thin blue left rule to show the active concept, lesson, or step. Keep inactive steps plain.

| State | Treatment |
|---|---|
| Active | Blue left rule, blue label, normal white background |
| Complete | Muted text with proof attached |
| Later | Muted text only; no decorative badge needed |

### Code Blocks

Every command should be copyable and readable without horizontal guessing.

```bash
git status --short
npm test
```

## Voice

Voice: a capable guide working beside the learner.

Write like this:

```text
Start with the smallest version. Run it on a fixture. Read the diff before you accept it.
```

Not like this:

```text
This module empowers you to harness agentic workflows for unparalleled productivity.
```

## Copy Rules

Use:

- short sentences,
- concrete nouns,
- commands,
- proof,
- small next steps,
- direct correction when needed.

Avoid:

- hype,
- vague transformation language,
- dramatic framing,
- meta explanations about the curriculum itself,
- long intros before the learner reaches the task.

## Workshop Feel

The in-person version should feel like a working room:

1. brief setup,
2. shared demo,
3. learner runs the agent,
4. diff review,
5. proof command,
6. next instruction.

Support that cadence. Make it easy to ask:

- What changed?
- How did you verify it?
- What would you ask the agent next?

## Reusable Copy

### One-line Description

```text
A practical agentic engineering curriculum for teams that need to brief, build, review, evaluate, and ship AI-assisted work.
```

### Workshop Description

```text
Agentic Engineering Day is an in-person workshop where learners use agents on real projects, review real diffs, run proof commands, and leave with a first-week adoption plan.
```

### Short CTA

```text
Bring a repo. Build one slice. Leave with proof.
```

### Quality Bar

```text
Do not call it done until the diff is read, the check has passed, and the proof is attached.
```

## Brand Checklist

Before publishing a new page, check:

1. Does the page start with the useful material?
2. Is the first task or decision visible quickly?
3. Are commands shown in copyable blocks?
4. Is the tone calm and specific?
5. Are there any marketing phrases that can be replaced with proof?
6. Does the page use blue/slate docs styling, not the old warm palette?
7. Would a fresh graduate and an experienced engineer both know what to do next?
