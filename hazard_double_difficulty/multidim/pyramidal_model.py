"""Multidimensional pyramidal model with separate correctness/hazard difficulty.

The parent family ('multidimensional/multidim_mirt') fits one difficulty curve
per tossup and uses it for two jobs: how hard the tossup is to answer correctly,
and how tempting it is to buzz on. The hazard is the correctness logit shifted by
a single per-player scalar, so the two only differ by a constant:

    correctness_logit = sum_k r_jk * (theta_ik - d_jk(t))
    hazard_logit      = correctness_logit - c_i

This variant fits the same curve twice, under identical priors, and lets each
term have its own:

    correctness_logit = sum_k r^corr_jk * (theta_ik - d^corr_jk(t))
    hazard_logit      = sum_k r^haz_jk * (theta_ik - d^haz_jk(t)) - c_i

Everything else is the parent's math verbatim. The skill 'theta' and confidence
'c' stay shared, while each branch has its own relevance vector and difficulty
curve. Setting both relevance vectors and both curves equal recovers the parent
model exactly (see 'tests/test_hazard_double_difficulty.py').

Relevance uses independent Gamma vectors by default and can instead use
independent simplexes. Optional global correctness/hazard intercepts affect only
the final question cell; both switches are exposed by the trainer, while its
legacy defaults remain unchanged.

Important dimensions:

* 'n_rows' is the number of player-by-game-tossup observation rows.
* 'n_players' and 'n_tossups' count the unique players and tossups.
* 'n_dimensions' is the number of latent skill dimensions.

Important shapes:

* 'theta' has shape '(n_players, n_dimensions)' and 'c' has shape
  '(n_players,)'.
* 'r_correct', 'r_hazard', and each curve's 'beta', 'gamma', and 'mu' have shape
  '(n_tossups, n_dimensions)'.
* A curve is passed around as a '(beta, gamma, mu)' tuple, so 'row_parameters'
  returns the two curves grouped rather than six loose tensors.
"""

from __future__ import annotations

import torch
import torch.nn.functional as F
from torch.utils.checkpoint import checkpoint

import pyro
import pyro.distributions as dist

from utils.training import survival_chunk_size


# Opt-in link for the difficulty curves: sigmoid keeps d_jk(t) between 0 and
# beta_jk (the default); tanh lets it swing to -beta_jk late in the question.
# Both curves share the choice, so they stay the same functional form.
DIFFICULTY_LINKS = {"sigmoid": torch.sigmoid, "tanh": torch.tanh}
DEFAULT_RELEVANCE_PRIOR = "gamma"
SUPPORTED_RELEVANCE_PRIORS = (DEFAULT_RELEVANCE_PRIOR, "simplex")
TERMINAL_PRIOR_SCALE = 2.0


def validate_relevance_prior(relevance_prior):
    """Return a supported relevance prior name or raise a clear error."""
    if relevance_prior not in SUPPORTED_RELEVANCE_PRIORS:
        choices = ", ".join(SUPPORTED_RELEVANCE_PRIORS)
        raise ValueError(f"relevance_prior must be one of: {choices}")
    return relevance_prior


def difficulty_curve(beta, gamma, mu, t, T_j, link="sigmoid"):
    """Return the per-dimension difficulty d_jk(t) at token position 't'.

    Each latent dimension 'k' gets its own sigmoid, so 'beta', 'gamma', and 'mu'
    carry a trailing dimension axis and the return value keeps shape
    '(..., n_dimensions)'. The correctness and hazard curves both come from this
    one function, called with their own parameters.
    """
    # 't / T_j' is a scalar per row; unsqueeze so it broadcasts across dimensions.
    relative_position = (t / T_j).unsqueeze(-1)
    # d_jk(t) = beta_jk * link(gamma_jk * (mu_jk - t / T_j)).
    return beta * DIFFICULTY_LINKS[link](gamma * (mu - relative_position))


def curve_logit(theta, r, beta, gamma, mu, t, T_j, link="sigmoid"):
    """Return 'sum_k r_jk * (theta_ik - d_jk(t))' for one difficulty curve.

    This is one branch's relevance-weighted skill gap. Correctness and hazard
    call it with their own relevance and curve parameters.
    """
    # Per-dimension skill gap theta_ik - d_jk(t).
    gap = theta - difficulty_curve(beta, gamma, mu, t, T_j, link)
    # sum_k r_jk * (theta_ik - d_jk(t)); r_jk >= 0 (see sample_parameters).
    return (r * gap).sum(-1)


