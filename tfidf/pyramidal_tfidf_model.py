"""Baseline pyramidal tossup model with TF-IDF-adjusted difficulty.

This is a local experiment copy. It does not modify or import the root
'pyramidal_model.py'. The model keeps the CompIRT structure:

    correctness_ij(t) = theta_i^T alpha_j - d'_j(t)
    hazard_ij(t) = correctness_ij(t) - c_i

where the TF-IDF feature adjusts the effective difficulty 'd'_j(t)' rather than
adding a separate hazard-only buzz trigger:

    d'_j(t) = d_j(t) - lambda_tfidf * tfidf_prefix_j(t)

Here 'lambda_tfidf' is a single learned nonnegative coefficient
('tfidf_clue_effect') and 'tfidf_prefix_j(t)' is the normalized cumulative
TF-IDF score revealed through token 't'. Difficulty therefore drops as more
rare-clue evidence accumulates, which makes later text easier to answer and
easier to buzz on.

Important Dimensions (same as the baseline):

* 'n_rows' is the number of player-by-game-tossup observation rows.
* 'n_players' and 'n_tossups' count the unique players and tossups.
* 'n_dimensions' is the number of latent skill dimensions.
* 'max_length' is the longest tossup length; TF-IDF features are padded to it.

Important Shapes:

* Latent parameters match the baseline: 'theta' is '(n_players, n_dimensions)',
  'alpha' is '(n_tossups, n_dimensions)', and 'c/beta/gamma/mu' are
  '(n_tossups,)' or '(n_players,)'.
* The TF-IDF feature lives on 'data': 'data["tfidf_prefix"]' has shape
  '(n_tossups, max_length)'.
* 'tfidf_clue_effect' is a single learned scalar shared across tossups.
"""

from __future__ import annotations

import torch
import torch.nn.functional as F

import pyro
import pyro.distributions as dist


def difficulty_curve(beta, gamma, mu, t, T_j):
    """Return baseline tossup difficulty at token position 't' (before TF-IDF)."""
    # Eq. 3: b_j(t) = beta_j * sigmoid(gamma_j * (mu_j - t / T_j)).
    return beta * torch.sigmoid(gamma * (mu - t / T_j))


def tfidf_score_at(prefix_score, t):
    """Gather cumulative TF-IDF scores at token positions 't'.

    'prefix_score' ends in the token-position (max_length) dimension; its leading
    dimensions may be broadcast against 't'. Positions are 1-indexed and clamped
    into range, so 't' selects the score revealed through that token. The
    returned tensor has the broadcast shape of 't'.
    """
    max_position = prefix_score.shape[-1]
    # 1-indexed positions clamped into [1, max_length], then shifted to 0-indexed.
    index = t.long().clamp(min=1, max=max_position) - 1
    expanded_prefix = prefix_score.expand(*index.shape, max_position)
    return torch.gather(expanded_prefix, -1, index.unsqueeze(-1)).squeeze(-1)


def adjusted_difficulty(
    beta,
    gamma,
    mu,
    t,
    T_j,
    tfidf_prefix,
    tfidf_clue_effect,
):
    """Return effective difficulty d'_j(t) after TF-IDF evidence adjusts it."""
    # d'_j(t) = d_j(t) - lambda_tfidf * tfidf_prefix_j(t). A positive adjustment
    # lowers difficulty as clue evidence accumulates.
    adjustment = tfidf_clue_effect * tfidf_prefix
    return difficulty_curve(beta, gamma, mu, t, T_j) - adjustment


