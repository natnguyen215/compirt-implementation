#!/usr/bin/env python3
"""Exploratory analysis of the 2024-25 season, the one complete season in the corpus.

The season runs ACF Fall (2024-10-19) -> Winter (2024-11-16) -> Regionals
(2025-02-01) -> Nationals (2025-04-19), spanning 33 mirror sites.  Because it is
a single season, calendar year is perfectly collinear with tier and is therefore
dropped as an axis entirely: **tier is the chronological axis**, and it happens
to be the difficulty axis too.

This scope buys two things the year-split analyses in ``analysis/full_dataset_eda``
cannot have:

* Complete category metadata.  The only unlabelled set in the corpus is 2024
  Regionals, which belongs to season 2023-24, so every question here is labelled.
* Within-season player progression.  Players can be followed across the four
  tiers of one season, and selection can be measured on a *fixed* question set
  rather than across sets of differing difficulty.
"""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import tempfile
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "season_eda_mpl"))

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
import pandas as pd
from datasets import load_from_disk


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
DEFAULT_DATA = ROOT / "data" / "hf" / "quizbowl-irt"
SEASON = "2024-25"

PAPER = "#F7F4EE"
INK = "#17282E"
MUTED = "#68777A"
GRID = "#D9D5CC"
BLUE = "#347A96"
GREEN = "#168064"
GOLD = "#D59A2F"
RED = "#C64F43"
PURPLE = "#76588F"

# Chronological order within the season, which is also the difficulty gradient.
TIER_ORDER = ["fall", "winter", "regionals", "nationals"]
TIER_LABELS = {
    "fall": "ACF Fall",
    "winter": "ACF Winter",
    "regionals": "ACF Regionals",
    "nationals": "ACF Nationals",
}
TIER_SHORT = {"fall": "Fall", "winter": "Winter", "regionals": "Regionals", "nationals": "Nationals"}
TIER_DATES = {
    "fall": "Oct 2024",
    "winter": "Nov 2024",
    "regionals": "Feb 2025",
    "nationals": "Apr 2025",
}
TIER_COLORS = {"fall": GOLD, "winter": PURPLE, "regionals": BLUE, "nationals": GREEN}
TIER_RANK = {tier: index for index, tier in enumerate(TIER_ORDER)}

CATEGORY_ORDER = [
    "History",
    "Literature",
    "Science",
    "Fine Arts",
    "Religion",
    "Philosophy",
    "Social Science",
    "Mythology",
    "Geography/Current Events",
    "Other Academic",
    "Pop Culture",
    "Unknown",
]
DIFFICULTY_ORDER = ["easy", "medium", "hard"]
DIFFICULTY_COLORS = {"easy": GREEN, "medium": GOLD, "hard": RED}

MIN_PLAYER_ATTEMPTS = 30
MIN_FIXED_SET_ATTEMPTS = 20
MIN_STABILITY_SCORED = 20
MIN_SPECIALTY_SCORED = 10


def load_table(data_dir: Path, name: str) -> pd.DataFrame:
    path = data_dir / name
    if not path.exists():
        raise FileNotFoundError(f"Missing {path}; build the tables described in data/README.md")
    return load_from_disk(str(path))["all"].to_pandas()


def clean_text(value: object) -> str:
    if value is None or (isinstance(value, float) and np.isnan(value)):
        return ""
    text = re.sub(r"<[^>]+>", "", str(value))
    return " ".join(html.unescape(text).split())


def normalize_category(value: object) -> str:
    category = clean_text(value).strip().rstrip(">").strip()
    aliases = {
        "": "Unknown",
        "Any History": "History",
        "Painting/Sculpture": "Fine Arts",
        "Painting & Sculpture": "Fine Arts",
        "Geography": "Geography/Current Events",
        "Current Events": "Geography/Current Events",
        "Current Events/Geography": "Geography/Current Events",
        "Popular Culture": "Pop Culture",
        "World/Other Literature": "Literature",
    }
    return aliases.get(category, category)


def season_from_date(start_date: object) -> str:
    """Season cut at July, so Fall/Winter join the following Regionals/Nationals."""
    stamp = pd.to_datetime(start_date, errors="coerce")
    if pd.isna(stamp):
        return "unknown"
    start_year = stamp.year if stamp.month >= 7 else stamp.year - 1
    return f"{start_year}-{str(start_year + 1)[-2:]}"


def short_site(name: str) -> str:
    text = re.sub(r"^\d{4} ACF (?:Fall|Regionals|Winter|Nationals)\s*(?:at|@)?\s*", "", str(name))
    return text if text else str(name)


def safe_divide(numerator: pd.Series, denominator: pd.Series) -> pd.Series:
    return numerator.astype(float).div(denominator.replace(0, np.nan))


def is_empty_value(value: object) -> bool:
    if value is None:
        return True
    if isinstance(value, str):
        return not value.strip()
    if isinstance(value, (list, tuple, np.ndarray)):
        return len(value) == 0
    return False


def clue_phase(position: int, boundaries: object, total_tokens: int) -> tuple[float, bool]:
    """Locate a token within its dataset-provided sentence/clue span.

    Positions are clipped for the 53 known overruns.  A phase of 1 is the final
    token of a span; ``at_boundary`` is stricter and only marks an explicit
    boundary supplied by the dataset.
    """
    total = max(int(total_tokens), 1)
    token = int(np.clip(position, 1, total))
    boundary_values = [] if is_empty_value(boundaries) else list(boundaries)
    ends = sorted(
        {
            min(int(value), total)
            for value in boundary_values
            if pd.notna(value) and int(value) > 0
        }
    )
    explicit_ends = set(ends)
    if not ends or ends[-1] < total:
        ends.append(total)
    start = 0
    for end in ends:
        if token <= end:
            return (token - start) / max(end - start, 1), token in explicit_ends
        start = end
    return 1.0, token in explicit_ends


def style_axis(axis: plt.Axes, grid_axis: str = "y") -> None:
    axis.set_facecolor(PAPER)
    axis.spines[["top", "right"]].set_visible(False)
    axis.spines[["left", "bottom"]].set_color(GRID)
    axis.tick_params(colors=MUTED, length=0, pad=5)
    axis.grid(axis=grid_axis, color=GRID, linewidth=0.8, alpha=0.7, zorder=0)


def save_figure(fig: plt.Figure, figures_dir: Path, name: str) -> None:
    fig.patch.set_facecolor(PAPER)
    fig.tight_layout()
    fig.savefig(figures_dir / name, dpi=180, facecolor=PAPER, bbox_inches="tight")
    plt.close(fig)


def tier_ticks(axis: plt.Axes, with_dates: bool = False) -> None:
    axis.set_xticks(np.arange(len(TIER_ORDER)))
    labels = [
        f"{TIER_SHORT[tier]}\n{TIER_DATES[tier]}" if with_dates else TIER_SHORT[tier]
        for tier in TIER_ORDER
    ]
    axis.set_xticklabels(labels, fontsize=9)


def tier_legend(axis: plt.Axes, **kwargs) -> None:
    handles = [
        Line2D([], [], color=TIER_COLORS[tier], marker="s", linestyle="none", label=TIER_LABELS[tier])
        for tier in TIER_ORDER
    ]
    axis.legend(handles=handles, frameon=False, labelcolor=MUTED, fontsize=8.5, **kwargs)


def legend_headroom(axis: plt.Axes, fraction: float = 0.18) -> None:
    """Raise the upper y-limit so a top-anchored legend sits over blank space.

    Panels that fill their whole plotting area — stacked bars, dense scatters —
    give `loc="best"` nowhere clean to land, so it drops the legend on top of
    the data. Reserving a band above the data first is more reliable than
    hunting for a free corner that does not exist.
    """
    bottom, top = axis.get_ylim()
    axis.set_ylim(bottom, bottom + (top - bottom) / (1.0 - fraction))


# ---------------------------------------------------------------------------
# Table preparation
# ---------------------------------------------------------------------------


def prepare_tables(data_dir: Path) -> dict[str, pd.DataFrame]:
    names = [
        "tournaments",
        "players",
        "teams",
        "games",
        "tossups",
        "bonuses",
        "tossup_buzzes",
        "bonus_responses",
    ]
    tables = {name: load_table(data_dir, name) for name in names}

    tournaments = tables["tournaments"].copy()
    tournaments["tier"] = tournaments["tier"].map(clean_text)
    tournaments["season"] = tournaments["start_date"].map(season_from_date)
    tournaments = tournaments[tournaments["season"] == SEASON].copy()
    if tournaments.empty:
        raise ValueError(f"No tournaments found for season {SEASON}")
    tournaments["tier_label"] = tournaments["tier"].map(TIER_LABELS)
    tournaments["site"] = tournaments["name"].map(short_site)
    tournaments["tier_rank"] = tournaments["tier"].map(TIER_RANK)
    tables["tournaments"] = tournaments

    site_ids = set(tournaments["tournament_id"])
    site_meta = tournaments[["tournament_id", "name", "site", "tier", "tier_label", "tier_rank"]]

    games = tables["games"]
    games = games[games["tournament_id"].isin(site_ids)].merge(site_meta, on="tournament_id", how="left")
    tables["games"] = games

    teams = tables["teams"]
    teams = teams[teams["tournament_id"].isin(site_ids)].copy()
    teams["roster_size"] = teams["player_ids"].map(len)
    teams = teams.merge(site_meta, on="tournament_id", how="left")
    tables["teams"] = teams

    # Question sets are scoped by the events these sites actually played.
    game_ids = set(games["game_id"])
    buzzes = tables["tossup_buzzes"]
    buzzes = buzzes[buzzes["game_id"].isin(game_ids)].copy()
    event_ids = set(buzzes["tossup_id"].str.rsplit("::", n=2).str[0])

    responses = tables["bonus_responses"]
    responses = responses[responses["game_id"].isin(game_ids)].copy()
    bonus_event_ids = set(responses["bonus_id"].str.rsplit("::", n=2).str[0])

    for name, keep in [("tossups", event_ids), ("bonuses", bonus_event_ids)]:
        frame = tables[name]
        frame = frame[frame["question_set_event_id"].isin(keep)].copy()
        frame["tier"] = frame["question_set_event_id"].map(
            lambda event: re.match(r"^\d{4}-acf-(fall|regionals|winter|nationals)", str(event)).group(1)
        )
        frame["tier_label"] = frame["tier"].map(TIER_LABELS)
        frame["tier_rank"] = frame["tier"].map(TIER_RANK)
        frame["category_raw"] = frame["category"].map(clean_text)
        frame["category_group"] = frame["category"].map(normalize_category)
        tables[name] = frame

    tossups = tables["tossups"]
    tossups["answer_clean"] = tossups["answer"].map(clean_text)
    tossups["num_tokens"] = tossups["tokens"].map(len)
    tossups["num_clues"] = tossups["sentence_boundaries"].map(len)

    bonuses = tables["bonuses"]
    bonuses["num_parts"] = bonuses["parts"].map(len)
    bonuses["leadin_tokens"] = bonuses["leadin"].map(lambda text: len(clean_text(text).split()))

    buzzes["position_raw_pct"] = 100 * safe_divide(buzzes["token_position"], buzzes["num_tokens_total"])
    buzzes["position_pct"] = buzzes["position_raw_pct"].clip(0, 100)
    buzzes["position_overrun"] = buzzes["token_position"] > buzzes["num_tokens_total"]
    buzzes["outcome"] = (
        buzzes["value"].map({10: "Correct (+10)", -5: "Neg (-5)", 0: "Zero (0)"}).fillna("Other")
    )
    buzzes["is_neg"] = buzzes["value"].eq(-5)
    buzzes["is_zero"] = buzzes["value"].eq(0)
    buzzes["is_scored"] = buzzes["value"].isin([10, -5])
    buzzes["_buzz_order"] = buzzes["buzz_id"].str.rsplit("-", n=1).str[-1].astype(int)
    first_buzz_ids = set(
        buzzes.sort_values(["game_id", "tossup_id", "token_position", "_buzz_order"])
        .drop_duplicates(["game_id", "tossup_id"])["buzz_id"]
    )
    buzzes["is_first_buzz"] = buzzes["buzz_id"].isin(first_buzz_ids)
    buzzes["is_early"] = buzzes["position_pct"].lt(50)
    buzzes["is_very_late"] = buzzes["position_pct"].ge(90)
    buzzes["timing_quartile"] = pd.cut(
        buzzes["position_pct"],
        [0, 25, 50, 75, 100],
        labels=["0–25%", "25–50%", "50–75%", "75–100%"],
        include_lowest=True,
        right=False,
    )
    buzzes = buzzes.merge(
        tossups[["tossup_id", "question_set_event_id", "category_group", "num_tokens", "num_clues"]],
        on="tossup_id",
        how="left",
    )
    buzzes = buzzes.merge(
        games[["game_id", "tournament_id", "site", "tier", "tier_label", "tier_rank"]],
        on="game_id",
        how="left",
    )
    buzzes = buzzes.merge(teams[["team_id", "team_name", "roster_size"]], on="team_id", how="left")
    tables["tossup_buzzes"] = buzzes

    responses = responses.merge(
        bonuses[["bonus_id", "question_set_event_id", "category_group", "parts"]],
        on="bonus_id",
        how="left",
    )
    responses = responses.merge(
        games[["game_id", "tournament_id", "site", "tier", "tier_label", "tier_rank"]],
        on="game_id",
        how="left",
    )
    responses = responses.merge(teams[["team_id", "team_name", "roster_size"]], on="team_id", how="left")
    responses["perfect_bonus"] = responses["total_points"].eq(30)
    responses["zero_bonus"] = responses["total_points"].eq(0)
    responses["parts_correct_count"] = responses["parts_correct"].map(
        lambda flags: int(sum(bool(flag) for flag in flags))
    )
    responses["has_earning_player"] = ~responses["earning_player_id"].map(is_empty_value)
    tables["bonus_responses"] = responses

    part_rows: list[dict[str, object]] = []
    for row in responses.itertuples(index=False):
        parts = list(row.parts) if row.parts is not None else []
        correctness = list(row.parts_correct)
        for index, part in enumerate(parts):
            part_rows.append(
                {
                    "response_id": row.response_id,
                    "bonus_id": row.bonus_id,
                    "team_id": row.team_id,
                    "tier": row.tier,
                    "tier_label": row.tier_label,
                    "category_group": row.category_group,
                    "part_number": index + 1,
                    "difficulty": clean_text(part.get("difficulty", "")) or f"part-{index + 1}",
                    "correct": bool(correctness[index]) if index < len(correctness) else False,
                }
            )
    tables["bonus_parts"] = pd.DataFrame(part_rows)

    players = tables["players"]
    tables["players"] = players[players["player_id"].isin(set(buzzes["player_id"]))].copy()
    return tables


