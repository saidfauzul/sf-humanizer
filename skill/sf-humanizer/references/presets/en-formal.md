---
name: en-formal
lang: en
register: formal
status: ready
metrics:
  mean_sentence_length: {median: 15.95, p25: 15.19, p75: 16.98}
  light_verbs_per_100_words: {median: 0.0, p25: 0.0, p75: 0.0}
  connectors_per_100_sentences: {median: 0.0, p25: 0.0, p75: 0.0}
  nominalizations_per_100_words: {median: 5.33, p25: 4.01, p75: 7.12}
---

## Register purpose

This register covers policy, regulation, contracts, official letters, procurement notices and formal reports. The reader is an official, a supplier or an auditor who may rely on the exact wording later, so precision comes before ease.

## Target features

- Address and pronouns: the institution speaks in the third person ("the Board", "the Sample Agency"). "You" appears in letters and in guidance to staff, and "we" only in routine letter lines. No contractions.
- Sentence length: stay near the `mean_sentence_length` range in the metrics block. Do not split a condition from the obligation it limits.
- Paragraphs: one matter each, usually two to five sentences. Numbered sections stay as numbered.
- Terms: glossary terms and defined terms are kept and used consistently. Do not explain them or vary them for style.
- Modal verbs: "shall" in normative text is locked and is never flagged or changed to "must". Keep "must", "may" and "should" as written too, since each sets a different duty.
- Punctuation: no em dashes. Use commas, colons and semicolons. Bullets or numbers only for clauses, requirements and attachments.
- Openings and closings: keep the reference line, subject, salutation and closing that the letter format requires ("Dear Sir or Madam,", "Yours faithfully,"). A notice opens with what it requires, and ends on its effect, deadline or contact.

## Pattern adjustments

| Pattern id | Treatment | Reason |
| --- | --- | --- |
| EN-08 | softer | Parallel clauses of duty or purpose are normal drafting. |
| EN-09 | stricter | Questions do not belong in the body of formal text, answered or not. |
| EN-10 | softer | Short numbered sections with labels are the document format. |
| EN-11 | softer | Noun phrases such as "the supply and fitting" are usual here. Act only where a chain hides the actor. |
| EN-13 | softer | Paired or tripled legal wording can carry distinct duties. |
| EN-16 | softer | A run of similar obligations may share one shape. |
| EN-17 | stricter | Any em dash joining clauses is replaced. |

## Mini examples

- "Furthermore, any staff member who identifies a Conflict of Interest must make a declaration of it in writing." → "Any staff member who identifies a Conflict of Interest must declare it in writing."
- "Upon the expiry of the Bid Protest period, the finalization of the award decision and the commencement of the preparation of the contract should take place." → "When the Bid Protest period expires, the award decision should be finalized and contract preparation should begin."
- "It is important to note that, under the terms of the award, the Sample Agency must be in receipt of this bond no later than 20 November 2026." → "Under the terms of the award, the Sample Agency must receive this bond no later than 20 November 2026."

## Limits

- Do not touch clause numbers, citations, quoted provisions or definitions.
- Do not soften or strengthen a duty, or replace passive voice where the actor is unknown or the form is standard.
- Do not add contractions, a friendly tone or second-person address the source lacks.
- Do not shorten a condition, exception or proviso for the sake of rhythm.

## References

no clearly licensed reference yet
