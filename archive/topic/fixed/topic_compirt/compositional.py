"""Topic-weighted compositional bonus model (Eq. 8, 10, 11, 14).

The model keeps the player skills 'theta' fixed and learns per-topic bonus-part
difficulty. The member score inside the Eq. 8 aggregation is:

    sum_k r_bk * theta_pk

Bonus-part difficulty is the per-topic vector 'difficulty_beta_bk'. The bonus
topic vector 'r_b' is shared by all three parts of a bonus.
"""

from __future__ import annotations

import math

import torch

import pyro
import pyro.distributions as dist

from compositional_model import lse_aggregation, synergy_contribution


def topic_weighted_member_abilities(member_theta, topic_weight):
    """Return 'sum_k r_bk * theta_pk' per roster member (Eq. 8, r replaces alpha)."""
    # member_theta: (n_observations, max_roster_size, n_dimensions)
    # topic_weight: (n_observations, n_dimensions)
    # Unsqueezing topic_weight lines it up with every roster slot.
    return (member_theta * topic_weight.unsqueeze(1)).sum(-1)


def topic_weighted_part_difficulty(part_difficulty_beta, topic_weight):
    """Return 'sum_k r_bk * difficulty_beta_bk' (Eq. 11 difficulty term)."""
    return (part_difficulty_beta * topic_weight).sum(-1)


def compositional_model(
    data, theta, use_synergy=False, synergy_dimensions=1, calibrate_correctness=False
):
    """Define the topic-weighted team bonus-part correctness likelihood (Eq. 8/10/11)."""
    n_parts = len(data["part_ids"])
    n_dimensions = theta.shape[1]
    zero = theta.new_tensor(0.0)
    one = theta.new_tensor(1.0)
    vector_zero = theta.new_zeros(n_dimensions)
    vector_one = theta.new_ones(n_dimensions)

    # Eq. 14 per-topic bonus-part difficulty prior. The "beta" site supplies the
    # difficulty_beta posterior and CSV columns.
    # difficulty_beta_bk ~ N(0, 1), shape (n_parts, n_dimensions).
    with pyro.plate("bonus_parts", n_parts):
        difficulty_beta = pyro.sample(
            "beta", dist.Normal(vector_zero, vector_one).to_event(1)
        )

    tau = pyro.sample("tau", dist.HalfCauchy(one))

    part_difficulty_beta = difficulty_beta[data["part"]]
    part_topic_weight = data["topic_weight"][data["part"]]
    member_theta = theta[data["roster"]]
    member_abilities = topic_weighted_member_abilities(member_theta, part_topic_weight)
    # Eq. 8: topic weighting forms member scores, and tau combines them into the
    # team score A_b(R).
    aggregate = lse_aggregation(member_abilities, data["roster_mask"], tau)
    weighted_difficulty = topic_weighted_part_difficulty(
        part_difficulty_beta, part_topic_weight
    )
    # Eq. 11 logit without synergy:
    # eta_rb = A_b(R_r) - sum_k r_bk * difficulty_beta_bk.
    logits = aggregate - weighted_difficulty

    if use_synergy:
        # Eq. 14 synergy prior psi_i ~ N(0, 0.5 I), followed by the Eq. 10
        # pairwise roster term.
        with pyro.plate("synergy_players", theta.shape[0]):
            psi = pyro.sample(
                "psi",
                dist.Normal(
                    theta.new_zeros(synergy_dimensions),
                    theta.new_full((synergy_dimensions,), math.sqrt(0.5)),
                ).to_event(1),
            )
        # Eq. 10 adds the pairwise roster synergy term.
        logits = logits + synergy_contribution(psi, data["roster"], data["roster_mask"])

    if calibrate_correctness:
        # Platt-scale the whole logit (bonus parallel of the tossup fix).
        scale = pyro.sample("correctness_scale", dist.LogNormal(zero, theta.new_tensor(0.5)))
        bias = pyro.sample("correctness_bias", dist.Normal(zero, theta.new_tensor(3.0)))
        logits = scale * logits + bias

    # Eq. 11: y_rb ~ Bernoulli(sigmoid(eta_rb)), observed directly.
    with pyro.plate("bonus_observations", len(data["y"])):
        pyro.sample("obs", dist.Bernoulli(logits=logits), obs=data["y"])


def posterior_predictions(
    data, theta, posterior, use_synergy=False, calibrate_correctness=False
):
    """Return fitted correctness, team aggregate, and synergy per row (Eq. 8/10/11)."""
    member_theta = theta[data["roster"]]
    topic_weight = data["topic_weight"][data["part"]]
    difficulty_beta = posterior["beta"][data["part"]]
    # Replay Eq. 8/10/11 at the posterior medians.
    member_abilities = topic_weighted_member_abilities(member_theta, topic_weight)
    aggregate = lse_aggregation(member_abilities, data["roster_mask"], posterior["tau"])
    synergy = aggregate.new_zeros(len(aggregate))
    if use_synergy:
        synergy = synergy_contribution(
            posterior["psi"], data["roster"], data["roster_mask"]
        )
    weighted_difficulty = topic_weighted_part_difficulty(difficulty_beta, topic_weight)
    logits = aggregate + synergy - weighted_difficulty
    if calibrate_correctness:
        logits = posterior["correctness_scale"] * logits + posterior["correctness_bias"]
    return torch.sigmoid(logits), aggregate, synergy
