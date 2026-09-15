"""Render auditable dimension-ablation reports from saved fold artifacts."""

from __future__ import annotations

import os
from pathlib import Path

import numpy as np
import pandas as pd


PRIMARY = "joint_tossup_event_log_loss"


def neg_f1(metrics):
    precision, recall = metrics.get("neg_precision"), metrics.get("neg_recall")
    if precision is None or recall is None or not np.isfinite([precision, recall]).all():
        return np.nan
    return 2 * precision * recall / (precision + recall) if precision + recall > 0 else 0.0


def training_diagnostics(summary: dict, train_dir: Path) -> dict:
    result = {
        f"train_{key}": summary.get(key)
        for key in ("players", "tossups", "events", "steps", "initial_loss",
                    "effective_item_parameters")
    }
    result.update({f"train_observations_{key}": value
                   for key, value in summary.get("observation_counts", {}).items()})
    result["train_finite_losses"] = (
        int(summary["finite_losses"]) if "finite_losses" in summary else np.nan
    )
    players_path = train_dir / "players.csv"
    if players_path.exists():
        players = pd.read_csv(players_path)
        for parameter in ("alpha", "beta"):
            for slice_name in ("scalar", "first", "middle", "last"):
                columns = [c for c in players if c == parameter] if slice_name == "scalar" else [
                    c for c in players if c.startswith(f"{parameter}_{slice_name}_")
                ]
                if not columns:
                    continue
                values = players[columns].to_numpy(dtype=float).ravel()
                values = values[np.isfinite(values)]
                if not len(values):
                    continue
                prefix = f"fitted_{parameter}_{slice_name}"
                result[f"{prefix}_mean"] = float(values.mean())
                result[f"{prefix}_std"] = float(values.std())
                result[f"{prefix}_negative_fraction"] = float((values < 0).mean())
    return result


def number(value, digits=6):
    if value is None or pd.isna(value):
        return "—"
    return f"{value:.{digits}g}"


def table(headers, rows):
    return [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
        *("| " + " | ".join(str(v) for v in row) + " |" for row in rows),
        "",
    ]


def mean_sd(row, metric):
    mean = row.get(f"{metric}_fold_mean")
    sd = row.get(f"{metric}_fold_std")
    n = row.get(f"{metric}_fold_n", 0)
    return f"{number(mean)} ± {number(sd)} (n={0 if pd.isna(n) else int(n)})"


