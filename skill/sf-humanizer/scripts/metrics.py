#!/usr/bin/env python3
"""Text metrics for sf-humanizer. Standard library only.

Usage:
    python3 scripts/metrics.py text.txt --lang id
    cat text.txt | python3 scripts/metrics.py --json
    python3 scripts/metrics.py --compare BEFORE AFTER
    python3 scripts/metrics.py --check-locked ORIGINAL RESULT [--glossary FILE ...] [--terms "A,B"]

The numbers are hints for a human or model reader, not a verdict on a text.
"""

from __future__ import annotations

import argparse
import difflib
import json
import re
import statistics
import sys
from pathlib import Path

MONTHS = (
    "Januari|Februari|Maret|April|Mei|Juni|Juli|Agustus|September|Oktober|November|Desember|"
    "January|February|March|May|June|July|August|December"
)
STOPWORDS = {
    "id": set(
        "yang dan di ke dari untuk dengan pada ini itu dalam tidak akan atau juga kami "
        "sebagai oleh adalah saya bisa sudah telah agar".split()
    ),
    "en": set(
        "the and of to in for with on this that is are was be will not or as by we it "
        "have has at from an".split()
    ),
}
ABBREVIATIONS = (
    "Yth|Sdr|Bpk|No|Dr|Prof|Mr|Mrs|Ms|Jl|dll|dsb|dst|tsb|a\\.n|u\\.p|e\\.g|i\\.e|etc|vs|p\\.m|a\\.m"
)
DOT = "\x00"

ID_LIGHT_VERBS = "melakukan|melaksanakan|memberikan|mengadakan|menjalankan"
ID_LIGHT_NOUN_SUFFIX = re.compile(r"(?:si|isasi|itas|ensi|isme|ur|if)$")
ID_LIGHT_NOUNS = set(
    "evaluasi klarifikasi kontribusi koordinasi verifikasi validasi analisis pemeriksaan "
    "pengecekan penilaian pembahasan pengawasan pemantauan penyusunan tindakan upaya kegiatan "
    "pembayaran pengiriman penyampaian pemetaan pengadaan perbaikan persiapan perubahan "
    "peninjauan reviu tindak".split()
)
EN_LIGHT_VERBS = (
    "conduct|conducts|conducted|conducting|perform|performs|performed|performing|"
    "carry out|carries out|carried out|carrying out|undertake|undertakes|undertook|undertaken|"
    "undertaking|make|makes|made|making|provide|provides|provided|providing|give|gives|gave|"
    "given|giving|take|takes|took|taken|taking|do|does|did|done|doing"
)
EN_LIGHT_NOUN_SUFFIX = re.compile(r"(?:tion|sion|ment|ance|ence|sis|al)$")
EN_LIGHT_NOUNS = set(
    "decision assistance review evaluation assessment consideration contribution analysis "
    "request".split()
)
EN_CONDUCT_OF = re.compile(r"\bthe conduct of (?:an? |the )?[^\W\d_]+", re.IGNORECASE)
EN_DETERMINERS = set("a an the some this that these those our your their any further".split())

ID_PE_AN = re.compile(r"^pe\w{3,}an$")
ID_NOMINAL = re.compile(r"^(?:pe\w{3,}an|ke\w{3,}an|per\w{3,}an)$")
ID_NOT_NOMINAL = {"pekan", "kemudian", "perempuan", "kebijakan", "perusahaan"}
EN_NOMINAL = re.compile(r"^\w{3,}(?:tion|sion|ment|ance|ence|ity)$")
EN_NOT_NOMINAL = set(
    "government department question station nation moment comment document instrument "
    "city quality".split()
)

