from __future__ import annotations

import importlib.util
import io
import json
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent

spec = importlib.util.spec_from_file_location(
    "metrics", REPO_ROOT / "skill" / "sf-humanizer" / "scripts" / "metrics.py"
)
metrics = importlib.util.module_from_spec(spec)
sys.modules["metrics"] = metrics
spec.loader.exec_module(metrics)


@pytest.mark.parametrize(
    ("text", "language", "expected"),
    [
        ("Panitia melakukan evaluasi penawaran.", "id", "melakukan evaluasi"),
        ("Unit itu memberikan kontribusi besar.", "id", "memberikan kontribusi"),
        ("Tim melaksanakan koordinasi dengan PPK.", "id", "melaksanakan koordinasi"),
        ("Tim melakukan proses verifikasi dokumen.", "id", "melakukan proses verifikasi"),
        ("We will conduct an evaluation of the bids.", "en", "conduct an evaluation"),
        ("They carried out a review.", "en", "carried out a review"),
        ("Please provide assistance today.", "en", "provide assistance"),
    ],
)
def test_light_verbs_found(text: str, language: str, expected: str) -> None:
    assert expected in metrics.find_light_verbs(text, language)


@pytest.mark.parametrize(
    ("text", "language"),
    [("Panitia melakukan hal itu.", "id"), ("Make sure the box is here.", "en")],
)
def test_light_verbs_ignored(text: str, language: str) -> None:
    assert metrics.find_light_verbs(text, language) == []


def test_indonesian_nominalization_chain() -> None:
    _, chains = metrics.find_nominalizations(
        "Divisi fokus pada peningkatan pelaksanaan pengawasan kontrak.", "id"
    )
    assert chains == ["peningkatan pelaksanaan pengawasan"]


def test_english_nominalization_chain_through_of() -> None:
    found, chains = metrics.find_nominalizations(
        "The focus is the implementation of the assessment today.", "en"
    )
    assert chains == ["implementation assessment"]
    assert len(found) == 2


def test_excluded_words_are_not_nominalizations() -> None:
    found, _ = metrics.find_nominalizations("The government asked one question.", "en")
    assert found == []


@pytest.mark.parametrize(
    ("sentence", "language", "count"),
    [
        ("Selain itu, Penyedia wajib melapor.", "id", 1),
        ("Penyedia, oleh karena itu, wajib melapor.", "id", 1),
        ("Moreover, the vendor must report.", "en", 1),
        ("PPK tidak hanya memeriksa, tetapi juga menilai.", "id", 1),
        ("Penyedia wajib melapor selain itu juga hadir.", "id", 0),
        ("Sehubungan dengan surat nomor 5, kami menjawab.", "id", 0),
        ("Demikian disampaikan untuk diketahui.", "id", 0),
        ("Atas perhatian Saudara, kami berterima kasih.", "id", 0),
    ],
)
def test_connectors(sentence: str, language: str, count: int) -> None:
    hits, _, _ = metrics.find_connectors([sentence], language)
    assert len(hits) == count


def test_official_formula_is_reported_but_not_counted() -> None:
    report = metrics.analyze("Demikian disampaikan untuk diketahui bersama.", "id")
    assert report["metrics"]["connectors"]["count"] == 0
    assert report["hits"]["official_formulas_not_counted"]


def test_stacked_connectors() -> None:
    text = "Selain itu, kami hadir di sana. Oleh karena itu, kami menunggu di sana."
    assert metrics.analyze(text, "id")["metrics"]["connectors"]["stacked_pairs"] == 1


@pytest.mark.parametrize(
    ("text", "language"),
    [
        ("Proses harus transparan, terbuka, dan jelas.", "id"),
        ("It is fast, cheap, and safe.", "en"),
    ],
)
def test_triplets(text: str, language: str) -> None:
    assert metrics.analyze(text, language)["metrics"]["triplets"]["count"] == 1