def terminal_intercept(effect, t, T_j):
    """Return ``effect`` in the final question cell and zero elsewhere."""
    if effect is None:
        return 0.0
    return effect * (t >= T_j).to(T_j.dtype)


def correctness_logit(
    theta, r, beta, gamma, mu, t, T_j, link="sigmoid", end=None
):
    """Return the log-odds of a correct answer if the player buzzes at 't'.

    Callers pass the *correctness* curve's parameters.
    """
    return curve_logit(theta, r, beta, gamma, mu, t, T_j, link) + terminal_intercept(
        end, t, T_j
    )


def hazard_logit(
    theta, r, beta, gamma, mu, c, t, T_j, link="sigmoid", end=None
):
    """Return the buzz hazard logit at 't', minus the confidence 'c_i'.

    Callers pass the *hazard* curve's parameters. Unlike the parent model this is
    not the correctness logit shifted by 'c' — it is its own weighted skill gap.
    """
    return (
        curve_logit(theta, r, beta, gamma, mu, t, T_j, link)
        - c
        + terminal_intercept(end, t, T_j)
    )


def log_survival(
    theta,
    r,
    beta,
    gamma,
    mu,
    c,
    t_star,
    T_j,
    link="sigmoid",
    chunk_size=None,
    t_start=None,
    end=None,
):
    """Return log probability of not buzzing across the interval '[t_start, t_star)'.

    Build one shared token grid, evaluate the hazard for every row-position
    pair, and sum the stable 'log(1 - hazard)' over positions in each row's risk
    interval. 't_start' (default 1) exceeds 1 only for phase-1 bounceback rows,
    where the opposing team enters the risk set at 't_neg + 1' after a neg;
    phase-0 rows keep the historical strict-before '[1, t_star)' survival exactly.

    Survival only ever evaluates hazards, so 'beta'/'gamma'/'mu' here are always
    the hazard curve's — the signature matches the parent family unchanged.
    """
    if chunk_size is None:
        chunk_size = survival_chunk_size()
    if chunk_size and t_star.shape[0] > chunk_size:
        # Each row's survival term is independent, so summing the grid in row
        # chunks under gradient checkpointing caps peak memory at one chunk's
        # (rows, positions, dimensions) grid while leaving the result identical
        # to the full-batch computation. 'link' is a non-tensor passthrough;
        # 't_start' is sliced per chunk alongside the other row tensors.
        parts = [
            checkpoint(
                log_survival,
                theta[lo:lo + chunk_size],
                r[lo:lo + chunk_size],
                beta[lo:lo + chunk_size],
                gamma[lo:lo + chunk_size],
                mu[lo:lo + chunk_size],
                c[lo:lo + chunk_size],
                t_star[lo:lo + chunk_size],
                T_j[lo:lo + chunk_size],
                link,
                use_reentrant=False,
                t_start=None if t_start is None else t_start[lo:lo + chunk_size],
                end=end,
            )
            for lo in range(0, t_star.shape[0], chunk_size)
        ]
        return torch.cat(parts)
    # Shared token-position grid [1, ..., max_t], broadcast to '(n_rows, max_t)'.
    max_t = int(t_star.max().item())
    positions = torch.arange(1, max_t + 1, device=t_star.device).unsqueeze(0)
    # Eq. 6 is strict-before survival, and Eq. 13 uses S(T_j) for dead tossups.
    # The published indexing stops NO-BUZZ rows at T_j - 1, so this comparison
    # must stay strict.
    before_stop = positions < t_star.unsqueeze(1)
    if t_start is not None:
        # Bounceback rows survive only from t_start onward; phase-0 rows pass
        # t_start = 1 (or None), for which this mask is all-True from position 1.
        before_stop = before_stop & (positions >= t_start.unsqueeze(1))
    # Unsqueeze row parameters so the hazard is evaluated at every row-position
    # pair; the dimension axis stays trailing. Logits are '(n_rows, max_t)'.
    logits = hazard_logit(
        theta.unsqueeze(1),
        r.unsqueeze(1),
        beta.unsqueeze(1),
        gamma.unsqueeze(1),
        mu.unsqueeze(1),
        c.unsqueeze(1),
        positions,
        T_j.unsqueeze(1),
        link,
        end,
    )
    # sum_{s < t*} log(1 - h_ij(s)); F.logsigmoid(-logits) is log(1 - hazard).
    return (F.logsigmoid(-logits) * before_stop).sum(1)


