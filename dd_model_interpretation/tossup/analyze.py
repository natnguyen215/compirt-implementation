"""Name the DD tossup model's skill axes from its hazard and correctness relevance.

Reads the full-season in-sample DD-Bernstein tossup fit and trains nothing. Each
tossup has two simplex relevance vectors over the shared player skills: `r_k`
(correctness) and `hazard_r_k` (buzz timing). Prints every number quoted in
README.md and writes the plotted table to `data/`.

Run from the repository root:

    .venv/bin/python -B -m dd_model_interpretation.tossup.analyze
"""

from pathlib import Path

import numpy as np
import pandas as pd

from dd_model_interpretation.shared.common import TOSSUP_FIT, eta2_with_null, tossup_metadata

OUT = Path(__file__).parent / "data"
HAZARD = ["hazard_r_1", "hazard_r_2", "hazard_r_3"]
CORRECT = ["r_1", "r_2", "r_3"]
rng = np.random.default_rng(0)
pd.set_option("display.width", 220)


def main():
    OUT.mkdir(exist_ok=True)
    tossups = pd.read_csv(TOSSUP_FIT / "tossups.csv")[["tossup_id"] + CORRECT + HAZARD]
    tossups = tossups.merge(tossup_metadata(), on="tossup_id", validate="1:1")
    theta = pd.read_csv(TOSSUP_FIT / "players.csv")[["theta_1", "theta_2", "theta_3"]]

    print(f"# Tossup relevance axes: {TOSSUP_FIT}")
    print(f"tossups {len(tossups)}, players {len(theta)}; player skill correlation:")
    print(theta.corr().round(2))

    print("\n## Share of tossup-level variance explained (eta^2, permutation-null mean in parentheses)\n")
    rows = [{"relevance": column, **{g: eta2_with_null(tossups[column], tossups[g], rng) for g in ("category", "subcategory")}}
            for column in HAZARD + CORRECT]
    print(pd.DataFrame(rows).to_string(index=False))

    by_sub = tossups.groupby("subcategory")[HAZARD + CORRECT].mean().assign(n=tossups.groupby("subcategory").size())
    by_sub = by_sub[by_sub.n >= 15].sort_values("hazard_r_1", ascending=False)
    print("\n## Mean relevance by subcategory (>= 15 tossups), sorted by hazard axis 1\n")
    print(by_sub.round(2).to_string())
    print("\nrange of subcategory means: hazard",
          [f"{by_sub[c].min():.2f}-{by_sub[c].max():.2f}" for c in HAZARD],
          "correctness", [f"{by_sub[c].min():.2f}-{by_sub[c].max():.2f}" for c in CORRECT])
    by_sub.to_csv(OUT / "subcategory_relevance.csv")


if __name__ == "__main__":
    main()
