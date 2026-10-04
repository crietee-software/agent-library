---
name: crietee-dev
description: "Cut build work into shippable slices with an hour estimate, definition of done, and a handover note. Use when the user asks for a build plan, technical approach, slice plan, estimate, or handover. Not for quotes, invoices, brand, or code review."
type: workflow
lifecycle: active
---

# Crietee dev

Plan and deliver build work in slices a client can see. No framework sermon. A diff review belongs to crietee-review. Write plans and notes in English.

Slices, done, and handover: [references/delivery.md](references/delivery.md).

## When

Trigger: build plan, technical approach, slice plan, hour estimate, implementation plan, handover.
Not: quote price, invoice, code review, brand, site motion, fitness.

## Loop

1. Read the repo or the files the user points at before choosing a stack. Existing language, framework, and folders win.
2. Write the delivery in one sentence: what the client can do afterwards.
3. Cut slices of 8 hours max. Each slice has a visible result. Read `references/delivery.md`.
4. Estimate in hours, not story points. Use a band if an assumption moves the hours by more than 30%.
5. Write code only if the user asks for the build, not if they ask for a plan.
6. For a plan: docx via crietee-brand, kicker `BUILD · PLAN`, path `/workspace/artifacts/build/YYYY-MM-DD-topic.docx`.
7. For a handover: note in the same folder, plus what was not done.
8. Write the path into project memory.

## Hard rules

- No new dependency without a reason in the note.
- No second source of truth next to the repo.
- No secrets in the note, in commits, or in chat if that can be avoided.
- Solo studio. No role split as if there is a team.
