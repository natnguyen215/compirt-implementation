"""Pyramidal tossup IRT models from Equations 3--7 and 13 of CompIRT.

A tossup's difficulty changes as clues are revealed. For each player-question
pair the model separates three quantities:

* correctness: would this player answer correctly if they buzzed now?
* hazard: conditional on not buzzing earlier, do they buzz now?
* survival: probability they have not buzzed before now.

Functions are vectorized over rows. The final dimension of 'theta' and 'alpha'
is always the latent skill dimension.

Important Dimensions:

* 'n_rows' is the number of player-by-game-tossup observation rows.
    - If one player buzzes first, that event creates
        - one 'BUZZ' row for the buzzer
        - 'CENSORED' rows for the other rostered players.
    - If nobody buzzes, it creates
        - 'NO-BUZZ' rows.
* 'n_players' and 'n_tossups' count the unique players and tossups.
* 'n_dimensions' is the number of latent skill dimensions.

Important Shapes:

* data is a Python dict of PyTorch tensors and ID lists of players, tossups, and events
* Before indexing by observation row, player parameters are stored by player:
    - 'theta' has shape '(n_players, n_dimensions)'
    - 'c' has shape '(n_players,)'.
* Before indexing by observation row, tossup parameters are stored by tossup:
    - 'alpha' has shape '(n_tossups, n_dimensions)',
    - 'beta', 'gamma', and 'mu' each have shape '(n_tossups,)'.
* 'data["player"]' and 'data["tossup"]' each have shape '(n_rows,)'.
   They say which player and tossup belong to each observation row.
* After 'row_parameters' uses those row indexes,
    - 'theta' and 'alpha' have shape '(n_rows, n_dimensions)'
    - The scalar parameters 'c', 'beta', 'gamma', and 'mu' have shape '(n_rows,)'
* Row-level data such as 'data["t_star"]', 'data["T_j"]', 'data["y"]', and
  'data["is_buzz"]' have shape '(n_rows,)'.
* Inside 'log_survival',
    - token positions are broadcast to shape '(n_rows, max_t)'.
    - That lets each row sum no-buzz log-probabilities over
      positions before its own 't_star'.
"""

import torch
import torch.nn.functional as F

from compirt_race import winner_log_prob, survival_stop
import pyro
import pyro.distributions as dist

from utils.prediction import event_rosters


def difficulty_curve(beta, gamma, mu, t, T_j):
    """Return the question's difficulty at token position 't'.

    't / T_j' is the relative position (0-1).
    'beta' is the size/sign of the difficulty
    'gamma' controls sharpness of difficulty transitions
    'mu' is the inflection point.
    """
    # Eq. 3: b_j(t) = beta_j * sigmoid(gamma_j * (mu_j - t / T_j)).
    # Return shape: (n_rows,).
    return beta * torch.sigmoid(gamma * (mu - t / T_j))


def correctness_logit(theta, alpha, beta, gamma, mu, t, T_j):
    """Return the log-odds of a correct answer if the player buzzes at 't'.

    'theta' is player skill
    'alpha' is discrimination
    """
    # Eq. 4 logit: theta_i^T alpha_j - d_j(t).
    skill = (theta * alpha).sum(-1)
    # Return shape: (n_rows,).
    return skill - difficulty_curve(beta, gamma, mu, t, T_j)


def hazard_logit(theta, alpha, beta, gamma, mu, c, t, T_j):
    """Return the log-odds of buzzing at 't', conditional on no earlier buzz.

    Given that the player has not buzzed before
    this token, what is the probability that they buzz now?

    'c' is the confidence threshold
    """
    # Eq. 5 logit: theta_i^T alpha_j - b_j(t) - c_i.
    # Return shape: (n_rows,).
    return correctness_logit(theta, alpha, beta, gamma, mu, t, T_j) - c


