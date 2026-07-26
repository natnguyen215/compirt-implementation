"""Pure Markdown rendering for the 2024 Nationals aggregate report."""

from __future__ import annotations


def markdown_table(rows: list[dict[str, object]], columns: list[str]) -> str:
    """Render selected dictionary columns as a compact Markdown table."""
    def format_value(value: object) -> str:
        if value is None:
            return ""
        if isinstance(value, float):
            return f"{value:.6g}"
        return str(value)

    header = "| " + " | ".join(columns) + " |"
    divider = "| " + " | ".join("---" for _ in columns) + " |"
    body = [
        "| " + " | ".join(format_value(row.get(column)) for column in columns) + " |"
        for row in rows
    ]
    return "\n".join([header, divider, *body])


def aggregate_markdown(args, rows: list[dict[str, object]]) -> str:
    """Render the established ranking-method explanation and summary table."""
    report_columns = [
        "run_name",
        "calibration",
        "tournament_rank_correlation",
        "actual_top_20_in_tournament_model_rank_top_20",
        "actual_top_50_in_tournament_model_rank_top_50",
    ]
    if args.actual_rank_mode == "ppg":
        ranking_method = (
            "This aggregate uses `actual_ppg`, which is `actual_points / games`, "
            "with total points and `player_id` used as tie-breakers."
        )
        rank_label = "PPG"
    else:
        ranking_method = (
            "This aggregate uses `actual_pp20`, which is `20 * actual_points / "
            "tossups_heard`, with total points and `player_id` used as tie-breakers."
        )
        rank_label = "PP20"
    report = [
        "# 2024 ACF Nationals Model Ranking Summary",
        "",
        f"Tournament: `{args.tournament}`",
        "",
        "## How Correlations Are Calculated",
        "",
        "The real-world rank is built from tournament individual scoring. "
        "The public [2024 ACF Nationals player standings](https://quizbowlstats.com/tournaments/2045) "
        "are ordered by PPG and do not state a minimum-games or minimum-TUH "
        "eligibility floor, so this batch defaults to `min_games=1` and "
        f"`min_tuh=1`. It includes only games with at least `{args.min_game_tossups}` "
        "tossups as a source-data integrity rule, not a player eligibility threshold.",
        "",
        ranking_method,
        "",
        "`tournament_rank_correlation` is the Pearson correlation between "
        "`actual_rank` and `tournament_model_rank` for players present in both "
        "rankings. `tournament_model_rank` is recalculated from this "
        "tournament's `BUZZ` rows only, sorting by average fitted "
        "`predicted_correct`, then model buzz count, then `player_id`.",
        "",
        "Because both inputs are ranks, this Pearson calculation is equivalent "
        "to a Spearman rank correlation over the matched players. The global "
        "and tournament rank correlations are identical for these runs because "
        "the models were fit on this one tournament, so this summary reports "
        "only the tournament-filtered correlation.",
        "",
        "Higher positive values mean the model ordering is more aligned with "
        f"the real {rank_label} ordering. `1.0` would be perfect agreement, `0` means "
        "little linear rank alignment, and negative values mean the ordering "
        "is moving in the opposite direction.",
        "",
        "## Top-N Overlap Columns",
        "",
        "`actual_top_20_in_tournament_model_rank_top_20` counts how many of "
        "the real top 20 players also appear in the model's top 20. "
        "`actual_top_50_in_tournament_model_rank_top_50` does the same check "
        "for the real top 50 against the model's top 50. A value like `17/20` "
        "means 17 of the real top 20 were captured by the model top 20; a "
        "value like `38/50` means 38 of the real top 50 were captured by the "
        "model top 50.",
        "",
        markdown_table(rows, report_columns),
        "",
    ]
    return "\n".join(report)
