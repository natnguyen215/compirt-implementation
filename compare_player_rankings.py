"""Compare fitted player rankings to tournament individual scoring.

The fitted ``top_players.csv`` ranks players by mean predicted correctness on
their observed buzzes. Public quizbowl standings usually rank by scoring volume
or points per tossup heard, so this script joins both views for a named
tournament and writes a compact audit report.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import sqlite3
import statistics
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).parent
DEFAULT_DATABASE = ROOT / "data" / "database.db"
DEFAULT_TOP_PLAYERS = ROOT / "results" / "cuda-all-2024" / "pyramidal" / "top_players.csv"
DEFAULT_PREDICTIONS = (
    ROOT / "results" / "cuda-all-2024" / "pyramidal" / "tossup_predictions.csv"
)
DEFAULT_OUTPUT_DIR = ROOT / "results" / "cuda-all-2024" / "ranking_comparison"


def read_global_model(path: Path) -> dict[str, dict[str, float | int]]:
    """Read the saved all-run player ranking keyed by player slug."""
    rows: dict[str, dict[str, float | int]] = {}
    with path.open(newline="", encoding="utf-8") as handle:
        for rank, row in enumerate(csv.DictReader(handle), start=1):
            rows[row["player_id"]] = {
                "global_model_rank": rank,
                "global_model_buzzes": int(row["buzzes"]),
                "global_observed_correctness": float(row["observed_correctness"]),
                "global_fitted_correctness": float(row["fitted_correctness"]),
                "global_average_relative_position": float(
                    row["average_relative_position"]
                ),
            }
    return rows


def read_tournament_model(path: Path, tournament: str) -> dict[str, dict[str, float | int]]:
    """Rank players within one tournament from row-level model predictions."""
    aggregates: dict[str, dict[str, float | int]] = defaultdict(
        lambda: {
            "tournament_model_buzzes": 0,
            "correct": 0.0,
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
            aggregate["correct"] += float(row["y"])
            aggregate["fitted"] += float(row["predicted_correct"])
            aggregate["position"] += float(row["relative_position"])

    rows = []
    for player_id, aggregate in aggregates.items():
        buzzes = int(aggregate["tournament_model_buzzes"])
        rows.append(
            {
                "player_id": player_id,
                "tournament_model_buzzes": buzzes,
                "tournament_observed_correctness": aggregate["correct"] / buzzes,
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
    database: Path, tournament: str, min_games: int, min_tuh: int
) -> list[dict[str, float | int | str]]:
    """Return tournament individual scoring from the source SQLite database."""
    query = """
    with eligible_games as (
      select g.id, g.tossups_read, g.team_one_id, g.team_two_id
      from game g
      join round r on r.id = g.round_id
      join tournament t on t.id = r.tournament_id
      where t.slug = ?
        and coalesce(r.exclude_from_individual, 0) = 0
        and g.tossups_read > 0
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
               order by 20.0 * actual_points / nullif(tuh, 0) desc,
                        actual_points desc,
                        player_id
             ) as actual_rank,
             name, player_id, team_name, games, tuh, actual_points, gets, negs,
             20.0 * actual_points / nullif(tuh, 0) as actual_pp20
      from player_totals
    )
    select * from ranked order by actual_rank
    """
    connection = sqlite3.connect(database)
    connection.row_factory = sqlite3.Row
    try:
        return [dict(row) for row in connection.execute(query, (tournament, min_games, min_tuh))]
    finally:
        connection.close()


def rank_correlation(rows: list[dict[str, object]], rank_key: str) -> float | None:
    """Pearson correlation on rank columns, equivalent to Spearman here."""
    matched = [
        (float(row["actual_rank"]), float(row[rank_key]))
        for row in rows
        if row.get(rank_key) not in (None, "")
    ]
    if len(matched) < 2:
        return None
    actual_ranks, model_ranks = zip(*matched)
    actual_mean = statistics.mean(actual_ranks)
    model_mean = statistics.mean(model_ranks)
    covariance = sum(
        (actual - actual_mean) * (model - model_mean)
        for actual, model in matched
    )
    actual_scale = math.sqrt(
        sum((actual - actual_mean) ** 2 for actual in actual_ranks)
    )
    model_scale = math.sqrt(sum((model - model_mean) ** 2 for model in model_ranks))
    if actual_scale == 0 or model_scale == 0:
        return None
    return covariance / (actual_scale * model_scale)


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
    report = [
        f"# Player Ranking Comparison: {summary['tournament']}",
        "",
        "The real-world comparator here is tournament individual scoring from "
        "the source database, ranked by points per 20 tossups heard. The fitted "
        "model ranks players by mean predicted correctness on observed buzzes, "
        "so it rewards accuracy more than scoring volume.",
        "",
        "Caveat: the source database does not include game-specific lineups, so "
        "tossups heard are inferred from registered rosters. That matches the "
        "modeling assumption used by this project, but it can blur players who "
        "did not play every game for their listed team.",
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


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tournament", required=True, help="Tournament slug to compare")
    parser.add_argument("--database", type=Path, default=DEFAULT_DATABASE)
    parser.add_argument("--top-players", type=Path, default=DEFAULT_TOP_PLAYERS)
    parser.add_argument("--predictions", type=Path, default=DEFAULT_PREDICTIONS)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--min-games", type=int, default=8)
    parser.add_argument("--min-tuh", type=int, default=160)
    parser.add_argument("--actual-top", type=int, default=20)
    args = parser.parse_args()

    global_model = read_global_model(args.top_players)
    tournament_model = read_tournament_model(args.predictions, args.tournament)
    actual = actual_tournament_stats(
        args.database, args.tournament, args.min_games, args.min_tuh
    )
    if not actual:
        raise ValueError(f"No actual scoring rows found for {args.tournament!r}")

    for row in actual:
        row.update(global_model.get(str(row["player_id"]), {}))
        row.update(tournament_model.get(str(row["player_id"]), {}))

    global_matches = sum("global_model_rank" in row for row in actual)
    tournament_matches = sum("tournament_model_rank" in row for row in actual)
    summary: dict[str, object] = {
        "tournament": args.tournament,
        "actual_players_after_floor": len(actual),
        "min_games": args.min_games,
        "min_tuh": args.min_tuh,
        "global_model_matches": global_matches,
        "tournament_model_matches": tournament_matches,
        "global_rank_correlation": rank_correlation(actual, "global_model_rank"),
        "tournament_rank_correlation": rank_correlation(
            actual, "tournament_model_rank"
        ),
    }
    for model_key in ("global_model_rank", "tournament_model_rank"):
        for model_top in (20, 50, 100, 200):
            summary[f"actual_top_{args.actual_top}_in_{model_key}_top_{model_top}"] = (
                f"{overlap_count(actual, args.actual_top, model_key, model_top)}/"
                f"{args.actual_top}"
            )

    output_dir = args.output_dir / args.tournament
    write_outputs(actual, summary, output_dir)
    print(f"Wrote {output_dir / 'player_ranking_comparison.md'}")
    print(f"Wrote {output_dir / 'player_ranking_comparison.csv'}")


if __name__ == "__main__":
    main()
