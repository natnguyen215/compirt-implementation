"""Vocabulary and bag-of-words tensors for the joint sLDA/CompIRT model.

The LDA word likelihood consumes a fixed-width word-count vector per document,
not a token list. These helpers build a vocabulary from the tokenized corpus and a
'(n_documents, vocab_size)' count matrix aligned to a caller-supplied id order
(e.g. 'data["tossup_ids"]'), so each model row's BoW lines up with that row's
topic latent and IRT parameters.
"""

from __future__ import annotations

from collections import Counter
from collections.abc import Sequence

import numpy as np
import torch


def build_vocabulary(
    documents: Sequence[dict],
    *,
    vocab_size: int = 5000,
    min_df: int = 2,
    rm_top: int = 0,
) -> tuple[list[str], dict[str, int]]:
    """Build a vocabulary from tokenized documents.

    Keeps words appearing in at least 'min_df' documents, drops the 'rm_top'
    most frequent (stopword-like) words, then keeps the 'vocab_size' most
    frequent of the rest. The returned vocabulary is sorted for a stable index.
    """
    document_frequency: Counter[str] = Counter()
    collection_frequency: Counter[str] = Counter()
    for document in documents:
        words = document["words"]
        collection_frequency.update(words)
        document_frequency.update(set(words))

    # Rank surviving words by collection frequency, drop the very top, then cap.
    candidates = [
        word for word in collection_frequency if document_frequency[word] >= min_df
    ]
    candidates.sort(key=lambda word: collection_frequency[word], reverse=True)
    kept = candidates[rm_top : rm_top + vocab_size]

    vocabulary = sorted(kept)
    vocabulary_index = {word: index for index, word in enumerate(vocabulary)}
    return vocabulary, vocabulary_index


def build_bow_matrix(
    documents: Sequence[dict],
    vocabulary_index: dict[str, int],
    ordered_ids: Sequence[str],
    *,
    id_key: str = "document_id",
) -> np.ndarray:
    """Return a '(len(ordered_ids), vocab_size)' float32 count matrix.

    Rows follow 'ordered_ids' exactly so the matrix aligns with the model's
    tossup/bonus order. Every requested ID is validated against the source
    documents before matrix construction.
    """
    documents_by_id = {str(document[id_key]): document for document in documents}
    missing = [str(value) for value in ordered_ids if str(value) not in documents_by_id]
    if missing:
        preview = ", ".join(missing[:5])
        if len(missing) > 5:
            preview += ", ..."
        raise ValueError(f"No BoW document for ids: {preview}")

    matrix = np.zeros((len(ordered_ids), len(vocabulary_index)), dtype=np.float32)
    for row, identifier in enumerate(ordered_ids):
        document = documents_by_id[str(identifier)]
        for word in document["words"]:
            index = vocabulary_index.get(word)
            if index is not None:
                matrix[row, index] += 1.0
    return matrix


def bow_tensor(
    documents: Sequence[dict],
    vocabulary_index: dict[str, int],
    ordered_ids: Sequence[str],
    *,
    id_key: str = "document_id",
    device: str | torch.device = "cpu",
) -> torch.Tensor:
    """Build the BoW count matrix and return it as a float32 tensor on 'device'."""
    matrix = build_bow_matrix(documents, vocabulary_index, ordered_ids, id_key=id_key)
    return torch.tensor(matrix, dtype=torch.float32, device=device)
