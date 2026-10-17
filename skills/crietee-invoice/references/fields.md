# Invoice fields

Source for the mandatory invoice fields: article 35a of the Dutch VAT act (Wet op de omzetbelasting). If the rate or the KOR status is unclear, check with the Belastingdienst. Do not guess.

## Always on the invoice

- Issue date
- Sequential number (`INV-YYYY-NNN`)
- The VAT identification number of Crietee, or the placeholder `[VAT number]`
- Name and address of seller and client
- Quantity and nature of the service
- Date or period of the service, if it differs from the invoice date
- Unit price excluding VAT, any discount, and the taxable amount per rate
- The VAT rate applied
- The VAT amount
- KvK number (not required on a VAT invoice, but the studio always shows it)

Labels follow the document language, Dutch by default: `Factuurnummer`, `Factuurdatum`, `Btw-identificatienummer`, `Btw-tarief`, `Btw-bedrag`, `KvK-nummer`. Use English labels only when the user asks for English.

## KOR

Only if Levi says the small-business scheme applies. No VAT amount. This Dutch sentence goes on the invoice unchanged: `Factuur vrijgesteld van omzetbelasting op grond van artikel 25 Wet OB (kleineondernemersregeling).`

## Reminder

No new invoice number. Same number, a reminder status, and a new letter with the open amount and the original due date.
