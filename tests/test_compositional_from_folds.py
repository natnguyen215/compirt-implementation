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
from compirt_eval.scenario_b_bonuses import folds as bonus_folds
from run_scripts.common import run_compositional_from_folds as runner
from compirt_eval.scenario_b_bonuses.folds import audit_predictions


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


@pytest.mark.parametrize("use_synergy,calibration,prior,synergy_form,bonus_difficulty,bonus_aggregation", [
    (*settings, "lse") for settings in [
    (False, False, "normal", "dot", "scalar"), (True, False, "gamma", "dot", "scalar"),
    (True, True, "gamma", "dot", "scalar"), (True, False, "normal", "phi-psi", "scalar"),
    (True, True, "gamma", "phi-psi", "scalar"),
    (False, False, "gamma", "dot", "multidim"),
    (True, False, "gamma", "dot", "multidim"),
    (True, True, "gamma", "phi-psi", "multidim"),
]] + [(False, False, "gamma", "dot", "scalar", "noisy-or"),
      (False, False, "gamma", "dot", "scalar", "max"),
      (True, False, "gamma", "dot", "scalar", "max"),
      (True, False, "gamma", "dot", "multidim", "max")])
@pytest.mark.parametrize("synergy_link", ["additive", "multiplicative"])
def test_bonus_train_save_replay_and_evaluate(tmp_path, monkeypatch, capsys, use_synergy, calibration, prior, synergy_form, bonus_difficulty, bonus_aggregation, synergy_link):
    if not use_synergy and synergy_link == "multiplicative":
        pytest.skip("Multiplicative synergy requires synergy profiles")
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
    pd.DataFrame({"player_id": ["p1", "p2"], "theta_1": [0.2, 0.8],
                  "theta_2": [1.2, -.5]}).to_csv(
        pyramidal / "players.csv", index=False)
    training = tmp_path / "fitted_bonus"
    args = SimpleNamespace(
        output_dir=training, player_skills=pyramidal / "players.csv",
        data_dir=tmp_path, split="all", tournament=None, device="cpu", seed=42,
        steps=3, lr=0.01, use_synergy=use_synergy, synergy_dimensions=2,
        synergy_form=synergy_form,
        synergy_link=synergy_link,
        bonus_difficulty=bonus_difficulty,
        bonus_aggregation=bonus_aggregation,
        save_synergy_details=False, calibrate_correctness=calibration, alpha_prior=prior,
        posterior_draws=0,
    )
    train_compositional.run_experiment(args)
    progress = capsys.readouterr().out
    assert "Step 1/3" in progress and "Step 3/3" in progress
    assert json.loads((training / "summary.json").read_text())["synergy_form"] == synergy_form
    assert json.loads((training / "summary.json").read_text())["synergy_link"] == synergy_link
    assert json.loads((training / "summary.json").read_text())["bonus_difficulty"] == bonus_difficulty
    assert (training / "tau.txt").exists() == (bonus_aggregation == "lse")
    if bonus_aggregation == "lse":
        summary_path = training / "summary.json"
        legacy_summary = json.loads(summary_path.read_text())
        del legacy_summary["bonus_aggregation"]
        summary_path.write_text(json.dumps(legacy_summary))
    parameters = pd.read_csv(training / "bonus_parts.csv")
    if bonus_difficulty == "multidim":
        assert {"r_1", "r_2", "beta_1", "beta_2"}.issubset(parameters.columns)
        assert (parameters[["r_1", "r_2"]] > 0).all().all()
    else:
        summary_path = training / "summary.json"
        legacy_summary = json.loads(summary_path.read_text())
        del legacy_summary["bonus_difficulty"]
        summary_path.write_text(json.dumps(legacy_summary))
    if synergy_link == "additive":
        # Legacy fits have no link field; their replay must remain additive.
        summary_path = training / "summary.json"
        legacy_summary = json.loads(summary_path.read_text())
        del legacy_summary["synergy_link"]
        summary_path.write_text(json.dumps(legacy_summary))
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
    replay_summary = frozen_predict.frozen_predict_bonuses(replay_args)
    assert replay_summary["synergy_link"] == synergy_link
    assert replay_summary["bonus_difficulty"] == bonus_difficulty
    assert replay_summary["bonus_aggregation"] == bonus_aggregation
    fitted = pd.read_csv(training / "bonus_part_predictions.csv")
    replay = pd.read_csv(replay_args.output_dir / "bonus_part_predictions.csv")
    columns = ["predicted_correct", "aggregate", "synergy_contribution"]
    np.testing.assert_allclose(fitted[columns], replay[columns], atol=1e-6)
    evaluation = tmp_path / "evaluation"
    metrics = evaluate_bonuses(replay_args.output_dir, evaluation, write_report=True)
    assert pd.read_csv(evaluation / "csvs/bonus_metrics.csv").iloc[0]["log_loss"] == pytest.approx(metrics["log_loss"])
    assert (evaluation / "experiment_report.md").exists()
    assert "Stage 1: Tossup Metrics" not in (evaluation / "experiment_report.md").read_text()
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
        if synergy_form == "phi-psi":
            profiles.drop(columns=["phi_1", "phi_2"]).to_csv(profile_path, index=False)
            with pytest.raises(ValueError, match="phi profiles disagree"):
                frozen_predict.frozen_predict_bonuses(replay_args)
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
    source = tmp_path / "source"
    source.mkdir()
    alias = tmp_path / "source_alias"
    alias.symlink_to(source, target_is_directory=True)
    config = {"root": str(tmp_path), "stage1_root": str(tmp_path / "source"),
              "folds": [2], "arms": ["synergy"],
              "sources": {"2": {"hash": "original", "path": str(alias)}}}
    manifest = tmp_path / "configuration.json"
    manifest.write_text(json.dumps(config))
    original = manifest.read_bytes()
    calls = []
    monkeypatch.setattr(runner, "source_fold", lambda root, fold: {"hash": "original", "path": str(source)})
    monkeypatch.setattr(runner, "run_arm", lambda config, fold, arm, **kw: calls.append((fold, arm, kw)))
    monkeypatch.setattr(runner, "aggregate", lambda config: calls.append("aggregate"))
    runner.main(["--root", str(tmp_path), "--evaluate-only"])
    assert calls == [(2, "synergy", {"only_stage": "evaluate"}), "aggregate"]
    assert manifest.read_bytes() == original
    monkeypatch.setattr(runner, "source_fold", lambda root, fold: {"hash": "changed"})
    with pytest.raises(ValueError, match="Source artifacts changed"):
        runner.main(["--root", str(tmp_path), "--evaluate-only"])