def log_survival(theta, alpha, beta, gamma, mu, c, t_star, T_j, t_start=None):
    """Return log probability of not buzzing across the interval '[t_start, t_star)'.

    This is the survival term from Eq. 6. For each row, it asks:

        What is the probability this player did not buzz between the row's start
        token and its stopping position?

    'T_j' is the total number of tokens in the tossup
    't_star' is the buzz token

    * for a 'BUZZ' row, it is that player's first-buzz position
    * for a 'CENSORED' row, 't_star' is the same as the first buzz position of the buzzed player
    * for a 'NO-BUZZ' row, 't_star' = 'T_j'.

    't_start' is the first token the player is at risk (default 1). It is greater
    than 1 only for phase-1 bounceback rows, where the opposing team enters the
    risk set at 't_neg + 1' after a neg; phase-0 rows keep the historical
    '[1, t_star)' survival exactly.

    Survival is a product over token positions in the interval:

        S = product over t_start <= s < t_star of (1 - hazard(s))

    The code returns 'log S' instead of 'S' because summing log probabilities is
    more stable than multiplying many small probabilities.

    """
    # Build one shared token-position grid: [1, 2, ..., max_t].
    max_t = int(t_star.max().item())
    positions = torch.arange(1, max_t + 1, device=t_star.device).unsqueeze(0)
    # Survival is strictly before its exclusive bound. Training and replay
    # pass T_j + 1 for dead rows so they include the final no-buzz cell.
    # Shape: '(n_rows, max_t)' after broadcasting.
    before_stop = positions < t_star.unsqueeze(1)
    if t_start is not None:
        # Bounceback rows survive only from t_start onward; phase-0 rows pass
        # t_start = 1 (or None), for which this mask is all-True from position 1.
        before_stop = before_stop & (positions >= t_start.unsqueeze(1))

    # Unsqueezing row parameters lets PyTorch evaluate the hazard for every
    # row-position pair, producing logits with shape '(n_rows, max_t)'.
    logits = hazard_logit(
        theta.unsqueeze(1),
        alpha.unsqueeze(1),
        beta.unsqueeze(1),
        gamma.unsqueeze(1),
        mu.unsqueeze(1),
        c.unsqueeze(1),
        positions,
        T_j.unsqueeze(1),
    )

    # Eq. 6 in log space:
    #   log S_ij(t*) = sum_{s < t*} log(1 - h_ij(s)).
    # F.logsigmoid(-logits) is log(1 - hazard), computed stably.
    # Multiplying by 'before_stop' ignores positions at/after 't_star'.
    # Return shape: (n_rows,).
    return (F.logsigmoid(-logits) * before_stop).sum(1)


def row_parameters(data, theta, c, alpha, beta, gamma, mu):
    """Index entity-level parameters down to one value per observation row."""
    player = data["player"]
    tossup = data["tossup"]

    # Before indexing, player parameters are
    # theta: (n_players, n_dimensions)
    # c: (n_players,)
    #
    # tossup parameters are
    # alpha: (n_tossups, n_dimensions)
    # beta/gamma/mu: (n_tossups,).
    #
    # player/tossup are row index vectors with shape (n_rows,), so each returned
    # value is aligned to observations: theta/alpha become
    # (n_rows, n_dimensions), while c/beta/gamma/mu become (n_rows,).

    return (
        theta[player],
        c[player],
        alpha[tossup],
        beta[tossup],
        gamma[tossup],
        mu[tossup],
    )


def sample_parameters(data, n_dimensions):
    """Sample the latent player and tossup parameters from their priors."""
    n_players = len(data["player_ids"])
    n_tossups = len(data["tossup_ids"])
    zero = data["y"].new_tensor(0.0)
    one = data["y"].new_tensor(1.0)
    vector_zero = data["y"].new_zeros(n_dimensions)
    vector_one = data["y"].new_ones(n_dimensions)

    # Eq. 14 player priors:
    # theta_i ~ N(0, I), c_i ~ N(0, 1) by default. For held-out evaluation the
    # caller can attach informative per-player priors to 'data' (training
    # posterior for returning players, tier-conditioned for new players).
    # Absent keys use the standard zero-location, unit-scale priors.
    # Dimensions:
    # theta: (n_players, n_dimensions), c: (n_players,).
    theta_loc = data.get("theta_prior_loc", vector_zero)
    theta_scale = data.get("theta_prior_scale", vector_one)
    c_loc = data.get("c_prior_loc", zero)
    c_scale = data.get("c_prior_scale", one)
    with pyro.plate("players", n_players):
        theta = pyro.sample("theta", dist.Normal(theta_loc, theta_scale).to_event(1))
        # Treat the whole skill vector as one player's latent event.
        c = pyro.sample("c", dist.Normal(c_loc, c_scale))

    # Eq. 14 tossup priors:
    # alpha_j ~ N(0, I), beta_j ~ N(0, 1),
    # gamma_j ~ Half-Cauchy(5), mu_j ~ Beta(2, 2).
    # Dimensions:
    # alpha: (n_tossups, n_dimensions), other tossup parameters: (n_tossups,).
    # y is the correctness label: NaN on censored and no-buzz. 1 or 0 on buzz.
    with pyro.plate("tossups", n_tossups):
        alpha = pyro.sample("alpha", dist.Normal(vector_zero, vector_one).to_event(1))
        beta = pyro.sample("beta", dist.Normal(zero, one))
        gamma = pyro.sample("gamma", dist.HalfCauchy(5.0 * one))
        mu = pyro.sample(
            "mu",
            dist.Beta(data["y"].new_tensor(2.0), data["y"].new_tensor(2.0)),
            # Build constants with the observation tensor's dtype and device.
        )
    return theta, c, alpha, beta, gamma, mu


def sample_correctness_calibration(data):
    """Sample the global correctness recalibration scale and bias."""
    zero = data["y"].new_tensor(0.0)
    scale = pyro.sample(
        "correctness_scale", dist.LogNormal(zero, data["y"].new_tensor(0.5))
    )
    bias = pyro.sample("correctness_bias", dist.Normal(zero, data["y"].new_tensor(3.0)))
    return scale, bias


