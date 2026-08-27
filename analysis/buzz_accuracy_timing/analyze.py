#!/usr/bin/env python3
"""Analyze whether player buzz accuracy is associated with early/late buzzing.

The primary definition treats every recorded buzz row as an attempt and defines
accuracy as ``correct / attempts``. A sensitivity analysis uses only scored
attempts (raw value -5 or +10), because raw value-0 attempts are concentrated at
the end of tossups and therefore matter substantially for this question.

Outputs are written beside this script:

* player_summary.csv
* accuracy_bin_summary.csv
* average_player_timing_distribution.csv
* sensitivity_summary.csv
* minimum_attempts_robustness.csv
* question_level.csv
* question_accuracy_bin_summary.csv
* accuracy_and_timing.png
* question_correlations.png
* report.md
"""

from __future__ import annotations

import html
import re
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datasets import load_from_disk
from scipy.stats import binomtest, false_discovery_control, pearsonr, spearmanr


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
DATA_DIR = ROOT / "data" / "hf" / "quizbowl-irt"
MIN_ATTEMPTS = 30
BOOTSTRAP_SAMPLES = 5_000
RANDOM_SEED = 20260728
BIN_LABELS = ("Q1 low", "Q2", "Q3", "Q4 high")
# Relative buzz position is bucketed once, here, and every "early"/"late"
# fraction below is derived from these bands rather than restating the cuts.
POSITION_EDGES = (0.50, 0.75, 0.90)
POSITION_BANDS = ("early", "middle", "late", "super_late")


def load_table(name: str) -> pd.DataFrame:
    return load_from_disk(str(DATA_DIR / name))["all"].to_pandas()


def clean_answer(value: object, limit: int = 100) -> str:
    text = html.unescape(re.sub(r"<[^>]+>", "", str(value)))
    text = " ".join(text.split())
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "…"


def add_buzz_context(buzzes: pd.DataFrame) -> pd.DataFrame:
    buzzes = buzzes.copy()
    required = {
        "buzz_id",
        "tossup_id",
        "game_id",
        "player_id",
        "team_id",
        "token_position",
        "num_tokens_total",
        "correct",
        "value",
    }
    missing = required - set(buzzes)
    if missing:
        raise ValueError(f"Missing required buzz columns: {sorted(missing)}")
    if not (buzzes["correct"].astype(bool) == (buzzes["value"] > 0)).all():
        raise ValueError("The correct flag does not agree with raw positive values")
    if (buzzes["num_tokens_total"] <= 0).any():
        raise ValueError("Every buzz must have a positive tossup token count")

    buzzes["_source_order"] = (
        buzzes["buzz_id"].str.rsplit("-", n=1).str[-1].astype(int)
    )
    event_cols = ["game_id", "tossup_id"]
    buzzes = buzzes.sort_values(
        event_cols + ["token_position", "_source_order"]
    ).reset_index(drop=True)
    buzzes["buzz_rank"] = buzzes.groupby(event_cols).cumcount() + 1

    first = (
        buzzes[buzzes["buzz_rank"] == 1]
        .set_index(event_cols)[["value", "team_id", "token_position"]]
        .rename(
            columns={
                "value": "first_value",
                "team_id": "first_team_id",
                "token_position": "first_token_position",
            }
        )
    )
    buzzes = buzzes.join(first, on=event_cols)
    is_post_neg = (
        (buzzes["buzz_rank"] > 1)
        & (buzzes["first_value"] == -5)
        & (buzzes["team_id"] != buzzes["first_team_id"])
    )
    buzzes["phase"] = np.select(
        [buzzes["buzz_rank"] == 1, is_post_neg],
        ["first", "post_neg"],
        default="other_later",
    )
    buzzes["raw_relative_position"] = (
        buzzes["token_position"] / buzzes["num_tokens_total"]
    )
    # The 65 source positions beyond the sanitized text length are retained in
    # raw_relative_position but clamped for comparable timing summaries.
    buzzes["relative_position"] = buzzes["raw_relative_position"].clip(0, 1)
    return buzzes


def player_accuracy(
    buzzes: pd.DataFrame, *, scored_only: bool = False
) -> pd.DataFrame:
    source = buzzes[buzzes["value"] != 0] if scored_only else buzzes
    prefix = "scored_" if scored_only else ""
    players = (
        source.groupby("player_id")
        .agg(
            **{
                f"{prefix}attempts": ("buzz_id", "size"),
                f"{prefix}correct": ("correct", "sum"),
            }
        )
        .reset_index()
    )
    players[f"{prefix}accuracy"] = (
        players[f"{prefix}correct"] / players[f"{prefix}attempts"]
    )
    return players


def quartile_bins(
    accuracy: pd.Series,
) -> tuple[np.ndarray, pd.Categorical]:
    cuts = accuracy.quantile([0.25, 0.50, 0.75]).to_numpy(dtype=float)
    if len(np.unique(cuts)) != 3:
        raise ValueError(f"Accuracy quartile cutoffs are not unique: {cuts}")
    bins = pd.cut(
        accuracy,
        [-np.inf, *cuts, np.inf],
        labels=BIN_LABELS,
        include_lowest=True,
    )
    return cuts, bins


def timing_category(values: pd.Series) -> pd.Categorical:
    return pd.cut(
        values,
        [-np.inf, *POSITION_EDGES, np.inf],
        labels=POSITION_BANDS,
        right=False,
    )


def band_fraction(band: str):
    """Return the share of positions falling in one timing band."""
    return lambda values: (timing_category(values) == band).mean()


