"""Bounded synthetic parameter-recovery study for multidimensional CompIRT.

The diagnostic generates one sigmoid dataset, fits it with AutoNormal SVI,
aligns the two latent dimensions by permutation, and reports errors and
approximate guide-interval behavior against the known truth. The report uses
descriptive measurements without hand-chosen pass/fail thresholds.
"""

from __future__ import annotations

import itertools
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pyro
import torch

from compirt_data import tossup_tensors
from multidimensional.multidim_mirt.pyramidal_model import (
    competing_risks_model,
    correctness_logit,
    hazard_logit,
)
from utils.training import fit_svi


DIMENSION_PARAMETERS = {"theta", "r", "beta", "gamma", "mu"}


def generate_recovery_data(
    players=12, tossups=16, events=160, dimensions=2, seed=42
):
    """Generate first-buzz/censoring observations and their known parameters."""
    if dimensions != 2:
        raise ValueError("The lightweight recovery check is fixed to two dimensions")
    pyro.set_rng_seed(seed)
    rng = np.random.default_rng(seed)
    truth = {
        "theta": torch.tensor(
            rng.normal(0, 0.8, (players, dimensions)), dtype=torch.float32
        ),
        "c": torch.tensor(rng.normal(2.2, 0.35, players), dtype=torch.float32),
        "r": torch.tensor(
            rng.gamma(2, 0.5, (tossups, dimensions)), dtype=torch.float32
        ),
        "beta": torch.tensor(
            rng.normal(0.8, 0.35, (tossups, dimensions)), dtype=torch.float32
        ),
        "gamma": torch.tensor(
            rng.lognormal(2.0, 0.35, (tossups, dimensions)), dtype=torch.float32
        ),
        "mu": torch.tensor(
            rng.beta(3, 3, (tossups, dimensions)), dtype=torch.float32
        ),
    }
    rows = []
    for event_index in range(events):
        # Draw a roster and a question length, then simulate one competing-risks
        # first buzz from the known truth (the same generative process the model
        # fits, so a good fit should recover 'truth').
        tossup_index = event_index % tossups
        roster = rng.choice(players, size=min(6, players), replace=False)
        total_tokens = int(rng.integers(55, 101))
        positions = torch.arange(1, total_tokens + 1, dtype=torch.float32)
        time = positions.unsqueeze(0).expand(len(roster), -1)
        total = torch.full_like(time, float(total_tokens))
        roster_tensor = torch.as_tensor(roster)
        # Eq. 5 hazard for every (roster player, token) pair.
        hazard = torch.sigmoid(
            hazard_logit(
                truth["theta"][roster_tensor].unsqueeze(1),
                truth["r"][tossup_index],
                truth["beta"][tossup_index],
                truth["gamma"][tossup_index],
                truth["mu"][tossup_index],
                truth["c"][roster_tensor].unsqueeze(1),
                time,
                total,
                "sigmoid",
            )
        )
        # Team first-buzz mass per token, then the dead-tossup mass as the
        # trailing category (nobody buzzes before the question ends).
        team_hazard = 1 - torch.prod(1 - hazard, dim=0)
        survival = torch.cat([torch.ones(1), torch.cumprod(1 - team_hazard[:-1], 0)])
        mass = survival * team_hazard
        distribution = torch.cat([mass, torch.prod(1 - team_hazard).reshape(1)])
        token = int(torch.multinomial(distribution / distribution.sum(), 1))
        buzzer_slot = None
        outcome = np.nan
        if token < total_tokens:
            # Attribute the buzz to a player by their probability of being the
            # sole buzzer at this token, then draw Eq. 4 correctness.
            token_hazard = hazard[:, token]
            no_buzz = torch.prod(1 - token_hazard)
            weights = token_hazard * no_buzz / (1 - token_hazard).clamp_min(1e-6)
            probabilities = weights / weights.sum()
            buzzer_slot = int(torch.multinomial(probabilities, 1))
            logit = correctness_logit(
                truth["theta"][roster[buzzer_slot]],
                truth["r"][tossup_index],
                truth["beta"][tossup_index],
                truth["gamma"][tossup_index],
                truth["mu"][tossup_index],
                positions[token],
                positions.new_tensor(float(total_tokens)),
                "sigmoid",
            )
            outcome = float(torch.bernoulli(torch.sigmoid(logit)))
        # Emit one row per roster member: the buzzer is BUZZ, a dead tossup makes
        # everyone NO-BUZZ, otherwise the non-buzzers are CENSORED at the buzz.
        stop = total_tokens if buzzer_slot is None else token + 1
        for slot, player_index in enumerate(roster):
            if slot == buzzer_slot:
                observation_type = "BUZZ"
            elif buzzer_slot is None:
                observation_type = "NO-BUZZ"
            else:
                observation_type = "CENSORED"
            rows.append(
                {
                    "event_id": f"e{event_index}",
                    "game_id": f"g{event_index // 20}",
                    "team_id": f"team-{slot % 2}",
                    "player_id": f"p{player_index:02d}",
                    "tossup_id": f"q{tossup_index:02d}",
                    "raw_t_star": stop,
                    "t_star": stop,
                    "T_j": total_tokens,
                    "relative_position": stop / total_tokens,
                    "y": outcome if slot == buzzer_slot else np.nan,
                    "z": observation_type,
                    "tournament_id": "synthetic",
                    "tier": "synthetic",
                    "category": "Synthetic",
                    "roster_size": len(roster),
                }
            )
    return pd.DataFrame(rows), truth


