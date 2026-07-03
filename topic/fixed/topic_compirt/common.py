"""Small shared helpers for the fixed-topic command-line scripts."""

from __future__ import annotations

import pyro
from pyro.infer import SVI, Trace_ELBO
from pyro.infer.autoguide import AutoNormal
from pyro.optim import ClippedAdam

from topic.utils.outputs import DEFAULT_TOPIC_VECTORS, REPO_ROOT


def tensor_values(tensor):
    """Return a tensor as a NumPy array for CSV output."""
    return tensor.detach().cpu().numpy()


def add_numbered_tensor_columns(target: dict, prefix: str, tensor) -> None:
    """Add columns like 'theta_1' or 'topic_weight_3' to 'target'."""
    values = tensor_values(tensor)
    for dimension in range(values.shape[1]):
        target[f"{prefix}_{dimension + 1}"] = values[:, dimension]


def fit_svi(model, model_args: tuple, n_steps: int, lr: float, return_guide: bool = False):
    """Fit a Pyro model with the project's standard AutoNormal SVI loop.

    With 'return_guide' the fitted 'AutoNormal' guide is returned alongside
    the medians and losses so callers can save the full variational posterior
    (used by the held-out evaluation to build returning-player priors).
    """
    # AutoNormal mean-field guide optimized with clipped Adam against the ELBO.
    pyro.clear_param_store()
    guide = AutoNormal(model)
    svi = SVI(model, guide, ClippedAdam({"lr": lr}), loss=Trace_ELBO())
    losses = []
    for step in range(n_steps):
        loss = svi.step(*model_args)
        losses.append(float(loss))
        if step % 100 == 0:
            print(f"step {step:4d}  ELBO loss: {loss:,.1f}")
    # Return posterior medians (point estimates) plus the full loss trace.
    medians = guide.median(*model_args)
    if return_guide:
        return medians, guide, losses
    return medians, losses
