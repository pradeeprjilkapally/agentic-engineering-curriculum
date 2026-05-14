# The Curriculum

Eight modules. The order matters — each one assumes the scaffolding from the last. Budget roughly a week per module if you're doing it alongside real work; faster if you're full-time on it.

The test of each module is not "did you read it." It's "did you install the artifact and use it on real work." Reading this changes nothing. Building the scaffolding changes everything.

---

## Module 0 — Mindset: the multiplier

**The idea you have to internalize first:** agentic engineering accelerates *execution*. It does not give you vision, taste, or judgment. Those still come from you. Point an agent at a vague goal with no opinion about the outcome, and it will efficiently build you the average of everything it has seen. Average, shipped fast, is still average.

**Vibe coding is not agentic engineering.** Vibe coding is: prompt, glance, accept, move on — no spec, no eval, no definition of done beyond "it ran." It's great for throwaway prototypes and learning. It collapses the moment the work needs to survive real users. Agentic engineering is a discipline: briefs, evals, orchestration, review gates.

**Exercise:** take something you "vibe coded" recently. Write down, after the fact, what the brief *should* have been and what the eval *should* have checked. Notice the gap. That gap is the whole curriculum.

---

## Module 1 — The brief

A brief is a **contract, not a description**. It states the goal, the constraints, the input format, the output format, and the eval that defines done. A good brief takes about thirty seconds to write and produces 15–40 minutes of agent work you don't have to babysit.

The shift: you stop reviewing implementation choices ("class or function?") and start reviewing whether the *brief* was right and whether the *eval* caught what you needed.

**Install:** a brief template. Goal / Constraints / Inputs / Outputs / Eval / Out-of-scope. Use it for every non-trivial task for one week.

**Exercise:** write five briefs for real tasks. Hand them off. For each one that came back wrong, the bug is almost always in the brief — find it there, not in the code.

---

## Module 2 — Evals: defining done

If you can't describe what "working" means precisely enough to test, you're not ready to hand the work off. The slop you're about to get is yours, authored in advance.

The agent is not done when it returns. It's done when the eval is green *and* the taste check passes. Eval-first is not optional discipline — it's the thing that makes the other modules work.

**Install:** for each project, get evals first-class — CI integration, fast feedback, real test data (not fixtures that lie). Spend a week on this early; the compounding starts here.

**Exercise:** take a brief from Module 1. Before any code, write the eval. Then hand off brief + eval together. Compare the result to a hand-off with no eval.

---

## Module 3 — The no-slop standard

"Pay more attention" is useless advice. Attention has to be **encoded into an artifact the agent reads**. Slop is not a feeling — it's a list: dead code, unhandled errors, copy-paste duplication, vague names, untested edges, comments that restate the code.

**Install:** the [`no-slop-skill/`](no-slop-skill/) in this repo. It's a review pass the agent runs against its own output before handing it back. Customize the checklist to your stack and your taste.

**Exercise:** run the no-slop skill on your last three PRs. Count what it catches. That count is your baseline.

---

## Module 4 — Design discipline

For anything with a surface — UI, API, CLI, docs — design quality cannot live in your head. It lives in a spec the agent reads on every task: tokens, voice, layout rules, the things that make output look intentional instead of generated. Without it, every screen is a fresh roll of the dice.

**Install:** fork [`templates/DESIGN.md`](templates/DESIGN.md). Fill it in for one real project. Reference it in your `CLAUDE.md` so the agent picks it up automatically.

**Exercise:** generate the same component twice — once with `DESIGN.md` in context, once without. The difference is the module.

---

## Module 5 — The second brain

The single highest-leverage move: stop keeping context in your head, start building a second brain the agent can read. An agent is only as good as the context you can hand it. Every time you re-explain your architecture, conventions, past decisions, product voice — that's leverage leaking.

**Install:** the [`second-brain-starter/`](second-brain-starter/) — a `CLAUDE.md` skeleton, playbook stubs, and a memory structure. Write your context down once, in a form the agent picks up automatically.

**Exercise:** for one week, every time you explain something to an agent that you've explained before, stop and write it into the second brain instead. Watch month-three you start every task with the agent already knowing your stack, standards, and scars.

---

## Module 6 — Orchestration

Once briefs, evals, and scaffolding are solid, the bottleneck stops being lines-per-hour and becomes **orchestration discipline**: how many parallel work streams can you keep coherent? When a task has N independent pieces, you spawn N agents — not one serial chain.

A 2-person team running parallel agents on three streams beats a 5-person team running serial agents on one stream. The 5-person team *feels* productive. The 2-person team ships.

**Install:** a habit. Any task where you catch yourself writing "then do the next one" — stop, and ask whether those pieces are independent. Learn your tools' sub-agent and background-task primitives.

**Exercise:** take a multi-part task. Do it serially, time it. Do an equivalent one with parallel agents, time it. Then notice the *real* lesson: the hard part wasn't speed, it was keeping the parallel streams coherent.

---

## Module 7 — Review gates & shipping

The gate is where mediocre gets caught: tests green, design check, a human taste call on which of three implementations you keep. And shipping has its own discipline — **never claim done without proof.** "Deployed" is not a feeling; it's a verification you ran in the same breath.

**Install:** a definition-of-done gate for your projects. And a deploy-verification habit — see [`second-brain-starter/playbooks/deploy-verification.md`](second-brain-starter/playbooks/deploy-verification.md).

**Exercise:** for your next ship, write down the proof *before* you say the word "done" — the curl, the screenshot, the log line. If you can't name the proof, you're not done.

---

## Where this leaves you

When all eight are installed, your day looks different. It's not full of tickets — it's full of briefs. You're not reviewing implementation; you're reviewing eval design, orchestration design, and taste calls. That's higher-leverage work. It's also harder. You can't fake your way through eval design.

The first weeks feel slower — you're rebuilding habits and the muscle memory isn't there. By week four it's clearly faster. By week eight it's a different way of working.

It's a transition, not a tool installation. Plan accordingly.

---

## Graduated practice projects

Don't practice on toys — practice on things with real stakes, scaled down:

1. **Internal tool, well-bounded** — clean evals, no users to break. The agentic sweet spot. Build it brief-first, eval-first.
2. **Greenfield product, small surface** — now `DESIGN.md` matters. Ship it to five real users.
3. **A feature in an existing codebase** — now the second brain matters; the agent needs your conventions.
4. **A multi-stream build under time pressure** — a hackathon, or a self-imposed weekend. Now orchestration matters.

Log every one in [`lessons/`](lessons/).
