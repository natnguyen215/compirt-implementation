"""Check this run's reference metrics against the previously published metrics."""

import json
from pathlib import Path

import numpy as np
import pandas as pd

from compirt_eval.common.metrics import classification_metrics


def main():
    root = Path(__file__).resolve().parents[1]
    repo = root.parents[5]
    previous = repo / "results/compirt/holdout/double-difficulty/compositional/dd-bernstein-332-simplex-locations-terminal"
    comparison = json.loads((previous / "aggregate/comparison_with_multidim.json").read_text())
    current = pd.read_csv(root / "aggregate/metrics.csv").set_index("model")
    rows = []
    for original in comparison["results"]:
        family, arm = original["model"], original["arm"]
        name = f"{'dd' if family == 'DD-Bernstein' else 'multidim'}_{arm}"
        source = repo / comparison["sources"][family]
        parts = pd.concat([
            pd.read_csv(source / f"fold_{fold}/holdout/{arm}/bonus_part_predictions.csv",
                        usecols=["observation_id", "team_id", "correct", "predicted_correct"])
            for fold in range(5)
        ], ignore_index=True)
        metrics = classification_metrics(parts.correct, parts.predicted_correct)
        team_means = parts.groupby("team_id")[["correct", "predicted_correct"]].mean()
        metrics["ppb_mae"] = float(30 * (team_means.correct - team_means.predicted_correct).abs().mean())
        for metric in ("auc", "log_loss", "accuracy", "brier", "ppb_mae"):
            np.testing.assert_allclose(metrics[metric], original[metric], rtol=0, atol=1e-6)
            current_key = "part_accuracy" if metric == "accuracy" else metric
            rows.append({"model": name, "metric": current_key,
                         "original_report": original[metric], "recomputed_original_population": metrics[metric],
                         "matched_population": current.loc[name, current_key],
                         "population_change": current.loc[name, current_key] - metrics[metric]})
        old_margins = pd.read_csv(previous / f"aggregate/bonus_metrics/{family}/{arm}/bonus_game_margin_predictions.csv")
        new_margins = pd.read_csv(root / f"aggregate/{name}/game_margins.csv")
        shared = new_margins.merge(old_margins, on="game_id", suffixes=("_new", "_old"), validate="one_to_one")
        assert len(shared) == len(new_margins) == 2330
        for column in ("observed_bonus_margin", "predicted_bonus_margin", "absolute_bonus_margin_error"):
            np.testing.assert_allclose(shared[f"{column}_new"], shared[f"{column}_old"], rtol=0, atol=1e-10)
        rows.append({"model": name, "metric": "bonus_game_margin_mae",
                     "original_report": old_margins.absolute_bonus_margin_error.mean(),
                     "recomputed_original_population": old_margins.absolute_bonus_margin_error.mean(),
                     "matched_population": new_margins.absolute_bonus_margin_error.mean(),
                     "population_change": new_margins.absolute_bonus_margin_error.mean() - old_margins.absolute_bonus_margin_error.mean()})
    audit = pd.DataFrame(rows)
    audit.to_csv(root / "aggregate/existing_metrics_parity.csv", index=False)
    print(audit.to_string(index=False))
    print("PASS: original metrics reproduced; all matched per-game reference margins unchanged.")


if __name__ == "__main__":
    main()
