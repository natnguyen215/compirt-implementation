"""Compare fitted per-player buzz accuracy to tournament individual scoring.

The model-side ordering comes from 'player_buzz_summary.csv': mean fitted
P(correct | the player buzzed where they did) over each player's observed
buzzes. That quantity is conditioned on the player's own shot selection and
ignores buzz volume and timing, so it is *not* a skill or scoring ranking --
cautious late buzzers rate high and aggressive early buzzers rate low
regardless of theta. The public standings comparators (PPG, PP20) reward
scoring volume, so weak rank agreement here is expected by construction and
does not by itself indicate model misfit. For a PPG-comparable model ranking,
use a competing-risks expected-points summary
(see 'compirt_eval.noise_floor').
"""

from __future__ import annotations

import csv
import json
import math
import sqlite3
from collections import defaultdict
from pathlib import Path

from scipy.stats import spearmanr


# This module lives at compirt_eval/player_rankings/evaluation.py, so the repository
# root (which holds data/database.db) is three parents up.
ROOT = Path(__file__).resolve().parents[2]
DEFAULT_DATABASE = ROOT / "data" / "database.db"
ACTUAL_RANK_MODES = ("ppg", "pp20")


def read_global_model(path: Path) -> dict[str, dict[str, float | int]]:
    """Read the saved all-run player buzz summary and order it by accuracy.

    The saved 'player_buzz_summary.csv' is sorted by buzz volume, so the
    fitted-buzz-accuracy order is derived here explicitly rather than from
    file order. 'global_model_rank' is a rank on conditional buzz accuracy,
    not on skill or scoring.
    """
    with path.open(newline="", encoding="utf-8") as handle:
        raw_rows = list(csv.DictReader(handle))
    raw_rows.sort(
        key=lambda row: (
            -float(row["fitted_correctness"]),
            -int(row["buzzes"]),
            row["player_id"],
        )
    )
    rows: dict[str, dict[str, float | int]] = {}
    for rank, row in enumerate(raw_rows, start=1):
        rows[row["player_id"]] = {
            "global_model_rank": rank,
            "global_model_buzzes": int(row["buzzes"]),
            "global_fitted_correctness": float(row["fitted_correctness"]),
            "global_average_relative_position": float(
                row["average_relative_position"]
            ),
        }
    return rows


def read_tournament_model(path: Path, tournament: str) -> dict[str, dict[str, float | int]]:
    """Order players within one tournament by fitted conditional buzz accuracy."""
    aggregates: dict[str, dict[str, float | int]] = defaultdict(
        lambda: {
            "tournament_model_buzzes": 0,
            "fitted": 0.0,
            "position": 0.0,
        }
    )
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            if row["tournament_id"] != tournament or row["z"] != "BUZZ":
                continue
            aggregate = aggregates[row["player_id"]]
            aggregate["tournament_model_buzzes"] += 1
            aggregate["fitted"] += float(row["predicted_correct"])
            aggregate["position"] += float(row["relative_position"])

    rows = []
    for player_id, aggregate in aggregates.items():
        buzzes = int(aggregate["tournament_model_buzzes"])
        rows.append(
            {
                "player_id": player_id,
                "tournament_model_buzzes": buzzes,
                "tournament_fitted_correctness": aggregate["fitted"] / buzzes,
                "tournament_average_relative_position": aggregate["position"] / buzzes,
            }
        )
    rows.sort(
        key=lambda row: (
            -row["tournament_fitted_correctness"],
            -row["tournament_model_buzzes"],
            row["player_id"],
        )
    )
    return {
        row["player_id"]: {"tournament_model_rank": rank, **row}
        for rank, row in enumerate(rows, start=1)
    }


