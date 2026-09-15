"""Collapse raw quizbowl category labels to canonical top-level categories."""

from __future__ import annotations


UNKNOWN = "Unknown"

# Ordered keyword -> canonical category rules. Raw labels are inconsistent
# across tournaments ("Any History", "Mythology>", "Pop Culture", ...), so
# collapse them to standard top-level quizbowl categories. Order matters.
CANONICAL_RULES = [
    ("social science", "Social Science"),
    ("science", "Science"),
    ("literature", "Literature"),
    ("history", "History"),
    ("painting", "Fine Arts"),
    ("sculpture", "Fine Arts"),
    ("music", "Fine Arts"),
    ("fine arts", "Fine Arts"),
    ("religion", "Religion"),
    ("mythology", "Mythology"),
    ("philosophy", "Philosophy"),
    ("geography", "Geography"),
    ("current events", "Current Events"),
    ("pop culture", "Popular Culture"),
    ("popular culture", "Popular Culture"),
    ("academic", "Other Academic"),
]


def top_level_category(label: str) -> str:
    """Map a raw 'category:X|subcategory:...' label to a canonical category."""
    if not isinstance(label, str) or not label.strip():
        return UNKNOWN
    first = label.split("|", 1)[0].strip()
    if first.lower().startswith("category:"):
        first = first.split(":", 1)[1].strip()
    text = first.lower()
    for keyword, canonical in CANONICAL_RULES:
        if keyword in text:
            return canonical
    return UNKNOWN
