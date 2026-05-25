# DESIGN.md — [Project Name]

> Fork this. Fill every section. Reference it from `CLAUDE.md` so the agent reads it before any surface work.
>
> Delete this blockquote when you fork.

---

## What this is

One paragraph: what the product is, who it's for, and the single feeling the design should produce. Be concrete. "Calm, fast, trustworthy" beats "modern and clean."

## Voice

How the product *talks* — in UI copy, errors, empty states, docs.

- **Tone:** [e.g. direct, warm, no hype — short sentences]
- **Person:** [first person? second? "we" or "you"?]
- **Do:** [say "Couldn't save — check your connection"]
- **Don't:** [say "Oops! Something went wrong 😅"]
- **Reference:** [a product whose voice you'd want to be mistaken for]

## Color tokens

Define tokens, not one-off hex values. The agent should never invent a color.

| Token | Light | Dark | Use |
|-------|-------|------|-----|
| `--surface` | `#______` | `#______` | Page background |
| `--on-surface` | `#______` | `#______` | Primary text |
| `--primary` | `#______` | `#______` | Accent, CTAs |
| `--outline` | `#______` | `#______` | Borders, dividers |
| ... | | | |

Rule: no token, no new color without discussion.

## Type

- **Display / headings:** [font, weights, when to use]
- **Body:** [font, size, line-height]
- **Mono:** [font, where it's allowed]
- **Scale:** [the actual sizes — don't let the agent pick]

## Layout & spacing

- **Spacing scale:** [e.g. 4 / 8 / 16 / 24 / 32 / 64 — and nothing in between]
- **Max content width:** [e.g. 720px prose, 1180px app]
- **Grid:** [columns, gutters, breakpoints]
- **Radius / elevation:** [the allowed values]

## Components

For each recurring component, the rules the agent must follow. Add as you go.

- **Buttons:** [variants, sizes, when each is used, what's never allowed]
- **Cards:** [padding, border, hover behavior]
- **Forms:** [label position, error display, validation timing]
- **Empty states:** [must have: ...]

## Motion

- **Default transition:** [duration, easing]
- **What animates:** [and what must not]
- **Reduced-motion:** [the rule]

## Accessibility floor

Non-negotiable minimums:

- [ ] Contrast meets WCAG AA against its actual background
- [ ] Every interactive element is keyboard-reachable and has a visible focus state
- [ ] Images have meaningful `alt`; icons that carry meaning have labels
- [ ] Nothing conveys information by color alone
- [ ] Respects `prefers-reduced-motion`

## Anti-patterns — never ship these

The slop list, design edition. The agent checks output against this.

- [ ] Generic AI gradient-on-everything aesthetic
- [ ] Inconsistent spacing (values off the scale)
- [ ] Invented colors not in the token table
- [ ] Emoji in place of real iconography or real copy
- [ ] Centered walls of text
- [ ] Three font families where one would do
- [ ] [your project's specific ones]

---

**How to use:** check generated output against the token table, layout scale, and anti-pattern list. If something is not covered, fill the spec before delegating.
