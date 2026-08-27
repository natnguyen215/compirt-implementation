"""Pooled correctness metrics and Markdown reports for holdout experiments."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Iterable, Mapping

import numpy as np
import pandas as pd

from compirt_eval.common.metrics import classification_metrics
from compirt_eval.common.metrics import negative_class_metrics
from compirt_eval.scenario_a_tossups.timing import (
    _first_buzzer_row,
    _full_pmf_score_row,
    _load_timing_evaluation_inputs,
    event_first_buzz_components,
)


REPORTED_CORRECTNESS_METRICS = ("accuracy", "auc", "log_loss")
MAIN_TABLE_METRICS = (
    ("accuracy", "Accuracy"),
    ("neg_f1", "Neg F1"),
    ("accuracy_lift_over_all_correct", "Lift over all-correct"),
    ("joint_tossup_event_log_loss", "Joint event LL"),
    ("log_loss", "Correctness LL"),
    ("auc", "AUC"),
    ("ece", "ECE"),
    ("buzz_position_mae", "Position MAE"),
    ("first_buzzer_top1_accuracy", "First-buzzer top-1"),
    ("no_buzz_calibration_error", "No-buzz error"),
    ("full_pmf_final_decile_mass", "Predicted final-decile mass"),
)


def _buzz_predictions(paths: Iterable[Path]) -> tuple[np.ndarray, np.ndarray]:
    """Load only observed buzz outcomes from saved tossup prediction CSVs."""
    outcomes: list[np.ndarray] = []
    probabilities: list[np.ndarray] = []
    for path in paths:
        if not path.exists():
            continue
        for chunk in pd.read_csv(
            path,
            usecols=["y", "z", "predicted_correct"],
            chunksize=250_000,
        ):
            buzz = chunk[chunk["z"] == "BUZZ"]
            if buzz.empty:
                continue
            outcomes.append(buzz["y"].to_numpy(dtype=float))
            probabilities.append(buzz["predicted_correct"].to_numpy(dtype=float))
    if not outcomes:
        return np.array([], dtype=float), np.array([], dtype=float)
    return np.concatenate(outcomes), np.concatenate(probabilities)


def pooled_correctness_metrics(
    run_dirs: Iterable[Path], *, split: str
) -> dict[str, float | int]:
    """Pool correctness predictions across folds for ``train`` or ``holdout``."""
    if split not in {"train", "holdout"}:
        raise ValueError("split must be 'train' or 'holdout'")
    paths = [
        Path(run_dir) / split / "pyramidal" / "tossup_predictions.csv"
        for run_dir in run_dirs
    ]
    outcomes, probabilities = _buzz_predictions(paths)
    metrics = classification_metrics(outcomes, probabilities)
    return {
        **{name: float(metrics[name]) for name in REPORTED_CORRECTNESS_METRICS},
        "observations": int(len(outcomes)),
    }


def add_in_sample_correctness_metrics(
    result: dict[str, object], run_dirs: Iterable[Path]
) -> None:
    """Add consistently prefixed pooled training metrics to an aggregate row."""
    metrics = pooled_correctness_metrics(run_dirs, split="train")
    result.update({f"in_sample_{key}": value for key, value in metrics.items()})


def add_main_table_fold_means(
    result: dict[str, object], run_dirs: Iterable[Path]
) -> None:
    """Add held-out fold means using the Research Log main-table convention."""
    rows = []
    for run_dir in run_dirs:
        candidates = (
            Path(run_dir) / "evaluation" / "csvs" / "tossup_metrics.csv",
            Path(run_dir)
            / "holdout"
            / "evaluation"
            / "csvs"
            / "tossup_metrics.csv",
        )
        path = next((candidate for candidate in candidates if candidate.exists()), None)
        if path is None:
            continue
        frame = pd.read_csv(path)
        if not frame.empty:
            rows.append(frame.iloc[0])
    if not rows:
        return
    frame = pd.DataFrame(rows)
    if {"neg_precision", "neg_recall"}.issubset(frame.columns):
        denominator = frame["neg_precision"] + frame["neg_recall"]
        frame["neg_f1"] = np.where(
            denominator > 0,
            2 * frame["neg_precision"] * frame["neg_recall"] / denominator,
            0.0,
        )
    else:
        frame["neg_f1"] = np.nan
    for name, _label in MAIN_TABLE_METRICS:
        values = frame[name] if name in frame else pd.Series(dtype=float)
        result[f"main_table_{name}"] = float(
            pd.to_numeric(values, errors="coerce").mean()
        )
    result["main_table_folds"] = int(len(frame))


def _neg_f1(metrics: Mapping[str, object]) -> float:
    precision = float(metrics.get("neg_precision", np.nan))
    recall = float(metrics.get("neg_recall", np.nan))
    denominator = precision + recall
    return 2 * precision * recall / denominator if denominator > 0 else 0.0


def _training_main_table_metrics(run_dir: Path) -> dict[str, float]:
    """Compute one training fold's Research Log metrics, caching the result."""
    results_dir = Path(run_dir) / "train" / "pyramidal"
    cache_path = results_dir / "in_sample_main_table_metrics.json"
    source_paths = [
        results_dir / name
        for name in (
            "players.csv",
            "tossups.csv",
            "tossup_predictions.csv",
            "buzz_event_predictions.csv",
        )
    ]
    signature = {
        path.name: [path.stat().st_size, path.stat().st_mtime_ns]
        for path in source_paths
        if path.exists()
    }
    if cache_path.exists():
        cached = json.loads(cache_path.read_text(encoding="utf-8"))
        if cached.get("source_signature") == signature:
            return cached["metrics"]

    inputs = _load_timing_evaluation_inputs(results_dir)
    if inputs is None:
        return {}
    predictions = inputs.predictions
    buzz = predictions[predictions["z"] == "BUZZ"]
    metrics = classification_metrics(buzz["y"], buzz["predicted_correct"])
    metrics.update(negative_class_metrics(buzz["y"], buzz["predicted_correct"]))
    metrics["neg_f1"] = _neg_f1(metrics)

    identity_rows = []
    pmf_rows = []
    reconstruction_cache: dict[object, object] = {}
    for event_id, event in predictions.groupby("event_id", sort=False):
        tossup_id = str(event["tossup_id"].iloc[0])
        if tossup_id not in inputs.tossups.index or not set(
            event["player_id"]
        ).issubset(inputs.players.index):
            continue
        components = event_first_buzz_components(
            event,
            inputs.players,
            inputs.tossups,
            inputs.adjustments,
            inputs.link,
            inputs.buzz_parameter_prefix,
            inputs.difficulty_scale,
            inputs.terminal_intercepts,
            reconstruction_cache=reconstruction_cache,
        )
        observed_buzz = event[event["z"] == "BUZZ"]
        identity, _missing = _first_buzzer_row(
            event_id, event, tossup_id, observed_buzz, components
        )
        if identity is not None:
            identity_rows.append(identity)
        pmf = _full_pmf_score_row(event_id, event, components)
        if pmf is not None:
            pmf_rows.append(pmf)

    if identity_rows:
        identities = pd.DataFrame(identity_rows)
        metrics["first_buzzer_top1_accuracy"] = float(
            (identities["actual_player_rank"] == 1).mean()
        )
    if pmf_rows:
        pmfs = pd.DataFrame(pmf_rows)
        metrics["joint_tossup_event_log_loss"] = float(
            pmfs["joint_event_log_loss"].mean()
        )
        metrics["no_buzz_calibration_error"] = float(
            (pmfs["predicted_no_buzz"] - pmfs["observed_no_buzz"]).mean()
        )
        metrics["full_pmf_final_decile_mass"] = float(
            pmfs["final_decile_mass"].mean()
        )
    position_path = results_dir / "buzz_event_predictions.csv"
    if position_path.exists():
        positions = pd.read_csv(position_path)
        error = (
            positions["predicted_relative_position"]
            - positions["observed_relative_position"]
        )
        metrics["buzz_position_mae"] = float(error.abs().mean())

    selected = {
        name: float(metrics.get(name, np.nan)) for name, _label in MAIN_TABLE_METRICS
    }
    cache_path.write_text(
        json.dumps({"source_signature": signature, "metrics": selected}, indent=2)
        + "\n",
        encoding="utf-8",
    )
    return selected


