"""Focused contracts for clue-aligned linear-spline double difficulty."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import numpy as np
import pandas as pd
import pyro
import torch

from compirt_data import build_tossup_observations
from compirt_eval.scenario_a_tossups.parameters import _saved_difficulty_curve
from dd_linear_spline.clues import (
    build_spline_tensors,
    protected_sentence_boundaries,
)
from dd_linear_spline import pyramidal_model as spline
from dd_linear_spline.train_pyramidal import (
    parse_args as parse_train_args,
    run_experiment,
    save_spline_parameters,
)
from dd_linear_spline.train_monotone_pyramidal import (
    parse_args as parse_monotone_args,
)
from hazard_double_difficulty.tests.test_hazard_double_difficulty import (
    synthetic_tables,
)
from holdout.frozen_predict import (
    frozen_predict_tossups,
    parse_args as parse_frozen_args,
)


def spline_tables():
    tables = synthetic_tables()
    tables["tossups"].at[0, "tokens"] = [
        "The",
        "instrument",
        "of",
        "J.",
        "S.",
        "Bach.",
        "For",
        "10",
        "points,",
        "name",
        "it.",
    ]
    tables["tossups"].at[1, "tokens"] = [
        "One",
        "clue",
        "only.",
    ]
    return tables


class ClueBoundaryTests(unittest.TestCase):
    def boundaries(self, text):
        tokens = text.split()
        return tokens, protected_sentence_boundaries(tokens)

    def test_protects_initials_abbreviations_and_acronyms(self):
        for text, expected_tokens in (
            ("The instrument of J. S. Bach. Name it.", ["Bach.", "it."]),
            ("The S. pyogenes protein. Name it.", ["protein.", "it."]),
            ("A St. Petersburg result. Name it.", ["result.", "it."]),
            ("A U.S. citizen spoke. The end.", ["spoke.", "end."]),
            ("Smith et al. proved it. Name it.", ["it.", "it."]),
        ):
            with self.subTest(text=text):
                tokens, boundaries = self.boundaries(text)
                self.assertEqual(
                    [tokens[index] for index in boundaries], expected_tokens
                )

    def test_splits_roman_numeral_and_trailing_closers(self):
        tokens, boundaries = self.boundaries(
            "Roman Emperor Maximilian I. A claim ends.” Does it work?)"
        )
        self.assertEqual(
            [tokens[index] for index in boundaries], ["I.", "ends.”", "work?)"]
        )

    def test_embedded_quotation_punctuation_stays_in_its_sentence(self):
        tokens, boundaries = self.boundaries(
            "The speaker asks “What is there?” and cries “O heart! heart!” "
            "before leaving. This is next."
        )
        self.assertEqual(
            [tokens[index] for index in boundaries], ["leaving.", "next."]
        )

    def test_quoted_sentence_end_still_splits(self):
        tokens, boundaries = self.boundaries(
            "The speaker answers “Everything.” This is the next clue."
        )
        self.assertEqual(
            [tokens[index] for index in boundaries], ["“Everything.”", "clue."]
        )

    def test_period_after_parenthesized_pronunciation_splits(self):
        tokens, boundaries = self.boundaries(
            "A clue ends with a pronunciation (“FOO”). Next clue."
        )
        self.assertEqual(
            [tokens[index] for index in boundaries], ["(“FOO”).", "clue."]
        )

    def test_ambiguous_abbreviations_can_end_sentences(self):
        tokens, boundaries = self.boundaries(
            "One idea is due to Amartya Sen. The pope was Pius V. "
            "For 10 points, answer."
        )
        self.assertEqual(
            [tokens[index] for index in boundaries],
            ["Sen.", "V.", "answer."],
        )

    def test_initial_like_endings_split_before_sentence_starters(self):
        tokens, boundaries = self.boundaries(
            "The note is low F. After that comes a chord. "
            "The ruler was Elizabeth I. Another ruler followed."
        )
        self.assertEqual(
            [tokens[index] for index in boundaries],
            ["F.", "chord.", "I.", "followed."],
        )

    def test_dotted_identifier_and_malformed_et_al_stay_internal(self):
        tokens, boundaries = self.boundaries(
            "The pseudonym C.3.3. was used by Cox et. al in a study. Next clue."
        )
        self.assertEqual(
            [tokens[index] for index in boundaries], ["study.", "clue."]
        )

    def test_single_letter_catalog_prefix_stays_with_number(self):
        tokens, boundaries = self.boundaries(
            "Schubert’s D. 804 inspired this work. Next clue."
        )
        self.assertEqual(
            [tokens[index] for index in boundaries], ["work.", "clue."]
        )

    def test_quoted_title_does_not_split_final_prompt(self):
        tokens, boundaries = self.boundaries(
            "For 10 points, “O Captain! My Captain!” by Whitman mourns whom?"
        )
        self.assertEqual([tokens[index] for index in boundaries], ["whom?"])

    def test_boundaries_cover_ordered_nonempty_clues(self):
        tokens, boundaries = self.boundaries("First clue. Second clue Third")
        starts = [0, *(boundary + 1 for boundary in boundaries[:-1])]
        spans = [
            list(range(start, boundary + 1))
            for start, boundary in zip(starts, boundaries)
        ]
        self.assertEqual(
            [index for span in spans for index in span], list(range(len(tokens)))
        )
        self.assertEqual(boundaries[-1], len(tokens) - 1)


class SplineMathTests(unittest.TestCase):
    def setUp(self):
        self.x = torch.tensor([[0.0, 0.5, 1.0]])
        self.count = torch.tensor([3])
        self.y = torch.tensor([[[2.0], [0.0], [1.0]]], requires_grad=True)
        self.T = torch.tensor([10.0])

    def test_exact_knots_and_intermediate_values(self):
        values = spline.difficulty_curve(
            self.y,
            self.x,
            self.count,
            torch.tensor([[0.0, 2.5, 5.0, 7.5, 10.0]]),
            self.T.unsqueeze(1),
        )
        torch.testing.assert_close(
            values.squeeze(),
            torch.tensor([2.0, 1.0, 0.0, 0.5, 1.0]),
        )
        values.sum().backward()
        self.assertTrue(torch.isfinite(self.y.grad).all())

    def test_correctness_and_hazard_are_independent(self):
        theta = torch.tensor([[0.5]])
        r = torch.tensor([[1.0]])
        t = torch.tensor([5.0])
        baseline = spline.correctness_logit(
            theta, r, self.y, self.x, self.count, t, self.T
        )
        moved_hazard = self.y.detach() + 10
        torch.testing.assert_close(
            spline.correctness_logit(
                theta, r, self.y, self.x, self.count, t, self.T
            ),
            baseline,
        )
        self.assertNotEqual(
            float(
                spline.hazard_logit(
                    theta,
                    r,
                    moved_hazard,
                    self.x,
                    self.count,
                    torch.tensor([0.0]),
                    t,
                    self.T,
                )
            ),
            float(baseline.detach()),
        )

    def test_survival_grid_is_finite(self):
        value = spline.log_survival(
            torch.tensor([[0.5]]),
            torch.tensor([[1.0]]),
            self.y,
            self.x,
            self.count,
            torch.tensor([0.2]),
            torch.tensor([8]),
            torch.tensor([10]),
            t_start=torch.tensor([3]),
        )
        self.assertTrue(torch.isfinite(value).all())

    def test_monotone_landmarks_are_decreasing_within_each_tossup(self):
        data = {"spline_knot_counts": torch.tensor([3, 2])}
        starts = torch.tensor([[2.0, -1.0], [4.0, 3.0]])
        drops = torch.tensor([[0.5, 0.25], [1.0, 2.0], [0.75, 0.5]])
        values = spline.monotone_spline_landmarks(data, starts, drops)
        expected = torch.tensor(
            [
                [2.0, -1.0],
                [1.5, -1.25],
                [0.5, -3.25],
                [4.0, 3.0],
                [3.25, 2.5],
            ]
        )
        torch.testing.assert_close(values, expected)
        self.assertTrue(torch.all(values[1:3] <= values[:2]))
        self.assertTrue(torch.all(values[4] <= values[3]))


class ModelAndIntegrationTests(unittest.TestCase):
    def test_variable_clue_counts_sample_only_valid_knots(self):
        tables = spline_tables()
        data = build_spline_tensors(
            build_tossup_observations(tables), tables["tossups"]
        )
        self.assertEqual(data["spline_knot_counts"].tolist(), [3, 2])
        pyro.clear_param_store()
        trace = pyro.poutine.trace(spline.competing_risks_model).get_trace(data, 2)
        self.assertEqual(
            tuple(trace.nodes["spline_y_correct"]["value"].shape),
            (int(data["spline_knot_counts"].sum()), 2),
        )
        self.assertEqual(
            tuple(trace.nodes["spline_y_hazard"]["value"].shape),
            (int(data["spline_knot_counts"].sum()), 2),
        )

    def test_monotone_model_samples_one_positive_drop_per_transition(self):
        tables = spline_tables()
        data = build_spline_tensors(
            build_tossup_observations(tables), tables["tossups"]
        )
        pyro.clear_param_store()
        trace = pyro.poutine.trace(spline.competing_risks_model).get_trace(
            data, 2, monotone_decreasing=True
        )
        expected_drops = int(data["n_spline_knots"]) - len(data["tossup_ids"])
        for branch in ("correct", "hazard"):
            drops = trace.nodes[f"spline_drop_{branch}"]["value"]
            self.assertEqual(tuple(drops.shape), (expected_drops, 2))
            self.assertTrue(torch.all(drops >= 0))

    def test_monotone_tiny_training_saves_decreasing_landmarks(self):
        tables = spline_tables()
        with tempfile.TemporaryDirectory() as tmp:
            args = parse_monotone_args(
                ["--steps", "2", "--dimensions", "2", "--output-dir", tmp]
            )
            summary = run_experiment(
                args, tables=tables, monotone_decreasing=True
            )
            self.assertEqual(summary["model"], "dd-monotone-linear-spline")
            self.assertTrue(summary["monotone_decreasing"])
            tossups = pd.read_csv(Path(tmp) / "tossups.csv")
            for _, row in tossups.iterrows():
                count = int(row["clue_count"]) + 1
                for prefix in ("", "hazard_"):
                    for dimension in (1, 2):
                        values = np.array(
                            [
                                row[f"{prefix}spline_y_{knot}_d{dimension}"]
                                for knot in range(count)
                            ]
                        )
                        self.assertTrue(np.all(np.diff(values) <= 1e-7))
    def test_tiny_training_and_saved_evaluator_replay(self):
        tables = spline_tables()
        with tempfile.TemporaryDirectory() as tmp:
            args = parse_train_args(
                ["--steps", "2", "--dimensions", "1", "--output-dir", tmp]
            )
            summary = run_experiment(args, tables=tables)
            self.assertEqual(summary["model"], "dd-linear-spline")
            tossups = pd.read_csv(Path(tmp) / "tossups.csv")
            self.assertIn("hazard_spline_y_0_d1", tossups)
            row = tossups.set_index("tossup_id").iloc[0]
            curve = _saved_difficulty_curve(row, np.array([0.0, 0.5, 1.0]))
            self.assertEqual(curve.shape, (3,))
            self.assertTrue(np.isfinite(curve).all())

    def test_frozen_replay_matches_native_predictions(self):
        tables = spline_tables()
        observations = build_tossup_observations(tables)
        data = build_spline_tensors(observations, tables["tossups"])
        torch.manual_seed(7)
        dimensions = 2
        posterior = {
            "theta": torch.randn(len(data["player_ids"]), dimensions),
            "c": torch.randn(len(data["player_ids"])),
            "r_correct": torch.rand(len(data["tossup_ids"]), dimensions) + 0.2,
            "r_hazard": torch.rand(len(data["tossup_ids"]), dimensions) + 0.2,
            "spline_y_correct": torch.randn(data["n_spline_knots"], dimensions),
            "spline_y_hazard": torch.randn(data["n_spline_knots"], dimensions),
        }
        native = spline.posterior_row_predictions(data, posterior)
        with tempfile.TemporaryDirectory() as tmp:
            train = Path(tmp) / "train"
            held = Path(tmp) / "held"
            train.mkdir()
            save_spline_parameters(train, data, posterior)
            (train / "summary.json").write_text(
                json.dumps({"model": "dd-linear-spline"}), encoding="utf-8"
            )
            args = parse_frozen_args(
                [
                    "tossup",
                    "--split",
                    "all",
                    "--train-pyramidal",
                    str(train),
                    "--dimensions",
                    str(dimensions),
                    "--output-dir",
                    str(held),
                ]
            )
            with patch("holdout.frozen_predict.load_hf_tables", return_value=tables):
                frozen_predict_tossups(args)
            saved = pd.read_csv(held / "tossup_predictions.csv")
            for expected, column in zip(
                native,
                ("predicted_correct", "predicted_hazard", "predicted_survival"),
            ):
                np.testing.assert_allclose(
                    expected.detach().numpy(), saved[column], rtol=1e-6
                )


if __name__ == "__main__":
    unittest.main()
