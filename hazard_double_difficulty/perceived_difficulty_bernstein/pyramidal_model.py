"""Bernstein CompIRT with a shared curve and player-specific perception.

For tossup ``j``, player ``i``, and relative position ``x=t/T_j`` the model is

    correctness = sum_k r_jk * (theta_ik - d_jk(x))
    hazard      = sum_k r_jk * (theta_ik - alpha_ik*d_jk(x) + beta_ik)

The relevance vector is a simplex and the monotone Bernstein curve is shared
exactly between the two branches.  Only the player vectors ``alpha`` and
``beta`` alter the buzz hazard.  Alpha is positive with median one (identity
difficulty perception); beta is unconstrained and centred at zero. Experiments
may instead request a unit Normal alpha prior centred at zero or one.

The optional three-slice experiment gives every player separate ``alpha`` and
``beta`` vectors for the first, middle, and final thirds of the question. The
slice is selected from relative token position ``t / T_j``; correctness is
unchanged.
"""

from __future__ import annotations

import math

from compirt_race import winner_log_prob
import pyro
import pyro.distributions as dist
import torch
import torch.nn.functional as F
from torch.utils.checkpoint import checkpoint

from utils.prediction import event_rosters
from utils.training import survival_chunk_size


MIN_DEGREE = 3
MAX_DEGREE = 6
SUPPORTED_DEGREES = range(MIN_DEGREE, MAX_DEGREE + 1)
DEFAULT_RELEVANCE_CONCENTRATION = 2.0
DEFAULT_DROP_CONCENTRATION = 2.0
TOTAL_DROP_LOG_SCALE = 0.5
ALPHA_LOG_SCALE = 1.0
ALPHA_PRIOR_LOGNORMAL = "lognormal"
ALPHA_PRIOR_NORMAL_ZERO = "normal-zero"
ALPHA_PRIOR_NORMAL_ONE = "normal-one"
SUPPORTED_ALPHA_PRIORS = (
    ALPHA_PRIOR_LOGNORMAL,
    ALPHA_PRIOR_NORMAL_ZERO,
    ALPHA_PRIOR_NORMAL_ONE,
)
PERCEPTION_SLICE_NAMES = ("first", "middle", "last")
SUPPORTED_PERCEPTION_SLICES = (1, len(PERCEPTION_SLICE_NAMES))


def validate_degree(degree: int) -> int:
    degree = int(degree)
    if degree not in SUPPORTED_DEGREES:
        raise ValueError(
            f"degree must be between {MIN_DEGREE} and {MAX_DEGREE}, got {degree}"
        )
    return degree


def validate_concentration(value: float, name: str = "concentration") -> float:
    value = float(value)
    if not math.isfinite(value) or value <= 0:
        raise ValueError(f"{name} must be finite and greater than zero")
    return value


def bernstein_basis(x: torch.Tensor, degree: int) -> torch.Tensor:
    """Return the nonnegative basis B_m,p(x), which sums to one on [0, 1]."""
    powers = torch.arange(degree + 1, dtype=x.dtype, device=x.device)
    binomial = x.new_tensor([math.comb(degree, m) for m in range(degree + 1)])
    return (
        binomial
        * x.unsqueeze(-1).pow(powers)
        * (1.0 - x).unsqueeze(-1).pow(degree - powers)
    )


def control_values(start_difficulty, total_drop, drop_proportions):
    """Build decreasing controls by distributing the positive total drop."""
    drops = total_drop.unsqueeze(-1) * drop_proportions
    later = start_difficulty.unsqueeze(-1) - drops.cumsum(-1)
    return torch.cat([start_difficulty.unsqueeze(-1), later], dim=-1)


def difficulty_curve(start_difficulty, total_drop, drop_proportions, t, T_j):
    """Evaluate the shared curve, retaining the trailing skill-dimension axis."""
    basis = bernstein_basis(t / T_j, drop_proportions.shape[-1])
    controls = control_values(start_difficulty, total_drop, drop_proportions)
    return (controls * basis.unsqueeze(-2)).sum(-1)


def correctness_logit(
    theta, r, start_difficulty, total_drop, drop_proportions, t, T_j
):
    difficulty = difficulty_curve(
        start_difficulty, total_drop, drop_proportions, t, T_j
    )
    return (r * (theta - difficulty)).sum(-1)


