"""Create diagnostic visualizations for fitted multidimensional IRT results."""

import argparse
import sqlite3
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


PROJECT_ROOT = Path(__file__).parent.parent
DEFAULT_RESPONSES = PROJECT_ROOT / "data" / "response_matrix.csv"
DEFAULT_DATABASE = PROJECT_ROOT / "data" / "database.db"
DEFAULT_RESULTS = PROJECT_ROOT / "results"
DEFAULT_OUTPUT = DEFAULT_RESULTS / "figures"


def sigmoid(x):
    """Numerically stable logistic function."""
    x = np.clip(x, -30, 30)
    return 1.0 / (1.0 + np.exp(-x))


def load_long_form(response_path, results_dir):
    """Join every observed response to its fitted player/question parameters."""
    responses = pd.read_csv(response_path, index_col=0)
    responses.index = responses.index.astype(str)
    responses.columns = responses.columns.astype(str)

    long = (
        responses.rename_axis(index="player_id", columns="question_id")
        .stack()
        .rename("response")
        .dropna()
        .reset_index()
    )
    players = pd.read_csv(results_dir / "players.csv")
    questions = pd.read_csv(results_dir / "questions.csv")
    players["player_id"] = players["player_id"].astype(str)
    questions["question_id"] = questions["question_id"].astype(str)
    theta_columns = sorted(column for column in players if column.startswith("theta_"))
    alpha_columns = sorted(column for column in questions if column.startswith("alpha_"))
    if len(theta_columns) != len(alpha_columns) or not theta_columns:
        raise ValueError("Results must contain matching theta_1... and alpha_1... columns")

    players["skill_norm"] = np.linalg.norm(players[theta_columns], axis=1)
    questions["discrimination_norm"] = np.linalg.norm(questions[alpha_columns], axis=1)
    long = long.merge(players, on="player_id").merge(questions, on="question_id")
    dot_product = sum(
        long[theta_column] * long[alpha_column]
        for theta_column, alpha_column in zip(theta_columns, alpha_columns)
    )
    long["logit"] = dot_product - long["d"]
    long["predicted_probability"] = sigmoid(long["logit"])
    return long, players, questions


