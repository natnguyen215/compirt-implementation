"""Combine fixed player skills into team-level bonus-part predictions.

This is the second stage of the CompIRT pipeline. The pyramidal tossup model
first estimates each player's skill vector 'theta'. This model keeps those
vectors fixed and learns how strongly each bonus part rewards those skills.

Each observation is one team attempting one bonus part. The model combines all
roster members' part abilities, optionally applies pairwise synergy, and predicts
whether the part was answered correctly.

Bonus-model options:

* 'bonus_aggregation' combines teammates with the paper's Eq. 8 log-sum-exp
  ('lse'), the best teammate on each skill axis ('max'), or the paper's Eq. 9
  Noisy-OR ('noisy-or').
* 'bonus_difficulty' is one scalar per part ('scalar') or one coordinate per
  skill dimension, weighted by positive relevance 'r' ('multidim').
* 'synergy_form' picks the pair formula, and 'synergy_link' either adds
  synergy to the base logit or scales the base logit by it.

Important Dimensions:

* 'n_observations' is the number of team-by-bonus-part rows. Each row is one
  team attempting one bonus part.
* 'n_players' and 'n_parts' count the unique players and bonus parts.
* 'n_dimensions' is the number of latent skill dimensions shared with the tossup
  model through the fixed 'theta' input.
* 'max_roster_size' is the largest roster. Shorter rosters are padded, and the
  padded slots are tracked by a boolean mask.
* 'synergy_dimensions' is the size of each player's synergy profile.

Important Shapes:

* data is a Python dict of PyTorch tensors and ID lists of players and bonus parts.
* 'theta' is fixed input from the tossup model with shape
  '(n_players, n_dimensions)'.
* Before indexing by observation row, bonus-part parameters are stored by part:
    - 'alpha' (named 'r' with multidim difficulty) has shape '(n_parts, n_dimensions)'
    - 'beta' has shape '(n_parts,)', or '(n_parts, n_dimensions)' with multidim difficulty.
* 'tau' is a single scalar used by LSE aggregation, and 'psi' has shape
  '(n_players, synergy_dimensions)'. The phi-psi variant also learns 'phi'
  with the same shape as 'psi'.
* 'data["part"]' has shape '(n_observations,)'. It says which bonus part each
  row attempts.
* 'data["roster"]' and 'data["roster_mask"]' each have shape
  '(n_observations, max_roster_size)'. 'roster' lists the player id in every
  slot, and 'roster_mask' is True only for real (non-padded) slots.
* 'data["y"]' has shape '(n_observations,)' and holds the 0/1 correctness label.
* After indexing rosters by player,
    - 'member_theta' has shape '(n_observations, max_roster_size, n_dimensions)'
    - 'member_abilities' has shape '(n_observations, max_roster_size)'.
"""

import math

import torch

import pyro
import pyro.distributions as dist


BONUS_AGGREGATIONS = ("lse", "max", "noisy-or")
BONUS_DIFFICULTIES = ("scalar", "multidim")
SYNERGY_FORMS = ("dot", "phi-psi")
SYNERGY_LINKS = ("additive", "multiplicative")


