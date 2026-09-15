"""Normalized discrete first-buzz law shared by training and replay.

For player logits eta, let q = product_i sigmoid(-eta_i). A cell has
P(no buzz) = q and P(winner=i) = (1-q) * softmax(eta)_i.
The allocation is proportional to hazard odds, equivalently normalized
sole-buzzer weights. It is an explicit categorical observation law, not a
claim that independent Bernoulli attempts cannot tie within a token.
"""

import numpy as np
import torch
import torch.nn.functional as F


FIRST_BUZZ_LIKELIHOOD = "normalized_hazard_odds_v1"


def cell_probabilities(logits, dim=0):
    """Return no-buzz, any-buzz, and conditional winner probabilities.

    Padded players may have logit -inf; each cell must have an active player.
    """
    log_no_buzz = F.logsigmoid(-logits).sum(dim=dim)
    return log_no_buzz.exp(), -torch.expm1(log_no_buzz), logits.softmax(dim=dim)


def survival_stop(data):
    """Exclusive survival bound; dead races survive THROUGH the final cell."""
    no_buzz = data.get("is_no_buzz")
    if no_buzz is None:
        return data["t_star"]
    return data["t_star"] + no_buzz.to(data["t_star"].dtype)


def _group_logsumexp(values, groups, n_groups):
    maximum = values.new_full((n_groups,), -torch.inf)
    maximum.scatter_reduce_(0, groups, values.detach(), reduce="amax")
    total = values.new_zeros(n_groups).scatter_add(
        0, groups, (values - maximum[groups]).exp()
    )
    # Empty groups (e.g. absent bounceback phases) never enter the result.
    return maximum + total.clamp_min(torch.finfo(values.dtype).tiny).log()


def winner_log_prob(data, row_logits):
    """Return log P(observed winner at stop | survival), one value per buzz.

    All active roster rows at their common stopping token are required, not
    just buzzers. Event and phase jointly identify a risk set, so an opponent
    continuation never competes with the original full-field first buzz.
    Survival before the stopping cell and correctness are added by callers.
    """
    if row_logits.shape != data["is_buzz"].shape:
        raise ValueError("winner_log_prob requires one logit per roster row")
    phase0 = data.get("is_phase0", torch.ones_like(data["is_buzz"]))
    groups = 2 * data["event"] + (~phase0).long()
    n_groups = 2 * len(data["event_ids"])
    buzz = data["is_buzz"]
    log_denominator = _group_logsumexp(row_logits, groups, n_groups)

    # -log(q) = sum softplus(eta). Work in log space even for eta=-1000,
    # where both sigmoid(eta) and softplus(eta) would underflow to zero.
    log_softplus = torch.where(
        row_logits < -35,
        row_logits,
        F.softplus(row_logits.clamp_min(-35)).log(),
    )
    log_exposure = _group_logsumexp(log_softplus, groups, n_groups)[groups[buzz]]
    exposure = log_exposure.exp()
    regular = (-torch.expm1(-exposure.clamp_min(1e-4))).log()
    small = exposure.clamp_max(1e-4)
    log_any = torch.where(
        exposure < 1e-4,
        log_exposure - small / 2 + small.square() / 24,
        regular,
    )
    return log_any + row_logits[buzz] - log_denominator[groups[buzz]]


def first_buzz_distribution(logits):
    """Return player-token mass and dead mass for a (players, tokens) grid.

    NumPy replay uses the same odds allocation as ``winner_log_prob``.
    Softmax from logits avoids the historical saturated-hazard fallback.
    """
    logits = np.asarray(logits, dtype=float)
    if logits.ndim != 2 or not logits.shape[0] or not logits.shape[1]:
        raise ValueError("expected a nonempty (players, tokens) logit grid")
    if not np.isfinite(logits).all():
        raise ValueError("first-buzz logits must be finite")
    log_no_buzz = -np.logaddexp(0.0, logits).sum(axis=0)
    survival_before = np.exp(np.r_[0.0, np.cumsum(log_no_buzz[:-1])])
    first_mass = survival_before * -np.expm1(log_no_buzz)
    weights = np.exp(logits - logits.max(axis=0, keepdims=True))
    attribution = weights / weights.sum(axis=0, keepdims=True)
    return attribution * first_mass[None, :], float(np.exp(log_no_buzz.sum()))
