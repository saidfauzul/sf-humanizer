---
name: en-email
lang: en
register: email
status: ready
metrics:
  mean_sentence_length: {median: 14.09, p25: 11.92, p75: 14.5}
  light_verbs_per_100_words: {median: 0.0, p25: 0.0, p75: 0.0}
  connectors_per_100_sentences: {median: 0.0, p25: 0.0, p75: 0.0}
  nominalizations_per_100_words: {median: 1.98, p25: 1.94, p75: 4.87}
---

## Register purpose

This register covers work email to vendors, managers, other teams and committees. The reader is busy, reads on any device, and wants to know at once what is being asked and by when.

## Target features

- Address and pronouns: "I" and "we", "you" for the recipient. Politeness follows the relationship. Contractions are natural after "Hi Sara,", and used sparingly or not at all after "Dear Director," or "Dear Sir or Madam,".
- Sentence length: stay near the `mean_sentence_length` range in the metrics block. A request gets its own sentence.
- Paragraphs: short, often two or three sentences. The request or main point comes in the first or second paragraph.
- Terms: glossary terms, document numbers and amounts are kept. Explain internal shorthand only if the source does.
- Punctuation: avoid em dashes. A short list or a Date, Time and Location block is fine when it holds real items.
- Subject line: it stays in the output, and every fact on it (item, count, document number, status, date) must be kept unchanged.
- Openings and closings: one short greeting that matches the source, the point straight after it, a clear request or next step, and a brief sign-off with the name and any title block as written.

## Pattern adjustments

| Pattern id | Treatment | Reason |
| --- | --- | --- |
| EN-04 | stricter | "I hope this email finds you well" goes in every relationship. The greeting itself stays. |
| EN-05 | stricter | An email ends on the request or next step, not on a recap. |
| EN-10 | softer | Meeting details and attachment lists are easier to use set out on their own lines. |
| EN-11 | stricter | A request hidden in a noun phrase slows the reader, so one is enough to act on. |
| EN-15 | softer | Courtesy formulas such as "Thanks a lot" stay. Claims such as "highly committed" still go. |
| EN-16 | softer | A short email has too few sentences to show a pattern. |
| EN-17 | stricter | Any em dash joining clauses is replaced. |

## Mini examples

- "I am reaching out to make a request for your approval to move the deadline for the Statement of Work (SOW) for the consulting services procurement from 14 November to 21 November 2026." → "Could you approve moving the deadline for the Statement of Work (SOW) for the consulting services procurement from 14 November to 21 November 2026?"
- "We conducted a careful check of the file to be sure nothing had been overlooked, and the record is missing." → "We checked the file carefully to be sure nothing had been overlooked, and the record is missing."
- "Could you kindly provide us with your comments by 18 November 2026?" → "Could you send us your comments by 18 November 2026?"

## Limits

- Do not drop, reword into something vaguer, or contradict any fact on the subject line.
- Do not remove the greeting or sign-off, or change the level of politeness the source sets.
- Do not add a deadline, recipient, attachment or offer of help the source lacks.
- Do not turn a request into a demand, or a demand into a suggestion.

## References

- Federal Plain Language Guidelines, https://github.com/GSA/plainlanguage.gov (archived repository; the site now redirects to https://digital.gov/guides/plain-language). License: public domain in the US and CC0 1.0. Applied here for its principles: the request up front, the reader addressed directly, short paragraphs.
