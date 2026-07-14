"""Topic-weighted pyramidal tossup model (topic variant of Eq. 3-7, 13, 14).

This mirrors the root 'pyramidal_model.py' competing-risks likelihood, but uses
a CAIMIRA-style topic relevance vector for each tossup. The correctness logit is

    sum_k r_jk * (theta_ik - d_jk(t))

where 'r_j' is the fixed PLDA topic mixture and 'd_jk(t)' is a per-topic
difficulty curve. There is no learned tossup discrimination 'alpha'; the fixed
topic weights 'r_jk' take its place, and 'difficulty_beta', 'gamma', and 'mu' are learned
per topic so difficulty sits inside the weighted sum.

The topic weights are not latent Pyro parameters. They are fixed inputs loaded
from 'document_latent_vectors.csv' and attached to 'data["topic_weight"]'
before training.
"""

from __future__ import annotations

import torch
import torch.nn.functional as F

import pyro
import pyro.distributions as dist


def difficulty_curve(difficulty_beta, gamma, mu, t, T_j):
    """Return per-topic tossup difficulty d_jk(t) (Eq. 3, made per-topic)."""
    # difficulty_beta/gamma/mu end in the topic dimension. Token positions do not,
    # so add a trailing axis before broadcasting across topics.
    relative_position = (t / T_j).unsqueeze(-1)
    return difficulty_beta * torch.sigmoid(gamma * (mu - relative_position))


def topic_weighted_skill(theta, topic_weight):
    """Return 'sum_k r_jk * theta_ik'."""
    return (theta * topic_weight).sum(-1)


def correctness_logit(theta, topic_weight, difficulty_beta, gamma, mu, t, T_j):
    """Return 'sum_k r_jk * (theta_ik - d_jk(t))' at 't' (Eq. 4, r replaces alpha)."""
    gap = theta - difficulty_curve(difficulty_beta, gamma, mu, t, T_j)
    return (topic_weight * gap).sum(-1)


def hazard_logit(theta, topic_weight, difficulty_beta, gamma, mu, c, t, T_j):
    """Return the topic-weighted buzz hazard logit at 't' (Eq. 5: correctness - c)."""
    return correctness_logit(theta, topic_weight, difficulty_beta, gamma, mu, t, T_j) - c


def log_survival(theta, topic_weight, difficulty_beta, gamma, mu, c, t_star, T_j):
    """Return log probability of not buzzing before 't_star' (Eq. 6).

    't_star' is the first buzz for BUZZ/CENSORED rows and 'T_j' for NO-BUZZ rows
    (the dead-tossup convention, Eq. 13).
    """
    max_t = int(t_star.max().item())
    positions = torch.arange(1, max_t + 1, device=t_star.device).unsqueeze(0)
    # Eq. 6 is strict-before survival, and Eq. 13 deliberately uses S(T_j) for
    # dead tossups. NO-BUZZ rows therefore stop at T_j - 1 under the paper's
    # indexing convention; an inclusive mask would define a different model.
    before_stop = positions < t_star.unsqueeze(1)
    # Unsqueezing row parameters broadcasts them against every token position,
    # producing one hazard logit per row-position pair.
    logits = hazard_logit(
        theta.unsqueeze(1),
        topic_weight.unsqueeze(1),
        difficulty_beta.unsqueeze(1),
        gamma.unsqueeze(1),
        mu.unsqueeze(1),
        c.unsqueeze(1),
        positions,
        T_j.unsqueeze(1),
    )
    return (F.logsigmoid(-logits) * before_stop).sum(1)


def row_parameters(data, theta, c, difficulty_beta, gamma, mu):
    """Index entity-level parameters and fixed topic weights by row."""
    player = data["player"]
    tossup = data["tossup"]
    # data["topic_weight"] is stored by tossup, not by observation row. Indexing
    # it with the same tossup vector keeps each row's fixed topic mixture
    # aligned with that row's learned per-topic difficulty parameters.
    return (
        theta[player],
        c[player],
        data["topic_weight"][tossup],
        difficulty_beta[tossup],
        gamma[tossup],
        mu[tossup],
    )


