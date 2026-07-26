"""Build informative player priors for the held-out temporal evaluation.

The paper's primary split trains on history (2024) and predicts the future
(2025). Question parameters are co-estimated transductively on the test data; the
player priors are the part that carries information across the split (Section 4.2
and Appendix B):

* returning players keep their training-set posterior as the 2025 prior, and
* new players draw a tier-conditioned population prior 'theta ~ N(mu_tier,
  Sigma_tier)' whose moments come from the training-set players in the same
  tournament tier. 'new_player_prior="flat"' selects the paper's N(0, I)
  ablation instead.

The output of :func:`build_prior_tensors` is the four optional 'data' keys the
Stage-1 models read ('theta_prior_loc/scale', 'c_prior_loc/scale'); when those
keys are absent the models fall back to the standard N(0, I)/N(0, 1) priors.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
import torch


# Difficulty ordering for tiers. A player who competes at several tiers is
# represented by the hardest tier they reached.
TIER_ORDER = ["fall", "winter", "regionals", "nationals"]
_MIN_SCALE = 1e-3


def player_tier_map(tables):
    """Map each player_id to a single tier from the split's 'teams' rows.

    A player can appear at multiple tournaments; we assign the hardest tier they
    reached according to 'TIER_ORDER'. Players attend each tier at most once in
    this dataset, making the result the modal tier as well. Difficulty ordering
    also resolves repeated appearances deterministically.
    """
    tier_by_tournament = dict(
        zip(tables["tournaments"]["tournament_id"], tables["tournaments"]["tier"])
    )
    hardest_tier: dict[str, str] = {}
    for _, team in tables["teams"].iterrows():
        tier = tier_by_tournament.get(team["tournament_id"])
        if tier is None:
            continue
        for player_id in team["player_ids"]:
            player_id = str(player_id)
            current = hardest_tier.get(player_id)
            if current is None or _tier_rank(tier) > _tier_rank(current):
                hardest_tier[player_id] = tier
    return hardest_tier


def _tier_rank(tier):
    """Return a tier's difficulty ordering (higher is harder), or -1 if unknown."""
    return TIER_ORDER.index(tier) if tier in TIER_ORDER else -1


def _theta_dimensions(posterior):
    """Count skill dimensions from a posterior's 'theta_k_loc' columns."""
    return sum(
        1
        for column in posterior.columns
        if column.startswith("theta_") and column.endswith("_loc")
    )


def load_train_posterior(path):
    """Load a 'player_posterior.csv' keyed by player_id."""
    posterior = pd.read_csv(path)
    posterior["player_id"] = posterior["player_id"].astype(str)
    return posterior.set_index("player_id")


def estimate_tier_priors(train_posterior):
    """Return per-tier (mu, sigma) over training players' posterior theta means.

    Training players are grouped by the 'tier' column written into
    'player_posterior.csv' at training time. 'Sigma_tier' is the diagonal
    population spread of the posterior means in a tier; a global fallback covers
    tiers with too few training players (or a posterior lacking tier labels).
    """
    n_dimensions = _theta_dimensions(train_posterior)
    loc_columns = [f"theta_{k + 1}_loc" for k in range(n_dimensions)]
    locs = train_posterior[loc_columns].to_numpy(dtype=float)
    if "tier" in train_posterior.columns:
        tiers = train_posterior["tier"].to_numpy()
    else:
        tiers = np.array([None] * len(train_posterior))

    global_mu = locs.mean(axis=0)
    global_sigma = np.clip(locs.std(axis=0), _MIN_SCALE, None)
    priors = {"__global__": (global_mu, global_sigma)}
    for tier in {tier for tier in tiers if tier is not None and not pd.isna(tier)}:
        rows = locs[tiers == tier]
        if len(rows) < 2:
            continue
        priors[tier] = (
            rows.mean(axis=0),
            np.clip(rows.std(axis=0), _MIN_SCALE, None),
        )
    return priors


