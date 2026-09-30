"""Compare fold-0 phi-psi 1D and 3D bonus runs with the dot-product references.

Reads saved predictions from '<root>/dim_1' and '<root>/dim_3', checks that
every arm scores the same held-out rows, and writes comparison.csv and
checks.json to '<root>/aggregate'. Run from the repository root.
"""

import argparse
import hashlib
import json
from pathlib import Path
import sys

REPO = next(p for p in Path(__file__).resolve().parents if (p / "compirt_data.py").exists())
sys.path.insert(0, str(REPO))

import numpy as np
import pandas as pd

from compirt_eval.scenario_b_bonuses.metrics import bonus_metrics, bonus_parts_with_difficulty
from compirt_eval.scenario_b_bonuses.outcomes import write_bonus_outcomes
from compirt_eval.scenario_b_bonuses.folds import audit_predictions, evaluation_tables


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True,
                        help="study directory containing dim_1 and dim_3 saved runs")
    root = parser.parse_args().root.resolve()
    reference = root.parent / "no-synergy-and-dot-additive-1d"
    config = json.loads((root / "dim_1/configuration.json").read_text())
    source = Path(config["stage1_root"])
    sources = config["sources"]
    inputs = {}
    for dim in (1, 3):
        run = root / f"dim_{dim}"
        train = run / "fold_0/train/synergy"
        summary = json.loads((train / "summary.json").read_text())
        assert summary["synergy_form"] == "phi-psi"
        assert summary["synergy_dimensions"] == dim
        assert summary["split"] == sources["0"]["train_split"]
        assert summary["finite_losses"] and not summary["dropped_rows_unknown_roster"]
        for name in ("summary.json", "bonus_parts.csv", "tau.txt", "player_synergy_profiles.csv", "bonus_part_predictions.csv"):
            path = train / name
            inputs[str(path.relative_to(REPO))] = hashlib.sha256(path.read_bytes()).hexdigest()

    tables = evaluation_tables(config, [0])
    stage1_games = pd.read_csv(source / "fold_0/train/pyramidal/tossup_predictions.csv", usecols=["game_id"])["game_id"]
    output = root / "aggregate"
    output.mkdir(exist_ok=True)
    rows, audits = [], {}
    # Every arm must score exactly the first arm's rows.
    matched = None
    arms = [
        ("DD no synergy", reference / "fold_0", "compositional"),
        ("DD dot synergy 1D", reference / "fold_0", "synergy"),
        ("DD phi-psi 1D", root / "dim_1/fold_0", "synergy"),
        ("DD phi-psi 3D", root / "dim_3/fold_0", "synergy"),
    ]
    for label, fold, arm in arms:
        train, test = fold / "train" / arm, fold / "holdout" / arm
        training = pd.read_csv(train / "bonus_part_predictions.csv")
        parts = pd.read_csv(test / "bonus_part_predictions.csv")
        teams = pd.read_csv(test / "team_predictions.csv")
        audits[label] = audit_predictions(training, parts, stage1_games)
        columns = ["observation_id", "response_id", "game_id", "team_id", "bonus_part_id", "correct", "player_ids"]
        population = parts[columns].sort_values("observation_id").reset_index(drop=True)
        if matched is None:
            matched = population
        else:
            pd.testing.assert_frame_equal(matched, population)
        parts = bonus_parts_with_difficulty(parts, tables["bonuses"])
        metrics = bonus_metrics(parts, teams)
        metrics.update(write_bonus_outcomes(parts, tables, output / label.lower().replace(" ", "_")))
        assert np.isfinite([metrics[k] for k in ("auc", "log_loss", "ppb_mae")]).all()
        rows.append(dict(model=label, fold=0, parts=len(parts), responses=parts.response_id.nunique(),
                         games=parts.game_id.nunique(), teams=parts.team_id.nunique(), **metrics))
        for path in (train / "summary.json", test / "bonus_part_predictions.csv"):
            inputs[str(path.relative_to(REPO))] = hashlib.sha256(path.read_bytes()).hexdigest()
    pd.DataFrame(rows).to_csv(output / "comparison.csv", index=False)
    (output / "checks.json").write_text(json.dumps(
        dict(common_population=True, arms=audits, source=sources, input_sha256=inputs),
        indent=2,
    ) + "\n")
    print(pd.DataFrame(rows)[["model", "parts", "auc", "log_loss", "part_accuracy", "exact_acc", "ppb_mae"]].to_string(index=False))


if __name__ == "__main__":
    main()