def build_team_games(games: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for game in games.itertuples(index=False):
        team_ids = list(game.team_ids)
        scores = list(game.final_scores)
        if len(team_ids) != 2 or len(scores) != 2:
            continue
        for side in [0, 1]:
            rows.append(
                {
                    "game_id": game.game_id,
                    "tournament_id": game.tournament_id,
                    "tier": game.tier,
                    "tier_label": game.tier_label,
                    "site": game.site,
                    "team_id": team_ids[side],
                    "opponent_team_id": team_ids[1 - side],
                    "score": int(scores[side]),
                    "opponent_score": int(scores[1 - side]),
                    "margin": int(scores[side]) - int(scores[1 - side]),
                    "win": scores[side] > scores[1 - side],
                    "loss": scores[side] < scores[1 - side],
                    "tie": scores[side] == scores[1 - side],
                    "tossups_read": game.tossups_read,
                }
            )
    return pd.DataFrame(rows)


# ---------------------------------------------------------------------------
# Aggregation
# ---------------------------------------------------------------------------


def _buzz_aggregate(frame: pd.DataFrame, keys: list[str]) -> pd.DataFrame:
    grouped = frame.groupby(keys, observed=True).agg(
        buzz_events=("buzz_id", "size"),
        correct=("correct", "sum"),
        negs=("is_neg", "sum"),
        zeros=("is_zero", "sum"),
        scored=("is_scored", "sum"),
        mean_position_pct=("position_pct", "mean"),
        median_position_pct=("position_pct", "median"),
        early_share=("is_early", "mean"),
        very_late_share=("is_very_late", "mean"),
    )
    grouped["accuracy_all_attempts"] = safe_divide(grouped["correct"], grouped["buzz_events"])
    grouped["scored_accuracy"] = safe_divide(grouped["correct"], grouped["scored"])
    grouped["neg_rate"] = safe_divide(grouped["negs"], grouped["buzz_events"])
    grouped["zero_rate"] = safe_divide(grouped["zeros"], grouped["buzz_events"])
    return grouped.reset_index()


def _bonus_aggregate(frame: pd.DataFrame, keys: list[str]) -> pd.DataFrame:
    grouped = frame.groupby(keys, observed=True).agg(
        bonuses_heard=("response_id", "size"),
        ppb=("total_points", "mean"),
        perfect_bonus_rate=("perfect_bonus", "mean"),
        zero_bonus_rate=("zero_bonus", "mean"),
        mean_parts_correct=("parts_correct_count", "mean"),
    )
    return grouped.reset_index()


def aggregate_outputs(tables: dict[str, pd.DataFrame]) -> dict[str, pd.DataFrame]:
    tournaments = tables["tournaments"]
    teams = tables["teams"]
    games = tables["games"]
    tossups = tables["tossups"]
    bonuses = tables["bonuses"]
    buzzes = tables["tossup_buzzes"]
    responses = tables["bonus_responses"]
    parts = tables["bonus_parts"]

    outputs: dict[str, pd.DataFrame] = {}
    team_games = build_team_games(games).merge(
        teams[["team_id", "team_name", "roster_size"]], on="team_id", how="left"
    )
    outputs["team_game_results"] = team_games

    # --- tier (chronological) structure -----------------------------------
    tier_summary = pd.DataFrame({"tier": TIER_ORDER})
    tier_summary["tier_label"] = tier_summary["tier"].map(TIER_LABELS)
    tier_summary["date"] = tier_summary["tier"].map(TIER_DATES)
    tier_summary["start_date"] = tier_summary["tier"].map(
        tournaments.groupby("tier")["start_date"].min()
    )
    for label, frame, column in [
        ("tournament_sites", tournaments, "tournament_id"),
        ("teams", teams, "team_id"),
        ("games", games, "game_id"),
        ("tossup_questions", tossups, "tossup_id"),
        ("bonus_questions", bonuses, "bonus_id"),
    ]:
        tier_summary[label] = tier_summary["tier"].map(
            frame.groupby("tier", observed=True)[column].nunique()
        ).fillna(0).astype(int)
    tier_summary["player_ids"] = tier_summary["tier"].map(
        buzzes.groupby("tier", observed=True)["player_id"].nunique()
    )
    tier_summary["roster_memberships"] = tier_summary["tier"].map(
        teams.explode("player_ids").groupby("tier", observed=True)["player_ids"].size()
    )
    tier_summary = tier_summary.merge(_buzz_aggregate(buzzes, ["tier"]), on="tier", how="left")
    tier_summary = tier_summary.merge(_bonus_aggregate(responses, ["tier"]), on="tier", how="left")
    tier_summary["mean_team_score"] = tier_summary["tier"].map(team_games.groupby("tier")["score"].mean())
    tier_summary["median_abs_margin"] = tier_summary["tier"].map(
        team_games.groupby("tier")["margin"].apply(lambda values: values.abs().median())
    )
    outputs["tier_summary"] = tier_summary

    # --- sites --------------------------------------------------------------
    site_summary = tournaments[
        ["tournament_id", "name", "site", "tier", "tier_label", "num_packets", "level", "start_date"]
    ].copy()
    site_summary = site_summary.merge(_buzz_aggregate(buzzes, ["tournament_id"]), on="tournament_id", how="left")
    site_summary = site_summary.merge(_bonus_aggregate(responses, ["tournament_id"]), on="tournament_id", how="left")
    for label, frame, column in [("teams", teams, "team_id"), ("games", games, "game_id")]:
        site_summary[label] = site_summary["tournament_id"].map(
            frame.groupby("tournament_id")[column].nunique()
        )
    site_summary["mean_tossups_read"] = site_summary["tournament_id"].map(
        games.groupby("tournament_id")["tossups_read"].mean()
    )
    site_summary["mean_team_score"] = site_summary["tournament_id"].map(
        team_games.groupby("tournament_id")["score"].mean()
    )
    site_summary["median_abs_margin"] = site_summary["tournament_id"].map(
        team_games.groupby("tournament_id")["margin"].apply(lambda values: values.abs().median())
    )
    outputs["site_summary"] = site_summary

    # --- teams --------------------------------------------------------------
    team_summary = teams[
        ["team_id", "team_name", "tournament_id", "site", "tier", "tier_label", "roster_size"]
    ].copy()
    team_summary = team_summary.merge(_buzz_aggregate(buzzes, ["team_id"]), on="team_id", how="left")
    team_summary = team_summary.merge(_bonus_aggregate(responses, ["team_id"]), on="team_id", how="left")
    for label, series in [
        ("games", team_games.groupby("team_id")["game_id"].nunique()),
        ("wins", team_games.groupby("team_id")["win"].sum()),
        ("points_per_game", team_games.groupby("team_id")["score"].mean()),
        ("mean_margin", team_games.groupby("team_id")["margin"].mean()),
    ]:
        team_summary[label] = team_summary["team_id"].map(series)
    team_summary["win_rate"] = safe_divide(team_summary["wins"], team_summary["games"])
    outputs["team_summary"] = team_summary

    # --- players ------------------------------------------------------------
    player_summary = _buzz_aggregate(buzzes, ["player_id"])
    for label, series in [
        ("tournaments", buzzes.groupby("player_id")["tournament_id"].nunique()),
        ("games", buzzes.groupby("player_id")["game_id"].nunique()),
        ("tiers_played", buzzes.groupby("player_id")["tier"].nunique()),
        ("points_per_attempt", buzzes.groupby("player_id")["value"].mean()),
    ]:
        player_summary[label] = player_summary["player_id"].map(series)
    entry_rank = buzzes.groupby("player_id")["tier_rank"].min()
    exit_rank = buzzes.groupby("player_id")["tier_rank"].max()
    player_summary["entry_tier"] = player_summary["player_id"].map(entry_rank).map(
        lambda rank: TIER_ORDER[int(rank)]
    )
    player_summary["furthest_tier"] = player_summary["player_id"].map(exit_rank).map(
        lambda rank: TIER_ORDER[int(rank)]
    )
    outputs["player_summary"] = player_summary

    outputs["player_tier_summary"] = _buzz_aggregate(buzzes, ["player_id", "tier"])

    # --- within-season progression -----------------------------------------
    tier_players = {tier: set(buzzes.loc[buzzes["tier"] == tier, "player_id"]) for tier in TIER_ORDER}

    retention_rows: list[dict[str, object]] = []
    for source in TIER_ORDER:
        for target in TIER_ORDER:
            overlap = len(tier_players[source] & tier_players[target])
            retention_rows.append(
                {
                    "from_tier": source,
                    "to_tier": target,
                    "from_player_ids": len(tier_players[source]),
                    "overlap": overlap,
                    "share_of_from": overlap / len(tier_players[source]) if tier_players[source] else np.nan,
                }
            )
    outputs["player_retention"] = pd.DataFrame(retention_rows)

    composition_rows: list[dict[str, object]] = []
    for index, tier in enumerate(TIER_ORDER):
        prior: set[str] = set()
        for earlier in TIER_ORDER[:index]:
            prior |= tier_players[earlier]
        subset = buzzes[buzzes["tier"] == tier]
        seen = subset["player_id"].isin(prior)
        composition_rows.append(
            {
                "tier": tier,
                "tier_label": TIER_LABELS[tier],
                "player_ids": len(tier_players[tier]),
                "seen_earlier_ids": len(tier_players[tier] & prior),
                "seen_earlier_id_share": (
                    len(tier_players[tier] & prior) / len(tier_players[tier]) if tier_players[tier] else np.nan
                ),
                "buzz_events": len(subset),
                "seen_earlier_buzz_share": float(seen.mean()) if len(subset) else np.nan,
            }
        )
    outputs["field_composition"] = pd.DataFrame(composition_rows)

    # Selection measured on a fixed question set: among players with enough
    # attempts on one tier's set, how does their performance *on that set* vary
    # with how far they later go?  Holding the set fixed removes the difficulty
    # confound that spoils any cross-tier performance comparison.
    selection_rows: list[dict[str, object]] = []
    for tier in TIER_ORDER[:-1]:
        subset = buzzes[buzzes["tier"] == tier]
        per_player = subset.groupby("player_id").agg(
            attempts=("buzz_id", "size"),
            correct=("correct", "sum"),
            scored=("is_scored", "sum"),
            mean_position_pct=("position_pct", "mean"),
        )
        per_player = per_player[per_player["attempts"] >= MIN_FIXED_SET_ATTEMPTS]
        per_player["scored_accuracy"] = safe_divide(per_player["correct"], per_player["scored"])
        per_player["furthest_rank"] = per_player.index.map(exit_rank)
        for rank, group in per_player.groupby("furthest_rank"):
            selection_rows.append(
                {
                    "fixed_set_tier": tier,
                    "furthest_tier": TIER_ORDER[int(rank)],
                    "players": len(group),
                    "mean_scored_accuracy": float(group["scored_accuracy"].mean()),
                    "mean_position_pct": float(group["mean_position_pct"].mean()),
                }
            )
    outputs["selection_on_fixed_set"] = pd.DataFrame(selection_rows)

    # --- diagnostics for CompIRT parameterization -------------------------
    # Question-center scored attempts before comparing the same player across
    # tiers.  This removes each question's raw timing/correctness level and
    # turns the correlations into descriptive stability checks for player
    # parameters rather than comparisons of different sets.
    scored_buzzes = buzzes[buzzes["is_scored"]].copy()
    scored_buzzes["timing_residual"] = scored_buzzes["position_pct"] - scored_buzzes.groupby(
        "tossup_id"
    )["position_pct"].transform("mean")
    scored_buzzes["correctness_residual"] = scored_buzzes["correct"].astype(float) - scored_buzzes.groupby(
        "tossup_id"
    )["correct"].transform("mean")
    player_tier_residuals = (
        scored_buzzes.groupby(["player_id", "tier"], observed=True)
        .agg(
            scored_attempts=("buzz_id", "size"),
            mean_timing_residual=("timing_residual", "mean"),
            mean_correctness_residual=("correctness_residual", "mean"),
        )
        .reset_index()
    )
    stability_rows: list[dict[str, object]] = []
    for source, target in zip(TIER_ORDER[:-1], TIER_ORDER[1:]):
        left = player_tier_residuals.query(
            "tier == @source and scored_attempts >= @MIN_STABILITY_SCORED"
        )
        right = player_tier_residuals.query(
            "tier == @target and scored_attempts >= @MIN_STABILITY_SCORED"
        )
        paired = left.merge(right, on="player_id", suffixes=("_source", "_target"))
        stability_rows.append(
            {
                "source_tier": source,
                "target_tier": target,
                "minimum_scored_attempts_per_tier": MIN_STABILITY_SCORED,
                "players": len(paired),
                "timing_residual_correlation": paired["mean_timing_residual_source"].corr(
                    paired["mean_timing_residual_target"]
                ),
                "correctness_residual_correlation": paired[
                    "mean_correctness_residual_source"
                ].corr(paired["mean_correctness_residual_target"]),
            }
        )
    outputs["player_parameter_stability"] = pd.DataFrame(stability_rows)

    # Test whether category-specific player deviations recur in the second
    # half of the season after removing question difficulty and each player's
    # general level in that half.  This is a direct diagnostic for whether a
    # multidimensional skill effect is more useful in the hazard or correctness
    # branch.  Threshold sensitivity is exported instead of selecting one
    # convenient cutoff after seeing the result.
    scored_buzzes["season_half"] = np.where(
        scored_buzzes["tier"].isin(TIER_ORDER[:2]), "Fall + Winter", "Regionals + Nationals"
    )
    specialty_rows: list[dict[str, object]] = []
    for minimum in [5, 8, 10, 15]:
        row: dict[str, object] = {"minimum_scored_attempts_per_category_half": minimum}
        for metric in ["timing", "correctness"]:
            residual = f"{metric}_residual"
            cells = (
                scored_buzzes.groupby(
                    ["season_half", "player_id", "category_group"], observed=True
                )
                .agg(scored_attempts=("buzz_id", "size"), category_residual=(residual, "mean"))
                .reset_index()
            )
            player_level = scored_buzzes.groupby(["season_half", "player_id"], observed=True)[
                residual
            ].mean()
            cells = cells.join(player_level.rename("player_residual"), on=["season_half", "player_id"])
            cells["specialty"] = cells["category_residual"] - cells["player_residual"]
            early = cells.query(
                "season_half == 'Fall + Winter' and scored_attempts >= @minimum"
            )
            late = cells.query(
                "season_half == 'Regionals + Nationals' and scored_attempts >= @minimum"
            )
            paired = early.merge(late, on=["player_id", "category_group"], suffixes=("_early", "_late"))
            row[f"{metric}_player_category_cells"] = len(paired)
            row[f"{metric}_players"] = paired["player_id"].nunique()
            row[f"{metric}_specialty_correlation"] = paired["specialty_early"].corr(
                paired["specialty_late"]
            )
            if minimum == MIN_SPECIALTY_SCORED:
                paired["metric"] = metric
                specialty_rows.extend(paired.to_dict("records"))
        outputs.setdefault("category_specialization_stability", pd.DataFrame())
        sensitivity = outputs.setdefault("category_specialization_sensitivity", pd.DataFrame())
        outputs["category_specialization_sensitivity"] = pd.concat(
            [sensitivity, pd.DataFrame([row])], ignore_index=True
        )
    outputs["category_specialization_stability"] = pd.DataFrame(specialty_rows)

    # --- categories ---------------------------------------------------------
    category = _buzz_aggregate(buzzes, ["category_group"])
    category = category.merge(_bonus_aggregate(responses, ["category_group"]), on="category_group", how="outer")
    category["tossup_questions"] = category["category_group"].map(
        tossups.groupby("category_group")["tossup_id"].nunique()
    )
    category["bonus_questions"] = category["category_group"].map(
        bonuses.groupby("category_group")["bonus_id"].nunique()
    )
    outputs["category_summary"] = category

    category_tier = _buzz_aggregate(buzzes, ["tier", "category_group"])
    category_tier["tossup_questions"] = category_tier.set_index(["tier", "category_group"]).index.map(
        tossups.groupby(["tier", "category_group"])["tossup_id"].nunique()
    )
    outputs["category_by_tier"] = category_tier

    # --- questions ----------------------------------------------------------
    tossup_question = tossups[
        [
            "tossup_id",
            "question_set_event_id",
            "tier",
            "tier_label",
            "category_group",
            "num_tokens",
            "num_clues",
            "answer_clean",
        ]
    ].merge(_buzz_aggregate(buzzes, ["tossup_id"]), on="tossup_id", how="left")
    tossup_question["mean_scored_position_pct"] = tossup_question["tossup_id"].map(
        buzzes[buzzes["is_scored"]].groupby("tossup_id")["position_pct"].mean()
    )
    tossup_question["conversion_rate"] = tossup_question["accuracy_all_attempts"]
    outputs["tossup_question_summary"] = tossup_question

    outputs["bonus_question_summary"] = bonuses[
        ["bonus_id", "question_set_event_id", "tier", "tier_label", "category_group", "num_parts", "leadin_tokens"]
    ].merge(_bonus_aggregate(responses, ["bonus_id"]), on="bonus_id", how="left")

    part_summary = (
        parts.groupby(["tier", "difficulty"], observed=True)
        .agg(observations=("correct", "size"), conversion=("correct", "mean"))
        .reset_index()
    )
    part_summary["tier_label"] = part_summary["tier"].map(TIER_LABELS)
    outputs["bonus_part_summary"] = part_summary

    # --- timing -------------------------------------------------------------
    decile = buzzes.copy()
    decile["position_decile"] = pd.cut(
        decile["position_pct"], np.arange(0, 101, 10), include_lowest=True, right=False
    )
    position_deciles = (
        decile.groupby(["tier", "position_decile"], observed=False)
        .agg(
            buzz_events=("buzz_id", "size"),
            correct=("correct", "sum"),
            negs=("is_neg", "sum"),
            zeros=("is_zero", "sum"),
            scored=("is_scored", "sum"),
        )
        .reset_index()
    )
    position_deciles["midpoint_pct"] = position_deciles["position_decile"].map(lambda x: float(x.mid))
    position_deciles["accuracy"] = safe_divide(position_deciles["correct"], position_deciles["buzz_events"])
    position_deciles["scored_accuracy"] = safe_divide(position_deciles["correct"], position_deciles["scored"])
    position_deciles["neg_rate"] = safe_divide(position_deciles["negs"], position_deciles["buzz_events"])
    position_deciles["zero_rate"] = safe_divide(position_deciles["zeros"], position_deciles["buzz_events"])
    outputs["position_decile_summary"] = position_deciles

    pooled = (
        decile.groupby("position_decile", observed=False)
        .agg(
            buzz_events=("buzz_id", "size"),
            correct=("correct", "sum"),
            negs=("is_neg", "sum"),
            zeros=("is_zero", "sum"),
            scored=("is_scored", "sum"),
        )
        .reset_index()
    )
    pooled["midpoint_pct"] = pooled["position_decile"].map(lambda x: float(x.mid))
    pooled["accuracy"] = safe_divide(pooled["correct"], pooled["buzz_events"])
    pooled["scored_accuracy"] = safe_divide(pooled["correct"], pooled["scored"])
    pooled["neg_rate"] = safe_divide(pooled["negs"], pooled["buzz_events"])
    pooled["zero_rate"] = safe_divide(pooled["zeros"], pooled["buzz_events"])
    outputs["position_decile_pooled"] = pooled

    timing_band = (
        buzzes.groupby(["tier", "timing_quartile"], observed=False)
        .agg(
            buzz_events=("buzz_id", "size"),
            correct=("correct", "sum"),
            negs=("is_neg", "sum"),
            zeros=("is_zero", "sum"),
        )
        .reset_index()
    )
    timing_band["accuracy"] = safe_divide(timing_band["correct"], timing_band["buzz_events"])
    timing_band["neg_rate"] = safe_divide(timing_band["negs"], timing_band["buzz_events"])
    timing_band["zero_rate"] = safe_divide(timing_band["zeros"], timing_band["buzz_events"])
    outputs["timing_band_summary"] = timing_band

    outcome = (
        buzzes.groupby(["tier", "outcome"], observed=True)
        .agg(buzz_events=("buzz_id", "size"), median_position_pct=("position_pct", "median"))
        .reset_index()
    )
    outcome["share_within_tier"] = outcome["buzz_events"] / outcome.groupby("tier")["buzz_events"].transform("sum")
    outputs["outcome_summary"] = outcome

    # Buzzes are not spread uniformly within clues: test the observed phase of
    # scored buzzes against the token opportunities in those same questions.
    # The opportunity baseline is deliberately descriptive, not a fitted
    # survival null, and therefore does not claim that token hazards are flat.
    tossup_lookup = tossups.set_index("tossup_id")
    phase_rows: list[dict[str, object]] = []
    boundary_rows: list[dict[str, object]] = []
    phase_edges = np.linspace(0, 1, 11)
    phase_groups = [
        ("Correct (+10)", buzzes["value"].eq(10)),
        ("Neg (-5)", buzzes["value"].eq(-5)),
        ("All scored", buzzes["is_scored"]),
        ("Phase-0 first buzz", buzzes["is_scored"] & buzzes["is_first_buzz"]),
    ]
    for outcome_label, mask in phase_groups:
        subset = buzzes[mask]
        observed = np.zeros(10, dtype=float)
        expected = np.zeros(10, dtype=float)
        observed_boundaries = 0
        expected_boundaries = 0.0
        for tossup_id, count in subset["tossup_id"].value_counts().items():
            question = tossup_lookup.loc[tossup_id]
            total = int(question["num_tokens"])
            boundaries = question["sentence_boundaries"]
            positions = subset.loc[subset["tossup_id"].eq(tossup_id), "token_position"]
            observed_info = [clue_phase(value, boundaries, total) for value in positions]
            observed_bins = np.minimum(
                (np.asarray([value[0] for value in observed_info]) * 10).astype(int), 9
            )
            observed += np.bincount(observed_bins, minlength=10)
            observed_boundaries += sum(value[1] for value in observed_info)

            opportunity_info = [clue_phase(value, boundaries, total) for value in range(1, total + 1)]
            opportunity_bins = np.minimum(
                (np.asarray([value[0] for value in opportunity_info]) * 10).astype(int), 9
            )
            expected += count * np.bincount(opportunity_bins, minlength=10) / total
            expected_boundaries += count * sum(value[1] for value in opportunity_info) / total
        for index in range(10):
            phase_rows.append(
                {
                    "outcome": outcome_label,
                    "phase_start": phase_edges[index],
                    "phase_end": phase_edges[index + 1],
                    "observed_buzzes": int(observed[index]),
                    "observed_share": observed[index] / observed.sum(),
                    "uniform_expected_buzzes": expected[index],
                    "uniform_expected_share": expected[index] / expected.sum(),
                    "enrichment": (observed[index] / observed.sum()) / (expected[index] / expected.sum()),
                }
            )
        boundary_rows.append(
            {
                "outcome": outcome_label,
                "buzzes": len(subset),
                "at_exact_boundary": int(observed_boundaries),
                "observed_boundary_share": observed_boundaries / len(subset),
                "uniform_expected_boundary_share": expected_boundaries / len(subset),
                "boundary_enrichment": observed_boundaries / expected_boundaries,
            }
        )
    outputs["clue_phase_summary"] = pd.DataFrame(phase_rows)
    outputs["clue_boundary_summary"] = pd.DataFrame(boundary_rows)

    # A shared hazard/correctness curve implies closely coupled question-level
    # timing, no-buzz, and conditional-correctness signals.  Export their raw
    # correlations within tier (plus pooled) to show how much coupling the data
    # actually contain before fitting either model family.
    question_rows: list[dict[str, object]] = []
    question_summary = outputs["tossup_question_summary"]
    for tier, frame in [("pooled", question_summary)] + [
        (tier, question_summary[question_summary["tier"].eq(tier)]) for tier in TIER_ORDER
    ]:
        question_rows.append(
            {
                "tier": tier,
                "questions": len(frame),
                "mean_scored_position_vs_scored_accuracy": frame["mean_scored_position_pct"].corr(
                    frame["scored_accuracy"]
                ),
                "zero_rate_vs_scored_accuracy": frame["zero_rate"].corr(frame["scored_accuracy"]),
                "mean_scored_position_vs_zero_rate": frame["mean_scored_position_pct"].corr(
                    frame["zero_rate"]
                ),
                "mean_scored_position_vs_all_attempt_accuracy": frame["mean_scored_position_pct"].corr(
                    frame["accuracy_all_attempts"]
                ),
            }
        )
    outputs["question_signal_correlations"] = pd.DataFrame(question_rows)

    # --- missingness --------------------------------------------------------
    missing_rows: list[dict[str, object]] = []
    for table_name, frame, columns in [
        ("tossups", tossups, ["category", "subcategory", "answer", "tokens", "sentence_boundaries"]),
        ("bonuses", bonuses, ["category", "subcategory", "leadin", "parts"]),
        ("bonus_responses", responses, ["earning_player_id"]),
        ("teams", teams, ["team_name", "player_ids"]),
        ("tournaments", tournaments, ["level", "location", "start_date", "end_date"]),
    ]:
        for column in columns:
            if column not in frame.columns:
                continue
            empty = frame[column].map(is_empty_value)
            missing_rows.append(
                {
                    "table": table_name,
                    "field": column,
                    "rows": len(frame),
                    "missing": int(empty.sum()),
                    "missing_rate": float(empty.mean()),
                }
            )
    outputs["missingness_summary"] = pd.DataFrame(missing_rows)

    metric_columns = [
        "accuracy_all_attempts",
        "scored_accuracy",
        "neg_rate",
        "zero_rate",
        "mean_position_pct",
        "early_share",
        "ppb",
        "perfect_bonus_rate",
        "zero_bonus_rate",
        "points_per_game",
        "win_rate",
        "mean_margin",
    ]
    stable = team_summary.query("games >= 5 and buzz_events >= 30 and bonuses_heard >= 15")
    outputs["team_metric_correlations"] = stable[metric_columns].corr().reset_index().rename(
        columns={"index": "metric"}
    )
    return outputs


# ---------------------------------------------------------------------------
# MDS
# ---------------------------------------------------------------------------


def classical_mds(
    frame: pd.DataFrame, feature_columns: list[str], id_columns: list[str]
) -> tuple[pd.DataFrame, pd.DataFrame, float, float]:
    work = frame[id_columns + feature_columns].copy()
    raw_features = work[feature_columns].apply(pd.to_numeric, errors="coerce")
    imputed = raw_features.fillna(raw_features.median())
    standardized = (imputed - imputed.mean()) / imputed.std(ddof=0).replace(0, 1)
    x = standardized.to_numpy(float)
    squared = ((x[:, None, :] - x[None, :, :]) ** 2).sum(axis=2)
    n = len(x)
    centering = np.eye(n) - np.ones((n, n)) / n
    gram = -0.5 * centering @ squared @ centering
    eigenvalues, eigenvectors = np.linalg.eigh(gram)
    order = np.argsort(eigenvalues)[::-1]
    positive = np.maximum(eigenvalues[order[:2]], 0)
    coordinates = eigenvectors[:, order[:2]] * np.sqrt(positive)
    original = np.sqrt(np.maximum(squared, 0))
    embedded = np.sqrt(((coordinates[:, None, :] - coordinates[None, :, :]) ** 2).sum(axis=2))
    upper = np.triu_indices(n, 1)
    stress = float(
        np.sqrt(np.sum((original[upper] - embedded[upper]) ** 2) / np.sum(original[upper] ** 2))
    )
    total = float(np.sum(np.maximum(eigenvalues, 0)))
    variance_explained = float(np.sum(positive) / total) if total > 0 else np.nan
    coordinates_frame = work[id_columns].copy()
    coordinates_frame["mds1"] = coordinates[:, 0]
    coordinates_frame["mds2"] = coordinates[:, 1]
    feature_frame = pd.concat([work[id_columns], raw_features.add_prefix("raw_")], axis=1)
    for column in feature_columns:
        feature_frame[f"z_{column}"] = standardized[column]
    return coordinates_frame, feature_frame, stress, variance_explained


TEAM_MDS_FEATURES = [
    "accuracy_all_attempts",
    "scored_accuracy",
    "neg_rate",
    "zero_rate",
    "mean_position_pct",
    "early_share",
    "very_late_share",
    "ppb",
    "perfect_bonus_rate",
    "zero_bonus_rate",
    "points_per_game",
    "mean_margin",
]
SITE_MDS_FEATURES = [
    "accuracy_all_attempts",
    "neg_rate",
    "zero_rate",
    "median_position_pct",
    "ppb",
    "perfect_bonus_rate",
    "zero_bonus_rate",
    "mean_team_score",
    "median_abs_margin",
    "mean_tossups_read",
]


def add_mds(outputs: dict[str, pd.DataFrame]) -> dict[str, float]:
    stats: dict[str, float] = {}
    eligible = outputs["team_summary"].query("games >= 5 and buzz_events >= 30 and bonuses_heard >= 15")
    team_coords, team_features, team_stress, team_variance = classical_mds(
        eligible, TEAM_MDS_FEATURES, ["team_id", "team_name", "tournament_id", "site", "tier", "tier_label"]
    )
    outputs["team_mds_coordinates"] = team_coords
    outputs["team_mds_features"] = team_features
    stats["team_stress_1"] = team_stress
    stats["team_variance_explained"] = team_variance
    stats["team_points"] = float(len(team_coords))

    site_coords, site_features, site_stress, site_variance = classical_mds(
        outputs["site_summary"], SITE_MDS_FEATURES, ["tournament_id", "name", "site", "tier", "tier_label"]
    )
    outputs["site_mds_coordinates"] = site_coords
    outputs["site_mds_features"] = site_features
    stats["site_stress_1"] = site_stress
    stats["site_variance_explained"] = site_variance
    stats["site_points"] = float(len(site_coords))

    # No event-grain MDS here: the season has only four question-set events, and
    # a two-dimensional embedding of four points is near-exact by construction,
    # so it would carry no information.  The nine-event map in
    # analysis/full_dataset_eda covers that question.
    for kind, key, coords, features, columns in [
        ("team", "team_id", team_coords, team_features, TEAM_MDS_FEATURES),
        ("site", "tournament_id", site_coords, site_features, SITE_MDS_FEATURES),
    ]:
        merged = coords[[key, "mds1", "mds2"]].merge(features, on=key, how="inner")
        outputs[f"{kind}_mds_loadings"] = pd.DataFrame(
            [
                {
                    "feature": column,
                    "mds1": merged[f"z_{column}"].corr(merged["mds1"]),
                    "mds2": merged[f"z_{column}"].corr(merged["mds2"]),
                }
                for column in columns
            ]
        )
    return stats


# ---------------------------------------------------------------------------
# Output writing
# ---------------------------------------------------------------------------


def write_outputs(
    output_dir: Path,
    tables: dict[str, pd.DataFrame],
    outputs: dict[str, pd.DataFrame],
    mds_stats: dict[str, float],
) -> None:
    data_dir = output_dir / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    for name, frame in outputs.items():
        export = frame.copy()
        for column in export.columns:
            if isinstance(export[column].dtype, pd.CategoricalDtype):
                export[column] = export[column].astype(str)
        export.to_csv(data_dir / f"{name}.csv", index=False, float_format="%.6f")

    tournaments = tables["tournaments"]
    teams = tables["teams"]
    buzzes = tables["tossup_buzzes"]
    responses = tables["bonus_responses"]
    tossups = tables["tossups"]
    bonuses = tables["bonuses"]
    composition = outputs["field_composition"].set_index("tier")

    summary_rows = [
        ("season", SEASON),
        ("tiers", ";".join(TIER_ORDER)),
        ("date_range", f"{tournaments['start_date'].min()} to {tournaments['start_date'].max()}"),
        ("tournament_sites", len(tournaments)),
        ("question_set_events", tossups["question_set_event_id"].nunique()),
        ("teams", len(teams)),
        ("roster_memberships", int(teams["roster_size"].sum())),
        ("normalized_player_ids_with_buzz", buzzes["player_id"].nunique()),
        ("games", len(tables["games"])),
        ("tossup_questions", len(tossups)),
        ("bonus_questions", len(bonuses)),
        ("buzz_events", len(buzzes)),
        ("correct_buzzes", int(buzzes["correct"].sum())),
        ("negs", int(buzzes["is_neg"].sum())),
        ("zero_value_attempts", int(buzzes["is_zero"].sum())),
        ("bonus_responses", len(responses)),
        ("bonus_part_observations", len(tables["bonus_parts"])),
        ("category_missing_tossups", int(tossups["category_group"].eq("Unknown").sum())),
        ("category_missing_bonuses", int(bonuses["category_group"].eq("Unknown").sum())),
        ("bonus_responses_without_earning_player", int((~responses["has_earning_player"]).sum())),
        ("buzz_position_overruns", int(buzzes["position_overrun"].sum())),
        ("players_in_one_tier_only", int(outputs["player_summary"]["tiers_played"].eq(1).sum())),
        ("players_in_all_four_tiers", int(outputs["player_summary"]["tiers_played"].eq(4).sum())),
        ("nationals_seen_earlier_buzz_share", round(float(composition.loc["nationals", "seen_earlier_buzz_share"]), 6)),
        ("team_mds_stress_1", round(mds_stats["team_stress_1"], 6)),
        ("site_mds_stress_1", round(mds_stats["site_stress_1"], 6)),
    ]
    pd.DataFrame(summary_rows, columns=["metric", "value"]).to_csv(
        data_dir / "dataset_summary.csv", index=False
    )

    validation = {
        "scope": {
            "season": SEASON,
            "sites_33": len(tournaments) == 33,
            "all_four_tiers_present": sorted(tournaments["tier"].unique()) == sorted(TIER_ORDER),
            "events_4": tossups["question_set_event_id"].nunique() == 4,
            "buzzes_64037": len(buzzes) == 64037,
        },
        "referential_checks": {
            "all_buzz_games_resolved": bool(buzzes["tournament_id"].notna().all()),
            "all_buzz_tossups_resolved": bool(buzzes["category_group"].notna().all()),
            "all_bonus_games_resolved": bool(responses["tournament_id"].notna().all()),
            "two_teams_per_game": bool(tables["games"]["team_ids"].map(len).eq(2).all()),
            "two_scores_per_game": bool(tables["games"]["final_scores"].map(len).eq(2).all()),
            "every_site_in_season": bool((tournaments["season"] == SEASON).all()),
        },
        "diagnostic_checks": {
            "clue_phase_has_four_views": outputs["clue_phase_summary"]["outcome"].nunique() == 4,
            "phase0_first_buzz_count_matches_source": int(
                outputs["clue_boundary_summary"]
                .set_index("outcome")
                .loc["Phase-0 first buzz", "buzzes"]
            )
            == int((buzzes["is_scored"] & buzzes["is_first_buzz"]).sum()),
            "three_adjacent_tier_stability_rows": len(outputs["player_parameter_stability"]) == 3,
            "specialty_sensitivity_thresholds_present": outputs[
                "category_specialization_sensitivity"
            ]["minimum_scored_attempts_per_category_half"].tolist()
            == [5, 8, 10, 15],
            "question_correlations_have_pooled_plus_tiers": outputs[
                "question_signal_correlations"
            ]["tier"].tolist()
            == ["pooled"] + TIER_ORDER,
        },
        "known_quality_items": {
            "missing_tossup_categories": int(tossups["category_group"].eq("Unknown").sum()),
            "missing_bonus_categories": int(bonuses["category_group"].eq("Unknown").sum()),
            "buzz_position_overruns_before_clipping": int(buzzes["position_overrun"].sum()),
            "missing_earning_player_bonus_responses": int((~responses["has_earning_player"]).sum()),
        },
        "mds": {key: round(value, 6) for key, value in mds_stats.items()},
    }
    with (data_dir / "validation.json").open("w", encoding="utf-8") as handle:
        json.dump(validation, handle, indent=2)


# ---------------------------------------------------------------------------
# Figures
# ---------------------------------------------------------------------------


def plot_season_overview(figures_dir: Path, outputs: dict[str, pd.DataFrame]) -> None:
    frame = outputs["tier_summary"].set_index("tier").loc[TIER_ORDER]
    metrics = [
        ("tournament_sites", "Mirror sites"),
        ("teams", "Team entries"),
        ("player_ids", "Player IDs with a buzz"),
        ("games", "Games"),
        ("buzz_events", "Tossup attempts"),
        ("bonuses_heard", "Bonuses heard"),
    ]
    fig, axes = plt.subplots(2, 3, figsize=(15, 8))
    for axis, (column, label) in zip(axes.flat, metrics):
        style_axis(axis)
        axis.bar(
            np.arange(len(TIER_ORDER)),
            frame[column],
            color=[TIER_COLORS[tier] for tier in TIER_ORDER],
            width=0.62,
            zorder=3,
        )
        for index, value in enumerate(frame[column]):
            axis.text(index, value, f"{int(value):,}", ha="center", va="bottom", color=INK, fontsize=8.5)
        tier_ticks(axis, with_dates=True)
        axis.set_title(label, color=INK, fontsize=11)
        axis.margins(y=0.14)
    fig.suptitle(f"ACF {SEASON} season, in chronological order", color=INK, fontsize=14)
    save_figure(fig, figures_dir, "01_season_overview.png")


def plot_site_scale(figures_dir: Path, outputs: dict[str, pd.DataFrame]) -> None:
    frame = outputs["site_summary"]
    fig, axis = plt.subplots(figsize=(10.5, 6.5))
    style_axis(axis)
    for tier in TIER_ORDER:
        subset = frame[frame["tier"] == tier]
        axis.scatter(
            subset["teams"], subset["games"], s=70, color=TIER_COLORS[tier], edgecolor=PAPER, linewidth=0.8, zorder=3
        )
    for row in frame.nlargest(7, "games").itertuples(index=False):
        axis.annotate(
            row.site, (row.teams, row.games), textcoords="offset points", xytext=(6, 3), fontsize=8, color=MUTED
        )
    axis.set_xlabel("Team entries", color=MUTED)
    axis.set_ylabel("Games", color=MUTED)
    axis.set_title(f"Mirror-site scale, {SEASON} season ({len(frame)} sites)", color=INK, fontsize=12)
    tier_legend(axis)
    save_figure(fig, figures_dir, "02_site_scale.png")


def plot_tossup_outcomes(figures_dir: Path, outputs: dict[str, pd.DataFrame]) -> None:
    outcome = outputs["outcome_summary"]
    order = ["Correct (+10)", "Neg (-5)", "Zero (0)"]
    colors = {"Correct (+10)": GREEN, "Neg (-5)": RED, "Zero (0)": MUTED}
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))

    style_axis(axes[0])
    for index, tier in enumerate(TIER_ORDER):
        bottom = 0.0
        for name in order:
            share = outcome.query("tier == @tier and outcome == @name")["share_within_tier"].sum()
            axes[0].bar(index, share, bottom=bottom, color=colors[name], width=0.62, zorder=3)
            if share > 0.03:
                axes[0].text(
                    index, bottom + share / 2, f"{share:.1%}", ha="center", va="center", color=PAPER, fontsize=9
                )
            bottom += share
    tier_ticks(axes[0], with_dates=True)
    axes[0].set_ylabel("Share of attempts", color=MUTED)
    axes[0].set_title("Attempt composition", color=INK, fontsize=11)
    legend_headroom(axes[0])
    axes[0].legend(
        handles=[Line2D([], [], color=colors[n], marker="s", linestyle="none", label=n) for n in order],
        frameon=False,
        labelcolor=MUTED,
        fontsize=9,
        loc="upper center",
        ncol=3,
    )

    style_axis(axes[1])
    for name in order:
        values = [
            outcome.query("tier == @tier and outcome == @name")["median_position_pct"].mean()
            for tier in TIER_ORDER
        ]
        axes[1].plot(np.arange(len(TIER_ORDER)), values, marker="o", color=colors[name], linewidth=2.0, label=name, zorder=3)
    tier_ticks(axes[1], with_dates=True)
    axes[1].set_ylabel("Median position (% revealed)", color=MUTED)
    axes[1].set_title("Median buzz position by outcome", color=INK, fontsize=11)
    axes[1].legend(frameon=False, labelcolor=MUTED, fontsize=9)
    save_figure(fig, figures_dir, "03_tossup_outcomes.png")


