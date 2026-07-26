"""Multidimensional-difficulty pyramidal tossup model.

Each latent skill dimension has its own difficulty curve:

    d_jk(t) = beta_jk * sigmoid(gamma_jk * (mu_jk - t / T_j))

The relevance vector 'r' weights the per-dimension skill gaps:

    correctness_logit = sum_k r_jk * (theta_ik - d_jk(t))
    hazard_logit = correctness_logit - c_i

'r' is a freely learned 'Gamma(2, 2)' vector. Its positive, unnormalized
coordinates give every added dimension independent capacity.

Important dimensions:

* 'n_rows' is the number of player-by-game-tossup observation rows.
* 'n_players' and 'n_tossups' count the unique players and tossups.
* 'n_dimensions' is the number of latent skill dimensions.

Important shapes:

* 'theta' has shape '(n_players, n_dimensions)' and 'c' has shape
  '(n_players,)'.
* 'r', 'beta', 'gamma', and 'mu' each have shape
  '(n_tossups, n_dimensions)'.
* After 'row_parameters' indexes by observation row, all six parameters have
  shape '(n_rows, n_dimensions)'.
"""

from __future__ import annotations

import torch
import torch.nn.functional as F
from torch.utils.checkpoint import checkpoint

import pyro
import pyro.distributions as dist

from utils.training import survival_chunk_size


# Opt-in link for the difficulty curve: sigmoid keeps d_jk(t) between 0 and
# beta_jk (the default); tanh lets it swing to -beta_jk late in the question.
DIFFICULTY_LINKS = {"sigmoid": torch.sigmoid, "tanh": torch.tanh}


def difficulty_curve(beta, gamma, mu, t, T_j, link="sigmoid"):
    """Return the per-dimension difficulty d_jk(t) at token position 't'.

    Each latent dimension 'k' gets its own sigmoid, so 'beta', 'gamma', and 'mu'
    carry a trailing dimension axis and the return value keeps shape
    '(..., n_dimensions)'.
    """
    # 't / T_j' is a scalar per row; unsqueeze so it broadcasts across dimensions.
    relative_position = (t / T_j).unsqueeze(-1)
    # d_jk(t) = beta_jk * link(gamma_jk * (mu_jk - t / T_j)).
    return beta * DIFFICULTY_LINKS[link](gamma * (mu - relative_position))


def correctness_logit(theta, r, beta, gamma, mu, t, T_j, link="sigmoid"):
    """Return the log-odds of a correct answer if the player buzzes at 't'.

    Each dimension's difficulty is subtracted from that dimension's skill, then
    the relevance-weighted sum collapses the dimension axis to '(n_rows,)'.
    """
    # Per-dimension skill gap theta_ik - d_jk(t).
    gap = theta - difficulty_curve(beta, gamma, mu, t, T_j, link)
    # sum_k r_jk * (theta_ik - d_jk(t)); r_jk >= 0 (see sample_parameters).
    return (r * gap).sum(-1)


def hazard_logit(theta, r, beta, gamma, mu, c, t, T_j, link="sigmoid"):
    """Return the buzz hazard logit at 't': correctness minus confidence 'c_i'."""
    return correctness_logit(theta, r, beta, gamma, mu, t, T_j, link) - c