CONNECTORS = {
    "id": (
        "selain itu",
        "di sisi lain",
        "perlu diketahui",
        "lebih lanjut",
        "dalam rangka",
        "sehubungan dengan hal tersebut",
        "dengan demikian",
        "oleh karena itu",
    ),
    "en": (
        "moreover",
        "furthermore",
        "additionally",
        "in addition",
        "it is worth noting",
        "it is important to note",
        "in conclusion",
        "overall",
    ),
}
ID_NOT_ONLY = re.compile(r"\btidak hanya\b.+?\btetapi juga\b", re.IGNORECASE)
POLITE_REQUEST = re.compile(r"(?:could|would|can|will) (?:you|i)\b|(?:bisakah|bolehkah)\b", re.I)
# Required by official letter formats. These are reported but never counted as connectors.
OFFICIAL_FORMULAS = re.compile(
    r"sehubungan dengan (?:surat|nomor)|demikian (?:disampaikan|surat|nota|laporan|pengumuman)|"
    r"atas perhatian",
    re.IGNORECASE,
)
INTENSIFIERS = {
    "id": ("sangat", "signifikan", "komprehensif", "optimal", "secara efektif"),
    "en": (
        "very",
        "significantly",
        "comprehensive",
        "robust",
        "seamless",
        "leverage",
        "delve",
        "crucial",
    ),
}
TRIPLET = {
    language: re.compile(
        r"([^\s,.;:]+(?:\s[^\s,.;:]+)?),\s"
        r"([^\s,.;:]+(?:\s[^\s,.;:]+)?),?\s" + word + r"\s[^\s,.;:]+",
        re.IGNORECASE,
    )
    for language, word in (("id", "dan"), ("en", "and"))
}
NUMBER_WORDS = {
    **dict(zip("one two three four five six seven eight nine ten".split(), range(1, 11))),
    **dict(
        zip("satu dua tiga empat lima enam tujuh delapan sembilan sepuluh".split(), range(1, 11))
    ),
    **{str(number): number for number in range(1, 11)},
}
COUNT_NOUNS = "hal|aturan|langkah|poin|tahap|alasan|things|rules|steps|points|reasons"
COUNT_RE = re.compile(
    r"(?<![\w-])(?<!atau )(?<!or )(" + "|".join(NUMBER_WORDS) + r")\s+(?:" + COUNT_NOUNS + r")\b",
    re.IGNORECASE,
)
DATE_MONTHS = set(MONTHS.lower().split("|")) | set(
    "october jan feb mar apr jun jul aug agu sep sept oct okt nov dec des".split()
)
NOT_COUNT_BEFORE = DATE_MONTHS | set(
    "or atau salah tanggal tgl date pukul jam pasal ayat section article clause nomor no number "
    "page halaman bab chapter rp idr usd".split()
)
NOT_ONE_BEFORE = set("this that the no each every any which another".split())
NOT_COUNT_AFTER = DATE_MONTHS | set(
    "of dari or atau and dan per to sampai hingga more lebih ribu juta miliar triliun rupiah "
    "dolar thousand million billion trillion dollars persen percent am pm pagi siang sore malam "
    "hari minggu bulan tahun jam menit days weeks months years hours minutes should must can "
    "may might will".split()
)
STATED_NUMBER = re.compile(
    r"(?<![\w.,/:$-])(" + "|".join(NUMBER_WORDS) + r")\s+([^\W\d_]+)", re.IGNORECASE
)
LIST_ITEM = re.compile(r"^(\s*)(?:[-*+•]|\d+[.)])\s+")
WORD = re.compile(r"[^\W_]+(?:[-'’/][^\W_]+)*")

