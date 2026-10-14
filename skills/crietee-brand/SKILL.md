---
name: crietee-brand
description: "Apply Crietee Software brand to a client document or to Crietee's own UI: paper, ink, gold cut, type, voice, and the document checklist. Use when another Crietee skill says to go through crietee-brand, or when the user asks for huisstijl, brandbook, or a branded docx/pdf. Not for recoloring a client shop, quote pricing, invoice VAT, or Crietee site motion."
type: workflow
lifecycle: active
---

# Crietee brand

Source: Brandbook 01 v1.1 (oktober 2026). Tokens: [references/system.md](references/system.md). Writing and document shape: [references/documents.md](references/documents.md).

A file for a client is a Crietee document. A client product is not. Recolor only Crietee's own surfaces.

## When

Trigger: branded document, huisstijl, brandbook, apply Crietee brand, restyle Crietee's own page.
Not: write the quote or invoice from scratch (those skills call this one), VAT rules, a client shop in Crietee gold.

## Loop

1. Read `references/system.md` and `references/documents.md`.
2. Build or restyle the file the calling skill named. Paper ground, ink type, one gold signal bar, kicker from the caller.
3. Client prose follows `documents.md`. Dutch unless the user asked for English.
4. Pdf, then spot-check the first and last page against the send checklist in `documents.md`.

## Do not

- No second gold bar, no gold frame around the page, no white logo box.
- No tagline as a document title.
- No Crietee gold on a client shop or client app.
