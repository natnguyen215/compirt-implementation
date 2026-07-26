"""Joint topic-gated CompIRT (sLDA-style) + pyramidal model in Pyro.

A Dirichlet topic model is trained *with* the pyramidal IRT model in one SVI.
Each document (tossup or bonus) has a Dirichlet topic-proportion latent
'theta_doc'; the discrete per-word topic assignments of classic LDA are
marginalized out, so the word model is the LDA mixture 'Multinomial(theta_doc @
topic_word)'. For tossups, 'theta_doc' is also the topic-weight 'r_j' that gates
the competing-risks likelihood, so buzz/answer outcomes propagate into the
topics. Bonuses contribute the shared 'topic_word' term, yielding topic vectors
in the same space for the downstream compositional stage.

The topic vector 'r_j = theta_doc' both explains the words and weights the IRT
skill dimensions.

'theta_doc' is a per-document latent and the topic-word matrix 'topic_word' is a
point-estimated parameter. One 'AutoNormal' guide covers every latent.

Documents must be ordered tossups-first, in 'data["tossup_ids"]' order, so the
first 'n_tossups' rows of 'theta_doc' line up with the IRT observations.
"""

from __future__ import annotations

import torch
import torch.nn.functional as F

import pyro
import pyro.distributions as dist
from pyro import poutine

from topic.fixed.topic_compirt.pyramidal import (
    correctness_logit,
    hazard_logit,
    log_survival,
)


def joint_model(
    data,
    n_dimensions,
    bow_weight,
    topic_concentration=1.0,
    calibrate_correctness=False,
):
    """Joint LDA word model + topic-weighted competing-risks likelihood."""
    bow = data["bow"]
    vocab_size = bow.shape[-1]
    n_documents = bow.shape[0]
    n_tossups = len(data["tossup_ids"])
    n_players = len(data["player_ids"])
    dim = n_dimensions
    zero, one = bow.new_tensor(0.0), bow.new_tensor(1.0)
    vector_zero, vector_one = bow.new_zeros(dim), bow.new_ones(dim)

    # Topic-word distributions are point-estimated for training. Small random
    # initialization breaks symmetry between topics. Held-out passes attach the
    # frozen training matrix so test-document theta_doc uses the same topic axes.
    frozen_topic_word = data.get("fixed_topic_word")
    if frozen_topic_word is not None:
        topic_word = frozen_topic_word
    else:
        topic_word_logits = pyro.param(
            "topic_word_logits",
            lambda: 0.01 * torch.randn(dim, vocab_size, device=bow.device),
        )
        topic_word = F.softmax(topic_word_logits, dim=-1)

    # Player priors: theta_i ~ N(0, I), c_i ~ N(0, 1) by default.
    # Held-out evaluation can attach informative per-player priors to 'data'.
    theta_loc = data.get("theta_prior_loc", vector_zero)
    theta_scale = data.get("theta_prior_scale", vector_one)
    c_loc = data.get("c_prior_loc", zero)
    c_scale = data.get("c_prior_scale", one)
    with pyro.plate("players", n_players):
        theta = pyro.sample("theta", dist.Normal(theta_loc, theta_scale).to_event(1))
        c = pyro.sample("c", dist.Normal(c_loc, c_scale))

    # Per-document topic proportions + LDA word reconstruction (mixture).
    # total_count is a nominal cap only: torch's Multinomial.log_prob takes the
    # coefficient from each row's own sum, so with validate_args off its value is
    # inert (it drives sampling/validation, neither of which we use here).
    total_count = int(bow.sum(-1).max().item())
    concentration = topic_concentration * vector_one
    with pyro.plate("documents", n_documents):
        theta_doc = pyro.sample("theta_doc", dist.Dirichlet(concentration))
        word_probs = theta_doc @ topic_word
        with poutine.scale(scale=bow_weight):
            pyro.sample(
                "bow_obs",
                dist.Multinomial(total_count, word_probs, validate_args=False),
                obs=bow,
            )

    # Per-topic tossup difficulty parameters. The "beta" site supplies the
    # difficulty_beta posterior consumed by topic_compirt evaluation.
    with pyro.plate("tossups", n_tossups):
        difficulty_beta = pyro.sample(
            "beta", dist.Normal(vector_zero, vector_one).to_event(1)
        )
        gamma = pyro.sample("gamma", dist.HalfCauchy(5.0 * vector_one).to_event(1))
        mu = pyro.sample(
            "mu", dist.Beta(2.0 * vector_one, 2.0 * vector_one).to_event(1)
        )

    # Competing-risks likelihood, gated by the tossup topic proportions r_j.
    tossup_topic = theta_doc[:n_tossups]
    topic_weight = tossup_topic[data["tossup"]]
    row_theta = theta[data["player"]]
    row_c = c[data["player"]]
    row_difficulty_beta = difficulty_beta[data["tossup"]]
    row_gamma = gamma[data["tossup"]]
    row_mu = mu[data["tossup"]]

    survival = log_survival(
        row_theta, topic_weight, row_difficulty_beta, row_gamma, row_mu, row_c,
        data["t_star"], data["T_j"],
    )
    buzz = data["is_buzz"]
    buzz_logits = hazard_logit(
        row_theta[buzz], topic_weight[buzz], row_difficulty_beta[buzz], row_gamma[buzz],
        row_mu[buzz], row_c[buzz], data["t_star"][buzz], data["T_j"][buzz],
    )
    correctness = correctness_logit(
        row_theta[buzz], topic_weight[buzz], row_difficulty_beta[buzz], row_gamma[buzz],
        row_mu[buzz], data["t_star"][buzz], data["T_j"][buzz],
    )
    if calibrate_correctness:
        scale = pyro.sample(
            "correctness_scale", dist.LogNormal(zero, bow.new_tensor(0.5))
        )
        bias = pyro.sample("correctness_bias", dist.Normal(zero, bow.new_tensor(3.0)))
        correctness = scale * correctness + bias

    log_likelihood = (
        survival.sum()
        + F.logsigmoid(buzz_logits).sum()
        + dist.Bernoulli(logits=correctness).log_prob(data["y"][buzz]).sum()
    )
    pyro.factor("topic_weighted_competing_risks_likelihood", log_likelihood)


def topic_word_distributions() -> torch.Tensor:
    """Return the fitted (n_topics, vocab_size) topic-word distributions."""
    logits = pyro.param("topic_word_logits").detach()
    return F.softmax(logits, dim=-1)
