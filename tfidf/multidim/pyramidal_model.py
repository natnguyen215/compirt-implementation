"""Multidimensional TF-IDF pyramidal tossup variants.

This combines the three isolated TF-IDF clue-timing variants from
``tfidf.pyramidal_tfidf_model`` with the vector-valued difficulty flow from
``multidimensional.multidim_mirt``:

    d_jk(t) = beta_jk * sigmoid(gamma_jk * (mu_jk - position_j(t)))
    correctness_ij(t) = sum_k alpha_jk * (theta_ik - d_jk(t))
    hazard_ij(t) = correctness_ij(t) - c_i

The TF-IDF variant selects the position or hazard intervention. Stage 2 remains
the root compositional model because these TF-IDF features are tossup clue-timing
features, not bonus-part features.
"""

from __future__ import annotations

import torch
import torch.nn.functional as F

import pyro
import pyro.distributions as dist

from tfidf.pyramidal_tfidf_model import (
    CUMULATIVE_DIFFICULTY,
    HAZARD_SPIKE,
    REPLACE_POSITION,
    TFIDF_VARIANTS,
    posterior_tfidf_effect,
    sample_tfidf_effect,
    tfidf_score_at,
    validate_tfidf_variant,
)


def _as_dimension_position(position, beta):
    """Broadcast scalar row positions across the trailing difficulty dimension."""
    if position.shape == beta.shape:
        return position
    return position.unsqueeze(-1)


def difficulty_curve(beta, gamma, mu, t, T_j, information_position=None):
    """Return per-dimension difficulty at token position ``t``."""
    position = t / T_j if information_position is None else information_position
    position = _as_dimension_position(position, beta)
    return beta * torch.sigmoid(gamma * (mu - position))


def effective_difficulty(
    beta,
    gamma,
    mu,
    t,
    T_j,
    tfidf_prefix,
    tfidf_effect,
    tfidf_variant=REPLACE_POSITION,
):
    """Return vector difficulty after the selected TF-IDF intervention."""
    tfidf_variant = validate_tfidf_variant(tfidf_variant)
    if tfidf_variant == REPLACE_POSITION:
        return difficulty_curve(
            beta,
            gamma,
            mu,
            t,
            T_j,
            information_position=tfidf_prefix,
        )

    base = difficulty_curve(beta, gamma, mu, t, T_j)
    if tfidf_variant == CUMULATIVE_DIFFICULTY:
        return base - tfidf_effect * _as_dimension_position(tfidf_prefix, beta)
    return base


def correctness_logit(
    theta,
    alpha,
    beta,
    gamma,
    mu,
    t,
    T_j,
    tfidf_prefix=None,
    tfidf_effect=None,
    tfidf_variant=REPLACE_POSITION,
):
    """Return log-odds of a correct buzz under the selected TF-IDF variant."""
    if tfidf_prefix is None:
        tfidf_prefix = t / T_j
    if tfidf_effect is None:
        tfidf_effect = t.new_tensor(0.0, dtype=torch.float32)
    gap = theta - effective_difficulty(
        beta,
        gamma,
        mu,
        t,
        T_j,
        tfidf_prefix,
        tfidf_effect,
        tfidf_variant,
    )
    return (alpha * gap).sum(-1)


def hazard_logit(
    theta,
    alpha,
    beta,
    gamma,
    mu,
    c,
    t,
    T_j,
    tfidf_prefix=None,
    tfidf_token=None,
    tfidf_effect=None,
    tfidf_variant=REPLACE_POSITION,
):
    """Return the buzz hazard logit at ``t`` for the selected variant."""
    tfidf_variant = validate_tfidf_variant(tfidf_variant)
    logit = (
        correctness_logit(
            theta,
            alpha,
            beta,
            gamma,
            mu,
            t,
            T_j,
            tfidf_prefix,
            tfidf_effect,
            tfidf_variant,
        )
        - c
    )
    if tfidf_variant == HAZARD_SPIKE:
        if tfidf_token is None:
            tfidf_token = torch.zeros_like(logit)
        if tfidf_effect is None:
            tfidf_effect = logit.new_tensor(0.0)
        logit = logit + tfidf_effect * tfidf_token
    return logit


def log_survival(
    theta,
    alpha,
    beta,
    gamma,
    mu,
    c,
    t_star,
    T_j,
    tfidf_prefix,
    tfidf_token,
    tfidf_effect,
    tfidf_variant=REPLACE_POSITION,
):
    """Return log probability of not buzzing before ``t_star``."""
    max_t = int(t_star.max().item())
    positions = torch.arange(1, max_t + 1, device=t_star.device).unsqueeze(0)
    before_stop = positions < t_star.unsqueeze(1)
    expanded_positions = positions.expand_as(before_stop)
    prefix = tfidf_score_at(tfidf_prefix.unsqueeze(1), expanded_positions)
    token = tfidf_score_at(tfidf_token.unsqueeze(1), expanded_positions)
    logits = hazard_logit(
        theta.unsqueeze(1),
        alpha.unsqueeze(1),
        beta.unsqueeze(1),
        gamma.unsqueeze(1),
        mu.unsqueeze(1),
        c.unsqueeze(1),
        positions,
        T_j.unsqueeze(1),
        prefix,
        token,
        tfidf_effect,
        tfidf_variant,
    )
    return (F.logsigmoid(-logits) * before_stop).sum(1)


