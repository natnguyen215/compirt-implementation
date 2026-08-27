"""Bernstein pyramidal model with separate correctness/hazard difficulty.

The parent family ('polynomial_compirt') fits one strictly-decreasing Bernstein
difficulty curve per tossup and uses it for two jobs: how hard the tossup is to
answer correctly, and how tempting it is to buzz on. The hazard is the
correctness logit shifted by a single per-player scalar, so the two only differ
by a constant:

    correctness_logit = sum_k r_jk * (theta_ik - d_jk(x))
    hazard_logit      = correctness_logit - c_i

This variant fits the same curve twice, under identical priors, and lets each
term have its own:

    correctness_logit = sum_k r^corr_jk * (theta_ik - d^corr_jk(x))
    hazard_logit      = sum_k r^haz_jk * (theta_ik - d^haz_jk(x)) - c_i

Everything else is the parent's math verbatim, including the parameterization
that makes each curve strictly decreasing on '[0, 1]' by construction. For
relative token position 'x = t / T_j' and degree 'p':

    d_jk(x)   = sum_m b_jkm * B_m,p(x)
    b_jk0     = start_jk
    delta_jkm = total_drop_jk * drop_share_jkm
    b_jkm     = b_jk,m-1 - delta_jkm

Both curves share the degree, the Dirichlet concentration, the skill 'theta',
and the confidence 'c'. Their relevance vectors are separate draws under the
same configurable prior. Optionally, each branch learns one global population
location for its start-difficulty prior. Setting both relevance vectors and
both curves equal recovers the parent model exactly (see
'tests/test_hazard_double_difficulty.py').

Important shapes:

* 'theta' is '(n_players, n_dimensions)' and 'c' is '(n_players,)'.
* 'r_correct', 'r_hazard', and each curve's 'start_difficulty' and
  'total_drop' are '(n_tossups, n_dimensions)'; each curve's 'drop_proportions' is
  '(n_tossups, n_dimensions, degree)' — one share per control-value step, hence
  'degree' shares for 'degree + 1' controls.
* A curve is passed around as a '(start_difficulty, total_drop,
  drop_proportions)' tuple, so 'row_parameters' returns the two curves grouped
  rather than six loose tensors.
"""

from __future__ import annotations

import math

import pyro
import pyro.distributions as dist
import torch
import torch.nn.functional as F
from torch.utils.checkpoint import checkpoint

from utils.training import survival_chunk_size


MIN_DEGREE = 3
MAX_DEGREE = 6
SUPPORTED_DEGREES = range(MIN_DEGREE, MAX_DEGREE + 1)
DEFAULT_DROP_CONCENTRATION = 2.0
TOTAL_DROP_LOG_SCALE = 0.5
CURVE_LOCATION_PRIOR_SCALE = 1.0
CURVE_START_PRIOR_SCALE = 1.0
PLAYER_PROPENSITY_SCALE_PRIOR = 1.0
DEFAULT_RELEVANCE_PRIOR = "gamma"
SUPPORTED_RELEVANCE_PRIORS = (DEFAULT_RELEVANCE_PRIOR, "simplex")


def validate_degree(degree: int) -> int:
    """Return a supported polynomial degree or raise a clear error."""
    degree = int(degree)
    if degree not in SUPPORTED_DEGREES:
        raise ValueError(
            f"degree must be between {MIN_DEGREE} and {MAX_DEGREE}, got {degree}"
        )
    return degree


def validate_drop_concentration(value: float) -> float:
    """Return a finite, positive Dirichlet concentration."""
    value = float(value)
    if not math.isfinite(value) or value <= 0:
        raise ValueError("drop_concentration must be finite and greater than zero")
    return value


def validate_relevance_prior(value: str) -> str:
    """Return a supported relevance prior name or raise a clear error."""
    value = str(value)
    if value not in SUPPORTED_RELEVANCE_PRIORS:
        choices = ", ".join(SUPPORTED_RELEVANCE_PRIORS)
        raise ValueError(f"relevance_prior must be one of {choices}, got {value!r}")
    return value


