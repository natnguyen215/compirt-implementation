"""Contracts for the fixed double-Bernstein 3-3-2 holdout runner."""

from pathlib import Path

from run_scripts.bernstein.run_dd_bernstein_332 import Configuration, experiment_commands


def test_selected_run_passes_incorrect_weight_to_training():
    config = Configuration(
        root="/tmp/dd-bernstein-332-incorrect3",
        base_split="year_2024",
        folds=[0],
        split_seed=42,
        optimization_seed=42,
        degree=3,
        dimensions=3,
        drop_concentration=2.0,
        relevance_prior="simplex",
        learned_curve_locations=True,
        terminal_intercepts=True,
        steps=3000,
        lr=0.005,
        device="cpu",
        posterior_draws=0,
        incorrect_weight=3.0,
        player_neg_propensity=True,
        data_dir=None,
    )
    run_dir, stages = experiment_commands(config, 0)
    train = stages[0][2]

    assert run_dir == Path(config.root) / "fold_0"
    assert train[train.index("--incorrect-weight") + 1] == "3.0"
    assert "--player-neg-propensity" in train
    assert train[train.index("--relevance-prior") + 1] == "simplex"
    assert "--learn-curve-locations" in train
    assert "--no-terminal-intercepts" not in train
