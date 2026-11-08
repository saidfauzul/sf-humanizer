# Locking

A locked segment is copied character for character into the output. Lock before looking for patterns, so that no later step can alter it.

## What is locked

- Article, paragraph and item numbering (pasal, ayat, huruf; article, section, clause), and quoted regulation text.
- Definitions in Ketentuan Umum, or in any "X means ..." or "X adalah ..." definitions section.
- Numbered procedure steps: their number, their order, and the actor of each step.
- Numbers, dates, times, units, amounts of money, percentages, and document numbers.
- Direct quotations.
- Terms in the glossary for the language, and terms the user added.
- Proper names of people, organizations, positions, systems and places.
- URLs and email addresses.

## How to mark segments

Internally, replace each locked segment with a numbered marker such as `⟦L1⟧`, and keep a list of what each marker stands for. Work on the text with the markers in place, then restore them.

Before output, confirm that every marker was restored once, in the right place, with its original text. Never show the markers to the user.

Inflected forms are not free to change either: when a locked term takes an affix or a possessive, keep the term itself intact and do not swap it for a synonym.

## What is still edited

Locking covers the segment, not the paragraph around it. The narrative before and after a locked segment is edited as usual.

In a numbered procedure step, the number and the actor stay. The wording of the action may change only if the action, its object and its conditions stay the same.

Before: Pasal 12 ayat (3) mengatur bahwa HPS perlu untuk dilakukan pemutakhiran oleh PPK.

After: Pasal 12 ayat (3) mengharuskan PPK memutakhirkan HPS.

Here "Pasal 12 ayat (3)", "HPS" and "PPK" are locked. The rest is narrative. If the source sentence quotes the article verbatim, the whole quotation is locked.

## If a locked segment seems wrong

Leave it unchanged and report a confirmation point. Examples: an article number that does not seem to fit its subject, a total that does not equal its parts, a date that falls before the event it follows, or a term spelled two ways. Quote the segment and say what looks wrong.

## User additions

The user can add locked terms inline with `kunci:` followed by a comma-separated list, for example:

```text
sf-humanizer preset id, formal  kunci: Tim Reviu Internal, Rencana Umum Pengadaan
```

These terms apply only to the current request. Treat them the same way as glossary terms.

When it is unclear whether something should be locked, lock it.