def validate_bonus_settings(
    bonus_aggregation="lse",
    bonus_difficulty="scalar",
    *,
    use_synergy=False,
    calibrate_correctness=False,
    synergy_form="dot",
    synergy_link="additive",
    synergy_dimensions=1,
    alpha_prior=None,
):
    """Raise ValueError for an unknown or incompatible bonus-model setting.

    Training, replay, and the fold runner share these rules. 'alpha_prior' is
    checked only when given, because replay reads fitted weights directly.
    """
    if bonus_aggregation not in BONUS_AGGREGATIONS:
        raise ValueError(f"Unknown bonus aggregation: {bonus_aggregation}")
    if bonus_difficulty not in BONUS_DIFFICULTIES:
        raise ValueError(f"Unknown bonus difficulty: {bonus_difficulty}")
    if synergy_form not in SYNERGY_FORMS:
        raise ValueError(f"Unknown synergy form: {synergy_form}")
    if synergy_link not in SYNERGY_LINKS:
        raise ValueError(f"Unknown synergy link: {synergy_link}")
    # Eq. 9 is the paper's independent-member baseline: one scalar difficulty
    # inside each member's sigmoid and nothing added to the team logit.
    if bonus_aggregation == "noisy-or" and (
        bonus_difficulty != "scalar" or use_synergy or calibrate_correctness
    ):
        raise ValueError("Eq. 9 noisy-or requires scalar difficulty, no synergy, and no calibration")
    # Multidim difficulty weights its coordinates by relevance, which must be positive.
    if bonus_difficulty == "multidim" and alpha_prior not in (None, "gamma"):
        raise ValueError("Multidim bonus difficulty requires alpha_prior='gamma' for positive relevance")
    if synergy_form != "dot" and not use_synergy:
        raise ValueError("phi-psi synergy requires use_synergy=True")
    if synergy_link != "additive" and not use_synergy:
        raise ValueError("multiplicative synergy requires use_synergy=True")
    if use_synergy and synergy_dimensions < 1:
        raise ValueError("synergy_dimensions must be positive")


def part_weight_site(bonus_difficulty):
    """Return the sample-site name of each bonus part's skill weights.

    Scalar difficulty uses discrimination 'alpha'. Multidim difficulty uses
    relevance 'r', matching the multidim pyramidal stage.
    """
    return "r" if bonus_difficulty == "multidim" else "alpha"


def lse_aggregation(member_abilities, roster_mask, tau):
    """Return one aggregate team-knowledge value from member abilities.

    'member_abilities' and 'roster_mask' have shape '(n_observations, max_roster_size)'.
    'tau' is the aggregation temperature.
    """
    # Eq. 8: A_k(T) = tau * log sum_m exp(alpha_k^T theta_p_m / tau).
    # masked_fill sets padded slots to -inf so they drop out of logsumexp.
    scaled = (member_abilities / tau).masked_fill(~roster_mask, -torch.inf)
    # Return shape: (n_observations,).
    return tau * torch.logsumexp(scaled, dim=1)


def pool_team_skills(member_theta, roster_mask, bonus_aggregation, tau=None):
    """Pool teammates separately on each skill axis.

    'member_theta' has shape '(n_observations, max_roster_size, n_dimensions)'.
    'max' keeps the best active teammate on each axis. 'lse' applies the Eq. 8
    smooth maximum to each axis: ts_k = tau * log sum_m exp(theta_mk / tau).
    """
    # Padded slots become -inf so they never win the max or enter logsumexp.
    padding = ~roster_mask.unsqueeze(-1)
    if bonus_aggregation == "max":
        team_skills = member_theta.masked_fill(padding, -torch.inf).amax(dim=1)
    else:
        scaled = (member_theta / tau).masked_fill(padding, -torch.inf)
        team_skills = tau * torch.logsumexp(scaled, dim=1)
    # Return shape: (n_observations, n_dimensions).
    return team_skills


def noisy_or_logits(member_logits, roster_mask):
    """Return the Eq. 9 logit that at least one active member knows the answer.

    Members answer independently, so P(team) = 1 - prod_m (1 - sigmoid(eta_m)).
    'member_logits' and 'roster_mask' have shape '(n_observations, max_roster_size)'.
    The calculation stays in log space so logits and gradients remain finite
    when P(team) rounds to zero or one.
    """
    # log P(member m misses). Padded slots add log(1) = 0.
    failure = torch.nn.functional.logsigmoid(-member_logits).masked_fill(~roster_mask, 0)
    # log P(every earlier slot missed), shifted so slot 0 starts at log(1) = 0.
    preceding = torch.cat((failure.new_zeros((len(failure), 1)),
                           failure.cumsum(1)[:, :-1]), dim=1)
    # log P(member m answers). Padded slots get -inf so they cannot answer.
    success = torch.nn.functional.logsigmoid(member_logits).masked_fill(~roster_mask, -torch.inf)
    # P(team) sums the disjoint events "slot m is the first to answer", and
    # log(1 - P(team)) sums every member's miss, so their difference is the logit.
    # Return shape: (n_observations,).
    return torch.logsumexp(success + preceding, dim=1) - failure.sum(1)


