"""Leakage and frozen-skill contracts for the compositional fold runner."""

import json
from types import SimpleNamespace

import numpy as np
import pandas as pd
import pytest

import train_compositional
from holdout import frozen_predict
from compirt_eval.common.reports import experiment_report_markdown
from compirt_eval.scenario_b_bonuses.evaluation import evaluate_bonuses
from run_scripts.common import run_compositional_from_folds as runner
from run_scripts.common.run_compositional_from_folds import audit_predictions


def parts(game, response):
    return pd.DataFrame({
        "game_id": [game] * 3, "response_id": [response] * 3,
        "observation_id": [f"{response}:{i}" for i in range(3)],
        "predicted_correct": [0.2, 0.5, 0.8],
    })


def test_audit_rejects_leakage_from_either_training_stage():
    train, test = parts("train", "r1"), parts("test", "r2")
    assert audit_predictions(train, test, {"train"})["test_parts"] == 3
    with pytest.raises(ValueError, match="overlap"):
        audit_predictions(train, test, {"train", "test"})
    with pytest.raises(ValueError, match="overlap"):
        audit_predictions(train, parts("train", "r2"), {"train"})
    with pytest.raises(ValueError, match="absent"):
        audit_predictions(train, test, {"different"})


def test_audit_rejects_invalid_or_partial_predictions():
    train, test = parts("train", "r1"), parts("test", "r2")
    with pytest.raises(ValueError, match="complete"):
        audit_predictions(train, test.iloc[:2], {"train"})
    test.loc[0, "predicted_correct"] = float("nan")
    with pytest.raises(ValueError, match="probabilities"):
        audit_predictions(train, test, {"train"})


@pytest.mark.parametrize("use_synergy,calibration,prior", [
    (False, False, "normal"), (True, False, "gamma"), (True, True, "gamma"),
])
def test_bonus_train_save_replay_and_evaluate(tmp_path, monkeypatch, use_synergy, calibration, prior):
    observations = pd.DataFrame([
        {"observation_id": f"{response}:{part}", "response_id": response,
         "game_id": "game", "team_id": response, "bonus_part_id": f"part-{part}",
         "part_index": part, "correct": int(part != 1), "total_points": 20,
         "player_ids": roster}
        for response, roster in (("r1", ["p1", "p2"]), ("r2", ["p2"]))
        for part in range(3)
    ])
    for module in (train_compositional, frozen_predict):
        monkeypatch.setattr(module, "load_hf_tables", lambda *args: {})
        monkeypatch.setattr(module, "filter_tournament", lambda tables, tournament: tables)
        monkeypatch.setattr(module, "build_bonus_part_observations", lambda tables: observations.copy())
    pyramidal = tmp_path / "pyramidal"
    pyramidal.mkdir()
    pd.DataFrame({"player_id": ["p1", "p2"], "theta_1": [0.2, 0.8]}).to_csv(
        pyramidal / "players.csv", index=False)
    training = tmp_path / "fitted_bonus"
    args = SimpleNamespace(
        output_dir=training, player_skills=pyramidal / "players.csv",
        data_dir=tmp_path, split="all", tournament=None, device="cpu", seed=42,
        steps=3, lr=0.01, use_synergy=use_synergy, synergy_dimensions=2,
        save_synergy_details=False, calibrate_correctness=calibration, alpha_prior=prior,
        posterior_draws=0,
    )
    train_compositional.run_experiment(args)
    assert (training / "player_synergy_profiles.csv").exists() == use_synergy
    assert not (training / "pairwise_synergy_scores.csv").exists()
    # Saved rows must align by ID, independently of their CSV order.
    for name in ("bonus_parts.csv", "player_synergy_profiles.csv"):
        path = training / name
        if path.exists():
            pd.read_csv(path).iloc[::-1].to_csv(path, index=False)
    replay_args = SimpleNamespace(
        **{key: getattr(args, key) for key in (
            "data_dir", "split", "tournament", "device", "use_synergy", "calibrate_correctness")},
        train_pyramidal=pyramidal, train_compositional=training,
        output_dir=tmp_path / "custom_replay", on_missing="error",
    )
    frozen_predict.frozen_predict_bonuses(replay_args)
    fitted = pd.read_csv(training / "bonus_part_predictions.csv")
    replay = pd.read_csv(replay_args.output_dir / "bonus_part_predictions.csv")
    columns = ["predicted_correct", "aggregate", "synergy_contribution"]
    np.testing.assert_allclose(fitted[columns], replay[columns], atol=1e-6)
    evaluation = tmp_path / "evaluation"
    evaluate_bonuses(replay_args.output_dir, evaluation)
    assert (evaluation / "graphs/parameters/bonus_part_parameter_distributions.png").exists()
    assert (evaluation / "graphs/parameters/synergy_parameter_distributions.png").exists() == use_synergy
    assert (evaluation / "graphs/bonus/bonus_prediction_distributions.png").exists()
    counts = pd.read_csv(evaluation / "csvs/bonus_prediction_distribution_summary.csv").set_index("parameter")
    assert counts.loc["aggregate", "observations"] == 6
    assert counts.loc["synergy_contribution", "observations"] == 2
    if use_synergy:
        replay_args.use_synergy = False
        with pytest.raises(ValueError, match="disagrees"):
            frozen_predict.frozen_predict_bonuses(replay_args)
        replay_args.use_synergy = True
        profile_path = training / "player_synergy_profiles.csv"
        profiles = pd.read_csv(profile_path)
        profiles[profiles.player_id != "p1"].to_csv(profile_path, index=False)
        with pytest.raises(ValueError, match="Missing fitted synergy profiles"):
            frozen_predict.frozen_predict_bonuses(replay_args)
        profiles.to_csv(profile_path, index=False)
    if calibration:
        replay_args.calibrate_correctness = False
        with pytest.raises(ValueError, match="disagrees"):
            frozen_predict.frozen_predict_bonuses(replay_args)
        replay_args.calibrate_correctness = True
    observations.at[0, "player_ids"] = ["unknown"]
    with pytest.raises(ValueError, match="uncovered rosters"):
        frozen_predict.frozen_predict_bonuses(replay_args)
    replay_args.on_missing = "drop"
    summary = frozen_predict.frozen_predict_bonuses(replay_args)
    assert summary["dropped_responses_unknown_roster"] == 1
    assert summary["bonus_part_observations"] == 3