def sample_parameters(data, n_dimensions):
    """Sample player and per-topic tossup difficulty parameters (Eq. 14)."""
    n_players = len(data["player_ids"])
    n_tossups = len(data["tossup_ids"])
    zero = data["y"].new_tensor(0.0)
    one = data["y"].new_tensor(1.0)
    vector_zero = data["y"].new_zeros(n_dimensions)
    vector_one = data["y"].new_ones(n_dimensions)

    # Player priors as in root CompIRT: theta_i ~ N(0, I), c_i ~ N(0, 1) by
    # default. Held-out evaluation can attach informative per-player priors to
    # 'data' (training posterior for returning players, tier-conditioned for
    # new players); absent keys reproduce the standard model exactly.
    theta_loc = data.get("theta_prior_loc", vector_zero)
    theta_scale = data.get("theta_prior_scale", vector_one)
    c_loc = data.get("c_prior_loc", zero)
    c_scale = data.get("c_prior_scale", one)
    with pyro.plate("players", n_players):
        theta = pyro.sample("theta", dist.Normal(theta_loc, theta_scale).to_event(1))
        c = pyro.sample("c", dist.Normal(c_loc, c_scale))

    # Tossup priors, now per-topic and with no 'alpha': difficulty_beta/gamma/mu
    # each have shape (n_tossups, n_dimensions). The sample site stays "beta" for
    # backwards-compatible posterior keys and CSV columns.
    with pyro.plate("tossups", n_tossups):
        difficulty_beta = pyro.sample(
            "beta", dist.Normal(vector_zero, vector_one).to_event(1)
        )
        gamma = pyro.sample("gamma", dist.HalfCauchy(5.0 * vector_one).to_event(1))
        mu = pyro.sample(
            "mu",
            dist.Beta(
                data["y"].new_full((n_dimensions,), 2.0),
                data["y"].new_full((n_dimensions,), 2.0),
            ).to_event(1),
        )
    return theta, c, difficulty_beta, gamma, mu


def sample_correctness_calibration(data):
    """Sample the global correctness recalibration scale and bias."""
    zero = data["y"].new_tensor(0.0)
    scale = pyro.sample(
        "correctness_scale", dist.LogNormal(zero, data["y"].new_tensor(0.5))
    )
    bias = pyro.sample("correctness_bias", dist.Normal(zero, data["y"].new_tensor(3.0)))
    return scale, bias


def competing_risks_model(data, n_dimensions=None, calibrate_correctness=False):
    """Define the topic-weighted competing-risks likelihood (Eq. 7 / Eq. 12)."""
    if n_dimensions is None:
        n_dimensions = data["topic_weight"].shape[1]
    theta, c, difficulty_beta, gamma, mu = sample_parameters(data, n_dimensions)
    (
        row_theta,
        row_c,
        row_topic_weight,
        row_difficulty_beta,
        row_gamma,
        row_mu,
    ) = row_parameters(data, theta, c, difficulty_beta, gamma, mu)

    # Eq. 6 survival on every BUZZ, CENSORED, and NO-BUZZ row (Eq. 13 enters via
    # t_star = T_j on NO-BUZZ rows). Only the logits use the topic-weighted gap.
    survival = log_survival(
        row_theta,
        row_topic_weight,
        row_difficulty_beta,
        row_gamma,
        row_mu,
        row_c,
        data["t_star"],
        data["T_j"],
    )
    # Eq. 7 / Eq. 12 event term: only actual first-buzzer rows contribute the
    # hazard-at-t* and correctness factors.
    buzz = data["is_buzz"]
    buzz_logits = hazard_logit(
        row_theta[buzz],
        row_topic_weight[buzz],
        row_difficulty_beta[buzz],
        row_gamma[buzz],
        row_mu[buzz],
        row_c[buzz],
        data["t_star"][buzz],
        data["T_j"][buzz],
    )
    correctness = correctness_logit(
        row_theta[buzz],
        row_topic_weight[buzz],
        row_difficulty_beta[buzz],
        row_gamma[buzz],
        row_mu[buzz],
        data["t_star"][buzz],
        data["T_j"][buzz],
    )
    if calibrate_correctness:
        # Recalibrate ONLY the correctness logit, leaving the hazard/timing
        # (which also calls correctness_logit) untouched.
        scale, bias = sample_correctness_calibration(data)
        correctness = scale * correctness + bias
    # Eq. 7 / Eq. 12 in log space:
    #   sum_i log S_ij(t*) + log h_i*j(t*) + log Bernoulli(y_i*j | p_i*j(t*)).
    # Competing risks are not a single built-in distribution, so the joint
    # log-likelihood is hand-computed and attached with pyro.factor.
    log_likelihood = (
        # Sum log survival over every player-event row: BUZZ, CENSORED, NO-BUZZ.
        survival.sum()
        # Sum log hazard only over observed first-buzzer rows.
        + F.logsigmoid(buzz_logits).sum()
        # Sum correctness log likelihood only over observed first-buzzer rows.
        + dist.Bernoulli(logits=correctness).log_prob(data["y"][buzz]).sum()
    )
    pyro.factor("topic_weighted_competing_risks_likelihood", log_likelihood)


