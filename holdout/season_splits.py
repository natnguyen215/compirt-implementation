"""Academic-season splits, which the calendar-year splits cannot express.

The built-in ``year_2024`` / ``year_2025`` splits cut on the tournament start
date's calendar year, but a quizbowl season runs autumn to spring: ACF Fall ->
Winter -> Regionals -> Nationals.  ``year_2024`` therefore holds the back half
of season 2023-24 (Regionals, Nationals) bolted onto the front half of 2024-25
(Fall, Winter), and the one complete season in the local corpus straddles both
year splits.

A season split is named ``season_<start>_<end2>`` and resolves against the
``all`` disk split::

    season_2024_25          # ACF Fall 2024 -> Winter 2024 -> Regionals 2025 -> Nationals 2025

The name carries no ``":"``, so it composes as the base split of a derived
round or game holdout (``game-holdout:season_2024_25:test:5:0:42``).  The
July cutoff matches ``analysis/season_2024_25_eda``.
"""

from __future__ import annotations

import pandas as pd

from holdout.round_splits import _tables_for_games


SEASON_PREFIX = "season_"
#: Disk split a season is carved out of; seasons span calendar years.
SEASON_BASE_SPLIT = "all"


def parse_season_split(split: str) -> str | None:
    """Return the season label in ``split``, or ``None`` if it is not one.

    The label is returned in its canonical ``"2024_25"`` form so callers can
    round-trip it back through :func:`season_split_name`.
    """
    if not isinstance(split, str) or not split.startswith(SEASON_PREFIX):
        return None
    label = split[len(SEASON_PREFIX) :]
    start, _, end = label.partition("_")
    if not start.isdigit() or len(start) != 4 or not end.isdigit() or len(end) != 2:
        raise ValueError(
            f"Malformed season split {split!r}; expected e.g. 'season_2024_25'"
        )
    if int(end) != (int(start) + 1) % 100:
        raise ValueError(
            f"Season split {split!r} must name consecutive years, e.g. 'season_2024_25'"
        )
    return label


def season_split_name(label: str) -> str:
    """Return the canonical loader split name for a season label."""
    return f"{SEASON_PREFIX}{label}"


def season_label_for_date(start_date: object) -> str | None:
    """Return the season a tournament start date belongs to.

    The cut is at July, so autumn events join the *following* calendar year's
    Regionals and Nationals.
    """
    stamp = pd.to_datetime(start_date, errors="coerce")
    if pd.isna(stamp):
        return None
    start_year = stamp.year if stamp.month >= 7 else stamp.year - 1
    return f"{start_year}_{str(start_year + 1)[-2:]}"


def select_season_tables(
    tables: dict[str, pd.DataFrame], label: str
) -> dict[str, pd.DataFrame]:
    """Return linked tables restricted to one academic season."""
    tournaments = tables["tournaments"]
    seasons = tournaments["start_date"].map(season_label_for_date)
    tournament_ids = set(tournaments.loc[seasons == label, "tournament_id"])
    if not tournament_ids:
        available = sorted({value for value in seasons if value is not None})
        raise ValueError(
            f"No tournaments in season {season_split_name(label)!r}; "
            f"available seasons: {', '.join(available) or 'none'}"
        )
    games = tables["games"]
    return _tables_for_games(
        tables, games[games["tournament_id"].isin(tournament_ids)]
    )
