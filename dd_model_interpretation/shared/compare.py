"""Compare bonus relevance direction with tossup relevance, per subcategory.

The bonus model scores parts on the tossup model's fixed player-skill axes, so
this checks whether a subject's bonus direction w = r / sum(r) follows the
tossup's hazard or correctness relevance. Reads saved fits only, prints every
number quoted in the parent README.md, and writes supporting tables to data/.

Run from the repository root:

    .venv/bin/python -B -m dd_model_interpretation.shared.compare
"""

from pathlib import Path

import pandas as pd
from scipy.stats import spearmanr

from dd_model_interpretation.shared.common import (
    BONUS_FIT, TOSSUP_FIT, bonus_part_metadata, bonus_part_table, tossup_metadata,
)

HERE = Path(__file__).parent
DATA = HERE / "data"
HAZARD = ["hazard_r_1", "hazard_r_2", "hazard_r_3"]
CORRECT = ["r_1", "r_2", "r_3"]


def subcategory_table():
    tossups = pd.read_csv(TOSSUP_FIT / "tossups.csv")[["tossup_id"] + CORRECT + HAZARD]
    tossups = tossups.merge(tossup_metadata(), on="tossup_id", validate="1:1")
    by_sub = tossups.groupby("subcategory")[HAZARD + CORRECT].mean().assign(n=tossups.groupby("subcategory").size())
    parts, _, _ = bonus_part_table(BONUS_FIT, bonus_part_metadata())
    bonus = (parts.groupby("subcategory")[["w1", "w2", "w3"]].mean().rename(columns=lambda c: f"bonus_{c}")
             .assign(bonus_parts=parts.groupby("subcategory").size()))
    return by_sub[by_sub.n >= 15].join(bonus, how="inner")


def main():
    DATA.mkdir(exist_ok=True)
    table = subcategory_table()
    print(f"# Bonus direction vs tossup relevance: {BONUS_FIT} and {TOSSUP_FIT}")
    print(f"subcategories with >= 15 tossups and bonus parts: {len(table)}")
    for source, columns in (("hazard", HAZARD), ("correctness", CORRECT)):
        rho = [spearmanr(table[c], table[f"bonus_w{k}"])[0] for k, c in enumerate(columns, start=1)]
        print(f"Spearman, tossup {source} relevance vs bonus w_k:", [round(float(x), 2) for x in rho])
    table.to_csv(DATA / "subcategory_axes.csv")


if __name__ == "__main__":
    main()