def plot_skill_difficulty_dashboard(long, output_dir):
    """Compare actual responses with fitted predictions."""
    fig, axes = plt.subplot_mosaic(
        [["calibration", "player"], ["question", "question"]],
        figsize=(14, 10),
    )

    # Calibration by the fitted MIRT logit alpha^T theta - d.
    ax = axes["calibration"]
    bins = pd.cut(long["logit"], bins=20)
    calibration = long.groupby(bins, observed=True).agg(
        logit=("logit", "mean"),
        actual=("response", "mean"),
        predicted=("predicted_probability", "mean"),
        n=("response", "size"),
    )
    ax.plot(calibration["logit"], calibration["actual"], "o-", label="Observed response rate")
    ax.plot(calibration["logit"], calibration["predicted"], "o--", label="Model prediction")
    ax.axvline(0, color="0.6", linewidth=1)
    ax.set(
        title="Responses by MIRT logit",
        xlabel=r"$\alpha^\mathsf{T}\theta - d$",
        ylabel="Probability of correct response",
        ylim=(-0.03, 1.03),
    )
    ax.legend()
    ax.grid(alpha=0.25)

    # Do fitted player skill estimates agree with players' raw conversion rates?
    ax = axes["player"]
    player_stats = long.groupby(["player_id", "skill_norm"]).agg(
        actual_rate=("response", "mean"),
        predicted_rate=("predicted_probability", "mean"),
        responses=("response", "size"),
    ).reset_index()
    sizes = 12 + 55 * np.sqrt(player_stats["responses"] / player_stats["responses"].max())
    ax.scatter(player_stats["skill_norm"], player_stats["actual_rate"], s=sizes, alpha=0.35)
    ordered = player_stats.sort_values("skill_norm")
    ax.plot(
        ordered["skill_norm"],
        ordered["predicted_rate"],
        color="tab:orange",
        label="Mean model prediction",
    )
    ax.set(
        title="Player skill-vector norm versus response rate",
        xlabel=r"Player skill norm $\|\theta\|$",
        ylabel="Response rate",
        ylim=(-0.03, 1.03),
    )
    ax.legend()
    ax.grid(alpha=0.25)

    # Do fitted difficulties agree with questions' raw solve rates?
    ax = axes["question"]
    question_stats = long.groupby(["question_id", "d", "discrimination_norm"]).agg(
        actual_rate=("response", "mean"),
        predicted_rate=("predicted_probability", "mean"),
        responses=("response", "size"),
    ).reset_index()
    sizes = 12 + 55 * np.sqrt(question_stats["responses"] / question_stats["responses"].max())
    scatter = ax.scatter(
        question_stats["d"],
        question_stats["actual_rate"],
        c=question_stats["discrimination_norm"],
        s=sizes,
        alpha=0.45,
        cmap="plasma",
    )
    question_trend = question_stats.assign(
        difficulty_bin=pd.cut(question_stats["d"], bins=30)
    ).groupby("difficulty_bin", observed=True).agg(
        d=("d", "mean"),
        predicted_rate=("predicted_rate", "mean"),
    )
    ax.plot(
        question_trend["d"],
        question_trend["predicted_rate"],
        color="tab:green",
        linewidth=2,
        label="Binned model prediction",
    )
    ax.set(
        title="Question difficulty versus response rate",
        xlabel=r"Question difficulty $d$",
        ylabel="Response rate",
        ylim=(-0.03, 1.03),
    )
    ax.legend()
    ax.grid(alpha=0.25)
    fig.colorbar(scatter, ax=ax, label=r"Discrimination norm $\|\alpha\|$")

    fig.suptitle("Multidimensional IRT response diagnostics", fontsize=16)
    fig.tight_layout()
    path = output_dir / "irt_response_dashboard.png"
    fig.savefig(path, dpi=180, bbox_inches="tight")
    plt.close(fig)
    return path


def plot_item_characteristic_curves(questions, players, output_dir):
    """Plot curves along each representative question's discrimination direction."""
    selected = (
        questions.sort_values("d")
        .iloc[np.linspace(0, len(questions) - 1, 5, dtype=int)]
        .drop_duplicates("question_id")
    )
    skill_limit = players["skill_norm"].max() + 0.5
    projected_skill_grid = np.linspace(-skill_limit, skill_limit, 300)

    fig, ax = plt.subplots(figsize=(10, 6))
    for row in selected.itertuples():
        probability = sigmoid(row.discrimination_norm * projected_skill_grid - row.d)
        ax.plot(
            projected_skill_grid,
            probability,
            label=(
                f"question {row.question_id}: "
                f"d={row.d:.2f}, ||alpha||={row.discrimination_norm:.2f}"
            ),
        )
    ax.set(
        title="Item curves along each question's discrimination direction",
        xlabel="Projected player skill",
        ylabel="Predicted probability of correct response",
        ylim=(-0.03, 1.03),
    )
    ax.grid(alpha=0.25)
    ax.legend(fontsize=8)
    fig.tight_layout()
    path = output_dir / "item_characteristic_curves.png"
    fig.savefig(path, dpi=180, bbox_inches="tight")
    plt.close(fig)
    return path


def plot_difficulty_vs_discrimination(questions, output_dir):
    """Plot effective difficulty d / ||alpha|| against discrimination-vector norm."""
    questions = questions.assign(
        effective_difficulty=questions["d"]
        / questions["discrimination_norm"].clip(lower=1e-12)
    )
    fig, ax = plt.subplots(figsize=(8, 6))
    for level, group in questions.groupby("level"):
        ax.scatter(
            group["effective_difficulty"],
            group["discrimination_norm"],
            alpha=0.5,
            label=level,
        )
    ax.set(
        title="Effective question difficulty vs discrimination norm",
        xlabel=r"Effective question difficulty $d / \|\alpha\|$",
        ylabel=r"Question discrimination norm $\|\alpha\|$",
        xlim=(0, 4),
    )
    ax.grid(alpha=0.25)
    ax.legend()
    fig.tight_layout()
    path = output_dir / "difficulty_vs_discrimination.png"
    fig.savefig(path, dpi=180, bbox_inches="tight")
    plt.close(fig)
    return path


