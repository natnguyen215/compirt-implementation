"""Evaluate outputs from the dedicated topic-specific TF-IDF experiment."""

from __future__ import annotations

import argparse
from pathlib import Path

from topic.tfidf.evaluation import evaluate_topic_tfidf
from topic.utils.outputs import load_dimension_labels


def main():
    """Parse result paths and run the TF-IDF-aware topic evaluation."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pyramidal-results", type=Path, required=True)
    parser.add_argument("--compositional-results", type=Path, required=True)
    parser.add_argument("--comparison-pyramidal-results", type=Path)
    parser.add_argument("--topic-names", type=Path)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    dimension_labels = (
        load_dimension_labels(args.topic_names) if args.topic_names else None
    )
    evaluate_topic_tfidf(
        args.pyramidal_results,
        args.compositional_results,
        args.output_dir,
        args.comparison_pyramidal_results,
        dimension_labels,
    )


if __name__ == "__main__":
    main()