LOCK_PATTERNS = (
    ("url", re.compile(r"https?://\S+|www\.\S+")),
    ("document_number", re.compile(r"\b[A-Z0-9]*\d[A-Z0-9]*(?:[-/][A-Z0-9]+)+\b|\b[A-Z]+-\d+\b")),
    ("date", re.compile(rf"\b\d{{1,2}}\s+(?:{MONTHS})(?:\s+\d{{4}})?\b")),
    ("money", re.compile(r"(?:Rp\s?|\$)\d[\d.,]*\d|(?:Rp\s?|\$)\d")),
    ("percentage", re.compile(r"\b\d[\d.,]*\s?(?:%|persen|percent)")),
    ("number", re.compile(r"(?<![\w.,])\d(?:[\d.,:]*\d)?(?![\w])")),
)
REFERENCE = re.compile(
    r"\b(?:Pasal\s+\d+[A-Z]?(?:\s+ayat\s+\(\d+\))?(?:\s+huruf\s+[a-z])?"
    r"|(?:Section|Article|Clause)\s+\d+[A-Za-z]?(?:\(\d+\))*)"
)
QUOTE = re.compile(r"\"[^\"\n]+\"|“[^”\n]+”")
PASAL_LINE = re.compile(r"^\s*Pasal\s+\d+", re.IGNORECASE)
AYAT_LINE = re.compile(r"^\s*\(\d+\)\s*\S")
STEP_LINE = re.compile(r"^\s*\d+[.)]\s+\S")
NOT_NAME_START = {"Hi", "Hello", "Hey", "Dear", "Halo", "Hai", "Yth"}
CAPITALIZED = re.compile(r"^[A-Z][\w'’/-]*$")
GLOSSARY_LINE = re.compile(r"^-\s+(.+?)(?:\s+\(|:\s|$)")


def rate(count: int | float, total: int) -> float:
    """Return count per 100 units, rounded to two places."""
    return round(100 * count / total, 2) if total else 0.0


def words_of(text: str) -> list[str]:
    return WORD.findall(text)


def detect_language(text: str) -> str:
    """Pick the language whose stopwords are most common in the text."""
    tokens = [token.lower() for token in words_of(text)]
    scores = {language: sum(t in words for t in tokens) for language, words in STOPWORDS.items()}
    return "en" if scores["en"] > scores["id"] else "id"


def clean_line(line: str) -> str:
    """Remove Markdown decoration and list markers from a line."""
    line = re.sub(r"^\s*#{1,6}\s+", "", line)
    line = LIST_ITEM.sub("", line)
    return line.replace("**", "").replace("__", "").strip()


def split_sentences(text: str) -> list[str]:
    """Split text into sentences. Short unpunctuated lines such as sign-offs are dropped."""
    sentences = []
    for raw in text.splitlines():
        line = clean_line(raw)
        if not line:
            continue
        line = re.sub(rf"\b({ABBREVIATIONS})\.", lambda m: m.group(1) + DOT, line)
        for part in re.split(r"(?<=[.!?])\s+(?=[\"“(]?[A-Z0-9])", line):
            part = part.replace(DOT, ".").strip()
            if len(words_of(part)) > 3 or re.search(r"[.!?]$", part):
                sentences.append(part)
    return sentences


def sentence_stats(sentences: list[str]) -> dict:
    lengths = [len(words_of(sentence)) for sentence in sentences]
    if not lengths:
        return {
            "count": 0,
            "mean_length": 0.0,
            "std_dev": 0.0,
            "share_under_8": 0.0,
            "share_over_30": 0.0,
            "longest_uniform_run": 0,
        }
    longest = run = 1
    for previous, current in zip(lengths, lengths[1:]):
        run = run + 1 if abs(current - previous) <= 3 else 1
        longest = max(longest, run)
    return {
        "count": len(lengths),
        "mean_length": round(statistics.mean(lengths), 2),
        "std_dev": round(statistics.pstdev(lengths), 2),
        "share_under_8": rate(sum(length < 8 for length in lengths), len(lengths)),
        "share_over_30": rate(sum(length > 30 for length in lengths), len(lengths)),
        "longest_uniform_run": longest,
    }


