"""Joint learned-topic pyramidal model with topic-specific TF-IDF effects.

Document topic proportions are learned Dirichlet latents; their tossup rows
weight both the ordinary per-topic skill gaps and the per-topic TF-IDF lambda
vector. The trainer saves topics, the topic-word matrix, and document vectors.
"""

from __future__ import annotations

import torch.nn.functional as F

from compirt_race import winner_log_prob, survival_stop
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
    bow_weight,
    topic_concentration=1.0,
    calibrate_correctness=False,
    prior_scale=1.0,
):
    """Define a joint LDA word model plus TF-IDF-adjusted IRT likelihood."""
    prefix = prefix_by_row(data)
    bow = data["bow"]
    vocab_size = bow.shape[-1]
    n_documents = bow.shape[0]
    n_tossups = len(data["tossup_ids"])
    n_players = len(data["player_ids"])
    zero, one = bow.new_tensor(0.0), bow.new_tensor(1.0)
    vector_zero, vector_one = bow.new_zeros(n_dimensions), bow.new_ones(n_dimensions)

    # Training learns the topic-word distributions; held-out replay attaches
    # the frozen training matrix through 'fixed_topic_word'.
    frozen_topic_word = data.get("fixed_topic_word")
    if frozen_topic_word is not None:
        topic_word = frozen_topic_word
    else:
        topic_word_logits = pyro.param(
            "topic_word_logits",
            lambda: 0.01 * bow.new_empty((n_dimensions, vocab_size)).normal_(),
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
        survival_stop(data),
        data["T_j"],
        prefix,
        lambdas,
    )
    buzz = data["is_buzz"]
    stop_prefix = tfidf_prefix_score_at(prefix, data["t_star"])
    stop_hazard_logits = hazard_logit(
        row_theta,
        topic_weight,
        row_difficulty_beta,
        row_gamma,
        row_mu,
        row_c,
        data["t_star"],
        data["T_j"],
        stop_prefix,
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
        stop_prefix[buzz],
        lambdas,
    )
    if calibrate_correctness:
        scale = pyro.sample(
            "correctness_scale", dist.LogNormal(zero, bow.new_tensor(0.5))
        )
        bias = pyro.sample("correctness_bias", dist.Normal(zero, bow.new_tensor(3.0)))
        correctness = scale * correctness + bias

    # Attach the hand-computed competing-risks log-likelihood with pyro.factor;
    # the word model's Multinomial factor contributes to the same objective.
    log_likelihood = (
        survival.sum()
        + winner_log_prob(data, stop_hazard_logits).sum()
        + dist.Bernoulli(logits=correctness).log_prob(data["y"][buzz]).sum()
    )
    pyro.factor("topic_tfidf_competing_risks_likelihood", log_likelihood)
