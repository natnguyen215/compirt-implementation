"""Readable one-file evaluation summaries for saved CompIRT artifacts."""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd
from pandas.errors import EmptyDataError

from compirt_eval.outputs import metrics_path


BONUS_METRICS = [
    "auc",
    "log_loss",
    "ece",
    "part_accuracy",
    "exact_acc",
    "per_bonus_points_mae",
    "ppb_mae",
]
TOSSUP_METRICS = [
    "auc",
    "log_loss",
    "ece",
    "accuracy",
    "buzz_position_mae",
    "buzz_position_median_absolute_error",
]


def load_metrics_row(evaluation_dir: Path, filename: str) -> dict[str, object]:
    """Load a single metrics CSV row from nested or legacy flat eval layout."""
    path = metrics_path(Path(evaluation_dir), filename)
    frame = _read_csv(path)
    if frame.empty:
        return {}
    return frame.iloc[0].to_dict()


def _metric_frame(row: dict[str, object], names: list[str]) -> pd.DataFrame:
    """Return a vertical metric table in requested order."""
    rows = []
    for name in names:
        if name in row:
            rows.append({"metric": name, "value": row[name]})
    for name, value in row.items():
        if name in names:
            continue
        if pd.notna(pd.to_numeric(value, errors="coerce")):
            rows.append({"metric": name, "value": value})
    return pd.DataFrame(rows)


def _read_csv(path: Path) -> pd.DataFrame:
    """Read a CSV when present, otherwise return an empty frame."""
    if not path.exists():
        return pd.DataFrame()
    try:
        return pd.read_csv(path)
    except EmptyDataError:
        return pd.DataFrame()


def _read_json(path: Path) -> dict[str, object]:
    """Read a JSON object when present."""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def stage_base_for_evaluation(evaluation_dir: Path) -> Path:
    """Return the directory containing pyramidal/compositional/synergy stages."""
    return Path(evaluation_dir).parent


def result_root_for_evaluation(evaluation_dir: Path) -> Path:
    """Return the result root whose run.log describes this eval folder."""
    evaluation_dir = Path(evaluation_dir)
    if evaluation_dir.parent.name == "holdout":
        return evaluation_dir.parent.parent
    return evaluation_dir.parent


def comparison_path_for_evaluation(evaluation_dir: Path) -> Path:
    """Return the sibling comparison CSV path for an evaluation folder."""
    return (
        stage_base_for_evaluation(evaluation_dir)
        / "comparison"
        / "bonus_model_comparison.csv"
    )


def bonus_stage_name(evaluation_dir: Path) -> str:
    """Return the bonus-stage directory used by this eval folder."""
    if Path(evaluation_dir).name == "synergy-evaluation":
        return "synergy"
    return "compositional"


def _display_tournament(value: object, evaluation_dir: Path) -> str:
    """Render an empty all-tournament selection in human terms when inferable."""
    if value not in (None, ""):
        return str(value)
    parts = {part.lower() for part in Path(evaluation_dir).parts}
    root_name = result_root_for_evaluation(evaluation_dir).name.lower()
    if "in_sample" in parts and ("all2024" in root_name or "all-2024" in root_name):
        return "all 2024"
    if "in_sample" in parts and "2024" in root_name:
        return "all 2024"
    return "all tournaments"


def _stage_dimensions(summary: dict[str, object]) -> object:
    """Return the single displayed dimensionality for a stage summary."""
    for field in ("dimensions", "topic_dimensions", "skill_dimensions"):
        value = summary.get(field)
        if value not in (None, ""):
            return value
    return None


def _stage_summary_rows(evaluation_dir: Path) -> pd.DataFrame:
    """Build a small table of run variables recoverable from stage summaries."""
    stage_base = stage_base_for_evaluation(evaluation_dir)
    paths = {
        "pyramidal": stage_base / "pyramidal" / "summary.json",
        bonus_stage_name(evaluation_dir): stage_base
        / bonus_stage_name(evaluation_dir)
        / "summary.json",
    }
    rows = []
    for stage, path in paths.items():
        summary = _read_json(path)
        if not summary:
            continue
        rows.append(
            {
                "stage": stage,
                "field": "tournament",
                "value": _display_tournament(summary.get("tournament"), evaluation_dir),
            }
        )
        dimensions = _stage_dimensions(summary)
        if dimensions is not None:
            rows.append({"stage": stage, "field": "dimensions", "value": dimensions})
        for field in (
            "steps",
            "final_loss",
            "calibrate_correctness",
            "predicted_buzz_positions",
            "synergy_dimensions",
            "topic_vectors",
        ):
            if field in summary:
                rows.append({"stage": stage, "field": field, "value": summary[field]})
    return pd.DataFrame(rows)


def _bonus_scalar_rows(evaluation_dir: Path) -> pd.DataFrame:
    """Return bonus-stage scalars that are useful but not run variables."""
    stage_base = stage_base_for_evaluation(evaluation_dir)
    summary = _read_json(stage_base / bonus_stage_name(evaluation_dir) / "summary.json")
    rows = []
    for field in (
        "tau",
        "mean_synergy_contribution",
        "median_synergy_contribution",
        "negative_synergy_fraction",
        "positive_synergy_fraction",
    ):
        if field in summary:
            rows.append({"field": field, "value": summary[field]})
    return pd.DataFrame(rows)


