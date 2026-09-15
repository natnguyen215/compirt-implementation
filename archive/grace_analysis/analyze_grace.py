#!/usr/bin/env python3
"""Reproduce the exploratory analysis of the local GRACE data.

The local ``grace_data`` directory contains the QANTA retrieval corpus and
several roster-summary pickles.  The raw live-competition buzz records are in
the authors' encrypted public archive, supplied with ``--buzz-archive``.
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import os
import pickle
import re
import tempfile
import zipfile
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "grace_mpl_cache"))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ARCHIVE_URL = (
    "https://raw.githubusercontent.com/Pinafore/advcalibration/main/"
    "%5Bpublic%5DALL_final_buzzpoints_enc.zip"
)
ARCHIVE_PASSWORD = b"buzzbuzz"
EXPECTED_ARCHIVE_SHA256 = "05eb4e5965c31d97182882e814c0365a0dd4caba9519f4fc354e4660f65a84c0"
BUZZ_RE = re.compile(r"^\[([^,]+),\s*([+-])\]$")
PACKET_RE = re.compile(r"packet(\d+)_buzzpoints\.json$")
MODEL_NAMES = {
    "M1": "GPT-4",
    "M2": "GPT-4o",
    "M3": "Mistral-7b-Instruct",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def natural_team_key(team: str) -> tuple[str, int]:
    match = re.match(r"([A-Za-z]+)(\d+)$", team)
    return (match.group(1), int(match.group(2))) if match else (team, 0)


def coarse_category(category: str) -> str:
    if category in {"Other Arts", "Other Fine Arts"} or "Music" in category or "Painting" in category:
        return "Arts"
    if "Hist" in category:
        return "History"
    if "Lit" in category or category == "World/Other":
        return "Literature"
    if category in {"Religion", "Social Science", "Philosophy", "Myth", "Myth/Other Academic"}:
        return "RMPSS"
    if category in {"Biology", "Physics", "Chemistry", "Other Sci"}:
        return "Science"
    if category in {"Geo/CE", "Geo/CE/other"}:
        return "Geo/CE"
    return category


def load_live_archive(path: Path) -> tuple[pd.DataFrame, pd.DataFrame]:
    event_rows: list[dict[str, object]] = []
    question_rows: list[dict[str, object]] = []

    with zipfile.ZipFile(path) as archive:
        members: list[tuple[int, str]] = []
        for name in archive.namelist():
            match = PACKET_RE.search(name)
            if match:
                members.append((int(match.group(1)), name))

        for packet, name in sorted(members):
            payload = json.loads(archive.read(name, pwd=ARCHIVE_PASSWORD))
            for packet_question_number, question in enumerate(payload, start=1):
                question_words = len(question["question"].split())
                key = f"p{packet}:q{question['tossup_index']}"
                question_events: list[dict[str, object]] = []

                for event_order, item in enumerate(question["position"], start=1):
                    if len(item) != 1:
                        raise ValueError(f"Expected one position per event, got {item!r}")
                    position_text, label = next(iter(item.items()))
                    match = BUZZ_RE.fullmatch(label)
                    if not match:
                        raise ValueError(f"Unrecognized buzz label: {label!r}")
                    team, result = match.groups()
                    position_words = int(position_text)
                    row = {
                        "question_key": key,
                        "packet": packet,
                        "packet_question_number": packet_question_number,
                        "tossup_index": str(question["tossup_index"]),
                        "category_raw": question["category"],
                        "category_group": coarse_category(question["category"]),
                        "question_words": question_words,
                        "event_order": event_order,
                        "team": team,
                        "team_type": "Model" if team.startswith("M") else "Human",
                        "model_name": MODEL_NAMES.get(team, ""),
                        "correct": result == "+",
                        "result": result,
                        "position_words": position_words,
                        "position_pct": 100.0 * position_words / question_words,
                    }
                    event_rows.append(row)
                    question_events.append(row)

                positions = [float(row["position_pct"]) for row in question_events]
                human_events = sum(row["team_type"] == "Human" for row in question_events)
                model_events = sum(row["team_type"] == "Model" for row in question_events)
                correct_events = sum(bool(row["correct"]) for row in question_events)
                question_rows.append(
                    {
                        "question_key": key,
                        "packet": packet,
                        "packet_question_number": packet_question_number,
                        "tossup_index": str(question["tossup_index"]),
                        "category_raw": question["category"],
                        "category_group": coarse_category(question["category"]),
                        "question_words": question_words,
                        "buzz_events": len(question_events),
                        "human_buzzes": human_events,
                        "model_buzzes": model_events,
                        "correct_buzzes": correct_events,
                        "incorrect_buzzes": len(question_events) - correct_events,
                        "accuracy": correct_events / len(question_events),
                        "earliest_position_pct": min(positions),
                        "latest_position_pct": max(positions),
                        "no_human_buzz": human_events == 0,
                        "no_model_buzz": model_events == 0,
                    }
                )

    events = pd.DataFrame(event_rows).sort_values(
        ["packet", "packet_question_number", "event_order"]
    )
    questions = pd.DataFrame(question_rows).sort_values(
        ["packet", "packet_question_number"]
    )
    return events, questions


def load_qanta_corpus(source_dir: Path) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for path in sorted(source_dir.glob("qanta.*.json.gz")):
        with gzip.open(path, "rt", encoding="utf-8") as handle:
            records = json.load(handle)
        for record in records:
            rows.append(
                {
                    "split": record["fold"],
                    "qanta_id": record["qanta_id"],
                    "category": record["category"],
                    "subcategory": record["subcategory"],
                    "tournament": record["tournament"],
                    "difficulty": record["difficulty"],
                    "year": record["year"],
                    "dataset": record["dataset"],
                    "gameplay": record["gameplay"],
                    "page_missing": record["page"] is None,
                    "proto_id_missing": record["proto_id"] is None,
                    "qdb_id_missing": record["qdb_id"] is None,
                    "question_words": len(record["text"].split()),
                    "clue_segments": len(record["tokenizations"]),
                    "text": record["text"],
                }
            )
    return pd.DataFrame(rows)


def grouped_event_summary(events: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    summary = (
        events.groupby(columns, observed=True)
        .agg(
            buzz_events=("correct", "size"),
            correct_buzzes=("correct", "sum"),
            median_position_pct=("position_pct", "median"),
            mean_position_pct=("position_pct", "mean"),
            q1_position_pct=("position_pct", lambda x: x.quantile(0.25)),
            q3_position_pct=("position_pct", lambda x: x.quantile(0.75)),
        )
        .reset_index()
    )
    summary["incorrect_buzzes"] = summary["buzz_events"] - summary["correct_buzzes"]
    summary["accuracy"] = summary["correct_buzzes"] / summary["buzz_events"]
    return summary


def write_tables(
    output_dir: Path,
    source_dir: Path,
    archive: Path,
    events: pd.DataFrame,
    questions: pd.DataFrame,
    qanta: pd.DataFrame,
) -> dict[str, pd.DataFrame]:
    data_dir = output_dir / "data"
    data_dir.mkdir(parents=True, exist_ok=True)

    events.to_csv(data_dir / "buzz_events.csv", index=False, float_format="%.4f")
    questions.to_csv(data_dir / "question_summary.csv", index=False, float_format="%.4f")

    team_summary = grouped_event_summary(events, ["team", "team_type", "model_name"])
    team_summary["packets_with_recorded_buzz"] = team_summary["team"].map(
        events.groupby("team")["packet"].nunique()
    )
    team_summary = team_summary.sort_values(
        "team", key=lambda x: x.map({t: i for i, t in enumerate(sorted(x.unique(), key=natural_team_key))})
    )
    team_summary.to_csv(data_dir / "team_summary.csv", index=False, float_format="%.4f")

    group_summary = grouped_event_summary(events, ["team_type"])
    group_summary.to_csv(data_dir / "team_type_summary.csv", index=False, float_format="%.4f")

    category_summary = grouped_event_summary(events, ["category_group", "team_type"])
    category_summary.to_csv(data_dir / "category_summary.csv", index=False, float_format="%.4f")

    packet_summary = grouped_event_summary(events, ["packet", "team_type"])
    packet_summary.to_csv(data_dir / "packet_summary.csv", index=False, float_format="%.4f")

    bin_edges = np.arange(0, 101, 10)
    events_with_bins = events.copy()
    events_with_bins["position_bin"] = pd.cut(
        events_with_bins["position_pct"], bins=bin_edges, right=False, include_lowest=True
    )
    position_bins = (
        events_with_bins.groupby(["team_type", "correct", "position_bin"], observed=False)
        .size()
        .rename("buzz_events")
        .reset_index()
    )
    position_bins["share_within_type_result"] = position_bins.groupby(
        ["team_type", "correct"], observed=True
    )["buzz_events"].transform(lambda x: x / x.sum())
    position_bins.to_csv(data_dir / "buzz_position_bins.csv", index=False, float_format="%.4f")

    timing_edges = [0, 25, 50, 75, 100]
    events_with_bands = events.copy()
    events_with_bands["timing_band"] = pd.cut(
        events_with_bands["position_pct"],
        bins=timing_edges,
        right=False,
        include_lowest=True,
        labels=["0-25%", "25-50%", "50-75%", "75-100%"],
    )
    timing_bands = (
        events_with_bands.groupby(["team_type", "timing_band"], observed=False)
        .agg(buzz_events=("correct", "size"), correct_buzzes=("correct", "sum"))
        .reset_index()
    )
    timing_bands["incorrect_buzzes"] = (
        timing_bands["buzz_events"] - timing_bands["correct_buzzes"]
    )
    timing_bands["accuracy"] = timing_bands["correct_buzzes"] / timing_bands["buzz_events"]
    timing_bands.to_csv(data_dir / "timing_band_summary.csv", index=False, float_format="%.4f")

    qanta_split = (
        qanta.groupby("split", observed=True)
        .agg(
            questions=("qanta_id", "size"),
            categories=("category", "nunique"),
            tournaments=("tournament", "nunique"),
            min_year=("year", "min"),
            max_year=("year", "max"),
            mean_question_words=("question_words", "mean"),
            median_question_words=("question_words", "median"),
            mean_clue_segments=("clue_segments", "mean"),
            missing_pages=("page_missing", "sum"),
            gameplay_questions=("gameplay", "sum"),
        )
        .reset_index()
    )
    qanta_split.to_csv(data_dir / "qanta_split_summary.csv", index=False, float_format="%.4f")

    qanta_category = (
        qanta.groupby(["split", "category"], observed=True)
        .size()
        .rename("questions")
        .reset_index()
    )
    qanta_category.to_csv(data_dir / "qanta_category_summary.csv", index=False)

    qanta_year = (
        qanta.groupby(["split", "year"], observed=True)
        .size()
        .rename("questions")
        .reset_index()
    )
    qanta_year.to_csv(data_dir / "qanta_year_summary.csv", index=False)

    qanta_tournaments = (
        qanta.groupby("tournament", observed=True)
        .size()
        .rename("questions")
        .sort_values(ascending=False)
        .reset_index()
    )
    qanta_tournaments.to_csv(data_dir / "qanta_tournament_summary.csv", index=False)

    input_paths = sorted(source_dir.rglob("*"))
    inventory = []
    for path in input_paths:
        if path.is_file():
            inventory.append(
                {
                    "input": str(path),
                    "bytes": path.stat().st_size,
                    "sha256": sha256(path),
                }
            )
    inventory.append(
        {
            "input": f"public GRACE archive ({ARCHIVE_URL})",
            "bytes": archive.stat().st_size,
            "sha256": sha256(archive),
        }
    )
    pd.DataFrame(inventory).to_csv(data_dir / "input_inventory.csv", index=False)

    summary_rows = [
        ("live_competition", "packets_in_public_archive", questions["packet"].nunique()),
        ("live_competition", "questions_in_public_archive", len(questions)),
        ("live_competition", "recorded_buzz_events", len(events)),
        ("live_competition", "teams_with_recorded_buzz", events["team"].nunique()),
        ("live_competition", "human_team_ids", events.query("team_type == 'Human'")["team"].nunique()),
        ("live_competition", "model_team_ids", events.query("team_type == 'Model'")["team"].nunique()),
        ("live_competition", "raw_category_labels", questions["category_raw"].nunique()),
        ("live_competition", "normalized_category_groups", questions["category_group"].nunique()),
        ("live_competition", "globally_unique_tossup_ids", questions["tossup_index"].nunique()),
        ("live_competition", "individual_player_count", "not derivable: player mapping is empty"),
        ("paper_context", "competitions", 3),
        ("paper_context", "matches", 93),
        ("paper_context", "human_vs_model_matches", 55),
        ("paper_context", "human_vs_human_matches", 38),
        ("paper_context", "qa_pairs_including_tiebreakers", 243),
        ("qanta_reference_corpus", "questions", len(qanta)),
        ("qanta_reference_corpus", "unique_qanta_ids", qanta["qanta_id"].nunique()),
        ("qanta_reference_corpus", "categories", qanta["category"].nunique()),
        ("qanta_reference_corpus", "tournaments", qanta["tournament"].nunique()),
        ("qanta_reference_corpus", "earliest_year", qanta["year"].min()),
        ("qanta_reference_corpus", "latest_year", qanta["year"].max()),
        ("qanta_reference_corpus", "duplicate_question_text_rows", len(qanta) - qanta["text"].nunique()),
        ("qanta_reference_corpus", "missing_wikipedia_pages", int(qanta["page_missing"].sum())),
    ]
    pd.DataFrame(summary_rows, columns=["component", "metric", "value"]).to_csv(
        data_dir / "dataset_summary.csv", index=False
    )

    return {
        "team": team_summary,
        "group": group_summary,
        "category": category_summary,
        "packet": packet_summary,
        "qanta_category": qanta_category,
        "qanta_year": qanta_year,
    }


def plot_position_distribution(output_dir: Path, events: pd.DataFrame) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.8), sharey=True)
    bins = np.arange(0, 101, 10)
    colors = {True: "#167d73", False: "#c74b50"}
    labels = {True: "Correct", False: "Incorrect"}
    for axis, team_type in zip(axes, ["Human", "Model"]):
        for correct in [True, False]:
            values = events.loc[
                (events["team_type"] == team_type) & (events["correct"] == correct),
                "position_pct",
            ]
            axis.hist(
                values,
                bins=bins,
                density=True,
                histtype="step",
                linewidth=2.4,
                color=colors[correct],
                label=f"{labels[correct]} (n={len(values):,})",
            )
            axis.axvline(
                values.median(), color=colors[correct], linestyle="--", linewidth=1.4, alpha=0.9
            )
        axis.set_title(f"{team_type} buzzes")
        axis.set_xlabel("Approx. question revealed at buzz (%)")
        axis.set_xlim(0, 100)
        axis.grid(axis="y", alpha=0.2)
        axis.legend(frameon=False)
    axes[0].set_ylabel("Density")
    fig.suptitle("Buzz timing: incorrect model buzzes are concentrated earlier", fontsize=14)
    fig.tight_layout()
    fig.savefig(output_dir / "figures" / "buzz_position_distribution.png", dpi=180)
    plt.close(fig)


def plot_team_profiles(output_dir: Path, team_summary: pd.DataFrame) -> None:
    ordered = team_summary.copy()
    ordered["sort"] = ordered["team"].map(natural_team_key)
    ordered = ordered.sort_values("sort")
    labels = [
        f"{row.team} ({row.model_name})" if row.model_name else row.team
        for row in ordered.itertuples()
    ]
    colors = ["#5b8db8" if kind == "Human" else "#e28e3f" for kind in ordered["team_type"]]

    fig, axes = plt.subplots(1, 3, figsize=(15, 7), sharey=True)
    y = np.arange(len(ordered))
    axes[0].barh(y, ordered["buzz_events"], color=colors)
    axes[0].set_xlabel("Recorded buzz events")
    axes[1].barh(y, 100 * ordered["accuracy"], color=colors)
    axes[1].set_xlabel("Accuracy when buzzing (%)")
    axes[1].set_xlim(0, 100)
    axes[2].barh(y, ordered["median_position_pct"], color=colors)
    axes[2].set_xlabel("Median question revealed (%)")
    axes[2].set_xlim(0, 100)
    for axis in axes:
        axis.grid(axis="x", alpha=0.2)
        axis.set_yticks(y, labels)
        axis.invert_yaxis()
    fig.suptitle("Team-level buzz volume, accuracy, and timing", fontsize=14)
    fig.tight_layout()
    fig.savefig(output_dir / "figures" / "team_buzz_profiles.png", dpi=180)
    plt.close(fig)


def plot_category_performance(output_dir: Path, category_summary: pd.DataFrame) -> None:
    categories = ["Arts", "Geo/CE", "History", "Literature", "RMPSS", "Science"]
    x = np.arange(len(categories))
    width = 0.36
    colors = {"Human": "#5b8db8", "Model": "#e28e3f"}
    fig, axes = plt.subplots(1, 2, figsize=(13, 4.8))
    for offset, team_type in [(-width / 2, "Human"), (width / 2, "Model")]:
        subset = category_summary.query("team_type == @team_type").set_index("category_group")
        axes[0].bar(
            x + offset,
            [100 * subset.loc[c, "accuracy"] for c in categories],
            width,
            label=team_type,
            color=colors[team_type],
        )
        axes[1].bar(
            x + offset,
            [subset.loc[c, "median_position_pct"] for c in categories],
            width,
            label=team_type,
            color=colors[team_type],
        )
    for axis in axes:
        axis.set_xticks(x, categories, rotation=30, ha="right")
        axis.set_ylim(0, 100)
        axis.grid(axis="y", alpha=0.2)
        axis.legend(frameon=False)
    axes[0].set_ylabel("Accuracy when buzzing (%)")
    axes[0].set_title("Buzz accuracy")
    axes[1].set_ylabel("Median question revealed (%)")
    axes[1].set_title("Buzz timing")
    fig.suptitle("Performance by normalized question category", fontsize=14)
    fig.tight_layout()
    fig.savefig(output_dir / "figures" / "category_performance.png", dpi=180)
    plt.close(fig)


def plot_packet_overview(output_dir: Path, packet_summary: pd.DataFrame) -> None:
    packets = sorted(packet_summary["packet"].unique())
    x = np.arange(len(packets))
    width = 0.36
    colors = {"Human": "#5b8db8", "Model": "#e28e3f"}
    fig, axes = plt.subplots(2, 1, figsize=(12, 7), sharex=True)
    for offset, team_type in [(-width / 2, "Human"), (width / 2, "Model")]:
        subset = packet_summary.query("team_type == @team_type").set_index("packet")
        axes[0].bar(
            x + offset,
            [subset.loc[p, "buzz_events"] for p in packets],
            width,
            label=team_type,
            color=colors[team_type],
        )
        axes[1].bar(
            x + offset,
            [100 * subset.loc[p, "accuracy"] for p in packets],
            width,
            label=team_type,
            color=colors[team_type],
        )
    axes[0].set_ylabel("Recorded buzz events")
    axes[1].set_ylabel("Accuracy when buzzing (%)")
    axes[1].set_ylim(0, 100)
    axes[1].set_xlabel("Packet")
    axes[1].set_xticks(x, packets)
    for axis in axes:
        axis.grid(axis="y", alpha=0.2)
        axis.legend(frameon=False, ncol=2)
    fig.suptitle("Packet-level variation reflects changing participant pools", fontsize=14)
    fig.tight_layout()
    fig.savefig(output_dir / "figures" / "packet_overview.png", dpi=180)
    plt.close(fig)


def plot_qanta_corpus(
    output_dir: Path, qanta_category: pd.DataFrame, qanta_year: pd.DataFrame
) -> None:
    categories = (
        qanta_category.groupby("category")["questions"].sum().sort_values(ascending=True).index
    )
    splits = ["buzztrain", "buzzdev"]
    colors = {"buzztrain": "#557a95", "buzzdev": "#d79b44"}
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))
    left = np.zeros(len(categories))
    for split in splits:
        subset = qanta_category.query("split == @split").set_index("category")
        values = np.array([subset["questions"].get(c, 0) for c in categories])
        axes[0].barh(categories, values, left=left, label=split, color=colors[split])
        left += values
    axes[0].set_xlabel("Questions")
    axes[0].set_title("Category distribution")
    axes[0].legend(frameon=False)
    for split in splits:
        subset = qanta_year.query("split == @split")
        axes[1].plot(
            subset["year"], subset["questions"], marker="o", label=split, color=colors[split]
        )
    axes[1].set_xlabel("Year")
    axes[1].set_ylabel("Questions")
    axes[1].set_title("Source year distribution")
    axes[1].grid(alpha=0.2)
    axes[1].legend(frameon=False)
    fig.suptitle("QANTA retrieval/reference corpus (not live GRACE buzz events)", fontsize=14)
    fig.tight_layout()
    fig.savefig(output_dir / "figures" / "qanta_reference_corpus.png", dpi=180)
    plt.close(fig)


def write_quality_report(
    output_dir: Path,
    source_dir: Path,
    archive: Path,
    events: pd.DataFrame,
    questions: pd.DataFrame,
) -> None:
    player_path = source_dir / "questions_packets" / "player_team_per_packet.pkl"
    mapping_path = source_dir / "questions_packets" / "human_model_team_per_question.pkl"
    mapping_records = 0
    collision_note = "not checked"
    seen_mismatches = "not checked"
    if mapping_path.exists() and mapping_path.stat().st_size:
        with mapping_path.open("rb") as handle:
            mapping = pickle.load(handle)
        mapping_records = len(mapping)
        collision_rows = questions.loc[questions["tossup_index"] == "128", ["packet", "tossup_index"]]
        collision_note = f"archive rows={len(collision_rows)}, mapping entries={int(128 in mapping)}"
        mismatch_questions = 0
        mismatch_memberships = 0
        for question in questions.itertuples():
            qid: object = int(question.tossup_index) if question.tossup_index.isdigit() else question.tossup_index
            row = mapping.get(qid)
            if row is None or row.get("packet") != question.packet:
                continue
            event_teams = set(
                events.loc[events["question_key"] == question.question_key, "team"]
            )
            missing = event_teams - set(row.get("seen", []))
            if missing:
                mismatch_questions += 1
                mismatch_memberships += len(missing)
        seen_mismatches = (
            f"{mismatch_questions} questions; {mismatch_memberships} team-question memberships"
        )

    checks = {
        "archive_sha256_matches_known_release": sha256(archive) == EXPECTED_ARCHIVE_SHA256,
        "archive_questions": len(questions),
        "archive_buzz_events": len(events),
        "all_positions_within_question": bool((events["position_words"] <= events["question_words"]).all()),
        "all_results_binary": set(events["result"]) == {"+", "-"},
        "team_ids": sorted(events["team"].unique(), key=natural_team_key),
        "player_mapping_bytes": player_path.stat().st_size if player_path.exists() else "missing",
        "human_model_mapping_records": mapping_records,
        "tossup_128_collision": collision_note,
        "buzzers_absent_from_seen_roster": seen_mismatches,
    }
    with (output_dir / "data" / "validation.json").open("w", encoding="utf-8") as handle:
        json.dump(checks, handle, indent=2)


def parse_args() -> argparse.Namespace:
    script_dir = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source-dir",
        type=Path,
        default=script_dir.parent / "grace_data",
        help="Local grace_data directory (default: ../grace_data).",
    )
    parser.add_argument(
        "--buzz-archive",
        type=Path,
        required=True,
        help="Path to [public]ALL_final_buzzpoints_enc.zip from the authors' release.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=script_dir,
        help="Analysis output directory (default: this script's directory).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "figures").mkdir(parents=True, exist_ok=True)

    events, questions = load_live_archive(args.buzz_archive)
    qanta = load_qanta_corpus(args.source_dir)

    tables = write_tables(
        args.output_dir, args.source_dir, args.buzz_archive, events, questions, qanta
    )
    plot_position_distribution(args.output_dir, events)
    plot_team_profiles(args.output_dir, tables["team"])
    plot_category_performance(args.output_dir, tables["category"])
    plot_packet_overview(args.output_dir, tables["packet"])
    plot_qanta_corpus(args.output_dir, tables["qanta_category"], tables["qanta_year"])
    write_quality_report(args.output_dir, args.source_dir, args.buzz_archive, events, questions)

    if len(questions) != 240 or len(events) != 1749:
        raise RuntimeError(
            f"Unexpected release shape: {len(questions)} questions, {len(events)} buzzes"
        )
    print(f"Wrote analysis to {args.output_dir}")


if __name__ == "__main__":
    main()