def competing_risks_model(data, n_dimensions=1, calibrate_correctness=False):
    """Define the competing-risks likelihood for tossup observations.

    Each rostered player is a competing risk because any player could produce
    the event's first recorded buzz. For every game-tossup event:

    * all rostered players contribute survival before the stopping position;
    * the winner contributes a normalized categorical probability at that position;
    * the actual first buzzer contributes observed correctness;
    * a dead tossup has only the roster's survival contributions.
    """
    # Sample entity-level parameters, then align them with observation rows.
    theta, c, alpha, beta, gamma, mu = sample_parameters(data, n_dimensions)
    row_theta, row_c, row_alpha, row_beta, row_gamma, row_mu = row_parameters(
        data, theta, c, alpha, beta, gamma, mu
    )

    # Survival is before the observed buzz, or through T_j for a dead race.
    # Missing t_start means the risk interval begins at token 1.
    survival = log_survival(
        row_theta,
        row_alpha,
        row_beta,
        row_gamma,
        row_mu,
        row_c,
        survival_stop(data),
        data["T_j"],
        data.get("t_start"),
    )
    # The exclusive-winner factor requires all roster hazards at t_star.
    # Only the observed winner contributes a correctness mark.
    buzz = data["is_buzz"]
    stop_hazard_logits = hazard_logit(
        row_theta,
        row_alpha,
        row_beta,
        row_gamma,
        row_mu,
        row_c,
        data["t_star"],
        data["T_j"],
    )
    correctness = correctness_logit(
        row_theta[buzz],
        row_alpha[buzz],
        row_beta[buzz],
        row_gamma[buzz],
        row_mu[buzz],
        data["t_star"][buzz],
        data["T_j"][buzz],
    )
    if calibrate_correctness:
        # Apply calibration to correctness; hazard/timing keeps its base logit.
        scale, bias = sample_correctness_calibration(data)
        correctness = scale * correctness + bias
    # Normalized event law in log space:
    #   roster log survival + log P(winner at t*) + log P(correctness mark).
    # The joint log-likelihood is one scalar for the full dataset.
    log_likelihood = (
        survival.sum()
        + winner_log_prob(data, stop_hazard_logits).sum()
        + dist.Bernoulli(logits=correctness).log_prob(data["y"][buzz]).sum()
    )
    # Attach the hand-computed competing-risks log-likelihood with pyro.factor.
    pyro.factor("competing_risks_likelihood", log_likelihood)


def posterior_row_predictions(data, posterior, calibrate_correctness=False):
    """Return fitted correctness, hazard, and survival for every input row.

    Indexing each fitted parameter by the row's player and tossup recreates the
    row-level inputs used during training.
    """
    theta, c, alpha, beta, gamma, mu = row_parameters(
        data,
        posterior["theta"],
        posterior["c"],
        posterior["alpha"],
        posterior["beta"],
        posterior["gamma"],
        posterior["mu"],
    )
    # Posterior prediction from Eq. 4, Eq. 5, and Eq. 6 for each row.
    correctness_logits = correctness_logit(
        theta, alpha, beta, gamma, mu, data["t_star"], data["T_j"]
    )
    if calibrate_correctness:
        correctness_logits = (
            posterior["correctness_scale"] * correctness_logits
            + posterior["correctness_bias"]
        )
    correctness = torch.sigmoid(correctness_logits)
    hazard = torch.sigmoid(
        hazard_logit(theta, alpha, beta, gamma, mu, c, data["t_star"], data["T_j"])
    )
    survival = torch.exp(
        log_survival(
            theta,
            alpha,
            beta,
            gamma,
            mu,
            c,
            survival_stop(data),
            data["T_j"],
            data.get("t_start"),
        )
    )
    return correctness, hazard, survival


def expected_first_buzz_positions(data, posterior):
    """Compute the expected first-buzz relative position for each event.

    Observation rows are first regrouped into padded event rosters. The
    function then walks token by token and computes:

        P(first buzz at t)
          = P(no earlier team buzz) * P(at least one player buzzes at t)

    The returned position is E[t | a buzz occurs], matching the observed-buzz
    events used for evaluation. Scoring this distribution mean against one draw
    per event gives downstream MAE an irreducible within-event spread floor.
    """
    # Rebuild the full first-buzz field before broadcasting fitted parameters.
    roster, roster_mask, event_tossup, event_T = event_rosters(data)
    n_events, max_roster = roster.shape

    # Parameter shapes now begin with (n_events, max_roster, ...).
    theta = posterior["theta"][roster]
    alpha = posterior["alpha"][event_tossup].unsqueeze(1)
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
        # Eq. 5 hazards are reused to derive a team first-buzz distribution.
        hazard = torch.sigmoid(hazard_logit(theta, alpha, beta, gamma, mu, c, t, T))
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
