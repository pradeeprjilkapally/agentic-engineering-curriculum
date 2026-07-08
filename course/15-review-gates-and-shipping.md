# Lesson 5.2 · Review gates and shipping

**Where this gets you:** you'll put a real gate in front of your work, and ship the next change with proof, not a feeling.

## The idea

When agents run in parallel, more work arrives faster. So does mediocre work. A **review gate** is the fixed set of checks every change clears before it reaches users.

It isn't one check, it's a few, in order: tests green, the eval suite from Lesson 4.2, a design check, the no-slop pass and the DESIGN.md from Lessons 4.4 and 4.5. Then a human taste call — you look at the result, or two versions of it, and decide which one is good enough to keep. The agent runs the first checks. Only you make the last one.

Shipping has one rule: never claim done without proof.

Here's what that rule is for. You run `npm run deploy`. It prints a URL and exits 0. You tell the team it's live. Two days later someone asks why the button still says the old thing — the build succeeded, the upload went to a stale bucket, and nobody looked. One `curl -sL` against the live URL, grepping for the new text, would have caught it in four seconds. Instead you spent two days believing something false.

So "deployed" means verification in the same breath: a `curl` against the live URL, a production screenshot, or a fresh log line. If you can't point to proof, you ran a command and hoped.

## Do it

Before your next change to your project goes out, write the gate down. A practical gate has five checks:

1. The diff is small enough to review.
2. The stated goal matches the actual change.
3. The eval or test passed.
4. The no-slop review found no unresolved issues.
5. The shipping proof is attached.

Run them in that order. Nothing ships that skips a line. Decide your deploy proof *before* you run anything.

Use this gate as a command block and swap the test and deploy lines for your stack:

```bash
# 1. confirm the change is reviewable
git status --short
git diff --stat
git diff

# 2. run the project check
npm test
# or
pytest
# or
make test

# 3. deploy with your normal command
npm run deploy

# 4. prove the live surface changed
curl -sI https://your-live-url.example
curl -sL https://your-live-url.example | grep "text you expect to be live"
```

## Your exercise

Pick the next change you'll ship to your project. Before you touch the deploy command, write down the exact proof you'll use to confirm it landed. Actually write it. Name the specific `curl` you'll run, or the screenshot you'll take, or the log line you'll grep for.

Then ship it. Run that exact check. Only after it passes do you get to say the word "done."

**You're done when** you've shipped one change and pointed at concrete proof (a curl, a screenshot, a log line) that it's actually live.

**Practice proof:** run the gate on your project and write the result as `pass`, `fix needed`, or `blocked`, with the evidence.

**Build on it:** Write a `ship.sh` for your project that runs your tests, deploys, then curls the live URL for an expected string and exits non-zero if it's missing.

## Why this matters

The gate keeps quality from sliding as your throughput climbs. "Proof before done" keeps you honest. The first time you write the proof down and then watch a deploy silently fail, you'll understand why this rule exists — and you won't go back to guessing.

---

Previous: [Lesson 5.1 · Orchestration: parallel agents](14-orchestration-parallel-agents.html) · Next: [Lesson 5.3 · Where to go next](16-where-to-go-next.html)
