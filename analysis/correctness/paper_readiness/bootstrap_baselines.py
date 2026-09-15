"""Conditional paired cluster-bootstrap diagnostic for saved correctness scores."""

import json
from pathlib import Path

import numpy as np
import pandas as pd


OUTPUT = Path("results/compirt/holdout/common/paper-readiness-tossups")
p = pd.read_csv(OUTPUT / "correctness_predictions.csv")
y = p.y.to_numpy()
simple = p.player_item_position_terminal.clip(1e-12, 1 - 1e-12).to_numpy()
comp = p.saved_simplex_332.clip(1e-12, 1 - 1e-12).to_numpy()
p["gain"] = -(y * np.log(simple) + (1 - y) * np.log(1 - simple)) + (
    y * np.log(comp) + (1 - y) * np.log(1 - comp)
)
p["tossup_id"] = [e[len(g) + 2:] for e, g in zip(p.event_id, p.game_id)]
rng = np.random.default_rng(20260906)
out = {"pooled_n": len(p), "pooled_log_loss_gain": float(p.gain.mean())}
for col in ["game_id", "tossup_id"]:
    q = p.groupby(col).gain.agg(["sum", "count"]).to_numpy()
    boot = []
    for _ in range(2000):
        take = rng.integers(len(q), size=len(q))
        z = q[take].sum(axis=0)
        boot.append(z[0] / z[1])
    out[col] = {
        "clusters": len(q),
        "conditional_percentile_95_interval": np.quantile(boot, [.025, .975]).tolist(),
    }
(OUTPUT / "baseline_uncertainty.json").write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2))