def synergy_contribution(psi, roster, roster_mask, phi=None):
    """Return the summed pairwise synergy for every roster.

    'psi' is the per-player synergy profile. A pair's synergy is the dot product
    of their two profiles, and a roster's synergy is that dot product summed over
    every active/non-padded pair.

    'psi' has shape (n_players, synergy_dimensions). When 'phi' is supplied
    with the same shape, each pair instead contributes
    sum_d phi_id * phi_jd * (psi_id + psi_jd).

    When rosters are mostly fixed, this can behave like a learned team intercept. Its
    sign should not be read as teamwork quality without held-out
    recombined-roster validation.
    """
    # Index psi by roster to get one profile per slot:
    # profiles has shape (n_observations, max_roster_size, synergy_dimensions).
    profiles = psi[roster]
    if phi is not None and phi.shape != psi.shape:
        raise ValueError("phi and psi must have the same shape")
    weights = phi[roster] if phi is not None else None
    result = profiles.new_zeros(len(roster))
    # Walk unordered pairs once. 'active' zeros out pairs touching padding.
    for left in range(roster.shape[1]):
        for right in range(left + 1, roster.shape[1]):
            active = roster_mask[:, left] & roster_mask[:, right]
            if weights is None:
                pair = profiles[:, left] * profiles[:, right]
            else:
                pair = weights[:, left] * weights[:, right] * (
                    profiles[:, left] + profiles[:, right]
                )
            result = result + pair.sum(-1) * active
    # Return shape: (n_observations,).
    return result


def bonus_aggregate_and_difficulty(
    data, theta, weights, beta, tau, bonus_difficulty="scalar", bonus_aggregation="lse"
):
    """Return the team aggregate and the difficulty subtracted from it.

    The base bonus-part logit is 'aggregate - difficulty'. 'weights' holds each
    part's 'alpha' or 'r' (see 'part_weight_site') with shape
    '(n_parts, n_dimensions)'. For each option:

    * LSE with scalar difficulty is Eq. 8: A_b(R) - beta_b.
    * LSE or max with multidim difficulty pools each skill axis first:
      sum_k r_bk * (ts_k(R) - beta_bk). Part responses identify only
      r_b dot beta_b, not each beta_bk.
    * Max with scalar difficulty is sum_k alpha_bk * max_m theta_mk - beta_b.
    * Noisy-OR is Eq. 9. Each member logit already subtracts beta_b, so the
      aggregate is the full team logit and the difficulty is zero.

    LSE is literal and unnormalized by roster size.
    """
    validate_bonus_settings(bonus_aggregation, bonus_difficulty)
    # part_weights has shape (n_observations, n_dimensions).
    # member_theta has shape (n_observations, max_roster_size, n_dimensions).
    part_weights = weights[data["part"]]
    member_theta = theta[data["roster"]]
    roster_mask = data["roster_mask"]

    if bonus_aggregation == "noisy-or":
        # Each member's own logit alpha_b^T theta_m - beta_b:
        # (n_observations, max_roster_size).
        member_logits = (
            (member_theta * part_weights.unsqueeze(1)).sum(-1)
            - beta[data["part"]].unsqueeze(1)
        )
        aggregate = noisy_or_logits(member_logits, roster_mask)
        return aggregate, torch.zeros_like(aggregate)

    if bonus_difficulty == "multidim":
        expected = (len(data["part_ids"]), theta.shape[1])
        if beta.shape != expected or weights.shape != expected:
            raise ValueError("Multidim bonus r and beta need one coordinate per skill dimension and part")
        difficulty = (part_weights * beta[data["part"]]).sum(-1)
    else:
        difficulty = beta[data["part"]]

    if bonus_aggregation == "max" or bonus_difficulty == "multidim":
        # Pool teammates on each skill axis, then weight the axes by the part.
        team_skills = pool_team_skills(member_theta, roster_mask, bonus_aggregation, tau)
        return (part_weights * team_skills).sum(-1), difficulty

    # Eq. 8 member ability alpha_b^T theta_m: (n_observations, max_roster_size).
    member_abilities = (member_theta * part_weights.unsqueeze(1)).sum(-1)
    return lse_aggregation(member_abilities, roster_mask, tau), difficulty