def row_parameters(
    data, theta, c, correct_r, hazard_r, correct_curve, hazard_curve
):
    """Index entity-level parameters down to one value per observation row.

    'correct_curve' and 'hazard_curve' are each a '(beta, gamma, mu)' tuple; they
    come back as tuples too, so call sites can splat them into the logit
    functions in the parent's positional order.
    """
    player = data["player"]
    tossup = data["tossup"]
    # player/tossup are row index vectors of shape '(n_rows,)'. theta/c come from
    # the player axis; both relevance vectors and curves come from the tossup axis. Every
    # returned tensor ends up '(n_rows, n_dimensions)'.
    return (
        theta[player],
        c[player],
        correct_r[tossup],
        hazard_r[tossup],
        tuple(parameter[tossup] for parameter in correct_curve),
        tuple(parameter[tossup] for parameter in hazard_curve),
    )


def sample_curve_parameters(data, n_dimensions, suffix):
    """Sample one difficulty curve's '(beta, gamma, mu)' under the parent priors.

    'suffix' names the branch ('correct' or 'hazard'). Both branches call this
    with the same arguments, so the two curves are identically distributed a
    priori and any fitted difference comes from the data.
    """
    vector_zero = data["y"].new_zeros(n_dimensions)
    vector_one = data["y"].new_ones(n_dimensions)
    beta = pyro.sample(
        f"beta_{suffix}",
        dist.Normal(vector_zero, vector_one).to_event(1),
    )
    gamma = pyro.sample(
        f"gamma_{suffix}", dist.HalfCauchy(5.0 * vector_one).to_event(1)
    )
    mu = pyro.sample(
        f"mu_{suffix}",
        dist.Beta(
            # new_full keeps the concentration tensors on the data's device.
            data["y"].new_full((n_dimensions,), 2.0),
            data["y"].new_full((n_dimensions,), 2.0),
        ).to_event(1),
    )
    return beta, gamma, mu


def survival_stop(data):
    """Return the exclusive survival stop, including the final no-buzz token."""
    no_buzz = data.get("is_no_buzz")
    if no_buzz is None:
        return data["t_star"]
    return data["t_star"] + no_buzz.to(data["t_star"].dtype)


def sample_terminal_intercepts(data):
    """Sample separate global final-cell effects for correctness and hazard."""
    zero = data["y"].new_tensor(0.0)
    scale = data["y"].new_tensor(TERMINAL_PRIOR_SCALE)
    return (
        pyro.sample("end_correct", dist.Normal(zero, scale)),
        pyro.sample("end_hazard", dist.Normal(zero, scale)),
    )


def posterior_terminal_intercepts(posterior):
    """Return fitted terminal effects, or ``(None, None)`` for older runs."""
    if "end_correct" not in posterior or "end_hazard" not in posterior:
        return None, None
    return posterior["end_correct"], posterior["end_hazard"]


def sample_parameters(
    data, n_dimensions, relevance_prior=DEFAULT_RELEVANCE_PRIOR
):
    """Sample player parameters and each branch's relevance and curve.

    Player priors follow Eq. 14: 'theta ~ N(0, I)' and 'c ~ N(0, 1)', with
    optional held-out overrides attached to 'data'. Every tossup difficulty
    parameter is per-dimension, and there are two full sets of them.
    """
    relevance_prior = validate_relevance_prior(relevance_prior)
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

    # Every tossup parameter carries a dimension axis, so each prior is wrapped in
    # .to_event(1) to keep the K coordinates as one tossup's vector draw.
    with pyro.plate("tossups", n_tossups):
        # Positive relevance so higher skill on a loaded dimension always helps.
        # Both branches use the configured prior but draw independently.
        relevance_distribution = (
            dist.Gamma(2.0 * vector_one, 2.0 * vector_one).to_event(1)
            if relevance_prior == "gamma"
            else dist.Dirichlet(vector_one)
        )
        correct_r = pyro.sample(
            "r_correct",
            relevance_distribution,
        )
        hazard_r = pyro.sample(
            "r_hazard",
            relevance_distribution,
        )
        correct_curve = sample_curve_parameters(data, n_dimensions, "correct")
        hazard_curve = sample_curve_parameters(data, n_dimensions, "hazard")
    return theta, c, correct_r, hazard_r, correct_curve, hazard_curve