def test_standard_evaluator_supports_bonus_only(tmp_path, monkeypatch):
    import evaluate_compirt

    tables = {"selected_split": "test"}
    monkeypatch.setattr(evaluate_compirt, "load_hf_tables", lambda *args: tables)
    monkeypatch.setattr(evaluate_compirt, "filter_tournament", lambda data, tournament: data)
    def fail(*args, **kwargs):
        pytest.fail("Bonus-only evaluation must not load tossup predictions")
    monkeypatch.setattr(evaluate_compirt, "evaluate_tossups", fail)
    calls = []
    monkeypatch.setattr(evaluate_compirt, "evaluate_bonuses",
                        lambda results, output, **kwargs: calls.append((results, output, kwargs)))
    evaluate_compirt.main(["--compositional-results", str(tmp_path / "bonus"),
                           "--output-dir", str(tmp_path / "evaluation"), "--split", "test"])
    assert calls == [(tmp_path / "bonus", tmp_path / "evaluation", {"tables": tables, "write_report": True})]


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


@pytest.mark.parametrize("form,link,bonus_difficulty", [
    ("dot", "additive", "scalar"), ("dot", "multiplicative", "scalar"),
    ("phi-psi", "additive", "scalar"), ("phi-psi", "multiplicative", "scalar"),
    ("dot", "additive", "multidim"),
])
def test_report_refresh_uses_saved_settings_without_scoring(tmp_path, monkeypatch, form, link, bonus_difficulty):
    config = {"root": str(tmp_path), "stage1_root": str(tmp_path / "source"),
              "folds": [0], "arms": ["synergy"], "steps": 2000, "lr": .01,
              "seed": 42, "alpha_prior": "gamma", "synergy_form": form,
              "synergy_link": link, "synergy_dimensions": 3,
              "bonus_difficulty": bonus_difficulty}
    (tmp_path / "configuration.json").write_text(json.dumps(config))
    output = tmp_path / "aggregate"
    output.mkdir()
    pooled = [{"arm": "synergy", "folds": 1, "parts": 6, "responses": 2,
               "games": 1, "teams": 2, "auc": .8, "log_loss": .42}]
    (output / "pooled.json").write_text(json.dumps(pooled))
    pd.DataFrame(pooled).to_csv(output / "pooled.csv", index=False)
    saved = {p: p.read_bytes() for p in (tmp_path / "configuration.json",
                                        output / "pooled.json", output / "pooled.csv")}
    def fail(*args, **kwargs):
        pytest.fail("Markdown refresh must not fit, score, or load source data")
    monkeypatch.setattr(runner, "run_arm", fail)
    monkeypatch.setattr(runner, "aggregate", fail)
    monkeypatch.setattr(runner, "source_fold", fail)
    runner.main(["--root", str(tmp_path), "--report-only"])
    report = (output / "report.md").read_text()
    assert f"{form}, {link}, 3D" in report
    assert "3-dimensional" in report
    if bonus_difficulty == "multidim":
        assert "sum_k r_bk * (ts_k(R) - beta_bk)" in report
    assert ("eta * (1 + s(R))" if link == "multiplicative" else "eta + s(R)") in report
    assert "../fold_0/synergy-evaluation/experiment_report.md" in report
    assert all(path.read_bytes() == content for path, content in saved.items())