def find_light_verbs(text: str, language: str) -> list[str]:
    if language == "id":
        pattern = rf"\b({ID_LIGHT_VERBS})\s+(?:proses\s+)?([^\W\d_]+)"
        return [
            match.group(0)
            for match in re.finditer(pattern, text, re.IGNORECASE)
            if match.group(2).lower() in ID_LIGHT_NOUNS
            or ID_LIGHT_NOUN_SUFFIX.search(match.group(2).lower())
            or ID_PE_AN.match(match.group(2).lower())
        ]
    hits = []
    for match in re.finditer(rf"\b({EN_LIGHT_VERBS})\b", text, re.IGNORECASE):
        following = re.findall(r"[^\W\d_]+", text[match.end() : match.end() + 60])[:3]
        index = 1 if following and following[0].lower() in EN_DETERMINERS else 0
        for offset, word in enumerate(following[index : index + 2]):
            lower = word.lower()
            if lower in EN_NOT_NOMINAL:
                continue
            if lower in EN_LIGHT_NOUNS or EN_LIGHT_NOUN_SUFFIX.search(lower):
                hits.append(f"{match.group(0)} {' '.join(following[: index + offset + 1])}")
                break
    hits.extend(match.group(0) for match in EN_CONDUCT_OF.finditer(text))
    return hits


def is_nominal(token: str, language: str) -> bool:
    token = token.lower()
    if language == "id":
        return bool(ID_NOMINAL.match(token)) and token not in ID_NOT_NOMINAL
    return bool(EN_NOMINAL.match(token)) and token not in EN_NOT_NOMINAL


def find_nominalizations(text: str, language: str) -> tuple[list[str], list[str]]:
    """Return nominalized words and chains of two or more."""
    found = []
    chains = []
    for sentence in split_sentences(text):
        tokens = words_of(sentence)
        run: list[str] = []
        index = 0
        while index < len(tokens):
            token = tokens[index]
            if is_nominal(token, language):
                found.append(token)
                run.append(token)
                index += 1
                continue
            lower = token.lower()
            linked = language == "en" and lower == "of" and run
            if linked:
                next_index = index + 1
                if next_index < len(tokens) and tokens[next_index].lower() == "the":
                    next_index += 1
                if next_index < len(tokens) and is_nominal(tokens[next_index], language):
                    index = next_index
                    continue
            if len(run) >= 2:
                chains.append(" ".join(run))
            run = []
            index += 1
        if len(run) >= 2:
            chains.append(" ".join(run))
    return found, chains


def find_connectors(sentences: list[str], language: str) -> tuple[list[str], int, list[str]]:
    """Return connector hits, adjacent stacks, and official formulas that were not counted."""
    hits = []
    formulas = []
    openers = []
    phrases = "|".join(re.escape(phrase) for phrase in CONNECTORS[language])
    clause_initial = re.compile(rf"(?:^|[,;:]\s+)({phrases})\b", re.IGNORECASE)
    for sentence in sentences:
        formula = OFFICIAL_FORMULAS.search(sentence)
        if formula:
            formulas.append(formula.group(0))
        matches = [match.group(1) for match in clause_initial.finditer(sentence)]
        hits.extend(matches)
        if language == "id":
            hits.extend(match.group(0) for match in ID_NOT_ONLY.finditer(sentence))
        starts = clause_initial.match(sentence)
        openers.append(bool(starts) and starts.start(1) == 0)
    stacks = sum(first and second for first, second in zip(openers, openers[1:]))
    return hits, stacks, formulas


def find_phrases(text: str, phrases: tuple[str, ...]) -> list[str]:
    pattern = "|".join(re.escape(phrase) for phrase in phrases)
    return [m.group(0) for m in re.finditer(rf"\b(?:{pattern})\b", text, re.IGNORECASE)]


def count_list_items(lines: list[str], start: int) -> int:
    """Count top-level items of a list beginning within three lines of start."""
    position = start
    nonblank = 0
    while position < len(lines) and nonblank < 3:
        if lines[position].strip():
            if LIST_ITEM.match(lines[position]):
                break
            nonblank += 1
        position += 1
    else:
        return 0
    if position >= len(lines):
        return 0
    indent = len(LIST_ITEM.match(lines[position]).group(1))
    count = 0
    for line in lines[position:]:
        if not line.strip():
            continue
        item = LIST_ITEM.match(line)
        if item:
            if len(item.group(1)) < indent:
                break
            count += len(item.group(1)) == indent
        elif len(line) - len(line.lstrip()) <= indent:
            break
    return count


