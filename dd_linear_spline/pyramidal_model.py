"""Vector double-difficulty CompIRT with clue-aligned linear splines."""

from __future__ import annotations

import pyro
import pyro.distributions as dist
import torch
import torch.nn.functional as F
from torch.utils.checkpoint import checkpoint

from hazard_double_difficulty.bernstein.pyramidal_model import (
    apply_correctness_calibration,
    sample_correctness_calibration,
    survival_stop,
)
from utils.training import survival_chunk_size


def difficulty_curve(knot_y, knot_x, knot_count, t, T_j):
    """Linearly interpolate per-dimension difficulty at token position ``t``."""
    query = (t / T_j).to(knot_x.dtype).clamp(0.0, 1.0)
    squeeze_query = query.ndim == knot_x.ndim - 1
    if squeeze_query:
        query = query.unsqueeze(-1)

    lower = torch.searchsorted(
        knot_x.contiguous(), query.contiguous(), right=True
    ) - 1
    last_lower = (knot_count - 2).unsqueeze(-1)
    lower = torch.minimum(lower.clamp(min=0), last_lower)
    upper = lower + 1
    x0 = torch.gather(knot_x, -1, lower)
    x1 = torch.gather(knot_x, -1, upper)
    dimensions = knot_y.shape[-1]
    lower_y = lower.unsqueeze(-1).expand(*lower.shape, dimensions)
    upper_y = upper.unsqueeze(-1).expand(*upper.shape, dimensions)
    y0 = torch.gather(knot_y, -2, lower_y)
    y1 = torch.gather(knot_y, -2, upper_y)
    weight = ((query - x0) / (x1 - x0).clamp_min(1e-8)).unsqueeze(-1)
    result = y0 + weight * (y1 - y0)
    return result.squeeze(-2) if squeeze_query else result


def curve_logit(theta, r, knot_y, knot_x, knot_count, t, T_j):
    difficulty = difficulty_curve(knot_y, knot_x, knot_count, t, T_j)
    return (r * (theta - difficulty)).sum(-1)


def terminal_intercept(effect, t, T_j):
    """Return 'effect' in the final cell only, zero everywhere else.

    Position 'T_j' also absorbs the whole post-reading buzz window, so its
    discrete-time cell spans far more real time than any single token. 'None'
    reproduces the model as it was before that cell got its own intercept.
    """
    if effect is None:
        return 0.0
    return effect * (t >= T_j).to(T_j.dtype)


def correctness_logit(theta, r, knot_y, knot_x, knot_count, t, T_j, end=None):
    return curve_logit(
        theta, r, knot_y, knot_x, knot_count, t, T_j
    ) + terminal_intercept(end, t, T_j)


def hazard_logit(theta, r, knot_y, knot_x, knot_count, c, t, T_j, end=None):
    return (
        curve_logit(theta, r, knot_y, knot_x, knot_count, t, T_j)
        - c
        + terminal_intercept(end, t, T_j)
    )


def log_survival(
    theta,
    r,
    knot_y,
    knot_x,
    knot_count,
    c,
    t_stop,
    T_j,
    chunk_size=None,
    t_start=None,
    end=None,
):
    """Return log survival over each row's ``[t_start, t_stop)`` interval."""
    if chunk_size is None:
        chunk_size = survival_chunk_size()
    if chunk_size and t_stop.shape[0] > chunk_size:
        return torch.cat(
            [
                checkpoint(
                    log_survival,
                    theta[lo : lo + chunk_size],
                    r[lo : lo + chunk_size],
                    knot_y[lo : lo + chunk_size],
                    knot_x[lo : lo + chunk_size],
                    knot_count[lo : lo + chunk_size],
                    c[lo : lo + chunk_size],
                    t_stop[lo : lo + chunk_size],
                    T_j[lo : lo + chunk_size],
                    use_reentrant=False,
                    t_start=None
                    if t_start is None
                    else t_start[lo : lo + chunk_size],
                    end=end,
                )
                for lo in range(0, t_stop.shape[0], chunk_size)
            ]
        )

    positions = torch.arange(
        1, int(t_stop.max().item()) + 1, device=t_stop.device
    ).unsqueeze(0)
    risk = positions < t_stop.unsqueeze(1)
    if t_start is not None:
        risk &= positions >= t_start.unsqueeze(1)
    logits = hazard_logit(
        theta.unsqueeze(1),
        r.unsqueeze(1),
        knot_y,
        knot_x,
        knot_count,
        c.unsqueeze(1),
        positions,
        T_j.unsqueeze(1),
        end,
    )
    return (F.logsigmoid(-logits) * risk).sum(1)


