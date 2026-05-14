# Playbook: Deploy Verification

> Example playbook. The shape — trigger, steps, definition of done — is what to copy. The specifics are illustrative; replace with yours.

## Trigger

Any time work is about to be reported as "deployed", "shipped", "live", or "done" after a publish command (`rsync`, `scp`, `vercel deploy`, `gcloud run deploy`, a CI deploy, any upload).

## Why this playbook exists

The single failure mode it prevents: declaring victory on a deploy that never actually landed. A deploy command returning cleanly is **not** proof. An ambiguous tool result is **not** proof. "It probably worked" is how broken things get called done.

## Steps

1. **Run the deploy.** Note exactly what command, what target.
2. **Verify in the same turn** — pick at least one, do not skip:
   - `curl -sI` the live URL → fresh `last-modified` or the new content present
   - `ssh host ls -l /path` → new file, fresh mtime
   - A screenshot of the live URL showing the change
   - The CI run's own smoke-test step passing
3. **If the deploy tool errored, returned ambiguous output, or returned nothing** — re-run or verify directly. Never assume success.
4. **Only now** report the outcome — and report it *with* the proof, not as a bare claim.

## Definition of done

The word "deployed" has not been earned until a verification from step 2 has been run and its result is in hand. Done = change confirmed live, with evidence, this turn.

## Anti-patterns

- Saying "deployed" because the command exited 0
- Polling a remote job repeatedly instead of one check + one report
- Re-running the deploy as a "retry" without first checking the previous one didn't already land
