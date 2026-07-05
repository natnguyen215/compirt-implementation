"""TF-IDF clue features for clue-adjusted pyramidal tossup experiments.

These helpers intentionally live beside the experiment script instead of in the
main data pipeline, so the baseline training path stays untouched.
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
    """Return smoothed inverse document frequency for every observed token."""
    document_frequency: Counter[str] = Counter()
    for tokens in ordered_tokens:
        document_frequency.update(set(tokens))

    n_documents = max(1, len(ordered_tokens))
    return {
        word: math.log((1.0 + n_documents) / (1.0 + frequency)) + 1.0
        for word, frequency in document_frequency.items()
    }


def _normalized_cumulative(values: Sequence[float], max_length: int) -> list[float]:
    """Return the padded cumulative sum of 'values', scaled to end at 1.0."""
    cumulative = 0.0
    prefix: list[float] = []
    for position in range(max_length):
        if position < len(values):
            cumulative += values[position]
        prefix.append(cumulative)
    if cumulative > 0.0:
        prefix = [value / cumulative for value in prefix]
    return prefix


def _raw_tfidf_token_scores(tokens: Sequence[str], idf: dict[str, float]) -> list[float]:
    """Return per-token TF-IDF scores: term frequency times inverse doc frequency."""
    counts = Counter(tokens)
    length = max(1, len(tokens))
    return [(counts[token] / length) * idf[token] for token in tokens]


def build_tfidf_prefix_matrix(
    tossups,
    tossup_ids: Sequence[str],
    *,
    max_length: int,
    normalize: bool = True,
    device: str | torch.device = "cpu",
) -> tuple[torch.Tensor, dict[str, object]]:
    """Return the cumulative per-token TF-IDF clue score matrix aligned to tossup ids.

    'prefix_j(t) = sum_{u <= t} tfidf_token_j(u)'. With 'normalize=True' the
    final value is scaled to end at '1.0' for every tossup.
    """
    if max_length < 1:
        raise ValueError("max_length must be at least 1")

    ordered_tokens = _ordered_tossup_tokens(tossups, tossup_ids)
    idf = _document_idf(ordered_tokens)

    prefix = torch.zeros(
        (len(tossup_ids), max_length), dtype=torch.float32, device=device
    )
    raw_final_scores: list[float] = []
    for row, tokens in enumerate(ordered_tokens):
        raw_scores = _raw_tfidf_token_scores(tokens, idf)
        raw_values = _normalized_cumulative(raw_scores, max_length)
        raw_total = sum(raw_scores)
        raw_final_scores.append(raw_total)

        output_values = raw_values
        if not normalize and raw_total > 0.0:
            output_values = [value * raw_total for value in raw_values]

        prefix[row] = torch.tensor(output_values, dtype=torch.float32, device=device)

    nonempty = [score for score in raw_final_scores if score > 0.0]
    summary = {
        "tossups": len(tossup_ids),
        "vocabulary_size": len(idf),
        "max_length": max_length,
        "normalized": normalize,
        "nonempty_tossups": len(nonempty),
        "mean_raw_final_score": sum(nonempty) / len(nonempty) if nonempty else 0.0,
    }
    return prefix, summary


def attach_tfidf_prefix_scores(
    data,
    tables,
    *,
    normalize: bool = True,
    device: str | torch.device = "cpu",
) -> dict[str, object]:
    """Attach the TF-IDF prefix feature matrix and return feature metadata."""
    prefix, summary = build_tfidf_prefix_matrix(
        tables["tossups"],
        data["tossup_ids"],
        max_length=int(data["T_j"].max().item()),
        normalize=normalize,
        device=device,
    )
    data["tfidf_prefix"] = prefix
    return summary