def monotone_spline_landmarks(data, starts, drops):
    """Build flattened decreasing landmarks from starts and positive drops.

    ``drops`` contains one row for every within-tossup knot transition.  The
    flattened return order matches ``spline_knot_indices``, so the ordinary
    interpolation and frozen-replay code does not need a monotone-specific
    path.
    """
    counts = data["spline_knot_counts"].detach().cpu().tolist()
    landmarks = []
    drop_offset = 0
    for tossup, count in enumerate(counts):
        transition_count = count - 1
        tossup_drops = drops[drop_offset : drop_offset + transition_count]
        cumulative_drop = torch.cat(
            (
                starts.new_zeros((1, starts.shape[-1])),
                torch.cumsum(tossup_drops, dim=0),
            ),
            dim=0,
        )
        landmarks.append(starts[tossup].unsqueeze(0) - cumulative_drop)
        drop_offset += transition_count
    if drop_offset != drops.shape[0]:
        raise ValueError(
            f"Expected {drop_offset} spline drops from knot counts, "
            f"received {drops.shape[0]}"
        )
    return torch.cat(landmarks, dim=0)


def materialize_spline_landmarks(data, posterior):
    """Add ordinary landmark tensors to a monotone guide posterior."""
    if "spline_y_correct" in posterior:
        return posterior
    posterior = dict(posterior)
    for suffix in ("correct", "hazard"):
        posterior[f"spline_y_{suffix}"] = monotone_spline_landmarks(
            data,
            posterior[f"spline_start_{suffix}"],
            posterior[f"spline_drop_{suffix}"],
        )
    return posterior


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


def sample_parameters(data, n_dimensions, monotone_decreasing=False):
    """Sample shared player parameters and separate branch spline parameters."""
    n_players = len(data["player_ids"])
    n_tossups = len(data["tossup_ids"])
    n_knots = int(data["n_spline_knots"])
    zero = data["y"].new_tensor(0.0)
    one = data["y"].new_tensor(1.0)
    vector_zero = data["y"].new_zeros(n_dimensions)
    vector_one = data["y"].new_ones(n_dimensions)
    with pyro.plate("players", n_players):
        theta = pyro.sample(
            "theta",
            dist.Normal(
                data.get("theta_prior_loc", vector_zero),
                data.get("theta_prior_scale", vector_one),
            ).to_event(1),
        )
        c = pyro.sample(
            "c",
            dist.Normal(
                data.get("c_prior_loc", zero),
                data.get("c_prior_scale", one),
            ),
        )
    with pyro.plate("tossups", n_tossups):
        correct_r = pyro.sample(
            "r_correct",
            dist.Gamma(2.0 * vector_one, 2.0 * vector_one).to_event(1),
        )
        hazard_r = pyro.sample(
            "r_hazard",
            dist.Gamma(2.0 * vector_one, 2.0 * vector_one).to_event(1),
        )
    if monotone_decreasing:
        n_drops = n_knots - n_tossups
        drop_scale = 0.5 * vector_one
        with pyro.plate("correct_spline_starts", n_tossups):
            correct_start = pyro.sample(
                "spline_start_correct",
                dist.Normal(vector_zero, vector_one).to_event(1),
            )
        with pyro.plate("correct_spline_drops", n_drops):
            correct_drop = pyro.sample(
                "spline_drop_correct", dist.HalfNormal(drop_scale).to_event(1)
            )
        with pyro.plate("hazard_spline_starts", n_tossups):
            hazard_start = pyro.sample(
                "spline_start_hazard",
                dist.Normal(vector_zero, vector_one).to_event(1),
            )
        with pyro.plate("hazard_spline_drops", n_drops):
            hazard_drop = pyro.sample(
                "spline_drop_hazard", dist.HalfNormal(drop_scale).to_event(1)
            )
        correct_y = monotone_spline_landmarks(
            data, correct_start, correct_drop
        )
        hazard_y = monotone_spline_landmarks(data, hazard_start, hazard_drop)
    else:
        with pyro.plate("correct_spline_knots", n_knots):
            correct_y = pyro.sample(
                "spline_y_correct", dist.Normal(vector_zero, vector_one).to_event(1)
            )
        with pyro.plate("hazard_spline_knots", n_knots):
            hazard_y = pyro.sample(
                "spline_y_hazard", dist.Normal(vector_zero, vector_one).to_event(1)
            )
    return theta, c, correct_r, hazard_r, correct_y, hazard_y


def row_parameters(data, theta, c, correct_r, hazard_r, correct_y, hazard_y):
    player, tossup = data["player"], data["tossup"]
    knot_indices = data["spline_knot_indices"][tossup]
    return (
        theta[player],
        c[player],
        correct_r[tossup],
        hazard_r[tossup],
        correct_y[knot_indices],
        hazard_y[knot_indices],
        data["spline_knot_positions"][tossup],
        data["spline_knot_counts"][tossup],
    )


