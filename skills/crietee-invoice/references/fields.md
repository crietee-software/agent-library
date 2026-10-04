# Invoice fields

Checklist source: mandatory invoice lines, article 35a of the Dutch Wet op de omzetbelasting. If the rate or KOR status is unclear, check the Belastingdienst. Do not guess.

## Always on the invoice

- Issue date
- Sequential number (`INV-YYYY-NNN`)
- VAT identification number of Crietee, or placeholder `[VAT number]`
- Name and address of seller and client
- Quantity and nature of the service
- Date or period of the service if it differs from the invoice date
- Unit price excl. VAT, any discount, taxable amount per rate
- VAT rate applied
- VAT amount
- KvK number (not required on the VAT invoice, studio default anyway)

Write labels in English (`Invoice number`, `VAT`). The VAT number itself stays the Dutch format once the user supplies it.

## KOR

Only if the user says the small-business scheme applies. No VAT amount. Dutch sentence on the invoice, unchanged: `Factuur vrijgesteld van omzetbelasting op grond van artikel 25 Wet OB (kleineondernemersregeling).`

## Credit note

- Own number `CRN-YYYY-NNN`
- Points at the original invoice number and invoice date
- Negative amounts, same rate as the original invoice
- Reason in one sentence

## Reminder

No new invoice number. Same number, status `reminder` in the register, new letter with the open amount and the original due date.