def plot_buzz_positions(figures_dir: Path, tables: dict[str, pd.DataFrame]) -> None:
    buzzes = tables["tossup_buzzes"]
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))
    bins = np.linspace(0, 100, 41)

    style_axis(axes[0])
    for tier in TIER_ORDER:
        values = buzzes.loc[buzzes["tier"] == tier, "position_pct"]
        axes[0].hist(
            values,
            bins=bins,
            density=True,
            histtype="step",
            linewidth=2.0,
            color=TIER_COLORS[tier],
            label=f"{TIER_SHORT[tier]} (n={len(values):,})",
            zorder=3,
        )
    axes[0].set_xlabel("Position (% of tossup revealed)", color=MUTED)
    axes[0].set_ylabel("Density", color=MUTED)
    axes[0].set_title("All attempts", color=INK, fontsize=11)
    axes[0].legend(frameon=False, labelcolor=MUTED, fontsize=8.5)

    style_axis(axes[1])
    scored = buzzes[buzzes["is_scored"]]
    for tier in TIER_ORDER:
        values = scored.loc[scored["tier"] == tier, "position_pct"]
        axes[1].hist(
            values, bins=bins, density=True, histtype="step", linewidth=2.0, color=TIER_COLORS[tier], zorder=3
        )
    axes[1].set_xlabel("Position (% of tossup revealed)", color=MUTED)
    axes[1].set_ylabel("Density", color=MUTED)
    axes[1].set_title("Scored attempts only (+10 / −5)", color=INK, fontsize=11)
    fig.suptitle("Buzz-position distributions: the end-of-question spike is value-0 attempts", color=INK, fontsize=13)
    save_figure(fig, figures_dir, "04_buzz_position_distributions.png")


