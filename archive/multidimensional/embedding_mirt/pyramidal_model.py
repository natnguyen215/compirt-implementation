"""Embedding-based multidimensional pyramidal tossup model.

Each frozen, centered question embedding is projected into a relevance vector:

    r_j = softmax(W_2 gelu(W_1 @ centered(e_j) + b_1) + b_2)

'e_j' is the Qwen3-Embedding-8B representation produced by
'embed_questions.py'. The FFN is point-estimated jointly with the player and
tossup parameters. Softmax makes each 'r_j' sum to 1, so increasing
'--dimensions' redistributes a fixed relevance budget across more coordinates.
"""

from __future__ import annotations

import math

import torch
import torch.nn.functional as F

from compirt_race import winner_log_prob, survival_stop
import pyro
import pyro.distributions as dist

from multidimensional.multidim_mirt.pyramidal_model import (
    correctness_logit,
    expected_first_buzz_positions,
    hazard_logit,
    log_survival,
    posterior_row_predictions,
    row_parameters,
    sample_correctness_calibration,
)

__all__ = [
    "DEFAULT_PROJECTION_HIDDEN_DIM",
    "correctness_logit",
    "fitted_projection",
    "hazard_logit",
    "log_survival",
    "row_parameters",
    "sample_correctness_calibration",
    "project_relevance",
    "sample_parameters",
    "competing_risks_model",
    "posterior_row_predictions",
    "expected_first_buzz_positions",
]

DEFAULT_PROJECTION_HIDDEN_DIM = 128


def _xavier_normal(reference: torch.Tensor, shape: tuple[int, int]) -> torch.Tensor:
    """Return a Xavier-style normal init with the same device/dtype as 'reference'."""
    fan_in, fan_out = shape
    std = math.sqrt(2.0 / float(fan_in + fan_out))
    return reference.new_empty(shape).normal_(0.0, std)


def _ffn_logits(embedding, projection):
    """Return pre-softmax relevance logits from the two-layer FFN projection.

    Implements 'W_2 . gelu(W_1 . e_j + b_1) + b_2'; 'project_relevance' applies
    the softmax that turns these into the relevance vector 'r_j'.
    """
    hidden = F.gelu(embedding @ projection["input_weight"] + projection["hidden_bias"])
    return hidden @ projection["output_weight"] + projection["output_bias"]


def projection_logits(embedding, projection, bias=None):
    """Return relevance logits from an FFN projection or linear weight and bias."""
    if isinstance(projection, dict):
        kind = projection.get("kind", "linear")
        if kind == "ffn":
            return _ffn_logits(embedding, projection)
        if kind == "linear":
            return embedding @ projection["weight"] + projection["bias"]
        raise ValueError(f"Unknown relevance projection kind: {kind}")
    if bias is None:
        raise TypeError("Linear project_relevance calls must pass both weight and bias")
    return embedding @ projection + bias


def project_relevance(embedding, projection, bias=None):
    """Return a softmax relevance distribution from an embedding projection.

    Supports an FFN projection dictionary and the three-argument linear
    'project_relevance(embedding, weight, bias)' form.
    """
    return F.softmax(projection_logits(embedding, projection, bias), dim=-1)


def fitted_projection() -> dict[str, torch.Tensor | str]:
    """Return the fitted relevance projection from Pyro's param store."""
    store = pyro.get_param_store()
    if "r_projection_input_weight" in store:
        return {
            "kind": "ffn",
            "input_weight": pyro.param("r_projection_input_weight").detach(),
            "hidden_bias": pyro.param("r_projection_hidden_bias").detach(),
            "output_weight": pyro.param("r_projection_output_weight").detach(),
            "output_bias": pyro.param("r_projection_output_bias").detach(),
        }
    return {
        "kind": "linear",
        "weight": pyro.param("r_projection_weight").detach(),
        "bias": pyro.param("r_projection_bias").detach(),
    }


def sample_parameters(data, n_dimensions):
    """Sample player and difficulty parameters; compute 'r' from embeddings.

    Player priors follow Eq. 14, and each tossup receives per-dimension 'beta',
    'gamma', and 'mu'. The relevance vector 'r' is a deterministic function of
    the fixed 'data["embedding"]' and the point-estimated FFN projection.
    """
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

    with pyro.plate("tossups", n_tossups):
        beta = pyro.sample("beta", dist.Normal(vector_zero, vector_one).to_event(1))
        gamma = pyro.sample("gamma", dist.HalfCauchy(5.0 * vector_one).to_event(1))
        mu = pyro.sample(
            "mu",
            dist.Beta(
                data["y"].new_full((n_dimensions,), 2.0),
                data["y"].new_full((n_dimensions,), 2.0),
            ).to_event(1),
        )

    # Point-estimate r_j = softmax(FFN(e_j)) from the frozen embedding.
    embedding = data["embedding"]
    embed_dim = embedding.shape[1]
    hidden_dim = int(data.get("projection_hidden_dim", DEFAULT_PROJECTION_HIDDEN_DIM))
    if hidden_dim < 1:
        raise ValueError("projection_hidden_dim must be at least 1")
    input_weight = pyro.param(
        "r_projection_input_weight",
        lambda: _xavier_normal(embedding, (embed_dim, hidden_dim)),
    )
    hidden_bias = pyro.param(
        "r_projection_hidden_bias",
        lambda: embedding.new_zeros(hidden_dim),
    )
    output_weight = pyro.param(
        "r_projection_output_weight",
        lambda: _xavier_normal(embedding, (hidden_dim, n_dimensions)),
    )
    output_bias = pyro.param(
        "r_projection_output_bias",
        lambda: embedding.new_zeros(n_dimensions),
    )
    r = project_relevance(
        embedding,
        {
            "kind": "ffn",
            "input_weight": input_weight,
            "hidden_bias": hidden_bias,
            "output_weight": output_weight,
            "output_bias": output_bias,
        },
    )
    return theta, c, r, beta, gamma, mu


def competing_risks_model(data, n_dimensions=5, calibrate_correctness=False):
    """Define the embedding-relevance competing-risks likelihood.

    Every rostered player contributes survival before the stopping position. The
    first buzzer also contributes the hazard at 't_star' and observed
    correctness. 'pyro.factor' attaches the hand-summed joint log-likelihood.
    """
    theta, c, r, beta, gamma, mu = sample_parameters(data, n_dimensions)
    row_theta, row_c, row_r, row_beta, row_gamma, row_mu = row_parameters(
        data, theta, c, r, beta, gamma, mu
    )

    survival = log_survival(
        row_theta, row_r, row_beta, row_gamma, row_mu, row_c,
        survival_stop(data), data["T_j"],
    )
    buzz = data["is_buzz"]
    stop_hazard_logits = hazard_logit(
        row_theta, row_r, row_beta, row_gamma, row_mu,
        row_c, data["t_star"], data["T_j"],
    )
    correctness = correctness_logit(
        row_theta[buzz], row_r[buzz], row_beta[buzz], row_gamma[buzz], row_mu[buzz],
        data["t_star"][buzz], data["T_j"][buzz],
    )
    if calibrate_correctness:
        scale, bias = sample_correctness_calibration(data)
        correctness = scale * correctness + bias

    log_likelihood = (
        survival.sum()
        + winner_log_prob(data, stop_hazard_logits).sum()
        + dist.Bernoulli(logits=correctness).log_prob(data["y"][buzz]).sum()
    )
    pyro.factor("embedding_competing_risks_likelihood", log_likelihood)
