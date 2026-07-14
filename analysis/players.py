"""Which players do the extra dimensions help — the strong, or the specialized?

    .venv/bin/python -m analysis.players

Computes each player's held-out log-loss change from the 1-D model to a
reference multidimensional model, then asks what predicts it. The covariates
are chosen under two constraints:

- **Rotation invariance.** The baseline model's latent axes are identified
  only up to rotation (`theta ~ N(0,I)`, `alpha ~ N(0,I)`, likelihood sees
  only `theta · alpha`), so nothing may be read off raw `theta_k` coordinates.
  Only norms, inner products, and the scalar dim-1 fit are used.
- **Exogeneity.** A covariate read off the model being evaluated (or off the
  scored labels) can explain the gain because of the fit, not the player. The
  decisive covariates therefore come from the sweep's 2024 *training* leg — a
  disjoint season's labels.

The decisive output is the joint OLS of the gain on the 2024 scalar rating
(general skill) and the 2024 multidim norm (general + off-axis skill mass).
Established answer: off-axis mass predicts *more* gain, general skill *less* —
"stronger players gain more" was an artifact of `theta_norm` bundling both.
The module also prints the model-free 2024 proxies (accuracy, buzz earliness)
whose disagreement that decomposition explains: accuracy is a general-skill
proxy (two opposing effects cancel → null); earliness partially loads on
specialized early-clue knowledge (→ weakly negative).
"""

from __future__ import annotations

import numpy as np
import pandas as pd
from scipy import stats

from compirt_eval.metrics import classification_metrics
from compirt_eval.outputs import csv_path, evaluation_output_dirs

from analysis.data import base_parser, load_buzzes, load_players, require_dimensions
from analysis.figures import plot_player_gains
from analysis.metrics import print_frame


def per_player_log_loss(sweep_dir, dimension, min_buzzes, leg="holdout"):
    """Per-player held-out log loss at one dimension.

    Log loss (not AUC): a player whose buzzes were all correct has no negative
    class, so their AUC is undefined, and dropping them would bias the panel
    toward the mediocre.
    """
    buzzes = load_buzzes(sweep_dir, dimension, leg)
    counts = buzzes.groupby("player_id").size()
    eligible = counts[counts >= min_buzzes].index
    rows = {}
    for player_id, group in buzzes[buzzes["player_id"].isin(eligible)].groupby("player_id"):
        rows[player_id] = classification_metrics(group["y"], group["predicted_correct"])[
            "log_loss"
        ]
    return pd.Series(rows)


def gain_frame(sweep_dir, low, reference, min_buzzes):
    """Each eligible player's log-loss change, negative = multidim better."""
    baseline = per_player_log_loss(sweep_dir, low, min_buzzes)
    multidim = per_player_log_loss(sweep_dir, reference, min_buzzes)
    frame = pd.DataFrame({"log_loss_1d": baseline, "log_loss_reference": multidim}).dropna()
    frame["log_loss_delta"] = frame["log_loss_reference"] - frame["log_loss_1d"]
    return frame


def oriented_scalar_theta(sweep_dir, leg):
    """The dim-1 fit's theta, sign-oriented so higher = stronger.

    At m=1 the sign of theta is arbitrary per run (theta and alpha can flip
    together), so orient it against that same leg's observed buzz accuracy —
    one bit of label information, used only to fix the direction.
    """
    theta = load_players(sweep_dir, 1, leg).set_index("player_id")["theta_1"]
    buzzes = load_buzzes(sweep_dir, 1, leg)
    accuracy = buzzes.groupby("player_id")["y"].mean()
    common = theta.index.intersection(accuracy.index)
    sign = np.sign(stats.pearsonr(theta[common], accuracy[common])[0])
    return sign * theta


def train_proxies(sweep_dir, min_buzzes):
    """Model-free 2024 strength proxies: accuracy and buzz earliness."""
    buzzes = load_buzzes(sweep_dir, 1, leg="train")
    grouped = buzzes.groupby("player_id")
    frame = pd.DataFrame(
        {
            "train_buzzes": grouped.size(),
            "accuracy_2024": grouped["y"].mean(),
            "earliness_2024": -grouped["relative_position"].mean(),
        }
    )
    return frame[frame["train_buzzes"] >= min_buzzes]


def joint_ols(outcome, covariates):
    """Standardized OLS with classic t-stats; returns one row per covariate."""
    design = np.column_stack(
        [np.ones(len(outcome))] + [stats.zscore(c) for c in covariates.values()]
    )
    target = stats.zscore(outcome)
    beta, *_ = np.linalg.lstsq(design, target, rcond=None)
    residual = target - design @ beta
    dof = len(target) - design.shape[1]
    covariance = (residual @ residual / dof) * np.linalg.inv(design.T @ design)
    errors = np.sqrt(np.diag(covariance))
    t_values = beta / errors
    p_values = 2 * stats.t.sf(np.abs(t_values), dof)
    return pd.DataFrame(
        {
            "term": list(covariates),
            "beta": beta[1:],
            "t": t_values[1:],
            "p": p_values[1:],
        }
    )