def plot_position_accuracy(figures_dir: Path, outputs: dict[str, pd.DataFrame]) -> None:
    frame = outputs["position_decile_summary"]
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.5), sharex=True)
    for axis, (column, title) in zip(
        axes, [("scored_accuracy", "Scored accuracy by position decile"), ("neg_rate", "Neg rate by position decile")]
    ):
        style_axis(axis)
        for tier in TIER_ORDER:
            subset = frame.query("tier == @tier and buzz_events > 0").sort_values("midpoint_pct")
            axis.plot(
                subset["midpoint_pct"],
                subset[column],
                marker="o",
                markersize=4.5,
                color=TIER_COLORS[tier],
                linewidth=1.9,
                label=TIER_SHORT[tier],
                zorder=3,
            )
        axis.set_xlabel("Position (% revealed)", color=MUTED)
        axis.set_title(title, color=INK, fontsize=11)
    axes[0].set_ylabel("Rate", color=MUTED)
    axes[0].legend(frameon=False, labelcolor=MUTED, fontsize=8.5)
    save_figure(fig, figures_dir, "05_position_accuracy_curves.png")


def plot_zero_artifact(figures_dir: Path, outputs: dict[str, pd.DataFrame]) -> None:
    """Make the all-attempt versus scored denominator difference explicit."""
    pooled = outputs["position_decile_pooled"].sort_values("midpoint_pct")
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))

    style_axis(axes[0])
    axes[0].plot(
        pooled["midpoint_pct"], pooled["accuracy"], marker="o", color=RED, linewidth=2.0, label="All-attempt accuracy", zorder=3
    )
    axes[0].plot(
        pooled["midpoint_pct"], pooled["scored_accuracy"], marker="s", color=GREEN, linewidth=2.0, label="Scored accuracy", zorder=3
    )
    axes[0].set_xlabel("Position (% revealed)", color=MUTED)
    axes[0].set_ylabel("Accuracy", color=MUTED)
    axes[0].set_title("Two denominators, two different stories", color=INK, fontsize=11)
    axes[0].legend(frameon=False, labelcolor=MUTED, fontsize=9)

    style_axis(axes[1])
    axes[1].bar(pooled["midpoint_pct"], pooled["zero_rate"], width=8, color=MUTED, zorder=3)
    axes[1].set_xlabel("Position (% revealed)", color=MUTED)
    axes[1].set_ylabel("Share of attempts with value 0", color=MUTED)
    axes[1].set_title("Value-0 attempts are an end-of-question phenomenon", color=INK, fontsize=11)
    fig.suptitle(
        "Scored accuracy rises monotonically; the all-attempt reversal is the zero pile-up", color=INK, fontsize=13
    )
    save_figure(fig, figures_dir, "06_zero_value_artifact.png")


