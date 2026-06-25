"""Small shared helpers for topic-modeling command-line scripts."""

from __future__ import annotations

import sys

import pyro
from pyro.infer import SVI, Trace_ELBO
from pyro.infer.autoguide import AutoNormal
from pyro.optim import ClippedAdam

from topic_utils.outputs import DEFAULT_TOPIC_VECTORS, REPO_ROOT, TOPIC_ROOT


def add_repo_root_to_path() -> None:
    """Allow topic-side scripts to import root CompIRT modules."""
    root = str(REPO_ROOT)
    if root not in sys.path:
        sys.path.insert(0, root)


def tensor_values(tensor):
    """Return a tensor as a NumPy array for CSV output."""
    return tensor.detach().cpu().numpy()


def add_numbered_tensor_columns(target: dict, prefix: str, tensor) -> None:
    """Add columns like 'theta_1' or 'topic_weight_3' to 'target'."""
    values = tensor_values(tensor)
    for dimension in range(values.shape[1]):
        target[f"{prefix}_{dimension + 1}"] = values[:, dimension]


def fit_svi(model, model_args: tuple, n_steps: int, lr: float):
    """Fit a Pyro model with the project's standard AutoNormal SVI loop."""
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
    return guide.median(*model_args), losses