def band_fractions(template: str, source: str = "relative_position") -> dict:
    """Named aggregations giving each band's share of ``source``.

    ``template`` is formatted with the band name, e.g. ``"first_{}_fraction"``.
    """
    return {
        template.format(band): (source, band_fraction(band))
        for band in POSITION_BANDS
    }


super_late_fraction = band_fraction("super_late")


def bootstrap_high_minus_low(
    frame: pd.DataFrame, column: str
) -> tuple[float, float, float]:
    rng = np.random.default_rng(RANDOM_SEED)
    low = frame.loc[frame["accuracy_bin"] == BIN_LABELS[0], column].dropna().to_numpy()
    high = frame.loc[
        frame["accuracy_bin"] == BIN_LABELS[-1], column
    ].dropna().to_numpy()
    observed = float(high.mean() - low.mean())
    samples = np.empty(BOOTSTRAP_SAMPLES)
    for index in range(BOOTSTRAP_SAMPLES):
        samples[index] = (
            rng.choice(high, size=len(high), replace=True).mean()
            - rng.choice(low, size=len(low), replace=True).mean()
        )
    low_ci, high_ci = np.quantile(samples, [0.025, 0.975])
    return observed, float(low_ci), float(high_ci)


def fmt_pct(value: float, digits: int = 1) -> str:
    return f"{100 * value:.{digits}f}%"


def fmt_num(value: float, digits: int = 3) -> str:
    return f"{value:.{digits}f}"


def player_timing_summary(
    eligible: pd.DataFrame, first: pd.DataFrame, post_neg: pd.DataFrame
) -> tuple[pd.DataFrame, float]:
    """Summarize each eligible player's buzz timing; write the player-level CSVs.

    Returns the per-player frame and the median mean-first-position used to
    split players into the earlier/later relative timing styles.
    """
    first_player = (
        first.groupby("player_id")
        .agg(
            first_attempts=("buzz_id", "size"),
            mean_first_position=("relative_position", "mean"),
            median_first_position=("relative_position", "median"),
            **band_fractions("first_{}_fraction"),
        )
        .reset_index()
    )
    post_player = (
        post_neg.groupby("player_id")
        .agg(
            post_neg_attempts=("buzz_id", "size"),
            mean_post_neg_position=("relative_position", "mean"),
            post_neg_super_late_fraction=(
                "relative_position",
                super_late_fraction,
            ),
        )
        .reset_index()
    )
    player_summary = (
        eligible.merge(first_player, on="player_id", how="left")
        .merge(post_player, on="player_id", how="left")
        .sort_values(["accuracy_bin", "accuracy", "player_id"])
    )
    player_summary["typical_first_timing"] = timing_category(
        player_summary["median_first_position"]
    )
    relative_style_cutoff = float(player_summary["mean_first_position"].median())
    player_summary["relative_timing_style"] = np.where(
        player_summary["mean_first_position"] < relative_style_cutoff,
        "earlier half",
        "later half",
    )
    player_summary.to_csv(HERE / "player_summary.csv", index=False, float_format="%.6f")
    # 5%-wide histogram of each player's mean first-buzz position. The last bin
    # runs to infinity so a player averaging exactly 1.0 lands in it.
    starts = np.arange(0, 1, 0.05)
    counts = pd.cut(
        player_summary["mean_first_position"], [*starts, np.inf], right=False
    ).value_counts(sort=False)
    pd.DataFrame(
        {
            "position_start": starts,
            "position_end": starts + 0.05,
            "players": counts.to_numpy(),
            "player_fraction": counts.to_numpy() / len(player_summary),
        }
    ).to_csv(
        HERE / "average_player_timing_distribution.csv",
        index=False,
        float_format="%.6f",
    )
    return player_summary, relative_style_cutoff


def accuracy_bin_summary(
    player_summary: pd.DataFrame, first: pd.DataFrame, post_neg: pd.DataFrame
) -> pd.DataFrame:
    """Aggregate players and pooled buzzes by accuracy quartile; write its CSV.

    Player-level columns average one value per player, so every player counts
    equally; the ``pooled_*`` columns instead pool the raw buzzes in the bin.
    """
    player_bin = (
        player_summary.groupby("accuracy_bin", observed=True)
        .agg(
            players=("player_id", "size"),
            min_accuracy=("accuracy", "min"),
            max_accuracy=("accuracy", "max"),
            mean_accuracy=("accuracy", "mean"),
            mean_player_first_position=("mean_first_position", "mean"),
            median_player_first_position=("mean_first_position", "median"),
            earlier_style_fraction=(
                "relative_timing_style",
                lambda x: (x == "earlier half").mean(),
            ),
            # Each player's own median position, bucketed, then shared out.
            **{
                f"typical_{band}_fraction": (
                    "typical_first_timing",
                    lambda x, band=band: (x == band).mean(),
                )
                for band in POSITION_BANDS
            },
            **{
                f"mean_player_first_{band}_fraction": (
                    f"first_{band}_fraction",
                    "mean",
                )
                for band in POSITION_BANDS
            },
        )
        .reset_index()
    )
    pooled_first = (
        first.groupby("accuracy_bin", observed=True)
        .agg(
            first_buzzes=("buzz_id", "size"),
            pooled_first_mean_position=("relative_position", "mean"),
            **band_fractions("pooled_first_{}_fraction"),
        )
        .reset_index()
    )
    pooled_post = (
        post_neg.groupby("accuracy_bin", observed=True)
        .agg(
            post_neg_buzzes=("buzz_id", "size"),
            pooled_post_neg_mean_position=("relative_position", "mean"),
            pooled_post_neg_super_late_fraction=(
                "relative_position",
                super_late_fraction,
            ),
        )
        .reset_index()
    )
    bin_summary = (
        player_bin.merge(pooled_first, on="accuracy_bin", validate="one_to_one")
        .merge(pooled_post, on="accuracy_bin", validate="one_to_one")
        .sort_values("accuracy_bin")
    )
    bin_summary.to_csv(
        HERE / "accuracy_bin_summary.csv", index=False, float_format="%.6f"
    )
    return bin_summary