def plot_player_distributions(figures_dir: Path, outputs: dict[str, pd.DataFrame]) -> None:
    players = outputs["player_summary"]
    active = players[players["buzz_events"] >= MIN_PLAYER_ATTEMPTS]
    fig, axes = plt.subplots(1, 3, figsize=(15, 4.8))

    style_axis(axes[0])
    axes[0].hist(
        players["buzz_events"],
        bins=np.logspace(0, np.log10(max(players["buzz_events"].max(), 10)), 36),
        color=BLUE,
        zorder=3,
    )
    axes[0].set_xscale("log")
    axes[0].set_xlabel("Attempts per player ID (log)", color=MUTED)
    axes[0].set_ylabel("Player IDs", color=MUTED)
    axes[0].set_title(f"Activity ({len(players):,} IDs with a buzz)", color=INK, fontsize=11)

    style_axis(axes[1])
    axes[1].hist(active["scored_accuracy"], bins=28, color=GREEN, zorder=3)
    axes[1].set_xlabel("Scored accuracy", color=MUTED)
    axes[1].set_ylabel("Player IDs", color=MUTED)
    axes[1].set_title(f"Scored accuracy (≥{MIN_PLAYER_ATTEMPTS} attempts, n={len(active):,})", color=INK, fontsize=11)

    style_axis(axes[2])
    axes[2].hist(active["mean_position_pct"], bins=28, color=PURPLE, zorder=3)
    axes[2].set_xlabel("Mean buzz position (% revealed)", color=MUTED)
    axes[2].set_ylabel("Player IDs", color=MUTED)
    axes[2].set_title("Timing", color=INK, fontsize=11)
    fig.suptitle(f"Player-ID distributions, {SEASON} season", color=INK, fontsize=13)
    save_figure(fig, figures_dir, "07_player_distributions.png")