def correctness_logit(
    theta,
    alpha,
    beta,
    gamma,
    mu,
    t,
    T_j,
    tfidf_prefix,
    tfidf_clue_effect,
):
    """Return log-odds of a correct answer if the player buzzes at 't'.

    Same as the baseline correctness logit, but the effective (TF-IDF-adjusted)
    difficulty replaces the plain sigmoid difficulty.
    """
    # theta_i^T alpha_j.
    skill = (theta * alpha).sum(-1)
    difficulty = adjusted_difficulty(
        beta,
        gamma,
        mu,
        t,
        T_j,
        tfidf_prefix,
        tfidf_clue_effect,
    )
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
    tfidf_prefix,
    tfidf_clue_effect,
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
            tfidf_clue_effect,
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
    tfidf_clue_effect,
):
    """Return log probability of not buzzing at any position before 't_star'.

    Same survival term as the baseline, but the hazard at each position uses the
    TF-IDF-adjusted difficulty, so the TF-IDF score must be gathered at every
    position on the shared grid rather than only at 't_star'.
    """
    # Shared token-position grid [1, ..., max_t], broadcast to '(n_rows, max_t)'.
    max_t = int(t_star.max().item())
    positions = torch.arange(1, max_t + 1, device=t_star.device).unsqueeze(0)
    before_stop = positions < t_star.unsqueeze(1)
    # Look up the TF-IDF feature for every row-position pair on the grid.
    expanded_positions = positions.expand_as(before_stop)
    tfidf = tfidf_score_at(tfidf_prefix.unsqueeze(1), expanded_positions)
    # Unsqueeze row parameters so the hazard is evaluated at every position.
    logits = hazard_logit(
        theta.unsqueeze(1),
        alpha.unsqueeze(1),
        beta.unsqueeze(1),
        gamma.unsqueeze(1),
        mu.unsqueeze(1),
        c.unsqueeze(1),
        positions,
        T_j.unsqueeze(1),
        tfidf,
        tfidf_clue_effect,
    )
    # sum_{s < t*} log(1 - h_ij(s)); F.logsigmoid(-logits) is log(1 - hazard).
    return (F.logsigmoid(-logits) * before_stop).sum(1)


def row_parameters(data, theta, c, alpha, beta, gamma, mu):
    """Index entity-level parameters down to one value per observation row.

    Returns the six latent parameters plus the per-tossup TF-IDF prefix feature
    row, all aligned to observation rows.
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
        # TF-IDF feature matrix is stored per tossup; index it the same way.
        data["tfidf_prefix"][tossup],
    )


def sample_parameters(data, n_dimensions):
    """Sample player and tossup latent parameters (identical to the baseline)."""
    n_players = len(data["player_ids"])
    n_tossups = len(data["tossup_ids"])
    zero = data["y"].new_tensor(0.0)
    one = data["y"].new_tensor(1.0)
    vector_zero = data["y"].new_zeros(n_dimensions)
    vector_one = data["y"].new_ones(n_dimensions)

    # Eq. 14 player priors, with optional held-out overrides attached to 'data'.
    theta_loc = data.get("theta_prior_loc", vector_zero)
    theta_scale = data.get("theta_prior_scale", vector_one)
    c_loc = data.get("c_prior_loc", zero)
    c_scale = data.get("c_prior_scale", one)
    with pyro.plate("players", n_players):
        theta = pyro.sample("theta", dist.Normal(theta_loc, theta_scale).to_event(1))
        c = pyro.sample("c", dist.Normal(c_loc, c_scale))

    # Eq. 14 tossup priors: alpha ~ N(0, I), beta ~ N(0, 1),
    # gamma ~ Half-Cauchy(5), mu ~ Beta(2, 2).
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


def sample_tfidf_effects(data, prior_scale):
    """Sample the nonnegative TF-IDF difficulty coefficient lambda_tfidf.

    A HalfNormal keeps the effect nonnegative so accumulated clue evidence can
    only ever lower effective difficulty, never raise it.
    """
    scale = data["y"].new_tensor(float(prior_scale))
    tfidf_clue_effect = pyro.sample("tfidf_clue_effect", dist.HalfNormal(scale))
    return tfidf_clue_effect


def competing_risks_model(
    data,
    n_dimensions=1,
    calibrate_correctness=False,
    tfidf_effect_prior_scale=1.0,
):
    """Define the TF-IDF-adjusted competing-risks likelihood.

    Structurally identical to the baseline competing-risks model, plus the
    single learned 'tfidf_clue_effect' coefficient threaded through survival,
    hazard, and correctness.
    """
    # The TF-IDF feature matrix must be attached to 'data' before fitting.
    if "tfidf_prefix" not in data:
        raise ValueError("TF-IDF experiment requires data key: tfidf_prefix")

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
    tfidf_clue_effect = sample_tfidf_effects(data, tfidf_effect_prior_scale)

    # Survival: every BUZZ, CENSORED, and NO-BUZZ row contributes.
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
        tfidf_clue_effect,
    )

    # Event term: only observed first buzzers contribute hazard and correctness.
    buzz = data["is_buzz"]
    # Gather each first buzzer's TF-IDF score at its own buzz position 't_star'.
    buzz_tfidf_prefix = tfidf_score_at(
        row_tfidf_prefix[buzz], data["t_star"][buzz]
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
        tfidf_clue_effect,
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
        tfidf_clue_effect,
    )
    if calibrate_correctness:
        # Recalibrate correctness only; hazard/timing keep the original logit.
        scale, bias = sample_correctness_calibration(data)
        correctness = scale * correctness + bias

    log_likelihood = (
        # Sum log survival over every player-event row.
        survival.sum()
        # Sum log hazard and correctness log likelihood over first-buzzer rows.
        + F.logsigmoid(buzz_logits).sum()
        + dist.Bernoulli(logits=correctness).log_prob(data["y"][buzz]).sum()
    )
    pyro.factor("tfidf_competing_risks_likelihood", log_likelihood)


def row_tfidf_scores(data):
    """Return each observation row's cumulative TF-IDF score at 't_star'."""
    return tfidf_score_at(data["tfidf_prefix"][data["tossup"]], data["t_star"])


