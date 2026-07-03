"""Tests for vocabulary building and bag-of-words alignment."""

from __future__ import annotations

import unittest

from topic.learned.bow import build_bow_matrix, build_vocabulary


def docs(*words_per_doc) -> list[dict]:
    return [
        {"document_id": f"d{index}", "words": list(words)}
        for index, words in enumerate(words_per_doc)
    ]


class VocabularyTests(unittest.TestCase):
    def test_min_df_filters_rare_words(self):
        # df: a=1, b=3, c=2, x=1, y=1 -> only b, c survive min_df=2.
        documents = docs(["a", "a", "b", "c"], ["b", "c", "c", "x"], ["b", "y"])
        vocabulary, index = build_vocabulary(documents, min_df=2)
        self.assertEqual(vocabulary, ["b", "c"])
        self.assertEqual(index, {"b": 0, "c": 1})

    def test_rm_top_drops_most_frequent(self):
        # cf: the=4, cat=3, dog=2; rm_top=1 removes "the".
        documents = docs(["the", "the", "the", "cat", "cat", "dog"], ["the", "cat", "dog"])
        vocabulary, _ = build_vocabulary(documents, min_df=1, rm_top=1)
        self.assertEqual(vocabulary, ["cat", "dog"])

    def test_vocab_size_caps_by_frequency(self):
        documents = docs(["the", "the", "the", "cat", "cat", "dog"], ["the", "cat", "dog"])
        vocabulary, _ = build_vocabulary(documents, min_df=1, vocab_size=1)
        self.assertEqual(vocabulary, ["the"])


class BowMatrixTests(unittest.TestCase):
    def test_counts_align_to_requested_order(self):
        documents = docs(["a", "a", "b", "c"], ["b", "c", "c", "x"], ["b", "y"])
        _, index = build_vocabulary(documents, min_df=2)  # vocab = [b, c]
        matrix = build_bow_matrix(documents, index, ["d2", "d0", "d1"])
        # Rows follow the requested id order, OOV words ignored.
        self.assertEqual(matrix.tolist(), [[1.0, 0.0], [1.0, 1.0], [1.0, 2.0]])

    def test_missing_id_raises(self):
        documents = docs(["a", "b"], ["b", "c"])
        _, index = build_vocabulary(documents, min_df=1)
        with self.assertRaises(ValueError):
            build_bow_matrix(documents, index, ["d0", "missing"])


if __name__ == "__main__":
    unittest.main()