def plot_player_accuracy_timing(figures_dir: Path, outputs: dict[str, pd.DataFrame]) -> None:
    active = outputs["player_summary"].query(f"buzz_events >= {MIN_PLAYER_ATTEMPTS}")
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.8))
    for axis, (column, label) in zip(
        axes, [("accuracy_all_attempts", "All-attempt accuracy"), ("scored_accuracy", "Scored accuracy")]
    ):
        style_axis(axis)
        hexbin = axis.hexbin(
            active["mean_position_pct"], active[column], gridsize=28, cmap="BuGn", mincnt=1, zorder=3
        )
        correlation = active["mean_position_pct"].corr(active[column])
        axis.set_xlabel("Mean buzz position (% revealed)", color=MUTED)
        axis.set_ylabel(label, color=MUTED)
        axis.set_title(f"{label} (r = {correlation:.3f})", color=INK, fontsize=11)
        fig.colorbar(hexbin, ax=axis).set_label("Player IDs", color=MUTED)
    fig.suptitle(
        f"The accuracy/timing relationship is a denominator artifact (n={len(active):,})", color=INK, fontsize=13
    )
    save_figure(fig, figures_dir, "08_player_accuracy_vs_timing.png")


def plot_player_retention(figures_dir: Path, outputs: dict[str, pd.DataFrame]) -> None:
    retention = outputs["player_retention"]
    players = outputs["player_summary"]
    matrix = retention.pivot(index="from_tier", columns="to_tier", values="share_of_from").loc[
        TIER_ORDER, TIER_ORDER
    ]
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.8))

    axis = axes[0]
    axis.set_facecolor(PAPER)
    image = axis.imshow(matrix.to_numpy(float), cmap="BuGn", vmin=0, vmax=1)
    axis.set_xticks(np.arange(len(TIER_ORDER)))
    axis.set_xticklabels([TIER_SHORT[tier] for tier in TIER_ORDER], fontsize=9, color=MUTED)
    axis.set_yticks(np.arange(len(TIER_ORDER)))
    axis.set_yticklabels([TIER_SHORT[tier] for tier in TIER_ORDER], fontsize=9, color=MUTED)
    axis.tick_params(length=0)
    for i in range(len(TIER_ORDER)):
        for j in range(len(TIER_ORDER)):
            value = matrix.to_numpy(float)[i, j]
            axis.text(
                j, i, f"{value:.0%}", ha="center", va="center", fontsize=10, color=INK if value < 0.6 else PAPER
            )
    axis.set_xlabel("also played", color=MUTED)
    axis.set_ylabel("of players who played", color=MUTED)
    axis.set_title("Player overlap between tiers", color=INK, fontsize=11)
    fig.colorbar(image, ax=axis, shrink=0.8).set_label("Share of row's players", color=MUTED)

    style_axis(axes[1])
    counts = players["tiers_played"].value_counts().reindex([1, 2, 3, 4]).fillna(0)
    axes[1].bar(counts.index, counts.to_numpy(), color=BLUE, width=0.6, zorder=3)
    for index, value in zip(counts.index, counts.to_numpy()):
        axes[1].text(index, value, f"{int(value):,}", ha="center", va="bottom", color=INK, fontsize=10)
    axes[1].set_xticks([1, 2, 3, 4])
    axes[1].set_xlabel("Tiers played in the season", color=MUTED)
    axes[1].set_ylabel("Player IDs", color=MUTED)
    axes[1].set_title("Most players appear at exactly one tier", color=INK, fontsize=11)
    axes[1].margins(y=0.12)
    fig.suptitle(f"Within-season player progression, {SEASON}", color=INK, fontsize=13)
    save_figure(fig, figures_dir, "09_player_retention.png")


def plot_field_composition(figures_dir: Path, outputs: dict[str, pd.DataFrame]) -> None:
    frame = outputs["field_composition"].set_index("tier").loc[TIER_ORDER].reset_index()
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))

    style_axis(axes[0])
    positions = np.arange(len(TIER_ORDER))
    axes[0].bar(positions - 0.19, frame["seen_earlier_id_share"], width=0.38, color=BLUE, label="Share of player IDs", zorder=3)
    axes[0].bar(
        positions + 0.19, frame["seen_earlier_buzz_share"], width=0.38, color=GOLD, label="Share of attempts", zorder=3
    )
    tier_ticks(axes[0], with_dates=True)
    axes[0].set_ylim(0, 1)
    axes[0].set_ylabel("Seen earlier this season", color=MUTED)
    axes[0].set_title("Field carry-over accumulates through the season", color=INK, fontsize=11)
    axes[0].legend(frameon=False, labelcolor=MUTED, fontsize=9)

    style_axis(axes[1])
    new_ids = frame["player_ids"] - frame["seen_earlier_ids"]
    axes[1].bar(positions, frame["seen_earlier_ids"], width=0.62, color=BLUE, label="Seen earlier", zorder=3)
    axes[1].bar(
        positions, new_ids, bottom=frame["seen_earlier_ids"], width=0.62, color=MUTED, label="First seen here", zorder=3
    )
    tier_ticks(axes[1], with_dates=True)
    axes[1].set_ylabel("Player IDs with a buzz", color=MUTED)
    axes[1].set_title("Field size and composition", color=INK, fontsize=11)
    axes[1].legend(frameon=False, labelcolor=MUTED, fontsize=9)
    save_figure(fig, figures_dir, "10_field_composition.png")


def plot_selection(figures_dir: Path, outputs: dict[str, pd.DataFrame]) -> None:
    """Holding the question set fixed, compare players by how far they later go.

    Fixing the set removes the difficulty confound that spoils any naive
    cross-tier comparison, so what is left is selection on the players.
    """
    frame = outputs["selection_on_fixed_set"].copy()
    frame["rank"] = frame["furthest_tier"].map(TIER_RANK)
    fixed_tiers = [tier for tier in TIER_ORDER[:-1] if tier in set(frame["fixed_set_tier"])]
    fig, axes = plt.subplots(1, 2, figsize=(14.5, 5.8))
    for axis, (column, label, title) in zip(
        axes,
        [
            ("mean_scored_accuracy", "Scored accuracy on that set", "Conditional accuracy: a modest gap"),
            ("mean_position_pct", "Mean buzz position on that set (%)", "Timing: a much larger gap"),
        ],
    ):
        style_axis(axis)
        for fixed in fixed_tiers:
            subset = frame[frame["fixed_set_tier"] == fixed].sort_values("rank")
            axis.plot(
                subset["rank"],
                subset[column],
                marker="o",
                markersize=7,
                color=TIER_COLORS[fixed],
                linewidth=2.0,
                label=f"{TIER_SHORT[fixed]} set",
                zorder=3,
            )
            for row in subset.itertuples(index=False):
                axis.annotate(
                    f"n={row.players}",
                    (row.rank, getattr(row, column)),
                    textcoords="offset points",
                    xytext=(0, -14),
                    ha="center",
                    fontsize=7.5,
                    color=MUTED,
                )
        axis.set_xticks(np.arange(len(TIER_ORDER)))
        axis.set_xticklabels([TIER_SHORT[tier] for tier in TIER_ORDER], fontsize=9)
        axis.set_xlabel("Furthest tier reached in the season", color=MUTED)
        axis.set_ylabel(label, color=MUTED)
        axis.set_title(title, color=INK, fontsize=11)
        axis.legend(frameon=False, labelcolor=MUTED, fontsize=8.5)
    axes[1].invert_yaxis()
    axes[1].set_ylabel("Mean buzz position (%) — earlier is higher", color=MUTED)
    fig.suptitle(
        f"Selection through the season, question set held fixed (≥{MIN_FIXED_SET_ATTEMPTS} attempts on that set)",
        color=INK,
        fontsize=13,
    )
    save_figure(fig, figures_dir, "11_selection_on_fixed_set.png")


def plot_team_tossup_vs_bonus(figures_dir: Path, outputs: dict[str, pd.DataFrame]) -> None:
    teams = outputs["team_summary"].query("games >= 5 and buzz_events >= 30 and bonuses_heard >= 15")
    fig, axis = plt.subplots(figsize=(10, 6.5))
    style_axis(axis)
    for tier in TIER_ORDER:
        subset = teams[teams["tier"] == tier]
        axis.scatter(
            subset["scored_accuracy"], subset["ppb"], s=30, alpha=0.72, color=TIER_COLORS[tier], edgecolor="none", zorder=3
        )
    correlation = teams["scored_accuracy"].corr(teams["ppb"])
    axis.set_xlabel("Scored-attempt accuracy (+10 / −5 only)", color=MUTED)
    axis.set_ylabel("Points per bonus", color=MUTED)
    axis.set_title(f"Team tossup skill versus bonus conversion (n={len(teams):,}, r = {correlation:.3f})", color=INK, fontsize=12)
    legend_headroom(axis)
    tier_legend(axis, loc="upper right", ncol=4)
    save_figure(fig, figures_dir, "12_team_tossup_vs_bonus.png")


def plot_category_composition(figures_dir: Path, outputs: dict[str, pd.DataFrame], tables: dict[str, pd.DataFrame]) -> None:
    tossups = tables["tossups"]
    pivot = (
        tossups.groupby(["tier", "category_group"], observed=True)
        .size()
        .unstack(fill_value=0)
        .reindex(index=TIER_ORDER)
    )
    columns = [column for column in CATEGORY_ORDER if column in pivot.columns]
    pivot = pivot[columns]
    shares = pivot.div(pivot.sum(axis=1), axis=0)
    fig, axes = plt.subplots(1, 2, figsize=(15, 6), sharey=True)
    cmap = plt.get_cmap("tab20")
    for axis, frame, title, xlabel in [
        (axes[0], pivot, "Question counts", "Tossup questions"),
        (axes[1], shares, "Share of set", "Share of tossups"),
    ]:
        style_axis(axis, grid_axis="x")
        left = np.zeros(len(frame))
        for index, column in enumerate(frame.columns):
            axis.barh(
                np.arange(len(frame)),
                frame[column],
                left=left,
                color=MUTED if column == "Unknown" else cmap(index % 20),
                label=column,
                zorder=3,
            )
            left += frame[column].to_numpy()
        axis.set_yticks(np.arange(len(frame)))
        axis.set_yticklabels([TIER_SHORT[tier] for tier in frame.index], fontsize=9)
        axis.invert_yaxis()
        axis.set_xlabel(xlabel, color=MUTED)
        axis.set_title(title, color=INK, fontsize=11)
    axes[1].legend(frameon=False, labelcolor=MUTED, fontsize=8.5, loc="center left", bbox_to_anchor=(1.02, 0.5))
    fig.suptitle(f"Category composition, {SEASON} season (complete metadata, no Unknown)", color=INK, fontsize=13)
    save_figure(fig, figures_dir, "13_category_composition.png")


