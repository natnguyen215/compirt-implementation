"""Embedding-based multidimensional pyramidal tossup model.

This is a sibling of 'multidimensional/multidim_mirt/pyramidal_model.py' that
replaces its freely learned, positive tossup discrimination 'alpha ~ Gamma(2,
2)' with a content-aware relevance vector computed from a frozen text
embedding. CAIMIRA (docs/2410.06524v1.pdf, Eq. 5/7) uses a linear map; this
variant uses a small feed-forward projection:

    r_j = softmax(W_2 gelu(W_1 @ centered(e_j) + b_1) + b_2)

'e_j' is a frozen Qwen3-Embedding-8B vector of the tossup's question text
(precomputed by 'embed_questions.py'); the FFN weights are the only new latent
parameters, point-estimated jointly with 'theta'/'beta'/'gamma'/'mu' via the same
AutoNormal SVI loop the rest of CompIRT uses (mirrors how
'topic/learned/joint_pyramidal.py' point-estimates its topic-word matrix).

Only 'sample_parameters' and 'competing_risks_model' differ from
'multidimensional.multidim_mirt.pyramidal_model': everything else -- 'difficulty_curve',
'correctness_logit', 'hazard_logit', 'log_survival', 'row_parameters',
'sample_correctness_calibration', 'posterior_row_predictions', and
'expected_first_buzz_positions' -- is imported unchanged, because they already
accept an 'alpha'-shaped argument positionally, and 'r' fills that slot
exactly like 'alpha' would. The two functions that read the *fitted posterior
dict by key* ('posterior_row_predictions', 'expected_first_buzz_positions')
are wrapped with a one-line 'alpha' alias so multidim_mirt's unmodified
implementation can read this package's 'posterior["r"]'.

Note on model behavior: unlike 'alpha ~ Gamma(2, 2)' (unbounded above, mean 1
per dimension regardless of 'n_dimensions'), 'r_j' is a softmax and always sums
to 1 across dimensions. Raising '--dimensions' here spreads a fixed relevance
budget thinner (mean r_jk ~ 1/n_dimensions) rather than adding independent
discriminative capacity, so dimension sweeps are not directly comparable
between the two packages -- this is CAIMIRA's design, not a bug.
"""

from __future__ import annotations

import math

import torch
import torch.nn.functional as F

import pyro
import pyro.distributions as dist

from multidimensional.multidim_mirt.pyramidal_model import (
    correctness_logit,
    hazard_logit,
    log_survival,
    row_parameters,
    sample_correctness_calibration,
)
from multidimensional.multidim_mirt.pyramidal_model import (
    expected_first_buzz_positions as _multidim_expected_first_buzz_positions,
)
from multidimensional.multidim_mirt.pyramidal_model import (
    posterior_row_predictions as _multidim_posterior_row_predictions,
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
    hidden = F.gelu(embedding @ projection["input_weight"] + projection["hidden_bias"])
    return hidden @ projection["output_weight"] + projection["output_bias"]


def projection_logits(embedding, projection, bias=None):
    """Return relevance logits from either a saved FFN projection or old linear args."""
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

    New embedding runs use an FFN projection,
    'softmax(W_2 gelu(W_1 @ e_j + b_1) + b_2)'. The old three-argument linear
    call, 'project_relevance(embedding, weight, bias)', is still accepted so
    existing tests and saved linear projections remain readable.
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

    Player and difficulty priors are identical to
    'multidimensional.multidim_mirt.pyramidal_model.sample_parameters'. There is no sampled
    'alpha' -- 'r' is a deterministic function of the fixed 'data["embedding"]'
    and the point-estimated FFN projection.
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

    # r_j = softmax(FFN(e_j)): point-estimated projection of the frozen
    # embedding, not a sampled site.
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

    Structurally identical to 'multidimensional.multidim_mirt.pyramidal_model.competing_risks_model':
    every rostered player contributes survival before the stopping position, the
    actual first buzzer additionally contributes a hazard-at-'t_star' factor and
    an observed correctness factor, and the joint log-likelihood is hand-summed
    and attached with 'pyro.factor'.
    """
    theta, c, r, beta, gamma, mu = sample_parameters(data, n_dimensions)
    row_theta, row_c, row_r, row_beta, row_gamma, row_mu = row_parameters(
        data, theta, c, r, beta, gamma, mu
    )

    survival = log_survival(
        row_theta, row_r, row_beta, row_gamma, row_mu, row_c,
        data["t_star"], data["T_j"],
    )
    buzz = data["is_buzz"]
    buzz_logits = hazard_logit(
        row_theta[buzz], row_r[buzz], row_beta[buzz], row_gamma[buzz], row_mu[buzz],
        row_c[buzz], data["t_star"][buzz], data["T_j"][buzz],
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
        + F.logsigmoid(buzz_logits).sum()
        + dist.Bernoulli(logits=correctness).log_prob(data["y"][buzz]).sum()
    )
    pyro.factor("embedding_competing_risks_likelihood", log_likelihood)


def _alias_r_as_alpha(posterior: dict) -> dict:
    """Return a shallow copy of 'posterior' with 'r' also keyed as 'alpha'.

    'multidimensional.multidim_mirt.pyramidal_model.posterior_row_predictions' and
    'expected_first_buzz_positions' are otherwise byte-identical to what this
    package would need, but they read the discrimination vector out of the
    posterior dict by the key 'alpha'. Aliasing avoids a ~90-line duplicate.
    """
    return {**posterior, "alpha": posterior["r"]}


def posterior_row_predictions(data, posterior, calibrate_correctness=False):
    """Return fitted correctness, hazard, and survival for each row."""
    return _multidim_posterior_row_predictions(
        data, _alias_r_as_alpha(posterior), calibrate_correctness
    )


def expected_first_buzz_positions(data, posterior):
    """Compute the expected first-buzz relative position for each event."""
    return _multidim_expected_first_buzz_positions(data, _alias_r_as_alpha(posterior))
