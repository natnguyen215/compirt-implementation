"""Embedding-relevance compositional bonus model.

Mirrors 'topic/fixed/topic_compirt/compositional.py', but 'r' comes from the
frozen projection fit during pyramidal (tossup) training rather than a fixed
topic CSV. The member score inside the Eq. 8 aggregation is:

    root CompIRT:      sum_k theta_pk * alpha_bk
    embedding CompIRT: sum_k r_bk * theta_pk

'r_b' is computed once in 'train_compositional.py' from each bonus's frozen
embedding and the pyramidal run's fitted projection -- it is passed into this
model as a fixed tensor, not sampled or re-fit here. Bonus-part difficulty
becomes a per-dimension vector 'difficulty_beta_bk', shared by all three parts
of a bonus like the topic variant.
"""

from __future__ import annotations

import math

import torch

import pyro
import pyro.distributions as dist

from compositional_model import lse_aggregation, synergy_contribution


def embedding_weighted_member_abilities(member_theta, r):
    """Return 'sum_k r_bk * theta_pk' per roster member (Eq. 8, r replaces alpha)."""
    return (member_theta * r.unsqueeze(1)).sum(-1)


def embedding_weighted_part_difficulty(part_difficulty_beta, r):
    """Return 'sum_k r_bk * difficulty_beta_bk' (Eq. 11 difficulty term)."""
    return (part_difficulty_beta * r).sum(-1)


def compositional_model(
    data, theta, r, use_synergy=False, synergy_dimensions=1, calibrate_correctness=False
):
    """Define the embedding-weighted team bonus-part correctness likelihood."""
    n_parts = len(data["part_ids"])
    n_dimensions = theta.shape[1]
    zero = theta.new_tensor(0.0)
    one = theta.new_tensor(1.0)
    vector_zero = theta.new_zeros(n_dimensions)
    vector_one = theta.new_ones(n_dimensions)

    with pyro.plate("bonus_parts", n_parts):
        difficulty_beta = pyro.sample(
            "beta", dist.Normal(vector_zero, vector_one).to_event(1)
        )

    tau = pyro.sample("tau", dist.HalfCauchy(one))

    part_difficulty_beta = difficulty_beta[data["part"]]
    part_r = r[data["part"]]
    member_theta = theta[data["roster"]]
    member_abilities = embedding_weighted_member_abilities(member_theta, part_r)
    aggregate = lse_aggregation(member_abilities, data["roster_mask"], tau)
    weighted_difficulty = embedding_weighted_part_difficulty(part_difficulty_beta, part_r)
    logits = aggregate - weighted_difficulty

    if use_synergy:
        with pyro.plate("synergy_players", theta.shape[0]):
            psi = pyro.sample(
                "psi",
                dist.Normal(
                    theta.new_zeros(synergy_dimensions),
                    theta.new_full((synergy_dimensions,), math.sqrt(0.5)),
                ).to_event(1),
            )
        logits = logits + synergy_contribution(psi, data["roster"], data["roster_mask"])

    if calibrate_correctness:
        scale = pyro.sample("correctness_scale", dist.LogNormal(zero, theta.new_tensor(0.5)))
        bias = pyro.sample("correctness_bias", dist.Normal(zero, theta.new_tensor(3.0)))
        logits = scale * logits + bias

    with pyro.plate("bonus_observations", len(data["y"])):
        pyro.sample("obs", dist.Bernoulli(logits=logits), obs=data["y"])


def posterior_predictions(
    data, theta, r, posterior, use_synergy=False, calibrate_correctness=False
):
    """Return fitted correctness, team aggregate, and synergy per row."""
    member_theta = theta[data["roster"]]
    part_r = r[data["part"]]
    difficulty_beta = posterior["beta"][data["part"]]
    member_abilities = embedding_weighted_member_abilities(member_theta, part_r)
    aggregate = lse_aggregation(member_abilities, data["roster_mask"], posterior["tau"])
    synergy = aggregate.new_zeros(len(aggregate))
    if use_synergy:
        synergy = synergy_contribution(posterior["psi"], data["roster"], data["roster_mask"])
    weighted_difficulty = embedding_weighted_part_difficulty(difficulty_beta, part_r)
    logits = aggregate + synergy - weighted_difficulty
    if calibrate_correctness:
        logits = posterior["correctness_scale"] * logits + posterior["correctness_bias"]
    return torch.sigmoid(logits), aggregate, synergy
