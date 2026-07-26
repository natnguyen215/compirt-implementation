"""Topic-weighted pyramidal likelihood with per-topic TF-IDF effects.

Stage 1 learns one nonnegative global 'lambda_k' for each topic. At token
position 't' its per-topic difficulty is

    d'_jk(t) = d_jk(t) - lambda_k * tfidf_prefix_j(t)

so fixed or learned topic weights combine the effect as
'tfidf_prefix_j(t) * sum_k r_jk * lambda_k'. This module owns the
text-conditioned likelihood and replay math for the experiment family.
"""

from __future__ import annotations

import torch
import torch.nn.functional as F
from torch.utils.checkpoint import checkpoint

import pyro
import pyro.distributions as dist

from topic.fixed.topic_compirt.pyramidal import (
    difficulty_curve,
    row_parameters,
    sample_correctness_calibration,
    sample_parameters,
)
from utils.training import survival_chunk_size


def tfidf_prefix_score_at(score_matrix, position):
    """Gather padded TF-IDF prefix values at 1-indexed token positions."""
    max_position = score_matrix.shape[-1]
    index = position.long().clamp(min=1, max=max_position) - 1
    expanded = score_matrix.expand(*index.shape, max_position)
    return torch.gather(expanded, -1, index.unsqueeze(-1)).squeeze(-1)


def effective_difficulty(difficulty_beta, gamma, mu, t, T_j, prefix, lambdas):
    """Return the per-topic base curve after its cumulative-TF-IDF reduction."""
    base = difficulty_curve(difficulty_beta, gamma, mu, t, T_j)
    return base - prefix.unsqueeze(-1) * lambdas


def correctness_logit(
    theta, topic_weight, difficulty_beta, gamma, mu, t, T_j, prefix, lambdas
):
    """Return the TF-IDF-adjusted topic-weighted correctness logit at 't'."""
    gap = theta - effective_difficulty(
        difficulty_beta, gamma, mu, t, T_j, prefix, lambdas
    )
    return (topic_weight * gap).sum(-1)


def hazard_logit(
    theta, topic_weight, difficulty_beta, gamma, mu, c, t, T_j, prefix, lambdas
):
    """Return the TF-IDF-adjusted topic-weighted buzz hazard logit at 't'."""
    return correctness_logit(
        theta, topic_weight, difficulty_beta, gamma, mu, t, T_j, prefix, lambdas
    ) - c


def log_survival(
    theta, topic_weight, difficulty_beta, gamma, mu, c, t_star, T_j, prefix, lambdas,
    chunk_size=None,
):
    """Return strict-before survival using the adjusted topic-weighted hazard."""
    if chunk_size is None:
        chunk_size = survival_chunk_size()
    if chunk_size and t_star.shape[0] > chunk_size:
        # Each row's survival term is independent, so summing the grid in row
        # chunks under gradient checkpointing caps peak memory at one chunk's
        # (rows, positions, topics) grid while leaving the result identical to
        # the full-batch computation. Only 'lambdas' is global (not row-sliced).
        parts = [
            checkpoint(
                log_survival,
                theta[lo:lo + chunk_size],
                topic_weight[lo:lo + chunk_size],
                difficulty_beta[lo:lo + chunk_size],
                gamma[lo:lo + chunk_size],
                mu[lo:lo + chunk_size],
                c[lo:lo + chunk_size],
                t_star[lo:lo + chunk_size],
                T_j[lo:lo + chunk_size],
                prefix[lo:lo + chunk_size],
                lambdas,
                use_reentrant=False,
            )
            for lo in range(0, t_star.shape[0], chunk_size)
        ]
        return torch.cat(parts)
    max_t = int(t_star.max().item())
    positions = torch.arange(1, max_t + 1, device=t_star.device).unsqueeze(0)
    # Eq. 6 is strict-before survival, and Eq. 13 uses S(T_j) for dead tossups.
    # The published indexing stops NO-BUZZ rows at T_j - 1, so this comparison
    # must stay strict.
    before_stop = positions < t_star.unsqueeze(1)
    prefix_at_positions = tfidf_prefix_score_at(
        prefix.unsqueeze(1), positions.expand_as(before_stop)
    )
    # Unsqueezing row parameters broadcasts them against every token position,
    # producing one hazard logit per row-position pair.
    logits = hazard_logit(
        theta.unsqueeze(1),
        topic_weight.unsqueeze(1),
        difficulty_beta.unsqueeze(1),
        gamma.unsqueeze(1),
        mu.unsqueeze(1),
        c.unsqueeze(1),
        positions,
        T_j.unsqueeze(1),
        prefix_at_positions,
        lambdas,
    )
    return (F.logsigmoid(-logits) * before_stop).sum(1)


