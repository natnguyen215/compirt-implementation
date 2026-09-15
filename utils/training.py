"""Training-runtime helpers shared by every CompIRT training script.

These helpers validate the requested device and run the project's standard
AutoNormal SVI loop. Each training script owns its model definition and
'run_experiment' orchestration.
"""

from __future__ import annotations

import os

import numpy as np
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

    'COMPIRT_SURVIVAL_CHUNK' sets the number of rows per chunk; unset or
    non-positive values select full-batch evaluation. Each family's
    'log_survival' evaluates its '(rows, positions, dims)' grid under gradient
    checkpointing, preserving the likelihood while limiting grid memory to
    one chunk. This supports higher-dimensional runs on memory-limited GPUs.
    """
    raw = os.environ.get("COMPIRT_SURVIVAL_CHUNK")
    if not raw:
        return None
    value = int(raw)
    return value if value > 0 else None


def convergence_summary(losses):
    """Summarize an SVI loss trace for a trainer's 'summary.json'.

    'last_100_loss_slope' is the least-squares slope over the final 100 steps;
    a value near zero is the usual signal that the ELBO has flattened.
    """
    tail = np.asarray(losses[-min(100, len(losses)) :], dtype=float)
    slope = (
        float(np.polyfit(np.arange(len(tail)), tail, 1)[0])
        if len(tail) > 1
        else float("nan")
    )
    return {
        "initial_loss": losses[0],
        "final_loss": losses[-1],
        "best_loss": min(losses),
        "last_100_loss_slope": slope,
        "finite_losses": bool(np.isfinite(losses).all()),
    }


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


def _set_autonormal_site_trainability(frozen_sites):
    """Freeze selected AutoNormal sites, including their optimizer momentum.

    Pyro zeroes gradients after each SVI step. Setting a frozen parameter's
    gradient to ``None`` also stops Adam from applying accumulated momentum.
    """
    frozen_sites = frozenset(frozen_sites)
    for parameter_name, parameter in pyro.get_param_store().named_parameters():
        site_name = parameter_name.rsplit(".", 1)[-1]
        trainable = site_name not in frozen_sites
        parameter.requires_grad_(trainable)
        if not trainable:
            parameter.grad = None


def fit_svi_alternating(
    model,
    *,
    model_kwargs,
    n_steps,
    lr,
    frozen_site_cycle,
    posterior_output_dir=None,
    posterior_draws=0,
    posterior_seed=42,
):
    """Fit one AutoNormal guide while cycling frozen latent-site blocks.

    Parameters outside the named frozen sites remain trainable on every step.
    One guide and optimizer are retained for the entire run, so trainable
    parameters keep continuous Adam state across the alternating schedule.
    """
    cycle = tuple(frozenset(sites) for sites in frozen_site_cycle)
    if not cycle or any(not sites for sites in cycle):
        raise ValueError("frozen_site_cycle must contain non-empty site sets")

    pyro.clear_param_store()
    guide = AutoNormal(model)
    # AutoNormal creates its location and scale parameters lazily. Initialize
    # them once so trainability can be set before the first SVI step.
    guide(**model_kwargs)
    known_sites = {
        name.rsplit(".", 1)[-1]
        for name, _parameter in pyro.get_param_store().named_parameters()
    }
    unknown_sites = set().union(*cycle) - known_sites
    if unknown_sites:
        names = ", ".join(sorted(unknown_sites))
        raise ValueError(f"cannot freeze unknown latent sites: {names}")

    svi = SVI(
        model,
        guide,
        ClippedAdam({"lr": lr}),
        loss=Trace_ELBO(),
    )
    losses = []
    try:
        for step in range(n_steps):
            frozen_sites = cycle[step % len(cycle)]
            _set_autonormal_site_trainability(frozen_sites)
            loss = float(svi.step(**model_kwargs))
            losses.append(loss)
            if step % 100 == 0:
                frozen_names = ", ".join(sorted(frozen_sites))
                print(
                    f"step {step:4d}  ELBO loss: {loss:,.1f}  "
                    f"frozen: {frozen_names}"
                )
    finally:
        # Leave the returned guide in the standard fully trainable state for
        # posterior summaries and any downstream caller reuse.
        _set_autonormal_site_trainability(())

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
