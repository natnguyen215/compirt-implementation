"""Evaluate topic-weighted CompIRT outputs.

Command-line entry point for 'topic_compirt.evaluation.evaluate_topic_compirt'.
It consumes the CSV files written by 'train_topic_pyramidal.py' and
'train_topic_compositional.py' (or the joint sLDA trainers in
'topic/learned') and writes metrics, plots, and a Markdown report.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from topic.fixed.topic_compirt.evaluation import evaluate_topic_compirt
from topic.utils.outputs import load_dimension_labels


def main():
    """Parse result paths and run the full topic-weighted evaluation."""
    # Parse the paths to the fitted pyramidal/compositional results and the output dir.
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pyramidal-results", type=Path, required=True)
    parser.add_argument("--compositional-results", type=Path, required=True)
    parser.add_argument(
        "--topic-names",
        type=Path,
        help="Optional dimension,column,category CSV to relabel topic-coordinate legends",
    )
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    dimension_labels = (
        load_dimension_labels(args.topic_names) if args.topic_names else None
    )
    # Run the full topic-weighted evaluation (metrics, plots, and report).
    evaluate_topic_compirt(
        args.pyramidal_results,
        args.compositional_results,
        args.output_dir,
        dimension_labels,
    )


if __name__ == "__main__":
    main()
