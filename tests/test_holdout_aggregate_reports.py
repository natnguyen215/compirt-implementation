"""Tests for pooled in-sample/holdout correctness reporting."""

from pathlib import Path

import pandas as pd
import pytest

from holdout.aggregate_reports import (
    MAIN_TABLE_METRICS,
    add_in_sample_correctness_metrics,
    add_in_sample_main_table_fold_means,
    add_main_table_fold_means,
    correctness_markdown,
    discover_experiment_roots,
    pooled_correctness_metrics,
    write_correctness_markdown,
    write_overview_from_reports,
)


def _write_predictions(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(path, index=False)


def test_pooled_correctness_uses_only_observed_buzzes(tmp_path: Path) -> None:
    run = tmp_path / "model" / "fold_0"
    rows = [
        {"y": 1.0, "z": "BUZZ", "predicted_correct": 0.9},
        {"y": 0.0, "z": "BUZZ", "predicted_correct": 0.2},
        {"y": None, "z": "CENSORED", "predicted_correct": 0.99},
    ]
    _write_predictions(run / "train/pyramidal/tossup_predictions.csv", rows)

    metrics = pooled_correctness_metrics([run], split="train")

    assert metrics["observations"] == 2
    assert metrics["accuracy"] == 1.0
    assert metrics["auc"] == 1.0
    # Exact expected value: mean(-log(.9), -log(.8)).
    assert metrics["log_loss"] == pytest.approx(0.164252033486018)


def test_markdown_compares_in_sample_and_held_out() -> None:
    metrics: dict[str, object] = {
        "accuracy": 0.7,
        "auc": 0.65,
        "log_loss": 0.62,
        "observations": 20,
    }
    metrics.update(
        in_sample_accuracy=0.8,
        in_sample_auc=0.75,
        in_sample_log_loss=0.5,
        in_sample_observations=80,
    )

    report = correctness_markdown(metrics, title="Example")

    assert "| accuracy | 0.800000 | 0.700000 | 0.100000 |" in report
    assert "| log loss | 0.500000 | 0.620000 | 0.120000 |" in report
    assert "| in-sample | 80 |" in report


def test_add_metrics_and_discover_experiment_root(tmp_path: Path) -> None:
    run = tmp_path / "family" / "model" / "fold_0"
    rows = [
        {"y": 1.0, "z": "BUZZ", "predicted_correct": 0.8},
        {"y": 0.0, "z": "BUZZ", "predicted_correct": 0.3},
    ]
    _write_predictions(run / "train/pyramidal/tossup_predictions.csv", rows)
    _write_predictions(run / "holdout/pyramidal/tossup_predictions.csv", rows)

    aggregate: dict[str, object] = {}
    add_in_sample_correctness_metrics(aggregate, [run])

    assert aggregate["in_sample_accuracy"] == 1.0
    assert discover_experiment_roots(tmp_path) == [run.parent]


def test_main_table_metrics_are_unweighted_fold_means(tmp_path: Path) -> None:
    runs = [tmp_path / f"model/fold_{fold}" for fold in range(2)]
    base = {
        name: 0.2 for name, _label in MAIN_TABLE_METRICS if name != "neg_f1"
    }
    for fold, run in enumerate(runs):
        row = {key: value + 0.2 * fold for key, value in base.items()}
        row.update(
            neg_precision=(0.25, 0.5)[fold],
            neg_recall=(1.0, 0.5)[fold],
        )
        path = run / "evaluation/csvs/tossup_metrics.csv"
        path.parent.mkdir(parents=True, exist_ok=True)
        pd.DataFrame([row]).to_csv(path, index=False)

    result: dict[str, object] = {}
    add_main_table_fold_means(result, runs)

    assert result["main_table_accuracy"] == pytest.approx(0.3)
    assert result["main_table_neg_f1"] == pytest.approx(0.45)
    assert result["main_table_folds"] == 2


def test_legacy_fold_metrics_leave_unavailable_values_blank(tmp_path: Path) -> None:
    run = tmp_path / "model/fold_0"
    path = run / "evaluation/csvs/tossup_metrics.csv"
    path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame([{"accuracy": 0.7}]).to_csv(path, index=False)

    result: dict[str, object] = {}
    add_main_table_fold_means(result, [run])

    assert result["main_table_accuracy"] == 0.7
    assert pd.isna(result["main_table_neg_f1"])
    assert pd.isna(result["main_table_joint_tossup_event_log_loss"])


def test_in_sample_main_table_metrics_are_fold_means(monkeypatch) -> None:
    calls = []

    def fake_metrics(run):
        calls.append(run)
        value = float(str(run).rsplit("_", 1)[-1])
        return {name: value for name, _label in MAIN_TABLE_METRICS}

    monkeypatch.setattr(
        "holdout.aggregate_reports._training_main_table_metrics", fake_metrics
    )
    result: dict[str, object] = {}

    add_in_sample_main_table_fold_means(
        result, [Path("fold_0"), Path("fold_1")]
    )

    assert result["in_sample_main_table_accuracy"] == 0.5
    assert result["in_sample_main_table_folds"] == 2
    assert calls == [Path("fold_0"), Path("fold_1")]


def test_overview_collects_all_model_markdown_reports(tmp_path: Path) -> None:
    metrics = {
        "accuracy": 0.7,
        "auc": 0.65,
        "log_loss": 0.62,
        "observations": 20,
        "in_sample_accuracy": 0.8,
        "in_sample_auc": 0.75,
        "in_sample_log_loss": 0.5,
        "in_sample_observations": 80,
    }
    metrics.update(
        {f"main_table_{name}": 0.25 for name, _label in MAIN_TABLE_METRICS}
    )
    metrics.update(
        {
            f"in_sample_main_table_{name}": 0.5
            for name, _label in MAIN_TABLE_METRICS
        }
    )
    metrics["main_table_folds"] = 5
    metrics["in_sample_main_table_folds"] = 5
    write_correctness_markdown(
        metrics,
        tmp_path / "family/model/aggregate/correctness_metrics.md",
        title="model correctness summary",
    )

    output = write_overview_from_reports(tmp_path)
    report = output.read_text(encoding="utf-8")

    assert "`family/model`" in report
    assert "| in-sample | 0.500000 | 0.500000 |" in report
    assert "| held-out | 0.250000 | 0.250000 |" in report
