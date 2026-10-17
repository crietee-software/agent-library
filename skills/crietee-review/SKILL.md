---
name: crietee-review
description: "Review code or a diff for correctness, scope, security and tests, with blocker, must and may. Use for a code review, PR review or diff check. Not for quotes, design, brand or a build plan."
type: workflow
lifecycle: active
---

# Crietee review

Review the diff, not the author. One finding, one consequence. Chat in English. A document for a client follows `crietee-brand` and is in Dutch unless the user asks for English.

Severity and checklist: [references/severity.md](references/severity.md).

## When

Use for: code review, PR review, diff check, "look at this change".

Not for: build plan, quote, invoice, visual brand, research memo.

## Workflow

1. Read the diff and the surrounding function. Do not review a file name alone.
2. Read `references/severity.md`.
3. Look for blockers first: a wrong answer, data loss, a secret, an auth hole, or work outside the agreed scope.
4. Then musts: a missing error path, a test that would not catch the bug, a name that misleads the next reader.
5. Only then mays, and only if no blocker is open. At most three may-points.
6. Answer in chat, unless the user asks for a document. A document follows `crietee-brand` and becomes a Crietee Werkplek document. Each finding: how it is now, what to do, why it helps.
7. Close with: ship, ship after the musts, or do not ship.

## Hard rules

- Cite the file and line, or say the line is not in the diff.
- No style comments on code outside the diff.
- Do not rewrite the feature when a targeted patch is enough.
- A secret in the diff is always a blocker. Name the kind of secret; do not repeat the value.