def _parameter_summary(path: Path) -> pd.DataFrame:
    """Return the saved parameter summary with display-friendly columns."""
    frame = _read_csv(path)
    if frame.empty:
        return frame
    preferred = [
        "group",
        "parameter",
        "observations",
        "mean",
        "standard_deviation",
        "minimum",
        "p05",
        "p25",
        "median",
        "p75",
        "p95",
        "maximum",
    ]
    columns = [column for column in preferred if column in frame.columns]
    columns.extend(column for column in frame.columns if column not in columns)
    return frame[columns]


def _comparison_frame(comparison_csv: Path | None) -> pd.DataFrame:
    """Load no-synergy versus synergy comparison metrics if available."""
    if comparison_csv is None or not Path(comparison_csv).exists():
        return pd.DataFrame()
    return pd.read_csv(comparison_csv)


def _append_table(
    lines: list[str],
    title: str,
    frame: pd.DataFrame,
    empty_text: str,
) -> None:
    """Append a Markdown table or an explicit missing-data note."""
    lines.extend([f"## {title}", ""])
    if frame.empty:
        lines.extend([empty_text, ""])
        return
    lines.extend([markdown_table(frame), ""])


def _format_cell(value: object) -> str:
    """Format one Markdown table cell without optional dependencies."""
    if isinstance(value, (list, tuple, dict)):
        return json.dumps(value, sort_keys=True).replace("|", "\\|")
    if pd.isna(value):
        return ""
    if isinstance(value, float):
        return f"{value:.6g}"
    return str(value).replace("|", "\\|").replace("\n", " ")


def markdown_table(frame: pd.DataFrame) -> str:
    """Render a simple GitHub-flavored Markdown table."""
    columns = [str(column) for column in frame.columns]
    rows = ["| " + " | ".join(columns) + " |"]
    rows.append("| " + " | ".join("---" for _ in columns) + " |")
    for _, row in frame.iterrows():
        rows.append(
            "| "
            + " | ".join(_format_cell(row[column]) for column in frame.columns)
            + " |"
        )
    return "\n".join(rows)


def write_eval_docs_summary(
    evaluation_dir: Path,
    comparison_csv: Path | None = None,
) -> Path:
    """Create 'docs/summary.md' for one evaluation or synergy-evaluation folder."""
    evaluation_dir = Path(evaluation_dir)
    if comparison_csv is None:
        candidate = comparison_path_for_evaluation(evaluation_dir)
        comparison_csv = candidate if candidate.exists() else None

    csv_dir = evaluation_dir / "csvs"
    docs_dir = evaluation_dir / "docs"
    docs_dir.mkdir(parents=True, exist_ok=True)
    output_path = docs_dir / "summary.md"

    bonus = _metric_frame(
        load_metrics_row(evaluation_dir, "bonus_metrics.csv"), BONUS_METRICS
    )
    tossup = _metric_frame(
        load_metrics_row(evaluation_dir, "tossup_metrics.csv"), TOSSUP_METRICS
    )
    stage_summary = _stage_summary_rows(evaluation_dir)
    bonus_scalars = _bonus_scalar_rows(evaluation_dir)
    comparison = _comparison_frame(comparison_csv)
    pyramidal_parameters = _parameter_summary(
        csv_dir / "pyramidal_parameter_distribution_summary.csv"
    )
    bonus_parameters = _parameter_summary(
        csv_dir / "bonus_parameter_distribution_summary.csv"
    )

    lines = [
        "# CompIRT Evaluation Summary",
        "",
        f"Evaluation folder: `{evaluation_dir}`",
        f"Result root: `{result_root_for_evaluation(evaluation_dir)}`",
        "",
        (
            "This file consolidates the metric CSVs, bonus-model comparison "
            "deltas, and fitted-parameter distribution summaries for quick review."
        ),
        "",
    ]
    _append_table(
        lines,
        "Run Variables And Stage Scalars",
        stage_summary,
        "No stage summary JSON files were found for this evaluation folder.",
    )
    _append_table(
        lines,
        "Bonus Stage Scalars",
        bonus_scalars,
        "No bonus-stage scalar summary values were found.",
    )
    _append_table(
        lines,
        "Stage 2 Bonus Metrics",
        bonus,
        "No bonus metrics CSV was found.",
    )
    _append_table(
        lines,
        "Stage 1 Tossup Metrics",
        tossup,
        "No tossup metrics CSV was found.",
    )
    _append_table(
        lines,
        "No-Synergy Versus Synergy Deltas",
        comparison,
        "No sibling comparison/bonus_model_comparison.csv was found.",
    )
    _append_table(
        lines,
        "Pyramidal Player And Tossup Parameters",
        pyramidal_parameters,
        "No pyramidal parameter distribution summary CSV was found.",
    )
    _append_table(
        lines,
        "Bonus And Synergy Parameters",
        bonus_parameters,
        "No bonus parameter distribution summary CSV was found.",
    )

    output_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return output_path