def stated_count(line: str) -> re.Match | None:
    """Return the first number in line that states how many things follow."""
    for match in STATED_NUMBER.finditer(line):
        before = line[: match.start()].split()
        previous = before[-1].strip(".,").lower() if before else ""
        if previous in NOT_COUNT_BEFORE or match.group(2).lower() in NOT_COUNT_AFTER:
            continue
        if match.group(1).lower() == "one" and previous in NOT_ONE_BEFORE:
            continue
        return match
    return None


def check_counts(text: str) -> list[dict]:
    """Compare stated counts with the list that follows.

    A count is a number word and a counting noun ("lima hal") on any line, or a number and
    any other word ("three documents") on a line that ends in a colon.
    """
    lines = text.splitlines()
    mismatches = []
    for index, line in enumerate(lines):
        if LIST_ITEM.match(line):
            continue
        match = COUNT_RE.search(line)
        if match is not None and re.match(r"\s+(?:atau|or)\b", line[match.end(1) :], re.IGNORECASE):
            match = None
        if match is None and line.rstrip().rstrip("*_").endswith(":"):
            match = stated_count(line)
        if match is None:
            continue
        found = count_list_items(lines, index + 1)
        expected = NUMBER_WORDS[match.group(1).lower()]
        if found and found != expected:
            mismatches.append(
                {"phrase": match.group(0), "line": index + 1, "expected": expected, "found": found}
            )
    return mismatches


def count_metric(hits: list, words: int) -> dict:
    return {"count": len(hits), "per_100_words": rate(len(hits), words)}


def sentence_metric(hits: list, sentences: int) -> dict:
    return {"count": len(hits), "per_100_sentences": rate(len(hits), sentences)}


def analyze(text: str, language: str | None = None) -> dict:
    """Compute all metrics for a text."""
    language = language or detect_language(text)
    words = len(words_of(text))
    sentences = split_sentences(text)
    total_sentences = len(sentences)

    light_verbs = find_light_verbs(text, language)
    nominalizations, chains = find_nominalizations(text, language)
    connectors, stacks, formulas = find_connectors(sentences, language)
    triplets = [
        m.group(0)
        for s in sentences
        for m in TRIPLET[language].finditer(s)
        if m.group(1).lower() not in CONNECTORS[language]
    ]
    intensifiers = find_phrases(text, INTENSIFIERS[language])
    questions = [
        sentence
        for sentence, following in zip(sentences, sentences[1:])
        if sentence.endswith("?")
        and not following.endswith("?")
        and not POLITE_REQUEST.match(sentence)
    ]
    lines = [line for line in text.splitlines() if line.strip()]
    bullets = [line for line in lines if LIST_ITEM.match(line)]
    mismatches = check_counts(text)

    metrics = {
        "sentences": sentence_stats(sentences),
        "light_verbs": count_metric(light_verbs, words),
        "nominalizations": count_metric(nominalizations, words),
        "nominalization_chains": count_metric(chains, words),
        "connectors": {**sentence_metric(connectors, total_sentences), "stacked_pairs": stacks},
        "triplets": sentence_metric(triplets, total_sentences),
        "intensifiers": count_metric(intensifiers, words),
        "em_dashes": count_metric(re.findall("—", text), words),
        "rhetorical_questions": sentence_metric(questions, total_sentences),
        "bullet_lines": {"count": len(bullets), "ratio": rate(len(bullets), len(lines))},
        "count_mismatches": {"count": len(mismatches)},
    }
    if language == "id":
        metrics["merupakan"] = count_metric(find_phrases(text, ("merupakan",)), words)
        metrics["adalah"] = count_metric(find_phrases(text, ("adalah",)), words)

    return {
        "lang": language,
        "words": words,
        "sentences": total_sentences,
        "metrics": metrics,
        "hits": {
            "light_verbs": light_verbs,
            "nominalization_chains": chains,
            "connectors": connectors,
            "official_formulas_not_counted": formulas,
            "triplets": triplets,
            "intensifiers": intensifiers,
            "rhetorical_questions": questions,
            "count_mismatches": mismatches,
        },
        "flags": [
            f'stated "{item["phrase"]}" on line {item["line"]}: '
            f"expected {item['expected']}, found {item['found']}"
            for item in mismatches
        ],
    }


