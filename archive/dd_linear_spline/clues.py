"""Protected sentence boundaries and spline metadata for tossup questions."""

from __future__ import annotations

import re

import pandas as pd
import torch

from compirt_data import tossup_tensors


_CLOSING = "\"'”’)]}"
_OPENING = "\"'“‘([{"
_INITIAL = re.compile(r"^[A-Z]\.$")
_DOTTED_ACRONYM = re.compile(r"^(?:[A-Za-z0-9]+\.){2,}$")
_TERMINAL = re.compile(r"[.!?]+$")

# This deliberately stays small. The context rules below handle initials and
# acronyms; this set covers titles and abbreviations that regularly occur in
# quizbowl prose.
_ABBREVIATIONS = {
    "ca.",
    "cf.",
    "dr.",
    "e.g.",
    "eq.",
    "fig.",
    "gen.",
    "gov.",
    "i.e.",
    "jr.",
    "mr.",
    "mrs.",
    "ms.",
    "mt.",
    "no.",
    "pres.",
    "prof.",
    "rep.",
    "rev.",
    "sen.",
    "sr.",
    "st.",
    "v.",
    "vs.",
}
_ALWAYS_INTERNAL_ABBREVIATIONS = {
    "dr.",
    "e.g.",
    "eq.",
    "fig.",
    "gen.",
    "gov.",
    "i.e.",
    "mr.",
    "mrs.",
    "ms.",
    "mt.",
    "no.",
    "pres.",
    "prof.",
    "rep.",
    "rev.",
    "st.",
}
_STRONG_SENTENCE_STARTERS = {
    "A",
    "Above",
    "According",
    "After",
    "Although",
    "An",
    "Another",
    "As",
    "At",
    "Before",
    "Both",
    "But",
    "By",
    "Despite",
    "During",
    "Each",
    "Early",
    "Following",
    "For",
    "He",
    "Her",
    "His",
    "However",
    "If",
    "In",
    "It",
    "Its",
    "Later",
    "Like",
    "Many",
    "Meanwhile",
    "More",
    "Most",
    "Name",
    "Near",
    "Neither",
    "On",
    "One",
    "Other",
    "Several",
    "She",
    "Since",
    "Some",
    "Still",
    "Such",
    "That",
    "The",
    "Their",
    "These",
    "They",
    "This",
    "Those",
    "To",
    "Two",
    "Unlike",
    "We",
    "What",
    "When",
    "Where",
    "Which",
    "Who",
    "While",
    "With",
    "Yet",
}


def _bare(token: str) -> str:
    return token.lstrip(_OPENING).rstrip(_CLOSING)


def _continues_abbreviation(tokens: list[str], index: int, core: str) -> bool:
    """Return whether a period-ending token is internal to a phrase."""
    lower = core.lower()
    if lower in _ALWAYS_INTERNAL_ABBREVIATIONS:
        return True
    if index + 1 >= len(tokens):
        return False

    previous = _bare(tokens[index - 1]) if index else ""
    following = _bare(tokens[index + 1])
    if lower == "et." and following.lower() == "al":
        return True
    if lower in _ABBREVIATIONS:
        return following not in _STRONG_SENTENCE_STARTERS
    if lower == "al." and previous.lower() == "et":
        return following not in _STRONG_SENTENCE_STARTERS
    if _INITIAL.fullmatch(core):
        # Initial chains and a final initial before a surname stay together.
        if _INITIAL.fullmatch(following) or _DOTTED_ACRONYM.fullmatch(following):
            return True
        if following and following[0].isdigit():
            return True
        if following in _STRONG_SENTENCE_STARTERS:
            return False
        if _INITIAL.fullmatch(previous):
            return True
        if following and following[0].islower():
            return True
        # A capitalized non-starter is normally a surname. A strong starter
        # allows "Maximilian I. A type ..." to remain a real boundary.
        return bool(
            following
            and following[0].isupper()
            and following not in _STRONG_SENTENCE_STARTERS
        )
    if _DOTTED_ACRONYM.fullmatch(core):
        return bool(following and following not in _STRONG_SENTENCE_STARTERS)
    return False


def _quote_context(token: str, in_quote: bool) -> tuple[bool, bool, bool]:
    """Return whether terminal punctuation is quoted, closes it, and next state."""
    terminal = re.search(r"[.!?]+[\"'”’)\]}]*$", token)

    def state_after(text, state):
        for character in text:
            if character == "“":
                state = True
            elif character == "”":
                state = False
            elif character == '"':
                state = not state
        return state

    punctuation_start = terminal.start() if terminal else len(token)
    inside_at_terminal = state_after(token[:punctuation_start], in_quote)
    next_state = state_after(token, in_quote)
    closes_at_terminal = bool(
        inside_at_terminal
        and terminal
        and re.search(r"[\"”]", token[punctuation_start:])
        and not next_state
    )
    return inside_at_terminal, closes_at_terminal, next_state


