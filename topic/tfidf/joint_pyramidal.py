"""Joint learned-topic pyramidal model with topic-specific TF-IDF effects.

This is the supervised-LDA-style counterpart to :mod:`topic.tfidf.pyramidal`.
Document topic proportions remain learned Dirichlet latents; their tossup rows
weight both the ordinary per-topic skill gaps and the per-topic TF-IDF lambda
vector. The baseline learned-topic package is intentionally left unchanged.

This is a near-copy of 'topic/learned/joint_pyramidal.py' -- diff against that
file when reconciling changes; the TF-IDF ``prefix``/``lambdas`` plumbing is
the only departure, and the trainer reuses the learned package's writers
(topics, topic-word matrix, document vectors) unchanged.
"""

from __future__ import annotations

import torch
import torch.nn.functional as F

import pyro
import pyro.distributions as dist
from pyro import poutine

from topic.tfidf.pyramidal import (
    correctness_logit,
    hazard_logit,
    log_survival,
    prefix_by_row,
    sample_lambdas,
    tfidf_prefix_score_at,
)


def joint_model(
    data,
    n_dimensions,
    vocab_size,
    bow_weight,
    topic_concentration=1.0,
    calibrate_correctness=False,
    prior_scale=1.0,
):
    """Define a joint LDA word model plus TF-IDF-adjusted IRT likelihood."""
    prefix = prefix_by_row(data)
    bow = data["bow"]
    n_documents = bow.shape[0]
    n_tossups = len(data["tossup_ids"])
    n_players = len(data["player_ids"])
    zero, one = bow.new_tensor(0.0), bow.new_tensor(1.0)
    vector_zero, vector_one = bow.new_zeros(n_dimensions), bow.new_ones(n_dimensions)

    # Topic-word distributions are learned from scratch unless held-out replay
    # attaches the frozen matrix from a previous dedicated TF-IDF run.
    frozen_topic_word = data.get("fixed_topic_word")
    if frozen_topic_word is not None:
        topic_word = frozen_topic_word
    else:
        topic_word_logits = pyro.param(
            "topic_word_logits",
            lambda: 0.01 * torch.randn(n_dimensions, vocab_size, device=bow.device),
        )
        topic_word = F.softmax(topic_word_logits, dim=-1)

    theta_loc = data.get("theta_prior_loc", vector_zero)
    theta_scale = data.get("theta_prior_scale", vector_one)
    c_loc = data.get("c_prior_loc", zero)
    c_scale = data.get("c_prior_scale", one)
    with pyro.plate("players", n_players):
        theta = pyro.sample("theta", dist.Normal(theta_loc, theta_scale).to_event(1))
        c = pyro.sample("c", dist.Normal(c_loc, c_scale))

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

    # Per-topic tossup difficulty curve parameters (no learned alpha). The Pyro
    # site is still named "beta" for compatibility with the existing
    # topic_compirt evaluation code, but this is CompIRT difficulty_beta, not
    # LDA's topic-word beta/phi.
    with pyro.plate("tossups", n_tossups):
        difficulty_beta = pyro.sample(
            "beta", dist.Normal(vector_zero, vector_one).to_event(1)
        )
        gamma = pyro.sample("gamma", dist.HalfCauchy(5.0 * vector_one).to_event(1))
        mu = pyro.sample(
            "mu", dist.Beta(2.0 * vector_one, 2.0 * vector_one).to_event(1)
        )

    # Competing-risks likelihood, gated by the tossup topic proportions r_j and
    # adjusted by the shared per-topic TF-IDF lambdas.
    lambdas = sample_lambdas(data, n_dimensions, prior_scale)
    topic_weight = theta_doc[:n_tossups][data["tossup"]]
    row_theta = theta[data["player"]]
    row_c = c[data["player"]]
    row_difficulty_beta = difficulty_beta[data["tossup"]]
    row_gamma = gamma[data["tossup"]]
    row_mu = mu[data["tossup"]]

    survival = log_survival(
        row_theta,
        topic_weight,
        row_difficulty_beta,
        row_gamma,
        row_mu,
        row_c,
        data["t_star"],
        data["T_j"],
        prefix,
        lambdas,
    )
    buzz = data["is_buzz"]
    buzz_prefix = tfidf_prefix_score_at(prefix[buzz], data["t_star"][buzz])
    buzz_logits = hazard_logit(
        row_theta[buzz],
        topic_weight[buzz],
        row_difficulty_beta[buzz],
        row_gamma[buzz],
        row_mu[buzz],
        row_c[buzz],
        data["t_star"][buzz],
        data["T_j"][buzz],
        buzz_prefix,
        lambdas,
    )
    correctness = correctness_logit(
        row_theta[buzz],
        topic_weight[buzz],
        row_difficulty_beta[buzz],
        row_gamma[buzz],
        row_mu[buzz],
        data["t_star"][buzz],
        data["T_j"][buzz],
        buzz_prefix,
        lambdas,
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
    pyro.factor("topic_tfidf_competing_risks_likelihood", log_likelihood)
