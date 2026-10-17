---
name: crietee-invoice
description: "Write a Crietee Software invoice with the statutory fields and VAT, as text for a document in Crietee Werkplek. Use for an invoice, invoicing hours or a reminder. Not for quotes, contracts or week plans."
type: workflow
lifecycle: active
---

# Crietee invoice

Write an invoice a bookkeeper can enter. The house style follows [crietee-brand](../crietee-brand/SKILL.md). Statutory fields are in [references/fields.md](references/fields.md).

## When

Use for: invoice, invoicing hours, reminder.

Not for: quote, proposal, contract, week plan.

## Defaults

| Field | Default |
|---|---|
| Seller | Crietee Software, sole proprietorship. Name, address, KvK number and VAT number come from the Werkplek settings |
| Rate | From the quote or from the hours. Ask if it is missing; do not invent it |
| VAT | 21%. 0% with the KOR sentence only if Levi says the small-business scheme applies |
| Payment term | 14 days |
| Number | Given by the Werkplek: INV-YYYY-NNN. Never reuse a number |
| Currency | Euro |
| Language | Dutch |

## Workflow

1. Read the house style in `crietee-brand`.
2. Invoice only hours that exist. If the client, the period or the hours are missing, ask. Do not invent hours.
3. Write the document in the form the Werkplek asks for:
   - **Title:** "Factuur" plus the period or the job, short, no full stop.
   - **Summary:** one sentence with the period or the project.
   - **Lines:** per line the description, the hours and the rate per hour, excluding VAT.
   - **Payment:** the payment term and a reason, for example the invoice number as payment reference.
4. The Werkplek calculates the amounts, VAT and total from the lines.

## Do not

- No invoice without a number from the Werkplek.
- Do not mark an invoice as paid unless Levi says so.
- The Werkplek does not make credit notes yet. Tell Levi, and do not make a loose note instead.
