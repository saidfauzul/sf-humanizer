---
name: en-chat
lang: en
register: chat
status: ready
metrics:
  mean_sentence_length: {median: 8.34, p25: 7.98, p75: 10.8}
  light_verbs_per_100_words: {median: 0.0, p25: 0.0, p75: 0.0}
  connectors_per_100_sentences: {median: 0.0, p25: 0.0, p75: 0.0}
  nominalizations_per_100_words: {median: 1.09, p25: 0.36, p75: 1.97}
---

## Register purpose

This register covers instant messages and short work threads with a teammate, a manager or a vendor contact. The reader is following along in real time and already has most of the context.

## Target features

- Address and pronouns: "I", "you", dropped subjects, and first names where the source uses them. Contractions are the default.
- Sentence length: stay near the `mean_sentence_length` range in the metrics block. Turns are short and uneven, and fragments are fine when the thread supplies the context.
- Paragraphs: one line or a few. In a longer announcement, one short block per point.
- Terms: glossary terms, numbers, dates and names stay exact, however casual the tone. No explanations of what the thread already knows.
- Speaker labels: where the source is a thread with bold labels, such as **Maya:**, keep each label as written. Do not add labels to a single message.
- Punctuation: minimal. A closing full stop may go. No em dashes and normally no bullets.
- Openings and closings: no letter-style greetings or sign-offs. A first name to get attention, a thanks, or a conversational "Speak soon." may stay. Start with the point.

## Pattern adjustments

| Pattern id | Treatment | Reason |
| --- | --- | --- |
| EN-04 | stricter | "I hope this message finds you well" and letter-style greetings have no place here, and the catalog's email allowance does not apply. |
| EN-06 | stricter | A chat line has no room for "Moreover", so even one goes. |
| EN-09 | softer | Quick questions and a question answered in the next breath are how people talk in chat. |
| EN-11 | stricter | Nouns in place of verbs sound like a report, and nothing here should. |
| EN-12 | stricter | "Make an approval" is never how a message reads. |
| EN-16 | exempt | Short turns are often alike in length, and that means nothing here. |
| EN-17 | stricter | Any em dash joining clauses is replaced. |

## Mini examples

- "Please leverage the shared document to note any questions so we can cover them at the meeting." → "Put any questions in the shared doc so we can cover them at the meeting."
- "Okay. Furthermore, send me the note and I'll make an approval of the extension if it looks reasonable." → "Okay. Send me the note and I'll approve the extension if it looks reasonable."
- "I am currently in the process of conducting a check with our logistics team now, no updated date yet." → "Checking with our logistics team now, no updated date yet."

## Limits

- Never add a greeting or sign-off to a single-line message.
- Do not expand fragments into full sentences or merge separate turns.
- Do not change who said what, or the order of turns.
- When another speaker replies to a line, rewrite the pattern in that line instead of removing it, and keep the claim the reply responds to, so the thread still makes sense.
- Do not drop a date, number or name to make a line shorter.
- Do not add slang, emoji or warmth the source does not have.

## References

no clearly licensed reference yet
