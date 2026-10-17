# Severity

| Severity | Meaning | Ship? |
|---|---|---|
| Blocker | Wrong answer, data loss, a secret, an auth hole, or work outside the agreed slice | No |
| Must | Missing error path, a test that does not cover the bug, a misleading name on the changed path | After the fix |
| May | Smaller readability issue inside the diff | Yes |

## Checklist, in this order

1. Does the diff do what the slice promised, and nothing more?
2. Error path: empty input, unexpected status, timeout.
3. Authorisation and data: who may do this, and what leaves the system?
4. Secrets and logs.
5. A test or a manual check that would catch this bug.
6. Name and boundary of the change.

A point that is not on this list and does not block the user stays out.