def flatten(report: dict) -> dict[str, float]:
    """Return every numeric metric as a flat name to value mapping."""
    flat: dict[str, float] = {"words": report["words"]}
    for name, values in report["metrics"].items():
        for key, value in values.items():
            flat[f"{name}.{key}"] = value
    return flat


def compare(before: str, after: str, language: str | None = None) -> dict:
    """Return per-metric before, after and delta values."""
    language = language or detect_language(before)
    first = flatten(analyze(before, language))
    second = flatten(analyze(after, language))
    return {
        "lang": language,
        "deltas": {
            key: {
                "before": first[key],
                "after": second.get(key, 0),
                "delta": round(second.get(key, 0) - first[key], 2),
            }
            for key in first
        },
    }


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def read_glossary(path: Path) -> list[str]:
    """Return the terms listed in a glossary file."""
    terms = []
    for line in path.read_text(encoding="utf-8").splitlines():
        match = GLOSSARY_LINE.match(line)
        if match:
            terms.append(match.group(1).strip())
    return terms


def proper_names(text: str) -> list[str]:
    """Return runs of two or more capitalized tokens that do not start a sentence."""
    names = []
    for sentence in split_sentences(text):
        tokens = sentence.split()
        run: list[str] = []
        for index, raw in enumerate(tokens):
            token = raw.strip('"“”()[],;:.!?')
            if raw.startswith("("):
                if len(run) >= 2:
                    names.append(" ".join(run))
                run = []
            capitalized = (
                index > 0 and bool(CAPITALIZED.match(token)) and token not in NOT_NAME_START
            )
            if capitalized:
                run.append(token)
            if not capitalized or raw[-1] in ",;:.!?)":
                if len(run) >= 2:
                    names.append(" ".join(run))
                run = []
        if len(run) >= 2:
            names.append(" ".join(run))
    return names


def locked_segments(text: str, terms: list[str]) -> list[tuple[str, str]]:
    """Extract the (kind, segment) pairs that must survive unchanged."""
    segments: list[tuple[str, str]] = []
    lines = text.splitlines()
    remaining = []
    in_pasal = False
    for line in lines:
        if PASAL_LINE.match(line):
            in_pasal = True
            segments.append(("pasal_text", normalize(line)))
            remaining.append("")
        elif in_pasal and AYAT_LINE.match(line):
            segments.append(("pasal_text", normalize(line)))
            remaining.append("")
        elif STEP_LINE.match(line):
            in_pasal = False
            segments.append(("numbered_step", normalize(line)))
            remaining.append("")
        else:
            if line.strip():
                in_pasal = False
            remaining.append(line)
    body = "\n".join(remaining)

    for match in QUOTE.finditer(body):
        segments.append(("quotation", normalize(match.group(0))))
    body = QUOTE.sub(" ", body)
    for match in REFERENCE.finditer(body):
        segments.append(("reference", normalize(match.group(0))))
    body = REFERENCE.sub(" ", body)
    for kind, pattern in LOCK_PATTERNS:
        for match in pattern.finditer(body):
            segments.append((kind, normalize(match.group(0)).rstrip(".,;:")))
        body = pattern.sub(" ", body)

    for term in terms:
        if re.search(rf"(?<!\w){re.escape(term)}(?!\w)", text):
            segments.append(("glossary_term", term))
    for name in proper_names(text):
        segments.append(("proper_name", name))

    unique = []
    seen = set()
    for item in segments:
        if item[1] and item not in seen:
            seen.add(item)
            unique.append(item)
    return unique


