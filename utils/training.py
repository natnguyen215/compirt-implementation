"""Training-runtime helpers shared by every CompIRT training script.

These cover the two pieces of per-run setup that were previously copy-pasted
into every 'train_*.py': validating the requested device and running the
project's standard AutoNormal SVI loop. Model definitions and each script's
'run_experiment' orchestration still live in the individual training scripts.
"""

from __future__ import annotations

import pyro
import torch
from pyro.infer import SVI, Trace_ELBO
from pyro.infer.autoguide import AutoNormal
from pyro.optim import ClippedAdam


def require_device(device):
    """Fail fast when a CUDA run is requested but no GPU is available."""
    if device == "cuda" and not torch.cuda.is_available():
        raise RuntimeError("CUDA requested, but no CUDA device is available")


def fit_svi(model, model_args, n_steps, lr, return_guide=False):
    """Fit a Pyro model with the project's standard AutoNormal SVI loop.

    'model_args' is the positional tuple passed to both 'svi.step' and
    'guide.median'. Returns '(medians, losses)', or '(medians, guide, losses)'
    when 'return_guide' is set so callers can save the full variational
    posterior (used by the held-out evaluation to build returning-player priors).
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
