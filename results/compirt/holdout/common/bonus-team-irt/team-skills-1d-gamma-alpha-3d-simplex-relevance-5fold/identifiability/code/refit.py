"""Refit Team IRT 3D on fold 0's training games under other seeds or priors.

Identical data, so any change in per-axis parameters comes from the seed or the
prior, not from the responses. Writes identifiability/refits/<name>.npz.
Run from the repository root:

    CUDA_VISIBLE_DEVICES=1 .venv/bin/python -B results/compirt/holdout/common/bonus-team-irt/team-skills-1d-gamma-alpha-3d-simplex-relevance-5fold/identifiability/code/refit.py
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[8]))

import numpy as np
import pyro
import pyro.distributions as dist
import torch

from analysis.bonus_team_irt.model import observations, part_logits, team_irt, training_tensors
from compirt_data import load_hf_tables
from compirt_eval.scenario_b_bonuses.metrics import bonus_parts_with_difficulty
from holdout.game_splits import GameHoldoutSpec, game_holdout_masks
from utils.training import fit_svi

STUDY = Path(__file__).resolve().parents[1]
RUN = STUDY.parent
SHIFT = (1.0, 0.0, -1.0)


def shifted_prior_team_irt(data, dimensions):
    """team_irt 3D with beta_bk ~ Normal(SHIFT_k, 1) instead of Normal(0, 1)."""
    one = data["y"].new_tensor(1.0)
    with pyro.plate("teams", len(data["team_ids"])):
        theta = pyro.sample("theta", dist.Normal(0 * one, one).expand([dimensions]).to_event(1))
    with pyro.plate("parts", len(data["part_ids"])):
        r = pyro.sample("r", dist.Dirichlet(one.expand([dimensions])))
        beta = pyro.sample("beta", dist.Normal(data["y"].new_tensor(SHIFT), one).to_event(1))
    logits = part_logits({"theta": theta, "r": r, "beta": beta}, data["team"], data["part"])
    with pyro.plate("observations", len(data["y"])):
        pyro.sample("correct", dist.Bernoulli(logits=logits), obs=data["y"])


def main():
    config = json.loads((RUN / "configuration.json").read_text())
    tables = load_hf_tables(config["data_dir"], config["split"])
    frame = bonus_parts_with_difficulty(observations(tables), tables["bonuses"])  # as in run.py
    mask = game_holdout_masks(tables, GameHoldoutSpec(config["split"], "test", config["n_folds"], 0, config["split_seed"]))
    train = frame[~frame.game_id.isin(tables["games"].loc[mask, "game_id"])]
    reference = json.loads((RUN / "fold_0/team_irt_3d/ids.json").read_text())
    output = STUDY / "refits"
    output.mkdir(exist_ok=True)
    for name, model, seed in (("seed_43", team_irt, 43), ("seed_44", team_irt, 44),
                              ("shifted_beta_prior_seed_42", shifted_prior_team_irt, 42)):
        if (output / f"{name}.npz").exists():
            continue
        pyro.set_rng_seed(seed)
        data = training_tensors(train, "cuda")
        if data["team_ids"] != reference["team_ids"] or data["part_ids"] != reference["part_ids"]:
            raise ValueError("Refit entities differ from the saved fold-0 fit")
        medians, _, losses = fit_svi(model, model_kwargs={"data": data, "dimensions": 3},
                                     n_steps=config["steps"], lr=config["lr"])
        np.savez_compressed(output / f"{name}.npz", losses=np.asarray(losses),
                            **{key: value.detach().cpu().numpy() for key, value in medians.items()})


if __name__ == "__main__":
    torch.set_num_threads(1)
    main()