def perception_slice_index(t, T_j):
    """Return first/middle/last indexes from relative token position."""
    relative = t / T_j
    return torch.where(
        relative < (1.0 / 3.0),
        torch.zeros_like(relative, dtype=torch.long),
        torch.where(
            relative < (2.0 / 3.0),
            torch.ones_like(relative, dtype=torch.long),
            torch.full_like(relative, 2, dtype=torch.long),
        ),
    )


def select_perception_slice(parameter, t, T_j):
    """Select a sliced vector, or return a legacy one-slice tensor unchanged.

    Sliced parameters have shape ``(..., 3, dimensions)``. Callers may add a
    singleton token-grid axis before the slice axis; this helper broadcasts it
    against ``t / T_j`` before gathering the active slice.
    """
    if parameter.ndim != t.ndim + 2:
        return parameter
    if parameter.shape[-2] != len(PERCEPTION_SLICE_NAMES):
        raise ValueError(
            "Sliced perception parameters must have exactly three slices"
        )
    indexes = perception_slice_index(t, T_j)
    leading_shape = torch.broadcast_shapes(parameter.shape[:-2], indexes.shape)
    expanded = parameter.expand(
        *leading_shape, len(PERCEPTION_SLICE_NAMES), parameter.shape[-1]
    )
    gather_index = indexes.expand(leading_shape).unsqueeze(-1).unsqueeze(-1)
    gather_index = gather_index.expand(*leading_shape, 1, parameter.shape[-1])
    return torch.gather(expanded, -2, gather_index).squeeze(-2)


def hazard_logit(
    theta,
    r,
    start_difficulty,
    total_drop,
    drop_proportions,
    alpha,
    beta,
    t,
    T_j,
):
    difficulty = difficulty_curve(
        start_difficulty, total_drop, drop_proportions, t, T_j
    )
    alpha = select_perception_slice(alpha, t, T_j)
    beta = select_perception_slice(beta, t, T_j)
    return (r * (theta - alpha * difficulty + beta)).sum(-1)


def log_survival(
    theta,
    r,
    start_difficulty,
    total_drop,
    drop_proportions,
    alpha,
    beta,
    t_star,
    T_j,
    chunk_size=None,
    t_start=None,
):
    """Return log probability of no buzz over ``[t_start, t_star)``."""
    if chunk_size is None:
        chunk_size = survival_chunk_size()
    if chunk_size and t_star.shape[0] > chunk_size:
        return torch.cat(
            [
                checkpoint(
                    log_survival,
                    theta[lo : lo + chunk_size],
                    r[lo : lo + chunk_size],
                    start_difficulty[lo : lo + chunk_size],
                    total_drop[lo : lo + chunk_size],
                    drop_proportions[lo : lo + chunk_size],
                    alpha[lo : lo + chunk_size],
                    beta[lo : lo + chunk_size],
                    t_star[lo : lo + chunk_size],
                    T_j[lo : lo + chunk_size],
                    use_reentrant=False,
                    t_start=None
                    if t_start is None
                    else t_start[lo : lo + chunk_size],
                )
                for lo in range(0, t_star.shape[0], chunk_size)
            ]
        )

    max_t = int(t_star.max().item())
    positions = torch.arange(1, max_t + 1, device=t_star.device).unsqueeze(0)
    before_stop = positions < t_star.unsqueeze(1)
    if t_start is not None:
        before_stop = before_stop & (positions >= t_start.unsqueeze(1))
    logits = hazard_logit(
        theta.unsqueeze(1),
        r.unsqueeze(1),
        start_difficulty.unsqueeze(1),
        total_drop.unsqueeze(1),
        drop_proportions.unsqueeze(1),
        alpha.unsqueeze(1),
        beta.unsqueeze(1),
        positions,
        T_j.unsqueeze(1),
    )
    return (F.logsigmoid(-logits) * before_stop).sum(1)


def row_parameters(
    data, theta, alpha, beta, r, start_difficulty, total_drop, drop_proportions
):
    player = data["player"]
    tossup = data["tossup"]
    return (
        theta[player],
        alpha[player],
        beta[player],
        r[tossup],
        start_difficulty[tossup],
        total_drop[tossup],
        drop_proportions[tossup],
    )


