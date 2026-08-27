"""Compact double-Bernstein competing-risks model.

Unlike the full double-difficulty Bernstein model, difficulty is not a vector
inside each skill gap.  A tossup first projects player skill onto a normalized
item direction and applies a positive discrimination::

    s_ij = a_j * sum_k w_jk * theta_ik,  w_j on the simplex, a_j > 0

Correctness and buzz timing then subtract separate *scalar*, monotone Bernstein
curves::

    z^C_ijt = s_ij - b^C_j(t/T_j) + e_C 1[t=T_j]
    z^H_ijt = s_ij - b^H_j(t/T_j) - c_i + e_H 1[t=T_j]

This preserves CompIRT's scalar-difficulty spine while removing the forced
correctness/hazard coupling.  Optional learned population locations provide
hierarchical centering for the two curve families; they and the two terminal
intercepts are global scalars, not per-item parameters.
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
DISCRIMINATION_LOG_SCALE = 0.5
CURVE_LOCATION_PRIOR_SCALE = 1.0
CURVE_START_PRIOR_SCALE = 1.0
TERMINAL_PRIOR_SCALE = 2.0


def validate_degree(degree: int) -> int:
    degree = int(degree)
    if degree not in SUPPORTED_DEGREES:
        raise ValueError(
            f"degree must be between {MIN_DEGREE} and {MAX_DEGREE}, got {degree}"
        )
    return degree


def validate_drop_concentration(value: float) -> float:
    value = float(value)
    if not math.isfinite(value) or value <= 0:
        raise ValueError("drop_concentration must be finite and greater than zero")
    return value


def bernstein_basis(x: torch.Tensor, degree: int) -> torch.Tensor:
    powers = torch.arange(degree + 1, dtype=x.dtype, device=x.device)
    binomial = x.new_tensor([math.comb(degree, m) for m in range(degree + 1)])
    return (
        binomial
        * x.unsqueeze(-1).pow(powers)
        * (1.0 - x).unsqueeze(-1).pow(degree - powers)
    )


def control_values(start_difficulty, total_drop, drop_proportions):
    drops = total_drop.unsqueeze(-1) * drop_proportions
    later = start_difficulty.unsqueeze(-1) - drops.cumsum(-1)
    return torch.cat((start_difficulty.unsqueeze(-1), later), dim=-1)


def difficulty_curve(start_difficulty, total_drop, drop_proportions, t, T_j):
    """Evaluate one scalar, strictly decreasing Bernstein curve per item."""
    basis = bernstein_basis(t / T_j, drop_proportions.shape[-1])
    return (control_values(start_difficulty, total_drop, drop_proportions) * basis).sum(-1)


def skill_score(theta, skill_weights, discrimination):
    """Return ``a_j (w_j dot theta_i)`` with simplex ``w_j`` and positive ``a_j``."""
    return discrimination * (theta * skill_weights).sum(-1)


def terminal_intercept(effect, t, T_j):
    if effect is None:
        return 0.0
    return effect * (t >= T_j).to(T_j.dtype)


def correctness_logit(
    theta,
    skill_weights,
    discrimination,
    start_difficulty,
    total_drop,
    drop_proportions,
    t,
    T_j,
    end=None,
):
    return (
        skill_score(theta, skill_weights, discrimination)
        - difficulty_curve(start_difficulty, total_drop, drop_proportions, t, T_j)
        + terminal_intercept(end, t, T_j)
    )


def hazard_logit(
    theta,
    skill_weights,
    discrimination,
    start_difficulty,
    total_drop,
    drop_proportions,
    c,
    t,
    T_j,
    end=None,
):
    return (
        skill_score(theta, skill_weights, discrimination)
        - difficulty_curve(start_difficulty, total_drop, drop_proportions, t, T_j)
        - c
        + terminal_intercept(end, t, T_j)
    )


def log_survival(
    theta,
    skill_weights,
    discrimination,
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
    """Return row-wise log survival over the half-open risk interval."""
    if chunk_size is None:
        chunk_size = survival_chunk_size()
    if chunk_size and t_star.shape[0] > chunk_size:
        parts = [
            checkpoint(
                log_survival,
                theta[lo : lo + chunk_size],
                skill_weights[lo : lo + chunk_size],
                discrimination[lo : lo + chunk_size],
                start_difficulty[lo : lo + chunk_size],
                total_drop[lo : lo + chunk_size],
                drop_proportions[lo : lo + chunk_size],
                c[lo : lo + chunk_size],
                t_star[lo : lo + chunk_size],
                T_j[lo : lo + chunk_size],
                use_reentrant=False,
                t_start=None if t_start is None else t_start[lo : lo + chunk_size],
                end=end,
            )
            for lo in range(0, t_star.shape[0], chunk_size)
        ]
        return torch.cat(parts)

    positions = torch.arange(
        1, int(t_star.max().item()) + 1, device=t_star.device
    ).unsqueeze(0)
    before_stop = positions < t_star.unsqueeze(1)
    if t_start is not None:
        before_stop &= positions >= t_start.unsqueeze(1)
    logits = hazard_logit(
        theta.unsqueeze(1),
        skill_weights.unsqueeze(1),
        discrimination.unsqueeze(1),
        start_difficulty.unsqueeze(1),
        total_drop.unsqueeze(1),
        drop_proportions.unsqueeze(1),
        c.unsqueeze(1),
        positions,
        T_j.unsqueeze(1),
        end,
    )
    return (F.logsigmoid(-logits) * before_stop).sum(1)


def survival_stop(data):
    """Include position ``T_j`` in terminal no-buzz survival rows."""
    no_buzz = data.get("is_no_buzz")
    if no_buzz is None:
        return data["t_star"]
    return data["t_star"] + no_buzz.to(data["t_star"].dtype)


def row_parameters(data, theta, c, skill_weights, discrimination, curves):
    player, tossup = data["player"], data["tossup"]
    correct_curve, hazard_curve = curves
    return (
        theta[player],
        c[player],
        skill_weights[tossup],
        discrimination[tossup],
        tuple(parameter[tossup] for parameter in correct_curve),
        tuple(parameter[tossup] for parameter in hazard_curve),
    )


def sample_curve_locations(data):
    zero = data["y"].new_tensor(0.0)
    scale = data["y"].new_tensor(CURVE_LOCATION_PRIOR_SCALE)
    return (
        pyro.sample("curve_location_correct", dist.Normal(zero, scale)),
        pyro.sample("curve_location_hazard", dist.Normal(zero, scale)),
    )


def sample_curve_parameters(data, concentration, suffix, location):
    scale = data["y"].new_tensor(CURVE_START_PRIOR_SCALE)
    zero = data["y"].new_tensor(0.0)
    start = pyro.sample(f"start_difficulty_{suffix}", dist.Normal(location, scale))
    total = pyro.sample(
        f"total_drop_{suffix}",
        dist.LogNormal(zero, data["y"].new_tensor(TOTAL_DROP_LOG_SCALE)),
    )
    shares = pyro.sample(f"drop_proportions_{suffix}", dist.Dirichlet(concentration))
    return start, total, shares


def sample_terminal_intercepts(data):
    zero = data["y"].new_tensor(0.0)
    scale = data["y"].new_tensor(TERMINAL_PRIOR_SCALE)
    return (
        pyro.sample("end_correct", dist.Normal(zero, scale)),
        pyro.sample("end_hazard", dist.Normal(zero, scale)),
    )


def posterior_terminal_intercepts(posterior):
    return posterior.get("end_correct"), posterior.get("end_hazard")


def sample_parameters(
    data,
    n_dimensions,
    degree,
    drop_concentration=DEFAULT_DROP_CONCENTRATION,
    learned_curve_locations=False,
):
    degree = validate_degree(degree)
    drop_concentration = validate_drop_concentration(drop_concentration)
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

    locations = (
        sample_curve_locations(data)
        if learned_curve_locations
        else (zero, zero)
    )
    weight_concentration = data["y"].new_ones(n_dimensions)
    share_concentration = data["y"].new_full((degree,), drop_concentration)
    with pyro.plate("tossups", n_tossups):
        skill_weights = pyro.sample(
            "skill_weights", dist.Dirichlet(weight_concentration)
        )
        discrimination = pyro.sample(
            "discrimination",
            dist.LogNormal(zero, data["y"].new_tensor(DISCRIMINATION_LOG_SCALE)),
        )
        curves = tuple(
            sample_curve_parameters(data, share_concentration, suffix, location)
            for suffix, location in zip(("correct", "hazard"), locations)
        )
    return theta, c, skill_weights, discrimination, curves


def competing_risks_model(
    data,
    n_dimensions=1,
    degree=MIN_DEGREE,
    drop_concentration=DEFAULT_DROP_CONCENTRATION,
    learned_curve_locations=False,
    terminal_intercepts=False,
):
    theta, c, weights, discrimination, curves = sample_parameters(
        data,
        n_dimensions,
        degree,
        drop_concentration,
        learned_curve_locations,
    )
    end_correct, end_hazard = (
        sample_terminal_intercepts(data) if terminal_intercepts else (None, None)
    )
    row_theta, row_c, row_weights, row_discrimination, correct_curve, hazard_curve = (
        row_parameters(data, theta, c, weights, discrimination, curves)
    )
    survival = log_survival(
        row_theta,
        row_weights,
        row_discrimination,
        *hazard_curve,
        row_c,
        survival_stop(data),
        data["T_j"],
        t_start=data.get("t_start"),
        end=end_hazard,
    )
    buzz = data["is_buzz"]
    hazard = hazard_logit(
        row_theta[buzz],
        row_weights[buzz],
        row_discrimination[buzz],
        *(parameter[buzz] for parameter in hazard_curve),
        row_c[buzz],
        data["t_star"][buzz],
        data["T_j"][buzz],
        end_hazard,
    )
    correctness = correctness_logit(
        row_theta[buzz],
        row_weights[buzz],
        row_discrimination[buzz],
        *(parameter[buzz] for parameter in correct_curve),
        data["t_star"][buzz],
        data["T_j"][buzz],
        end_correct,
    )
    log_likelihood = (
        survival.sum()
        + F.logsigmoid(hazard).sum()
        + dist.Bernoulli(logits=correctness).log_prob(data["y"][buzz]).sum()
    )
    pyro.factor("compact_double_bernstein_competing_risks_likelihood", log_likelihood)


def posterior_curves(posterior):
    return tuple(
        (
            posterior[f"start_difficulty_{suffix}"],
            posterior[f"total_drop_{suffix}"],
            posterior[f"drop_proportions_{suffix}"],
        )
        for suffix in ("correct", "hazard")
    )


def posterior_row_predictions(data, posterior):
    curves = posterior_curves(posterior)
    end_correct, end_hazard = posterior_terminal_intercepts(posterior)
    theta, c, weights, discrimination, correct_curve, hazard_curve = row_parameters(
        data,
        posterior["theta"],
        posterior["c"],
        posterior["skill_weights"],
        posterior["discrimination"],
        curves,
    )
    correct = torch.sigmoid(
        correctness_logit(
            theta,
            weights,
            discrimination,
            *correct_curve,
            data["t_star"],
            data["T_j"],
            end_correct,
        )
    )
    hazard = torch.sigmoid(
        hazard_logit(
            theta,
            weights,
            discrimination,
            *hazard_curve,
            c,
            data["t_star"],
            data["T_j"],
            end_hazard,
        )
    )
    survival = torch.exp(
        log_survival(
            theta,
            weights,
            discrimination,
            *hazard_curve,
            c,
            survival_stop(data),
            data["T_j"],
            t_start=data.get("t_start"),
            end=end_hazard,
        )
    )
    return correct, hazard, survival


def expected_first_buzz_positions(data, posterior):
    """Compute event-level ``E[t/T | a buzz occurs]`` from the hazard branch."""
    n_events = len(data["event_ids"])
    phase0 = data.get("is_phase0")
    if phase0 is None:
        phase0 = torch.ones(
            len(data["event"]), dtype=torch.bool, device=data["event"].device
        )
    counts = torch.bincount(data["event"][phase0], minlength=n_events)
    max_roster = int(counts.max().item())
    roster = data["player"].new_zeros((n_events, max_roster))
    roster_mask = torch.zeros(
        (n_events, max_roster), dtype=torch.bool, device=data["event"].device
    )
    event_tossup = data["tossup"].new_zeros(n_events)
    event_T = data["T_j"].new_ones(n_events)
    next_slot = [0] * n_events
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

    _, hazard_curve = posterior_curves(posterior)
    theta = posterior["theta"][roster]
    weights = posterior["skill_weights"][event_tossup].unsqueeze(1)
    discrimination = posterior["discrimination"][event_tossup].unsqueeze(1)
    start, total, shares = (
        parameter[event_tossup].unsqueeze(1) for parameter in hazard_curve
    )
    c = posterior["c"][roster]
    _, end_hazard = posterior_terminal_intercepts(posterior)
    event_survival = data["y"].new_ones(n_events)
    expected = data["y"].new_zeros(n_events)
    for position in range(1, int(event_T.max().item()) + 1):
        active = position <= event_T
        t = data["y"].new_full((n_events, max_roster), float(position))
        T = event_T.unsqueeze(1).expand_as(t)
        hazard = torch.sigmoid(
            hazard_logit(
                theta,
                weights,
                discrimination,
                start,
                total,
                shares,
                c,
                t,
                T,
                end_hazard,
            )
        )
        hazard = torch.where(roster_mask, hazard, torch.zeros_like(hazard))
        total_hazard = 1.0 - torch.prod(1.0 - hazard, dim=1)
        total_hazard = torch.where(active, total_hazard, torch.zeros_like(total_hazard))
        first = event_survival * total_hazard
        expected += position * first
        event_survival *= 1.0 - total_hazard
    buzz_mass = 1.0 - event_survival
    end_position = event_T.to(expected.dtype)
    expected = torch.where(
        buzz_mass > 1e-9, expected / buzz_mass.clamp_min(1e-9), end_position
    )
    relative = (expected / end_position).detach().cpu().tolist()
    return dict(zip(data["event_ids"], relative))
