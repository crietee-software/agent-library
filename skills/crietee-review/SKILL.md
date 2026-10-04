---
name: crietee-review
description: "Review code or a diff for correctness, scope, security, and tests, with blocker, must, and may. Use when the user asks for a code review, PR review, or diff check. Not for quotes, design, brand, or a build plan."
type: workflow
lifecycle: active
---

# Crietee review

Review the diff, not the author. One finding, one consequence. Write the review in English.

Severity and checklist: [references/severity.md](references/severity.md).

## When

Trigger: code review, PR review, diff check, look at this change.
Not: build plan, quote, invoice, visual brand, research memo.

## Loop

1. Read the diff and the surrounding function. Do not review a filename alone.
2. Read `references/severity.md`.
3. Look for blockers first: wrong answer, data loss, secret, auth hole, scope that is not the job.
4. Then must: missing error path, test that would not catch the bug, name that misleads the next reader.
5. May only if no blocker is open. Three may-points max.
6. Answer in chat, unless the user asks for a file. A file goes through crietee-brand at `/workspace/artifacts/reviews/YYYY-MM-DD-topic.docx`.
7. Close with: ship / ship after must / do not ship.

## Hard rules

- Cite file and line, or say the line is not in the diff.
- No style comments on code outside the diff.
- Do not rewrite the feature if a targeted patch is enough.
- A secret in the diff is always a blocker. Name the kind of secret, do not repeat the value.
