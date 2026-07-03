"""Clean raw question/HTML text into the plain strings the dataset stores.

Source question and bonus-part text comes out of the database with HTML
markup (bold/italic clue markers, entity-escaped quotes, moderator asides).
These helpers strip that markup down to the flat text and token list the
tossup/bonus tables need, and detect the one recurring editorial pattern
(a leading "note to moderator" aside) that should not count as part of the
question itself.
"""

from __future__ import annotations

import html
import re
from html.parser import HTMLParser


class _TextExtractor(HTMLParser):
    """Collect only the text content of an HTML fragment, discarding tags."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []

    def handle_data(self, data: str) -> None:
        self.parts.append(data)


def sanitize_html(value: str | None) -> str:
    """Strip HTML tags, unescape entities, and collapse whitespace to single spaces."""
    parser = _TextExtractor()
    parser.feed(value or "")
    parser.close()
    return " ".join(html.unescape("".join(parser.parts)).replace("\xa0", " ").split())


def strip_leading_moderator_note(value: str | None) -> tuple[str, int]:
    """Remove a leading "note to moderator" aside, if the question has one.

    Some tossups open with an italicized editorial note (e.g. instructions
    about pronunciation) rather than question content. That note is wrapped
    in a leading '<em>...</em>' and its text contains "note to moderator:".
    When present, it is dropped from the returned question text and its word
    count is returned as 'prefix_tokens' so callers ('build_records') can
    keep buzz token positions -- which were recorded against the *original*
    token stream -- aligned with the cleaned, note-free token stream.
    """
    raw = value or ""
    match = re.match(r"^\s*<em[^>]*>.*?</em>\s*", raw, flags=re.IGNORECASE | re.DOTALL)
    if match and "note to moderator:" in sanitize_html(match.group(0)).lower():
        prefix_tokens = len(sanitize_html(match.group(0)).split())
        return sanitize_html(raw[match.end() :]), prefix_tokens
    return sanitize_html(raw), 0


def sentence_boundaries(tokens: list[str]) -> list[int]:
    """Return the token indices where a sentence ends, whitespace-tokenized.

    A token counts as sentence-ending when it closes with '.', '!', or
    '?' (optionally followed by a closing quote/bracket). The final token is
    always included as a boundary, even if it lacks terminal punctuation, so
    every tossup has at least one "sentence" to reveal.
    """
    boundaries = [idx for idx, token in enumerate(tokens) if re.search(r"[.!?][\"')\]]*$", token)]
    if tokens and (not boundaries or boundaries[-1] != len(tokens) - 1):
        boundaries.append(len(tokens) - 1)
    return boundaries