def player_level_tests(player_summary: pd.DataFrame) -> dict[str, object]:
    """Correlate player accuracy with mean first-buzz position, across players."""
    return {
        "player_pearson": pearsonr(
            player_summary["accuracy"], player_summary["mean_first_position"]
        ),
        "player_spearman": spearmanr(
            player_summary["accuracy"], player_summary["mean_first_position"]
        ),
        "timing_diff": bootstrap_high_minus_low(
            player_summary, "mean_first_position"
        ),
        "style_diff": bootstrap_high_minus_low(
            player_summary.assign(
                earlier_style=(
                    player_summary["relative_timing_style"] == "earlier half"
                ).astype(float)
            ),
            "earlier_style",
        ),
    }


def leave_question_out_rows(
    buzzes: pd.DataFrame,
    eligible: pd.DataFrame,
    first: pd.DataFrame,
    cuts: np.ndarray,
) -> pd.DataFrame:
    """Re-bin every first buzz by its buzzer's accuracy *excluding that tossup*.

    Question-specific accuracy drops all of the player's rows on the focal
    tossup, so the focal outcome cannot define the bin it is then compared in.
    Players left with fewer than ``MIN_ATTEMPTS`` elsewhere are dropped, and the
    bins reuse the pooled quartile cutoffs so they stay comparable.
    """
    player_totals = eligible[["player_id", "attempts", "correct"]].rename(
        columns={"correct": "total_correct"}
    )
    player_question = (
        buzzes[buzzes["player_id"].isin(set(eligible["player_id"]))]
        .groupby(["player_id", "tossup_id"])
        .agg(question_attempts=("buzz_id", "size"), question_correct=("correct", "sum"))
        .reset_index()
    )
    question_rows = (
        first.drop(columns=["attempts", "accuracy_bin"])
        .merge(player_totals, on="player_id", validate="many_to_one")
        .merge(
            player_question,
            on=["player_id", "tossup_id"],
            validate="many_to_one",
        )
    )
    question_rows["other_attempts"] = (
        question_rows["attempts"] - question_rows["question_attempts"]
    )
    question_rows["other_accuracy"] = (
        question_rows["total_correct"] - question_rows["question_correct"]
    ) / question_rows["other_attempts"]
    question_rows = question_rows[
        question_rows["other_attempts"] >= MIN_ATTEMPTS
    ].copy()
    question_rows["accuracy_bin"] = pd.cut(
        question_rows["other_accuracy"],
        [-np.inf, *cuts, np.inf],
        labels=BIN_LABELS,
        include_lowest=True,
    )
    return question_rows