def posterior_row_predictions(data, posterior, calibrate_correctness=False):
    """Return fitted correctness, hazard, and survival per row (Eq. 4/5/6 replay)."""
    # Replay the row-level topic-weighted logits at posterior medians so saved
    # CSVs match the training likelihood.
    theta, c, topic_weight, difficulty_beta, gamma, mu = row_parameters(
        data,
        posterior["theta"],
        posterior["c"],
        posterior["beta"],
        posterior["gamma"],
        posterior["mu"],
    )
    correctness_logits = correctness_logit(
        theta, topic_weight, difficulty_beta, gamma, mu, data["t_star"], data["T_j"]
    )
    if calibrate_correctness:
        correctness_logits = (
            posterior["correctness_scale"] * correctness_logits
            + posterior["correctness_bias"]
        )
    correctness = torch.sigmoid(correctness_logits)
    hazard = torch.sigmoid(
        hazard_logit(
            theta, topic_weight, difficulty_beta, gamma, mu, c, data["t_star"], data["T_j"]
        )
    )
    survival = torch.exp(
        log_survival(
            theta,
            topic_weight,
            difficulty_beta,
            gamma,
            mu,
            c,
            data["t_star"],
            data["T_j"],
        )
    )
    return correctness, hazard, survival


def expected_first_buzz_positions(data, posterior):
    """Compute expected first-buzz relative positions with topic-weighted hazards.

    Rows are regrouped into padded event rosters, then walked token by token:
    P(first buzz at t) = P(no earlier team buzz) * P(at least one buzzes at t),
    using the Eq. 5 hazards. Leftover probability goes to the question end.
    """
    n_events = len(data["event_ids"])
    counts = torch.bincount(data["event"], minlength=n_events)
    max_roster = int(counts.max().item())
    roster = data["player"].new_zeros((n_events, max_roster))
    roster_mask = torch.zeros(
        (n_events, max_roster), dtype=torch.bool, device=data["event"].device
    )
    next_slot = [0] * n_events
    event_tossup = data["tossup"].new_zeros(n_events)
    event_T = data["T_j"].new_ones(n_events)
    for row in range(len(data["event"])):
        # Training rows are player-event rows. This loop rebuilds one padded
        # roster per event so the team first-buzz distribution can be simulated.
        event = int(data["event"][row].item())
        slot = next_slot[event]
        roster[event, slot] = data["player"][row]
        roster_mask[event, slot] = True
        event_tossup[event] = data["tossup"][row]
        event_T[event] = data["T_j"][row]
        next_slot[event] += 1

    theta = posterior["theta"][roster]
    topic_weight = data["topic_weight"][event_tossup].unsqueeze(1)
    difficulty_beta = posterior["beta"][event_tossup].unsqueeze(1)
    gamma = posterior["gamma"][event_tossup].unsqueeze(1)
    mu = posterior["mu"][event_tossup].unsqueeze(1)
    c = posterior["c"][roster]

    event_survival = data["y"].new_ones(n_events)
    expected = data["y"].new_zeros(n_events)
    for position in range(1, int(event_T.max().item()) + 1):
        # At each token, combine independent player hazards into the chance
        # that at least one roster member produces the first buzz right now.
        active_event = position <= event_T
        t = data["y"].new_full((n_events, max_roster), float(position))
        T = event_T.unsqueeze(1).expand_as(t)
        # Eq. 5 hazards reused to derive a team first-buzz distribution.
        hazard = torch.sigmoid(
            hazard_logit(theta, topic_weight, difficulty_beta, gamma, mu, c, t, T)
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
