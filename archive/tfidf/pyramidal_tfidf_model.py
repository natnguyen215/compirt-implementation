"""Pyramidal tossup model with cumulative TF-IDF-aware clue timing.

The model uses the CompIRT correctness and hazard structure:

    correctness_ij(t) = theta_i^T alpha_j - d_j(t)
    hazard_ij(t) = correctness_ij(t) - c_i

The cumulative TF-IDF signal lowers the base difficulty curve by
'lambda_tfidf * p_j(t)' with a learned nonnegative coefficient.

Important shapes:

* 'theta' has shape
  '(n_players, n_dimensions)', 'c' has shape '(n_players,)', 'alpha' has shape
  '(n_tossups, n_dimensions)', and 'beta'/'gamma'/'mu' have shape '(n_tossups,)'.
* One precomputed feature matrix rides along in 'data' (attached by
  'tfidf.tfidf_features.attach_tfidf_prefix_scores'): 'tfidf_prefix' has shape
  '(n_tossups, max_T)' where 'max_T' is the longest tossup in tokens.
  'row_parameters' indexes it down to '(n_rows, max_T)' alongside the latent
  parameters.
* 'tfidf_score_at' gathers one column per row at a 1-indexed token position,
  collapsing '(n_rows, max_T)' features to '(n_rows,)' scores.
"""

from __future__ import annotations

import torch
import torch.nn.functional as F

from compirt_race import winner_log_prob, survival_stop
import pyro
import pyro.distributions as dist

from utils.prediction import event_rosters


def difficulty_curve(beta, gamma, mu, t, T_j):
    """Return tossup difficulty at token position 't'.

    This is the CompIRT Eq. 3 curve over relative token position.
    """
    # Eq. 3: d_j(t) = beta_j * sigmoid(gamma_j * (mu_j - position)).
    return beta * torch.sigmoid(gamma * (mu - t / T_j))


def tfidf_score_at(score_matrix, t):
    """Gather per-position TF-IDF scores at 1-indexed token positions 't'."""
    # Token positions are 1-indexed; the feature matrices are 0-indexed and
    # padded to 'max_position', so clamp before shifting down by one.
    max_position = score_matrix.shape[-1]
    index = t.long().clamp(min=1, max=max_position) - 1
    expanded_scores = score_matrix.expand(*index.shape, max_position)
    return torch.gather(expanded_scores, -1, index.unsqueeze(-1)).squeeze(-1)


def effective_difficulty(beta, gamma, mu, t, T_j, tfidf_prefix, tfidf_effect):
    """Return base difficulty reduced by cumulative TF-IDF."""
    return difficulty_curve(beta, gamma, mu, t, T_j) - tfidf_effect * tfidf_prefix


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
):
    """Return log-odds of a correct answer if the player buzzes at 't'."""
    if tfidf_prefix is None:
        tfidf_prefix = t / T_j
    if tfidf_effect is None:
        tfidf_effect = 0.0
    # Eq. 4 logit: theta_i^T alpha_j - d_j(t), with the TF-IDF-adjusted d_j(t).
    skill = (theta * alpha).sum(-1)
    difficulty = effective_difficulty(beta, gamma, mu, t, T_j, tfidf_prefix, tfidf_effect)
    return skill - difficulty


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
    tfidf_effect=None,
):
    """Return the buzz hazard logit at 't': correctness minus confidence 'c_i'."""
    return (
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
        )
        - c
    )


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
    tfidf_effect,
):
    """Return log probability of not buzzing at any position before 't_star'.

    Build one shared token grid, evaluate the hazard for every row-position
    pair, and sum the stable
    'log(1 - hazard)' over positions strictly before each row's stopping token.
    The cumulative TF-IDF feature is looked up on the same grid.
    """
    # Shared token-position grid [1, ..., max_t], broadcast to '(n_rows, max_t)'.
    max_t = int(t_star.max().item())
    positions = torch.arange(1, max_t + 1, device=t_star.device).unsqueeze(0)
    # Eq. 6 is strict-before survival, and Eq. 13 uses S(T_j) for dead tossups.
    # The published indexing stops NO-BUZZ rows at T_j - 1, so this comparison
    # must stay strict.
    before_stop = positions < t_star.unsqueeze(1)
    expanded_positions = positions.expand_as(before_stop)
    prefix = tfidf_score_at(tfidf_prefix.unsqueeze(1), expanded_positions)
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
        tfidf_effect,
    )
    # sum_{s < t*} log(1 - h_ij(s)); F.logsigmoid(-logits) is log(1 - hazard).
    return (F.logsigmoid(-logits) * before_stop).sum(1)