def test_sentence_stats_and_uniform_run() -> None:
    text = "Satu dua tiga empat lima. Satu dua tiga empat lima. Satu dua tiga empat lima."
    stats = metrics.analyze(text, "id")["metrics"]["sentences"]
    assert stats["count"] == 3
    assert stats["mean_length"] == 5
    assert stats["longest_uniform_run"] == 3
    assert stats["share_under_8"] == 100


def test_abbreviation_does_not_split_sentence() -> None:
    assert len(metrics.split_sentences("Yth. Direktur PT Contoh menerima surat ini.")) == 1


def test_per_language_word_metrics() -> None:
    report = metrics.analyze("Ini merupakan hal yang sangat baik — dan ini adalah contoh.", "id")
    values = report["metrics"]
    assert values["merupakan"]["count"] == 1
    assert values["adalah"]["count"] == 1
    assert values["intensifiers"]["count"] == 1
    assert values["em_dashes"]["count"] == 1
    assert "merupakan" not in metrics.analyze("This is a test of it.", "en")["metrics"]


def test_rhetorical_question_and_bullets() -> None:
    text = "Mengapa harus diulang? Karena harga berubah.\n- satu butir\n- dua butir\n"
    values = metrics.analyze(text, "id")["metrics"]
    assert values["rhetorical_questions"]["count"] == 1
    assert values["bullet_lines"]["count"] == 2


def items(number: int) -> str:
    return "".join(f"- butir {index}\n" for index in range(number))


def test_count_mismatch_reported() -> None:
    report = metrics.analyze(f"Ada lima hal yang perlu dilihat:\n\n{items(6)}", "id")
    assert report["hits"]["count_mismatches"][0]["expected"] == 5
    assert report["hits"]["count_mismatches"][0]["found"] == 6
    assert "expected 5, found 6" in report["flags"][0]


@pytest.mark.parametrize(
    "intro", ["Ada lima hal:", "Ada 5 langkah:", "Five things to check:", "There are five steps:"]
)
def test_count_match_passes(intro: str) -> None:
    assert metrics.check_counts(f"{intro}\n\n{items(5)}") == []


@pytest.mark.parametrize("intro", ["Ada dua atau tiga hal:", "There are two or three things:"])
def test_count_ranges_ignored(intro: str) -> None:
    assert metrics.check_counts(f"{intro}\n\n{items(5)}") == []


def test_count_without_list_ignored() -> None:
    assert metrics.check_counts("Ada lima hal yang penting.\n\nLalu paragraf lain.\n") == []


def test_compare_reports_deltas() -> None:
    result = metrics.compare("Panitia melakukan evaluasi dokumen.", "Panitia mengevaluasi.", "id")
    assert result["deltas"]["light_verbs.count"] == {"before": 1, "after": 0, "delta": -1}


ORIGINAL = """Pasal 7
(2) HPS ditetapkan paling lambat 14 hari kerja.

Nomor ND-001/XI/2026 berlaku sejak 20 November 2026, senilai Rp1.250.000.000, naik 10%.
Dokumen ini disusun oleh Pokja Pemilihan bersama Kepala Divisi Pengadaan.
Ia menulis "harus selesai hari ini" di https://example.org/doc.

1. Penyedia menyerahkan tagihan.
"""


def problems(result: str, terms: list[str] | None = None) -> list[dict]:
    return metrics.check_locked(ORIGINAL, result, terms or [])["problems"]


def test_check_locked_passes_on_identical_text() -> None:
    assert problems(ORIGINAL, ["HPS"]) == []


def test_check_locked_allows_surrounding_changes() -> None:
    result = ORIGINAL.replace("Dokumen ini disusun oleh", "Penyusunnya")
    assert problems(result) == []


@pytest.mark.parametrize(
    ("old", "new", "kind"),
    [
        ("Rp1.250.000.000", "Rp1.350.000.000", "money"),
        ("20 November 2026", "21 November 2026", "date"),
        ("ND-001/XI/2026", "ND-002/XI/2026", "document_number"),
        ("10%", "12%", "percentage"),
        ("harus selesai hari ini", "harus selesai besok", "quotation"),
        ("https://example.org/doc", "https://example.org/x", "url"),
        ("Pokja Pemilihan", "Panitia Pemilihan", "proper_name"),
    ],
)
def test_check_locked_catches_changed_segment(old: str, new: str, kind: str) -> None:
    assert kind in [problem["kind"] for problem in problems(ORIGINAL.replace(old, new))]


