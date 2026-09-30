"""Markdown reports for compositional bonus folds, built from saved artifacts."""

from __future__ import annotations

import json
import os
from pathlib import Path

import pandas as pd

from compirt_eval.common.reports import (
    experiment_report_markdown, load_metrics_row, markdown_table,
)
from compirt_eval.common.report_paths import metrics_path


def evaluation_dir(fold_dir, arm):
    """Return the directory holding one arm's evaluation of a saved fold."""
    return Path(fold_dir) / ("evaluation" if arm == "compositional" else "synergy-evaluation")


def write_bonus_evaluation_report(output_dir, metrics=None):
    """Write experiment_report.md for a bonus-only evaluation.

    'metrics' defaults to the saved csvs/bonus_metrics.csv.
    """
    if metrics is None:
        metrics = load_metrics_row(output_dir, "bonus_metrics.csv")
    report = experiment_report_markdown(
        output_dir, tossup=None, bonus=metrics, title="Bonus Evaluation"
    )
    (output_dir / "experiment_report.md").write_text(report, encoding="utf-8")


def bonus_model_label(config, arm):
    """Return the table label for one arm, e.g. 'No synergy' or 'dot, additive, 1D'."""
    if config.get("bonus_aggregation") == "noisy-or":
        return "Noisy-OR (Eq. 9)"
    prefix = "Multidim difficulty; " if config.get("bonus_difficulty") == "multidim" else ""
    if config.get("bonus_aggregation") == "max":
        prefix = "Per-dimension max; " + prefix
    if arm == "compositional":
        return prefix + "No synergy"
    form = config.get("synergy_form", "dot")
    link = config.get("synergy_link", "additive")
    dimensions = config.get("synergy_dimensions", 1)
    return prefix + f"{form}, {link}, {dimensions}D"


def _metric_table(pooled, config, columns):
    """Render the pooled metrics named in 'columns' as one table row per arm."""
    frame = pd.DataFrame(pooled)
    frame.insert(0, "Model", [bonus_model_label(config, arm) for arm in frame.arm])
    selected = {key: label for key, label in columns.items() if key in frame}
    if not selected:
        return "Run `--collect-only` to add these metrics to this saved aggregate."
    return markdown_table(frame[["Model", *selected]].rename(columns=selected))


def _base_model_lines(config):
    """Describe the base logit that both arms share."""
    multidim = config.get("bonus_difficulty") == "multidim"
    aggregation = config.get("bonus_aggregation")
    if aggregation == "noisy-or":
        return [
            "Noisy-OR (Eq. 9) uses `p = 1 - product_i(1 - sigmoid(alpha_b dot theta_i - beta_b))`: "
            "the team answers when at least one member does, with members independent.", "",
        ]
    if aggregation == "max":
        formula = ("`eta = sum_k r_bk * (max_i theta_ik - beta_bk)`" if multidim
                   else "`eta = sum_k alpha_bk * max_i theta_ik - beta_b`")
        return [
            f"The base logit is {formula}. The maximum takes the best active teammate "
            "on each skill dimension before the part weights apply. "
            "The compositional arm fits this base logit alone.", "",
        ]
    if multidim:
        return [
            "The base logit is `eta = sum_k r_bk * (ts_k(R) - beta_bk)`, where "
            "`ts_k(R) = tau * logsumexp_{i in R}(theta_ik / tau)` pools players "
            "separately in each skill dimension, unnormalized by roster size. "
            "Relevance r is positive, and difficulty has one coordinate per skill "
            "dimension. Responses identify only `r_b dot beta_b`, not the individual "
            "difficulty coordinates. The compositional arm fits this base logit alone.", "",
        ]
    return [
        "The base logit is `eta = A_b(R) - beta_b`, using log-sum-exp aggregation "
        "unnormalized by roster size. The compositional arm fits this base logit alone.", "",
    ]


def _synergy_lines(config):
    """Describe the synergy arm's pair formula and link."""
    dimensions = config.get("synergy_dimensions", 1)
    if config.get("synergy_form", "dot") == "phi-psi":
        lines = [f"Phi-psi synergy learns two {dimensions}-dimensional vectors "
                 "per player: `s(R) = sum_d sum_{i<j} phi_id * phi_jd * (psi_id + psi_jd)`.", ""]
    else:
        lines = [f"Dot-product synergy learns one {dimensions}-dimensional vector "
                 "per player: `s(R) = sum_{i<j} psi_i dot psi_j`.", ""]
    if config.get("synergy_link", "additive") == "multiplicative":
        lines += ["The multiplicative link uses `eta * (1 + s(R))`. The multiplier "
                  "is unconstrained; values below zero reverse the base logit's sign.", ""]
    else:
        lines += ["The additive link uses `eta + s(R)`.", ""]
    return lines


