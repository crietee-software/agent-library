---
name: crietee-quote
description: "Draft a Crietee quote with scope, assumptions, price, and validity, as a branded docx and pdf. Use when the user asks for a quote, proposal, estimate, or price. Not for invoices, contracts, or week plans."
type: workflow
lifecycle: active
---

# Crietee quote

Write an offer a client can accept. Not a brochure. Every file goes through crietee-brand.

Price models: [references/pricing.md](references/pricing.md).

## When

Trigger: quote, proposal, estimate, price, offer.
Not: invoice, credit note, terms, collaboration agreement, fitness week plan, code.

## Defaults

| Field | Default |
|---|---|
| Seller | Crietee Software, sole proprietorship. Placeholders `[name]`, `[city]`, `[KvK number]`, `[VAT number]` until the user fills them |
| Rate | Elusive Innovations: € 40 excl. VAT. Any other client: ask the rate, do not invent it |
| VAT | 21%. 0% plus the Dutch exemption line only if the user says KOR |
| Validity | 14 days from the quote date |
| Payment after acceptance | 14 days. Statutory B2B default is 30, maximum 60 |
| Terms | `artifacts/1-algemene-voorwaarden.docx` applies. Do not rewrite them |
| Number | `QTE-YYYY-NNN` from the script below |

## Loop

1. Read `crietee-brand` plus `references/system.md` and `references/documents.md`.
2. Ask only if missing client, goal, or rate (non-Elusive) blocks the price. Everything else becomes a numbered assumption.
3. Allocate a number and register the draft:

```bash
python3 /root/.grok/server-skills/crietee-quote/scripts/next_doc.py \
  --kind QTE --client "Client" --title "Short title"
```

4. Build the docx with the docx skill. Paper `#F2EFE6`, ink hero, one gold signal bar. Title ends with a period. Kicker `COMMERCIAL · QUOTE`.
5. Save as `/workspace/artifacts/quotes/QTE-YYYY-NNN-client.docx`. Convert to pdf. Spot-check the first and last page.
6. Write the path into project memory.

## Required blocks

1. Parties, date, number, valid until.
2. Why this quote exists, three sentences max.
3. Scope, as work that will be delivered.
4. Out of scope.
5. Approach in slices, hours per slice.
6. Price: hours × rate, subtotal excl. VAT, VAT, incl. No invented discount.
7. Assumptions, each with the consequence if it is wrong.
8. Schedule, payment, what acceptance means.
9. Acceptance line: name, date, signature.
10. One sentence: the general terms of Crietee Software apply.

## Do not

- No fixed price without an hour band when the scope is still vague.
- No team language. Solo studio.
- No second gold bar, no white logo box.
- Write the quote in English unless the user asks for Dutch.