def test_evaluate_only_uses_saved_config_without_training(tmp_path, monkeypatch):
    config = {"root": str(tmp_path), "stage1_root": str(tmp_path / "source"),
              "folds": [2], "arms": ["synergy"], "sources": {"2": {"hash": "original"}}}
    manifest = tmp_path / "configuration.json"
    manifest.write_text(json.dumps(config))
    original = manifest.read_bytes()
    calls = []
    monkeypatch.setattr(runner, "source_fold", lambda root, fold: {"hash": "original"})
    monkeypatch.setattr(runner, "run_arm", lambda config, fold, arm, **kw: calls.append((fold, arm, kw)))
    monkeypatch.setattr(runner, "aggregate", lambda config: calls.append("aggregate"))
    runner.main(["--root", str(tmp_path), "--evaluate-only"])
    assert calls == [(2, "synergy", {"only_stage": "evaluate"}), "aggregate"]
    assert manifest.read_bytes() == original
    monkeypatch.setattr(runner, "source_fold", lambda root, fold: {"hash": "changed"})
    with pytest.raises(ValueError, match="Source artifacts changed"):
        runner.main(["--root", str(tmp_path), "--evaluate-only"])


def test_bonus_only_report_identifies_frozen_regime(tmp_path):
    stage = tmp_path / "holdout/compositional"
    stage.mkdir(parents=True)
    (stage / "summary.json").write_text(json.dumps({"frozen_predict": True}))
    csvs = tmp_path / "evaluation/csvs"
    csvs.mkdir(parents=True)
    pd.DataFrame({"scenario": ["bonus_part_correctness"], "stratum": ["category"],
                  "value": ["history"], "observations": [3], "auc": [0.8]}).to_csv(
        csvs / "bonus_prediction_diagnostics_by_stratum.csv", index=False)
    report = experiment_report_markdown(tmp_path / "evaluation", tossup=None, bonus={"auc": 0.8})
    assert "frozen matrix-infill holdout" in report
    assert "Stage 1: Tossup Metrics" not in report
    assert "history" in report
