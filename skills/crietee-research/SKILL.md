---
name: crietee-research
description: "Set up a research effort and deliver a decision memo: question, scope, method, sources, findings. Use when the user asks for research, discovery, a competitor scan, a spike report, or a research plan. Not for quotes, invoices, or code review."
type: workflow
lifecycle: active
---

# Crietee research

Deliver a decision, not a reading pile. Every document goes through crietee-brand. Write the memo in English.

Types and source rules: [references/types.md](references/types.md).

## When

Trigger: research, research plan, discovery, competitor scan, market scan, spike report, decision memo.
Not: quote, invoice, code review, a one-off bugfix, fitness week plan.

## Loop

1. State the decision question in one sentence. No question, no research.
2. Pick one type from `references/types.md`. Read that file.
3. Write scope and non-goals before opening sources. Default timebox: 4 hours desk, 8 hours spike, unless the user says otherwise.
4. Collect sources. Every finding gets a source and a confidence: high / medium / low.
5. Separate fact, interpretation, and recommendation.
6. Build the memo with the docx skill. Kicker `RESEARCH · MEMO`. Title ends with a period.
7. Save as `/workspace/artifacts/research/YYYY-MM-DD-topic.docx`. Pdf, spot-check first and last page.
8. Write the path into project memory.

## Required blocks

1. Decision question.
2. Scope and non-goals.
3. Method and timebox.
4. Sources, with date.
5. Findings, 7 max, each with confidence.
6. Recommendation: do / don't / first X. One choice.
7. Open points that could still flip the choice.
8. What this does not answer.

## Do not

- No recommendation without the counterargument.
- No unsourced percentage.
- No quote price in the memo. Point at crietee-quote if the user wants an offer.
