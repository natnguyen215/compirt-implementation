"""Contracts for the pinned sigmoid/simplex/terminal holdout runner."""

from pathlib import Path

from run_scripts.multidimensional.multidim.run_dd_sigmoid_simplex_terminal import (
    Configuration,
    experiment_commands,
)


def test_commands_pin_sigmoid_simplex_terminal_model():
    config = Configuration(
        root="/tmp/dd-sigmoid-simplex-terminal",
        base_split="year_2024",
        folds=[0],
        split_seed=42,
        optimization_seed=42,
        dimensions=3,
        steps=3000,
        lr=0.005,
        device="cpu",
        posterior_draws=0,
        data_dir=None,
    )
    run_dir, stages = experiment_commands(config, 0)
    train = stages[0][2]
    frozen = stages[1][2]
    evaluate = stages[2][2]

    assert run_dir == Path(config.root) / "fold_0"
    assert "hazard_double_difficulty.multidim.train_pyramidal" in train
    assert train[train.index("--difficulty-link") + 1] == "sigmoid"
    assert train[train.index("--relevance-prior") + 1] == "simplex"
    assert "--terminal-intercepts" in train
    assert train[train.index("--dimensions") + 1] == "3"
    assert "game-holdout:year_2024:train:5:0:42" in train
    assert "holdout.frozen_predict" in frozen
    assert frozen[frozen.index("--difficulty-link") + 1] == "sigmoid"
    assert "game-holdout:year_2024:test:5:0:42" in frozen
    assert "run_scripts.paper_model_selection.evaluate_fold" in evaluate