def sample_correctness_calibration(data, with_scale=True):
    """Sample the global correctness recalibration scale and bias.

    `with_scale=False` drops the multiplicative term and returns `None` in its
    place, leaving a bias-only shift that moves the correctness level without
    compressing its spread (see `neg_test/README.md`).
    """
    zero = data["y"].new_tensor(0.0)
    scale = (
        pyro.sample("correctness_scale", dist.LogNormal(zero, data["y"].new_tensor(0.5)))
        if with_scale
        else None
    )
    bias = pyro.sample("correctness_bias", dist.Normal(zero, data["y"].new_tensor(3.0)))
    return scale, bias


def apply_correctness_calibration(correctness, scale, bias):
    """Recalibrate a correctness logit; a `scale` of None is the bias-only form."""
    if scale is None:
        return correctness + bias
    return scale * correctness + bias


def competing_risks_model(
    data,
    n_dimensions=1,
    calibrate_correctness=False,
    link="sigmoid",
    calibrate_scale=True,
    relevance_prior=DEFAULT_RELEVANCE_PRIOR,
    terminal_intercepts=False,
):
    """Define the double-difficulty competing-risks likelihood.

    Every rostered player contributes survival before the stopping position. The
    actual first buzzer additionally contributes a hazard-at-'t_star' factor and
    an observed correctness factor, and the hand-computed joint log-likelihood is
    added with 'pyro.factor'. Survival and hazard read the hazard curve;
    correctness reads the correctness curve.
    """
    theta, c, correct_r, hazard_r, correct_curve, hazard_curve = sample_parameters(
        data, n_dimensions, relevance_prior
    )
    end_correct, end_hazard = (
        sample_terminal_intercepts(data) if terminal_intercepts else (None, None)
    )
    row_theta, row_c, row_correct_r, row_hazard_r, row_correct, row_hazard = (
        row_parameters(
            data, theta, c, correct_r, hazard_r, correct_curve, hazard_curve
        )
    )

    # Survival: every BUZZ, CENSORED, and NO-BUZZ row contributes over its risk
    # interval [t_start, t_star). 'data.get' keeps manual data dicts (no t_start)
    # on the historical [1, t_star) path.
    survival = log_survival(
        row_theta,
        row_hazard_r,
        *row_hazard,
        row_c,
        survival_stop(data),
        data["T_j"],
        link,
        t_start=data.get("t_start"),
        end=end_hazard,
    )
    # Event term: only observed first buzzers contribute hazard and correctness.
    buzz = data["is_buzz"]
    buzz_logits = hazard_logit(
        row_theta[buzz],
        row_hazard_r[buzz],
        *(parameter[buzz] for parameter in row_hazard),
        row_c[buzz],
        data["t_star"][buzz],
        data["T_j"][buzz],
        link,
        end_hazard,
    )
    correctness = correctness_logit(
        row_theta[buzz],
        row_correct_r[buzz],
        *(parameter[buzz] for parameter in row_correct),
        data["t_star"][buzz],
        data["T_j"][buzz],
        link,
        end_correct,
    )
    if calibrate_correctness:
        # Apply calibration to correctness; hazard/timing keeps its base logit.
        scale, bias = sample_correctness_calibration(data, with_scale=calibrate_scale)
        correctness = apply_correctness_calibration(correctness, scale, bias)

    log_likelihood = (
        # Sum log survival over every player-event row.
        survival.sum()
        # Sum log hazard and correctness log likelihood over first-buzzer rows.
        + F.logsigmoid(buzz_logits).sum()
        + dist.Bernoulli(logits=correctness).log_prob(data["y"][buzz]).sum()
    )
    pyro.factor("multidim_double_difficulty_competing_risks_likelihood", log_likelihood)


def posterior_curves(posterior):
    """Return the fitted '(beta, gamma, mu)' tuples for both curves."""
    return (
        (posterior["beta_correct"], posterior["gamma_correct"], posterior["mu_correct"]),
        (posterior["beta_hazard"], posterior["gamma_hazard"], posterior["mu_hazard"]),
    )


