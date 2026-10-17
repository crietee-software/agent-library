---
name: crietee-dev
description: "Cut build work into shippable slices with an hour estimate, a definition of done and a handover note. Use for a build plan, technical approach, slice plan, estimate or handover. Not for quotes, invoices, brand or code review."
type: workflow
lifecycle: active
---

# Crietee dev

Plan and deliver build work in slices a client can see. No framework sermon. A diff review belongs to crietee-review. A plan for a client is written in Dutch unless the user asks for English.

Slices, definition of done and handover: [references/delivery.md](references/delivery.md).

## When

Use for: build plan, technical approach, slice plan, hour estimate, implementation plan, handover.

Not for: quote price, invoice, code review, brand, site motion, fitness.

## Workflow

1. Read the repo or the files the user points at before you choose a stack. The existing language, framework and folders win.
2. Write the delivery in one sentence: what the client can do afterwards.
3. Cut slices of at most 8 hours. Each slice has a visible result. See `references/delivery.md`.
4. Estimate in hours, not story points. Give a band when an assumption moves the hours by more than 30%.
5. Write code only when the user asks for the build, not when they ask for a plan.
6. For a plan: write it as a Crietee Werkplek document with the kicker `BUILD · PLAN`, in the style of `crietee-brand`. The first prose is the delivery sentence.
7. For a handover: a note next to the repo, plus what was not done.
8. Write the location into project memory.

## Hard rules

- No new dependency without a reason in the note.
- No second source of truth next to the repo.
- No secrets in the note, in commits, or in chat if it can be avoided.
- Solo studio. No role split as if there were a team.
