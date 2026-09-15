"""Bernstein CompIRT with a scalar player transform of correctness evidence.

    correctness = sum_k r_jk * (theta_ik - d_jk(x))
    hazard      = alpha_i * correctness + beta_i

The item relevance and difficulty are shared literally between the branches.
Each player has only two additional scalar parameters. The default is a
positive slope with median one and an unconstrained intercept centred at zero;
experiments may instead request a unit Normal slope centred at zero or one.
"""

from __future__ import annotations

from compirt_race import winner_log_prob
import pyro
import pyro.distributions as dist
import torch
import torch.nn.functional as F
from torch.utils.checkpoint import checkpoint

from hazard_double_difficulty.perceived_difficulty_bernstein.pyramidal_model import (
    ALPHA_PRIOR_LOGNORMAL,
    ALPHA_LOG_SCALE,
    DEFAULT_DROP_CONCENTRATION,
    DEFAULT_RELEVANCE_CONCENTRATION,
    MAX_DEGREE,
    MIN_DEGREE,
    SUPPORTED_ALPHA_PRIORS,
    SUPPORTED_DEGREES,
    TOTAL_DROP_LOG_SCALE,
    alpha_distribution,
    bernstein_basis,
    control_values,
    difficulty_curve,
    survival_stop,
    validate_concentration,
    validate_degree,
)
from utils.prediction import event_rosters
from utils.training import survival_chunk_size


def correctness_logit(
    theta, r, start_difficulty, total_drop, drop_proportions, t, T_j
):
    difficulty = difficulty_curve(
        start_difficulty, total_drop, drop_proportions, t, T_j
    )
    return (r * (theta - difficulty)).sum(-1)


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
    evidence = correctness_logit(
        theta, r, start_difficulty, total_drop, drop_proportions, t, T_j
    )
    return alpha * evidence + beta


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


def sample_parameters(
    data,
    n_dimensions,
    degree,
    relevance_concentration=DEFAULT_RELEVANCE_CONCENTRATION,
    drop_concentration=DEFAULT_DROP_CONCENTRATION,
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
    vector_zero = data["y"].new_zeros(n_dimensions)
    vector_one = data["y"].new_ones(n_dimensions)
    zero = data["y"].new_tensor(0.0)
    one = data["y"].new_tensor(1.0)

    # Each player has a skill vector and a scalar transform of correctness evidence.
    theta_loc = data.get("theta_prior_loc", vector_zero)
    theta_scale = data.get("theta_prior_scale", vector_one)
    with pyro.plate("players", n_players):
        theta = pyro.sample(
            "theta", dist.Normal(theta_loc, theta_scale).to_event(1)
        )
        alpha = pyro.sample("alpha", alpha_distribution(zero, one, alpha_prior))
        beta = pyro.sample("beta", dist.Normal(zero, one))

    # Both branches share the item's relevance and monotone difficulty curve.
    relevance = data["y"].new_full(
        (n_dimensions,), relevance_concentration
    )
    drop = data["y"].new_full((n_dimensions, degree), drop_concentration)
    with pyro.plate("tossups", n_tossups):
        r = pyro.sample("r", dist.Dirichlet(relevance))
        start = pyro.sample(
            "start_difficulty", dist.Normal(vector_zero, vector_one).to_event(1)
        )
        total = pyro.sample(
            "total_drop",
            dist.LogNormal(
                vector_zero, TOTAL_DROP_LOG_SCALE * vector_one
            ).to_event(1),
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
    alpha_prior=ALPHA_PRIOR_LOGNORMAL,
):
    parameters = sample_parameters(
        data,
        n_dimensions,
        degree,
        relevance_concentration,
        drop_concentration,
        alpha_prior,
    )
    theta, alpha, beta, r, start, total, shares = row_parameters(
        data, *parameters
    )
    # The full roster contributes survival; winner terms use the full risk set at the stopping token.
    survival = log_survival(
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
    pyro.factor("perceived_logit_bernstein_competing_risks_likelihood", likelihood)


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
        total_hazard = torch.where(
            active, total_hazard, torch.zeros_like(total_hazard)
        )
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


__all__ = [
    "ALPHA_LOG_SCALE",
    "ALPHA_PRIOR_LOGNORMAL",
    "DEFAULT_DROP_CONCENTRATION",
    "DEFAULT_RELEVANCE_CONCENTRATION",
    "MAX_DEGREE",
    "MIN_DEGREE",
    "SUPPORTED_ALPHA_PRIORS",
    "SUPPORTED_DEGREES",
    "TOTAL_DROP_LOG_SCALE",
    "bernstein_basis",
    "competing_risks_model",
    "control_values",
    "correctness_logit",
    "difficulty_curve",
    "expected_first_buzz_positions",
    "hazard_logit",
    "log_survival",
    "posterior_row_predictions",
    "row_parameters",
    "sample_parameters",
    "survival_stop",
    "validate_concentration",
    "validate_degree",
]