def sample_lambdas(data, n_dimensions, prior_scale):
    """Sample one global nonnegative cumulative-TF-IDF effect per topic."""
    scale = data["y"].new_full((n_dimensions,), float(prior_scale))
    return pyro.sample("topic_tfidf_lambdas", dist.HalfNormal(scale).to_event(1))


def prefix_by_row(data):
    """Return cumulative TF-IDF rows aligned to the observation rows."""
    if "tfidf_prefix" not in data:
        raise ValueError("Topic TF-IDF runs require data['tfidf_prefix']")
    return data["tfidf_prefix"][data["tossup"]]


def competing_risks_model(data, calibrate_correctness=False, prior_scale=1.0):
    """Define the fixed-topic TF-IDF-adjusted competing-risks likelihood."""
    n_dimensions = data["topic_weight"].shape[1]
    theta, c, difficulty_beta, gamma, mu = sample_parameters(data, n_dimensions)
    (
        row_theta,
        row_c,
        row_topic_weight,
        row_difficulty_beta,
        row_gamma,
        row_mu,
    ) = row_parameters(data, theta, c, difficulty_beta, gamma, mu)
    prefix = prefix_by_row(data)
    lambdas = sample_lambdas(data, n_dimensions, prior_scale)

    # Eq. 6 survival on every BUZZ, CENSORED, and NO-BUZZ row (Eq. 13 enters via
    # t_star = T_j on NO-BUZZ rows); only the logits carry the TF-IDF adjustment.
    survival = log_survival(
        row_theta,
        row_topic_weight,
        row_difficulty_beta,
        row_gamma,
        row_mu,
        row_c,
        data["t_star"],
        data["T_j"],
        prefix,
        lambdas,
    )
    # Eq. 7 / Eq. 12 event term: only actual first-buzzer rows contribute the
    # hazard-at-t* and correctness factors.
    buzz = data["is_buzz"]
    buzz_prefix = tfidf_prefix_score_at(prefix[buzz], data["t_star"][buzz])
    buzz_logits = hazard_logit(
        row_theta[buzz],
        row_topic_weight[buzz],
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
        row_topic_weight[buzz],
        row_difficulty_beta[buzz],
        row_gamma[buzz],
        row_mu[buzz],
        data["t_star"][buzz],
        data["T_j"][buzz],
        buzz_prefix,
        lambdas,
    )
    if calibrate_correctness:
        # Apply calibration to correctness; hazard/timing keeps its base logit.
        scale, bias = sample_correctness_calibration(data)
        correctness = scale * correctness + bias
    # Attach the hand-computed competing-risks log-likelihood with pyro.factor.
    log_likelihood = (
        survival.sum()
        + F.logsigmoid(buzz_logits).sum()
        + dist.Bernoulli(logits=correctness).log_prob(data["y"][buzz]).sum()
    )
    pyro.factor("topic_tfidf_competing_risks_likelihood", log_likelihood)


def posterior_row_predictions(data, posterior, calibrate_correctness=False):
    """Replay fitted correctness, hazard, and strict-before survival per row."""
    theta, c, topic_weight, difficulty_beta, gamma, mu = row_parameters(
        data,
        posterior["theta"],
        posterior["c"],
        posterior["beta"],
        posterior["gamma"],
        posterior["mu"],
    )
    prefix = prefix_by_row(data)
    prefix_at_star = tfidf_prefix_score_at(prefix, data["t_star"])
    lambdas = posterior["topic_tfidf_lambdas"]
    correctness_logits = correctness_logit(
        theta,
        topic_weight,
        difficulty_beta,
        gamma,
        mu,
        data["t_star"],
        data["T_j"],
        prefix_at_star,
        lambdas,
    )
    if calibrate_correctness:
        correctness_logits = (
            posterior["correctness_scale"] * correctness_logits
            + posterior["correctness_bias"]
        )
    correctness = torch.sigmoid(correctness_logits)
    hazard = torch.sigmoid(
        hazard_logit(
            theta,
            topic_weight,
            difficulty_beta,
            gamma,
            mu,
            c,
            data["t_star"],
            data["T_j"],
            prefix_at_star,
            lambdas,
        )
    )
    survival = torch.exp(
        log_survival(
            theta,
            topic_weight,
            difficulty_beta,
            gamma,
            mu,
            c,
            data["t_star"],
            data["T_j"],
            prefix,
            lambdas,
        )
    )
    return correctness, hazard, survival


