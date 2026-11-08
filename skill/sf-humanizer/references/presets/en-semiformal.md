---
name: en-semiformal
lang: en
register: semiformal
status: ready
metrics:
  mean_sentence_length: {median: 13.79, p25: 13.21, p75: 16.39}
  light_verbs_per_100_words: {median: 0.0, p25: 0.0, p75: 0.0}
  connectors_per_100_sentences: {median: 0.0, p25: 0.0, p75: 0.0}
  nominalizations_per_100_words: {median: 2.4, p25: 1.53, p75: 4.03}
---

## Register purpose

This register covers internal memos, meeting notes, project updates, briefings and work articles. The reader is a colleague or manager who needs to know what happened, who owns what, and what has to be decided.

## Target features

- Address and pronouns: "I" and "we" for the writer and team, "you" for the reader. Name the person when a task or decision is theirs. Contractions are allowed where they read naturally, and need not appear in every clause.
- Sentence length: stay near the `mean_sentence_length` range in the metrics block, mixing shorter sentences with longer ones.
- Paragraphs: short, usually one topic of two to five sentences. Labelled note sections may be a single paragraph.
- Terms: glossary terms are kept. Workplace shorthand the team already shares needs no explanation. Prefer plain verbs to official phrasing.
- Punctuation: avoid em dashes. Use commas, colons or a new sentence. Bullets are for action items and real lists.
- Openings and closings: keep memo headers, a brief greeting and a short sign-off when the source has them. Open with the news, and end on a next step, owner or decision when the source gives one.

## Pattern adjustments

| Pattern id | Treatment | Reason |
| --- | --- | --- |
| EN-04 | softer | A short greeting such as "Good morning, everyone." or "Dear team," stays. Stock openers still go. |
| EN-05 | stricter | Memos should end on action, so a closer that repeats the paragraph is folded in. |
| EN-06 | stricter | Memos are short, and even one "Moreover" reads as official phrasing. |
| EN-10 | softer | Labelled sections in notes ("Discussion:", "Decisions:") stay when each holds full sentences. |
| EN-11 | stricter | Colleagues expect verbs and named actors, as the low nominalization range shows. |
| EN-12 | stricter | Plain verbs are the mark of this register. |

## Mini examples

- "We will conduct a review of the new process after the first three months to see whether it is working as intended." → "We'll review the new process after the first three months to see whether it's working as intended."
- "The meeting confirmed that two teams have not sent their proposals yet. Moreover, the consolidated plan cannot be finalized without them." → "The meeting confirmed that two teams haven't sent their proposals yet, and the consolidated plan can't be finalized without them."
- "This update provides a summary of progress on the moving of contract files from the legacy storage system to the new records system." → "This update summarizes progress on moving contract files from the legacy storage system to the new records system."

## Limits

- Do not invent an owner, deadline or decision that the source leaves open.
- Do not merge or rewrite numbered steps and action items beyond what locking allows.
- Do not turn the memo chatty, with jokes or fragments the source lacks.
- Do not force a contraction into a sentence that reads better without one.

## References

no clearly licensed reference yet