def competing_risks_model(
    data,
    n_dimensions=1,
    calibrate_correctness=False,
    calibrate_scale=True,
    monotone_decreasing=False,
    terminal_intercepts=True,
):
    parameters = sample_parameters(data, n_dimensions, monotone_decreasing)
    end_correct, end_hazard = (
        sample_terminal_intercepts(data) if terminal_intercepts else (None, None)
    )
    theta, c, correct_r, hazard_r, correct_y, hazard_y, knot_x, knot_count = (
        row_parameters(data, *parameters)
    )
    survival = log_survival(
        theta,
        hazard_r,
        hazard_y,
        knot_x,
        knot_count,
        c,
        survival_stop(data),
        data["T_j"],
        t_start=data.get("t_start"),
        end=end_hazard,
    )
    buzz = data["is_buzz"]
    hazard_logits = hazard_logit(
        theta[buzz],
        hazard_r[buzz],
        hazard_y[buzz],
        knot_x[buzz],
        knot_count[buzz],
        c[buzz],
        data["t_star"][buzz],
        data["T_j"][buzz],
        end_hazard,
    )
    correctness = correctness_logit(
        theta[buzz],
        correct_r[buzz],
        correct_y[buzz],
        knot_x[buzz],
        knot_count[buzz],
        data["t_star"][buzz],
        data["T_j"][buzz],
        end_correct,
    )
    if calibrate_correctness:
        scale, bias = sample_correctness_calibration(data, with_scale=calibrate_scale)
        correctness = apply_correctness_calibration(correctness, scale, bias)
    likelihood = (
        survival.sum()
        + F.logsigmoid(hazard_logits).sum()
        + dist.Bernoulli(logits=correctness).log_prob(data["y"][buzz]).sum()
    )
    pyro.factor("linear_spline_double_difficulty_likelihood", likelihood)


def posterior_row_predictions(
    data, posterior, calibrate_correctness=False, calibrate_scale=True
):
    end_correct, end_hazard = posterior_terminal_intercepts(posterior)
    theta, c, correct_r, hazard_r, correct_y, hazard_y, knot_x, knot_count = (
        row_parameters(
            data,
            posterior["theta"],
            posterior["c"],
            posterior["r_correct"],
            posterior["r_hazard"],
            posterior["spline_y_correct"],
            posterior["spline_y_hazard"],
        )
    )
    correctness_logits = correctness_logit(
        theta,
        correct_r,
        correct_y,
        knot_x,
        knot_count,
        data["t_star"],
        data["T_j"],
        end_correct,
    )
    if calibrate_correctness:
        correctness_logits = apply_correctness_calibration(
            correctness_logits,
            posterior["correctness_scale"] if calibrate_scale else None,
            posterior["correctness_bias"],
        )
    hazard_logits = hazard_logit(
        theta,
        hazard_r,
        hazard_y,
        knot_x,
        knot_count,
        c,
        data["t_star"],
        data["T_j"],
        end_hazard,
    )
    survival = log_survival(
        theta,
        hazard_r,
        hazard_y,
        knot_x,
        knot_count,
        c,
        survival_stop(data),
        data["T_j"],
        t_start=data.get("t_start"),
        end=end_hazard,
    )
    return (
        torch.sigmoid(correctness_logits),
        torch.sigmoid(hazard_logits),
        torch.exp(survival),
    )


def expected_first_buzz_positions(data, posterior):
    """Return conditional expected first-buzz positions for phase-0 events."""
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

    _, end_hazard = posterior_terminal_intercepts(posterior)
    theta = posterior["theta"][roster]
    c = posterior["c"][roster]
    r = posterior["r_hazard"][event_tossup].unsqueeze(1)
    knot_indices = data["spline_knot_indices"][event_tossup]
    knot_y = posterior["spline_y_hazard"][knot_indices]
    knot_x = data["spline_knot_positions"][event_tossup]
    knot_count = data["spline_knot_counts"][event_tossup]
    event_survival = data["y"].new_ones(n_events)
    expected = data["y"].new_zeros(n_events)
    for position in range(1, int(event_T.max().item()) + 1):
        active = position <= event_T
        t = data["y"].new_full((n_events, max_roster), float(position))
        T = event_T.unsqueeze(1).expand_as(t)
        hazard = torch.sigmoid(
            hazard_logit(theta, r, knot_y, knot_x, knot_count, c, t, T, end_hazard)
        )
        hazard = torch.where(roster_mask, hazard, torch.zeros_like(hazard))
        total_hazard = 1.0 - torch.prod(1.0 - hazard, dim=1)
        total_hazard = torch.where(
            active, total_hazard, torch.zeros_like(total_hazard)
        )
        first = event_survival * total_hazard
        expected += position * first
        event_survival *= 1.0 - total_hazard
    buzz_mass = 1.0 - event_survival
    end = event_T.to(expected.dtype)
    expected = torch.where(
        buzz_mass > 1e-9, expected / buzz_mass.clamp_min(1e-9), end
    )
    relative = (expected / end).detach().cpu().tolist()
    return dict(zip(data["event_ids"], relative))
