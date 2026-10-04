# Severity

| Severity | Meaning | Ship |
|---|---|---|
| Blocker | Wrong answer, data loss, secret, auth hole, or work outside the agreed slice | No |
| Must | Missing error path, test does not cover the bug, misleading name on the changed path | After the fix |
| May | Smaller readability inside the diff | Yes |

## Checklist, in this order

1. Does the diff do what the slice promised, and nothing extra?
2. Error path: empty input, unexpected status, timeout.
3. Auth and data: who may do this, what leaves the system?
4. Secrets and logs.
5. Test or manual check that would catch this bug.
6. Name and boundary of the change.

A point that is not on this list and does not block the user stays out.
