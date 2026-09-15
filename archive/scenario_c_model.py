"""Fit new bonus-item parameters while freezing CompIRT player/team parameters.

Scenario C asks whether player synergy profiles learned on historical rosters
transfer to test rosters.  Consequently 'theta', 'psi', and 'tau' enter
this model as ordinary fixed tensors.  Only the new test bonus parts have Pyro
sample sites ('alpha' and 'beta'), which makes it impossible for an
'AutoNormal' guide to silently relearn the purportedly transferred values.
This is transductive with respect to test items, as specified in paper Section
4.2, but frozen with respect to the player/team parameters whose compositional
transfer Scenario C measures.
"""

from __future__ import annotations

import torch

import pyro
import pyro.distributions as dist

from compositional_model import lse_aggregation, synergy_contribution


def frozen_global_item_model(
    data,
    theta,
    tau,
    psi=None,
    correctness_scale=None,
    correctness_bias=None,
):
    """Observe test responses while sampling only per-part 'alpha'/'beta'."""
    n_parts = len(data["part_ids"])
    n_dimensions = theta.shape[1]
    one = theta.new_tensor(1.0)
    vector_zero = theta.new_zeros(n_dimensions)
    vector_one = theta.new_ones(n_dimensions)

    with pyro.plate("bonus_parts", n_parts):
        alpha = pyro.sample(
            "alpha", dist.Normal(vector_zero, vector_one).to_event(1)
        )
        beta = pyro.sample("beta", dist.Normal(theta.new_tensor(0.0), one))

    part_alpha = alpha[data["part"]]
    member_theta = theta[data["roster"]]
    member_abilities = (member_theta * part_alpha.unsqueeze(1)).sum(-1)
    aggregate = lse_aggregation(member_abilities, data["roster_mask"], tau)
    logits = aggregate - beta[data["part"]]
    if psi is not None:
        logits = logits + synergy_contribution(
            psi, data["roster"], data["roster_mask"]
        )
    if correctness_scale is not None:
        logits = correctness_scale * logits + correctness_bias

    with pyro.plate("bonus_observations", len(data["y"])):
        pyro.sample("obs", dist.Bernoulli(logits=logits), obs=data["y"])


def frozen_global_predictions(
    data,
    theta,
    posterior,
    tau,
    psi=None,
    correctness_scale=None,
    correctness_bias=None,
):
    """Replay the frozen-global model at posterior-median item parameters."""
    alpha = posterior["alpha"][data["part"]]
    member_theta = theta[data["roster"]]
    member_abilities = (member_theta * alpha.unsqueeze(1)).sum(-1)
    aggregate = lse_aggregation(member_abilities, data["roster_mask"], tau)
    synergy = aggregate.new_zeros(len(aggregate))
    if psi is not None:
        synergy = synergy_contribution(psi, data["roster"], data["roster_mask"])
    logits = aggregate + synergy - posterior["beta"][data["part"]]
    if correctness_scale is not None:
        logits = correctness_scale * logits + correctness_bias
    return torch.sigmoid(logits), aggregate, synergy