def correlation_table(frame, covariates):
    rows = []
    for name in covariates:
        subset = frame.dropna(subset=[name, "log_loss_delta"])
        pearson_r, pearson_p = stats.pearsonr(subset[name], subset["log_loss_delta"])
        spearman_r, spearman_p = stats.spearmanr(subset[name], subset["log_loss_delta"])
        rows.append(
            {
                "covariate": name,
                "players": len(subset),
                "pearson_r": pearson_r,
                "pearson_p": pearson_p,
                "spearman_r": spearman_r,
                "spearman_p": spearman_p,
            }
        )
    return pd.DataFrame(rows)


def quartile_table(frame, covariate, labels):
    subset = frame.dropna(subset=[covariate, "log_loss_delta"]).copy()
    subset["quartile"] = pd.qcut(subset[covariate], 4, labels=labels)
    summary = subset.groupby("quartile", observed=True)["log_loss_delta"].agg(["mean", "count"])
    return pd.DataFrame(
        {
            "covariate": covariate,
            "quartile": summary.index,
            "mean_log_loss_delta": summary["mean"].to_numpy(),
            "players": summary["count"].to_numpy(),
        }
    )


def main():
    parser = base_parser(__doc__)
    parser.add_argument(
        "--reference-dimension",
        type=int,
        default=5,
        help="Multidimensional model the 1-D baseline is contrasted against.",
    )
    parser.add_argument(
        "--min-player-buzzes",
        type=int,
        default=30,
        help="Drop players with fewer scored buzzes; their log loss is mostly noise.",
    )
    arguments = parser.parse_args()
    evaluation_output_dirs(arguments.output_dir)
    dimensions = require_dimensions(arguments.sweep_dir)
    low = min(dimensions)
    reference = arguments.reference_dimension
    if reference not in dimensions:
        raise SystemExit(f"reference dimension {reference} not in sweep {dimensions}")

    frame = gain_frame(arguments.sweep_dir, low, reference, arguments.min_player_buzzes)
    print(
        f"{len(frame)} players with >= {arguments.min_player_buzzes} buzzes; "
        f"{(frame['log_loss_delta'] < 0).mean():.1%} predicted better at dim {reference} "
        f"(mean delta {frame['log_loss_delta'].mean():+.4f})"
    )

    # Endogenous (same-season, model-derived) and exogenous (2024) covariates.
    frame["norm_2025"] = load_players(arguments.sweep_dir, reference).set_index("player_id")[
        "theta_norm"
    ]
    frame["norm_2024"] = load_players(arguments.sweep_dir, reference, leg="train").set_index(
        "player_id"
    )["theta_norm"]
    frame["general_2024"] = oriented_scalar_theta(arguments.sweep_dir, leg="train")
    frame = frame.join(train_proxies(arguments.sweep_dir, arguments.min_player_buzzes))

    print_frame(
        "marginal correlations with the gain (negative = that kind of player gains more)",
        correlation_table(
            frame,
            ["norm_2025", "norm_2024", "general_2024", "accuracy_2024", "earliness_2024"],
        ),
    )

    returning = frame.dropna(subset=["general_2024", "norm_2024"])
    print_frame(
        f"joint OLS, exogenous 2024 covariates (n={len(returning)} returning players)",
        joint_ols(
            returning["log_loss_delta"].to_numpy(),
            {
                "general skill (2024 dim-1 theta)": returning["general_2024"].to_numpy(),
                "norm incl. off-axis mass (2024 dim-5)": returning["norm_2024"].to_numpy(),
            },
        ),
    )

    quartiles = pd.concat(
        [
            quartile_table(returning, "general_2024",
                           ["Q1 weakest", "Q2", "Q3", "Q4 strongest"]),
            quartile_table(returning, "norm_2024",
                           ["Q1 smallest", "Q2", "Q3", "Q4 largest"]),
        ],
        ignore_index=True,
    )
    print_frame("mean gain by 2024-covariate quartile", quartiles)

    frame.reset_index(names="player_id").to_csv(
        csv_path(arguments.output_dir, "player_gains.csv"), index=False
    )
    print(f"\nwrote {csv_path(arguments.output_dir, 'player_gains.csv')}")
    plot_player_gains(quartiles, arguments.output_dir)


if __name__ == "__main__":
    main()