def _best_dimension_permutation(estimate, truth):
    """Resolve the label-switching ambiguity for the small two-D experiment."""
    return min(
        itertools.permutations(range(truth.shape[1])),
        key=lambda permutation: np.mean(
            (estimate[:, permutation] - truth.detach().cpu().numpy()) ** 2
        ),
    )


def run_parameter_recovery(
    output_dir: Path,
    steps=800,
    seed=42,
    players=12,
    tossups=16,
    events=160,
):
    """Generate, fit, and save one bounded recovery experiment."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    observations, truth = generate_recovery_data(players, tossups, events, 2, seed)
    data = tossup_tensors(observations)
    model_kwargs = {
        "data": data,
        "n_dimensions": 2,
        "calibrate_correctness": False,
        "link": "sigmoid",
    }
    posterior, guide, _ = fit_svi(
        competing_risks_model,
        model_kwargs=model_kwargs,
        n_steps=steps,
        lr=0.02,
    )
    quantiles = guide.quantiles([0.025, 0.975], **model_kwargs)
    permutation = _best_dimension_permutation(
        posterior["theta"].detach().cpu().numpy(), truth["theta"]
    )
    rows = []
    scatter = []
    for name, true_tensor in truth.items():
        estimate = posterior[name].detach().cpu().numpy()
        lower = quantiles[name][0].detach().cpu().numpy()
        upper = quantiles[name][1].detach().cpu().numpy()
        true_values = true_tensor.detach().cpu().numpy()
        if name in DIMENSION_PARAMETERS:
            estimate = estimate[:, permutation]
            lower = lower[:, permutation]
            upper = upper[:, permutation]
        true_flat = true_values.reshape(-1)
        estimate_flat = estimate.reshape(-1)
        rows.append(
            {
                "parameter_class": name,
                "parameters": len(true_flat),
                "bias": float(np.mean(estimate_flat - true_flat)),
                "rmse": float(np.sqrt(np.mean((estimate_flat - true_flat) ** 2))),
                "coverage_95": float(
                    np.mean((true_values >= lower) & (true_values <= upper))
                ),
                "mean_interval_width_95": float(np.mean(upper - lower)),
            }
        )
        scatter.extend(
            {"parameter_class": name, "true": true_value, "estimated": estimated_value}
            for true_value, estimated_value in zip(true_flat, estimate_flat)
        )
    metrics = pd.DataFrame(rows)
    metrics.to_csv(output_dir / "parameter_recovery_metrics.csv", index=False)
    pd.DataFrame(scatter).to_csv(
        output_dir / "parameter_recovery_estimates.csv", index=False
    )
    fig, ax = plt.subplots(figsize=(7, 6))
    scatter_frame = pd.DataFrame(scatter)
    for name, group in scatter_frame.groupby("parameter_class"):
        ax.scatter(group["true"], group["estimated"], alpha=0.45, s=18, label=name)
    limits = [
        scatter_frame[["true", "estimated"]].min().min(),
        scatter_frame[["true", "estimated"]].max().max(),
    ]
    ax.plot(limits, limits, "--", color="0.5")
    ax.set(title="Synthetic parameter recovery", xlabel="True", ylabel="Estimated")
    ax.grid(alpha=0.25)
    ax.legend(ncol=2, fontsize=8)
    fig.tight_layout()
    fig.savefig(output_dir / "parameter_recovery.png", dpi=160)
    plt.close(fig)
    (output_dir / "README.md").write_text(
        "# Minimal parameter recovery\n\n"
        "This seeded check generates a small two-dimensional sigmoid competing-risks "
        "dataset, refits it with the repository's AutoNormal SVI baseline, and resolves "
        "only dimension-label switching before scoring. The reported errors, interval "
        "coverage, and interval width are descriptive and have no built-in pass/fail "
        "cutoffs. This is a smoke test for recovery, not evidence for synergy "
        "identifiability or a replacement for a multi-size study.\n",
        encoding="utf-8",
    )
    return metrics
