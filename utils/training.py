"""Training-runtime helpers shared by every CompIRT training script.

These helpers validate the requested device and run the project's standard
AutoNormal SVI loop. Each training script owns its model definition and
'run_experiment' orchestration.
"""

from __future__ import annotations

import os

import pyro
import torch
from pyro.infer import SVI, Trace_ELBO
from pyro.infer.autoguide import AutoNormal
from pyro.optim import ClippedAdam

from utils.posterior import save_variational_posterior


def require_device(device):
    """Fail fast when a CUDA run is requested but no GPU is available."""
    if device == "cuda" and not torch.cuda.is_available():
        raise RuntimeError("CUDA requested, but no CUDA device is available")


def survival_chunk_size():
    """Row-chunk size for the per-dimension 'log_survival' hazard grid.

    Read from the 'COMPIRT_SURVIVAL_CHUNK' env var; unset (or non-positive)
    means full-batch (no chunking), so default runs are byte-identical. When
    set, each family's 'log_survival' evaluates its '(rows, positions, dims)'
    grid in row chunks under gradient checkpointing: the summed likelihood is
    unchanged, but peak memory is capped at one chunk's grid instead of the
    whole batch. This is the knob that lets high-dimension ablations
    (m >= 16) fit on the GPU.
    """
    raw = os.environ.get("COMPIRT_SURVIVAL_CHUNK")
    if not raw:
        return None
    value = int(raw)
    return value if value > 0 else None


def fit_svi(
    model,
    *,
    model_kwargs,
    n_steps,
    lr,
    posterior_output_dir=None,
    posterior_draws=0,
    posterior_seed=42,
):
    """Fit a Pyro model and return its medians, guide, and loss trace.

    When ``posterior_output_dir`` is provided, save constrained quantiles and
    optional aligned parameter draws before the in-memory guide is discarded.
    Existing library/test callers omit it and retain the former behavior.
    """
    # AutoNormal mean-field guide optimized with clipped Adam against the ELBO.
    pyro.clear_param_store()
    guide = AutoNormal(model)
    svi = SVI(model, guide, ClippedAdam({"lr": lr}), loss=Trace_ELBO())
    losses = []
    for step in range(n_steps):
        loss = svi.step(**model_kwargs)
        losses.append(float(loss))
        if step % 100 == 0:
            print(f"step {step:4d}  ELBO loss: {loss:,.1f}")
    # Return posterior medians (point estimates) plus the full loss trace.
    medians = guide.median(**model_kwargs)
    if posterior_output_dir is not None:
        save_variational_posterior(
            posterior_output_dir,
            guide,
            model_kwargs,
            draws=posterior_draws,
            seed=posterior_seed,
        )
    return medians, guide, losses