def row_parameters(data, theta, c, alpha, beta, gamma, mu):
    """Index entity-level parameters and TF-IDF features down to rows.

    Each row receives its latent parameters and its tossup's full '(max_T,)'
    cumulative TF-IDF prefix vector.
    """
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
    )


def sample_parameters(data, n_dimensions):
    """Sample player and tossup latent parameters from the Eq. 14 priors."""
    n_players = len(data["player_ids"])
    n_tossups = len(data["tossup_ids"])
    zero = data["y"].new_tensor(0.0)
    one = data["y"].new_tensor(1.0)
    vector_zero = data["y"].new_zeros(n_dimensions)
    vector_one = data["y"].new_ones(n_dimensions)

    # Held-out evaluation can attach informative per-player priors to 'data'.
    # Absent keys use the standard zero-location, unit-scale priors.
    theta_loc = data.get("theta_prior_loc", vector_zero)
    theta_scale = data.get("theta_prior_scale", vector_one)
    c_loc = data.get("c_prior_loc", zero)
    c_scale = data.get("c_prior_scale", one)
    with pyro.plate("players", n_players):
        # .to_event(1) treats the whole skill vector as one player's latent draw.
        theta = pyro.sample("theta", dist.Normal(theta_loc, theta_scale).to_event(1))
        c = pyro.sample("c", dist.Normal(c_loc, c_scale))

    with pyro.plate("tossups", n_tossups):
        alpha = pyro.sample("alpha", dist.Normal(vector_zero, vector_one).to_event(1))
        beta = pyro.sample("beta", dist.Normal(zero, one))
        gamma = pyro.sample("gamma", dist.HalfCauchy(5.0 * one))
        mu = pyro.sample(
            "mu",
            dist.Beta(data["y"].new_tensor(2.0), data["y"].new_tensor(2.0)),
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


def sample_tfidf_effect(data, prior_scale):
    """Sample the nonnegative cumulative TF-IDF difficulty coefficient."""
    scale = data["y"].new_tensor(float(prior_scale))
    return pyro.sample("tfidf_clue_effect", dist.HalfNormal(scale))


def posterior_tfidf_effect(posterior):
    """Return the fitted cumulative TF-IDF difficulty coefficient."""
    return posterior["tfidf_clue_effect"]


def _require_tfidf_features(data):
    """Raise if the trainer forgot to attach TF-IDF feature matrices."""
    if "tfidf_prefix" not in data:
        raise ValueError("TF-IDF experiment requires data key(s): tfidf_prefix")


def competing_risks_model(
    data,
    n_dimensions=1,
    calibrate_correctness=False,
    tfidf_effect_prior_scale=1.0,
):
    """Define the cumulative TF-IDF competing-risks likelihood.

    Every rostered player contributes survival before the stopping position. The
    actual first buzzer additionally
    contributes a hazard-at-'t_star' factor and an observed correctness factor,
    and the hand-computed joint log-likelihood is added with 'pyro.factor'.
    """
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
    ) = row_parameters(data, theta, c, alpha, beta, gamma, mu)
    tfidf_effect = sample_tfidf_effect(data, tfidf_effect_prior_scale)

    # Survival: every BUZZ, CENSORED, and NO-BUZZ row contributes.
    survival = log_survival(
        row_theta,
        row_alpha,
        row_beta,
        row_gamma,
        row_mu,
        row_c,
        survival_stop(data),
        data["T_j"],
        row_tfidf_prefix,
        tfidf_effect,
    )

    # Winner allocation uses all roster hazards at the stopping token;
    # correctness is observed only for the winner.
    buzz = data["is_buzz"]
    stop_tfidf_prefix = tfidf_score_at(row_tfidf_prefix, data["t_star"])
    stop_hazard_logits = hazard_logit(
        row_theta,
        row_alpha,
        row_beta,
        row_gamma,
        row_mu,
        row_c,
        data["t_star"],
        data["T_j"],
        stop_tfidf_prefix,
        tfidf_effect,
    )
    correctness = correctness_logit(
        row_theta[buzz],
        row_alpha[buzz],
        row_beta[buzz],
        row_gamma[buzz],
        row_mu[buzz],
        data["t_star"][buzz],
        data["T_j"][buzz],
        stop_tfidf_prefix[buzz],
        tfidf_effect,
    )
    if calibrate_correctness:
        # Apply calibration to correctness; hazard/timing keeps its base logit.
        scale, bias = sample_correctness_calibration(data)
        correctness = scale * correctness + bias

    # Combine survival for the full roster with the observed buzzer terms.
    log_likelihood = (
        survival.sum()
        + winner_log_prob(data, stop_hazard_logits).sum()
        + dist.Bernoulli(logits=correctness).log_prob(data["y"][buzz]).sum()
    )
    # Attach the hand-computed competing-risks log-likelihood with pyro.factor.
    pyro.factor("tfidf_competing_risks_likelihood", log_likelihood)


