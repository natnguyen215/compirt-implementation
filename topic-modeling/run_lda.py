"""Train a plain unsupervised LDA topic model on quizbowl questions.

This script reads quizbowl question text from the local database and fits
``tomotopy.LDAModel`` with every topic treated as a free latent topic. Database
category/subcategory fields are preserved in the exported metadata, but they
are not fed to LDA during training.

The saved ``document_latent_vectors.csv`` uses the standard topic-vector schema
consumed by the topic CompIRT pipeline. Point ``TOPIC_VECTORS`` at that file and
run the downstream stages with ``RUN_PLDA=0`` to use these unsupervised vectors.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

try:
    import tomotopy as tp
except ModuleNotFoundError as exc:
    raise SystemExit(
        "tomotopy is required. Install it with: .venv/bin/pip install tomotopy==0.14.0"
    ) from exc

from topic_utils.corpus import load_documents
from topic_utils.outputs import (
    DOCUMENT_VECTOR_FILENAME,
    DEFAULT_DATABASE,
    DEFAULT_LDA_OUTPUT_DIR,
    document_vector_fieldnames,
    document_vector_row,
)


def train_model(
    documents: list[dict[str, object]],
    dimensions: int,
    iterations: int,
    train_interval: int,
    min_df: int,
    rm_top: int,
    seed: int,
    workers: int,
):
    """Train a plain LDA model on the documents and return it with the kept docs.

    Every topic is free and latent. Category labels carried by the loaded
    documents are intentionally ignored by the model and only exported later as
    metadata.
    """
    # Create a plain LDA model with 'dimensions' latent topics and no labels.
    model = tp.LDAModel(
        k=dimensions,
        min_df=min_df,
        rm_top=rm_top,
        seed=seed,
    )
    added_documents = []
    for document in documents:
        before_count = len(model.docs)
        # Regular LDA: add only the words, never the labels.
        model.add_doc(document["words"])
        if len(model.docs) > before_count:
            added_documents.append(document)

    if not added_documents:
        raise ValueError("No documents were added to the model.")

    # Train in train_interval-sized chunks, logging log-likelihood per word.
    trained = 0
    while trained < iterations:
        step = min(train_interval, iterations - trained)
        model.train(step, workers=workers)
        trained += step
        print(f"iteration={trained} ll_per_word={model.ll_per_word:.4f}")

    return model, added_documents


def write_topics(model: tp.LDAModel, output_path: Path, top_n: int) -> None:
    """Write 'topics.csv': one row per latent topic with its top words."""
    with output_path.open("w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["topic_id", "topic_type", "label", "top_words"],
        )
        writer.writeheader()
        for topic_id in range(model.k):
            words = [word for word, _ in model.get_topic_words(topic_id, top_n=top_n)]
            writer.writerow(
                {
                    "topic_id": topic_id,
                    "topic_type": "latent",
                    "label": f"latent_topic_{topic_id:02d}",
                    "top_words": " ".join(words),
                }
            )


def write_document_vectors(
    model: tp.LDAModel,
    added_documents: list[dict[str, object]],
    output_path: Path,
    dimensions: int,
) -> None:
    """Write standard topic-vector rows with the full LDA topic distribution."""
    if len(model.docs) != len(added_documents):
        raise ValueError("Model document count does not match source document count.")

    # Plain LDA has no label topics, so the full topic distribution is latent.
    with output_path.open("w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=document_vector_fieldnames(dimensions))
        writer.writeheader()
        for doc, source in zip(model.docs, added_documents):
            latent_dist = doc.get_topic_dist()
            writer.writerow(document_vector_row(source, latent_dist))


def write_run_summary(
    model: tp.LDAModel,
    output_path: Path,
    database: Path,
    question_type: str,
    dimensions: int,
    iterations: int,
    document_count: int,
) -> None:
    """Write 'run_summary.json': run settings and basic model fit statistics."""
    summary = {
        "model": "LDA",
        "database": str(database),
        "question_type": question_type,
        "documents": document_count,
        "latent_dimensions": dimensions,
        "total_topics": model.k,
        "iterations": iterations,
        "ll_per_word": model.ll_per_word,
        "perplexity": model.perplexity,
    }
    output_path.write_text(json.dumps(summary, indent=2) + "\n")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--database", type=Path, default=DEFAULT_DATABASE)
    parser.add_argument(
        "--output-dir",
        type=Path,
        help="Defaults to topic-modeling/outputs/lda.",
    )
    parser.add_argument(
        "--question-type",
        choices=["both", "tossups", "bonuses"],
        default="both",
        help="Which database question text to model.",
    )
    parser.add_argument(
        "--dimensions",
        type=int,
        default=10,
        help="Number of latent LDA topics.",
    )
    parser.add_argument("--iterations", type=int, default=500)
    parser.add_argument("--train-interval", type=int, default=50)
    parser.add_argument("--min-df", type=int, default=2)
    parser.add_argument("--rm-top", type=int, default=0)
    parser.add_argument("--top-n", type=int, default=15)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--workers", type=int, default=1)
    args = parser.parse_args()
    if args.output_dir is None:
        args.output_dir = DEFAULT_LDA_OUTPUT_DIR
    return args


def main() -> None:
    # Parse and validate the command-line arguments.
    args = parse_args()
    if args.dimensions < 1:
        raise ValueError("--dimensions must be at least 1.")
    if args.iterations < 1:
        raise ValueError("--iterations must be at least 1.")
    if args.train_interval < 1:
        raise ValueError("--train-interval must be at least 1.")

    # Load and tokenize the question documents from the database.
    documents = load_documents(args.database, args.question_type)
    print(f"loaded {len(documents)} documents from {args.database}")

    # Train the LDA topic model.
    model, added_documents = train_model(
        documents=documents,
        dimensions=args.dimensions,
        iterations=args.iterations,
        train_interval=args.train_interval,
        min_df=args.min_df,
        rm_top=args.rm_top,
        seed=args.seed,
        workers=args.workers,
    )

    # Resolve the output paths for the saved artifacts.
    args.output_dir.mkdir(parents=True, exist_ok=True)
    model_path = args.output_dir / f"lda_{args.dimensions}d.bin"
    topics_path = args.output_dir / "topics.csv"
    vectors_path = args.output_dir / DOCUMENT_VECTOR_FILENAME
    summary_path = args.output_dir / "run_summary.json"

    # Save the model, topic words, per-document latent vectors, and run summary.
    model.save(str(model_path))
    write_topics(model, topics_path, args.top_n)
    write_document_vectors(model, added_documents, vectors_path, args.dimensions)
    write_run_summary(
        model=model,
        output_path=summary_path,
        database=args.database,
        question_type=args.question_type,
        dimensions=args.dimensions,
        iterations=args.iterations,
        document_count=len(added_documents),
    )

    print(f"saved model to {model_path}")
    print(f"saved topics to {topics_path}")
    print(f"saved {args.dimensions}d document vectors to {vectors_path}")
    print(f"saved run summary to {summary_path}")


if __name__ == "__main__":
    main()