def survival_stop(data):
    """Return the exclusive stop, including token T for terminal no-buzz rows."""
    no_buzz = data.get("is_no_buzz")
    if no_buzz is None:
        return data["t_star"]
    return data["t_star"] + no_buzz.to(data["t_star"].dtype)


def alpha_distribution(zero, one, alpha_prior=ALPHA_PRIOR_LOGNORMAL):
    """Return the requested unit-scale alpha population prior."""
    if alpha_prior == ALPHA_PRIOR_LOGNORMAL:
        return dist.LogNormal(zero, ALPHA_LOG_SCALE * one)
    if alpha_prior == ALPHA_PRIOR_NORMAL_ZERO:
        return dist.Normal(zero, one)
    if alpha_prior == ALPHA_PRIOR_NORMAL_ONE:
        return dist.Normal(one, one)
    raise ValueError(
        f"alpha_prior must be one of {SUPPORTED_ALPHA_PRIORS}, got {alpha_prior!r}"
    )


def sample_player_perception(
    data,
    n_dimensions,
    perception_slices=1,
    alpha_prior=ALPHA_PRIOR_LOGNORMAL,
):
    """Sample player alpha/beta vectors, with an optional three-slice axis.

    Keeping this population-prior boundary separate makes alternate alpha
    population priors local to this function.
    """
    perception_slices = int(perception_slices)
    if perception_slices not in SUPPORTED_PERCEPTION_SLICES:
        raise ValueError(
            "perception_slices must be one or three, "
            f"got {perception_slices}"
        )
    perception_shape = (
        (n_dimensions,)
        if perception_slices == 1
        else (perception_slices, n_dimensions)
    )
    zero = data["y"].new_zeros(perception_shape)
    one = data["y"].new_ones(perception_shape)
    alpha = pyro.sample(
        "alpha",
        alpha_distribution(zero, one, alpha_prior).to_event(len(perception_shape)),
    )
    beta = pyro.sample(
        "beta", dist.Normal(zero, one).to_event(len(perception_shape))
    )
    return alpha, beta


def sample_parameters(
    data,
    n_dimensions,
    degree,
    relevance_concentration=DEFAULT_RELEVANCE_CONCENTRATION,
    drop_concentration=DEFAULT_DROP_CONCENTRATION,
    perception_slices=1,
    alpha_prior=ALPHA_PRIOR_LOGNORMAL,
):
    degree = validate_degree(degree)
    relevance_concentration = validate_concentration(
        relevance_concentration, "relevance_concentration"
    )
    drop_concentration = validate_concentration(
        drop_concentration, "drop_concentration"
    )
    n_players = len(data["player_ids"])
    n_tossups = len(data["tossup_ids"])
    zero = data["y"].new_zeros(n_dimensions)
    one = data["y"].new_ones(n_dimensions)

    # Each player has a skill vector and a transform of the shared difficulty.
    theta_loc = data.get("theta_prior_loc", zero)
    theta_scale = data.get("theta_prior_scale", one)
    with pyro.plate("players", n_players):
        theta = pyro.sample("theta", dist.Normal(theta_loc, theta_scale).to_event(1))
        alpha, beta = sample_player_perception(
            data, n_dimensions, perception_slices, alpha_prior
        )

    # Simplex relevance combines monotone per-dimension difficulty curves.
    relevance = data["y"].new_full(
        (n_dimensions,), relevance_concentration
    )
    drop = data["y"].new_full(
        (n_dimensions, degree), drop_concentration
    )
    with pyro.plate("tossups", n_tossups):
        r = pyro.sample("r", dist.Dirichlet(relevance))
        start = pyro.sample("start_difficulty", dist.Normal(zero, one).to_event(1))
        total = pyro.sample(
            "total_drop",
            dist.LogNormal(zero, TOTAL_DROP_LOG_SCALE * one).to_event(1),
        )
        shares = pyro.sample(
            "drop_proportions", dist.Dirichlet(drop).to_event(1)
        )
    return theta, alpha, beta, r, start, total, shares