def test_fold_pooling_uses_predictions_before_team_errors(tmp_path, monkeypatch):
    config = {"root": str(tmp_path), "stage1_root": str(tmp_path / "source"),
              "folds": [0, 1], "arms": ["compositional"], "steps": 2,
              "lr": .01, "seed": 42, "alpha_prior": "gamma"}
    # The same team has equal, opposite bonus errors in its held-out folds.
    for fold, probability in enumerate((.1, 17 / 30)):
        root = tmp_path / f"fold_{fold}"
        train, test = root / "train/compositional", root / "holdout/compositional"
        train.mkdir(parents=True)
        test.mkdir(parents=True)
        predictions = pd.DataFrame({
            "observation_id": [f"r{fold}:{i}" for i in range(3)],
            "response_id": [f"r{fold}"] * 3, "team_id": ["team"] * 3,
            "game_id": [f"game{fold}"] * 3, "bonus_id": ["bonus"] * 3,
            "part_index": [0, 1, 2], "correct": [1, 0, 0],
            "predicted_correct": [probability] * 3,
        })
        predictions.to_csv(test / "bonus_part_predictions.csv", index=False)
        pd.DataFrame({"response_id": [f"r{fold}"], "team_id": ["team"],
                      "game_id": [f"game{fold}"], "total_points": [10],
                      "predicted_points": [30 * probability]}).to_csv(test / "team_predictions.csv", index=False)
        (train / "summary.json").write_text(json.dumps({
            "tau": 1., "final_loss": 1., "best_loss": 1.,
            "last_100_loss_slope": 0., "finite_losses": True,
        }))
        (root / "compositional_checks.json").write_text(json.dumps({"disjoint_games": True}))
        evaluation = root / "evaluation/csvs"
        evaluation.mkdir(parents=True)
        pd.DataFrame([{"ppb_mae": 7.}]).to_csv(evaluation / "bonus_metrics.csv", index=False)
    tables = {"bonuses": pd.DataFrame({"bonus_id": ["bonus"], "parts": [[
        {"difficulty": name} for name in ("easy", "medium", "hard")]]})}
    monkeypatch.setattr(bonus_folds, "evaluation_tables", lambda *args: tables)
    monkeypatch.setattr(bonus_folds, "write_bonus_outcomes", lambda *args: {})
    bonus_folds.aggregate(config)
    pooled = pd.read_csv(tmp_path / "aggregate/pooled.csv").iloc[0]
    assert pooled.ppb_mae == pytest.approx(0.)
    assert pooled.parts == 6 and pooled.responses == 2 and pooled.teams == 1
    assert pooled.part_count_easy == 2
    assert "No synergy" in (tmp_path / "aggregate/report.md").read_text()


