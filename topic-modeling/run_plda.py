"""Train a partially labeled LDA topic model on quizbowl questions.

This script reads quizbowl question text from the local database and fits
``tomotopy.PLDAModel``. Database category, subcategory, and subsubcategory
labels seed label-guided topics, while ``--dimensions`` controls the shared
latent topics exported for topic CompIRT.

The saved ``document_latent_vectors.csv`` contains only the shared latent-topic
proportions. Label-guided topics structure PLDA training, but they are not used
as CompIRT topic gates.
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
    DEFAULT_PLDA_OUTPUT_DIR,
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
    """Train a PLDA model on the documents and return it with the kept docs.

    tomotopy may drop a document whose words all fall below 'min_df', so the
    returned 'added_documents' is the subset actually in the model, aligned
    one-to-one with 'model.docs' for the later vector export.
    """
    # Create the PLDA model and add each document (tracking which ones were kept).
    model = tp.PLDAModel(
        latent_topics=dimensions,
        topics_per_label=1,
        min_df=min_df,
        rm_top=rm_top,
        seed=seed,
    )
    added_documents = []
    for document in documents:
        before_count = len(model.docs)
        model.add_doc(document["words"], labels=document["labels"])
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


def topic_name(model: tp.PLDAModel, topic_id: int) -> tuple[str, str]:
    """Return the '(topic_type, name)' for a topic id.

    tomotopy lays out the label-guided topics first ('topics_per_label' per
    category label) and the shared latent topics after them. So a 'topic_id'
    below 'label_topic_count' is a label topic; anything past it is the
    'latent_id'-th shared latent topic.
    """
    label_topic_count = len(model.topic_label_dict) * model.topics_per_label
    if topic_id < label_topic_count:
        label_id = topic_id // model.topics_per_label
        label = model.topic_label_dict[label_id]
        return "label", str(label)
    latent_id = topic_id - label_topic_count
    return "latent", f"latent_topic_{latent_id:02d}"


def write_topics(model: tp.PLDAModel, output_path: Path, top_n: int) -> None:
    """Write 'topics.csv': one row per topic with its top 'top_n' words."""
    with output_path.open("w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["topic_id", "topic_type", "label", "top_words"],
        )
        writer.writeheader()
        for topic_id in range(model.k):
            topic_type, label = topic_name(model, topic_id)
            words = [word for word, _ in model.get_topic_words(topic_id, top_n=top_n)]
            writer.writerow(
                {
                    "topic_id": topic_id,
                    "topic_type": topic_type,
                    "label": label,
                    "top_words": " ".join(words),
                }
            )


def write_document_vectors(
    model: tp.PLDAModel,
    added_documents: list[dict[str, object]],
    output_path: Path,
    dimensions: int,
) -> None:
    """Write 'document_latent_vectors.csv': each document's latent topic mix.

    Only the shared latent topics are exported (the label topics are dropped),
    so each row is the fixed topic vector 'r' consumed by topic-weighted
    CompIRT. 'latent_mass' is how much of the document's distribution those
    latent topics hold.
    """
    if len(model.docs) != len(added_documents):
        raise ValueError("Model document count does not match source document count.")

    # Write one row per document with only the shared latent topic proportions.
    label_topic_count = len(model.topic_label_dict) * model.topics_per_label
    with output_path.open("w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=document_vector_fieldnames(dimensions))
        writer.writeheader()
        for doc, source in zip(model.docs, added_documents):
            topic_dist = doc.get_topic_dist()
            latent_dist = topic_dist[label_topic_count : label_topic_count + dimensions]
            writer.writerow(document_vector_row(source, latent_dist))


def write_run_summary(
    model: tp.PLDAModel,
    output_path: Path,
    database: Path,
    question_type: str,
    dimensions: int,
    iterations: int,
    document_count: int,
) -> None:
    """Write 'run_summary.json': run settings and basic model fit statistics."""
    summary = {
        "database": str(database),
        "question_type": question_type,
        "documents": document_count,
        "label_count": len(model.topic_label_dict),
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
        help="Defaults to topic-modeling/outputs/plda.",
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
        help="Number of shared latent PLDA topics to export.",
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
        args.output_dir = DEFAULT_PLDA_OUTPUT_DIR
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

    # Train the PLDA topic model.
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
    model_path = args.output_dir / f"plda_{args.dimensions}d.bin"
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
