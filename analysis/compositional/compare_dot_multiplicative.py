"""Compare the multiplicative dot 1D bonus run with the no-synergy and additive dot 1D arms.

Checks that both five-fold runs score the same held-out rows, then writes
comparison.csv, paired_fold_deltas.csv, and comparison_checks.json to the
multiplicative run's aggregate/ directory. Reads saved predictions only.
"""

import hashlib
import json
from pathlib import Path

import pandas as pd


def main():
    root = (Path(__file__).resolve().parents[2]
            / "results/compirt/holdout/double-difficulty/compositional"
            / "dot-multiplicative-1d")
    reference = root.parent / "no-synergy-and-dot-additive-1d"
    # Rows match when these identifying columns and labels agree.
    keys = ["observation_id", "response_id", "game_id", "team_id", "bonus_part_id", "correct", "player_ids"]
    counts, hashes = [], {}
    for fold in range(5):
        target = root / f"fold_{fold}/holdout/synergy/bonus_part_predictions.csv"
        current = pd.read_csv(target)[keys].sort_values("observation_id").reset_index(drop=True)
        for arm in ("compositional", "synergy"):
            path = reference / f"fold_{fold}/holdout/{arm}/bonus_part_predictions.csv"
            baseline = pd.read_csv(path)[keys].sort_values("observation_id").reset_index(drop=True)
            pd.testing.assert_frame_equal(current, baseline)
            hashes[str(path)] = hashlib.sha256(path.read_bytes()).hexdigest()
        hashes[str(target)] = hashlib.sha256(target.read_bytes()).hexdigest()
        # The fold passed the runner's audit and trained the intended synergy.
        check = json.loads((root / f"fold_{fold}/synergy_checks.json").read_text())
        assert check["disjoint_games"] and check["finite_probabilities"]
        assert not check["train_dropped_rows_unknown_roster"] and not check["test_dropped_rows_unknown_roster"]
        train = json.loads((root / f"fold_{fold}/train/synergy/summary.json").read_text())
        assert train["finite_losses"] and train["synergy_link"] == "multiplicative"
        assert train["synergy_form"] == "dot" and train["synergy_dimensions"] == 1
        counts.append(dict(fold=fold, parts=len(current), common_labels_and_lineups=True, **check))
    base = pd.read_csv(reference / "aggregate/pooled.csv")
    new = pd.read_csv(root / "aggregate/pooled.csv")
    base["model"] = base.arm.map({"compositional": "DD no synergy", "synergy": "DD additive dot 1D"})
    new["model"] = "DD multiplicative dot 1D"
    metrics = ["folds", "parts", "responses", "games", "teams", "auc", "log_loss", "part_accuracy", "exact_acc", "ppb_mae"]
    pd.concat([base, new], ignore_index=True)[["model", *metrics]].to_csv(root / "aggregate/comparison.csv", index=False)
    # Paired per-fold differences against both reference arms.
    old_folds = pd.read_csv(reference / "aggregate/per_fold.csv")
    new_folds = pd.read_csv(root / "aggregate/per_fold.csv")
    comparisons = []
    for row in new_folds.itertuples(index=False):
        for arm in ("compositional", "synergy"):
            other = old_folds[(old_folds.fold == row.fold) & (old_folds.arm == arm)].iloc[0]
            comparisons.append(dict(fold=row.fold, reference=arm,
                                    log_loss_delta=row.log_loss - other.log_loss,
                                    ppb_mae_delta=row.ppb_mae - other.ppb_mae))
    pd.DataFrame(comparisons).to_csv(root / "aggregate/paired_fold_deltas.csv", index=False)
    (root / "aggregate/comparison_checks.json").write_text(json.dumps(dict(folds=counts, input_sha256=hashes), indent=2) + "\n")
    print(pd.read_csv(root / "aggregate/comparison.csv").to_string(index=False))
    print(pd.DataFrame(comparisons).to_string(index=False))


if __name__ == "__main__":
    main()