def protected_sentence_boundaries(tokens: list[str]) -> list[int]:
    """Return zero-based clue-end token indices without common false splits."""
    boundaries: list[int] = []
    in_quote = False
    for index, token in enumerate(tokens):
        inside_quote, closes_quote, next_quote_state = _quote_context(
            token, in_quote
        )
        core = _bare(token)
        terminal = _TERMINAL.search(core)
        if terminal is None:
            in_quote = next_quote_state
            continue
        punctuation = terminal.group(0)
        is_final = index == len(tokens) - 1
        following = _bare(tokens[index + 1]) if not is_final else ""
        following_is_lower = bool(following and following[0].islower())
        # Punctuation inside a quotation or title is not a clue boundary unless
        # it closes the quote and the surrounding sentence also ends there.
        if not is_final and inside_quote and not closes_quote:
            in_quote = next_quote_state
            continue
        if not is_final and closes_quote and following_is_lower:
            in_quote = next_quote_state
            continue
        # A question/exclamation used as a title or embedded quotation is
        # followed by the surrounding sentence's lowercase continuation.
        if not is_final and punctuation[-1] in "!?" and following_is_lower:
            in_quote = next_quote_state
            continue
        # Ellipses within quoted material are pauses, not sentence boundaries.
        if not is_final and punctuation.startswith(".."):
            in_quote = next_quote_state
            continue
        if punctuation == "." and _continues_abbreviation(tokens, index, core):
            in_quote = next_quote_state
            continue
        boundaries.append(index)
        in_quote = next_quote_state
    if tokens and (not boundaries or boundaries[-1] != len(tokens) - 1):
        boundaries.append(len(tokens) - 1)
    return boundaries


def attach_spline_knot_positions(data, positions_by_tossup, device="cpu"):
    """Attach padded fixed knot positions and flattened valid-knot indices."""
    positions = [
        list(map(float, positions_by_tossup[tossup_id]))
        for tossup_id in data["tossup_ids"]
    ]
    if any(len(row) < 2 for row in positions):
        raise ValueError(
            "Every spline must contain x=0 and at least one clue endpoint"
        )
    if any(row[0] != 0.0 or abs(row[-1] - 1.0) > 1e-6 for row in positions):
        raise ValueError("Spline knot positions must begin at 0 and end at 1")
    if any(
        any(right <= left for left, right in zip(row, row[1:]))
        for row in positions
    ):
        raise ValueError("Spline knot positions must be strictly increasing")

    counts = [len(row) for row in positions]
    max_knots = max(counts)
    padded_positions = []
    padded_indices = []
    offset = 0
    for row in positions:
        count = len(row)
        padded_positions.append(row + [2.0] * (max_knots - count))
        padded_indices.append(
            list(range(offset, offset + count)) + [0] * (max_knots - count)
        )
        offset += count
    data.update(
        {
            "spline_knot_positions": torch.tensor(
                padded_positions, dtype=torch.float32, device=device
            ),
            "spline_knot_indices": torch.tensor(
                padded_indices, dtype=torch.long, device=device
            ),
            "spline_knot_counts": torch.tensor(
                counts, dtype=torch.long, device=device
            ),
            "n_spline_knots": offset,
        }
    )
    return data


def build_spline_tensors(observations, tossups: pd.DataFrame, device="cpu"):
    """Build ordinary tossup tensors plus protected clue-aligned spline knots."""
    data = tossup_tensors(observations, device)
    indexed = tossups.assign(tossup_id=tossups["tossup_id"].astype(str)).set_index(
        "tossup_id"
    )
    positions_by_tossup = {}
    for tossup_id in data["tossup_ids"]:
        if tossup_id not in indexed.index:
            raise ValueError(f"Tossup {tossup_id!r} is missing from the tossup table")
        tokens = list(indexed.loc[tossup_id, "tokens"])
        if not tokens:
            raise ValueError(f"Tossup {tossup_id!r} has no tokens")
        boundaries = protected_sentence_boundaries(tokens)
        positions_by_tossup[tossup_id] = [
            0.0,
            *((boundary + 1) / len(tokens) for boundary in boundaries),
        ]
    return attach_spline_knot_positions(data, positions_by_tossup, device)
