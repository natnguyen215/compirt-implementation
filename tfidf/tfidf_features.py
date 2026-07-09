"""TF-IDF clue features for text-aware pyramidal tossup experiments.

These helpers intentionally live beside the experiment script instead of in the
main data pipeline, so the baseline training path stays untouched. The reveal
signal is TF-IDF: each token contributes its document-normalized term frequency
times its corpus inverse document frequency, so both informative terms and
repeated terms raise the revealed clue mass.
"""

from __future__ import annotations

import math
import re
from collections import Counter
from collections.abc import Sequence

import torch


TOKEN_RE = re.compile(r"[a-z][a-z'-]+")


def normalize_token(value) -> str | None:
    """Normalize one source token into a lowercase content-ish token."""
    match = TOKEN_RE.search(str(value).lower())
    if match is None:
        return None
    token = match.group(0).strip("'-")
    return token or None


def _tokens_from_value(value) -> list[str]:
    """Normalize a raw token cell (string, sequence, or scalar) into tokens."""
    if value is None:
        return []
    if isinstance(value, str):
        raw_tokens = value.split()
    elif isinstance(value, Sequence):
        raw_tokens = value
    else:
        raw_tokens = list(value) if hasattr(value, "__iter__") else [value]
    return [
        token for token in (normalize_token(raw_token) for raw_token in raw_tokens) if token
    ]


def _ordered_tossup_tokens(tossups, tossup_ids: Sequence[str]) -> list[list[str]]:
    """Return tossup tokens aligned to the model's tossup id order."""
    by_id: dict[str, list[str]] = {}
    for row in tossups.itertuples(index=False):
        by_id[str(row.tossup_id)] = _tokens_from_value(getattr(row, "tokens", None))

    missing = [str(tossup_id) for tossup_id in tossup_ids if str(tossup_id) not in by_id]
    if missing:
        preview = ", ".join(missing[:5])
        if len(missing) > 5:
            preview += ", ..."
        raise ValueError(f"No tossup text for ids: {preview}")

    return [by_id[str(tossup_id)] for tossup_id in tossup_ids]


def _document_idf(ordered_tokens: Sequence[Sequence[str]]) -> dict[str, float]:
    """Return inverse document frequency for every observed token.

    IDF is 'log((1 + N) / (1 + df(w)))' over the selected question corpus. No
    '+1' floor is added, so ubiquitous words ('df == N') collapse to ~0 and
    the cumulative reveal jumps only at informative clues. The '1 +' terms
    inside the log guard the denominator.
    """
    document_frequency: Counter[str] = Counter()
    for tokens in ordered_tokens:
        document_frequency.update(set(tokens))

    n_documents = max(1, len(ordered_tokens))
    return {
        word: math.log((1.0 + n_documents) / (1.0 + frequency))
        for word, frequency in document_frequency.items()
    }


def _padded_cumulative(values: Sequence[float], max_length: int) -> list[float]:
    """Return a padded cumulative sum through 'max_length' positions."""
    cumulative = 0.0
    prefix: list[float] = []
    for position in range(max_length):
        if position < len(values):
            cumulative += values[position]
        prefix.append(cumulative)
    return prefix


def _normalized_cumulative(values: Sequence[float], max_length: int) -> list[float]:
    """Return a padded cumulative sum of 'values', scaled to end at 1.0."""
    prefix = _padded_cumulative(values, max_length)
    total = prefix[-1] if prefix else 0.0
    if total > 0.0:
        prefix = [value / total for value in prefix]
    return prefix


def _padded_token_scores(values: Sequence[float], max_length: int) -> list[float]:
    """Return per-token values padded with zeros after the tossup ends."""
    return [
        float(values[position]) if position < len(values) else 0.0
        for position in range(max_length)
    ]


def build_tfidf_feature_matrices(
    tossups,
    tossup_ids: Sequence[str],
    *,
    max_length: int,
    normalize: bool = True,
    device: str | torch.device = "cpu",
) -> tuple[torch.Tensor, torch.Tensor, dict[str, object]]:
    """Return cumulative and local TF-IDF clue matrices aligned to tossup ids.

    Returns '(prefix, token, summary)':

    * 'prefix[j, t]' is cumulative TF-IDF revealed through token 't'. With
      'normalize=True' each nonempty tossup ends at 1.0.
    * 'token[j, t]' is the TF-IDF weight of the token at position 't' and is
      zero after the tossup ends. It is used by the hazard-spike variant.

    Both matrices have shape '(len(tossup_ids), max_length)'.
    """
    if max_length < 1:
        raise ValueError("max_length must be at least 1")

    ordered_tokens = _ordered_tossup_tokens(tossups, tossup_ids)
    idf = _document_idf(ordered_tokens)

    prefix = torch.zeros(
        (len(tossup_ids), max_length), dtype=torch.float32, device=device
    )
    token_matrix = torch.zeros_like(prefix)
    raw_final_scores: list[float] = []
    for row, tokens in enumerate(ordered_tokens):
        counts = Counter(tokens)
        length = max(1, len(tokens))
        token_scores = [(counts[token] / length) * idf[token] for token in tokens]
        raw_total = sum(token_scores)
        raw_final_scores.append(raw_total)

        prefix_values = (
            _normalized_cumulative(token_scores, max_length)
            if normalize
            else _padded_cumulative(token_scores, max_length)
        )
        token_values = _padded_token_scores(token_scores, max_length)

        prefix[row] = torch.tensor(prefix_values, dtype=torch.float32, device=device)
        token_matrix[row] = torch.tensor(
            token_values, dtype=torch.float32, device=device
        )

    nonempty = [score for score in raw_final_scores if score > 0.0]
    summary = {
        "tossups": len(tossup_ids),
        "vocabulary_size": len(idf),
        "max_length": max_length,
        "normalized": normalize,
        "token_weighting": "tf-idf",
        "nonempty_tossups": len(nonempty),
        "mean_raw_final_tfidf": sum(nonempty) / len(nonempty) if nonempty else 0.0,
    }
    return prefix, token_matrix, summary


def attach_tfidf_prefix_scores(
    data,
    tables,
    *,
    normalize: bool = True,
    device: str | torch.device = "cpu",
) -> dict[str, object]:
    """Attach TF-IDF prefix/token feature matrices and return feature metadata."""
    prefix, token_matrix, summary = build_tfidf_feature_matrices(
        tables["tossups"],
        data["tossup_ids"],
        max_length=int(data["T_j"].max().item()),
        normalize=normalize,
        device=device,
    )
    data["tfidf_prefix"] = prefix
    data["tfidf_token"] = token_matrix
    return summary
