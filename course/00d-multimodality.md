# Lesson 1.4 · Multimodality

**Where this gets you:** you'll know when reaching for vision, voice, or video is the right move on a customer project and when text is still the better answer.

## The idea

Voice was bottlenecked by intelligence, not audio quality. Vision the same. Knowing when to reach for a modality beats knowing every model that supports one.

Four modalities are worth knowing about today.

**Text.** Still the default. Still the winner for most tasks. Cheap, fast, well-understood, easy to evaluate. If you're not sure which modality fits, the answer is usually text.

**Vision.** Reading images, screenshots, documents with layout, real-world physical state. This one unlocked when models could ground in actual visual structure instead of pattern-matching captions. Reach for it when there's a visual artifact the user actually cares about: a UI to test, a document with tables, a before-and-after comparison, a piece of equipment to inspect.

**Voice.** Listening to speech, speaking back. This one unlocked when reasoning got fast enough to actually think while talking, instead of speaking after a long pause. Reach for it when hands or eyes are busy: a coach on the sideline, a doctor doing intake, a sales rep on a call, accessibility scenarios.

**Video.** Long-form context with motion. Still moving fast in 2026. Reach for it when temporal structure matters: event timeline analysis, sports coaching, surveillance, demo replay.

A useful mental model for cost: text is the cheapest. Vision is roughly 2-5x text per input. Voice is 3-10x text plus the latency budget for the audio round trip. Video is 10x and up, often charged by frame. Use the cheapest modality that actually captures the property you care about.

The rule that keeps you out of trouble: don't reach for a modality because it's new. Reach for it because the task has a property that text doesn't capture. A meeting summary doesn't need voice in; the transcript is text. A UI bug report does need vision in; the screenshot is the bug. A live coaching loop does need voice out; the user can't read while doing the thing.

## Your exercise

Take your project candidate. Identify one place where text is the wrong modality and another modality would unlock something the project can't currently do.

If you can't find one, that's also a valid answer. Write down why text is actually right for every step.

**You're done when** you have a defensible answer in one paragraph either way.

**Practice proof:** save it in `NOTES.md` under "modality choice."

## Why this matters

Every product has a modality choice. Most engineers default to text without thinking. The ones who think first about modality before they pick a stack ship better products and win the surface. As an FDE you'll often be the first person in the room asking the question.

---

Next: [Lesson 1.5 · The model zoo](00e-the-model-zoo.html)