def row_tfidf_prefix_scores(data):
    """Return the cumulative TF-IDF value at each observation's 't_star'."""
    return tfidf_prefix_score_at(prefix_by_row(data), data["t_star"])


def expected_first_buzz_positions(data, posterior):
    """Replay expected team first-buzz positions with TF-IDF-adjusted hazards.

    The returned position is E[t | a buzz occurs], since the evaluation
    compares it only against events with an observed buzz.
    """
    n_events = len(data["event_ids"])
    counts = torch.bincount(data["event"], minlength=n_events)
    max_roster = int(counts.max().item())
    roster = data["player"].new_zeros((n_events, max_roster))
    roster_mask = torch.zeros(
        (n_events, max_roster), dtype=torch.bool, device=data["event"].device
    )
    next_slot = [0] * n_events
    event_tossup = data["tossup"].new_zeros(n_events)
    event_T = data["T_j"].new_ones(n_events)
    for row in range(len(data["event"])):
        # Training rows are player-event rows. This loop rebuilds one padded
        # roster per event so the team first-buzz distribution can be simulated.
        event = int(data["event"][row].item())
        slot = next_slot[event]
        roster[event, slot] = data["player"][row]
        roster_mask[event, slot] = True
        event_tossup[event] = data["tossup"][row]
        event_T[event] = data["T_j"][row]
        next_slot[event] += 1

    theta = posterior["theta"][roster]
    topic_weight = data["topic_weight"][event_tossup].unsqueeze(1)
    difficulty_beta = posterior["beta"][event_tossup].unsqueeze(1)
    gamma = posterior["gamma"][event_tossup].unsqueeze(1)
    mu = posterior["mu"][event_tossup].unsqueeze(1)
    c = posterior["c"][roster]
    prefix = data["tfidf_prefix"][event_tossup].unsqueeze(1)
    lambdas = posterior["topic_tfidf_lambdas"]

    event_survival = data["y"].new_ones(n_events)
    expected = data["y"].new_zeros(n_events)
    for position in range(1, int(event_T.max().item()) + 1):
        # At each token, combine independent player hazards into the chance
        # that at least one roster member produces the first buzz right now.
        active_event = position <= event_T
        t = data["y"].new_full((n_events, max_roster), float(position))
        T = event_T.unsqueeze(1).expand_as(t)
        prefix_at_position = tfidf_prefix_score_at(prefix, t)
        hazard = torch.sigmoid(
            hazard_logit(
                theta,
                topic_weight,
                difficulty_beta,
                gamma,
                mu,
                c,
                t,
                T,
                prefix_at_position,
                lambdas,
            )
        )
        hazard = torch.where(roster_mask, hazard, torch.zeros_like(hazard))
        total_hazard = 1.0 - torch.prod(1.0 - hazard, dim=1)
        total_hazard = torch.where(
            active_event, total_hazard, torch.zeros_like(total_hazard)
        )
        first_probability = event_survival * total_hazard
        expected = expected + position * first_probability
        event_survival = event_survival * (1.0 - total_hazard)
    # Condition the prediction on a buzz occurring:
    #   E[t | buzz] = sum_t t * P(first buzz at t) / P(any buzz).
    # Use the question end when the fitted buzz mass is numerically zero.
    buzz_mass = 1.0 - event_survival
    end_position = event_T.to(expected.dtype)
    expected = torch.where(
        buzz_mass > 1e-9, expected / buzz_mass.clamp(min=1e-9), end_position
    )
    relative = (expected / end_position).detach().cpu().tolist()
    return dict(zip(data["event_ids"], relative))
