---
name: crietee-invoice
description: "Create a Crietee invoice with Dutch statutory lines, sequential numbering, and VAT, as a branded docx and pdf. Use when the user asks for an invoice, credit note, or hours-to-invoice. Not for quotes, contracts, or week plans."
type: workflow
lifecycle: active
---

# Crietee invoice

Write an invoice a bookkeeper can enter. Every file goes through crietee-brand.

Statutory fields and credit notes: [references/fields.md](references/fields.md).

## When

Trigger: invoice, credit note, hours to invoice, reminder attachment.
Not: quote, proposal, terms, collaboration agreement, fitness week plan.

## Defaults

| Field | Default |
|---|---|
| Seller | Crietee Software, sole proprietorship. Placeholders `[name]`, `[city]`, `[KvK number]`, `[VAT number]`, `[iban]` until the user fills them |
| Rate | Elusive Innovations: € 40 excl. VAT. Any other client: take it from the quote, or ask |
| VAT | 21%. KOR only if the user says so, with the Dutch exemption sentence |
| Payment term | 14 days. Statutory B2B default is 30, maximum 60 |
| Number | `INV-YYYY-NNN`, credit `CRN-YYYY-NNN`. Never reuse |
| Currency | EUR |
| Language | English. Keep Dutch legal labels and the KOR sentence as specified in the reference |

## Loop

1. Read `crietee-brand` plus `references/documents.md`.
2. Read `references/fields.md` for a credit note, KOR, or a rate other than 21%.
3. Missing client, period, or hours block the invoice. Ask. Do not invent hours.
4. Allocate a number:

```bash
python3 /root/.grok/server-skills/crietee-invoice/scripts/next_doc.py \
  --kind INV --client "Client" --title "Period or job" --amount "0"
```

Use `--kind CRN` for a credit note. The script writes `/workspace/artifacts/admin/register.json`.
5. Build the docx. Kicker `COMMERCIAL · INVOICE` or `COMMERCIAL · CREDIT NOTE`. Title ends with a period.
6. Save as `/workspace/artifacts/invoices/INV-YYYY-NNN-client.docx` (credit: `CRN-...`). Pdf, spot-check first and last page.
7. Write path and number into project memory. Register status stays `draft` until the user says it was sent.

## Line block

Each line: date or period, description, hours or units, rate excl. VAT, amount excl. VAT.
Then subtotal, VAT rate, VAT amount, total incl. VAT.
Payment block: iban placeholder, payable to Crietee Software, reference the invoice number, due date.

## Do not

- No invoice without a number from the register.
- No credit note without the original invoice number.
- Do not mark paid unless the user says so.
