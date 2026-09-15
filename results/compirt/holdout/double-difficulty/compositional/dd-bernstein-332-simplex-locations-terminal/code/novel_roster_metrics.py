"""Held-out bonus metrics split by whether the exact team+roster was seen in training.

Replays saved bonus_part_predictions.csv files; nothing is refit. Run from the
repository root:

    .venv/bin/python results/compirt/holdout/double-difficulty/compositional/dd-bernstein-332-simplex-locations-terminal/code/novel_roster_metrics.py
"""

import ast
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.metrics import log_loss, roc_auc_score

HOLDOUT = Path("results/compirt/holdout")
RUN = HOLDOUT / "double-difficulty/compositional/dd-bernstein-332-simplex-locations-terminal"
RUNS = {
    "Multidim": HOLDOUT / "multidim/multidim-all2024-gameinfill-5fold",
    "DD-Bernstein": RUN,
}
OUTPUT = RUN / "aggregate/novel_roster_metrics.csv"


def roster_key(frame):
    players = frame["player_ids"].map(lambda s: frozenset(ast.literal_eval(s)))
    return list(zip(frame["team_id"], players)), players


rows = []
familiar_counts = []
for model, run in RUNS.items():
    for fold in range(5):
        train = pd.read_csv(run / f"fold_{fold}/train/synergy/bonus_part_predictions.csv")
        train_keys, train_players = roster_key(train)
        seen_rosters = set(train_keys)
        seen_players = set().union(*train_players)

        for arm in ["compositional", "synergy"]:
            test = pd.read_csv(run / f"fold_{fold}/holdout/{arm}/bonus_part_predictions.csv")
            keys, players = roster_key(test)
            familiar = np.array([k in seen_rosters for k in keys])
            all_players_seen = players.map(lambda p: p <= seen_players).to_numpy()
            test["group"] = np.where(
                familiar,
                "familiar roster",
                np.where(all_players_seen, "new roster, known players", "new roster, unseen player"),
            )
            test["model"], test["arm"], test["fold"] = model, arm, fold
            rows.append(test)
            if arm == "synergy":
                familiar_counts.append(
                    (model, fold, test["response_id"].nunique(),
                     test.loc[familiar, "response_id"].nunique())
                )

data = pd.concat(rows, ignore_index=True)
# Familiar counts should match aggregate/roster_familiarity.json.
print(pd.DataFrame(familiar_counts, columns=["model", "fold", "responses", "familiar"]))


def metrics(g):
    p = g["predicted_correct"].clip(1e-7, 1 - 1e-7).to_numpy()
    y = g["correct"].to_numpy()
    hit = (p >= 0.5) == (y == 1)
    exact = pd.Series(hit).groupby(g["response_id"].to_numpy()).all()
    return pd.Series({
        "bonuses": g["response_id"].nunique(),
        "part_acc": hit.mean(),
        "exact_acc": exact.mean(),
        "auc": roc_auc_score(y, p),
        "log_loss": log_loss(y, p),
        "pred_minus_obs": p.mean() - y.mean(),
        "mean_synergy": g["synergy_contribution"].mean(),
    })


summary = (
    data.groupby(["model", "group", "arm"])
    .apply(metrics, include_groups=False)
    .reset_index()
)
summary.to_csv(OUTPUT, index=False)
pd.set_option("display.width", 200)
print(summary.round(4).to_string(index=False))