def plot_player_skill_vs_buzz_position(players, buzz_stats, output_dir):
    """Plot fitted player skill norm against average recorded buzz position."""
    player_buzz = players.merge(buzz_stats, on="player_id")
    sizes = 10 + 60 * np.sqrt(
        player_buzz["buzz_count"] / player_buzz["buzz_count"].max()
    )

    fig, ax = plt.subplots(figsize=(9, 6))
    ax.scatter(
        player_buzz["skill_norm"],
        player_buzz["avg_buzz_position"],
        s=sizes,
        alpha=0.3,
    )

    trend = player_buzz.assign(
        skill_bin=pd.qcut(player_buzz["skill_norm"], q=20, duplicates="drop")
    ).groupby("skill_bin", observed=True).agg(
        skill_norm=("skill_norm", "mean"),
        avg_buzz_position=("avg_buzz_position", "mean"),
    )
    ax.plot(
        trend["skill_norm"],
        trend["avg_buzz_position"],
        color="tab:orange",
        linewidth=2,
        marker="o",
        label="Binned mean",
    )
    ax.set(
        title="Player skill norm vs average buzz position",
        xlabel=r"Player skill norm $\|\theta\|$",
        ylabel="Average buzz position",
    )
    ax.grid(alpha=0.25)
    ax.legend()
    fig.tight_layout()
    path = output_dir / "player_skill_vs_average_buzz_position.png"
    fig.savefig(path, dpi=180, bbox_inches="tight")
    plt.close(fig)
    return path


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--responses", type=Path, default=DEFAULT_RESPONSES)
    parser.add_argument("--database", type=Path, default=DEFAULT_DATABASE)
    parser.add_argument("--results-dir", type=Path, default=DEFAULT_RESULTS)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def main():
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    long, players, questions = load_long_form(args.responses, args.results_dir)
    with sqlite3.connect(args.database) as connection:
        question_levels = pd.read_sql_query(
            """
            SELECT DISTINCT
              question_set.slug || '::' || question_set_edition.slug
                || '::p' || packet.id
                || '::q' || packet_question.question_number AS question_id,
              tournament.level
            FROM tossup
            JOIN packet_question ON packet_question.question_id = tossup.question_id
            JOIN packet ON packet.id = packet_question.packet_id
            JOIN question_set_edition
              ON question_set_edition.id = packet.question_set_edition_id
            JOIN question_set
              ON question_set.id = question_set_edition.question_set_id
            JOIN tournament
              ON tournament.question_set_edition_id = packet.question_set_edition_id
            """,
            connection,
        )
        buzz_stats = pd.read_sql_query(
            """
            SELECT
              player.slug AS player_id,
              AVG(buzz.buzz_position) AS avg_buzz_position,
              COUNT(*) AS buzz_count
            FROM buzz
            JOIN player ON player.id = buzz.player_id
            WHERE buzz.buzz_position IS NOT NULL
            GROUP BY player.slug
            """,
            connection,
        )
    questions = questions.merge(question_levels, on="question_id", how="left")
    paths = [
        plot_skill_difficulty_dashboard(long, args.output_dir),
        plot_item_characteristic_curves(questions, players, args.output_dir),
        plot_difficulty_vs_discrimination(questions, args.output_dir),
        plot_player_skill_vs_buzz_position(players, buzz_stats, args.output_dir),
    ]
    print(f"Plotted {len(long):,} observed responses.")
    for path in paths:
        print(f"Saved {path}")


if __name__ == "__main__":
    main()
