---
name: en-standard
lang: en
register: standard
status: ready
metrics:
  mean_sentence_length: {median: 14.59, p25: 12.65, p75: 17.56}
  light_verbs_per_100_words: {median: 0.0, p25: 0.0, p75: 0.61}
  connectors_per_100_sentences: {median: 0.0, p25: 0.0, p75: 0.0}
  nominalizations_per_100_words: {median: 3.82, p25: 0.0, p75: 4.61}
---

## Register purpose

This register covers web content, explanatory articles, FAQs, public announcements and short public reports. The reader is a member of the general public or a supplier with no inside knowledge, who has come to find something out or get something done.

## Target features

- Address and pronouns: "you" for the reader wherever that fits, "we" for the organization. Use few contractions, keeping them to common negatives.
- Sentence length: stay near the `mean_sentence_length` range in the metrics block, with varied lengths and one main idea per sentence.
- Paragraphs: short, each on one topic, with the main point first.
- Terms: short, everyday words. Glossary terms stay. Explain a term of art only if the source explains it, and otherwise leave it as it is.
- Requirements: "must" is the plain word for a requirement in running prose. Do not turn "should" or "may" into "must".
- Punctuation: no em dashes. Numbered lists for steps and checks, and informative headings.
- Openings and closings: start with what the reader most needs. End on what to do next, or when the content stops. No greeting or sign-off.

## Pattern adjustments

| Pattern id | Treatment | Reason |
| --- | --- | --- |
| EN-01 | stricter | A general reader should meet only common words, and figurative use goes every time. |
| EN-05 | softer | A closing sentence that gives the reader the takeaway may stay once its marker is removed. |
| EN-09 | softer | Question headings in FAQs are a real format, because they ask what the reader is asking. |
| EN-11 | stricter | Plain language favors verbs and named actors over noun strings. |
| EN-12 | stricter | The real verb is shorter and clearer for a general reader. |
| EN-15 | stricter | Intensifiers tell a general reader nothing, so cut them even when alone. |
| EN-17 | stricter | Any em dash joining clauses is replaced. |

## Mini examples

- "You will not be asked to make a payment of any fee to submit an application" → "You will not be asked to pay any fee to submit an application"
- "The agency conducts the measurement of procurement against approved budgets." → "The agency measures procurement against approved budgets."
- "It is worth noting that a Performance Bond plays a pivotal role in the reduction of the risk the buyer faces." → "A Performance Bond reduces the risk the buyer faces."

## Limits

- Do not add explanations, examples or definitions the source does not contain.
- Do not simplify a term of art into something that changes its meaning.
- Do not change the strength of a requirement, or the certainty of a claim, in the name of plainness.
- A quoted provision that uses "shall" is locked and stays as quoted.
- Do not become chatty. This register is neither stiff nor casual.

## References

- Federal Plain Language Guidelines, https://github.com/GSA/plainlanguage.gov (archived repository; the site now redirects to https://digital.gov/guides/plain-language). License: public domain in the US and CC0 1.0. Applied here for its principles: main point first, the reader addressed directly, common words, active verbs, short sections.