def write_report(config, frame, per_fold, path, model_specs, plot_metrics):
    """Keep every saved metric visible, with aggregation and missingness explicit."""
    tolerance = 100 * config.plateau_relative_tolerance
    metric_doc = os.path.relpath(
        Path(__file__).resolve().parents[2] / "compirt_eval" / "METRICS.md", path.parent
    )
    completed = int(per_fold["complete"].sum())
    expected = len(config.models) * len(config.dimensions) * len(config.folds)
    lines = [
        f"# Perceived difficulty and logit dimension ablation: {config.steps:,} steps",
        "",
        f"**Coverage: {completed}/{expected} fits complete.** "
        f"Dimensions tested: {', '.join(map(str, config.dimensions))}. "
        "Selection uses pooled held-out joint event log loss (lower is better).",
        "",
        "## Selection and interpretation",
        "",
        f"For each model, select the smallest tested dimension with loss ≤ "
        f"(1 + {config.plateau_relative_tolerance:g}) × its best loss "
        f"(a {tolerance:g}% relative tolerance). Only points with all requested "
        "folds and required scoring artifacts are eligible.",
        "",
    ]
    selection_rows = []
    conclusions = []
    for model in config.models:
        rows = frame[(frame.model == model) & frame[PRIMARY].notna()]
        selected_rows = rows[rows.selected_dimension]
        if selected_rows.empty:
            selection_rows.append([model, "—", "—", "—", "—", "—", "—"])
            continue
        selected = selected_rows.iloc[0]
        best = rows.sort_values([PRIMARY, "dimensions"]).iloc[0]
        gap = selected[PRIMARY] - best[PRIMARY]
        selection_rows.append([
            model, int(selected.dimensions), number(selected[PRIMARY]),
            int(best.dimensions), number(best[PRIMARY]), number(gap),
            f"{100 * gap / best[PRIMARY]:.3f}%",
        ])
        cutoff = best[PRIMARY] * (1 + config.plateau_relative_tolerance)
        conclusions.append(
            f"- **{model}:** cutoff {cutoff:.6f}; selected K={int(selected.dimensions)} "
            f"with {number(selected.get('effective_parameter_count_fold_mean'))} "
            "effective parameters (fold mean). "
            + ("The best loss is at the largest tested dimension, so the search "
               "does not establish an optimum beyond this grid."
               if best.dimensions == max(config.dimensions) else
               "The selection favors smaller capacity within the stated tolerance.")
        )
    lines += table(
        ["Model", "Selected K", "Selected joint LL", "Best K", "Best joint LL",
         "Selected − best", "Relative gap"], selection_rows
    )
    lines += conclusions + [
        "",
        "These are model-selection scores on the same folds used to choose K, "
        "not an unbiased final test estimate. The tolerance is a capacity rule, "
        "not a significance test or an absolute performance target. One optimizer "
        "seed cannot establish seed robustness; fold SD is descriptive, not a "
        "confidence interval, since training sets overlap.",
        "",
        "### Full capacity grid",
        "",
    ]
    lines += table(["Model", "K", "Complete folds", "Joint LL (pooled)",
                    "Joint LL (fold mean ± SD)", "Rank", "Within tolerance", "Selected",
                    "Effective parameters (fold mean)"], [
        [r.model, int(r.dimensions), f"{int(r.complete_folds)}/{int(r.required_folds)}",
         number(r.get(PRIMARY)), mean_sd(r, PRIMARY), number(r.primary_rank),
         "yes" if r.within_plateau else "no", "yes" if r.selected_dimension else "no",
         number(r.get("effective_parameter_count_fold_mean"))]
        for _, r in frame.iterrows()
    ])
    lines += [
        "## Experimental protocol",
        "",
    ]
    lines += table(["Setting", "Value"], [
        ["Dataset", f"`{config.base_split}`"],
        ["Holdout", "Five-fold whole-game matrix infill, stratified within tournament/round; "
         "coverage repair returns games with unseen entities to training"],
        ["Scored fold IDs", ", ".join(map(str, config.folds))],
        ["Split seed / optimization seed", f"{config.split_seed} / {config.optimization_seed}"],
        ["Fit and replay", "SVI on training games; frozen player/item posterior-median predictions on held-out games"],
        ["Steps / learning rate / device", f"{config.steps} / {config.lr} / {config.device}"],
        ["Bernstein degree", config.degree],
        ["Relevance / drop Dirichlet concentration", f"{config.relevance_concentration} / {config.drop_concentration}"],
        ["Other priors", "theta and start difficulty: Normal(0,1); total drop: LogNormal(0,0.5); simplex relevance"],
        ["Terminal intercepts / bouncebacks", "Disabled / excluded"],
        ["Posterior draws requested", config.posterior_draws],
        ["Survival row × dimension budget", config.survival_chunk_dimension_budget],
        ["Data directory override", config.data_dir or "None (repository default)"],
    ])
    lines += [
        "The evaluation estimates missing interactions among already observed players "
        "and questions. It does not test new-player or new-question generalization.",
        "",
        "Both arms share correctness `zC = sum_k r_jk (theta_ik − d_jk(x))`. "
        "Scalar perceived-logit uses `zH = alpha_i zC + beta_i`. Three-slice "
        "perceived-difficulty uses `zH = sum_k r_jk (theta_ik − alpha_i,s,k d_jk(x) "
        "+ beta_i,s,k)`, with slices x < 1/3, 1/3 ≤ x < 2/3, and x ≥ 2/3. "
        "K changes latent dimension; the logit transform remains scalar per player.",
        "",
    ]
    lines += table(["Model", "Alpha prior", "Beta prior", "Transform parameters per player"], [
        [model, model_specs[model]["alpha_prior_description"],
         model_specs[model]["beta_prior_description"],
         "2" if model == "perceived-logit" else "6K"] for model in config.models
    ])
    lines += [
        "Alpha is unconstrained in these sweeps. The two arms differ in transform "
        "placement, alpha prior, and parameter count; their comparison does not "
        "isolate slicing alone. With P players, Q items, degree p and K dimensions, "
        "effective item parameters per item are `(p+2)K−1`; total effective "
        "parameters are `P(K+2)+Q((p+2)K−1)` for logit and "
        "`7PK+Q((p+2)K−1)` for three-slice difficulty.",
        "",
        "## How to read the scores",
        "",
        "Pooled tables recompute scores from concatenated held-out rows. "
        "Correctness and neg detection condition on observed BUZZ rows, with a "
        "0.5 classification threshold. Neg F1 is computed from precision and "
        "recall at the same aggregation level. Joint LL includes first-buzz "
        "identity, position, correctness and no-buzz outcomes. Position errors "
        "condition on observed buzzes and use relative question position.",
        "",
        "All rates are fractions (0.01 = 1 percentage point). Positive position "
        "bias means predicted later; positive no-buzz error means overprediction. "
        "Loss, ECE, Brier and absolute errors are better when lower; accuracy, "
        "AUC, precision, recall, F1 and rank agreement are better when higher. "
        "Signed biases target zero. Final-decile mass is descriptive. "
        "Integrated Brier pools event-weighted Brier scores on the time grid. "
        "Downstream and identity tables show equally weighted fold mean ± sample "
        "SD and the number of available folds, rather than pooled nonlinear scores.",
        "",
        f"See the [metric contract]({metric_doc}) for definitions and denominators. "
        "A dash means unavailable, never zero. The appendix exposes every numeric "
        "fold metric, including denominator counts and diagnostics.",
        "",
    ]
    sections = [
        ("Pooled correctness and neg detection", ["accuracy", "all_correct_accuracy",
         "accuracy_lift_over_all_correct", "log_loss", "auc", "ece", "brier",
         "neg_precision", "neg_recall", "neg_f1", "neg_average_precision"], False),
        ("Pooled timing and no-buzz diagnostics", [PRIMARY, "integrated_brier_score",
         "buzz_position_mae", "buzz_position_median_absolute_error", "buzz_position_bias",
         "no_buzz_observed_rate", "no_buzz_predicted_rate", "no_buzz_calibration_error",
         "no_buzz_brier", "full_pmf_final_decile_mass", "full_pmf_max_mass_error"], False),
        ("First-buzzer and downstream outcomes: fold mean ± SD", [
         "first_buzzer_top1_accuracy", "first_buzzer_mean_reciprocal_rank",
         "first_buzzer_log_loss", "first_buzzer_team_replay_accuracy",
         "tossup_scorer_player_replay_accuracy", "tossup_scorer_team_replay_accuracy",
         "tossup_game_winner_accuracy", "tossup_game_margin_mae",
         "tournament_player_ppg_spearman", "tournament_player_ppg_mae",
         "tournament_player_ppg_top10_overlap"], True),
        ("Training and capacity: fold mean ± SD", ["effective_parameter_count",
         "train_effective_item_parameters", "train_steps", "train_finite_losses",
         "train_initial_loss", "final_loss", "best_loss", "last_100_loss_slope"], True),
        ("Fitted perception parameters: fold mean ± SD", [
            c.removesuffix("_fold_mean") for c in frame
            if c.startswith("fitted_") and c.endswith("_fold_mean")
            and ("_mean_fold_mean" in c or "_negative_fraction_fold_mean" in c)
        ], True),
        ("Coverage and denominators: pooled counts", ["observations", "full_pmf_events",
         "survival_events"], False),
    ]
    for title, metrics, fold_average in sections:
        lines += [f"## {title}", ""]
        for model in config.models:
            rows = frame[frame.model == model].sort_values("dimensions")
            lines += [f"### {model}", ""]
            lines += table(["Metric", *(f"K={int(r.dimensions)}" for _, r in rows.iterrows())], [
                [f"`{metric}`", *(mean_sd(r, metric) if fold_average else number(r.get(metric))
                                   for _, r in rows.iterrows())] for metric in metrics
            ])
    lines += [
        "Training losses are the saved SVI objective, not held-out log loss. "
        "Finite losses do not establish convergence; negative final-100-step "
        "slopes indicate the objective was still descending locally. Parameter "
        "summaries below describe fitted posterior medians across players and "
        "dimensions (with separate slices); they are not posterior uncertainty "
        "intervals or independent samples across folds.",
        "",
        "## Matched-fold selected versus best dimension",
        "",
        "Differences are selected minus best joint LL on the same fold; positive "
        "values favor the best-loss dimension. These pairs describe the cost of "
        "the capacity rule without making a significance claim.",
        "",
    ]
    pairs = []
    for model in config.models:
        eligible = frame[(frame.model == model) & frame[PRIMARY].notna()]
        if eligible.empty or not eligible.selected_dimension.any():
            continue
        selected_k = int(eligible[eligible.selected_dimension].iloc[0].dimensions)
        best_k = int(eligible.sort_values([PRIMARY, "dimensions"]).iloc[0].dimensions)
        folds = per_fold[(per_fold.model == model) & per_fold.complete]
        for fold in config.folds:
            a = folds[(folds.dimensions == selected_k) & (folds.fold == fold)]
            b = folds[(folds.dimensions == best_k) & (folds.fold == fold)]
            if a.empty or b.empty:
                continue
            av, bv = a.iloc[0].get(PRIMARY, np.nan), b.iloc[0].get(PRIMARY, np.nan)
            pairs.append([model, fold, selected_k, best_k, number(av), number(bv), number(av - bv)])
    lines += table(["Model", "Fold", "Selected K", "Best K", "Selected LL", "Best LL", "Difference"], pairs)
    lines += ["## Figures", ""]
    for metric, label in plot_metrics.items():
        if (path.parent / "graphs" / f"{metric}_vs_dimensions.png").exists():
            lines += [f"![{label}](graphs/{metric}_vs_dimensions.png)", ""]
    lines += ["## Complete metric appendix: fold mean ± SD", "",
              "Each cell includes n, the number of finite fold values used. "
              "Within-fit parameter SD and across-fold SD are different: an "
              "`fitted_*_std` row averages the within-fit dispersion, with ± "
              "showing variation of that dispersion across folds.", ""]
    metrics = sorted(c.removesuffix("_fold_mean") for c in frame if c.endswith("_fold_mean"))
    for model in config.models:
        rows = frame[frame.model == model].sort_values("dimensions")
        lines += [f"### {model}", ""]
        lines += table(["Metric", *(f"K={int(r.dimensions)}" for _, r in rows.iterrows())], [
            [f"`{metric}`", *(mean_sd(r, metric) for _, r in rows.iterrows())] for metric in metrics
        ])
    lines += ["## Artifact index and reproducibility", "",
              "[Saved configuration](../configuration.json) · [Per-fold values](per_fold.csv) · "
              "[Fold mean/SD](fold_mean_std.csv) · [Pooled values](pooled.csv)", "",
              "Each fit links to its saved commands, training summary, and evaluator report. "
              "Training posterior quantiles and player parameters are beside the training summary. "
              "Training-set predictive metrics, optimizer-seed replication, posterior-predictive "
              "intervals, and a separate final test estimate are not supplied by this sweep.", ""]
    artifacts = []
    for _, row in per_fold.iterrows():
        run = Path(row.run_path)
        def link(label, relative):
            target = run / relative
            return f"[{label}]({os.path.relpath(target, path.parent)})" if target.exists() else "—"
        artifacts.append([row.model, int(row.dimensions), int(row.fold),
                          "complete" if row.complete else "incomplete",
                          link("commands", "command.json"),
                          link("training", "train/pyramidal/summary.json"),
                          link("evaluation", "evaluation/experiment_report.md"),
                          row.get("missing_artifacts", "") or "—"])
    lines += table(["Model", "K", "Fold", "Status", "Commands", "Training", "Evaluation", "Missing required artifacts"], artifacts)
    lines += ["Regenerate from the saved configuration without refitting:", "", "```python",
              "import json", "from pathlib import Path",
              "from run_scripts.double_difficulty.run_perception_dimension_ablation import Configuration, aggregate",
              f"root = Path({os.path.relpath(Path(config.root), Path(__file__).resolve().parents[2])!r})",
              "saved = json.loads((root / 'configuration.json').read_text())",
              "saved['root'] = str(root.resolve())", "aggregate(Configuration(**saved))", "```", ""]
    path.write_text("\n".join(lines), encoding="utf-8")