def log_survival(
    theta, r, beta, gamma, mu, c, t_star, T_j, link="sigmoid", chunk_size=None, t_start=None
):
    """Return log probability of not buzzing across the interval '[t_start, t_star)'.

    Build one shared token grid, evaluate the hazard for every row-position
    pair, and sum the stable 'log(1 - hazard)' over positions in each row's risk
    interval. 't_start' (default 1) exceeds 1 only for phase-1 bounceback rows,
    where the opposing team enters the risk set at 't_neg + 1' after a neg;
    phase-0 rows keep the historical strict-before '[1, t_star)' survival exactly.
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
    )
    # sum_{s < t*} log(1 - h_ij(s)); F.logsigmoid(-logits) is log(1 - hazard).
    return (F.logsigmoid(-logits) * before_stop).sum(1)


def row_parameters(data, theta, c, r, beta, gamma, mu):
    """Index entity-level parameters down to one value per observation row."""
    player = data["player"]
    tossup = data["tossup"]
    # player/tossup are row index vectors of shape '(n_rows,)'. theta/c come from
    # the player axis; the four vector-valued tossup parameters come from the
    # tossup axis. Every returned tensor ends up '(n_rows, n_dimensions)'.
    return (
        theta[player],
        c[player],
        r[tossup],
        beta[tossup],
        gamma[tossup],
        mu[tossup],
    )


def sample_parameters(data, n_dimensions):
    """Sample player parameters and vector-valued tossup parameters.

    Player priors follow Eq. 14: 'theta ~ N(0, I)' and 'c ~ N(0, 1)', with
    optional held-out overrides attached to 'data'. Every tossup difficulty
    parameter is per-dimension.
    """
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
        # Positive relevance so higher skill on a loaded dimension always helps:
        # Gamma(concentration=2, rate=2) has mean 1 and stays nonnegative.
        r = pyro.sample(
            "r",
            dist.Gamma(2.0 * vector_one, 2.0 * vector_one).to_event(1),
        )
        beta = pyro.sample("beta", dist.Normal(vector_zero, vector_one).to_event(1))
        gamma = pyro.sample("gamma", dist.HalfCauchy(5.0 * vector_one).to_event(1))
        mu = pyro.sample(
            "mu",
            dist.Beta(
                # new_full keeps the concentration tensors on the data's device.
                data["y"].new_full((n_dimensions,), 2.0),
                data["y"].new_full((n_dimensions,), 2.0),
            ).to_event(1),
        )
    return theta, c, r, beta, gamma, mu


def sample_correctness_calibration(data):
    """Sample the global correctness recalibration scale and bias."""
    zero = data["y"].new_tensor(0.0)
    scale = pyro.sample(
        "correctness_scale", dist.LogNormal(zero, data["y"].new_tensor(0.5))
    )
    bias = pyro.sample("correctness_bias", dist.Normal(zero, data["y"].new_tensor(3.0)))
    return scale, bias


def competing_risks_model(data, n_dimensions=1, calibrate_correctness=False, link="sigmoid"):
    """Define the multidimensional-difficulty competing-risks likelihood.

    Every rostered player contributes survival before the stopping position. The
    actual first buzzer additionally
    contributes a hazard-at-'t_star' factor and an observed correctness factor,
    and the hand-computed joint log-likelihood is added with 'pyro.factor'.
    """
    theta, c, r, beta, gamma, mu = sample_parameters(data, n_dimensions)
    row_theta, row_c, row_r, row_beta, row_gamma, row_mu = row_parameters(
        data, theta, c, r, beta, gamma, mu
    )

    # Survival: every BUZZ, CENSORED, and NO-BUZZ row contributes over its risk
    # interval [t_start, t_star). 'data.get' keeps manual data dicts (no t_start)
    # on the historical [1, t_star) path.
    survival = log_survival(
        row_theta,
        row_r,
        row_beta,
        row_gamma,
        row_mu,
        row_c,
        data["t_star"],
        data["T_j"],
        link,
        t_start=data.get("t_start"),
    )
    # Event term: only observed first buzzers contribute hazard and correctness.
    buzz = data["is_buzz"]
    buzz_logits = hazard_logit(
        row_theta[buzz],
        row_r[buzz],
        row_beta[buzz],
        row_gamma[buzz],
        row_mu[buzz],
        row_c[buzz],
        data["t_star"][buzz],
        data["T_j"][buzz],
        link,
    )
    correctness = correctness_logit(
        row_theta[buzz],
        row_r[buzz],
        row_beta[buzz],
        row_gamma[buzz],
        row_mu[buzz],
        data["t_star"][buzz],
        data["T_j"][buzz],
        link,
    )
    if calibrate_correctness:
        # Apply calibration to correctness; hazard/timing keeps its base logit.
        scale, bias = sample_correctness_calibration(data)
        correctness = scale * correctness + bias

    log_likelihood = (
        # Sum log survival over every player-event row.
        survival.sum()
        # Sum log hazard and correctness log likelihood over first-buzzer rows.
        + F.logsigmoid(buzz_logits).sum()
        + dist.Bernoulli(logits=correctness).log_prob(data["y"][buzz]).sum()
    )
    pyro.factor("multidim_competing_risks_likelihood", log_likelihood)


def posterior_row_predictions(data, posterior, calibrate_correctness=False, link="sigmoid"):
    """Return fitted correctness, hazard, and survival for each row.

    Indexing each fitted parameter by the row's player and tossup recreates the
    row-level inputs used during training.
    """
    theta, c, r, beta, gamma, mu = row_parameters(
        data,
        posterior["theta"],
        posterior["c"],
        posterior["r"],
        posterior["beta"],
        posterior["gamma"],
        posterior["mu"],
    )
    correctness_logits = correctness_logit(
        theta, r, beta, gamma, mu, data["t_star"], data["T_j"], link
    )
    if calibrate_correctness:
        correctness_logits = (
            posterior["correctness_scale"] * correctness_logits
            + posterior["correctness_bias"]
        )
    correctness = torch.sigmoid(correctness_logits)
    hazard = torch.sigmoid(
        hazard_logit(theta, r, beta, gamma, mu, c, data["t_star"], data["T_j"], link)
    )
    survival = torch.exp(
        log_survival(
            theta,
            r,
            beta,
            gamma,
            mu,
            c,
            data["t_star"],
            data["T_j"],
            link,
            t_start=data.get("t_start"),
        )
    )
    return correctness, hazard, survival


def expected_first_buzz_positions(data, posterior, link="sigmoid"):
    """Compute the expected first-buzz relative position for each event.

    Observation rows are first regrouped into padded event rosters, then the
    function walks token by token and accumulates 't * P(first buzz at t)'. The
    returned position is E[t | a buzz occurs], matching the observed-buzz events
    used for evaluation.
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
    theta = posterior["theta"][roster]
    r = posterior["r"][event_tossup].unsqueeze(1)
    beta = posterior["beta"][event_tossup].unsqueeze(1)
    gamma = posterior["gamma"][event_tossup].unsqueeze(1)
    mu = posterior["mu"][event_tossup].unsqueeze(1)
    c = posterior["c"][roster]

    # event_survival is P(nobody has buzzed yet); expected accumulates
    # t * P(first buzz at t).
    event_survival = data["y"].new_ones(n_events)
    expected = data["y"].new_zeros(n_events)
    for position in range(1, int(event_T.max().item()) + 1):
        active_event = position <= event_T
        t = data["y"].new_full((n_events, max_roster), float(position))
        T = event_T.unsqueeze(1).expand_as(t)
        hazard = torch.sigmoid(hazard_logit(theta, r, beta, gamma, mu, c, t, T, link))
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
