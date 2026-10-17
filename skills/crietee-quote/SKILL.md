---
name: crietee-quote
description: "Write a Crietee Software quote: scope, assumptions, price and validity, as text for a document in Crietee Werkplek. Use for a quote, proposal, estimate or price. Not for invoices, contracts or week plans."
type: workflow
lifecycle: active
---

# Crietee quote

Write a quote a client can accept. Not a brochure. The house style and writing rules follow [crietee-brand](../crietee-brand/SKILL.md) and the brand book.

Price models: [references/pricing.md](references/pricing.md).

## When

Use for: quote, proposal, estimate, price.

Not for: invoice, contract, general terms, week plan.

## Defaults

| Field | Default |
|---|---|
| Parties | Crietee Software, sole proprietorship |
| Rate | Elusive Innovations: € 40,00 excluding VAT. For another client, ask for the rate; do not invent it |
| VAT | 21% |
| Valid until | 14 days after the quote date |
| Payment after acceptance | 14 days |
| Terms | Crietee Software's general terms apply. Do not rewrite them |
| Number | Given by the Werkplek: QTE-YYYY-NNN |
| Language | Dutch, unless the user asks for English |

## Workflow

1. Read the house style in `crietee-brand`.
2. Ask only if the client, the goal or the rate is missing. Everything else becomes a numbered assumption.
3. Write the document in the form the Werkplek asks for:
   - **Title:** "Offerte" plus the subject, short, no full stop.
   - **Summary:** three sentences: what, for whom, and what it costs.
   - **Sections:** the standard section titles below, in this order.
   - **Lines:** per item the description, the hours and the rate per hour.
4. The Werkplek calculates the amounts and VAT from the lines. Do not write amounts in the text that are already in the lines.

## Required sections

1. Summary: why this quote exists, in three sentences.
2. Scope of the assignment: what will be delivered.
3. Out of scope: what is not in the price.
4. Approach: in phases, with the hours per phase.
5. Price and rate.
6. Assumptions: each with the consequence if it turns out wrong.
7. Schedule, payment and what acceptance means.
8. Acceptance: name, date and signature.
9. One sentence: Crietee Software's general terms apply.

## Do not

- No fixed price while the scope is still vague. Give an hour band instead.
- No team language: Crietee is a sole proprietorship.
- No discount that was not asked for.
- No slogan as the title.
