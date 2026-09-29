"""Compare frozen skill/correctness game scores with saved full tossup replay.

Run from the repository root with .venv/bin/python -B <this file>.
Correctness is evaluated at the observed first-buzz position for every active
player, or the terminal cell on dead tossups. This is conditional evaluation.
"""
from pathlib import Path
import hashlib
import json
import sys

ROOT = next(path for path in Path(__file__).resolve().parents if (path / "compirt_eval").is_dir())
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import numpy as np
import pandas as pd
from scipy.special import expit

from compirt_eval.common.figures import numeric_columns
from compirt_eval.scenario_a_tossups.parameters import (
    _parameter_columns, _saved_difficulty_curve,
    load_difficulty_link, load_difficulty_scale, load_terminal_intercepts,
)
from utils.run_logging import resolve_result_root

BASE = ROOT / "results/compirt/holdout"
REPLAY = BASE / "common/token-threshold-replay/buzz-0p5-correctness-0p5-random-ties-seed42"
CONFIGS = [
    ("DD-Bernstein historical (bonus reference)",
     BASE / "double-difficulty/ablations/model-components/relevance-locations-terminal/dd-bernstein-332-simplex-locations-terminal",
     REPLAY / "simplex-relevance-locations-terminal", "fold_{fold}/csvs/tossup_game_predictions.csv"),
    ("DD-Bernstein historical (unconstrained terminal)",
     BASE / "double-difficulty/ablations/model-components/relevance-locations-terminal/dd-bernstein-332-unconstrained-terminal",
     REPLAY / "dd-bernstein-3-3-2-terminal", "fold_{fold}/csvs/tossup_game_predictions.csv"),
    ("DD-Bernstein normalized 3000 steps",
     BASE / "double-difficulty/likelihood-refits/dd-bernstein-332-simplex-locations-terminal-normalized-first-buzz-3000steps",
     BASE / "double-difficulty/likelihood-refits/dd-bernstein-332-simplex-locations-terminal-normalized-first-buzz-3000steps",
     "fold_{fold}/holdout/evaluation/csvs/tossup_game_predictions.csv"),
    ("Multidimensional normalized 3000 steps",
     BASE / "multidim/likelihood-refits/multidim-5d-normalized-first-buzz-3000steps-5fold",
     BASE / "multidim/likelihood-refits/multidim-5d-normalized-first-buzz-3000steps-5fold",
     "fold_{fold}/holdout/evaluation/csvs/tossup_game_predictions.csv"),
]
KEYS = ["game_id", "event_id", "team_id"]
METHODS = ["lse", "dimensionwise_lse", "scalar_sum", "correctness"]


def grouped_lse(frame, columns):
    """Stable LSE across the active players in each team-question lineup."""
    grouped = frame.groupby(KEYS)[columns]
    maxima = grouped.transform("max")
    shifted = frame[KEYS].copy()
    shifted[columns] = np.exp(frame[columns] - maxima)
    return np.log(shifted.groupby(KEYS)[columns].sum()) + grouped.max()


def correctness_logits(raw, players, tossups, source):
    """Reconstruct canonical correctness at each event's observed stopping cell."""
    theta = numeric_columns(players, "theta_")
    weights = _parameter_columns(tossups)["alpha"]
    assert len(theta) == len(weights) > 0
    positions = (raw.t_star / raw.T_j).to_numpy()
    difficulty = np.empty(len(raw))
    link, scale = load_difficulty_link(source), load_difficulty_scale(source)
    for tossup_id, indices in raw.groupby("tossup_id").indices.items():
        curve = _saved_difficulty_curve(tossups.loc[tossup_id], positions[indices], link, scale)
        if curve is None:
            raise ValueError(f"Cannot reconstruct {tossup_id}")
        difficulty[indices] = curve
    logits = np.einsum("ij,ij->i", players.loc[raw.player_id, theta].to_numpy(),
                       tossups.loc[raw.tossup_id, weights].to_numpy()) - difficulty
    if "a" in players:
        logits += players.loc[raw.player_id, "a"].to_numpy()
    end_correct, _ = load_terminal_intercepts(source)
    logits += end_correct * raw.t_star.eq(raw.T_j).to_numpy()
    metadata = json.loads((source / "summary.json").read_text())
    # These four saved arms have identity calibration; reject silent protocol changes.
    assert metadata.get("correctness_scale", 1.0) == 1.0
    assert metadata.get("correctness_bias", 0.0) == 0.0
    assert np.isfinite(logits).all()
    # Independent agreement with the trainers' saved row probabilities.
    np.testing.assert_allclose(expit(logits), raw.predicted_correct, atol=2e-6, rtol=2e-5)
    return logits


