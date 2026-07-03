"""Joint topic-gated CompIRT (sLDA-style) + compositional bonus model in Pyro.

This is the bonus-stage analogue of 'joint_pyramidal'. The pyramidal stage
already learns player skills 'theta' and the topic-word matrix 'topic_word' with
tossup outcomes supervising the topics. This stage keeps both of those *fixed*
and re-learns each bonus's Dirichlet topic proportions 'theta_doc' so that the
bonus's own part-correctness outcomes -- not just its words -- shape its place in
topic space (sLDA-style supervision for bonuses).

It is supervised-LDA in spirit, not the canonical Blei-McAuliffe form: there is no
separate response-regression coefficient. The bonus's topic vector 'r_b' =
'theta_doc' double-duties as the compositional weight that gates the bonus-part
likelihood, so the one vector both explains the words and weights the skills.

Each bonus is one document: its three parts share the single 'theta_doc' that
also serves as the compositional topic weight 'r_b'. The word model is the LDA
mixture 'Multinomial(theta_doc @ topic_word)' (discrete per-word assignments
marginalized out), scaled by 'bow_weight' against the bonus-part likelihood.

'theta' and 'topic_word' arrive as plain fixed tensors (never sampled), so the one
'AutoNormal' guide only covers 'theta_doc', the per-part 'difficulty_beta',
'tau', and the optional synergy/calibration latents. The aggregation,
difficulty, and synergy math is reused unchanged from
'topic_compirt.compositional'; only the source of the topic weight differs (a
learned latent here vs. a fixed CSV there).
"""

from __future__ import annotations

import math

import torch

import pyro
import pyro.distributions as dist
from pyro import poutine

# Reuse the compositional helpers from the fixed-topic package.
from compositional_model import lse_aggregation, synergy_contribution
from topic.fixed.topic_compirt.compositional import (
    topic_weighted_member_abilities,
    topic_weighted_part_difficulty,
)


def joint_compositional_model(
    data,
    theta,
    topic_word,
    bow_weight,
    topic_concentration=1.0,
    use_synergy=False,
    synergy_dimensions=1,
    calibrate_correctness=False,
):
    """Joint LDA word model + topic-weighted compositional bonus likelihood.

    'theta' (fixed players) and 'topic_word' (fixed topic-word matrix) are plain tensors,
    held constant from the pyramidal stage; only 'theta_doc' and the bonus-part
    parameters are learned. The topic dimension is read from 'theta', so the
    number of topics, skill dimensions, and topic_word rows cannot disagree.
    """
    bonus_bow = data["bonus_bow"]
    n_bonuses = bonus_bow.shape[0]
    n_parts = len(data["part_ids"])
    dim = theta.shape[1]
    zero = theta.new_tensor(0.0)
    one = theta.new_tensor(1.0)
    vector_zero = theta.new_zeros(dim)
    vector_one = theta.new_ones(dim)

    # Per-bonus topic proportions + LDA word reconstruction (mixture, fixed topic_word).
    # total_count is a nominal cap only: torch's Multinomial.log_prob takes the
    # coefficient from each row's own sum, so with validate_args off its value is
    # inert (it drives sampling/validation, neither of which we use here).
    total_count = int(bonus_bow.sum(-1).max().item())
    concentration = topic_concentration * vector_one
    with pyro.plate("bonus_documents", n_bonuses):
        theta_doc = pyro.sample("theta_doc", dist.Dirichlet(concentration))
        word_probs = theta_doc @ topic_word
        with poutine.scale(scale=bow_weight):
            pyro.sample(
                "bow_obs",
                dist.Multinomial(total_count, word_probs, validate_args=False),
                obs=bonus_bow,
            )

    # Eq. 14 bonus-part prior, per-topic and with no learned alpha.
    # The Pyro site is still named "beta" for compatibility with existing
    # topic_compirt outputs, but this is CompIRT difficulty_beta, not LDA beta.
    # difficulty_beta_bk ~ N(0, 1), shape (n_parts, n_dimensions).
    with pyro.plate("bonus_parts", n_parts):
        difficulty_beta = pyro.sample(
            "beta", dist.Normal(vector_zero, vector_one).to_event(1)
        )
    tau = pyro.sample("tau", dist.HalfCauchy(one))

    # Each part inherits its bonus's learned topic weight r_b = theta_doc.
    part_topic_weight = theta_doc[data["part_doc_index"]]
    obs_topic_weight = part_topic_weight[data["part"]]
    part_difficulty_beta = difficulty_beta[data["part"]]
    member_theta = theta[data["roster"]]
    member_abilities = topic_weighted_member_abilities(member_theta, obs_topic_weight)
    # Eq. 8 smooth maximum; tau combines member scores into one team score A_b(R).
    aggregate = lse_aggregation(member_abilities, data["roster_mask"], tau)
    weighted_difficulty = topic_weighted_part_difficulty(
        part_difficulty_beta, obs_topic_weight
    )
    # Eq. 11 logit without synergy:
    # eta_rb = A_b(R_r) - sum_k r_bk * difficulty_beta_bk.
    logits = aggregate - weighted_difficulty

    if use_synergy:
        # Eq. 14 synergy prior psi_i ~ N(0, 0.5 I); Eq. 10 pairwise roster term.
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
        # Platt-scale the whole logit (bonus parallel of the tossup fix).
        scale = pyro.sample("correctness_scale", dist.LogNormal(zero, theta.new_tensor(0.5)))
        bias = pyro.sample("correctness_bias", dist.Normal(zero, theta.new_tensor(3.0)))
        logits = scale * logits + bias

    # Eq. 11: y_rb ~ Bernoulli(sigmoid(eta_rb)), observed directly.
    with pyro.plate("bonus_observations", len(data["y"])):
        pyro.sample("obs", dist.Bernoulli(logits=logits), obs=data["y"])


def joint_posterior_predictions(
    data, theta, posterior, use_synergy=False, calibrate_correctness=False
):
    """Return fitted correctness, team aggregate, and synergy per row.

    Replays Eq. 8/10/11 at the posterior medians, using the learned per-bonus
    'theta_doc' as the topic weight.
    """
    theta_doc = posterior["theta_doc"]
    topic_weight = theta_doc[data["part_doc_index"]][data["part"]]
    difficulty_beta = posterior["beta"][data["part"]]
    member_theta = theta[data["roster"]]
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