def actual_tournament_stats(
    database: Path,
    tournament: str,
    min_games: int,
    min_tuh: int,
    rank_mode: str = "ppg",
    min_game_tossups: int = 1,
) -> list[dict[str, float | int | str]]:
    """Return tournament individual scoring ranked by the selected public metric."""
    rank_expressions = {
        "ppg": "actual_points / nullif(games, 0)",
        "pp20": "20.0 * actual_points / nullif(tuh, 0)",
    }
    try:
        rank_expression = rank_expressions[rank_mode]
    except KeyError as error:
        choices = ", ".join(ACTUAL_RANK_MODES)
        raise ValueError(f"Unknown rank mode {rank_mode!r}; choose one of: {choices}") from error

    query = f"""
    with eligible_games as (
      select g.id, g.tossups_read, g.team_one_id, g.team_two_id
      from game g
      join round r on r.id = g.round_id
      join tournament t on t.id = r.tournament_id
      where t.slug = ?
        and coalesce(r.exclude_from_individual, 0) = 0
        -- The Nationals batch uses 20 here to exclude its local 12-tossup
        -- Team 1/Team 2 test game; this is game validation, not player eligibility.
        and g.tossups_read >= ?
    ),
    game_totals as (
      select p.id as player_db_id, p.name, p.slug as player_id, tm.name as team_name,
             count(distinct eg.id) as games, sum(eg.tossups_read) as tuh
      from player p
      join team tm on tm.id = p.team_id
      join eligible_games eg on p.team_id in (eg.team_one_id, eg.team_two_id)
      group by p.id
    ),
    buzz_totals as (
      select b.player_id as player_db_id, sum(b.value) as actual_points,
             sum(case when b.value > 0 then 1 else 0 end) as gets,
             sum(case when b.value < 0 then 1 else 0 end) as negs
      from buzz b
      join eligible_games eg on eg.id = b.game_id
      group by b.player_id
    ),
    player_totals as (
      select gt.*, coalesce(bt.actual_points, 0) as actual_points,
             coalesce(bt.gets, 0) as gets, coalesce(bt.negs, 0) as negs
      from game_totals gt
      left join buzz_totals bt using (player_db_id)
      where gt.games >= ? and gt.tuh >= ?
    ),
    ranked as (
      select row_number() over (
               order by {rank_expression} desc,
                        actual_points desc,
                        player_id
             ) as actual_rank,
             name, player_id, team_name, games, tuh, actual_points, gets, negs,
             actual_points / nullif(games, 0) as actual_ppg,
             20.0 * actual_points / nullif(tuh, 0) as actual_pp20
      from player_totals
    )
    select * from ranked order by actual_rank
    """
    connection = sqlite3.connect(database)
    connection.row_factory = sqlite3.Row
    try:
        return [
            dict(row)
            for row in connection.execute(
                query, (tournament, min_game_tossups, min_games, min_tuh)
            )
        ]
    finally:
        connection.close()


def rank_correlation(rows: list[dict[str, object]], rank_key: str) -> float | None:
    """Return Spearman rank correlation for players present in both rankings."""
    matched = [
        (float(row["actual_rank"]), float(row[rank_key]))
        for row in rows
        if row.get(rank_key) not in (None, "")
    ]
    if len(matched) < 2:
        return None
    actual_ranks, model_ranks = zip(*matched)
    correlation = spearmanr(actual_ranks, model_ranks).statistic
    # A constant column leaves the correlation undefined.
    return None if math.isnan(correlation) else float(correlation)


def overlap_count(
    rows: list[dict[str, object]], actual_top: int, model_key: str, model_top: int
) -> int:
    """Count actual top-N players also inside a model top-N set."""
    actual = {row["player_id"] for row in rows if int(row["actual_rank"]) <= actual_top}
    model = {
        row["player_id"]
        for row in rows
        if row.get(model_key) not in (None, "") and int(row[model_key]) <= model_top
    }
    return len(actual & model)


def tournament_overlap_summary(
    rows: list[dict[str, object]], *, cutoffs: tuple[int, ...] = (20, 50)
) -> dict[str, str]:
    """Return only like-for-like actual/model tournament-rank overlaps."""
    return {
        f"actual_top_{cutoff}_in_tournament_model_rank_top_{cutoff}": (
            f"{overlap_count(rows, cutoff, 'tournament_model_rank', cutoff)}/{cutoff}"
        )
        for cutoff in dict.fromkeys(cutoffs)
    }


def format_value(value: object) -> str:
    """Render values for Markdown tables."""
    if value is None:
        return ""
    if isinstance(value, float):
        return f"{value:.3f}"
    return str(value)


def markdown_table(rows: list[dict[str, object]], columns: list[str]) -> str:
    """Create a small GitHub-flavored Markdown table without extra dependencies."""
    header = "| " + " | ".join(columns) + " |"
    divider = "| " + " | ".join("---" for _ in columns) + " |"
    body = [
        "| " + " | ".join(format_value(row.get(column)) for column in columns) + " |"
        for row in rows
    ]
    return "\n".join([header, divider, *body])