def evaluate_fold(label, root, replay, pattern, fold):
    source = root / f"fold_{fold}/holdout/pyramidal"
    train_path = root / f"fold_{fold}/train/pyramidal/players.csv"
    skills = pd.read_csv(train_path).set_index("player_id")
    heldout = pd.read_csv(source / "players.csv").set_index("player_id")
    tossups = pd.read_csv(source / "tossups.csv").set_index("tossup_id")
    theta = numeric_columns(skills, "theta_")
    shared = heldout.index.intersection(skills.index)
    np.testing.assert_allclose(heldout.loc[shared, theta], skills.loc[shared, theta])
    game_path = replay / pattern.format(fold=fold)
    games = pd.read_csv(game_path)
    assert games.evaluation_method.eq("token_threshold_replay").all()
    assert games.tossup_outcome_schema_version.eq(3).all()
    raw = pd.read_csv(source / "tossup_predictions.csv", usecols=[
        "game_id", "event_id", "team_id", "player_id", "tossup_id", "phase",
        "t_star", "T_j", "z", "predicted_correct",
    ])
    raw = raw[raw.phase.eq(0) & raw.game_id.isin(games.game_id)].reset_index(drop=True)
    assert not raw.duplicated(["event_id", "player_id"]).any()
    assert set(raw.player_id) <= set(skills.index)
    assert raw.groupby("event_id")[["t_star", "T_j", "tossup_id"]].nunique().eq(1).all().all()
    assert raw.t_star.between(1, raw.T_j).all()
    assert raw.loc[raw.z.eq("NO-BUZZ"), "t_star"].eq(raw.loc[raw.z.eq("NO-BUZZ"), "T_j"]).all()
    raw["correctness_logit"] = correctness_logits(raw, heldout, tossups, source)
    raw = raw.join(skills[theta], on="player_id", validate="many_to_one")
    raw["scalar_skill"] = raw[theta].mean(axis=1)
    raw["summed_skill"] = raw[theta].sum(axis=1)
    aggregates = grouped_lse(raw, ["scalar_skill", "summed_skill", "correctness_logit", *theta])
    scores = pd.DataFrame({
        "lse": aggregates.scalar_skill,
        "scalar_sum": aggregates.summed_skill,
        "dimensionwise_lse": aggregates[theta].mean(axis=1),
        # This is a team scoring surrogate, not a calibrated chance to win a race.
        "correctness": expit(aggregates.correctness_logit),
    })
    averages = scores.groupby(["game_id", "team_id"]).mean()
    coverage = scores.groupby(["game_id", "team_id"]).size()
    for side in (1, 2):
        index = pd.MultiIndex.from_frame(games[["game_id", f"team_{side}_id"]])
        np.testing.assert_array_equal(coverage.reindex(index), games.usable_tossups)
        for method in METHODS:
            games[f"{method}_team_{side}"] = averages[method].reindex(index).to_numpy()
    for method in METHODS:
        delta = games[f"{method}_team_1"] - games[f"{method}_team_2"]
        assert np.isfinite(delta).all()
        games[f"{method}_winner"] = np.where(
            np.isclose(delta, 0, atol=1e-12, rtol=0), "tie",
            np.where(delta > 0, games.team_1_id, games.team_2_id))
        games[f"{method}_correct"] = games[f"{method}_winner"].eq(games.actual_tossup_winner)
    games["replay_correct"] = games.predicted_tossup_winner.eq(games.actual_tossup_winner)
    games["model"], games["fold"] = label, fold
    events = raw.drop_duplicates("event_id")
    signatures = {}
    for path in [train_path, game_path, *(source / name for name in (
        "players.csv", "tossups.csv", "tossup_predictions.csv", "summary.json"))]:
        with path.open("rb") as handle:
            signatures[str(path.relative_to(ROOT))] = hashlib.file_digest(handle, "sha256").hexdigest()
    audit = {"model": label, "fold": fold, "events": len(events),
             "no_buzz_events": raw.loc[raw.z.eq("NO-BUZZ"), "event_id"].nunique(),
             "sha256": signatures}
    return games, audit


def main():
    output = Path(resolve_result_root(Path(__file__).resolve().parents[1], tier="holdout"))
    frames, audits = [], []
    for label, root, replay, pattern in CONFIGS:
        for fold in range(5):
            games, audit = evaluate_fold(label, root, replay, pattern, fold)
            frames.append(games)
            audits.append(audit)
            print(f"Completed {label}, fold {fold}", flush=True)
    allgames = pd.concat(frames, ignore_index=True)
    assert not allgames.duplicated(["model", "game_id"]).any()
    populations = [set(group.game_id) for _, group in allgames.groupby("model")]
    assert all(population == populations[0] for population in populations)
    assert allgames.groupby("game_id")[["actual_tossup_winner", "actual_tossup_margin"]].nunique().eq(1).all().all()
    rows = []
    for label, games in allgames.groupby("model", sort=False):
        decisive = games[games.actual_tossup_winner.ne("tie")]
        row = {"model": label, "complete_games": len(games), "decisive_games": len(decisive)}
        for method in [*METHODS, "replay"]:
            row[f"{method}_correct_games"] = int(decisive[f"{method}_correct"].sum())
            row[f"{method}_accuracy"] = float(decisive[f"{method}_correct"].mean())
        row["correctness_ties"] = int(decisive.correctness_winner.eq("tie").sum())
        row["replay_ties"] = int(decisive.predicted_tossup_winner.eq("tie").sum())
        rows.append(row)
    summary = pd.DataFrame(rows)
    output.mkdir(parents=True, exist_ok=True)
    allgames.to_csv(output / "game_predictions.csv", index=False)
    summary.to_csv(output / "summary.csv", index=False)
    (output / "validation.json").write_text(json.dumps(audits, indent=2) + "\n")
    print(summary.to_string(index=False))


if __name__ == "__main__":
    main()
