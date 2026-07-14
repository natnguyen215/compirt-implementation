"""Command-level tests for opt-in Scenario C holdout orchestration."""

from __future__ import annotations

import os
import unittest
from unittest.mock import patch

from run_scripts import run_compirt_holdout as runner


def run_with_environment(**values):
    commands = []
    environment = {
        "COMPIRT_LOG_ACTIVE": "1",
        "ROOT": "/tmp/scenario-c-runner-test",
        "PYTHON": ".venv/bin/python",
        "PREDICT_BUZZ_POSITIONS": "0",
        **{key: str(value) for key, value in values.items()},
    }
    with patch.dict(os.environ, environment, clear=True), patch.object(
        runner, "run", side_effect=lambda command: commands.append([str(x) for x in command])
    ):
        runner.main()
    return [" ".join(command) for command in commands]


class ScenarioCRunnerTests(unittest.TestCase):
    def test_disabled_is_a_noop_for_existing_holdout_pipeline(self):
        commands = run_with_environment(MODEL="baseline", RUN_C1_C4="0")
        text = "\n".join(commands)

        self.assertNotIn("run_scripts.run_scenario_c", text)
        self.assertNotIn("/train/compositional", text)
        self.assertNotIn("/train/synergy", text)

    def test_enabled_adds_historical_branches_and_scenario_runner(self):
        commands = run_with_environment(
            MODEL="baseline",
            RUN_C1_C4="1",
            C1_C4_MIN_CROSS_TEAM_GAMES="7",
        )
        text = "\n".join(commands)

        self.assertIn("/train/compositional", text)
        self.assertIn("/train/synergy", text)
        self.assertIn("--save-synergy-details", text)
        self.assertIn("run_scripts.run_scenario_c", text)
        self.assertIn("--min-cross-team-games 7", text)
        self.assertIn("/holdout/c1-c4/evaluation", text)

    def test_all_supported_model_families_use_shared_scenario_runner(self):
        for model in ("baseline", "multidim", "tfidf", "tfidf_multidim"):
            with self.subTest(model=model):
                commands = run_with_environment(MODEL=model, RUN_C1_C4="1")
                text = "\n".join(commands)
                self.assertIn("run_scripts.run_scenario_c", text)
                self.assertIn("/train/compositional", text)
                self.assertIn("/train/synergy", text)

    def test_topic_family_rejects_scenario_c(self):
        with patch.dict(
            os.environ,
            {
                "COMPIRT_LOG_ACTIVE": "1",
                "MODEL": "topic",
                "RUN_C1_C4": "1",
            },
            clear=True,
        ):
            with self.assertRaisesRegex(SystemExit, "supports baseline"):
                runner.main()


if __name__ == "__main__":
    unittest.main()