def bernstein_basis(x: torch.Tensor, degree: int) -> torch.Tensor:
    """Return the degree-'p' Bernstein basis 'B_m,p(x)' as a trailing axis.

    'B_m,p(x) = C(p, m) * x^m * (1 - x)^(p - m)'. The basis is nonnegative and
    sums to one at every 'x', so a curve never leaves the range of its control
    values.
    """
    powers = torch.arange(degree + 1, dtype=x.dtype, device=x.device)
    binomial = x.new_tensor([math.comb(degree, m) for m in range(degree + 1)])
    return (
        binomial
        * x.unsqueeze(-1).pow(powers)
        * (1.0 - x).unsqueeze(-1).pow(degree - powers)
    )


def control_values(
    start_difficulty: torch.Tensor,
    total_drop: torch.Tensor,
    drop_proportions: torch.Tensor,
) -> torch.Tensor:
    """Build strictly ordered Bernstein control values from start/range/shape.

    The shares are positive and sum to one, so the running total consumes
    exactly 'total_drop': the last control value is 'start - total_drop'.
    Returns '(..., degree + 1)'.
    """
    drops = total_drop.unsqueeze(-1) * drop_proportions
    later = start_difficulty.unsqueeze(-1) - drops.cumsum(-1)
    return torch.cat([start_difficulty.unsqueeze(-1), later], dim=-1)


def difficulty_curve(start_difficulty, total_drop, drop_proportions, t, T_j):
    """Return the per-dimension difficulty 'd_jk(x)' at token position 't'.

    The correctness and hazard curves both come from this one function, called
    with their own parameters.
    """
    # Every dimension shares the same relative position, so the basis carries no
    # dimension axis; unsqueeze(-2) broadcasts it across the K control rows.
    basis = bernstein_basis(t / T_j, drop_proportions.shape[-1])
    controls = control_values(start_difficulty, total_drop, drop_proportions)
    # sum_m b_jkm * B_m,p(x), collapsing the control axis to '(..., K)'.
    return (controls * basis.unsqueeze(-2)).sum(-1)


def curve_logit(theta, r, start_difficulty, total_drop, drop_proportions, t, T_j):
    """Return 'sum_k r_jk * (theta_ik - d_jk(x))' for one difficulty curve.

    This is one branch's relevance-weighted skill gap. Correctness and hazard
    call it with their own relevance and curve parameters.
    """
    gap = theta - difficulty_curve(
        start_difficulty, total_drop, drop_proportions, t, T_j
    )
    # sum_k r_jk * (theta_ik - d_jk(x)); r_jk >= 0 (see sample_parameters).
    return (r * gap).sum(-1)


def terminal_intercept(effect, t, T_j):
    """Return 'effect' in the final cell only, zero everywhere else.

    Position 'T_j' also absorbs the whole post-reading buzz window, so its
    discrete-time survival cell spans far more real time than any single token.
    'None' reproduces the model as it was before that cell had its own
    intercept. See 'analysis/terminal_cell/' for the measurement behind it.
    """
    if effect is None:
        return 0.0
    return effect * (t >= T_j).to(T_j.dtype)


def correctness_logit(
    theta, r, start_difficulty, total_drop, drop_proportions, t, T_j, end=None
):
    """Return the log-odds of a correct answer if the player buzzes at 't'.

    Callers pass the *correctness* curve's parameters.
    """
    return curve_logit(
        theta, r, start_difficulty, total_drop, drop_proportions, t, T_j
    ) + terminal_intercept(end, t, T_j)


def hazard_logit(
    theta, r, start_difficulty, total_drop, drop_proportions, c, t, T_j, end=None
):
    """Return the buzz hazard logit at 't', minus the confidence 'c_i'.

    Callers pass the *hazard* curve's parameters. Unlike the parent model this is
    not the correctness logit shifted by 'c' — it is its own weighted skill gap.
    """
    return (
        curve_logit(theta, r, start_difficulty, total_drop, drop_proportions, t, T_j)
        - c
        + terminal_intercept(end, t, T_j)
    )


