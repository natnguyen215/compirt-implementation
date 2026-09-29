"""Inputs shared by the bonus and tossup interpretation studies.

Both read the full-season in-sample DD-Bernstein fits: the tossup stage in
`dd/pyramidal` and the multidimensional-difficulty bonus stage that holds its
player skills fixed. Nothing here trains a model.
"""

import re
from pathlib import Path

import numpy as np
import pandas as pd
from datasets import load_from_disk

SEASON = Path("results/compirt/in_sample/common/bonus-difficulty-season-2024-25/dd")
TOSSUP_FIT = SEASON / "pyramidal"
BONUS_FIT = SEASON / "multidim-difficulty-synergy"   # LSE, additive dot synergy 1D
AXES = ["w1", "w2", "w3"]
# Source category spellings vary by set; merge them into one label each.
CATEGORY = {
    "Painting &amp; Sculpture": "Fine Arts", "Painting/Sculpture": "Fine Arts",
    "Any History": "History", "Pop Culture": "Popular Culture",
    "Geography": "Geography/CE", "Current Events": "Geography/CE",
    "Geography/Current Events": "Geography/CE", "Current Events/Geography": "Geography/CE",
    "World/Other Literature&gt;": "Literature", "": "Unknown",
}


def category(name):
    return CATEGORY.get(name, name)


def bonus_part_metadata():
    """One row per bonus part: set, packet, subject, declared difficulty, and text."""
    rows = []
    for bonus in load_from_disk("data/hf/quizbowl-irt/bonuses/all").to_pandas().itertuples():
        for index, part in enumerate(bonus.parts, start=1):
            rows.append({
                "bonus_part_id": f"{bonus.bonus_id}::part-{index}",
                "bonus_id": bonus.bonus_id,
                "set": bonus.question_set_event_id,
                "packet": f"{bonus.question_set_event_id}::p{bonus.packet}",
                "category": category(bonus.category),
                "subcategory": f"{category(bonus.category)}/{bonus.subcategory}",
                "label": part["difficulty"],
                "answer": re.sub(r"<[^>]+>", "", part["answer"]).split("[")[0].strip(),
                "document": re.sub(r"<[^>]+>", " ", f"{bonus.leadin} {part['text']} {part['answer']}"),
            })
    return pd.DataFrame(rows)


def tossup_metadata():
    meta = load_from_disk("data/hf/quizbowl-irt/tossups/all").to_pandas()
    meta["category"] = meta.category.map(category)
    meta["subcategory"] = meta.category + "/" + meta.subcategory
    return meta[["tossup_id", "category", "subcategory"]]


def bonus_part_table(fit, meta):
    """Per-part relevance r and per-dimension difficulty d (saved as beta_k).

    The likelihood sees only r and r . d, so the table also carries the
    identified reparameterization: direction w = r / sum(r), discrimination
    sum(r), and location loc = r . d / sum(r) on the team-skill scale.
    """
    saved = pd.read_csv(fit / "bonus_parts.csv")
    r = saved[["r_1", "r_2", "r_3"]].to_numpy()
    d = saved[["beta_1", "beta_2", "beta_3"]].to_numpy()
    parts = saved[["bonus_part_id"]].copy()
    parts[["r1", "r2", "r3"]] = r
    parts[["d1", "d2", "d3"]] = d
    parts[AXES] = r / r.sum(1, keepdims=True)
    parts["rsum"] = r.sum(1)
    parts["rd"] = (r * d).sum(1)
    parts["loc"] = parts.rd / parts.rsum
    return parts.merge(meta, on="bonus_part_id", how="left", validate="1:1"), r, d


def eta2(y, groups):
    """Share of variance in y explained by group means."""
    y = np.asarray(y, float)
    stats = pd.Series(y).groupby(np.asarray(groups)).agg(["size", "mean"])
    return (stats["size"] * (stats["mean"] - y.mean()) ** 2).sum() / ((y - y.mean()) ** 2).sum()


def eta2_with_null(y, groups, rng, reps=200):
    """eta^2 with the mean over label permutations as a chance baseline."""
    null = [eta2(rng.permutation(np.asarray(y)), groups) for _ in range(reps)]
    return f"{eta2(y, groups):.3f} (null {np.mean(null):.3f})"