def posterior_row_predictions(data, posterior, calibrate_correctness=False):
    """Return fitted correctness, hazard, survival, and cumulative TF-IDF score.

    Indexing each fitted parameter by the row's player and tossup recreates the
    row-level inputs used during training; the cumulative TF-IDF score is returned
    as a prediction diagnostic.
    """
    (
        theta,
        c,
        alpha,
        beta,
        gamma,
        mu,
        tfidf_prefix,
    ) = row_parameters(
        data,
        posterior["theta"],
        posterior["c"],
        posterior["alpha"],
        posterior["beta"],
        posterior["gamma"],
        posterior["mu"],
    )
    tfidf_effect = posterior_tfidf_effect(posterior)
    prefix_score = tfidf_score_at(tfidf_prefix, data["t_star"])

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
            tfidf_effect,
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
            survival_stop(data),
            data["T_j"],
            tfidf_prefix,
            tfidf_effect,
        )
    )
    return correctness, hazard, survival, prefix_score


def expected_first_buzz_positions(data, posterior):
    """Compute the expected first-buzz relative position for each event.

    Observation rows are first regrouped into padded event rosters, then the
    function walks token by token using TF-IDF-adjusted hazards and accumulates
    't * P(first buzz at t)'. The returned position is E[t | a buzz occurs],
    matching the observed-buzz events used for evaluation.
    """
    # Rebuild the full first-buzz field before broadcasting fitted parameters.
    roster, roster_mask, event_tossup, event_T = event_rosters(data)
    n_events, max_roster = roster.shape

    # Parameter shapes now begin with (n_events, max_roster, ...). The extra
    # unsqueeze(1) on the tossup parameters broadcasts them across the roster.
    theta = posterior["theta"][roster]
    alpha = posterior["alpha"][event_tossup].unsqueeze(1)
    beta = posterior["beta"][event_tossup].unsqueeze(1)
    gamma = posterior["gamma"][event_tossup].unsqueeze(1)
    mu = posterior["mu"][event_tossup].unsqueeze(1)
    c = posterior["c"][roster]
    tfidf_prefix = data["tfidf_prefix"][event_tossup].unsqueeze(1)
    tfidf_effect = posterior_tfidf_effect(posterior)

    # event_survival is P(nobody has buzzed yet); expected accumulates
    # t * P(first buzz at t).
    event_survival = data["y"].new_ones(n_events)
    expected = data["y"].new_zeros(n_events)
    for position in range(1, int(event_T.max().item()) + 1):
        active_event = position <= event_T
        t = data["y"].new_full((n_events, max_roster), float(position))
        T = event_T.unsqueeze(1).expand_as(t)
        prefix = tfidf_score_at(tfidf_prefix, t)
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
                tfidf_effect,
            )
        )
        hazard = torch.where(roster_mask, hazard, torch.zeros_like(hazard))
        # Independent player hazards: P(nobody buzzes) is the product of each
        # player's no-buzz probability.
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
