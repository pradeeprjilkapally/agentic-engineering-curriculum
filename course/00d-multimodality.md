# Lesson 1.4 · Multimodality

**Where this gets you:** you'll know when reaching for vision, voice, or video is the right move on a customer project and when text is still the better answer.

## The idea

A **modality** is the kind of input or output a model works in: text, images, audio, video. Voice was never bottlenecked by audio quality. It was bottlenecked by intelligence. Vision the same. So knowing when to reach for a modality beats knowing every model that supports one.

Four are worth knowing today.

**Text.** Still the default. Still the winner for most tasks. Cheap, fast, well-understood, easy to evaluate. If you're not sure which modality fits, the answer is usually text.

**Vision.** Images, screenshots, documents with layout, real-world physical state. This unlocked when models could ground in actual visual structure instead of pattern-matching captions. Reach for it when there's a visual artifact the user cares about: a UI to test, a document with tables, a before-and-after, a piece of equipment to inspect.

**Voice.** Listening to speech, speaking back. This unlocked when reasoning got fast enough to think while talking, instead of speaking after a long pause. Reach for it when hands or eyes are busy: a coach on the sideline, a doctor doing intake, a sales rep on a call, accessibility.

**Video.** Long-form context with motion. Still moving fast in 2026. Reach for it when time matters: event timelines, sports coaching, surveillance, demo replay.

Cost, roughly. Text is cheapest. Vision runs 2-5x text per input. Voice runs 3-10x, plus latency for the audio round trip. Video is 10x and up, often charged by frame. Use the cheapest modality that captures the property you care about.

The rule that keeps you out of trouble: don't reach for a modality because it's new. Reach for it because the task has a property text doesn't capture.

**What that looks like in practice.** A customer wants an agent to triage bug reports. The team's first instinct is voice in — let users record what went wrong. But a spoken "the button doesn't work" carries no more information than a typed one, and now you're paying 5x and waiting on a transcript. The bug is *in the screenshot*: the button is there, it's just behind a modal. Vision in, text out, and a ten-minute triage takes four seconds. One modality decision, and the wrong one costs you the margin.

A meeting summary doesn't need voice in; the transcript is text. A live coaching loop does need voice out; the user can't read while doing the thing.

## Your exercise

Take your project candidate. Find one place where text is the wrong modality and another modality would unlock something the project can't do today.

If you can't find one, that's a valid answer too. Write down why text is right for every step.

**You're done when** you have a defensible answer in one paragraph either way.

**Practice proof:** save it in `NOTES.md` under "modality choice."

**Build on it:** build a screenshot-to-bug-report CLI: pass it a PNG, it sends the image to a vision model and prints a filled-in bug report.

## Why this matters

Every product has a modality choice. Most engineers default to text without thinking. The ones who ask the question before they pick a stack ship better products. As an FDE you'll often be the first person in the room asking it.

---

Next: [Lesson 1.5 · The model zoo](00e-the-model-zoo.html)