def build_prior_tensors(
    player_ids,
    train_posterior,
    tier_priors,
    test_tier_map,
    device="cpu",
    new_player_prior="tier",
):
    """Assemble the per-player prior tensors aligned to 'player_ids' order.

    Returns the four 'data' keys read by the Stage-1 models plus a small
    'summary' dict (returning vs. new counts) for logging.
    """
    n_dimensions = _theta_dimensions(train_posterior)
    loc_columns = [f"theta_{k + 1}_loc" for k in range(n_dimensions)]
    scale_columns = [f"theta_{k + 1}_scale" for k in range(n_dimensions)]
    global_mu, global_sigma = tier_priors["__global__"]

    theta_loc = np.zeros((len(player_ids), n_dimensions))
    theta_scale = np.ones((len(player_ids), n_dimensions))
    c_loc = np.zeros(len(player_ids))
    c_scale = np.ones(len(player_ids))
    returning = 0
    for row, player_id in enumerate(player_ids):
        player_id = str(player_id)
        if player_id in train_posterior.index:
            # Returning player: prior = training posterior (loc + scale).
            record = train_posterior.loc[player_id]
            theta_loc[row] = record[loc_columns].to_numpy(dtype=float)
            theta_scale[row] = np.clip(
                record[scale_columns].to_numpy(dtype=float), _MIN_SCALE, None
            )
            c_loc[row] = float(record["c_loc"])
            c_scale[row] = max(float(record["c_scale"]), _MIN_SCALE)
            returning += 1
        elif new_player_prior == "flat":
            # Ablation: flat N(0, I) on new players (defaults already set).
            continue
        else:
            # New player: tier-conditioned population prior.
            tier = test_tier_map.get(player_id)
            mu, sigma = tier_priors.get(tier, (global_mu, global_sigma))
            theta_loc[row] = mu
            theta_scale[row] = sigma

    def to_tensor(array):
        return torch.tensor(array, dtype=torch.float32, device=device)

    priors = {
        "theta_prior_loc": to_tensor(theta_loc),
        "theta_prior_scale": to_tensor(theta_scale),
        "c_prior_loc": to_tensor(c_loc),
        "c_prior_scale": to_tensor(c_scale),
    }
    summary = {
        "players": len(player_ids),
        "returning": returning,
        "new": len(player_ids) - returning,
        "new_player_prior": new_player_prior,
    }
    return priors, summary


def attach_player_priors(
    data,
    tables,
    train_posterior_path,
    new_player_prior="tier",
    device="cpu",
    n_dimensions=None,
    tier_map=None,
):
    """Build priors from a training posterior + tables and attach them to 'data'.

    Convenience wrapper used by the Stage-1 trainers: estimates tier priors from
    the training posterior, maps the test split's players to tiers, and writes the
    four prior keys into 'data' in place. Returns the logging summary.

    'n_dimensions' (the held-out model's skill dimensionality) is checked
    against the saved posterior so a mismatch fails loudly rather than as a
    cryptic broadcast error during sampling.

    'tier_map' (player_id -> tier) may be passed precomputed; callers that also
    save it with the run posterior reuse it here instead of rebuilding it from
    'tables'. When omitted it is derived from 'tables' as needed.
    """
    train_posterior = load_train_posterior(train_posterior_path)
    posterior_dimensions = _theta_dimensions(train_posterior)
    if n_dimensions is not None and n_dimensions != posterior_dimensions:
        raise ValueError(
            f"Held-out model uses {n_dimensions} skill dimensions but "
            f"{train_posterior_path} was fit with {posterior_dimensions}; "
            "retrain the held-out pass with matching --dimensions"
        )
    tier_priors = estimate_tier_priors(train_posterior)
    if new_player_prior == "tier":
        test_tier_map = tier_map if tier_map is not None else player_tier_map(tables)
    else:
        test_tier_map = {}
    priors, summary = build_prior_tensors(
        data["player_ids"],
        train_posterior,
        tier_priors,
        test_tier_map,
        device=device,
        new_player_prior=new_player_prior,
    )
    data.update(priors)
    return summary