def log_survival(
    theta,
    r,
    start_difficulty,
    total_drop,
    drop_proportions,
    c,
    t_star,
    T_j,
    chunk_size=None,
    t_start=None,
    end=None,
):
    """Return log probability of not buzzing across '[t_start, t_star)'.

    Build one shared token grid, evaluate the hazard for every row-position
    pair, and sum the stable 'log(1 - hazard)' over positions in each row's risk
    interval. 't_start' (default 1) exceeds 1 only for phase-1 bounceback rows.

    Survival only ever evaluates hazards, so the curve parameters here are always
    the hazard curve's — the signature matches the parent family unchanged.
    """
    if chunk_size is None:
        chunk_size = survival_chunk_size()
    if chunk_size and t_star.shape[0] > chunk_size:
        # Each row's survival term is independent, so summing the grid in row
        # chunks under gradient checkpointing caps peak memory at one chunk's
        # (rows, positions, dimensions) grid while leaving the result identical
        # to the full-batch computation.
        parts = [
            checkpoint(
                log_survival,
                theta[lo:lo + chunk_size],
                r[lo:lo + chunk_size],
                start_difficulty[lo:lo + chunk_size],
                total_drop[lo:lo + chunk_size],
                drop_proportions[lo:lo + chunk_size],
                c[lo:lo + chunk_size],
                t_star[lo:lo + chunk_size],
                T_j[lo:lo + chunk_size],
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
    # Eq. 6 is strict-before survival, and Eq. 13 uses S(T_j) for dead tossups,
    # so this comparison must stay strict.
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
        start_difficulty.unsqueeze(1),
        total_drop.unsqueeze(1),
        drop_proportions.unsqueeze(1),
        c.unsqueeze(1),
        positions,
        T_j.unsqueeze(1),
        end,
    )
    # sum_{s < t*} log(1 - h_ij(s)); F.logsigmoid(-logits) is log(1 - hazard).
    return (F.logsigmoid(-logits) * before_stop).sum(1)


def row_parameters(
    data, theta, c, correct_r, hazard_r, correct_curve, hazard_curve
):
    """Index entity-level parameters down to one value per observation row.

    'correct_curve' and 'hazard_curve' are each a '(start_difficulty, total_drop,
    drop_proportions)' tuple; they come back as tuples too, so call sites can
    splat them into the logit functions in the parent's positional order.
    """
    player = data["player"]
    tossup = data["tossup"]
    return (
        theta[player],
        c[player],
        correct_r[tossup],
        hazard_r[tossup],
        tuple(parameter[tossup] for parameter in correct_curve),
        tuple(parameter[tossup] for parameter in hazard_curve),
    )


def survival_stop(data):
    """Return the exclusive survival stop, including the final no-buzz token."""
    no_buzz = data.get("is_no_buzz")
    if no_buzz is None:
        return data["t_star"]
    return data["t_star"] + no_buzz.to(data["t_star"].dtype)


def sample_curve_locations(data):
    """Sample population locations for correctness and hazard curve starts."""
    zero = data["y"].new_tensor(0.0)
    scale = data["y"].new_tensor(CURVE_LOCATION_PRIOR_SCALE)
    return (
        pyro.sample("curve_location_correct", dist.Normal(zero, scale)),
        pyro.sample("curve_location_hazard", dist.Normal(zero, scale)),
    )


def sample_curve_parameters(
    data, n_dimensions, concentration, suffix, location=None
):
    """Sample one Bernstein curve's parameters under its branch location.

    'suffix' names the branch ('correct' or 'hazard'). Both branches call this
    with the same arguments, so the two curves are identically distributed a
    priori and any fitted difference comes from the data.
    """
    if location is None:
        location = data["y"].new_tensor(0.0)
    vector_zero = data["y"].new_zeros(n_dimensions)
    vector_one = data["y"].new_ones(n_dimensions)
    start_difficulty = pyro.sample(
        f"start_difficulty_{suffix}",
        dist.Normal(
            location,
            CURVE_START_PRIOR_SCALE * vector_one,
        ).to_event(1),
    )
    # LogNormal keeps the total decline strictly positive, which is what
    # makes the fitted curve strictly (not weakly) decreasing.
    total_drop = pyro.sample(
        f"total_drop_{suffix}",
        dist.LogNormal(vector_zero, TOTAL_DROP_LOG_SCALE * vector_one).to_event(1),
    )
    # Dirichlet is already a distribution over the trailing share axis, so
    # .to_event(1) here folds in the dimension axis.
    drop_proportions = pyro.sample(
        f"drop_proportions_{suffix}", dist.Dirichlet(concentration).to_event(1)
    )
    return start_difficulty, total_drop, drop_proportions


TERMINAL_PRIOR_SCALE = 2.0


def sample_terminal_intercepts(data):
    """Sample the correctness and hazard intercepts for the final cell."""
    zero = data["y"].new_tensor(0.0)
    scale = data["y"].new_tensor(TERMINAL_PRIOR_SCALE)
    return (
        pyro.sample("end_correct", dist.Normal(zero, scale)),
        pyro.sample("end_hazard", dist.Normal(zero, scale)),
    )


def posterior_terminal_intercepts(posterior):
    """Return saved terminal intercepts, or '(None, None)' for older fits."""
    if "end_correct" not in posterior or "end_hazard" not in posterior:
        return None, None
    return posterior["end_correct"], posterior["end_hazard"]


def sample_parameters(
    data,
    n_dimensions,
    degree,
    drop_concentration=DEFAULT_DROP_CONCENTRATION,
    relevance_prior=DEFAULT_RELEVANCE_PRIOR,
    learned_curve_locations=False,
    player_neg_propensity=False,
):
    """Sample player parameters and each branch's relevance and monotone curve.

    Player priors follow Eq. 14: 'theta ~ N(0, I)' and 'c ~ N(0, 1)', with
    optional held-out overrides attached to 'data'.
    """
    degree = validate_degree(degree)
    drop_concentration = validate_drop_concentration(drop_concentration)
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
    a_scale = (
        pyro.sample(
            "a_scale",
            dist.HalfNormal(data["y"].new_tensor(PLAYER_PROPENSITY_SCALE_PRIOR)),
        )
        if player_neg_propensity
        else None
    )
    with pyro.plate("players", n_players):
        # .to_event(1) treats the whole skill vector as one player's latent draw.
        theta = pyro.sample("theta", dist.Normal(theta_loc, theta_scale).to_event(1))
        c = pyro.sample("c", dist.Normal(c_loc, c_scale))
        a = (
            pyro.sample("a", dist.Normal(zero, a_scale))
            if a_scale is not None
            else None
        )

    locations = (
        sample_curve_locations(data) if learned_curve_locations else (zero, zero)
    )

    # One symmetric Dirichlet over the 'degree' drop shares of every dimension,
    # shared by both curves so they have the same degree and shape prior.
    concentration = data["y"].new_full((n_dimensions, degree), drop_concentration)
    # Gamma coordinates are wrapped in .to_event(1); Dirichlet already treats
    # the K-dimensional simplex as one event.
    with pyro.plate("tossups", n_tossups):
        # Positive relevance so higher skill on a loaded dimension always helps.
        # Both branches use the same configured prior but draw independently.
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
        correct_curve = sample_curve_parameters(
            data, n_dimensions, concentration, "correct", locations[0]
        )
        hazard_curve = sample_curve_parameters(
            data, n_dimensions, concentration, "hazard", locations[1]
        )
    return theta, c, a, correct_r, hazard_r, correct_curve, hazard_curve


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


def correctness_log_likelihood(correctness, y, incorrect_weight=1.0):
    """Sum correctness log likelihood with a configurable incorrect-class weight."""
    log_prob = dist.Bernoulli(logits=correctness).log_prob(y)
    weights = torch.where(
        y == 0,
        log_prob.new_tensor(incorrect_weight),
        log_prob.new_tensor(1.0),
    )
    return (weights * log_prob).sum()


def competing_risks_model(
    data,
    n_dimensions=1,
    degree=MIN_DEGREE,
    drop_concentration=DEFAULT_DROP_CONCENTRATION,
    calibrate_correctness=False,
    calibrate_scale=True,
    terminal_intercepts=True,
    relevance_prior=DEFAULT_RELEVANCE_PRIOR,
    learned_curve_locations=False,
    incorrect_weight=1.0,
    player_neg_propensity=False,
):
    """Define the monotone double-difficulty competing-risks likelihood.

    Every rostered player contributes survival before the stopping position. The
    actual first buzzer additionally contributes a hazard-at-'t_star' factor and
    an observed correctness factor, and the hand-computed joint log-likelihood is
    added with 'pyro.factor'. Survival and hazard read the hazard curve;
    correctness reads the correctness curve.
    """
    theta, c, a, correct_r, hazard_r, correct_curve, hazard_curve = sample_parameters(
        data,
        n_dimensions,
        degree,
        drop_concentration,
        relevance_prior,
        learned_curve_locations,
        player_neg_propensity,
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
        end_hazard,
    )
    correctness = correctness_logit(
        row_theta[buzz],
        row_correct_r[buzz],
        *(parameter[buzz] for parameter in row_correct),
        data["t_star"][buzz],
        data["T_j"][buzz],
        end_correct,
    )
    if a is not None:
        correctness = correctness + a[data["player"]][buzz]
    if calibrate_correctness:
        # Apply calibration to correctness; hazard/timing keeps its base logit.
        scale, bias = sample_correctness_calibration(data, with_scale=calibrate_scale)
        correctness = apply_correctness_calibration(correctness, scale, bias)

    log_likelihood = (
        # Sum log survival over every player-event row.
        survival.sum()
        # Sum log hazard and correctness log likelihood over first-buzzer rows.
        + F.logsigmoid(buzz_logits).sum()
        + correctness_log_likelihood(
            correctness, data["y"][buzz], incorrect_weight
        )
    )
    pyro.factor("bernstein_double_difficulty_competing_risks_likelihood", log_likelihood)


def posterior_curves(posterior):
    """Return the fitted parameter tuples for both curves."""
    return tuple(
        (
            posterior[f"start_difficulty_{suffix}"],
            posterior[f"total_drop_{suffix}"],
            posterior[f"drop_proportions_{suffix}"],
        )
        for suffix in ("correct", "hazard")
    )


def posterior_row_predictions(
    data, posterior, calibrate_correctness=False, calibrate_scale=True
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
        theta, correct_r, *row_correct, data["t_star"], data["T_j"], end_correct
    )
    if "a" in posterior:
        correctness_logits = correctness_logits + posterior["a"][data["player"]]
    if calibrate_correctness:
        correctness_logits = apply_correctness_calibration(
            correctness_logits,
            posterior["correctness_scale"] if calibrate_scale else None,
            posterior["correctness_bias"],
        )
    correctness = torch.sigmoid(correctness_logits)
    hazard = torch.sigmoid(
        hazard_logit(
            theta, hazard_r, *row_hazard, c, data["t_star"], data["T_j"], end_hazard
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
            t_start=data.get("t_start"),
            end=end_hazard,
        )
    )
    return correctness, hazard, survival


def expected_first_buzz_positions(data, posterior):
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
    start, total_drop, shares = (
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
            hazard_logit(theta, r, start, total_drop, shares, c, t, T, end_hazard)
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
