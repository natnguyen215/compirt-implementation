"""Evaluate one tossup-only frozen fold with the shared Scenario A evaluator."""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from compirt_eval.common.report_paths import csv_path, evaluation_output_dirs
from compirt_eval.common.reports import (
    experiment_report_markdown,
    load_metrics_row,
    write_eval_docs_summary,
)
from compirt_eval.scenario_a_tossups import evaluate_tossups


def write_tossup_docs(output_dir: Path, metrics=None):
    """Write the standard reports for a tossup-only fold evaluation."""
    output_dir = Path(output_dir)
    if metrics is None:
        metrics = load_metrics_row(output_dir, "tossup_metrics.csv")
    report = experiment_report_markdown(
        output_dir,
        metrics,
        bonus=None,
        game=None,
        title="CompIRT Tossup Evaluation Report",
    )
    report_path = output_dir / "experiment_report.md"
    report_path.write_text(report, encoding="utf-8")
    summary_path = write_eval_docs_summary(output_dir, include_bonus=False)
    return report_path, summary_path


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pyramidal-results", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args(argv)
    evaluation_output_dirs(args.output_dir)
    metrics = evaluate_tossups(args.pyramidal_results, args.output_dir)
    pd.DataFrame([metrics]).to_csv(
        csv_path(args.output_dir, "tossup_metrics.csv"), index=False
    )
    write_tossup_docs(args.output_dir, metrics)


if __name__ == "__main__":
    main()