def write_outputs(
    rows: list[dict[str, object]],
    summary: dict[str, object],
    output_dir: Path,
) -> None:
    """Write the joined CSV, machine-readable summary, and Markdown report."""
    output_dir.mkdir(parents=True, exist_ok=True)
    columns = [
        "actual_rank",
        "name",
        "player_id",
        "team_name",
        "games",
        "tuh",
        "actual_points",
        "gets",
        "negs",
        "actual_ppg",
        "actual_pp20",
        "global_model_rank",
        "global_fitted_correctness",
        "global_model_buzzes",
        "global_average_relative_position",
        "tournament_model_rank",
        "tournament_fitted_correctness",
        "tournament_model_buzzes",
        "tournament_average_relative_position",
    ]
    with (output_dir / "player_ranking_comparison.csv").open(
        "w", newline="", encoding="utf-8"
    ) as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)

    (output_dir / "summary.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8"
    )

    table_columns = [
        "actual_rank",
        "name",
        "team_name",
        "actual_ppg",
        "actual_pp20",
        "actual_points",
        "global_model_rank",
        "tournament_model_rank",
        "tournament_fitted_correctness",
        "tournament_model_buzzes",
    ]
    actual_top = rows[:25]
    tournament_model_top = sorted(
        [row for row in rows if row.get("tournament_model_rank") not in (None, "")],
        key=lambda row: int(row["tournament_model_rank"]),
    )[:25]
    rank_mode = str(summary["actual_rank_mode"])
    min_game_tossups = int(summary["min_game_tossups"])
    if rank_mode == "ppg":
        ranking_method = (
            "This report uses `actual_ppg` (`actual_points / games`) as its real "
            "rank metric."
        )
    else:
        ranking_method = (
            "This report uses `actual_pp20` (`20 * actual_points / tossups_heard`) "
            "as its real rank metric."
        )
    if min_game_tossups > 1:
        game_filter_note = (
            f"Only games with at least `{min_game_tossups}` tossups are included "
            "as a source-data integrity filter; this is separate from player "
            "eligibility."
        )
    else:
        game_filter_note = "All recorded games with at least one tossup are included."
    report = [
        f"# Player Ranking Comparison: {summary['tournament']}",
        "",
        "The real-world comparator here is tournament individual scoring from "
        "the source database. The default `ppg` mode follows the public "
        "[2024 ACF Nationals player standings](https://quizbowlstats.com/tournaments/2045), "
        "which are ordered by points per game and do not state a minimum-games "
        "or minimum-TUH eligibility floor. The model-side ordering is mean "
        "fitted P(correct | the player buzzed where they did) over observed "
        "buzzes -- conditional buzz accuracy. It is conditioned on each "
        "player's own shot selection and ignores buzz volume and timing, so "
        "it is not a skill or scoring ranking, and weak agreement with the "
        "PPG/PP20 standings is expected by construction rather than evidence "
        "of model misfit.",
        "",
        ranking_method,
        "",
        game_filter_note,
        "",
        "Caveat: the actual games/TUH counts here credit every registered "
        "roster member with all of their team's games, because the source "
        "database has no per-game lineups. The model side instead uses "
        "lineups inferred from buzz evidence (`lineup.py`), so the two sides "
        "make different participation assumptions, and `actual_ppg` "
        "denominators are inflated for players who did not play every game "
        "for their listed team.",
        "",
        "## Summary",
        "",
        markdown_table(
            [
                {"metric": key, "value": value}
                for key, value in summary.items()
                if key != "tournament"
            ],
            ["metric", "value"],
        ),
        "",
        "## Actual Top 25",
        "",
        markdown_table(actual_top, table_columns),
        "",
        "## Tournament-Filtered Model Top 25",
        "",
        markdown_table(tournament_model_top, table_columns),
        "",
    ]
    (output_dir / "player_ranking_comparison.md").write_text(
        "\n".join(report), encoding="utf-8"
    )


def evaluate_player_rankings(
    tournament: str,
    database: Path,
    player_summary: Path,
    predictions: Path,
    output_root: Path,
    actual_rank_mode: str = "ppg",
    min_games: int = 1,
    min_tuh: int = 1,
    min_game_tossups: int = 1,
    actual_top: int = 20,
) -> Path:
    """Compare one fitted run with tournament standings and write reports."""
    if actual_rank_mode not in ACTUAL_RANK_MODES:
        raise ValueError(f"actual_rank_mode must be one of {ACTUAL_RANK_MODES}")
    if (
        min_games < 0
        or min_tuh < 0
        or min_game_tossups < 1
        or actual_top < 1
    ):
        raise ValueError(
            "Player thresholds must be non-negative, min-game-tossups and actual-top positive"
        )

    global_model = read_global_model(player_summary)
    tournament_model = read_tournament_model(predictions, tournament)
    actual = actual_tournament_stats(
        database,
        tournament,
        min_games,
        min_tuh,
        actual_rank_mode,
        min_game_tossups,
    )
    if not actual:
        raise ValueError(f"No actual scoring rows found for {tournament!r}")

    for row in actual:
        row.update(global_model.get(str(row["player_id"]), {}))
        row.update(tournament_model.get(str(row["player_id"]), {}))

    tournament_matches = sum("tournament_model_rank" in row for row in actual)
    summary: dict[str, object] = {
        "tournament": tournament,
        "actual_players_after_floor": len(actual),
        "actual_rank_mode": actual_rank_mode,
        "actual_rank_metric": "actual_ppg"
        if actual_rank_mode == "ppg"
        else "actual_pp20",
        "min_games": min_games,
        "min_tuh": min_tuh,
        "min_game_tossups": min_game_tossups,
        "tournament_model_matches": tournament_matches,
        "tournament_rank_correlation": rank_correlation(
            actual, "tournament_model_rank"
        ),
    }
    # Global and tournament ranks are identical for these single-tournament
    # in-sample runs. Keep only like-for-like tournament overlaps; cross-cutoff
    # values such as actual top 20 in model top 200 are not informative.
    summary.update(tournament_overlap_summary(actual, cutoffs=(actual_top, 50)))

    output_dir = output_root / tournament
    write_outputs(actual, summary, output_dir)
    return output_dir
