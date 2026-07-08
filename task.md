# Tasks

## 01-080726 · Simplify curriculum + add real images (PILOT)

- **Date:** 2026-07-08
- **Status:** In progress
- **Task:** De-slop and simplify curriculum content; add real-life examples and real
  (non-AI) images to each scenario. Pilot on 2–3 lessons first, get sign-off, then roll out.
- **Goal:** Lessons readable by a non-expert. Every scenario has a concrete real-life
  example. Imagery = hand-authored SVG diagrams + real stock photos + real terminal
  screenshots. No important curriculum content lost.
- **Constraints:** Keep the mandated 8-part lesson shape (AGENTS.md). Feature branch, no
  push to main. Images must be real/non-AI (SVG diagrams, downloaded CC0 stock, captured
  terminal output). Run `scripts/check_links.py` before any PR.
- **Inputs:** course/*.md, assets/style.css, _layouts/docs.html, index.html.
- **Outputs:** Transformed pilot lessons, committed image assets, a local rendered preview
  the user can open in a browser.
- **Done-check:** 3 pilot lessons transformed + rendered locally with images showing;
  user approves the style before rollout.
- **Out-of-scope (pilot):** The other ~37 files. Rolled out after sign-off.