def write_bonus_fold_reports(config, pooled=None):
    """Write each fold's evaluation report and the pooled aggregate/report.md.

    Reports are rendered from saved metrics; 'pooled' defaults to
    aggregate/pooled.json.
    """
    root = Path(config["root"])
    output = root / "aggregate"
    if pooled is None:
        pooled = json.loads((output / "pooled.json").read_text())
    for fold in config["folds"]:
        for arm in config["arms"]:
            evaluation = evaluation_dir(root / f"fold_{fold}", arm)
            if metrics_path(evaluation, "bonus_metrics.csv").exists():
                write_bonus_evaluation_report(evaluation)
    source = os.path.relpath(Path(config["stage1_root"]).resolve(), root.resolve())
    lines = [
        "# Compositional bonuses from frozen Stage-1 folds", "",
        "[Configuration](../configuration.json) · "
        "[Pooled metrics](pooled.csv) · [Per-fold metrics](per_fold.csv) · "
        "[Fold mean and standard deviation](fold_mean_std.csv)", "",
        f"Source: [saved Stage-1 folds](../{source}).", "",
        f"{config['steps']} SVI steps, learning rate {config['lr']}, seed {config['seed']}; "
        f"bonus discrimination prior `{config['alpha_prior']}`. Skills are fixed at "
        "the saved Stage-1 medians. All bonus parameters are fit on training games "
        "and frozen for held-out replay.", "",
        "## Bonus model", "",
        *_base_model_lines(config),
    ]
    if "synergy" in config["arms"]:
        lines += _synergy_lines(config)
    lines += [
        "The saved Stage-1 fits supply player skills. Every held-out player and part "
        "appears in training, and lineups are inferred from observed game buzzes, so "
        "these reused development folds measure frozen matrix infill. Reading synergy "
        "as teamwork requires a held-out recombined-roster experiment.", "",
        "## Pooled held-out metrics", "",
        "Metrics are computed on predictions pooled across folds. PPB MAE first "
        "averages observed and predicted bonus points within each team, then averages "
        "absolute errors across teams. Exact accuracy requires all three part labels "
        "to match.", "",
        _metric_table(pooled, config, {
            "auc": "AUC ↑", "log_loss": "Log loss ↓", "part_accuracy": "Part accuracy ↑",
            "brier": "Brier ↓", "ece": "ECE ↓", "exact_acc": "Exact accuracy ↑",
            "ppb_mae": "PPB MAE ↓",
        }), "",
        "## Difficulty, bonus-only team PPG and game margins", "",
        "Difficulty uses declared easy/medium/hard labels. Bonus-only PPG uses expected "
        "points on recorded bonus opportunities, divided by games played. Zero-bonus "
        "games count; incomplete prediction games are excluded. Pool folds before "
        "calculating team PPG, average team absolute errors within each tournament, "
        "then macro-average tournament MAE and defined Spearman correlations. Margin "
        "MAE averages absolute errors in signed team bonus-score differences across games.", "",
        _metric_table(pooled, config, {
            "part_accuracy_easy": "Easy accuracy ↑", "part_accuracy_medium": "Medium accuracy ↑",
            "part_accuracy_hard": "Hard accuracy ↑", "tournament_team_bonus_ppg_mae": "PPG MAE ↓",
            "tournament_team_bonus_ppg_spearman": "PPG Spearman ↑", "bonus_game_margin_mae": "Margin MAE ↓",
        }), "",
    ]
    for row in pooled:
        arm = row["arm"]
        # Link the per-arm outcome tables when this aggregate wrote them.
        if (output / arm / "bonus_team_ppg_leaderboard.csv").exists():
            lines += [f"{bonus_model_label(config, arm)}: "
                      f"[team PPG]({arm}/bonus_team_ppg_leaderboard.csv) · "
                      f"[tournament metrics]({arm}/bonus_team_ranking_metrics.csv) · "
                      f"[game margins]({arm}/bonus_game_margin_predictions.csv)", ""]
    lines += [
        "## Scoring population and checks", "",
        _metric_table(pooled, config, {
            "folds": "Folds", "parts": "Parts", "responses": "Bonuses",
            "games": "Games with bonuses", "teams": "Teams with bonuses",
        }), "",
        "PPG and margin populations also include zero-bonus games and teams; their "
        "counts are recorded separately in `pooled.csv`. Per-fold separation checks, "
        "dropped-row counts, finite-loss checks, and loss slopes are in `per_fold.csv`. "
        "Fold variation is descriptive. All fits use one optimization seed and the "
        "step budget above.", "",
    ]
    lines += ["## Fold artifacts", "",
              "| Fold | Model | Training | Held-out predictions | Evaluation | Checks |",
              "| --- | --- | --- | --- | --- | --- |"]
    for fold in config["folds"]:
        for arm in config["arms"]:
            base = f"../fold_{fold}"
            evaluation = evaluation_dir("", arm).name
            lines.append(
                f"| {fold} | {bonus_model_label(config, arm)} | "
                f"[fit]({base}/train/{arm}/summary.json) | "
                f"[predictions]({base}/holdout/{arm}/bonus_part_predictions.csv) | "
                f"[report]({base}/{evaluation}/experiment_report.md) | "
                f"[audit]({base}/{arm}_checks.json) |"
            )
    (output / "report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
