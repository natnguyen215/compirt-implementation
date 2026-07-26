"""Stratified whole-game k-fold holdout for matrix-infill evaluation.

Where 'round_splits' holds out each tournament's *final* fraction of rounds for
a temporal test, this module holds out whole games spread *evenly* across every
tournament and round, so the test set carries no late-round / playoff bias. It
is the split behind the frozen "matrix infill" question: given players and
questions already estimated on the training games, can the model fill in the
held-out player x question interactions?

A derived split has the form::

    game-holdout:<base-split>:<train|test>:<n_folds>:<fold_index>:<seed>

For example, ``game-holdout:year_2024:test:5:0:42`` is fold 0 of a 5-fold split
(each fold ~20% of games) seeded at 42.  Games are assigned to folds within each
``(tournament_id, round)`` group by a seeded round-robin, so every group is
spread across all folds.  A **coverage pass** then moves any test game back to
train if it references a player, tossup, or bonus not otherwise seen in
training, because the frozen scorer needs a training-fit parameter for every
test entity.  Selection is always at the whole-game grain, so an event's shared
first-buzz outcome is never split across train and test.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd

from holdout.round_splits import _tables_for_games


GAME_HOLDOUT_PREFIX = "game-holdout"


@dataclass(frozen=True)
class GameHoldoutSpec:
    """Parsed description of one side of a stratified whole-game holdout."""

    base_split: str
    part: str
    n_folds: int
    fold_index: int
    seed: int


def game_holdout_split_name(
    base_split: str, part: str, n_folds: int, fold_index: int, seed: int
) -> str:
    """Return the canonical loader split name for a game holdout."""
    if not base_split or ":" in base_split:
        raise ValueError("base_split must be a non-empty dataset split name")
    if part not in {"train", "test"}:
        raise ValueError("game holdout part must be 'train' or 'test'")
    n_folds = int(n_folds)
    fold_index = int(fold_index)
    seed = int(seed)
    if n_folds < 2:
        raise ValueError("game holdout n_folds must be at least 2")
    if not 0 <= fold_index < n_folds:
        raise ValueError("game holdout fold_index must be in [0, n_folds)")
    return f"{GAME_HOLDOUT_PREFIX}:{base_split}:{part}:{n_folds}:{fold_index}:{seed}"


def parse_game_holdout_split(split: str) -> GameHoldoutSpec | None:
    """Parse a derived split name, returning ``None`` for ordinary splits."""
    if not split.startswith(f"{GAME_HOLDOUT_PREFIX}:"):
        return None
    pieces = split.split(":")
    if len(pieces) != 6:
        raise ValueError(
            "game holdout splits must use "
            "'game-holdout:<base-split>:<train|test>:<n_folds>:<fold_index>:<seed>'"
        )
    _, base_split, part, raw_folds, raw_index, raw_seed = pieces
    try:
        n_folds = int(raw_folds)
        fold_index = int(raw_index)
        seed = int(raw_seed)
    except ValueError as error:
        raise ValueError(
            "game holdout n_folds, fold_index, and seed must be integers, got "
            f"{raw_folds!r}, {raw_index!r}, {raw_seed!r}"
        ) from error
    # Reuse the public constructor's validation without depending on its text.
    game_holdout_split_name(base_split, part, n_folds, fold_index, seed)
    return GameHoldoutSpec(base_split, part, n_folds, fold_index, seed)


def game_holdout_fold_assignment(
    games: pd.DataFrame, n_folds: int, seed: int
) -> pd.Series:
    """Assign each game to a fold, spreading each round group across folds.

    Games are grouped by ``(tournament_id, round)``.  Within a group the game
    IDs are sorted for reproducibility and permuted by a seed-derived
    generator, then fold labels are dealt from a single running counter that
    *continues* across groups rather than restarting at fold 0 each time.
    Continuing the deal keeps every group's games in distinct folds (so each
    round is spread across folds) while balancing the folds globally to within
    one game -- restarting each group at 0 would pile small groups onto the
    low-numbered folds.  The generator (start offset and per-group permutations)
    is advanced over groups in sorted key order, so the assignment depends only
    on ``seed`` and the data, never on input row order.
    """
    if "tournament_id" not in games or "round" not in games:
        raise ValueError("games table needs 'tournament_id' and 'round' columns")
    n_folds = int(n_folds)
    rng = np.random.default_rng(int(seed))

    keys = list(zip(games["tournament_id"].astype("string"), games["round"].astype("string")))
    members: dict[tuple, list[str]] = {}
    for key, game_id in zip(keys, games["game_id"].astype(str)):
        members.setdefault(key, []).append(game_id)

    fold_of: dict[str, int] = {}
    position = int(rng.integers(n_folds))
    for key in sorted(members, key=lambda k: (str(k[0]), str(k[1]))):
        group = sorted(members[key])
        for slot in rng.permutation(len(group)):
            fold_of[group[slot]] = position % n_folds
            position += 1
    return games["game_id"].astype(str).map(fold_of).astype(int)


def _per_game_entities(tables: dict[str, pd.DataFrame]):
    """Return per-game sets of buzzer players, tossups, and bonuses.

    These are the entities a game contributes to training observations, so a
    test game is "covered" only if every one of them also appears in some
    training game.
    """
    buzzes = tables["tossup_buzzes"]
    responses = tables["bonus_responses"]

    def grouped_sets(frame, key, value):
        if frame.empty or key not in frame or value not in frame:
            return {}
        return {
            str(game_id): set(group.astype(str))
            for game_id, group in frame.groupby(key)[value]
        }

    return (
        grouped_sets(buzzes, "game_id", "player_id"),
        grouped_sets(buzzes, "game_id", "tossup_id"),
        grouped_sets(responses, "game_id", "bonus_id"),
    )


def game_holdout_masks(tables: dict[str, pd.DataFrame], spec: GameHoldoutSpec) -> pd.Series:
    """Return a boolean mask selecting this fold's coverage-guaranteed test games.

    Games start in test iff they fall in ``spec.fold_index``.  A test game is
    then moved back to train if it references a player, tossup, or bonus absent
    from the current training games.  Moving a game into train only grows
    training coverage, so the pass shrinks the test set monotonically to a fixed
    point where every remaining test game is fully covered.
    """
    games = tables["games"]
    assignment = game_holdout_fold_assignment(games, spec.n_folds, spec.seed)
    game_ids = games["game_id"].astype(str).tolist()
    is_test = dict(zip(game_ids, (assignment == spec.fold_index).tolist()))

    game_players, game_tossups, game_bonuses = _per_game_entities(tables)
    empty: set = set()

    while True:
        train_players: set = set()
        train_tossups: set = set()
        train_bonuses: set = set()
        for game_id in game_ids:
            if is_test[game_id]:
                continue
            train_players |= game_players.get(game_id, empty)
            train_tossups |= game_tossups.get(game_id, empty)
            train_bonuses |= game_bonuses.get(game_id, empty)

        moved = False
        for game_id in game_ids:
            if not is_test[game_id]:
                continue
            covered = (
                game_players.get(game_id, empty) <= train_players
                and game_tossups.get(game_id, empty) <= train_tossups
                and game_bonuses.get(game_id, empty) <= train_bonuses
            )
            if not covered:
                is_test[game_id] = False
                moved = True
        if not moved:
            break

    return pd.Series([is_test[gid] for gid in game_ids], index=games.index)


def select_game_holdout_tables(
    tables: dict[str, pd.DataFrame], spec: GameHoldoutSpec
) -> dict[str, pd.DataFrame]:
    """Return linked tables for the train or test side of a game holdout."""
    held_out = game_holdout_masks(tables, spec)
    selected = held_out if spec.part == "test" else ~held_out
    return _tables_for_games(tables, tables["games"].loc[selected])