def plot_category_performance(figures_dir: Path, outputs: dict[str, pd.DataFrame]) -> None:
    category = outputs["category_summary"]
    present = [name for name in CATEGORY_ORDER if name in set(category["category_group"]) and name != "Unknown"]
    frame = category.set_index("category_group").loc[present]
    fig, axes = plt.subplots(1, 3, figsize=(16, 5.5))
    positions = np.arange(len(present))
    for axis, (column, label) in zip(
        axes,
        [
            ("scored_accuracy", "Scored accuracy"),
            ("mean_position_pct", "Mean buzz position (%)"),
            ("ppb", "Points per bonus"),
        ],
    ):
        style_axis(axis, grid_axis="x")
        axis.barh(positions, frame[column], height=0.66, color=BLUE, zorder=3)
        axis.set_yticks(positions)
        axis.set_yticklabels(present, fontsize=9)
        axis.invert_yaxis()
        axis.set_title(label, color=INK, fontsize=11)
    fig.suptitle(f"Category performance, {SEASON} season (all questions labelled)", color=INK, fontsize=13)
    save_figure(fig, figures_dir, "14_category_performance.png")


def plot_question_difficulty(figures_dir: Path, outputs: dict[str, pd.DataFrame]) -> None:
    tossups = outputs["tossup_question_summary"]
    bonuses = outputs["bonus_question_summary"]
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))
    for axis, frame, column, label in [
        (axes[0], tossups, "conversion_rate", "Per-question all-attempt accuracy"),
        (axes[1], bonuses, "ppb", "Per-question points per bonus"),
    ]:
        style_axis(axis)
        data = [frame.loc[frame["tier"] == tier, column].dropna() for tier in TIER_ORDER]
        parts = axis.violinplot(data, showmedians=True, widths=0.8)
        for body, tier in zip(parts["bodies"], TIER_ORDER):
            body.set_facecolor(TIER_COLORS[tier])
            body.set_alpha(0.68)
        for key in ["cbars", "cmins", "cmaxes", "cmedians"]:
            parts[key].set_color(INK)
            parts[key].set_linewidth(1.0)
        axis.set_xticks(np.arange(1, len(TIER_ORDER) + 1))
        axis.set_xticklabels([TIER_SHORT[tier] for tier in TIER_ORDER], fontsize=9)
        axis.set_ylabel(label, color=MUTED)
    axes[0].set_title("Tossup difficulty spread", color=INK, fontsize=11)
    axes[1].set_title("Bonus difficulty spread", color=INK, fontsize=11)
    fig.suptitle(f"Question-level difficulty through the {SEASON} season", color=INK, fontsize=13)
    save_figure(fig, figures_dir, "15_question_difficulty.png")


def plot_length_relationships(figures_dir: Path, outputs: dict[str, pd.DataFrame]) -> None:
    tossups = outputs["tossup_question_summary"].dropna(subset=["mean_position_pct"])
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    style_axis(axes[0])
    for tier in TIER_ORDER:
        axes[0].hist(
            tossups.loc[tossups["tier"] == tier, "num_tokens"],
            bins=28,
            histtype="step",
            linewidth=1.9,
            color=TIER_COLORS[tier],
            label=TIER_SHORT[tier],
            zorder=3,
        )
    axes[0].set_xlabel("Tossup tokens", color=MUTED)
    axes[0].set_ylabel("Questions", color=MUTED)
    axes[0].set_title("Question length", color=INK, fontsize=11)
    legend_headroom(axes[0])
    axes[0].legend(frameon=False, labelcolor=MUTED, fontsize=8.5, loc="upper right", ncol=2)

    for axis, xcolumn, ycolumn, xlabel, ylabel in [
        (axes[1], "num_tokens", "mean_position_pct", "Tossup tokens", "Mean buzz position (%)"),
        (axes[2], "num_clues", "conversion_rate", "Clue spans", "All-attempt accuracy"),
    ]:
        style_axis(axis)
        axis.scatter(
            tossups[xcolumn],
            tossups[ycolumn],
            s=11,
            alpha=0.38,
            c=[TIER_COLORS[tier] for tier in tossups["tier"]],
            edgecolor="none",
            zorder=3,
        )
        correlation = tossups[xcolumn].corr(tossups[ycolumn])
        axis.set_xlabel(xlabel, color=MUTED)
        axis.set_ylabel(ylabel, color=MUTED)
        axis.set_title(f"r = {correlation:.3f}", color=INK, fontsize=11)
    save_figure(fig, figures_dir, "16_question_length_relationships.png")


def plot_game_scores(figures_dir: Path, outputs: dict[str, pd.DataFrame]) -> None:
    team_games = outputs["team_game_results"]
    tier_summary = outputs["tier_summary"].set_index("tier").loc[TIER_ORDER]
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    for axis, column, xlabel, title in [
        (axes[0], "score", "Team score", "Scoring environment"),
        (axes[1], "abs_margin", "Absolute margin", "Competitiveness"),
    ]:
        style_axis(axis)
        for tier in TIER_ORDER:
            subset = team_games[team_games["tier"] == tier]
            values = subset["margin"].abs() if column == "abs_margin" else subset[column]
            axis.hist(
                values, bins=36, histtype="step", linewidth=1.9, density=True, color=TIER_COLORS[tier], label=TIER_SHORT[tier], zorder=3
            )
        axis.set_xlabel(xlabel, color=MUTED)
        axis.set_ylabel("Density", color=MUTED)
        axis.set_title(title, color=INK, fontsize=11)
    axes[0].legend(frameon=False, labelcolor=MUTED, fontsize=8.5)

    style_axis(axes[2])
    axes[2].plot(
        np.arange(len(TIER_ORDER)), tier_summary["mean_team_score"], marker="o", color=BLUE, linewidth=2.0, label="Mean team score", zorder=3
    )
    axes[2].plot(
        np.arange(len(TIER_ORDER)), tier_summary["median_abs_margin"], marker="s", color=RED, linewidth=2.0, label="Median absolute margin", zorder=3
    )
    tier_ticks(axes[2], with_dates=True)
    axes[2].set_ylabel("Points", color=MUTED)
    axes[2].set_title("Scoring and margin through the season", color=INK, fontsize=11)
    axes[2].legend(frameon=False, labelcolor=MUTED, fontsize=9)
    save_figure(fig, figures_dir, "17_game_scores_and_margins.png")


def plot_bonus_parts(figures_dir: Path, outputs: dict[str, pd.DataFrame]) -> None:
    parts = outputs["bonus_part_summary"]
    present = [name for name in DIFFICULTY_ORDER if name in set(parts["difficulty"])]
    fig, axis = plt.subplots(figsize=(10, 6))
    style_axis(axis)
    positions = np.arange(len(TIER_ORDER))
    width = 0.8 / max(len(present), 1)
    for index, difficulty in enumerate(present):
        values = [
            parts.query("tier == @tier and difficulty == @difficulty")["conversion"].mean() for tier in TIER_ORDER
        ]
        offsets = positions + (index - (len(present) - 1) / 2) * width
        axis.bar(offsets, values, width=width, color=DIFFICULTY_COLORS.get(difficulty, MUTED), label=difficulty, zorder=3)
        for x, value in zip(offsets, values):
            axis.text(x, value, f"{value:.2f}", ha="center", va="bottom", color=INK, fontsize=8)
    tier_ticks(axis, with_dates=True)
    axis.set_ylim(0, 1.05)
    axis.set_ylabel("Part conversion rate", color=MUTED)
    axis.set_title(f"Bonus-part conversion by declared difficulty, {SEASON}", color=INK, fontsize=12)
    axis.legend(frameon=False, labelcolor=MUTED, fontsize=9)
    save_figure(fig, figures_dir, "18_bonus_part_conversion.png")


def plot_site_performance(figures_dir: Path, outputs: dict[str, pd.DataFrame]) -> None:
    frame = outputs["site_summary"]
    fig, axis = plt.subplots(figsize=(10, 6.5))
    style_axis(axis)
    for tier in TIER_ORDER:
        subset = frame[frame["tier"] == tier]
        axis.scatter(
            subset["accuracy_all_attempts"], subset["ppb"], s=72, color=TIER_COLORS[tier], edgecolor=PAPER, linewidth=0.8, zorder=3
        )
    axis.set_xlabel("Site tossup accuracy (all attempts)", color=MUTED)
    axis.set_ylabel("Site points per bonus", color=MUTED)
    axis.set_title("Mirror-site difficulty profile", color=INK, fontsize=12)
    tier_legend(axis)
    save_figure(fig, figures_dir, "19_site_performance.png")


def plot_missingness(figures_dir: Path, outputs: dict[str, pd.DataFrame]) -> None:
    frame = outputs["missingness_summary"].sort_values("missing_rate", ascending=False)
    fig, axis = plt.subplots(figsize=(10, 6.5))
    style_axis(axis, grid_axis="x")
    positions = np.arange(len(frame))
    axis.barh(
        positions, frame["missing_rate"], color=[RED if rate > 0 else GRID for rate in frame["missing_rate"]], zorder=3
    )
    axis.set_yticks(positions)
    axis.set_yticklabels(frame["table"] + "." + frame["field"], fontsize=9)
    axis.invert_yaxis()
    axis.set_xlabel("Missing or empty rate", color=MUTED)
    axis.set_title(f"Field-level missingness, {SEASON} season", color=INK, fontsize=12)
    save_figure(fig, figures_dir, "20_data_missingness.png")


def plot_mds(figures_dir: Path, outputs: dict[str, pd.DataFrame], kind: str, filename: str, title: str) -> None:
    coords = outputs[f"{kind}_mds_coordinates"]
    fig, axis = plt.subplots(figsize=(10, 7))
    style_axis(axis, grid_axis="both")
    size = 30 if kind == "team" else 78
    for tier in TIER_ORDER:
        subset = coords[coords["tier"] == tier]
        axis.scatter(
            subset["mds1"],
            subset["mds2"],
            s=size,
            alpha=0.75 if kind == "team" else 0.95,
            color=TIER_COLORS[tier],
            edgecolor="none" if kind == "team" else PAPER,
            linewidth=0 if kind == "team" else 0.8,
            zorder=3,
        )
    if kind == "site":
        extreme = coords.reindex(coords["mds1"].abs().sort_values(ascending=False).index).head(6)
        for row in extreme.itertuples(index=False):
            axis.annotate(
                row.site, (row.mds1, row.mds2), textcoords="offset points", xytext=(7, 3), fontsize=8, color=MUTED
            )
    axis.axhline(0, color=GRID, linewidth=0.8)
    axis.axvline(0, color=GRID, linewidth=0.8)
    axis.set_xlabel("MDS dimension 1", color=MUTED)
    axis.set_ylabel("MDS dimension 2", color=MUTED)
    axis.set_title(title, color=INK, fontsize=12)
    legend_headroom(axis)
    tier_legend(axis, loc="upper right", ncol=4)
    save_figure(fig, figures_dir, filename)


def plot_mds_loadings(figures_dir: Path, outputs: dict[str, pd.DataFrame]) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(15, 7))
    for axis, kind, title in [(axes[0], "team", "Team map"), (axes[1], "site", "Mirror-site map")]:
        loadings = outputs[f"{kind}_mds_loadings"]
        style_axis(axis, grid_axis="both")
        axis.axhline(0, color=GRID, linewidth=0.8)
        axis.axvline(0, color=GRID, linewidth=0.8)
        for row in loadings.itertuples(index=False):
            axis.annotate(
                "", xy=(row.mds1, row.mds2), xytext=(0, 0), arrowprops={"arrowstyle": "->", "color": BLUE, "linewidth": 1.3}
            )
            axis.annotate(
                row.feature, (row.mds1, row.mds2), textcoords="offset points", xytext=(5, 3), fontsize=8, color=INK
            )
        axis.set_xlim(-1.2, 1.2)
        axis.set_ylim(-1.2, 1.2)
        axis.set_xlabel("Correlation with dimension 1", color=MUTED)
        axis.set_ylabel("Correlation with dimension 2", color=MUTED)
        axis.set_title(title, color=INK, fontsize=11)
    fig.suptitle("What the MDS axes mean", color=INK, fontsize=13)
    save_figure(fig, figures_dir, "23_mds_loadings.png")


