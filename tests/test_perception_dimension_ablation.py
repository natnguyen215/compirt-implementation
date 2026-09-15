"""Contracts for the unconstrained perception dimension sweep."""

from __future__ import annotations

from dataclasses import replace
import json
from pathlib import Path

import pandas as pd
import numpy as np

from run_scripts.double_difficulty.run_perception_dimension_ablation import (
    Configuration,
    PRIMARY_METRIC,
    collect_pooled,
    collect_per_fold,
    fold_dir,
    write_summary,
)


def configuration(tmp_path: Path) -> Configuration:
    return Configuration(
        root=str(tmp_path),
        models=["perceived-logit", "perceived-difficulty-three-slice"],
        dimensions=[1, 2, 3],
        base_split="year_2024",
        folds=[0, 1, 2, 3, 4],
        split_seed=42,
        optimization_seed=42,
        degree=3,
        relevance_concentration=2.0,
        drop_concentration=2.0,
        steps=3000,
        lr=0.005,
        device="cuda",
        posterior_draws=0,
        plateau_relative_tolerance=0.01,
        survival_chunk_dimension_budget=81920,
        data_dir=None,
    )


def test_plateau_rule_selects_smallest_dimension_within_one_percent(
    tmp_path, monkeypatch
):
    config = replace(
        configuration(tmp_path),
        models=["perceived-logit"],
        dimensions=[1, 2, 3],
        folds=[0],
    )
    per_fold = pd.DataFrame(
        [
            {
                "model": "perceived-logit",
                "dimensions": dimension,
                "fold": 0,
                "complete": True,
                "run_path": str(fold_dir(tmp_path, "perceived-logit", dimension, 0)),
            }
            for dimension in config.dimensions
        ]
    )
    scores = iter(
        [
            {PRIMARY_METRIC: 7.0},
            {PRIMARY_METRIC: 6.65},
            {PRIMARY_METRIC: 6.60},
        ]
    )
    monkeypatch.setattr(
        "run_scripts.double_difficulty.run_perception_dimension_ablation._pooled_scores",
        lambda _paths, **_kwargs: next(scores),
    )
    pooled = collect_pooled(config, per_fold)
    assert pooled.loc[pooled["within_plateau"], "dimensions"].tolist() == [2, 3]
    assert pooled.loc[pooled["selected_dimension"], "dimensions"].tolist() == [2]


def test_completion_marker_cannot_hide_missing_scoring_artifacts(tmp_path):
    config = replace(configuration(tmp_path), models=["perceived-logit"],
                     dimensions=[1], folds=[0])
    run = fold_dir(tmp_path, "perceived-logit", 1, 0)
    run.mkdir(parents=True)
    (run / ".complete.json").write_text("{}")
    per_fold = collect_per_fold(config)
    assert not per_fold.iloc[0].complete
    assert "tossup_full_pmf_scores.csv" in per_fold.iloc[0].missing_artifacts
    pooled = collect_pooled(config, per_fold)
    assert pooled.iloc[0].complete_folds == 0
    assert not pooled.iloc[0].selected_dimension
    write_summary(config, pooled, tmp_path / "summary.md", per_fold)
    assert "0/1 fits complete" in (tmp_path / "summary.md").read_text()


def test_report_preserves_all_metrics_and_distinguishes_pooled_from_fold_scores(
    tmp_path, monkeypatch
):
    config = replace(configuration(tmp_path), models=["perceived-logit"],
                     dimensions=[1], folds=[0, 1])
    per_fold = pd.DataFrame([
        {"model": "perceived-logit", "dimensions": 1, "fold": fold,
         "complete": True, "run_path": str(fold_dir(tmp_path, "perceived-logit", 1, fold)),
         PRIMARY_METRIC: loss, "accuracy": accuracy, "custom_diagnostic": fold + 10,
         "neg_f1": .4}
        for fold, loss, accuracy in [(0, 6.0, .6), (1, 8.0, .8)]
    ])
    monkeypatch.setattr(
        "run_scripts.double_difficulty.run_perception_dimension_ablation._pooled_scores",
        lambda *_args, **_kwargs: {PRIMARY_METRIC: 7.2, "accuracy": .75,
                                  "neg_precision": .6, "neg_recall": .3},
    )
    pooled = collect_pooled(config, per_fold)
    row = pooled.iloc[0]
    assert row.accuracy == .75
    assert np.isclose(row.accuracy_fold_mean, .7)
    assert np.isclose(row.accuracy_fold_std, np.sqrt(.02))
    assert np.isclose(row.neg_f1, .4)
    assert row.custom_diagnostic_fold_n == 2
    write_summary(config, pooled, tmp_path / "summary.md", per_fold)
    report = (tmp_path / "summary.md").read_text()
    assert "`custom_diagnostic`" in report
    assert "`accuracy` | 0.75" in report
    assert "0.7 ± 0.141421 (n=2)" in report
    assert "not an unbiased final test estimate" in report


def test_parameter_diagnostics_and_missing_neg_f1(tmp_path):
    from run_scripts.double_difficulty.perception_ablation_report import training_diagnostics, neg_f1

    pd.DataFrame({"alpha_first_1": [-2, 4], "beta_first_1": [1, 3]}).to_csv(
        tmp_path / "players.csv", index=False
    )
    summary = json.loads('{"finite_losses": true, "steps": 10000}')
    diagnostics = training_diagnostics(summary, tmp_path)
    assert diagnostics["fitted_alpha_first_mean"] == 1
    assert diagnostics["fitted_alpha_first_negative_fraction"] == .5
    assert diagnostics["train_finite_losses"] == 1
    assert np.isnan(neg_f1({"neg_precision": np.nan, "neg_recall": np.nan}))
    assert neg_f1({"neg_precision": 0, "neg_recall": 0}) == 0


def test_budget_comparison_matches_dimensions_and_folds(tmp_path):
    from run_scripts.double_difficulty.perception_ablation_report import write_budget_comparison

    configs = []
    for steps, shift in [(3000, 0.0), (10000, -.5)]:
        config = replace(configuration(tmp_path), root=str(tmp_path / str(steps)),
                         models=["perceived-logit"], dimensions=[1], folds=[0, 1], steps=steps)
        configs.append(config)
        output = Path(config.root) / "aggregate"
        output.mkdir(parents=True)
        pd.DataFrame([{"model": "perceived-logit", "dimensions": 1,
                       "selected_dimension": True, "complete_folds": 2,
                       "required_folds": 2, PRIMARY_METRIC: 7 + shift}]).to_csv(
            output / "pooled.csv", index=False
        )
        pd.DataFrame([{"model": "perceived-logit", "dimensions": 1, "fold": fold,
                       "complete": True, PRIMARY_METRIC: 6 + fold * 2 + shift}
                      for fold in [1, 0]]).to_csv(output / "per_fold.csv", index=False)
    path = tmp_path / "comparison.md"
    write_budget_comparison(configs, path)
    report = path.read_text()
    assert "7 | 6.5 | -0.5" in report
    assert "-0.5 ± 0 | 2/2" in report

    import pytest
    with pytest.raises(ValueError, match="matching non-budget settings"):
        write_budget_comparison([configs[0], replace(configs[1], optimization_seed=43)], path)
