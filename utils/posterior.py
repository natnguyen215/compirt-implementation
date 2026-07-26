"""Portable uncertainty artifacts for fitted Pyro ``AutoNormal`` guides.

Training scripts normally save posterior medians for fast evaluation.  This
module adds two complementary artifacts while the fitted guide is still alive:

* constrained marginal parameter quantiles for every latent site; and
* optional joint posterior draws, stored one memory-mappable ``.npy`` file per
  site with a shared leading draw index.

The draws contain parameters, not replayed row/token predictions.  Keeping
those concerns separate makes the standard output inexpensive while allowing
later prediction-uncertainty jobs to replay only the outputs they need.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path

import numpy as np
import torch


DEFAULT_POSTERIOR_DRAWS = 100
DEFAULT_QUANTILES = (0.025, 0.5, 0.975)


def add_posterior_output_args(parser: argparse.ArgumentParser):
    """Add consistent posterior-artifact controls to a training CLI."""
    parser.add_argument(
        "--posterior-draws",
        type=int,
        default=DEFAULT_POSTERIOR_DRAWS,
        help=(
            "joint AutoNormal parameter draws to save after fitting (default: "
            f"{DEFAULT_POSTERIOR_DRAWS}; use 0 to save quantiles only)"
        ),
    )
    return parser


def _safe_site_name(site):
    """Return a stable filename component for one Pyro latent-site name."""
    value = re.sub(r"[^A-Za-z0-9_.-]+", "_", str(site)).strip("._")
    return value or "site"


def _quantile_label(probability):
    """Return compact artifact labels such as ``p025`` and ``p975``."""
    basis_points = int(round(float(probability) * 1000))
    return f"p{basis_points:03d}"


def _tensor_cuda_devices(value):
    """Find CUDA device indexes nested inside the model keyword arguments."""
    devices = set()
    if torch.is_tensor(value):
        if value.is_cuda:
            devices.add(value.device.index or 0)
    elif isinstance(value, dict):
        for nested in value.values():
            devices.update(_tensor_cuda_devices(nested))
    elif isinstance(value, (tuple, list)):
        for nested in value:
            devices.update(_tensor_cuda_devices(nested))
    return devices


def _as_numpy(tensor):
    """Detach one guide value and return a CPU NumPy array."""
    if not torch.is_tensor(tensor):
        raise TypeError(f"Posterior guide values must be tensors, got {type(tensor)!r}")
    return tensor.detach().cpu().numpy()


def _write_quantile_csv(path, quantiles, probabilities):
    """Write one long, shape-agnostic table of constrained site quantiles."""
    labels = [_quantile_label(value) for value in probabilities]
    temporary = path.with_suffix(path.suffix + ".tmp")
    with temporary.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["site", "index", *labels])
        for site, values in quantiles.items():
            array = _as_numpy(values)
            if array.shape[0] != len(probabilities):
                raise ValueError(
                    f"Guide returned unexpected quantile shape for {site!r}: "
                    f"{array.shape}"
                )
            parameter_shape = array.shape[1:]
            indexes = np.ndindex(parameter_shape) if parameter_shape else [()]
            for index in indexes:
                readable_index = "|".join(map(str, index))
                writer.writerow(
                    [site, readable_index, *(float(array[(q, *index)]) for q in range(len(labels)))]
                )
    temporary.replace(path)


def _write_quantile_npz(path, quantiles, probabilities, safe_names):
    """Write shape-preserving quantile arrays for programmatic consumers."""
    arrays = {}
    for site, values in quantiles.items():
        array = _as_numpy(values)
        for index, probability in enumerate(probabilities):
            key = f"{safe_names[site]}__{_quantile_label(probability)}"
            arrays[key] = array[index]
    temporary = path.with_suffix(path.suffix + ".tmp")
    with temporary.open("wb") as handle:
        np.savez_compressed(handle, **arrays)
    temporary.replace(path)


def save_variational_posterior(
    output_dir,
    guide,
    model_kwargs,
    *,
    draws=DEFAULT_POSTERIOR_DRAWS,
    seed=42,
    probabilities=DEFAULT_QUANTILES,
):
    """Save constrained quantiles and optional joint draws for every guide site.

    Draw arrays use shape ``(draws, *site_shape)``.  Their leading indexes are
    aligned across files: row ``d`` in every site file belongs to the same
    complete posterior draw.  Files are memory mapped while being written so
    the implementation never holds all sites and draws in RAM simultaneously.
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    draws = int(draws)
    if draws < 0:
        raise ValueError("posterior draws must be non-negative")
    probabilities = tuple(float(value) for value in probabilities)
    if not probabilities or any(not 0 < value < 1 for value in probabilities):
        raise ValueError("posterior quantiles must lie strictly between zero and one")
    if tuple(sorted(probabilities)) != probabilities:
        raise ValueError("posterior quantiles must be sorted")

    with torch.no_grad():
        quantiles = guide.quantiles(list(probabilities), **model_kwargs)
    if not quantiles:
        raise ValueError("fitted guide returned no latent-site quantiles")

    safe_names = {}
    used_names = set()
    for site in quantiles:
        safe_name = _safe_site_name(site)
        if safe_name in used_names:
            raise ValueError(f"posterior site filename collision for {site!r}")
        safe_names[site] = safe_name
        used_names.add(safe_name)

    _write_quantile_csv(
        output_dir / "posterior_quantiles.csv",
        quantiles,
        probabilities,
    )
    _write_quantile_npz(
        output_dir / "posterior_quantiles.npz",
        quantiles,
        probabilities,
        safe_names,
    )

    sites = {}
    for site, values in quantiles.items():
        array = _as_numpy(values)
        parameter_shape = array.shape[1:]
        sites[site] = {
            "shape": list(parameter_shape),
            "dtype": str(array.dtype),
            "quantile_prefix": safe_names[site],
            "draw_file": (
                f"posterior_draws/{safe_names[site]}.npy" if draws else None
            ),
        }

    if draws:
        draw_dir = output_dir / "posterior_draws"
        draw_dir.mkdir(parents=True, exist_ok=True)
        maps = {
            site: np.lib.format.open_memmap(
                draw_dir / f"{safe_names[site]}.npy",
                mode="w+",
                dtype=np.dtype(metadata["dtype"]),
                shape=(draws, *metadata["shape"]),
            )
            for site, metadata in sites.items()
        }
        devices = sorted(_tensor_cuda_devices(model_kwargs))
        try:
            with torch.no_grad(), torch.random.fork_rng(devices=devices):
                torch.manual_seed(int(seed))
                if devices:
                    torch.cuda.manual_seed_all(int(seed))
                for draw_index in range(draws):
                    sample = guide(**model_kwargs)
                    if set(sample) != set(maps):
                        missing = sorted(set(maps) - set(sample))
                        extra = sorted(set(sample) - set(maps))
                        raise ValueError(
                            "guide draw sites differ from quantile sites: "
                            f"missing={missing}, extra={extra}"
                        )
                    for site, target in maps.items():
                        values = _as_numpy(sample[site])
                        if values.shape != target.shape[1:]:
                            raise ValueError(
                                f"guide draw shape changed for {site!r}: "
                                f"expected {target.shape[1:]}, got {values.shape}"
                            )
                        target[draw_index] = values
        finally:
            for target in maps.values():
                target.flush()
            maps.clear()

    estimated_draw_bytes = sum(
        draws
        * int(np.prod(metadata["shape"], dtype=np.int64))
        * np.dtype(metadata["dtype"]).itemsize
        for metadata in sites.values()
    )
    manifest = {
        "approximation": "Pyro AutoNormal variational posterior",
        "mean_field": True,
        "quantile_probabilities": list(probabilities),
        "draws": draws,
        "draw_seed": int(seed),
        "estimated_draw_bytes": estimated_draw_bytes,
        "draw_alignment": (
            "The same leading draw index across every site file is one joint "
            "variational-posterior draw."
        ),
        "interpretation": (
            "Intervals are approximate SVI credible intervals conditional on "
            "this model and fitted dataset; they are not bootstrap intervals."
        ),
        "sites": sites,
    }
    temporary = output_dir / "posterior_manifest.json.tmp"
    temporary.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    temporary.replace(output_dir / "posterior_manifest.json")
    return manifest

