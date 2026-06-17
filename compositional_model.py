"""Combine fixed player skills into team-level bonus-part predictions.

This is the second stage of the CompIRT pipeline. The pyramidal tossup model
first estimates each player's skill vector 'theta'. This model keeps those
vectors fixed and learns how strongly each bonus part rewards those skills.

Each observation is one team attempting one bonus part. The model combines all
roster members' part abilities, optionally adds pairwise synergy, and predicts
whether the part was answered correctly.

Important Dimensions:

* 'n_observations' is the number of team-by-bonus-part rows. Each row is one
  team attempting one bonus part.
* 'n_players' and 'n_parts' count the unique players and bonus parts.
* 'n_dimensions' is the number of latent skill dimensions. It is shared with the
  tossup model because 'theta' is reused unchanged.
* 'max_roster_size' is the largest roster. Shorter rosters are padded, and the
  padded slots are tracked by a boolean mask.
* 'synergy_dimensions' is the size of each player's synergy profile.

Important Shapes:

* data is a Python dict of PyTorch tensors and ID lists of players and bonus parts.
* 'theta' is fixed input from the tossup model with shape
  '(n_players, n_dimensions)'.
* Before indexing by observation row, bonus-part parameters are stored by part:
    - 'alpha' has shape '(n_parts, n_dimensions)'
    - 'beta' has shape '(n_parts,)'.
* 'tau' is a single scalar, and 'psi' has shape '(n_players, synergy_dimensions)'.
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


def lse_aggregation(member_abilities, roster_mask, tau):
    """Return one aggregate team-knowledge value from member abilities.

    'member_abilities' and 'roster_mask' have shape '(n_observations, max_roster_size)'.
    'tau' is the aggregation temperature.
    """
    # Eq. 8: A_k(T) = tau * log sum_m exp(alpha_k^T theta_p_m / tau).
    # masked_fill sets padded slots to -inf so they drop out of logsumexp.
    scaled = (member_abilities / tau).masked_fill(~roster_mask, -torch.inf)
    # return shape is (n_observations,)
    return tau * torch.logsumexp(scaled, dim=1)


def synergy_contribution(psi, roster, roster_mask):
    """Return the summed pairwise synergy for every roster.

    'psi' is the per-player synergy profile. A pair's synergy is the dot product
    of their two profiles, and a roster's synergy is that dot product summed over
    every active/non-padded pair. 
    
    'psi' has shape (n_players, synergy_dimensions)

    When rosters are mostly fixed, can behave like a learned team intercept. Its
    sign should not be read as teamwork quality without held-out
    recombined-roster validation.
    """
    # Index psi by roster to get one profile per slot:
    # profiles has shape (n_observations, max_roster_size, synergy_dimensions).
    profiles = psi[roster]
    result = profiles.new_zeros(len(roster))
    # Eq. 10: synergy(R) = sum_{i < k in R} psi_i^T psi_k.
    # Walk the upper triangle of roster slot pairs and add each pair's dot
    # product. 'active' zeros out any pair that touches a padded slot.
    for left in range(roster.shape[1]):
        for right in range(left + 1, roster.shape[1]):
            active = roster_mask[:, left] & roster_mask[:, right]
            result = result + (profiles[:, left] * profiles[:, right]).sum(-1) * active
    # return shape is (n_observations,)
    return result


def compositional_model(data, theta, use_synergy=False, synergy_dimensions=1):
    """Define the team bonus-part correctness likelihood.

    'theta' comes from the tossup model and is treated as fixed input, so this
    stage learns only the bonus-part and synergy parameters:

    'alpha' is bonus-part discrimination
    'beta' is bonus-part difficulty
    'tau' is the aggregation temperature
    'psi' is the optional per-player synergy profile
    """
    n_parts = len(data["part_ids"])
    n_dimensions = theta.shape[1]
    zero = theta.new_tensor(0.0)
    one = theta.new_tensor(1.0)
    vector_zero = theta.new_zeros(n_dimensions)
    vector_one = theta.new_ones(n_dimensions)

    # Eq. 14 bonus-part priors:
    # alpha_b ~ N(0, I), beta_b ~ N(0, 1).
    # Dimensions: alpha: (n_parts, n_dimensions), beta: (n_parts,).
    with pyro.plate("bonus_parts", n_parts):
        alpha = pyro.sample("alpha", dist.Normal(vector_zero, vector_one).to_event(1))
        # .to_event forces Pyro to treat the whole discrimination vector as one bonus part's latent vector
        beta = pyro.sample("beta", dist.Normal(zero, one))
        
    # tau is a single shared scalar, so it is sampled outside the part plate.
    tau = pyro.sample("tau", dist.HalfCauchy(one))

    # Eq. 8 member ability: alpha_k^T theta_p_m.
    # part_alpha indexes one discrimination vector per observation row: (n_observations, n_dimensions).
    # member_theta indexes one skill vector per roster slot:
    # (n_observations, max_roster_size, n_dimensions).
    part_alpha = alpha[data["part"]]
    member_theta = theta[data["roster"]]
    # member_abilities has shape (n_observations, max_roster_size).
    member_abilities = (member_theta * part_alpha.unsqueeze(1)).sum(-1)
    # Collapse each roster's member abilities into A_k(T): (n_observations,).
    aggregate = lse_aggregation(member_abilities, data["roster_mask"], tau)
    # Eq. 11 logit without synergy: eta_rb = A_b(R_r) - beta_b.
    logits = aggregate - beta[data["part"]]

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
        # Eq. 10 adds the pairwise roster synergy term to Eq. 11's logit.
        logits = logits + synergy_contribution(psi, data["roster"], data["roster_mask"])

    # Eq. 11: y_rb ~ Bernoulli(sigmoid(eta_rb)).
    # Unlike the tossup model's competing risks, the bonus likelihood is a single
    # built-in Bernoulli, so it is observed directly with obs=data["y"] rather
    # than added by hand with pyro.factor.
    with pyro.plate("bonus_observations", len(data["y"])):
        pyro.sample("obs", dist.Bernoulli(logits=logits), obs=data["y"])


#-----------------------------------------------------------------------------------
# Predictions Code
#-----------------------------------------------------------------------------------

def posterior_predictions(data, theta, posterior, use_synergy=False):
    """Return fitted correctness probability, team aggregate, and synergy per row.

    Indexing each learned posterior parameter by the row's bonus part and roster
    recreates the row-level inputs used during fitting, so Eq. 8, Eq. 10, and
    Eq. 11 can be replayed at the posterior medians.
    """
    member_theta = theta[data["roster"]]
    alpha = posterior["alpha"][data["part"]]
    # Posterior replay of Eq. 8's member abilities and smooth maximum.
    member_abilities = (member_theta * alpha.unsqueeze(1)).sum(-1)
    aggregate = lse_aggregation(member_abilities, data["roster_mask"], posterior["tau"])
    synergy = aggregate.new_zeros(len(aggregate))
    if use_synergy:
        # Posterior replay of Eq. 10.
        synergy = synergy_contribution(
            posterior["psi"], data["roster"], data["roster_mask"]
        )
    # Posterior replay of Eq. 11.
    logits = aggregate + synergy - posterior["beta"][data["part"]]
    # Each returned tensor has shape (n_observations,).
    return torch.sigmoid(logits), aggregate, synergy
