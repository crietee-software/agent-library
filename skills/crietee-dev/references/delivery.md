# Delivery

## Slice

A slice is done when the client can point at it without an explanation of the diff.

| Field | Rule |
|---|---|
| Name | Verb + object |
| Result | What is now possible |
| Not | What this slice does not solve |
| Hours | Whole number, max 8 |
| Done when | One check the user can run |

More than five slices: write the first two fully, the rest as a name plus an hour band.

## Definition of done

- Does what the slice promised, on the agreed input.
- The error path is visible, no silent fail.
- No debug logs with client data.
- Existing repo checks were run, or the note says why not.

## Handover note

1. What shipped.
2. How to run or open it.
3. What was deliberately not done.
4. Hours against the estimate.
5. The next slice, if there is one.

No changelog novel. No screenshot wall.
