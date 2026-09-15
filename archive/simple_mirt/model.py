"""
Compensatory multidimensional IRT model for players and tossup questions.

The model says:
    P(player i answers question j correctly) = sigmoid(alpha_j^T theta_i - d_j)

Where:
    theta_i  = player i's skill vector
    alpha_j  = question j's discrimination vector
    d_j      = question j's scalar difficulty intercept
"""

import pyro
import pyro.distributions as dist


def model(responses, mask, n_dimensions=2):
    """
    Args:
        responses : (n_players, n_questions) float tensor, values 0.0 or 1.0
        mask      : (n_players, n_questions) bool tensor, True where the cell is observed
        n_dimensions: number of latent skill dimensions
    """
    n_players, n_questions = responses.shape
    zero = responses.new_tensor(0.0)
    one = responses.new_tensor(1.0)
    vector_zero = responses.new_zeros(n_dimensions)
    vector_one = responses.new_ones(n_dimensions)

    # Each player has one latent skill vector: (n_players, n_dimensions).
    with pyro.plate("players", n_players):
        theta = pyro.sample(
            "theta", dist.Normal(vector_zero, vector_one).to_event(1)
        )

    # Questions have discrimination vectors (n_questions, n_dimensions) and
    # scalar difficulties (n_questions,).
    with pyro.plate("questions", n_questions):
        alpha = pyro.sample(
            "alpha", dist.Normal(vector_zero, vector_one).to_event(1)
        )
        d = pyro.sample("d", dist.Normal(zero, one))

    # Matrix multiplication computes alpha_j^T theta_i for every player-question pair.
    logit = theta @ alpha.transpose(0, 1) - d.unsqueeze(0)

    # Only observe cells where the player was actually in a game with that tossup.
    # Flatten to a 1-D vector of observed (player, question) pairs.
    obs_logit = logit[mask]
    obs_resp = responses[mask]

    with pyro.plate("obs_plate", obs_resp.numel()):
        pyro.sample("obs", dist.Bernoulli(logits=obs_logit), obs=obs_resp)
