"""Choose, persist, load, and apply event drops for robustness studies.

Every selector takes the tossup observations DataFrame and returns an ordered
list of ``event_id`` strings — the shared interface behind the drop-list
files. A future influence-based (AMIP-style, arXiv 2508.11847) selector should
implement the same signature; today's selectors are the random baseline and a
heuristic influence proxy (a player's earliest correct buzzes carry the most
upward evidence on their skill).
"""

from __future__ import annotations

import math
from pathlib import Path


def load_event_drop_list(path):
    """Read event ids, one per line; blank lines and comments are skipped."""
    event_ids = []
    seen = set()
    for line in Path(path).read_text().splitlines():
        event_id = line.strip()
        if not event_id or event_id.startswith("#"):
            continue
        if event_id not in seen:
            seen.add(event_id)
            event_ids.append(event_id)
    return event_ids


def drop_tossup_events(observations, event_ids):
    """Remove every row of each listed event and return counts with the frame."""
    requested = set(event_ids)
    present = set(observations["event_id"])
    missing = requested - present
    if missing:
        sample = ", ".join(sorted(missing)[:5])
        raise ValueError(
            f"{len(missing)} drop-list event ids not in the observations "
            f"(wrong split/tournament?): {sample}"
        )
    keep = ~observations["event_id"].isin(requested)
    if not keep.any():
        raise ValueError("Dropping the listed events would leave no observations")
    filtered = observations[keep].reset_index(drop=True)
    info = {
        "dropped_events": len(requested),
        "dropped_rows": int((~keep).sum()),
        "remaining_events": int(filtered["event_id"].nunique()),
        "remaining_rows": len(filtered),
    }
    return filtered, info


def random_drop_events(observations, fraction, rng):
    """A random fraction of all events; at least one, sorted for determinism."""
    if not 0 < fraction < 1:
        raise ValueError(f"fraction must be in (0, 1), got {fraction}")
    event_ids = sorted(observations["event_id"].unique())
    count = max(1, math.floor(fraction * len(event_ids)))
    chosen = rng.choice(len(event_ids), size=count, replace=False)
    return sorted(event_ids[i] for i in chosen)


def rank_events_for_target(observations, player_id, direction):
    """The target player's own buzz events, most-influential-first.

    direction="demote": correct buzzes, earliest relative position first —
    the strongest upward evidence on the target's skill, so dropping the
    prefix removes their best support. direction="promote": their negs,
    earliest first, so dropping the prefix removes their worst evidence.

    Returns the ranked frame (event_id, relative_position, y); a drop list of
    size n is its n-prefix, so lists are nested and the minimum flip count is
    well defined.
    """
    buzzes = observations[
        (observations["z"] == "BUZZ") & (observations["player_id"] == player_id)
    ]
    if direction == "demote":
        buzzes = buzzes[buzzes["y"] == 1]
    elif direction == "promote":
        buzzes = buzzes[buzzes["y"] == 0]
    else:
        raise ValueError(f"direction must be 'demote' or 'promote', got {direction}")
    ranked = buzzes.sort_values(
        ["relative_position", "event_id"]
    ).drop_duplicates("event_id")
    return ranked[["event_id", "relative_position", "y"]].reset_index(drop=True)


def select_drop_events(observations, player_id, direction, count):
    """The first 'count' event ids of the target's ranked event table."""
    ranked = rank_events_for_target(observations, player_id, direction)
    if count > len(ranked):
        raise ValueError(
            f"Requested {count} events but {player_id} has only "
            f"{len(ranked)} {direction} candidates"
        )
    return ranked["event_id"].head(count).tolist()


def write_drop_list(path, event_ids):
    """Write one event id per line; parents are created."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(f"{event_id}\n" for event_id in event_ids))