def add_in_sample_main_table_fold_means(
    result: dict[str, object], run_dirs: Iterable[Path]
) -> None:
    """Add mean training-fold values for every Research Log main-table metric."""
    rows = [_training_main_table_metrics(Path(run_dir)) for run_dir in run_dirs]
    rows = [row for row in rows if row]
    if not rows:
        return
    frame = pd.DataFrame(rows)
    for name, _label in MAIN_TABLE_METRICS:
        result[f"in_sample_main_table_{name}"] = float(
            pd.to_numeric(frame[name], errors="coerce").mean()
        )
    result["in_sample_main_table_folds"] = int(len(frame))


def _show(value: object) -> str:
    if value is None or pd.isna(value):
        return ""
    return f"{float(value):.6f}"


def correctness_markdown(
    metrics: Mapping[str, object], *, title: str = "Holdout correctness summary"
) -> str:
    """Render pooled in-sample and held-out correctness metrics as Markdown."""
    lines = [
        f"# {title}",
        "",
        "These are pooled correctness metrics for rows with an observed buzz. "
        "In-sample rows come from each fold's training fit; the same underlying "
        "observation can therefore appear in multiple cross-validation fits.",
        "",
        "| metric | in-sample | held-out | generalization gap |",
        "| --- | ---: | ---: | ---: |",
    ]
    for name in REPORTED_CORRECTNESS_METRICS:
        train = metrics.get(f"in_sample_{name}")
        held_out = metrics.get(name)
        gap = None
        if train is not None and held_out is not None:
            gap = (
                float(held_out) - float(train)
                if name == "log_loss"
                else float(train) - float(held_out)
            )
        lines.append(
            f"| {name.replace('_', ' ')} | {_show(train)} | "
            f"{_show(held_out)} | {_show(gap)} |"
        )
    lines += [
        "",
        "For all three rows, a positive generalization gap means held-out "
        "performance is worse.",
        "",
        "| sample | observed buzzes |",
        "| --- | ---: |",
        f"| in-sample | {metrics.get('in_sample_observations', '')} |",
        f"| held-out | {metrics.get('observations', '')} |",
        "",
        "## Research Log main-table metrics",
        "",
        "Both samples use unweighted means of their fold-level metrics, matching "
        "the convention used by the Research Log main table.",
        "",
        "| metric | in-sample fold mean | held-out fold mean |",
        "| --- | ---: | ---: |",
    ]
    for name, label in MAIN_TABLE_METRICS:
        lines.append(
            f"| {label} | "
            f"{_show(metrics.get(f'in_sample_main_table_{name}'))} | "
            f"{_show(metrics.get(f'main_table_{name}'))} |"
        )
    lines += [
        "",
        f"Training folds included: {metrics.get('in_sample_main_table_folds', '')}. "
        f"Held-out folds included: {metrics.get('main_table_folds', '')}.",
    ]
    return "\n".join(lines).rstrip() + "\n"