def question_level_correlations(
    question_rows: pd.DataFrame, tossups: pd.DataFrame
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Correlate accuracy with buzz position *within* each tossup; write its CSV.

    A tossup only qualifies when its first buzzers span enough distinct
    accuracies to make the within-question correlation meaningful; unqualified
    tossups are kept in the CSV with null statistics. Returns the per-question
    frame and the tossup metadata other summaries reuse.
    """
    q_records: list[dict[str, object]] = []
    for tossup_id, group in question_rows.groupby("tossup_id"):
        accuracy_spread = float(
            group["other_accuracy"].max() - group["other_accuracy"].min()
        )
        qualifies = (
            len(group) >= 30
            and group["other_accuracy"].nunique() >= 10
            and group["accuracy_bin"].nunique() >= 3
            and accuracy_spread >= 0.15
        )
        record: dict[str, object] = {
            "tossup_id": tossup_id,
            "eligible_first_buzzes": len(group),
            "accuracy_bins_present": int(group["accuracy_bin"].nunique()),
            "other_accuracy_spread": accuracy_spread,
            "qualifies": qualifies,
            "spearman_rho": np.nan,
            "p_value": np.nan,
            "linear_slope": np.nan,
        }
        if qualifies:
            rho, p_value = spearmanr(
                group["other_accuracy"], group["relative_position"]
            )
            record.update(
                {
                    "spearman_rho": float(rho),
                    "p_value": float(p_value),
                    "linear_slope": float(
                        np.polyfit(
                            group["other_accuracy"],
                            group["relative_position"],
                            1,
                        )[0]
                    ),
                }
            )
        q_records.append(record)
    question_level = pd.DataFrame(q_records)
    qualified_mask = question_level["qualifies"]
    question_level.loc[qualified_mask, "fdr_bh"] = false_discovery_control(
        question_level.loc[qualified_mask, "p_value"].to_numpy(dtype=float)
    )
    metadata = tossups[["tossup_id", "category", "subcategory", "answer"]].copy()
    metadata["answer_label"] = metadata["answer"].map(clean_answer)
    question_level = (
        question_level.merge(
            metadata.drop(columns="answer"), on="tossup_id", how="left"
        )
        .sort_values(["qualifies", "spearman_rho"], ascending=[False, True])
    )
    question_level.to_csv(
        HERE / "question_level.csv", index=False, float_format="%.6f"
    )
    return question_level, metadata


def question_bin_breakdown(
    question_rows: pd.DataFrame,
    question_level: pd.DataFrame,
    metadata: pd.DataFrame,
) -> pd.DataFrame:
    """Break each qualifying tossup down by accuracy quartile; write its CSV."""
    qualified_ids = set(
        question_level.loc[question_level["qualifies"], "tossup_id"]
    )
    question_bin_summary = (
        question_rows[question_rows["tossup_id"].isin(qualified_ids)]
        .groupby(["tossup_id", "accuracy_bin"], observed=True)
        .agg(
            first_buzzes=("buzz_id", "size"),
            mean_other_accuracy=("other_accuracy", "mean"),
            mean_first_position=("relative_position", "mean"),
            early_fraction=("relative_position", lambda x: (x < 0.50).mean()),
            late_fraction=("relative_position", lambda x: (x >= 0.75).mean()),
            super_late_fraction=("relative_position", lambda x: (x >= 0.90).mean()),
        )
        .reset_index()
        .merge(metadata.drop(columns="answer"), on="tossup_id", how="left")
    )
    question_bin_summary.to_csv(
        HERE / "question_accuracy_bin_summary.csv",
        index=False,
        float_format="%.6f",
    )
    return question_bin_summary


def within_question_effects(
    question_rows: pd.DataFrame, question_level: pd.DataFrame
) -> dict[str, object]:
    """Pool the within-tossup association into one slope and one sign test.

    The slope is the question fixed-effect estimate: both variables are
    demeaned within their tossup, so a +1.0 change in leave-question-out
    accuracy maps to this change in relative buzz position. ``question_rows``
    gains the two demeaned columns in place.
    """
    question_rows["accuracy_dm"] = question_rows["other_accuracy"] - question_rows.groupby(
        "tossup_id"
    )["other_accuracy"].transform("mean")
    question_rows["position_dm"] = question_rows[
        "relative_position"
    ] - question_rows.groupby("tossup_id")["relative_position"].transform("mean")

    qualified = question_level[question_level["qualifies"]]
    return {
        "within_question_slope": float(
            (question_rows["accuracy_dm"] * question_rows["position_dm"]).sum()
            / (question_rows["accuracy_dm"] ** 2).sum()
        ),
        "negative_fraction": float((qualified["spearman_rho"] < 0).mean()),
        "negative_binomial_p": float(
            binomtest(
                int((qualified["spearman_rho"] < 0).sum()),
                len(qualified),
                p=0.5,
                alternative="greater",
            ).pvalue
        ),
    }


def write_primary_outputs(
    buzzes: pd.DataFrame, tossups: pd.DataFrame
) -> dict[str, object]:
    """Run the primary analysis end to end and return everything the report needs.

    Players are binned by pooled accuracy over every recorded buzz; the question
    stage then re-bins each first buzz on leave-question-out accuracy so the
    two views can disagree.
    """
    all_accuracy = player_accuracy(buzzes)
    eligible = all_accuracy[all_accuracy["attempts"] >= MIN_ATTEMPTS].copy()
    cuts, eligible["accuracy_bin"] = quartile_bins(eligible["accuracy"])

    attached = buzzes.merge(
        eligible[["player_id", "attempts", "accuracy", "accuracy_bin"]],
        on="player_id",
        how="inner",
        validate="many_to_one",
    )
    first = attached[attached["phase"] == "first"].copy()
    post_neg = attached[attached["phase"] == "post_neg"].copy()

    player_summary, relative_style_cutoff = player_timing_summary(
        eligible, first, post_neg
    )
    bin_summary = accuracy_bin_summary(player_summary, first, post_neg)

    question_rows = leave_question_out_rows(buzzes, eligible, first, cuts)
    question_level, metadata = question_level_correlations(question_rows, tossups)
    question_bin_summary = question_bin_breakdown(
        question_rows, question_level, metadata
    )

    return {
        "player_summary": player_summary,
        "bin_summary": bin_summary,
        "cuts": cuts,
        "relative_style_cutoff": relative_style_cutoff,
        "question_level": question_level,
        "question_bin_summary": question_bin_summary,
        **player_level_tests(player_summary),
        **within_question_effects(question_rows, question_level),
    }


def write_sensitivity_output(buzzes: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, object]] = []

    def one_definition(
        definition: str,
        accuracy_frame: pd.DataFrame,
        accuracy_col: str,
        attempts_col: str,
        timing_rows: pd.DataFrame,
    ) -> None:
        eligible = accuracy_frame[accuracy_frame[attempts_col] >= MIN_ATTEMPTS].copy()
        cuts, eligible["accuracy_bin"] = quartile_bins(eligible[accuracy_col])
        first = timing_rows[
            (timing_rows["phase"] == "first")
            & timing_rows["player_id"].isin(set(eligible["player_id"]))
        ].merge(
            eligible[["player_id", accuracy_col, "accuracy_bin"]],
            on="player_id",
            validate="many_to_one",
        )
        player = (
            first.groupby("player_id")
            .agg(
                accuracy=(accuracy_col, "first"),
                accuracy_bin=("accuracy_bin", "first"),
                timing_attempts=("buzz_id", "size"),
                mean_first_position=("relative_position", "mean"),
            )
            .reset_index()
        )
        pearson = pearsonr(player["accuracy"], player["mean_first_position"])
        spearman = spearmanr(player["accuracy"], player["mean_first_position"])
        first["accuracy_dm"] = first[accuracy_col] - first.groupby("tossup_id")[
            accuracy_col
        ].transform("mean")
        first["position_dm"] = first["relative_position"] - first.groupby(
            "tossup_id"
        )["relative_position"].transform("mean")
        within_slope = float(
            (first["accuracy_dm"] * first["position_dm"]).sum()
            / (first["accuracy_dm"] ** 2).sum()
        )
        by_bin = (
            player.groupby("accuracy_bin", observed=True)
            .agg(
                players=("player_id", "size"),
                mean_accuracy=("accuracy", "mean"),
                mean_player_first_position=("mean_first_position", "mean"),
            )
            .reset_index()
        )
        for record in by_bin.to_dict("records"):
            record.update(
                {
                    "definition": definition,
                    "accuracy_q1_cut": cuts[0],
                    "accuracy_q2_cut": cuts[1],
                    "accuracy_q3_cut": cuts[2],
                    "player_pearson_r": float(pearson.statistic),
                    "player_pearson_p": float(pearson.pvalue),
                    "player_spearman_rho": float(spearman.statistic),
                    "player_spearman_p": float(spearman.pvalue),
                    "within_question_slope": within_slope,
                }
            )
            rows.append(record)

    all_accuracy = player_accuracy(buzzes)
    one_definition(
        "all recorded attempts; timing on all first buzzes",
        all_accuracy,
        "accuracy",
        "attempts",
        buzzes,
    )
    one_definition(
        "all recorded attempts; timing excludes value-0 first buzzes",
        all_accuracy,
        "accuracy",
        "attempts",
        buzzes[buzzes["value"] != 0],
    )
    scored_accuracy = player_accuracy(buzzes, scored_only=True)
    one_definition(
        "scored attempts only (-5/+10); timing excludes value-0 first buzzes",
        scored_accuracy,
        "scored_accuracy",
        "scored_attempts",
        buzzes[buzzes["value"] != 0],
    )
    sensitivity = pd.DataFrame(rows)
    sensitivity.to_csv(
        HERE / "sensitivity_summary.csv", index=False, float_format="%.6f"
    )
    return sensitivity


def write_minimum_threshold_robustness(buzzes: pd.DataFrame) -> pd.DataFrame:
    accuracy = player_accuracy(buzzes)
    records: list[dict[str, object]] = []
    for minimum in (20, 30, 50, 100):
        eligible = accuracy[accuracy["attempts"] >= minimum].copy()
        cuts, eligible["accuracy_bin"] = quartile_bins(eligible["accuracy"])
        first = (
            buzzes[
                (buzzes["phase"] == "first")
                & buzzes["player_id"].isin(set(eligible["player_id"]))
            ]
            .groupby("player_id")
            .agg(mean_first_position=("relative_position", "mean"))
            .reset_index()
            .merge(
                eligible[["player_id", "accuracy", "accuracy_bin"]],
                on="player_id",
                validate="one_to_one",
            )
        )
        by_bin = first.groupby("accuracy_bin", observed=True)[
            "mean_first_position"
        ].mean()
        pearson = pearsonr(first["accuracy"], first["mean_first_position"])
        spearman = spearmanr(first["accuracy"], first["mean_first_position"])
        records.append(
            {
                "minimum_attempts": minimum,
                "players": len(eligible),
                "accuracy_q1_cut": cuts[0],
                "accuracy_q2_cut": cuts[1],
                "accuracy_q3_cut": cuts[2],
                "q1_mean_player_first_position": by_bin.loc[BIN_LABELS[0]],
                "q4_mean_player_first_position": by_bin.loc[BIN_LABELS[-1]],
                "q4_minus_q1_position": (
                    by_bin.loc[BIN_LABELS[-1]] - by_bin.loc[BIN_LABELS[0]]
                ),
                "player_pearson_r": float(pearson.statistic),
                "player_pearson_p": float(pearson.pvalue),
                "player_spearman_rho": float(spearman.statistic),
                "player_spearman_p": float(spearman.pvalue),
            }
        )
    robustness = pd.DataFrame(records)
    robustness.to_csv(
        HERE / "minimum_attempts_robustness.csv",
        index=False,
        float_format="%.6f",
    )
    return robustness


def make_plots(primary: dict[str, object]) -> None:
    bin_summary = primary["bin_summary"].copy()
    player_summary = primary["player_summary"].copy()
    colors = ["#4477AA", "#66CCEE", "#EEAA33", "#CC6677"]

    fig, axes = plt.subplots(1, 3, figsize=(14, 4.6))
    x = np.arange(len(bin_summary))
    axes[0].bar(
        x,
        100 * bin_summary["mean_player_first_position"],
        color=colors,
        width=0.72,
    )
    axes[0].set_xticks(x, BIN_LABELS)
    axes[0].set_ylabel("Mean first-buzz position (% of clue)")
    axes[0].set_title("Player-weighted timing")
    axes[0].set_ylim(55, 74)

    style_columns = [
        "typical_early_fraction",
        "typical_middle_fraction",
        "typical_late_fraction",
        "typical_super_late_fraction",
    ]
    style_labels = ["<50%", "50–75%", "75–90%", "≥90%"]
    style_colors = ["#228833", "#CCBB44", "#EE8866", "#AA3377"]
    bottom = np.zeros(len(bin_summary))
    for column, label, color in zip(style_columns, style_labels, style_colors):
        values = 100 * bin_summary[column].to_numpy()
        axes[1].bar(x, values, bottom=bottom, label=label, color=color)
        bottom += values
    axes[1].set_xticks(x, BIN_LABELS)
    axes[1].set_ylabel("Players (%)")
    axes[1].set_title("Player's median first-buzz position")
    axes[1].legend(title="Clue position", frameon=False, fontsize=8)

    width = 0.34
    axes[2].bar(
        x - width / 2,
        100 * bin_summary["pooled_first_super_late_fraction"],
        width,
        label="First buzz",
        color="#4477AA",
    )
    axes[2].bar(
        x + width / 2,
        100 * bin_summary["pooled_post_neg_super_late_fraction"],
        width,
        label="After opponent neg",
        color="#CC6677",
    )
    axes[2].set_xticks(x, BIN_LABELS)
    axes[2].set_ylabel("Buzzes at ≥90% of clue (%)")
    axes[2].set_title("Super-late buzzing by phase")
    axes[2].legend(frameon=False)

    fig.suptitle(
        f"Buzz timing by all-attempt accuracy (players with ≥{MIN_ATTEMPTS} attempts)",
        y=1.02,
    )
    fig.tight_layout()
    fig.savefig(HERE / "accuracy_and_timing.png", dpi=180, bbox_inches="tight")
    plt.close(fig)

    positions = player_summary["mean_first_position"]
    fig, ax = plt.subplots(figsize=(8.5, 4.8))
    ax.hist(
        100 * positions,
        bins=np.arange(35, 101, 2.5),
        color="#4477AA",
        edgecolor="white",
    )
    ax.axvline(
        100 * positions.mean(),
        color="#CC3311",
        linestyle="--",
        linewidth=2,
        label=f"Mean = {100 * positions.mean():.1f}%",
    )
    ax.axvline(
        100 * positions.median(),
        color="#228833",
        linestyle=":",
        linewidth=2,
        label=f"Median = {100 * positions.median():.1f}%",
    )
    ax.axvspan(
        100 * positions.quantile(0.25),
        100 * positions.quantile(0.75),
        color="#CCBB44",
        alpha=0.18,
        label=(
            f"Middle 50%: {100 * positions.quantile(0.25):.1f}–"
            f"{100 * positions.quantile(0.75):.1f}%"
        ),
    )
    ax.set_xlabel("Player's mean first-buzz position (% of clue)")
    ax.set_ylabel("Players")
    ax.set_title(
        f"Distribution of average player buzz timing (n = {len(positions):,})"
    )
    ax.legend(frameon=False)
    fig.tight_layout()
    fig.savefig(
        HERE / "average_player_buzz_timing_distribution.png",
        dpi=180,
        bbox_inches="tight",
    )
    plt.close(fig)

    qualified = primary["question_level"]
    qualified = qualified[qualified["qualifies"]]
    fig, ax = plt.subplots(figsize=(8.5, 4.8))
    ax.hist(
        qualified["spearman_rho"],
        bins=np.linspace(-0.65, 0.50, 36),
        color="#4477AA",
        edgecolor="white",
    )
    ax.axvline(0, color="#333333", linewidth=1)
    ax.axvline(
        qualified["spearman_rho"].median(),
        color="#CC3311",
        linestyle="--",
        label=f"Median = {qualified['spearman_rho'].median():.3f}",
    )
    ax.set_xlabel(
        "Within-question Spearman ρ: leave-question-out accuracy vs buzz position"
    )
    ax.set_ylabel("Questions")
    ax.set_title("Question-specific timing relationships")
    ax.legend(frameon=False)
    fig.tight_layout()
    fig.savefig(HERE / "question_correlations.png", dpi=180, bbox_inches="tight")
    plt.close(fig)


def write_report(
    buzzes: pd.DataFrame,
    primary: dict[str, object],
    sensitivity: pd.DataFrame,
    robustness: pd.DataFrame,
) -> None:
    bins = primary["bin_summary"].set_index("accuracy_bin")
    low = bins.loc[BIN_LABELS[0]]
    high = bins.loc[BIN_LABELS[-1]]
    cuts = primary["cuts"]
    timing_diff, timing_low, timing_high = primary["timing_diff"]
    style_diff, style_low, style_high = primary["style_diff"]
    q = primary["question_level"]
    qualified = q[q["qualifies"]].copy()
    significant_negative = qualified[
        (qualified["fdr_bh"] < 0.05) & (qualified["spearman_rho"] < 0)
    ]
    significant_positive = qualified[
        (qualified["fdr_bh"] < 0.05) & (qualified["spearman_rho"] > 0)
    ]

    qbins = primary["question_bin_summary"]
    wide = qbins.pivot(
        index="tossup_id", columns="accuracy_bin", values=["first_buzzes", "mean_first_position"]
    )
    wide.columns = [f"{metric}__{accuracy_bin}" for metric, accuracy_bin in wide.columns]
    qualified = qualified.merge(wide.reset_index(), on="tossup_id", how="left")
    has_extremes = (
        qualified[f"first_buzzes__{BIN_LABELS[0]}"].fillna(0).ge(3)
        & qualified[f"first_buzzes__{BIN_LABELS[-1]}"].fillna(0).ge(3)
    )
    negative_examples = qualified[
        has_extremes
        & (qualified["spearman_rho"] < 0)
        & (qualified["fdr_bh"] < 0.05)
    ].sort_values(["fdr_bh", "spearman_rho"]).head(4)
    positive_examples = qualified[
        has_extremes & (qualified["spearman_rho"] > 0)
    ].sort_values("p_value").head(3)

    scored = sensitivity[
        sensitivity["definition"].str.startswith("scored attempts only")
    ].set_index("accuracy_bin")
    zero_first = buzzes[
        (buzzes["phase"] == "first") & (buzzes["value"] == 0)
    ]

    def question_lines(frame: pd.DataFrame, label: str) -> list[str]:
        lines = [
            f"| {label} | Answer | n | ρ | Q1 mean position | Q4 mean position | FDR q |",
            "| --- | --- | ---: | ---: | ---: | ---: | ---: |",
        ]
        for _, row in frame.iterrows():
            q1 = row[f"mean_first_position__{BIN_LABELS[0]}"]
            q4 = row[f"mean_first_position__{BIN_LABELS[-1]}"]
            lines.append(
                "| `{}` | {} | {} | {} | {} | {} | {} |".format(
                    row["tossup_id"],
                    str(row["answer_label"]).replace("|", "\\|"),
                    int(row["eligible_first_buzzes"]),
                    fmt_num(row["spearman_rho"]),
                    fmt_pct(q1),
                    fmt_pct(q4),
                    fmt_num(row["fdr_bh"]),
                )
            )
        return lines

    report = [
        "# Buzz accuracy and early/late buzzing",
        "",
        "## Bottom line",
        "",
        (
            "Using the literal dataset definition—every recorded buzz is an attempt "
            "and any positive value is correct—higher-accuracy players buzz earlier "
            "on average. This is a smooth, overlapping gradient rather than two "
            "clean clusters of “early” and “late” players."
        ),
        "",
        (
            f"Among {len(primary['player_summary']):,} players with at least "
            f"{MIN_ATTEMPTS} attempts, the low-accuracy quartile averaged its first "
            f"buzz at {fmt_pct(low['mean_player_first_position'])} of the clue, "
            f"versus {fmt_pct(high['mean_player_first_position'])} for the "
            f"high-accuracy quartile. The player-bootstrap high-minus-low difference "
            f"is {fmt_pct(timing_diff)} (95% CI {fmt_pct(timing_low)} to "
            f"{fmt_pct(timing_high)})."
        ),
        "",
        (
            f"Defining “earlier-style” relatively as below the overall player median "
            f"mean position ({fmt_pct(primary['relative_style_cutoff'])}), "
            f"{fmt_pct(low['earlier_style_fraction'])} of Q1 and "
            f"{fmt_pct(high['earlier_style_fraction'])} of Q4 are earlier-style "
            f"(difference {fmt_pct(style_diff)}, 95% CI {fmt_pct(style_low)} to "
            f"{fmt_pct(style_high)}). That separation is meaningful but far from "
            f"perfect."
        ),
        "",
        (
            "The proposed “high accuracy = early or super-late after an opponent "
            "misses” story is only half supported. Q4 players are super-late after "
            f"an opponent neg on {fmt_pct(high['pooled_post_neg_super_late_fraction'])} "
            "of such buzzes, but Q1 players are at least as likely to be super-late "
            f"({fmt_pct(low['pooled_post_neg_super_late_fraction'])}). Post-neg "
            "buzzing is overwhelmingly late for everyone, not a special high-accuracy "
            "subgroup."
        ),
        "",
        "![Accuracy bins and timing](accuracy_and_timing.png)",
        "",
        "## Distribution of average player timing",
        "",
        (
            f"Each eligible player contributes once. The mean player buzz position is "
            f"{fmt_pct(primary['player_summary']['mean_first_position'].mean())}, "
            f"the median is "
            f"{fmt_pct(primary['player_summary']['mean_first_position'].median())}, "
            f"and the middle 50% of players range from "
            f"{fmt_pct(primary['player_summary']['mean_first_position'].quantile(0.25))} "
            f"to "
            f"{fmt_pct(primary['player_summary']['mean_first_position'].quantile(0.75))} "
            f"of the clue."
        ),
        "",
        "![Distribution of average player buzz timing]"
        "(average_player_buzz_timing_distribution.png)",
        "",
        "## Primary bin results",
        "",
        (
            "Accuracy quartiles are player-weighted and cut at "
            f"{fmt_pct(cuts[0])}, {fmt_pct(cuts[1])}, and {fmt_pct(cuts[2])}. "
            "Timing fractions below are pooled first-buzz events; mean position is "
            "first computed per player and then averaged so prolific players do not "
            "dominate."
        ),
        "",
        "| Accuracy bin | Players | Mean accuracy | Mean player position | "
        "First <50% | First 75–90% | First ≥90% | Post-neg ≥90% |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for label, row in bins.iterrows():
        report.append(
            f"| {label} | {int(row['players']):,} | {fmt_pct(row['mean_accuracy'])} "
            f"| {fmt_pct(row['mean_player_first_position'])} "
            f"| {fmt_pct(row['pooled_first_early_fraction'])} "
            f"| {fmt_pct(row['pooled_first_late_fraction'])} "
            f"| {fmt_pct(row['pooled_first_super_late_fraction'])} "
            f"| {fmt_pct(row['pooled_post_neg_super_late_fraction'])} |"
        )
    report.extend(
        [
            "",
            (
                f"At player level, accuracy and mean first-buzz position have Pearson "
                f"r = {primary['player_pearson'].statistic:.3f} "
                f"(p = {primary['player_pearson'].pvalue:.2g}) and Spearman "
                f"ρ = {primary['player_spearman'].statistic:.3f} "
                f"(p = {primary['player_spearman'].pvalue:.2g})."
            ),
            "",
            (
                "The result is stable to the player sample-size floor: with minimums "
                "of 20, 30, 50, and 100 attempts, the Q4-minus-Q1 position differences "
                "are "
                + ", ".join(
                    fmt_pct(value)
                    for value in robustness["q4_minus_q1_position"]
                )
                + ", respectively."
            ),
            "",
            "## Question-controlled and specific-question checks",
            "",
            (
                "For each first-buzz row, player accuracy here is recomputed after "
                "excluding all of that player's attempts on the focal tossup. This "
                "prevents the question being analyzed from helping define the "
                "player's accuracy. Questions qualify with at least 30 eligible "
                "first buzzes, at least 3 accuracy bins, at least 10 distinct accuracy "
                "values, and at least a 15-point accuracy spread."
            ),
            "",
            (
                f"Across {len(qualified):,} qualifying tossups, "
                f"{fmt_pct(primary['negative_fraction'])} have a negative "
                f"accuracy–position correlation and the median Spearman ρ is "
                f"{qualified['spearman_rho'].median():.3f}. The one-sided sign-test "
                f"p-value against a 50/50 split is {primary['negative_binomial_p']:.2g}. "
                f"After Benjamini–Hochberg correction across questions, "
                f"{len(significant_negative)} are significantly negative and "
                f"{len(significant_positive)} significantly positive at FDR 5%."
            ),
            "",
            (
                f"A question fixed-effect regression gives a slope of "
                f"{primary['within_question_slope']:.3f}; equivalently, +10 accuracy "
                f"points is associated with buzzing "
                f"{abs(primary['within_question_slope']) * 10:.1f} percentage points "
                "earlier within the same tossup."
            ),
            "",
            "![Distribution of question correlations](question_correlations.png)",
            "",
            "Strong negative examples that survive the across-question FDR correction:",
            "",
            *question_lines(negative_examples, "Pattern"),
            "",
            (
                "The strongest contrary examples are shown below for completeness. "
                "None remains significant at FDR 5%, so they should be treated as "
                "question-level exceptions/noise rather than established reversals."
            ),
            "",
            *question_lines(positive_examples, "Contrary"),
            "",
            "## Crucial sensitivity: what counts as an attempt?",
            "",
            (
                f"There are {len(zero_first):,} value-0 first attempts; "
                f"{fmt_pct((zero_first['relative_position'] >= 0.90).mean())} occur "
                "at or after 90% of the clue and their median position is "
                f"{fmt_pct(zero_first['relative_position'].median())}. These rows are "
                "both incorrect and extremely late, so they strongly couple low "
                "all-attempt accuracy to late timing."
            ),
            "",
            (
                "When accuracy and timing are both restricted to ordinary scored "
                "attempts (−5/+10), the gradient does not replicate: Q1 averages "
                f"{fmt_pct(scored.loc[BIN_LABELS[0], 'mean_player_first_position'])} "
                "and Q4 averages "
                f"{fmt_pct(scored.loc[BIN_LABELS[-1], 'mean_player_first_position'])}; "
                "the player-level Pearson r is "
                f"{scored.iloc[0]['player_pearson_r']:.3f}, and the within-question "
                f"slope is {scored.iloc[0]['within_question_slope']:.3f}. Under that "
                "common alternative definition, higher scored-attempt accuracy is "
                "slightly associated with later, not earlier, buzzing."
            ),
            "",
            (
                "So the safe conclusion is: **yes, the raw all-attempt data show a "
                "clear earlier-timing gradient with accuracy, including within many "
                "specific questions; no, they do not show two sharply separated "
                "player types, and the result is not robust to excluding value-0 "
                "end-of-question attempts.**"
            ),
            "",
            "## Scope and files",
            "",
            (
                "This is descriptive and conditional on a recorded buzz. It does not "
                "include rostered players who never buzzed on a question, estimate a "
                "causal effect of accuracy, or resolve the dataset's intentionally "
                "unmerged numeric-suffix player IDs. Positions beyond the sanitized "
                "text length are clamped to 100% for summaries."
            ),
            "",
            "- [`player_summary.csv`](player_summary.csv): one row per eligible player.",
            "- [`accuracy_bin_summary.csv`](accuracy_bin_summary.csv): primary "
            "player- and event-weighted bin results.",
            "- [`average_player_timing_distribution.csv`]"
            "(average_player_timing_distribution.csv): 5%-wide player timing "
            "histogram bins.",
            "- [`sensitivity_summary.csv`](sensitivity_summary.csv): alternate "
            "attempt/timing definitions.",
            "- [`minimum_attempts_robustness.csv`]"
            "(minimum_attempts_robustness.csv): checks at 20/30/50/100 attempts.",
            "- [`question_level.csv`](question_level.csv): one row per tossup "
            "with correlation, p-value, and FDR value.",
            "- [`question_accuracy_bin_summary.csv`]"
            "(question_accuracy_bin_summary.csv): bin summaries for every "
            "qualifying tossup.",
            "- [`analyze.py`](analyze.py): reproducible analysis.",
        ]
    )
    (HERE / "report.md").write_text("\n".join(report) + "\n", encoding="utf-8")


def main() -> None:
    buzzes = add_buzz_context(load_table("tossup_buzzes"))
    tossups = load_table("tossups")
    primary = write_primary_outputs(buzzes, tossups)
    sensitivity = write_sensitivity_output(buzzes)
    robustness = write_minimum_threshold_robustness(buzzes)
    make_plots(primary)
    write_report(buzzes, primary, sensitivity, robustness)
    print(f"Wrote analysis outputs to {HERE}")
    print(
        f"Eligible players: {len(primary['player_summary']):,}; "
        f"qualifying questions: "
        f"{int(primary['question_level']['qualifies'].sum()):,}"
    )


if __name__ == "__main__":
    main()