def alpha_distribution(alpha_prior, vector_zero, vector_one):
    """Return the bonus-part discrimination prior named by 'alpha_prior'.

    'normal' is N(0, I): signed loadings for a rotation-arbitrary Stage 1 basis.
    'gamma' is Gamma(2, 2): mean-1 nonnegative loadings, matching the positive
    relevance vector 'r' used by the multidim pyramidal stage, whose positivity
    already pins the basis.
    """
    if alpha_prior == "normal":
        return dist.Normal(vector_zero, vector_one).to_event(1)
    if alpha_prior == "gamma":
        return dist.Gamma(2.0 * vector_one, 2.0 * vector_one).to_event(1)
    raise ValueError(f"Unknown alpha prior: {alpha_prior}")


def apply_synergy(logits, synergy, synergy_link="additive"):
    """Combine the base bonus-part logit with roster synergy s(R).

    'additive' returns eta + s(R), as in Eq. 11. 'multiplicative' returns
    eta * (1 + s(R)), so s(R) rescales the whole base logit. Optional
    correctness calibration is applied afterwards.
    """
    if synergy_link == "additive":
        return logits + synergy
    if synergy_link == "multiplicative":
        return logits * (1 + synergy)
    raise ValueError(f"Unknown synergy link: {synergy_link}")