def segment_present(kind: str, segment: str, result: str) -> bool:
    if kind in ("number", "percentage"):
        return re.search(rf"(?<![\d]){re.escape(segment)}(?![\d])", result) is not None
    return segment in result


def check_locked(original: str, result: str, terms: list[str]) -> dict:
    """Report locked segments of original that are missing or altered in result."""
    normalized_result = normalize(result)
    result_lines = [normalize(line) for line in result.splitlines() if line.strip()]
    problems = []
    segments = locked_segments(original, terms)
    for kind, segment in segments:
        if segment_present(kind, segment, normalized_result):
            continue
        close = None
        if kind in ("pasal_text", "numbered_step", "quotation"):
            matches = difflib.get_close_matches(segment, result_lines, n=1, cutoff=0.6)
            close = matches[0] if matches else None
        problems.append(
            {
                "kind": kind,
                "segment": segment,
                "status": "altered" if close else "missing",
                "found": close,
            }
        )
    return {"checked": len(segments), "problems": problems, "ok": not problems}


def read_input(path: str | None) -> str:
    if path in (None, "-"):
        return sys.stdin.read()
    return Path(path).read_text(encoding="utf-8")


def format_report(report: dict) -> str:
    lines = [f"lang: {report['lang']}  words: {report['words']}  sentences: {report['sentences']}"]
    lines += [f"{key}: {value}" for key, value in flatten(report).items() if key != "words"]
    for name, hits in report["hits"].items():
        if hits:
            lines.append(f"hits.{name}: {json.dumps(hits, ensure_ascii=False)}")
    lines += [f"flag: {flag}" for flag in report["flags"]]
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Text metrics for sf-humanizer.")
    parser.add_argument("file", nargs="?", help="text file; reads stdin if omitted")
    parser.add_argument("--lang", choices=("id", "en"), help="language; detected if omitted")
    parser.add_argument("--json", action="store_true", help="print JSON")
    parser.add_argument("--compare", nargs=2, metavar=("BEFORE", "AFTER"))
    parser.add_argument("--check-locked", nargs=2, metavar=("ORIGINAL", "RESULT"))
    parser.add_argument("--glossary", nargs="+", action="extend", default=[], metavar="FILE")
    parser.add_argument("--terms", default="", help="extra locked terms, comma separated")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    if args.compare:
        before, after = (read_input(path) for path in args.compare)
        result = compare(before, after, args.lang)
        if args.json:
            print(json.dumps(result, ensure_ascii=False, indent=2))
        else:
            for key, values in result["deltas"].items():
                print(f"{key}: {values['before']} -> {values['after']} ({values['delta']:+})")
        return 0

    if args.check_locked:
        original, result_text = (read_input(path) for path in args.check_locked)
        language = args.lang or detect_language(original)
        terms = [term.strip() for term in args.terms.split(",") if term.strip()]
        paths = [Path(path) for path in args.glossary]
        default = Path(__file__).resolve().parent.parent / "references" / f"glossary-{language}.md"
        if default.is_file():
            paths.append(default)
        for path in paths:
            terms += read_glossary(path)
        report = check_locked(original, result_text, terms)
        if args.json:
            print(json.dumps(report, ensure_ascii=False, indent=2))
        else:
            print(f"checked: {report['checked']}  problems: {len(report['problems'])}")
            for problem in report["problems"]:
                print(f"{problem['status']} ({problem['kind']}): {problem['segment']}")
        return 0 if report["ok"] else 1

    report = analyze(read_input(args.file), args.lang)
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(format_report(report))
    return 0


if __name__ == "__main__":
    sys.exit(main())