def row_parameters(data, theta, c, alpha, beta, gamma, mu):
    """Index entity-level parameters and TF-IDF features down to rows."""
    player = data["player"]
    tossup = data["tossup"]
    return (
        theta[player],
        c[player],
        alpha[tossup],
        beta[tossup],
        gamma[tossup],
        mu[tossup],
        data["tfidf_prefix"][tossup],
        data["tfidf_token"][tossup],
    )


def sample_parameters(data, n_dimensions):
    """Sample player and vector-valued tossup parameters."""
    n_players = len(data["player_ids"])
    n_tossups = len(data["tossup_ids"])
    zero = data["y"].new_tensor(0.0)
    one = data["y"].new_tensor(1.0)
    vector_zero = data["y"].new_zeros(n_dimensions)
    vector_one = data["y"].new_ones(n_dimensions)

    theta_loc = data.get("theta_prior_loc", vector_zero)
    theta_scale = data.get("theta_prior_scale", vector_one)
    c_loc = data.get("c_prior_loc", zero)
    c_scale = data.get("c_prior_scale", one)
    with pyro.plate("players", n_players):
        theta = pyro.sample("theta", dist.Normal(theta_loc, theta_scale).to_event(1))
        c = pyro.sample("c", dist.Normal(c_loc, c_scale))

    with pyro.plate("tossups", n_tossups):
        alpha = pyro.sample(
            "alpha",
            dist.Gamma(2.0 * vector_one, 2.0 * vector_one).to_event(1),
        )
        beta = pyro.sample("beta", dist.Normal(vector_zero, vector_one).to_event(1))
        gamma = pyro.sample("gamma", dist.HalfCauchy(5.0 * vector_one).to_event(1))
        mu = pyro.sample(
            "mu",
            dist.Beta(
                data["y"].new_full((n_dimensions,), 2.0),
                data["y"].new_full((n_dimensions,), 2.0),
            ).to_event(1),
        )
    return theta, c, alpha, beta, gamma, mu


def sample_correctness_calibration(data):
    """Sample a global correctness-only recalibration scale and bias."""
    zero = data["y"].new_tensor(0.0)
    scale = pyro.sample(
        "correctness_scale", dist.LogNormal(zero, data["y"].new_tensor(0.5))
    )
    bias = pyro.sample("correctness_bias", dist.Normal(zero, data["y"].new_tensor(3.0)))
    return scale, bias


def _require_tfidf_features(data):
    """Raise if the trainer forgot to attach TF-IDF feature matrices."""
    missing = [
        name for name in ("tfidf_prefix", "tfidf_token") if name not in data
    ]
    if missing:
        joined = ", ".join(missing)
        raise ValueError(f"Multidim TF-IDF experiment requires data key(s): {joined}")


def competing_risks_model(
    data,
    n_dimensions=1,
    calibrate_correctness=False,
    tfidf_effect_prior_scale=1.0,
    tfidf_variant=REPLACE_POSITION,
):
    """Define the multidimensional TF-IDF competing-risks likelihood."""
    tfidf_variant = validate_tfidf_variant(tfidf_variant)
    _require_tfidf_features(data)

    theta, c, alpha, beta, gamma, mu = sample_parameters(data, n_dimensions)
    (
        row_theta,
        row_c,
        row_alpha,
        row_beta,
        row_gamma,
        row_mu,
        row_tfidf_prefix,
        row_tfidf_token,
    ) = row_parameters(data, theta, c, alpha, beta, gamma, mu)
    tfidf_effect = sample_tfidf_effect(
        data, tfidf_effect_prior_scale, tfidf_variant
    )

    survival = log_survival(
        row_theta,
        row_alpha,
        row_beta,
        row_gamma,
        row_mu,
        row_c,
        data["t_star"],
        data["T_j"],
        row_tfidf_prefix,
        row_tfidf_token,
        tfidf_effect,
        tfidf_variant,
    )

    buzz = data["is_buzz"]
    buzz_tfidf_prefix = tfidf_score_at(
        row_tfidf_prefix[buzz], data["t_star"][buzz]
    )
    buzz_tfidf_token = tfidf_score_at(
        row_tfidf_token[buzz], data["t_star"][buzz]
    )
    buzz_logits = hazard_logit(
        row_theta[buzz],
        row_alpha[buzz],
        row_beta[buzz],
        row_gamma[buzz],
        row_mu[buzz],
        row_c[buzz],
        data["t_star"][buzz],
        data["T_j"][buzz],
        buzz_tfidf_prefix,
        buzz_tfidf_token,
        tfidf_effect,
        tfidf_variant,
    )
    correctness = correctness_logit(
        row_theta[buzz],
        row_alpha[buzz],
        row_beta[buzz],
        row_gamma[buzz],
        row_mu[buzz],
        data["t_star"][buzz],
        data["T_j"][buzz],
        buzz_tfidf_prefix,
        tfidf_effect,
        tfidf_variant,
    )
    if calibrate_correctness:
        scale, bias = sample_correctness_calibration(data)
        correctness = scale * correctness + bias

    log_likelihood = (
        survival.sum()
        + F.logsigmoid(buzz_logits).sum()
        + dist.Bernoulli(logits=correctness).log_prob(data["y"][buzz]).sum()
    )
    pyro.factor("multidim_tfidf_competing_risks_likelihood", log_likelihood)