def posterior_row_predictions(
    data, posterior, calibrate_correctness=False, link="sigmoid", calibrate_scale=True
):
    """Return fitted correctness, hazard, and survival for each row.

    Indexing each fitted parameter by the row's player and tossup recreates the
    row-level inputs used during training.
    """
    correct_curve, hazard_curve = posterior_curves(posterior)
    end_correct, end_hazard = posterior_terminal_intercepts(posterior)
    theta, c, correct_r, hazard_r, row_correct, row_hazard = row_parameters(
        data,
        posterior["theta"],
        posterior["c"],
        posterior["r_correct"],
        posterior["r_hazard"],
        correct_curve,
        hazard_curve,
    )
    correctness_logits = correctness_logit(
        theta,
        correct_r,
        *row_correct,
        data["t_star"],
        data["T_j"],
        link,
        end_correct,
    )
    if calibrate_correctness:
        correctness_logits = apply_correctness_calibration(
            correctness_logits,
            posterior["correctness_scale"] if calibrate_scale else None,
            posterior["correctness_bias"],
        )
    correctness = torch.sigmoid(correctness_logits)
    hazard = torch.sigmoid(
        hazard_logit(
            theta,
            hazard_r,
            *row_hazard,
            c,
            data["t_star"],
            data["T_j"],
            link,
            end_hazard,
        )
    )
    survival = torch.exp(
        log_survival(
            theta,
            hazard_r,
            *row_hazard,
            c,
            survival_stop(data),
            data["T_j"],
            link,
            t_start=data.get("t_start"),
            end=end_hazard,
        )
    )
    return correctness, hazard, survival


def expected_first_buzz_positions(data, posterior, link="sigmoid"):
    """Compute the expected first-buzz relative position for each event.

    Observation rows are first regrouped into padded event rosters, then the
    function walks token by token and accumulates 't * P(first buzz at t)'. The
    returned position is E[t | a buzz occurs], matching the observed-buzz events
    used for evaluation. Timing is a pure hazard quantity, so only the hazard
    curve is read here.
    """
    n_events = len(data["event_ids"])
    # First-buzz timing is a full-field phase-0 quantity; skip phase-1 bounceback
    # rows (they share an event_id but are an opponent-only continuation).
    # Absent 'is_phase0' (pre-bounceback data) means every row is phase 0.
    phase0 = data.get("is_phase0")
    if phase0 is None:
        phase0 = torch.ones(
            len(data["event"]), dtype=torch.bool, device=data["event"].device
        )
    counts = torch.bincount(data["event"][phase0], minlength=n_events)
    max_roster = int(counts.max().item())
    # Training rows are one player at a time; regroup them into per-event roster
    # matrices so all of an event's players can be stepped through together.
    roster = data["player"].new_zeros((n_events, max_roster))
    roster_mask = torch.zeros(
        (n_events, max_roster), dtype=torch.bool, device=data["event"].device
    )
    next_slot = [0] * n_events
    event_tossup = data["tossup"].new_zeros(n_events)
    event_T = data["T_j"].new_ones(n_events)
    for row in range(len(data["event"])):
        if not bool(phase0[row]):
            continue
        event = int(data["event"][row].item())
        slot = next_slot[event]
        roster[event, slot] = data["player"][row]
        roster_mask[event, slot] = True
        event_tossup[event] = data["tossup"][row]
        event_T[event] = data["T_j"][row]
        next_slot[event] += 1

    # Parameter shapes now begin with (n_events, max_roster, ...). The extra
    # unsqueeze(1) on the tossup parameters broadcasts them across the roster.
    _, hazard_curve = posterior_curves(posterior)
    _, end_hazard = posterior_terminal_intercepts(posterior)
    theta = posterior["theta"][roster]
    r = posterior["r_hazard"][event_tossup].unsqueeze(1)
    beta, gamma, mu = (
        parameter[event_tossup].unsqueeze(1) for parameter in hazard_curve
    )
    c = posterior["c"][roster]

    # event_survival is P(nobody has buzzed yet); expected accumulates
    # t * P(first buzz at t).
    event_survival = data["y"].new_ones(n_events)
    expected = data["y"].new_zeros(n_events)
    for position in range(1, int(event_T.max().item()) + 1):
        active_event = position <= event_T
        t = data["y"].new_full((n_events, max_roster), float(position))
        T = event_T.unsqueeze(1).expand_as(t)
        hazard = torch.sigmoid(
            hazard_logit(theta, r, beta, gamma, mu, c, t, T, link, end_hazard)
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