def plot_team_correlations(figures_dir: Path, outputs: dict[str, pd.DataFrame]) -> None:
    frame = outputs["team_metric_correlations"].set_index("metric")
    values = frame.to_numpy(float)
    fig, axis = plt.subplots(figsize=(9.5, 8))
    axis.set_facecolor(PAPER)
    image = axis.imshow(values, cmap="RdBu_r", vmin=-1, vmax=1)
    axis.set_xticks(np.arange(len(frame.columns)))
    axis.set_xticklabels(frame.columns, rotation=45, ha="right", fontsize=8.5, color=MUTED)
    axis.set_yticks(np.arange(len(frame.index)))
    axis.set_yticklabels(frame.index, fontsize=8.5, color=MUTED)
    axis.tick_params(length=0)
    for i in range(values.shape[0]):
        for j in range(values.shape[1]):
            axis.text(
                j, i, f"{values[i, j]:.2f}", ha="center", va="center", fontsize=7, color=INK if abs(values[i, j]) < 0.6 else PAPER
            )
    fig.colorbar(image, ax=axis, shrink=0.82).set_label("Pearson r", color=MUTED)
    axis.set_title("Team metric correlations (stable team entries)", color=INK, fontsize=12)
    save_figure(fig, figures_dir, "24_team_metric_correlations.png")


def plot_question_relationships(figures_dir: Path, outputs: dict[str, pd.DataFrame]) -> None:
    tossups = outputs["tossup_question_summary"].dropna(subset=["mean_position_pct", "conversion_rate"])
    bonuses = outputs["bonus_question_summary"].dropna(subset=["ppb", "perfect_bonus_rate"])
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))
    for axis, frame, xcolumn, ycolumn, xlabel, ylabel, title in [
        (axes[0], tossups, "mean_position_pct", "conversion_rate", "Mean buzz position (%)", "All-attempt accuracy", "Tossups: timing versus conversion"),
        (axes[1], bonuses, "ppb", "perfect_bonus_rate", "Points per bonus", "30-point rate", "Bonuses: PPB versus 30 rate"),
    ]:
        style_axis(axis)
        axis.scatter(
            frame[xcolumn],
            frame[ycolumn],
            s=11,
            alpha=0.36,
            c=[TIER_COLORS[tier] for tier in frame["tier"]],
            edgecolor="none",
            zorder=3,
        )
        correlation = frame[xcolumn].corr(frame[ycolumn])
        axis.set_xlabel(xlabel, color=MUTED)
        axis.set_ylabel(ylabel, color=MUTED)
        axis.set_title(f"{title} (r = {correlation:.3f})", color=INK, fontsize=11)
    tier_legend(axes[1])
    save_figure(fig, figures_dir, "25_question_relationships.png")


def plot_clue_phase(figures_dir: Path, outputs: dict[str, pd.DataFrame]) -> None:
    frame = outputs["clue_phase_summary"].query("outcome == 'Phase-0 first buzz'")
    boundary = outputs["clue_boundary_summary"].set_index("outcome").loc["Phase-0 first buzz"]
    x = 100 * (frame["phase_start"].to_numpy() + frame["phase_end"].to_numpy()) / 2
    width = 8.2
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.3), gridspec_kw={"width_ratios": [1.6, 1]})
    style_axis(axes[0])
    axes[0].bar(
        x - width / 4,
        100 * frame["observed_share"],
        width=width / 2,
        color=BLUE,
        label="Observed phase-0 first buzzes",
        zorder=3,
    )
    axes[0].bar(
        x + width / 4,
        100 * frame["uniform_expected_share"],
        width=width / 2,
        color=GRID,
        edgecolor=MUTED,
        linewidth=0.5,
        label="Uniform token opportunity",
        zorder=3,
    )
    axes[0].set_xticks(x)
    axes[0].set_xticklabels([f"{int(value - 5)}–{int(value + 5)}" for value in x], fontsize=8)
    axes[0].set_xlabel("Position within current clue span (%)", color=MUTED)
    axes[0].set_ylabel("Share (%)", color=MUTED)
    axes[0].set_title("Buzzes concentrate at the ends of clues", color=INK, fontsize=11)
    axes[0].legend(frameon=False, labelcolor=MUTED, fontsize=8.5, loc="upper left")

    style_axis(axes[1])
    shares = 100 * np.array(
        [boundary["uniform_expected_boundary_share"], boundary["observed_boundary_share"]]
    )
    axes[1].bar([0, 1], shares, color=[GRID, BLUE], width=0.58, zorder=3)
    axes[1].set_xticks([0, 1])
    axes[1].set_xticklabels(["Token\nopportunity", "Observed phase-0\nfirst buzzes"], fontsize=9)
    axes[1].set_ylabel("Exactly on a clue boundary (%)", color=MUTED)
    axes[1].set_title(
        f"Exact-boundary enrichment: {boundary['boundary_enrichment']:.2f}×",
        color=INK,
        fontsize=11,
    )
    for index, value in enumerate(shares):
        axes[1].text(index, value, f"{value:.1f}%", ha="center", va="bottom", color=INK, fontsize=9)
    fig.suptitle("Clue-local structure is visible in first-buzz positions", color=INK, fontsize=13)
    save_figure(fig, figures_dir, "26_clue_phase_buzzing.png")


def plot_player_parameter_stability(figures_dir: Path, outputs: dict[str, pd.DataFrame]) -> None:
    frame = outputs["player_parameter_stability"]
    x = np.arange(len(frame))
    width = 0.34
    fig, axis = plt.subplots(figsize=(10, 5.5))
    style_axis(axis)
    axis.bar(
        x - width / 2,
        frame["timing_residual_correlation"],
        width,
        color=BLUE,
        label="Timing residual",
        zorder=3,
    )
    axis.bar(
        x + width / 2,
        frame["correctness_residual_correlation"],
        width,
        color=GOLD,
        label="Correctness residual",
        zorder=3,
    )
    axis.set_xticks(x)
    axis.set_xticklabels(
        [
            f"{TIER_SHORT[row.source_tier]} → {TIER_SHORT[row.target_tier]}\n(n = {int(row.players)})"
            for row in frame.itertuples()
        ],
        fontsize=9,
    )
    axis.set_ylim(0, 0.85)
    axis.set_ylabel("Pearson r across returning players", color=MUTED)
    axis.set_title(
        f"Question-centered player signals persist (≥{MIN_STABILITY_SCORED} scored attempts per tier)",
        color=INK,
        fontsize=12,
    )
    axis.legend(frameon=False, labelcolor=MUTED, fontsize=9, loc="upper left")
    save_figure(fig, figures_dir, "27_player_parameter_stability.png")


def plot_category_specialization(figures_dir: Path, outputs: dict[str, pd.DataFrame]) -> None:
    frame = outputs["category_specialization_stability"]
    colors = {
        category: color
        for category, color in zip(CATEGORY_ORDER, [BLUE, GOLD, GREEN, RED, PURPLE] * 3)
    }
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.8))
    for axis, metric, title in [
        (axes[0], "timing", "Timing specialty"),
        (axes[1], "correctness", "Correctness specialty"),
    ]:
        subset = frame[frame["metric"].eq(metric)]
        style_axis(axis)
        for category, group in subset.groupby("category_group", observed=True):
            axis.scatter(
                group["specialty_early"],
                group["specialty_late"],
                s=22,
                alpha=0.52,
                color=colors.get(category, MUTED),
                edgecolor="none",
                label=category,
                zorder=3,
            )
        low = min(axis.get_xlim()[0], axis.get_ylim()[0])
        high = max(axis.get_xlim()[1], axis.get_ylim()[1])
        axis.plot([low, high], [low, high], color=MUTED, linewidth=0.9, linestyle="--", zorder=2)
        axis.axhline(0, color=GRID, linewidth=0.8)
        axis.axvline(0, color=GRID, linewidth=0.8)
        correlation = subset["specialty_early"].corr(subset["specialty_late"])
        axis.set_xlabel("Fall + Winter residual", color=MUTED)
        axis.set_ylabel("Regionals + Nationals residual", color=MUTED)
        axis.set_title(f"{title} (r = {correlation:.3f})", color=INK, fontsize=11)
    handles, labels = axes[0].get_legend_handles_labels()
    axes[1].legend(handles, labels, frameon=False, labelcolor=MUTED, fontsize=8, loc="best")
    fig.suptitle(
        f"Do category-specific player deviations repeat? (≥{MIN_SPECIALTY_SCORED} scored attempts per half)",
        color=INK,
        fontsize=13,
    )
    save_figure(fig, figures_dir, "28_category_specialization_stability.png")


def plot_question_signal_coupling(figures_dir: Path, outputs: dict[str, pd.DataFrame]) -> None:
    frame = outputs["tossup_question_summary"].dropna(
        subset=["mean_scored_position_pct", "zero_rate", "scored_accuracy"]
    )
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))
    for axis, xcolumn, xlabel in [
        (axes[0], "mean_scored_position_pct", "Mean scored-buzz position (%)"),
        (axes[1], "zero_rate", "No-buzz / value-0 rate"),
    ]:
        style_axis(axis)
        axis.scatter(
            frame[xcolumn],
            frame["scored_accuracy"],
            s=12,
            alpha=0.38,
            c=[TIER_COLORS[tier] for tier in frame["tier"]],
            edgecolor="none",
            zorder=3,
        )
        correlation = frame[xcolumn].corr(frame["scored_accuracy"])
        axis.set_xlabel(xlabel, color=MUTED)
        axis.set_ylabel("Scored accuracy", color=MUTED)
        axis.set_title(f"Pooled question-level r = {correlation:.3f}", color=INK, fontsize=11)
    tier_legend(axes[1])
    fig.suptitle("Hazard/timing and conditional correctness are coupled, but not interchangeable", color=INK, fontsize=13)
    save_figure(fig, figures_dir, "29_question_signal_coupling.png")


def make_figures(output_dir: Path, tables: dict[str, pd.DataFrame], outputs: dict[str, pd.DataFrame]) -> None:
    figures_dir = output_dir / "figures"
    figures_dir.mkdir(parents=True, exist_ok=True)
    plot_season_overview(figures_dir, outputs)
    plot_site_scale(figures_dir, outputs)
    plot_tossup_outcomes(figures_dir, outputs)
    plot_buzz_positions(figures_dir, tables)
    plot_position_accuracy(figures_dir, outputs)
    plot_zero_artifact(figures_dir, outputs)
    plot_player_distributions(figures_dir, outputs)
    plot_player_accuracy_timing(figures_dir, outputs)
    plot_player_retention(figures_dir, outputs)
    plot_field_composition(figures_dir, outputs)
    plot_selection(figures_dir, outputs)
    plot_team_tossup_vs_bonus(figures_dir, outputs)
    plot_category_composition(figures_dir, outputs, tables)
    plot_category_performance(figures_dir, outputs)
    plot_question_difficulty(figures_dir, outputs)
    plot_length_relationships(figures_dir, outputs)
    plot_game_scores(figures_dir, outputs)
    plot_bonus_parts(figures_dir, outputs)
    plot_site_performance(figures_dir, outputs)
    plot_missingness(figures_dir, outputs)
    plot_mds(figures_dir, outputs, "team", "21_team_mds.png", "Team profile map (classical metric MDS)")
    plot_mds(figures_dir, outputs, "site", "22_site_mds.png", "Mirror-site profile map (classical metric MDS)")
    plot_mds_loadings(figures_dir, outputs)
    plot_team_correlations(figures_dir, outputs)
    plot_question_relationships(figures_dir, outputs)
    plot_clue_phase(figures_dir, outputs)
    plot_player_parameter_stability(figures_dir, outputs)
    plot_category_specialization(figures_dir, outputs)
    plot_question_signal_coupling(figures_dir, outputs)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA)
    parser.add_argument("--output-dir", type=Path, default=HERE)
    parser.add_argument("--skip-figures", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    tables = prepare_tables(args.data_dir)
    outputs = aggregate_outputs(tables)
    mds_stats = add_mds(outputs)
    if not args.skip_figures:
        make_figures(args.output_dir, tables, outputs)
    write_outputs(args.output_dir, tables, outputs, mds_stats)
    print(f"Season {SEASON}: {len(tables['tournaments'])} sites, {len(tables['tossup_buzzes']):,} attempts")
    print(f"Wrote CSVs to {args.output_dir / 'data'}")
    if not args.skip_figures:
        print(f"Wrote figures to {args.output_dir / 'figures'}")
    for key, value in mds_stats.items():
        print(f"  {key}: {value:.4f}")


if __name__ == "__main__":
    main()