def competing_risks_model(
    data,
    n_dimensions=3,
    degree=MIN_DEGREE,
    relevance_concentration=DEFAULT_RELEVANCE_CONCENTRATION,
    drop_concentration=DEFAULT_DROP_CONCENTRATION,
    perception_slices=1,
    alpha_prior=ALPHA_PRIOR_LOGNORMAL,
):
    parameters = sample_parameters(
        data,
        n_dimensions,
        degree,
        relevance_concentration,
        drop_concentration,
        perception_slices,
        alpha_prior,
    )
    theta, alpha, beta, r, start, total, shares = row_parameters(data, *parameters)
    # The full roster contributes survival; winner terms use the full risk set at the stopping token.
    stop = survival_stop(data)
    survival = log_survival(
        theta,
        r,
        start,
        total,
        shares,
        alpha,
        beta,
        stop,
        data["T_j"],
        t_start=data.get("t_start"),
    )
    buzz = data["is_buzz"]
    stop_hazard_logits = hazard_logit(
        theta,
        r,
        start,
        total,
        shares,
        alpha,
        beta,
        data["t_star"],
        data["T_j"],
    )
    correct_logits = correctness_logit(
        theta[buzz],
        r[buzz],
        start[buzz],
        total[buzz],
        shares[buzz],
        data["t_star"][buzz],
        data["T_j"][buzz],
    )
    likelihood = (
        survival.sum()
        + winner_log_prob(data, stop_hazard_logits).sum()
        + dist.Bernoulli(logits=correct_logits).log_prob(data["y"][buzz]).sum()
    )
    pyro.factor(
        "perceived_difficulty_bernstein_competing_risks_likelihood", likelihood
    )


def posterior_row_predictions(data, posterior):
    theta, alpha, beta, r, start, total, shares = row_parameters(
        data,
        posterior["theta"],
        posterior["alpha"],
        posterior["beta"],
        posterior["r"],
        posterior["start_difficulty"],
        posterior["total_drop"],
        posterior["drop_proportions"],
    )
    correct = torch.sigmoid(
        correctness_logit(
            theta, r, start, total, shares, data["t_star"], data["T_j"]
        )
    )
    hazard = torch.sigmoid(
        hazard_logit(
            theta,
            r,
            start,
            total,
            shares,
            alpha,
            beta,
            data["t_star"],
            data["T_j"],
        )
    )
    survival = torch.exp(
        log_survival(
            theta,
            r,
            start,
            total,
            shares,
            alpha,
            beta,
            survival_stop(data),
            data["T_j"],
            t_start=data.get("t_start"),
        )
    )
    return correct, hazard, survival


def expected_first_buzz_positions(data, posterior):
    """Return event -> expected relative first-buzz position, conditional on buzz."""
    # Rebuild the full first-buzz field before broadcasting fitted parameters.
    roster, roster_mask, event_tossup, event_T = event_rosters(data)
    n_events, max_roster = roster.shape

    theta = posterior["theta"][roster]
    alpha = posterior["alpha"][roster]
    beta = posterior["beta"][roster]
    r = posterior["r"][event_tossup].unsqueeze(1)
    start = posterior["start_difficulty"][event_tossup].unsqueeze(1)
    total = posterior["total_drop"][event_tossup].unsqueeze(1)
    shares = posterior["drop_proportions"][event_tossup].unsqueeze(1)

    event_survival = data["y"].new_ones(n_events)
    expected = data["y"].new_zeros(n_events)
    for position in range(1, int(event_T.max().item()) + 1):
        active = position <= event_T
        t = data["y"].new_full((n_events, max_roster), float(position))
        T = event_T.unsqueeze(1).expand_as(t)
        hazard = torch.sigmoid(
            hazard_logit(theta, r, start, total, shares, alpha, beta, t, T)
        )
        hazard = torch.where(roster_mask, hazard, torch.zeros_like(hazard))
        total_hazard = 1.0 - torch.prod(1.0 - hazard, dim=1)
        total_hazard = torch.where(active, total_hazard, torch.zeros_like(total_hazard))
        first = event_survival * total_hazard
        expected = expected + position * first
        event_survival = event_survival * (1.0 - total_hazard)
    buzz_mass = 1.0 - event_survival
    end = event_T.to(expected.dtype)
    expected = torch.where(
        buzz_mass > 1e-9, expected / buzz_mass.clamp(min=1e-9), end
    )
    relative = (expected / end).detach().cpu().tolist()
    return dict(zip(data["event_ids"], relative))