def posterior_row_predictions(data, posterior, calibrate_correctness=False):
    """Return fitted correctness, hazard, survival, and TF-IDF score per row.

    Indexing each fitted parameter by the row's player and tossup recreates the
    row-level inputs used during training. In addition to the three fitted
    probabilities, this returns the diagnostic TF-IDF score for downstream CSV
    output.
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
    tfidf_clue_effect = posterior["tfidf_clue_effect"]
    # Diagnostic cumulative TF-IDF score at 't_star'.
    tfidf_score = tfidf_score_at(tfidf_prefix, data["t_star"])
    correctness_logits = correctness_logit(
        theta,
        alpha,
        beta,
        gamma,
        mu,
        data["t_star"],
        data["T_j"],
        tfidf_score,
        tfidf_clue_effect,
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
            tfidf_score,
            tfidf_clue_effect,
        )
    )
    # Survival needs the full per-position TF-IDF matrix, not the 't_star' slice.
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
            tfidf_clue_effect,
        )
    )
    return correctness, hazard, survival, tfidf_score


def expected_first_buzz_positions(data, posterior):
    """Compute expected first-buzz relative positions with TF-IDF hazards.

    Same event-roster walk as the baseline model; the only difference is that
    each position's hazard uses the TF-IDF-adjusted difficulty, so the TF-IDF
    score is gathered at every step.
    """
    n_events = len(data["event_ids"])
    counts = torch.bincount(data["event"], minlength=n_events)
    max_roster = int(counts.max().item())
    # Regroup one-player-at-a-time training rows into per-event roster matrices.
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

    # Tossup parameters get an unsqueeze(1) to broadcast across the roster axis.
    theta = posterior["theta"][roster]
    alpha = posterior["alpha"][event_tossup].unsqueeze(1)
    beta = posterior["beta"][event_tossup].unsqueeze(1)
    gamma = posterior["gamma"][event_tossup].unsqueeze(1)
    mu = posterior["mu"][event_tossup].unsqueeze(1)
    c = posterior["c"][roster]
    tfidf_prefix = data["tfidf_prefix"][event_tossup].unsqueeze(1)
    tfidf_clue_effect = posterior["tfidf_clue_effect"]

    # event_survival is P(nobody has buzzed yet); expected accumulates
    # t * P(first buzz at t).
    event_survival = data["y"].new_ones(n_events)
    expected = data["y"].new_zeros(n_events)
    for position in range(1, int(event_T.max().item()) + 1):
        active_event = position <= event_T
        t = data["y"].new_full((n_events, max_roster), float(position))
        T = event_T.unsqueeze(1).expand_as(t)
        tfidf = tfidf_score_at(tfidf_prefix, t)
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
                tfidf,
                tfidf_clue_effect,
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
    expected = expected + event_T * event_survival
    relative = (expected / event_T).detach().cpu().tolist()
    return dict(zip(data["event_ids"], relative))
