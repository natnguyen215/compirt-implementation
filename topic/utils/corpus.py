"""Corpus loading and tokenization shared by topic-model scripts."""

from __future__ import annotations

import html
import re
import sqlite3
from html.parser import HTMLParser
from pathlib import Path


TOKEN_RE = re.compile(r"[a-z][a-z'-]+")

# Common quizbowl/boilerplate words dropped before topic modeling so topics key
# on subject content rather than question phrasing.
STOPWORDS = {
    "about",
    "according",
    "after",
    "against",
    "all",
    "also",
    "among",
    "and",
    "another",
    "any",
    "are",
    "argue",
    "argued",
    "argues",
    "because",
    "been",
    "begin",
    "began",
    "begins",
    "before",
    "being",
    "between",
    "both",
    "but",
    "called",
    "can",
    "could",
    "decade",
    "describe",
    "described",
    "describes",
    "different",
    "did",
    "does",
    "due",
    "during",
    "each",
    "early",
    "end",
    "ending",
    "ends",
    "every",
    "feature",
    "featured",
    "features",
    "featuring",
    "first",
    "following",
    "form",
    "forms",
    "for",
    "former",
    "from",
    "good",
    "had",
    "has",
    "have",
    "her",
    "herself",
    "him",
    "himself",
    "his",
    "how",
    "include",
    "included",
    "includes",
    "including",
    "inspired",
    "into",
    "its",
    "itself",
    "known",
    "last",
    "later",
    "led",
    "leads",
    "like",
    "made",
    "many",
    "man",
    "may",
    "men",
    "might",
    "most",
    "name",
    "named",
    "names",
    "namesake",
    "not",
    "object",
    "objects",
    "one",
    "open",
    "opened",
    "opens",
    "often",
    "only",
    "other",
    "out",
    "over",
    "part",
    "people",
    "person",
    "points",
    "profession",
    "question",
    "read",
    "reads",
    "said",
    "same",
    "see",
    "seen",
    "several",
    "she",
    "since",
    "such",
    "than",
    "that",
    "the",
    "their",
    "them",
    "then",
    "there",
    "these",
    "they",
    "thing",
    "things",
    "three",
    "this",
    "those",
    "through",
    "title",
    "titled",
    "two",
    "type",
    "types",
    "under",
    "upon",
    "use",
    "used",
    "uses",
    "using",
    "was",
    "well",
    "were",
    "what",
    "when",
    "where",
    "which",
    "while",
    "who",
    "whose",
    "will",
    "with",
    "woman",
    "women",
    "work",
    "works",
    "would",
    "write",
    "writes",
    "written",
    "wrote",
    "you",
    "your",
}


class TextExtractor(HTMLParser):
    """Collect the visible text of an HTML fragment, dropping the tags."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []

    def handle_data(self, data: str) -> None:
        self.parts.append(data)


def clean_text(value: str | None) -> str:
    """Strip HTML, unescape entities, and collapse whitespace to one string."""
    parser = TextExtractor()
    parser.feed(value or "")
    parser.close()
    text = html.unescape("".join(parser.parts)).replace("\xa0", " ")
    return " ".join(text.split())


def tokenize(value: str | None) -> list[str]:
    """Clean text into lowercase content words, dropping short and stop words."""
    text = clean_text(value).lower()
    # TOKEN_RE already requires 2+ characters, but a token can include a
    # leading/trailing apostrophe or hyphen (e.g. "author's"); stripping those
    # before the length check keeps genuinely short leftovers (e.g. "s'") out
    # of the vocabulary, while STOPWORDS is matched against the unstripped
    # token since none of its entries carry a leading/trailing "'"/"-".
    return [
        token.strip("'-")
        for token in TOKEN_RE.findall(text)
        if len(token.strip("'-")) > 2 and token not in STOPWORDS
    ]


def label_text(value: str | None) -> str:
    """Clean a single category field into a plain label string."""
    return clean_text(value).strip()


def labels_from_row(row: sqlite3.Row) -> list[str]:
    """Build database category labels for model supervision and metadata."""
    labels: list[str] = []
    category = label_text(row["category"])
    subcategory = label_text(row["subcategory"])
    subsubcategory = label_text(row["subsubcategory"])

    if category:
        labels.append(f"category:{category}")
    if subcategory and subcategory != category:
        prefix = category or "Uncategorized"
        labels.append(f"subcategory:{prefix}/{subcategory}")
    if subsubcategory:
        prefix = category or "Uncategorized"
        middle = subcategory or "Other"
        labels.append(f"subsubcategory:{prefix}/{middle}/{subsubcategory}")
    return labels


def load_documents(database: Path, question_type: str) -> list[dict[str, object]]:
    """Read SQLite questions into tokenized topic documents.

    'document_id' is built as 'set-slug::edition-slug::pN::qM' (or '::bM' for
    bonuses) so it matches the composite tossup/bonus IDs used elsewhere in
    CompIRT (e.g. 'compirt_data'); topic vectors keyed by this ID can then be
    aligned to model rows without a separate join table.
    """
    queries = []
    if question_type in {"both", "tossups"}:
        queries.append(
            """
            SELECT
                'tossup' AS question_type,
                qs.slug || '::' || qse.slug || '::p' || pq.packet_id
                    || '::q' || pq.question_number AS document_id,
                'tossup-' || tossup.id AS source_document_id,
                tossup.question AS text,
                question.category,
                question.subcategory,
                question.subsubcategory
            FROM packet_question pq
            JOIN packet p ON p.id = pq.packet_id
            JOIN question_set_edition qse ON qse.id = p.question_set_edition_id
            JOIN question_set qs ON qs.id = qse.question_set_id
            JOIN question ON question.id = pq.question_id
            JOIN tossup ON tossup.question_id = question.id
            ORDER BY pq.packet_id, pq.question_number, tossup.id
            """
        )
    if question_type in {"both", "bonuses"}:
        queries.append(
            """
            SELECT
                'bonus' AS question_type,
                qs.slug || '::' || qse.slug || '::p' || pq.packet_id
                    || '::b' || pq.question_number AS document_id,
                'bonus-' || bonus.id AS source_document_id,
                COALESCE(bonus.leadin, '') || ' ' || COALESCE((
                    SELECT GROUP_CONCAT(part, ' ')
                    FROM (
                        SELECT part
                        FROM bonus_part
                        WHERE bonus_part.bonus_id = bonus.id
                        ORDER BY part_number
                    )
                ), '') AS text,
                question.category,
                question.subcategory,
                question.subsubcategory
            FROM packet_question pq
            JOIN packet p ON p.id = pq.packet_id
            JOIN question_set_edition qse ON qse.id = p.question_set_edition_id
            JOIN question_set qs ON qs.id = qse.question_set_id
            JOIN question ON question.id = pq.question_id
            JOIN bonus ON bonus.question_id = question.id
            ORDER BY pq.packet_id, pq.question_number, bonus.id
            """
        )

    connection = sqlite3.connect(
        f"file:{database.resolve().as_posix()}?mode=ro", uri=True
    )
    connection.row_factory = sqlite3.Row
    documents: list[dict[str, object]] = []
    try:
        for query in queries:
            for row in connection.execute(query):
                words = tokenize(row["text"])
                if not words:
                    continue
                documents.append(
                    {
                        "document_id": row["document_id"],
                        "source_document_id": row["source_document_id"],
                        "question_type": row["question_type"],
                        "words": words,
                        "labels": labels_from_row(row),
                    }
                )
    finally:
        connection.close()
    return documents
