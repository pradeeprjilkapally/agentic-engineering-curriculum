# Lesson 6.7 · Discovery and scoping the engagement

**Where this gets you:** you'll be able to run a 3-7 day discovery sprint and produce a 1-page document that names the wedge, the constraints, and what done looks like. Before you write any code.

## The idea

Most failed engagements were scoped wrong on day 3. **Discovery** is the sprint that happens before any code, and it's the cheapest insurance you'll ever buy.

The output is one page that names six things:

1. **The wedge.** What's the smallest thing that, if it worked, would change the conversation?
2. **The constraints.** What can't you touch? What data can you use? What's the security posture?
3. **The success criteria.** How will we know it worked? Who decides?
4. **The timeline.** What does week 4 look like? Week 12?
5. **The team.** Who from the customer is in the room? Who's the executive sponsor?
6. **The unknowns.** What could you learn in week 1 that would change the plan?

**What skipping it costs.** You scope a support-triage agent in a kickoff call. Everyone nods. You build for three weeks and demo it. Then someone asks which ticket system it writes back to — and the write API is behind a month-long security review, and the VP who wanted this left in week 2. Nothing you built was wrong. It just wasn't scoped. A one-page doc on day 3 catches both, and those three weeks go to the read-only version that ships.

Five questions to ask in discovery conversations:

- What's the smallest thing that, if it worked, would change the conversation internally?
- Who decides whether it worked?
- What am I not allowed to touch?
- What data am I allowed to train on, retrieve from, write back to?
- What does success at month 3 look like from the executive's chair?

Four failure modes you're insuring against:

- **Scoped the project but not the customer.** Their priorities will shift. Budget time for it.
- **Scoped the engineering but not the politics.** Find the executive sponsor on day 1. If you can't name them by Friday, the engagement is at risk.
- **Scoped the timeline but not the data access.** Security review can eat four weeks. Start that conversation in week 1.
- **Scoped the outcome but not "done."** Write the eval before kickoff. Lesson 4.2 taught you this; in discovery you do it before any code exists.

The one page keeps you honest. If the wedge takes a page to describe, it's not a wedge. If the success criteria are vague, you didn't finish discovery.

## Your exercise

Pick a customer engagement, real or imagined. Write the one-page discovery doc. Cover all six sections. Keep it to one page.

**You're done when** a skeptical engineering leader could read it and say "this is buildable, and I know what done looks like."

**Practice proof:** save it as `discovery.md` in NOTES.

**Build on it:** a CLI that takes your `discovery.md` and flags every section with vague success criteria, no named decider, or an unbounded wedge.

## Why this matters

You'll be paid to know, on day one, what's possible in four weeks versus four months. Discovery is what makes that judgment accurate instead of fictional. The FDEs who get re-engaged are the ones whose discovery doc still held up at month 3.

---

Next: [Lesson 6.8 · Communicating to non-engineers](24-communicating-to-non-engineers.html)