def test_fold_training_streams_progress_and_preserves_stage_log(tmp_path, monkeypatch, capsys):
    import sys

    output = tmp_path / "fold_0/train/synergy"
    command = [sys.executable, "-u", "-c",
               "import os; print('Step 1/3  ELBO loss: 10.0'); "
               "print('Step 3/3  ELBO loss: 8.0'); "
               "assert os.environ['OMP_NUM_THREADS'] == '1'"]
    monkeypatch.setattr(runner, "commands", lambda *args: [("train", output, command)])
    runner.run_arm({"root": str(tmp_path), "steps": 3}, 0, "synergy", only_stage="train")
    console = capsys.readouterr().out
    assert "Fold 0 | synergy | train (3 steps)" in console
    assert "Step 3/3" in console
    assert "import os" not in console  # Commands belong in the saved manifest.
    assert "Step 3/3" in (output / "run.log").read_text()
    assert json.loads((tmp_path / "fold_0/synergy_train_commands.json").read_text()) == [command]
    (output / "summary.json").write_text("{}")
    original = (output / "run.log").read_bytes()
    runner.run_arm({"root": str(tmp_path), "steps": 3}, 0, "synergy", only_stage="train")
    assert "already complete, skipping" in capsys.readouterr().out
    assert (output / "run.log").read_bytes() == original


@pytest.mark.parametrize("save_log", [False, True])
@pytest.mark.parametrize("return_code", [0, 7])
def test_shared_logger_streams_before_child_exits(tmp_path, monkeypatch, save_log, return_code):
    import io
    import os
    import subprocess
    import sys
    from utils.run_logging import run_logged

    gate = tmp_path / "output_seen"

    class Console(io.StringIO):
        def write(self, text):
            result = super().write(text)
            if "first step" in self.getvalue():
                gate.touch()
            return result

    console = Console()
    monkeypatch.setattr(sys, "stdout", console)
    script = (
        "import os, sys, time\n"
        "from pathlib import Path\n"
        "assert os.environ['COMPIRT_LOG_TEST'] == 'forwarded'\n"
        "print('first step', flush=True)\n"
        "deadline = time.monotonic() + 5\n"
        "while not Path('output_seen').exists() and time.monotonic() < deadline:\n"
        "    time.sleep(0.01)\n"
        "assert Path('output_seen').exists(), 'output was buffered until exit'\n"
        "print('last step: θ', file=sys.stderr, flush=True)\n"
        f"sys.exit({return_code})\n"
    )
    log = tmp_path / "logs/run.log" if save_log else None
    kwargs = dict(cwd=tmp_path, env={**os.environ, "COMPIRT_LOG_TEST": "forwarded"}, log_path=log)
    command = [sys.executable, "-u", "-c", script]
    if return_code:
        with pytest.raises(subprocess.CalledProcessError) as error:
            run_logged(command, **kwargs)
        assert error.value.returncode == return_code
    else:
        run_logged(command, **kwargs)
    assert console.getvalue() == "first step\nlast step: θ\n"
    if log:
        assert log.read_text() == console.getvalue()
