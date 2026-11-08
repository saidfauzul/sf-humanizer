---
name: sf-humanizer
description: Rewrites AI-sounding text so it reads as human-written, with facts unchanged. Works in Indonesian and English, with presets by language and register. Use when the user says "sf-humanizer", "humanize", "manusiakan", or "tulis ulang agar natural".
version: 0.1.0-beta.1
---

# sf-humanizer

Rewrite AI-sounding text so a careful reader takes it for human writing. The facts stay as they are.

## Invocation

```text
sf-humanizer preset <bahasa>, <register> [mode cepat|lengkap|audit]
```

Every argument is optional:

- Language: detected from the text when not given.
- Register: the general register of the language, `standar` for Indonesian and `standard` for English.
- Mode: `cepat`.

If the request gives no text, ask for it. Mixed-language text uses the language of most of its sentences; leave passages in the other language as they are and note this as a confirmation point.

## Presets

| Language | Register | Preset file | Use for |
| --- | --- | --- | --- |
| id | formal | `references/presets/id-formal.md` | Official letters, regulations, SOPs, nota dinas, procurement reports |
| id | semiformal | `references/presets/id-semiformal.md` | Internal memos, short reports, briefing material |
| id | informal | `references/presets/id-informal.md` | Messages to colleagues, personal notes, casual posts |
| id | standar | `references/presets/id-standar.md` | Neutral standard Indonesian for a broad audience |
| id | email | `references/presets/id-email.md` | Work email |
| en | formal | `references/presets/en-formal.md` | Policy, regulation, contracts, formal reports |
| en | semiformal | `references/presets/en-semiformal.md` | Internal memos, briefings, work articles |
| en | informal | `references/presets/en-informal.md` | Personal posts, notes to close colleagues |
| en | standard | `references/presets/en-standard.md` | Plain general-audience prose |
| en | email | `references/presets/en-email.md` | Work email |
| en | chat | `references/presets/en-chat.md` | Instant messages: short, direct lines |

If the preset file is missing, apply the general rules with the register description in this table.

An unknown combination is not an error. Say that the preset does not exist and use the nearest one; for example, id chat becomes id informal.

## Modes

Begin the response with the first item of the mode. Add no preamble, status line, recap of checks, or closing summary.

`cepat` shows only:

- the final text;
- one to three short notes on what changed;
- confirmation points, if there are any.

`lengkap` shows, in this order:

1. Findings, with pattern IDs.
2. Draft: the complete draft text, written out in full, not a description or a reference to the final text.
3. Audit of the draft.
4. Final text.
5. Confirmation points.
6. Metrics summary. Run `scripts/metrics.py` if it is available; otherwise report word and sentence counts for the original and the final text, and say that they are estimates.

`audit` shows findings and a score only, with no rewrite. Use it for text already edited by another model.

Compute the audit score as pattern density: (3 x strong findings + weak findings that count) x 100 / word count. Report the number and its band: low below 3, medium from 3 to 6, high above 6. Make the totals match the findings listed. These bands were calibrated on synthetic samples. A weak finding counts only under the co-occurrence rule in step 3 of the workflow.

## Files to load

Read only these files, and nothing else from `references/`:

- this file;
- [locking.md](references/locking.md);
- the glossary for the language: [glossary-id.md](references/glossary-id.md) or [glossary-en.md](references/glossary-en.md);
- the patterns file for the language: [patterns-id.md](references/patterns-id.md) or [patterns-en.md](references/patterns-en.md);
- the one preset file from the table above;
- the one examples file, `references/examples/<lang>-<register>.md`, if it exists.

## Workflow

Follow these seven steps in order:

1. **Determine preset and mode.** Apply the defaults above where the user gave nothing.
2. **Lock normative segments** as described in locking.md, including any terms the user added with `kunci:`.
3. **Mark patterns** from the patterns file, strongest first. Act on a weak pattern only when it co-occurs with another pattern in the same sentence or paragraph.
4. **Filter false positives** using the catalog's do-not-flag list.
5. **Draft** according to the preset. For Indonesian, run the calque test on every sentence: ask "what English sentence is behind this one?" If one is plainly visible, rebuild the sentence from the Indonesian outward.
6. **Audit the draft.** Look for remaining patterns and changed facts, confirm that locked segments are intact, and confirm that counts match. Return to step 5 for anything that fails.
7. **Output** according to the mode.

Steps 3 to 6 are internal. `cepat` mode does not show them.

## Core rules

- Rewrite, never trim. Keep the same information in the same order of ideas, unless clarity demands a change.
- Leave numbers, names, dates, references, quotations and locked terms unchanged.
- Keep the author's claims. Never add facts, examples, sources or opinions.
- Keep the strength of every obligation and claim. Do not turn "perlu" or "sebaiknya" into "wajib", or "should" into "must", and do not drop a hedge.
- Report substantive problems as confirmation points and never fix them silently. These include suspicious numbers, possibly wrong article references, unsupported claims, and a stated count that does not match the items listed.
- Respect the register of the preset. A pattern that is wrong in one register may be right in another, so the preset file decides.
- Vary sentence length the way a person does when thinking through a point. Do not alternate long and short mechanically.
- Prefer a concrete verb to a light verb with a noun.
- Do not swap in a new tic for the one removed. A text in which every sentence has been made short and punchy still reads as machine-made.
- If the text already reads as human, say so and change little or nothing.
- Keep generic rules free of specific preset names. Behavior that belongs to one register goes in its preset file.

## Metrics

Use `scripts/metrics.py` only where code can be run. If it cannot, estimate by reading and say that the figures are estimates.

- In `lengkap` mode, run `python3 scripts/metrics.py --compare ORIGINAL FINAL --lang <id|en>` and summarize the changes that matter.
- In `audit` mode, run `python3 scripts/metrics.py TEXT --lang <id|en> --json` and use its hits as candidates for findings. Judge each hit against the do-not-flag list before counting it.
- After rewriting in `lengkap` mode, run `python3 scripts/metrics.py --check-locked ORIGINAL FINAL --lang <id|en>`, adding `--terms "A,B"` for terms given with `kunci:`.

Exit code 1 from `--check-locked` lists segments as missing or altered. Restore each listed segment. If one looks like a false alarm, keep the original wording and mention it as a confirmation point.

A preset file's `metrics` block gives the typical range of its samples. Treat it as context, and do not rewrite a text only to move a number.

## Confirmation points

A confirmation point names the passage, says what looks wrong, and asks the author to check it. Leave the passage as written in the final text. Do not raise a point only because a date is later than today.

Write notes and confirmation points in the language the user is writing in. When the message holds only the invocation and the text, use the language of the text.

Do not include the internal lock markers in any output.
