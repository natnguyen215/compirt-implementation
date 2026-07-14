"""Topic-weighted pyramidal likelihood with per-topic TF-IDF effects.

This isolated Stage 1 variant learns one nonnegative global ``lambda_k`` for
each topic. At token position ``t`` its per-topic difficulty is

    d'_jk(t) = d_jk(t) - lambda_k * tfidf_prefix_j(t)

so fixed or learned topic weights combine the effect as
``tfidf_prefix_j(t) * sum_k r_jk * lambda_k``. Baseline topic-model helpers
remain unmodified; this module owns all text-conditioned likelihood and replay
math for the experiment family. It is a near-copy of
'topic/fixed/topic_compirt/pyramidal.py' -- diff against that file when
reconciling changes; the TF-IDF ``prefix``/``lambdas`` arguments are the only
departure.
"""

from __future__ import annotations

import torch
import torch.nn.functional as F

import pyro
import pyro.distributions as dist

from topic.fixed.topic_compirt.pyramidal import (
    difficulty_curve,
    row_parameters,
    sample_correctness_calibration,
    sample_parameters,
)


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
    """Return the TF-IDF-adjusted topic-weighted correctness logit at ``t``."""
    gap = theta - effective_difficulty(
        difficulty_beta, gamma, mu, t, T_j, prefix, lambdas
    )
    return (topic_weight * gap).sum(-1)


def hazard_logit(
    theta, topic_weight, difficulty_beta, gamma, mu, c, t, T_j, prefix, lambdas
):
    """Return the TF-IDF-adjusted topic-weighted buzz hazard logit at ``t``."""
    return correctness_logit(
        theta, topic_weight, difficulty_beta, gamma, mu, t, T_j, prefix, lambdas
    ) - c


def log_survival(
    theta, topic_weight, difficulty_beta, gamma, mu, c, t_star, T_j, prefix, lambdas
):
    """Return strict-before survival using the adjusted topic-weighted hazard."""
    max_t = int(t_star.max().item())
    positions = torch.arange(1, max_t + 1, device=t_star.device).unsqueeze(0)
    # Eq. 6 is strict-before survival, and Eq. 13 deliberately uses S(T_j) for
    # dead tossups. NO-BUZZ rows therefore stop at T_j - 1 under the paper's
    # indexing convention; an inclusive mask would define a different model.
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


def competing_risks_model(
    data, n_dimensions=None, calibrate_correctness=False, prior_scale=1.0
):
    """Define the fixed-topic TF-IDF-adjusted competing-risks likelihood."""
    if n_dimensions is None:
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
        # Recalibrate ONLY the correctness logit, leaving the hazard/timing
        # (which also calls correctness_logit) untouched.
        scale, bias = sample_correctness_calibration(data)
        correctness = scale * correctness + bias
    # Competing risks are not a single built-in distribution, so the joint
    # log-likelihood is hand-computed and attached with pyro.factor.
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
    """Return the cumulative TF-IDF value at each observation's ``t_star``."""
    return tfidf_prefix_score_at(prefix_by_row(data), data["t_star"])


def expected_first_buzz_positions(data, posterior):
    """Replay expected team first-buzz positions with TF-IDF-adjusted hazards."""
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
    expected = expected + event_T * event_survival
    relative = (expected / event_T).detach().cpu().tolist()
    return dict(zip(data["event_ids"], relative))