def compositional_model(
    data,
    theta,
    use_synergy=False,
    synergy_dimensions=1,
    calibrate_correctness=False,
    alpha_prior="normal",
    synergy_form="dot",
    synergy_link="additive",
    bonus_difficulty="scalar",
    bonus_aggregation="lse",
):
    """Define the team bonus-part correctness likelihood.

    'theta' comes from the tossup model and is treated as fixed input, so this
    stage learns only the bonus-part and synergy parameters:

    'alpha' is bonus-part discrimination ('r', positive relevance, for multidim difficulty)
    'beta' is bonus-part difficulty, scalar or one coordinate per skill dimension
    'tau' is the LSE aggregation temperature
    'psi' is the optional per-player synergy profile
    'phi' is a second per-player vector for synergy_form='phi-psi'
    """
    validate_bonus_settings(
        bonus_aggregation,
        bonus_difficulty,
        use_synergy=use_synergy,
        calibrate_correctness=calibrate_correctness,
        synergy_form=synergy_form,
        synergy_link=synergy_link,
        synergy_dimensions=synergy_dimensions,
        alpha_prior=alpha_prior,
    )
    n_parts = len(data["part_ids"])
    n_dimensions = theta.shape[1]
    zero = theta.new_tensor(0.0)
    one = theta.new_tensor(1.0)
    vector_zero = theta.new_zeros(n_dimensions)
    vector_one = theta.new_ones(n_dimensions)

    # Eq. 14 bonus-part priors:
    # alpha_b ~ N(0, I) by default; Gamma(2, 2) when the fixed theta basis is
    # compatible with positive relevance. beta_b ~ N(0, 1).
    # Multidim difficulty samples r_b from the Gamma prior and beta_b ~ N(0, I).
    # Dimensions: alpha or r: (n_parts, n_dimensions);
    # beta: (n_parts,) or (n_parts, n_dimensions).
    with pyro.plate("bonus_parts", n_parts):
        # Treat each part's whole weight vector as one latent event.
        weights = pyro.sample(
            part_weight_site(bonus_difficulty),
            alpha_distribution(alpha_prior, vector_zero, vector_one),
        )
        if bonus_difficulty == "multidim":
            beta = pyro.sample("beta", dist.Normal(vector_zero, vector_one).to_event(1))
        else:
            beta = pyro.sample("beta", dist.Normal(zero, one))

    # tau is a single shared scalar, so it is sampled outside the part plate.
    # Only LSE aggregation has a temperature.
    tau = pyro.sample("tau", dist.HalfCauchy(one)) if bonus_aggregation == "lse" else None

    # Eq. 11 logit without synergy: eta_rb = aggregate - difficulty.
    # Both terms have shape (n_observations,).
    aggregate, difficulty = bonus_aggregate_and_difficulty(
        data, theta, weights, beta, tau, bonus_difficulty, bonus_aggregation
    )
    logits = aggregate - difficulty

    if use_synergy:
        # Eq. 14 synergy prior: psi_i ~ N(0, 0.5 I).
        # Dimensions: psi: (n_players, synergy_dimensions).
        # These player-level latent vectors are unrelated to theta.
        with pyro.plate("synergy_players", theta.shape[0]):
            psi = pyro.sample(
                "psi",
                dist.Normal(
                    theta.new_zeros(synergy_dimensions),
                    theta.new_full((synergy_dimensions,), math.sqrt(0.5)),
                ).to_event(1),
            )
            phi = None
            if synergy_form == "phi-psi":
                phi = pyro.sample(
                    "phi",
                    dist.Normal(
                        theta.new_zeros(synergy_dimensions),
                        theta.new_ones(synergy_dimensions),
                    ).to_event(1),
                )
        synergy = synergy_contribution(
            psi, data["roster"], data["roster_mask"], phi=phi
        )
        logits = apply_synergy(logits, synergy, synergy_link)

    if calibrate_correctness:
        # Platt-scale the full part-correctness logit.
        scale = pyro.sample(
            "correctness_scale", dist.LogNormal(zero, theta.new_tensor(0.5))
        )
        bias = pyro.sample("correctness_bias", dist.Normal(zero, theta.new_tensor(3.0)))
        logits = scale * logits + bias

    # Eq. 11 is a built-in Bernoulli likelihood, so register y_rb directly as
    # the observed value at this sample site.
    with pyro.plate("bonus_observations", len(data["y"])):
        pyro.sample("obs", dist.Bernoulli(logits=logits), obs=data["y"])


def posterior_predictions(
    data,
    theta,
    posterior,
    use_synergy=False,
    calibrate_correctness=False,
    synergy_link="additive",
    bonus_difficulty="scalar",
    bonus_aggregation="lse",
):
    """Return fitted correctness probability, team aggregate, and synergy per row.

    Indexing each learned posterior parameter by the row's bonus part and roster
    recreates the row-level inputs used during fitting, so Eq. 8, Eq. 10, and
    Eq. 11 can be replayed at the posterior medians.
    """
    validate_bonus_settings(
        bonus_aggregation,
        bonus_difficulty,
        use_synergy=use_synergy,
        calibrate_correctness=calibrate_correctness,
    )
    # Posterior replay of the team aggregate and difficulty.
    aggregate, difficulty = bonus_aggregate_and_difficulty(
        data,
        theta,
        posterior[part_weight_site(bonus_difficulty)],
        posterior["beta"],
        posterior.get("tau"),
        bonus_difficulty,
        bonus_aggregation,
    )
    synergy = aggregate.new_zeros(len(aggregate))
    if use_synergy:
        # Replay Eq. 10 or the phi-psi variant, identified by its extra site.
        synergy = synergy_contribution(
            posterior["psi"], data["roster"], data["roster_mask"],
            phi=posterior.get("phi"),
        )
    # Posterior replay of Eq. 11.
    logits = apply_synergy(aggregate - difficulty, synergy, synergy_link)
    if calibrate_correctness:
        logits = posterior["correctness_scale"] * logits + posterior["correctness_bias"]
    # Each returned tensor has shape (n_observations,).
    return torch.sigmoid(logits), aggregate, synergy
