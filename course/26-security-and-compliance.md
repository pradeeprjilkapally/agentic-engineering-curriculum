# Lesson 6.10 · Security and compliance for AI products

**Where this gets you:** you'll be able to write a one-page security model for any agentic system on day one of an engagement, and pass a customer security review without needing a second meeting.

## The idea

Prompt injection is not a research topic. It is an attack vector. PII is not a buzzword. It is a contract.

Most AI products you'll ship into customer environments touch sensitive data and have contract or regulatory implications. The FDE who treats security as an afterthought gets bounced in week two. The one who treats it as a first-class concern from day one gets renewed.

The six things you need to know well enough to defend.

**1. Prompt injection.** Adversarial inputs that hijack the agent's intended behavior. Common in any system that ingests user-supplied text or web content. Mitigations: sandboxed tool execution, allow-listing the tool surface, output validation, no high-permission actions triggered by low-trust input. Treat any text from outside your control as untrusted.

**2. PII handling.** What can leave the customer's environment, and what cannot. Read the customer's Data Protection Agreement before you ship anything. For sensitive workloads, route through local models (Lesson 1.5) or add a redaction layer at the boundary.

**3. Data residency.** If the customer is EU, your model often cannot be a US-only API. Know the rules for the customer's geography. Have a fallback plan if the primary model isn't available in their region.

**4. Audit trail.** Every model call, with timestamp, redacted inputs, outputs, and outcome. Your eval suite contributes here. Your observability dashboard (Lesson 6.9) is half of it.

**5. Access control.** Who can invoke which agent. Who can read which brain page. Match the customer's existing role-based access controls; don't invent your own scheme.

**6. Vendor risk.** Every API you call is a vendor dependency the customer is now exposed to. Document them. Have a fallback for at least the critical ones. The harness-wars argument (Lesson 6.1) is a security argument as much as a strategic one.

The pattern: write a one-page security model on day one of any engagement. Get it signed off by the customer's security team before you ship anything that touches their data. Doing this in week one is cheap. Doing it after a leak is career-ending.

## Your exercise

Write the one-page security model for your project. Cover all six axes. Be honest about what's not yet mitigated.

**You're done when** a customer security reviewer could read it and not need a second meeting.

**Practice proof:** save as `security-model.md` in NOTES.

## Why this matters

Security is the foundation that decides whether you can ship at all. Not a hat you put on at the end. FDEs who think about it from day one are scarce, valued, and re-engaged, and since most interesting AI customers are in regulated industries (mortgage, healthcare, fintech), this habit unlocks a much bigger pool of work.

---

Next: [Lesson 6.11 · The handoff playbook](27-the-handoff-playbook.html)