def write_correctness_markdown(
    metrics: Mapping[str, object], output_path: Path, *, title: str
) -> Path:
    """Write the human-readable pooled train/holdout correctness report."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(correctness_markdown(metrics, title=title), encoding="utf-8")
    return output_path


def discover_experiment_roots(root: Path) -> list[Path]:
    """Find directories whose immediate ``fold_*`` children contain predictions."""
    parents = {
        path.parents[3]
        for path in root.glob("**/fold_*/train/pyramidal/tossup_predictions.csv")
    }
    return sorted(parents)


def backfill_markdown(root: Path) -> int:
    """Create correctness Markdown reports for all completed experiments below root."""
    written = 0
    for experiment_root in discover_experiment_roots(root):
        run_dirs = sorted(
            path
            for path in experiment_root.glob("fold_*")
            if (path / "train" / "pyramidal" / "tossup_predictions.csv").exists()
            and (path / "holdout" / "pyramidal" / "tossup_predictions.csv").exists()
        )
        if not run_dirs:
            continue
        aggregate: dict[str, object] = pooled_correctness_metrics(
            run_dirs, split="holdout"
        )
        add_in_sample_correctness_metrics(aggregate, run_dirs)
        add_in_sample_main_table_fold_means(aggregate, run_dirs)
        add_main_table_fold_means(aggregate, run_dirs)
        write_correctness_markdown(
            aggregate,
            experiment_root / "aggregate" / "correctness_metrics.md",
            title=f"{experiment_root.name} correctness summary",
        )
        written += 1
    write_overview_from_reports(root)
    return written


def write_overview_from_reports(root: Path) -> Path:
    """Build one all-model Markdown table from per-experiment reports."""
    rows: list[dict[str, str]] = []
    row_pattern = re.compile(
        r"^\| (accuracy|auc|log loss) \| ([^|]*) \| ([^|]*) \| ([^|]*) \|$"
    )
    main_pattern = re.compile(r"^\| ([^|]+) \| ([^|]*) \| ([^|]*) \|$")
    label_to_key = {label: name for name, label in MAIN_TABLE_METRICS}
    for report_path in sorted(root.glob("**/aggregate/correctness_metrics.md")):
        experiment_root = report_path.parent.parent
        values: dict[str, str] = {
            "model": str(experiment_root.relative_to(root)),
        }
        for line in report_path.read_text(encoding="utf-8").splitlines():
            match = row_pattern.match(line)
            if not match:
                continue
            metric = match.group(1).replace(" ", "_")
            values[f"train_{metric}"] = match.group(2).strip()
            values[f"holdout_{metric}"] = match.group(3).strip()
        for line in report_path.read_text(encoding="utf-8").splitlines():
            match = main_pattern.match(line)
            if match and match.group(1).strip() in label_to_key:
                key = label_to_key[match.group(1).strip()]
                values[f"main_train_{key}"] = match.group(2).strip()
                values[f"main_holdout_{key}"] = match.group(3).strip()
        if all(
            key in values
            for key in (
                "train_accuracy",
                "train_auc",
                "train_log_loss",
                "holdout_accuracy",
                "holdout_auc",
                "holdout_log_loss",
                *(f"main_train_{name}" for name, _label in MAIN_TABLE_METRICS),
                *(f"main_holdout_{name}" for name, _label in MAIN_TABLE_METRICS),
            )
        ):
            rows.append(values)

    lines = [
        "# Research Log models: in-sample versus held-out metrics",
        "",
        "Both samples use unweighted fold means, matching the Research Log main "
        "table. Each model has one fitted-training row and one frozen-held-out row.",
        "",
        "| model | sample | accuracy | Neg F1 | lift | joint event LL | "
        "correctness LL | AUC | ECE | "
        "position MAE | first-buzzer top-1 | no-buzz error | final-decile mass |",
        "| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | "
        "---: | ---: | ---: | ---: |",
    ]
    for row in rows:
        for sample, prefix in (
            ("in-sample", "main_train"),
            ("held-out", "main_holdout"),
        ):
            lines.append(
                f"| `{row['model']}` | {sample} | {row[f'{prefix}_accuracy']} | "
                f"{row[f'{prefix}_neg_f1']} | "
                f"{row[f'{prefix}_accuracy_lift_over_all_correct']} | "
                f"{row[f'{prefix}_joint_tossup_event_log_loss']} | "
                f"{row[f'{prefix}_log_loss']} | {row[f'{prefix}_auc']} | "
                f"{row[f'{prefix}_ece']} | {row[f'{prefix}_buzz_position_mae']} | "
                f"{row[f'{prefix}_first_buzzer_top1_accuracy']} | "
                f"{row[f'{prefix}_no_buzz_calibration_error']} | "
                f"{row[f'{prefix}_full_pmf_final_decile_mass']} |"
            )
    output_path = root / "aggregate_correctness_metrics.md"
    output_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return output_path


def main(argv=None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, nargs="?")
    parser.add_argument(
        "--training-fold",
        type=Path,
        help="compute/cache the in-sample main-table metrics for one fold",
    )
    parser.add_argument(
        "--overview-only",
        action="store_true",
        help="rebuild only the all-model index from existing Markdown reports",
    )
    args = parser.parse_args(argv)
    if args.training_fold is not None:
        metrics = _training_main_table_metrics(args.training_fold)
        print(json.dumps(metrics, sort_keys=True))
        return
    if args.root is None:
        parser.error("root is required unless --training-fold is used")
    if args.overview_only:
        path = write_overview_from_reports(args.root)
        print(f"Wrote aggregate correctness overview to {path}")
        return
    count = backfill_markdown(args.root)
    print(f"Wrote {count} aggregate correctness Markdown reports under {args.root}")


if __name__ == "__main__":
    main()