def row_tfidf_scores(data):
    """Return row-level cumulative and local TF-IDF scores at ``t_star``."""
    tossup = data["tossup"]
    return (
        tfidf_score_at(data["tfidf_prefix"][tossup], data["t_star"]),
        tfidf_score_at(data["tfidf_token"][tossup], data["t_star"]),
    )


def posterior_row_predictions(
    data,
    posterior,
    calibrate_correctness=False,
    tfidf_variant=REPLACE_POSITION,
):
    """Return fitted correctness, hazard, survival, prefix score, and token score."""
    tfidf_variant = validate_tfidf_variant(tfidf_variant)
    (
        theta,
        c,
        alpha,
        beta,
        gamma,
        mu,
        tfidf_prefix,
        tfidf_token,
    ) = row_parameters(
        data,
        posterior["theta"],
        posterior["c"],
        posterior["alpha"],
        posterior["beta"],
        posterior["gamma"],
        posterior["mu"],
    )
    tfidf_effect = posterior_tfidf_effect(posterior, tfidf_variant)
    prefix_score = tfidf_score_at(tfidf_prefix, data["t_star"])
    token_score = tfidf_score_at(tfidf_token, data["t_star"])

    correctness_logits = correctness_logit(
        theta,
        alpha,
        beta,
        gamma,
        mu,
        data["t_star"],
        data["T_j"],
        prefix_score,
        tfidf_effect,
        tfidf_variant,
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
            alpha,
            beta,
            gamma,
            mu,
            c,
            data["t_star"],
            data["T_j"],
            prefix_score,
            token_score,
            tfidf_effect,
            tfidf_variant,
        )
    )
    survival = torch.exp(
        log_survival(
            theta,
            alpha,
            beta,
            gamma,
            mu,
            c,
            data["t_star"],
            data["T_j"],
            tfidf_prefix,
            tfidf_token,
            tfidf_effect,
            tfidf_variant,
        )
    )
    return correctness, hazard, survival, prefix_score, token_score


def expected_first_buzz_positions(
    data,
    posterior,
    tfidf_variant=REPLACE_POSITION,
):
    """Compute expected first-buzz relative positions with selected hazards."""
    tfidf_variant = validate_tfidf_variant(tfidf_variant)
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
        event = int(data["event"][row].item())
        slot = next_slot[event]
        roster[event, slot] = data["player"][row]
        roster_mask[event, slot] = True
        event_tossup[event] = data["tossup"][row]
        event_T[event] = data["T_j"][row]
        next_slot[event] += 1

    theta = posterior["theta"][roster]
    alpha = posterior["alpha"][event_tossup].unsqueeze(1)
    beta = posterior["beta"][event_tossup].unsqueeze(1)
    gamma = posterior["gamma"][event_tossup].unsqueeze(1)
    mu = posterior["mu"][event_tossup].unsqueeze(1)
    c = posterior["c"][roster]
    tfidf_prefix = data["tfidf_prefix"][event_tossup].unsqueeze(1)
    tfidf_token = data["tfidf_token"][event_tossup].unsqueeze(1)
    tfidf_effect = posterior_tfidf_effect(posterior, tfidf_variant)

    event_survival = data["y"].new_ones(n_events)
    expected = data["y"].new_zeros(n_events)
    for position in range(1, int(event_T.max().item()) + 1):
        active_event = position <= event_T
        t = data["y"].new_full((n_events, max_roster), float(position))
        T = event_T.unsqueeze(1).expand_as(t)
        prefix = tfidf_score_at(tfidf_prefix, t)
        token = tfidf_score_at(tfidf_token, t)
        hazard = torch.sigmoid(
            hazard_logit(
                theta,
                alpha,
                beta,
                gamma,
                mu,
                c,
                t,
                T,
                prefix,
                token,
                tfidf_effect,
                tfidf_variant,
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