def test_check_locked_reports_altered_pasal_text() -> None:
    found = problems(ORIGINAL.replace("paling lambat 14 hari", "paling cepat 14 hari"))
    pasal = [problem for problem in found if problem["kind"] == "pasal_text"]
    assert pasal[0]["status"] == "altered"


def test_check_locked_catches_changed_step() -> None:
    found = problems(ORIGINAL.replace("Penyedia menyerahkan", "Vendor menyerahkan"))
    assert "numbered_step" in [problem["kind"] for problem in found]


def test_check_locked_catches_missing_glossary_term() -> None:
    found = problems(ORIGINAL.replace("Nomor ND", "HPS Nomor ND"), ["HPS"])
    assert found == []
    original = "HPS ditetapkan hari ini."
    result = metrics.check_locked(original, "Harga ditetapkan hari ini.", ["HPS"])
    assert result["problems"][0]["kind"] == "glossary_term"


def test_read_glossary(tmp_path: Path) -> None:
    path = tmp_path / "glossary.md"
    path.write_text("# T\n\n- HPS (Harga)\n- Tender\n- Pengadaan Langsung: desc\n", "utf-8")
    assert metrics.read_glossary(path) == ["HPS", "Tender", "Pengadaan Langsung"]


@pytest.mark.parametrize(
    ("text", "language"),
    [
        ("Kami akan mengirim dokumen yang diminta untuk rapat dan laporan itu.", "id"),
        ("We will send the document that was requested for the meeting and the report.", "en"),
    ],
)
def test_detect_language(text: str, language: str) -> None:
    assert metrics.detect_language(text) == language


def test_main_reads_stdin_and_prints_json(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.setattr(sys, "stdin", io.StringIO("Panitia melakukan evaluasi dokumen hari ini."))
    assert metrics.main(["--json"]) == 0
    report = json.loads(capsys.readouterr().out)
    assert set(report) == {"lang", "words", "sentences", "metrics", "hits", "flags"}
    assert report["metrics"]["light_verbs"]["count"] == 1


def test_main_text_output(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    path = tmp_path / "text.txt"
    path.write_text("Panitia melakukan evaluasi dokumen.", "utf-8")
    assert metrics.main([str(path), "--lang", "id"]) == 0
    assert "light_verbs.count: 1" in capsys.readouterr().out


def test_main_compare(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    first = tmp_path / "a.txt"
    second = tmp_path / "b.txt"
    first.write_text("Panitia melakukan evaluasi dokumen.", "utf-8")
    second.write_text("Panitia mengevaluasi dokumen.", "utf-8")
    assert metrics.main(["--compare", str(first), str(second), "--lang", "id"]) == 0
    assert "light_verbs.count: 1 -> 0 (-1)" in capsys.readouterr().out


def test_main_check_locked_exit_codes(tmp_path: Path) -> None:
    first = tmp_path / "a.txt"
    second = tmp_path / "b.txt"
    first.write_text("Nilai kontrak Rp100.000 saja.", "utf-8")
    second.write_text("Nilai kontrak Rp100.000 saja.", "utf-8")
    assert metrics.main(["--check-locked", str(first), str(second), "--lang", "id"]) == 0
    second.write_text("Nilai kontrak Rp200.000 saja.", "utf-8")
    assert metrics.main(["--check-locked", str(first), str(second), "--lang", "id"]) == 1


def test_main_check_locked_uses_terms_option(tmp_path: Path) -> None:
    first = tmp_path / "a.txt"
    second = tmp_path / "b.txt"
    first.write_text("Tim Reviu hadir hari ini.", "utf-8")
    second.write_text("Mereka hadir hari ini.", "utf-8")
    args = ["--check-locked", str(first), str(second), "--terms", "Tim Reviu"]
    assert metrics.main([*args, "--lang", "id", "--json"]) == 1