def write_budget_comparison(configs, path):
    """Compare matching dimensions only when non-budget settings agree."""
    from dataclasses import asdict

    path.parent.mkdir(parents=True, exist_ok=True)
    lines = ["# Perceived difficulty and logit ablation: optimization-budget comparison", "",
             "This report compares the saved dimension sweeps at matching K. "
             "Each detailed report includes all scores, fold variability, parameter "
             "diagnostics, coverage and source links. Scores are pooled unless "
             "explicitly labeled as fold statistics.", ""]
    frames = {}
    for config in configs:
        root = Path(config.root)
        frames[config.root] = (
            pd.read_csv(root / "aggregate" / "pooled.csv"),
            pd.read_csv(root / "aggregate" / "per_fold.csv"),
        )
        link = os.path.relpath(root / "aggregate" / "summary.md", path.parent)
        lines.append(f"- [{config.steps:,} steps: {', '.join(config.models)}]({link})")
    lines += ["", "## Selected capacities", ""]
    selections = []
    for config in configs:
        frame, _ = frames[config.root]
        for _, row in frame[frame.selected_dimension].iterrows():
            selections.append([row.model, config.steps, int(row.dimensions),
                               number(row[PRIMARY]), number(row.get("effective_parameter_count_fold_mean")),
                               number(row.get("accuracy")), number(row.get("neg_f1")),
                               number(row.get("buzz_position_mae"))])
    lines += table(["Model", "Steps", "Selected K", "Joint LL", "Parameters (fold mean)",
                    "Accuracy", "Neg F1", "Position MAE"], selections)
    lines += ["## Matched-dimension changes", "",
              "Delta is longer-budget minus shorter-budget. Negative loss/MAE "
              "deltas favor longer training. Accuracy and F1 deltas are percentage "
              "points. Matched-fold joint-loss SD is descriptive, not a confidence "
              "interval. Only complete points with identical non-budget settings "
              "are compared; different K selections are not matched controls.", ""]
    comparisons = []
    metrics = [PRIMARY, "log_loss", "accuracy", "neg_f1", "buzz_position_mae"]
    ordered = sorted(configs, key=lambda c: c.steps)
    for i, short in enumerate(ordered):
        for long in ordered[i + 1:]:
            if short.steps == long.steps:
                continue
            ignore = {"root", "models", "dimensions", "steps"}
            a = {k: v for k, v in asdict(short).items() if k not in ignore}
            b = {k: v for k, v in asdict(long).items() if k not in ignore}
            if a != b:
                raise ValueError("Budget comparison requires matching non-budget settings")
            sf, sp = frames[short.root]
            lf, lp = frames[long.root]
            matched = sf.merge(lf, on=["model", "dimensions"], suffixes=("_short", "_long"))
            for _, row in matched.iterrows():
                if (row.complete_folds_short != row.required_folds_short
                        or row.complete_folds_long != row.required_folds_long):
                    continue
                sm = sp[(sp.model == row.model) & (sp.dimensions == row.dimensions) & sp.complete]
                lm = lp[(lp.model == row.model) & (lp.dimensions == row.dimensions) & lp.complete]
                paired = sm.merge(lm, on="fold", suffixes=("_short", "_long"))
                delta = paired[f"{PRIMARY}_long"] - paired[f"{PRIMARY}_short"]
                values = []
                for metric in metrics:
                    change = row.get(f"{metric}_long", np.nan) - row.get(f"{metric}_short", np.nan)
                    values.append(number(change * (100 if metric in {"accuracy", "neg_f1"} else 1)))
                comparisons.append([row.model, int(row.dimensions), f"{short.steps} → {long.steps}",
                                    number(row[f"{PRIMARY}_short"]), number(row[f"{PRIMARY}_long"]),
                                    *values, f"{number(delta.mean())} ± {number(delta.std())}",
                                    f"{int((delta < 0).sum())}/{int(delta.notna().sum())}"])
    lines += table(["Model", "K", "Steps", "Short joint LL", "Long joint LL", "Δ joint LL",
                    "Δ correctness LL", "Δ accuracy (pp)", "Δ neg F1 (pp)", "Δ position MAE",
                    "Fold Δ joint LL mean ± SD", "Folds with lower joint LL"], comparisons)
    lines += ["## Interpretation limits", "",
              "The 1% selection rule is applied separately within each saved grid. "
              "A sparse follow-up grid does not establish the smallest adequate K "
              "among dimensions that were not rerun. Hyperparameter selection and "
              "scoring share folds; these results require a separate test or nested "
              "selection for an unbiased final estimate. The arms also differ in "
              "prior and transform structure, so their comparison does not isolate "
              "slicing. Training loss slopes and fitted alpha/beta distributions "
              "are available in the linked reports; these fits use one optimizer seed.", ""]
    path.write_text("\n".join(lines), encoding="utf-8")


def main():
    import argparse
    import json
    from run_scripts.double_difficulty.run_perception_dimension_ablation import Configuration, aggregate

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("roots", nargs="+", type=Path)
    parser.add_argument("--comparison-output", type=Path)
    args = parser.parse_args()
    configs = []
    for root in args.roots:
        saved = json.loads((root / "configuration.json").read_text())
        saved["root"] = str(root.resolve())
        config = Configuration(**saved)
        aggregate(config)
        configs.append(config)
    if args.comparison_output:
        write_budget_comparison(configs, args.comparison_output)


if __name__ == "__main__":
    main()
