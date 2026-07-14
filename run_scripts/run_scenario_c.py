#!/usr/bin/env python3
"""Fit frozen-global test items and write the paper Scenario C evaluation.

This runner is invoked by ``run_compirt_holdout`` only when ``RUN_C1_C4=1``.
It is shared by every model family whose bonus stage is the root compositional
model: baseline, multidimensional difficulty, and cumulative TF-IDF.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pyro
import torch

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from compirt_data import (
    DEFAULT_DATA_DIR,
    bonus_tensors,
    build_bonus_part_observations,
    filter_tournament,
    load_hf_tables,
)
from compirt_eval.eval_docs import markdown_table
from compirt_eval.outputs import csv_path, evaluation_output_dirs, graph_path
from compirt_eval.scenario_c import (
    SCENARIOS,
    add_lineup_metadata,
    build_training_context,
    classify_observations,
    composition_graph_summary,
    model_difference_rows,
    scenario_count_table,
    scenario_metrics,
    validate_historical_prediction_ids,
)
from lineup import LineupIndex
from scenario_c_model import frozen_global_item_model, frozen_global_predictions
from train_compositional import load_player_skills
from utils.saving import save_loss_plot, tensor_values
from utils.training import fit_svi, require_device


def _load_summary(path):
    return json.loads((path / "summary.json").read_text(encoding="utf-8"))


def _fixed_globals(results_dir, player_ids, psi_informed, device):
    """Load and align historical globals to the test-player index."""
    summary = _load_summary(results_dir)
    tau = torch.tensor(
        float((results_dir / "tau.txt").read_text(encoding="utf-8").strip()),
        dtype=torch.float32,
        device=device,
    )
    psi = None
    profile_path = results_dir / "player_synergy_profiles.csv"
    if summary.get("use_synergy"):
        if not profile_path.exists():
            raise ValueError(
                f"Historical synergy run lacks {profile_path.name}; rerun it with "
                "--save-synergy-details"
            )
        profiles = pd.read_csv(profile_path).set_index("player_id")
        psi_columns = sorted(
            [column for column in profiles if column.startswith("psi_")],
            key=lambda value: int(value.removeprefix("psi_")),
        )
        psi_values = np.zeros((len(player_ids), len(psi_columns)), dtype=np.float32)
        for index, player_id in enumerate(player_ids):
            if player_id in psi_informed and player_id in profiles.index:
                psi_values[index] = profiles.loc[player_id, psi_columns].to_numpy(dtype=float)
        psi = torch.tensor(psi_values, dtype=torch.float32, device=device)

    scale = bias = None
    if summary.get("calibrate_correctness"):
        scale = torch.tensor(float(summary["correctness_scale"]), device=device)
        bias = torch.tensor(float(summary["correctness_bias"]), device=device)
    return summary, tau, psi, scale, bias


def _fit_branch(
    name,
    observations,
    player_ids,
    theta,
    historical_results,
    output_dir,
    context,
    args,
):
    """Fit test item sites for one frozen historical bonus branch."""
    output_dir.mkdir(parents=True, exist_ok=True)
    data = bonus_tensors(observations, player_ids, args.device)
    summary, tau, psi, scale, bias = _fixed_globals(
        historical_results, player_ids, context["psi_informed"], args.device
    )
    pyro.set_rng_seed(args.seed)
    model_args = (data, theta, tau, psi, scale, bias)
    posterior, losses = fit_svi(
        frozen_global_item_model, model_args, args.steps, args.lr
    )
    probabilities, aggregates, synergy = frozen_global_predictions(
        data, theta, posterior, tau, psi, scale, bias
    )
    predictions = observations.copy()
    predictions["predicted_correct"] = tensor_values(probabilities)
    predictions["aggregate"] = tensor_values(aggregates)
    predictions["synergy_contribution"] = tensor_values(synergy)
    predictions.to_csv(output_dir / "bonus_part_predictions.csv", index=False)
    team_predictions = predictions.groupby("response_id", as_index=False).agg(
        game_id=("game_id", "first"),
        team_id=("team_id", "first"),
        tournament_id=("tournament_id", "first"),
        tier=("tier", "first"),
        scenario=("scenario", "first"),
        roster_key=("roster_key", "first"),
        total_points=("total_points", "first"),
        predicted_points=("predicted_correct", lambda values: float(10.0 * values.sum())),
    )
    team_predictions.to_csv(output_dir / "team_predictions.csv", index=False)

    part_parameters = {"bonus_part_id": data["part_ids"], "beta": tensor_values(posterior["beta"])}
    for dimension in range(posterior["alpha"].shape[1]):
        part_parameters[f"alpha_{dimension + 1}"] = tensor_values(
            posterior["alpha"][:, dimension]
        )
    pd.DataFrame(part_parameters).to_csv(output_dir / "bonus_parts.csv", index=False)
    save_loss_plot(output_dir, losses, f"Scenario C {name} test-item loss")
    branch_summary = {
        "model": name,
        "train_split": args.train_split,
        "test_split": args.test_split,
        "steps": args.steps,
        "lr": args.lr,
        "seed": args.seed,
        "final_loss": losses[-1],
        "parts": len(data["part_ids"]),
        "observations": len(observations),
        "test_player_parameter_source": "test_tossup_posterior_initialized_from_training_priors",
        "test_bonus_item_parameter_source": "fit_from_test_bonus_responses",
        "synergy_parameter_source": (
            "training_bonus_posterior_frozen_during_test"
            if psi is not None
            else "not_used"
        ),
        "aggregation_parameter_source": "training_bonus_posterior_frozen_during_test",
        "prediction_outcomes_used_for_item_estimation": True,
        "known_member_definition": "present_in_training_pyramidal_fit",
        "historical_summary": summary,
    }
    (output_dir / "summary.json").write_text(
        json.dumps(branch_summary, indent=2), encoding="utf-8"
    )
    return predictions, branch_summary


def _metric_rows(parts, model, lineup_scope, args):
    rows = []
    for scenario in SCENARIOS:
        values = scenario_metrics(parts, scenario)
        values.update({"model": model, "lineup_scope": lineup_scope, "scenario": scenario})
        rows.append(values)
    return rows


def _c4_base_rates(training_parts, predictions_by_model, scopes):
    """Compare C4 predictions with training-only tier part/PPB base rates."""
    rows = []
    for scope_name, scope_filter in scopes.items():
        scoped_training = training_parts[scope_filter(training_parts)]
        if scoped_training.empty:
            continue
        training_responses = scoped_training.drop_duplicates("response_id")
        global_part = float(scoped_training["correct"].mean())
        training_game_ppb = training_responses.groupby(
            ["tier", "game_id", "team_id"], as_index=False
        ).agg(ppb=("total_points", "mean"))
        global_ppb = float(training_game_ppb["ppb"].mean())
        tier_part = scoped_training.groupby("tier")["correct"].agg(["mean", "size"])
        tier_ppb = training_game_ppb.groupby("tier")["ppb"].agg(["mean", "size"])
        for model, predictions in predictions_by_model.items():
            c4 = predictions[(predictions["scenario"] == "C4") & scope_filter(predictions)]
            for tier, parts in c4.groupby("tier"):
                responses = parts.drop_duplicates("response_id")
                fallback = tier not in tier_part.index or tier not in tier_ppb.index
                train_part = global_part if fallback else float(tier_part.loc[tier, "mean"])
                train_ppb = global_ppb if fallback else float(tier_ppb.loc[tier, "mean"])
                predicted_part = float(parts["predicted_correct"].mean())
                predicted_responses = parts.groupby("response_id", as_index=False).agg(
                    game_id=("game_id", "first"),
                    team_id=("team_id", "first"),
                    predicted_points=("predicted_correct", lambda values: float(10.0 * values.sum())),
                )
                predicted_ppb = float(
                    predicted_responses.groupby(["game_id", "team_id"])[
                        "predicted_points"
                    ].mean().mean()
                )
                rows.append(
                    {
                        "model": model,
                        "lineup_scope": scope_name,
                        "tier": tier,
                        "training_part_correct_rate": train_part,
                        "training_ppb": train_ppb,
                        "c4_mean_predicted_part_probability": predicted_part,
                        "c4_mean_predicted_ppb": predicted_ppb,
                        "part_probability_gap": predicted_part - train_part,
                        "ppb_gap": predicted_ppb - train_ppb,
                        "training_part_count": len(scoped_training) if fallback else int(tier_part.loc[tier, "size"]),
                        "training_game_team_count": len(training_game_ppb) if fallback else int(tier_ppb.loc[tier, "size"]),
                        "c4_part_count": len(parts),
                        "c4_response_count": len(responses),
                        "used_global_training_fallback": fallback,
                    }
                )
    return pd.DataFrame(rows)


def _write_metric_plot(metrics, output_dir):
    selected = metrics[(metrics["lineup_scope"] == "all_lineups") & metrics["scenario"].isin(["C1", "C2", "C3", "C4"])]
    if selected.empty:
        return
    fig, ax = plt.subplots(figsize=(8, 5))
    x = np.arange(4)
    for offset, (model, group) in zip((-0.12, 0.12), selected.groupby("model")):
        ordered = group.set_index("scenario").reindex(["C1", "C2", "C3", "C4"])
        ax.plot(x + offset, ordered["auc"], marker="o", label=model)
    ax.set_xticks(x, ["C1", "C2", "C3", "C4"])
    ax.set(title="Scenario C bonus-part AUC", xlabel="Roster observability", ylabel="AUC")
    ax.grid(alpha=0.25)
    ax.legend()
    fig.tight_layout()
    fig.savefig(graph_path(output_dir, "scenario_c_auc.png"), dpi=160)
    plt.close(fig)


def _write_report(
    counts, metrics, comparisons, diagnostics, graph_stats, c4, output_dir, args
):
    cross = counts[
        (counts["lineup_scope"] == "all_lineups") & (counts["scenario"] == "C2")
    ]
    cross_responses = int(cross["cross_team_c2_responses"].iloc[0]) if len(cross) else 0
    cross_games = int(cross["cross_team_c2_games"].iloc[0]) if len(cross) else 0
    warning = ""
    if cross_games < args.min_cross_team_games:
        warning = (
            "**C2 interpretation warning:** cross-team recombination is too sparse "
            "for the paper's central claim; aggregate C2 primarily measures roster "
            "substitution robustness.\n\n"
        )
    report = (
        "# CompIRT Scenario C Report\n\n"
        "Temporal test evaluation with test-person and test-item co-estimation.\n\n"
        + warning
        + "Test item parameters are fit from the reported test outcomes and may "
        "absorb team-level variation, attenuating frozen-synergy differences. "
        "Exact-slug identity linking may inflate C3/C4; same-school substitutions "
        "may dominate C2 without Chicago Open; and zero-buzz lineup inference may "
        "create artificial roster novelty. Current data does not reproduce the "
        "paper's full nine-tournament experiment.\n\n"
        "## Sample Sizes and Coverage\n\n"
        + markdown_table(counts)
        + "\n\n## Primary Metrics\n\n"
        + markdown_table(metrics)
        + "\n\n## Synergy Point Differences on Identical Observations\n\n"
        + markdown_table(comparisons)
        + "\n\n## C2/C3 Diagnostic Slices\n\n"
        + markdown_table(diagnostics)
        + "\n\n## Training Composition Graph\n\n"
        + markdown_table(graph_stats)
        + "\n\n## C4 Tier Base-Rate Comparison\n\n"
        + markdown_table(c4)
        + f"\n\nCross-team C2 responses: {cross_responses}.\n"
    )
    (output_dir / "experiment_report.md").write_text(report, encoding="utf-8")


def run(args):
    require_device(args.device)
    evaluation_output_dirs(args.evaluation_dir)
    train_tables = filter_tournament(load_hf_tables(args.data_dir, args.train_split), args.tournament)
    test_tables = filter_tournament(load_hf_tables(args.data_dir, args.test_split), args.tournament)
    train_lineups = LineupIndex.load_or_build(train_tables)
    test_lineups = LineupIndex.load_or_build(test_tables)
    train_parts = add_lineup_metadata(build_bonus_part_observations(train_tables, train_lineups), train_tables, train_lineups)
    test_parts = add_lineup_metadata(build_bonus_part_observations(test_tables, test_lineups), test_tables, test_lineups)

    eligible_ids, response_ids = validate_historical_prediction_ids(
        args.train_compositional / "bonus_part_predictions.csv",
        args.train_synergy / "bonus_part_predictions.csv",
    )
    train_parts["observation_id"] = train_parts["observation_id"].astype(str)
    train_parts = train_parts[
        train_parts["observation_id"].isin(eligible_ids)
    ].reset_index(drop=True)
    recovered_ids = set(train_parts["observation_id"])
    if recovered_ids != eligible_ids:
        missing = sorted(eligible_ids - recovered_ids)[:5]
        extra = sorted(recovered_ids - eligible_ids)[:5]
        raise ValueError(
            "Could not recover the exact historical Stage-2 observations from "
            f"the training split: missing={missing}, extra={extra}"
        )
    pd.DataFrame({"response_id": response_ids}).to_csv(
        csv_path(args.evaluation_dir, "eligible_training_response_ids.csv"), index=False
    )
    theta_known = pd.read_csv(args.train_player_skills)["player_id"].astype(str)
    context = build_training_context(train_parts, theta_known)
    test_parts = classify_observations(test_parts, context)

    player_ids, theta = load_player_skills(args.test_player_skills, args.device)
    known_test = set(player_ids)
    keep = test_parts["player_ids"].map(
        lambda roster: bool(roster) and all(str(player) in known_test for player in roster)
    )
    test_parts = test_parts[keep].reset_index(drop=True)
    if test_parts.empty:
        raise ValueError("No Scenario C test observations have complete test-player skills")

    no_synergy, no_summary = _fit_branch(
        "no_synergy", test_parts, player_ids, theta, args.train_compositional,
        args.output_root / "compositional", context, args,
    )
    synergy, synergy_summary = _fit_branch(
        "synergy", test_parts, player_ids, theta, args.train_synergy,
        args.output_root / "synergy", context, args,
    )
    predictions = {"no_synergy": no_synergy, "synergy": synergy}
    scopes = {
        "all_lineups": lambda frame: pd.Series(True, index=frame.index),
        "game_buzz_evidence_only": lambda frame: frame["lineup_has_game_buzz_evidence"],
    }
    count_frames, metric_rows, graph_rows = [], [], []
    for scope_name, scope_filter in scopes.items():
        scoped_train = train_parts[scope_filter(train_parts)].copy()
        scoped_context = build_training_context(scoped_train, theta_known)
        graph_rows.append(composition_graph_summary(scoped_context, scope_name))
        reference = no_synergy[scope_filter(no_synergy)].copy()
        count_frames.append(scenario_count_table(reference, scope_name))
        for model, frame in predictions.items():
            metric_rows.extend(_metric_rows(frame[scope_filter(frame)].copy(), model, scope_name, args))
    counts = pd.concat(count_frames, ignore_index=True)
    metrics = pd.DataFrame(metric_rows)
    graph_stats = pd.DataFrame(graph_rows)

    diagnostic_rows = []
    for scope_name, scope_filter in scopes.items():
        for model, frame in predictions.items():
            scoped = frame[scope_filter(frame)]
            c2 = scoped[scoped["scenario"] == "C2"].copy()
            c2["pair_novelty"] = np.select(
                [c2["training_pair_fraction"].eq(0), c2["training_pair_fraction"].eq(1)],
                ["all_pairs_new", "all_pairs_familiar"],
                default="partially_familiar",
            )
            for column in ("c2_provenance", "pair_novelty"):
                for value, group in c2.groupby(column):
                    row = scenario_metrics(group, "ALL")
                    row.update(
                        {
                            "diagnostic": column,
                            "group": value,
                            "model": model,
                            "lineup_scope": scope_name,
                        }
                    )
                    diagnostic_rows.append(row)
            c3 = scoped[scoped["scenario"] == "C3"]
            for (roster_size, unknown_count), group in c3.groupby(
                ["roster_size", "unknown_member_count"]
            ):
                row = scenario_metrics(group, "ALL")
                row.update(
                    {
                        "diagnostic": "c3_unknown_members",
                        "group": f"{unknown_count}-of-{roster_size}",
                        "model": model,
                        "lineup_scope": scope_name,
                    }
                )
                diagnostic_rows.append(row)
    diagnostics = pd.DataFrame(diagnostic_rows)

    comparison_rows = []
    for scope_name, scope_filter in scopes.items():
        left = no_synergy[scope_filter(no_synergy)].copy()
        right = synergy[scope_filter(synergy)].copy()
        for scenario in ("ALL", "C2"):
            for row in model_difference_rows(left, right, scenario):
                row["lineup_scope"] = scope_name
                comparison_rows.append(row)
    comparisons = pd.DataFrame(comparison_rows)
    c4 = _c4_base_rates(train_parts, predictions, scopes)

    counts.to_csv(csv_path(args.evaluation_dir, "scenario_counts.csv"), index=False)
    metrics.to_csv(csv_path(args.evaluation_dir, "scenario_metrics.csv"), index=False)
    comparisons.to_csv(csv_path(args.evaluation_dir, "synergy_comparison.csv"), index=False)
    graph_stats.to_csv(csv_path(args.evaluation_dir, "composition_graph_stats.csv"), index=False)
    c4.to_csv(csv_path(args.evaluation_dir, "c4_tier_base_rate_comparison.csv"), index=False)
    diagnostics.to_csv(csv_path(args.evaluation_dir, "scenario_diagnostic_metrics.csv"), index=False)
    diagnostic_columns = [
        "response_id", "game_id", "team_id", "tournament_id", "tier", "scenario",
        "roster_key", "roster_size", "unknown_member_count",
        "unknown_member_fraction", "theta_known_member_count", "psi_informed_member_count",
        "c2_provenance", "training_pair_fraction", "team_label_key",
        "test_team_label_seen_in_training", "all_members_shared_training_team_label",
        "all_members_same_training_component", "lineup_segment", "registered_roster_size",
        "inferred_lineup_size", "distinct_game_buzzers", "lineup_confidence",
        "lineup_resolution_rule",
        "lineup_has_game_buzz_evidence", "lineup_is_full_roster_fallback",
    ]
    no_synergy.drop_duplicates("response_id")[diagnostic_columns].to_csv(
        csv_path(args.evaluation_dir, "response_classification.csv"), index=False
    )
    _write_metric_plot(metrics, args.evaluation_dir)
    _write_report(
        counts,
        metrics,
        comparisons,
        diagnostics,
        graph_stats,
        c4,
        args.evaluation_dir,
        args,
    )
    combined_summary = {
        "run_c1_c4": True,
        "c2_cross_team_roster_count": int(
            no_synergy.loc[no_synergy["c2_provenance"] == "cross_team_recombination_candidate", "roster_key"].nunique()
        ),
        "c2_cross_team_game_count": int(
            no_synergy.loc[no_synergy["c2_provenance"] == "cross_team_recombination_candidate", "game_id"].nunique()
        ),
        "mixed_scenario_game_team_count": int(
            (
                no_synergy.drop_duplicates("response_id")
                .groupby(["game_id", "team_id"])["scenario"]
                .nunique()
                > 1
            ).sum()
        ),
        "zero_evidence_response_count": int(
            (~no_synergy.drop_duplicates("response_id")["lineup_has_game_buzz_evidence"]).sum()
        ),
        "full_roster_fallback_response_count": int(
            no_synergy.drop_duplicates("response_id")["lineup_is_full_roster_fallback"].sum()
        ),
        "no_synergy": no_summary,
        "synergy": synergy_summary,
    }
    (args.evaluation_dir / "summary.json").write_text(
        json.dumps(combined_summary, indent=2), encoding="utf-8"
    )


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR)
    parser.add_argument("--train-split", default="year_2024")
    parser.add_argument("--test-split", default="year_2025")
    parser.add_argument("--tournament")
    parser.add_argument("--train-player-skills", type=Path, required=True)
    parser.add_argument("--test-player-skills", type=Path, required=True)
    parser.add_argument("--train-compositional", type=Path, required=True)
    parser.add_argument("--train-synergy", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, required=True)
    parser.add_argument("--evaluation-dir", type=Path, required=True)
    parser.add_argument("--steps", type=int, default=2000)
    parser.add_argument("--lr", type=float, default=0.01)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--min-cross-team-games", type=int, default=10)
    parser.add_argument("--device", choices=("cpu", "cuda"), default="cpu")
    args = parser.parse_args(argv)
    if args.steps <= 0 or args.min_cross_team_games < 1:
        parser.error("steps and minimum cross-team games must be positive")
    return args


if __name__ == "__main__":
    run(parse_args())
