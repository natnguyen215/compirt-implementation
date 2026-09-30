"""Held-out bonus metrics split by whether the exact team roster was seen in training.

Reads the saved bonus_part_predictions.csv files of every compositional run and
the multidimensional reference; no model is refit. Run from the repository root:

    .venv/bin/python analysis/compositional/novel_roster_metrics.py

Outputs go to the reference run's aggregate/ directory: novel_roster_metrics.csv,
bonus_metrics_report.md, the bonus PPG summaries, and per-model outcome tables
under bonus_metrics/.
"""

import ast
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import numpy as np
import pandas as pd
from sklearn.metrics import log_loss, roc_auc_score

from compirt_data import load_hf_tables
from compirt_eval.common.reports import markdown_table
from compirt_eval.scenario_b_bonuses.metrics import bonus_accuracy_by_difficulty, bonus_parts_with_difficulty
from compirt_eval.scenario_b_bonuses.outcomes import write_bonus_outcomes

HOLDOUT = Path("results/compirt/holdout")
# The DD reference run. Its aggregate/ directory receives this analysis's outputs.
RUN = HOLDOUT / "double-difficulty/compositional/no-synergy-and-dot-additive-1d"
MULTIDIM_RUN = HOLDOUT / "multidim/multidim-all2024-gameinfill-5fold"
LEVELS = ("easy", "medium", "hard")


def comparison_runs():
    """Return {label: run directory} for both references and every other compositional run."""
    runs = {"Multidim": MULTIDIM_RUN, "DD-Bernstein": RUN}
    for manifest in sorted(RUN.parent.glob("*/configuration.json")):
        if manifest.parent == RUN:
            continue
        config = json.loads(manifest.read_text())
        if config.get("bonus_aggregation") == "noisy-or":
            label = "DD Noisy-OR"
        else:
            difficulty = "multidim difficulty " if config.get("bonus_difficulty") == "multidim" else ""
            if config.get("bonus_aggregation") == "max":
                difficulty = "max skill " + difficulty
            label = (f"DD {difficulty}{config.get('synergy_link', 'additive')} "
                     f"{config.get('synergy_form', 'dot')} {config.get('synergy_dimensions', 1)}D")
        if label in runs:
            raise ValueError(f"Duplicate comparison label: {label}")
        runs[label] = manifest.parent
    return runs


def roster_key(frame):
    """Return each row's (team, roster) key and its roster as a player set."""
    rosters = {value: frozenset(ast.literal_eval(value)) for value in frame["player_ids"].unique()}
    players = frame["player_ids"].map(rosters)
    return list(zip(frame["team_id"], players)), players


def load_grouped_predictions(runs):
    """Load every held-out prediction and label its roster group.

    A roster is familiar when the same team used the same player set in the
    fold's training bonuses. New rosters are split by whether every player
    appeared in training. Also returns per-fold familiar-response counts.
    """
    rows, familiar_counts = [], []
    for model, run in runs.items():
        manifest = run / "configuration.json"
        arms = json.loads(manifest.read_text())["arms"] if manifest.exists() else ["compositional", "synergy"]
        for fold in range(5):
            # Every arm trains on the same bonuses, so the first arm's rows define familiarity.
            train = pd.read_csv(run / f"fold_{fold}/train/{arms[0]}/bonus_part_predictions.csv")
            train_keys, train_players = roster_key(train)
            seen_rosters = set(train_keys)
            seen_players = set().union(*train_players)

            for arm in arms:
                test = pd.read_csv(run / f"fold_{fold}/holdout/{arm}/bonus_part_predictions.csv")
                keys, players = roster_key(test)
                familiar = np.array([k in seen_rosters for k in keys])
                all_players_seen = players.map(lambda p: p <= seen_players).to_numpy()
                test["group"] = np.where(
                    familiar,
                    "familiar roster",
                    np.where(all_players_seen, "new roster, known players", "new roster, unseen player"),
                )
                test["model"], test["arm"], test["fold"] = model, arm, fold
                rows.append(test)
                if arm == "synergy":
                    familiar_counts.append(
                        (model, fold, test["response_id"].nunique(),
                         test.loc[familiar, "response_id"].nunique())
                    )
    return pd.concat(rows, ignore_index=True), familiar_counts


def group_metrics(group):
    """Return part, exact-bonus, and difficulty metrics for one prediction group."""
    p = group["predicted_correct"].clip(1e-7, 1 - 1e-7).to_numpy()
    y = group["correct"].to_numpy()
    hit = (p >= 0.5) == (y == 1)
    exact = pd.Series(hit).groupby(group["response_id"].to_numpy()).all()
    difficulty = bonus_accuracy_by_difficulty(group).set_index("difficulty")
    return pd.Series({
        "bonuses": group["response_id"].nunique(),
        "part_acc": hit.mean(),
        "exact_acc": exact.mean(),
        "auc": roc_auc_score(y, p),
        "log_loss": log_loss(y, p),
        "pred_minus_obs": p.mean() - y.mean(),
        "mean_synergy": group["synergy_contribution"].mean(),
        **{f"{level}_part_acc": difficulty.loc[level, "part_accuracy"] for level in LEVELS},
        **{f"{level}_parts": difficulty.loc[level, "parts"] for level in (*LEVELS, "unknown")},
    })


def difficulty_report_lines(data, summary):
    """Return one accuracy table per roster group, each with its always-correct baseline."""
    display = summary[["model", "group", "arm", "bonuses", "part_acc", "easy_part_acc",
                       "medium_part_acc", "hard_part_acc", "exact_acc", "auc", "log_loss"]].copy()
    for column in ("part_acc", "easy_part_acc", "medium_part_acc", "hard_part_acc", "exact_acc"):
        display[column] = display[column].map(lambda value: f"{value:.2%}")
    # One row per scored part, so the baseline counts each part once across models.
    baseline_parts = data.drop_duplicates(["response_id", "part_index"])
    baseline = baseline_parts.groupby("difficulty")["correct"].mean()
    lines = [
        "The always-predict-correct baseline over all rosters is "
        + ", ".join(f"{baseline[level]:.2%} {level}" for level in LEVELS)
        + ". This equals the observed correct-answer rate. Baselines are shared by "
        "both models and synergy settings; n counts parts per configuration.", "",
    ]
    for group, frame in display.groupby("group", sort=False):
        headers = {"model": "Model", "arm": "Synergy", "bonuses": "Bonuses",
                   "part_acc": "Part acc. ↑", "exact_acc": "Exact bonus acc. ↑",
                   "auc": "AUC ↑", "log_loss": "Log loss ↓"}
        for level in LEVELS:
            counts = summary.loc[summary["group"] == group, f"{level}_parts"].unique()
            if len(counts) != 1:
                raise ValueError(f"Different {level} denominators across configurations for {group}")
            headers[f"{level}_part_acc"] = f"{level.title()} acc. ↑ (n = {int(counts[0]):,})"
        frame = frame.drop(columns="group").copy()
        frame["arm"] = frame["arm"].map({"compositional": "off", "synergy": "on"})
        group_baseline = baseline_parts[baseline_parts["group"] == group].groupby("difficulty")["correct"].mean()
        lines += [f"## {group.capitalize()}", "", markdown_table(frame.rename(columns=headers)), "",
                  "Always-predict-correct baseline: "
                  + ", ".join(f"{group_baseline[level]:.2%} {level}" for level in LEVELS)
                  + ".", ""]
    return lines


def main(output_dir=RUN / "aggregate"):
    output_dir = Path(output_dir)
    data, familiar_counts = load_grouped_predictions(comparison_runs())
    tables = load_hf_tables(split="year_2024")
    data = bonus_parts_with_difficulty(data, tables["bonuses"])
    # Familiar counts should match aggregate/roster_familiarity.json.
    print(pd.DataFrame(familiar_counts, columns=["model", "fold", "responses", "familiar"]))

    summary = (
        data.groupby(["model", "group", "arm"])
        .apply(group_metrics, include_groups=False)
        .reset_index()
    )
    summary.to_csv(output_dir / "novel_roster_metrics.csv", index=False)
    pd.set_option("display.width", 200)
    print(summary.round(4).to_string(index=False))

    # Team PPG and margins pool every roster group, since one tournament mixes them.
    ppg_rows, tournament_rows = [], []
    for (model, arm), parts in data.groupby(["model", "arm"]):
        output = output_dir / "bonus_metrics" / model / arm
        ppg_rows.append({"model": model, "arm": arm, **write_bonus_outcomes(parts, tables, output)})
        tournaments = pd.read_csv(output / "bonus_team_ranking_metrics.csv")
        tournament_rows.append(tournaments.assign(model=model, arm=arm))
    ppg_summary = pd.DataFrame(ppg_rows)
    ppg_summary.to_csv(output_dir / "bonus_ppg_summary.csv", index=False)
    tournaments = pd.concat(tournament_rows, ignore_index=True)
    tournaments.to_csv(output_dir / "bonus_ppg_by_tournament.csv", index=False)

    lines = ["# Bonus difficulty, team tournament PPG and game margins", "",
             "Saved predictions from the same five whole-game folds as the original "
             "comparison, scored without refitting. DD sources use skills from the "
             "normalized first-buzz likelihood. Difficulty is the source's declared "
             "easy/medium/hard part label. Each roster group has one easy, one medium, "
             "and one hard part per bonus.", "",
             *difficulty_report_lines(data, summary),
             "## Bonus-only team PPG and margins", "",
             "Sum each team's observed or expected points on its recorded bonuses. "
             "Expected response points are 10 times the sum of the three "
             "part probabilities. Divide by unique games played, including zero-bonus games. "
             "All held-out folds are pooled before computing "
             "team PPG. Each team's absolute PPG error is in the leaderboard CSV; tournament "
             "MAE averages these errors. Spearman ranks teams within each mirror tournament "
             "with average ranks for ties, and its macro mean covers tournaments with a "
             "defined correlation. Games with incomplete bonus predictions are excluded "
             "entirely. Bonus margin is team A's points minus team B's "
             "in a game, with teams ordered by ID. Its MAE averages absolute errors in these "
             "signed margins, one vote per game. Both metrics condition on the observed "
             "bonus opportunities.", "", markdown_table(ppg_summary), "",
             "[All tournament metrics](bonus_ppg_by_tournament.csv). "
             "The PPG summary averages tournaments equally after computing their metrics; "
             "the overall margin MAE weights games equally.", ""]
    for row in ppg_rows:
        prefix = f"bonus_metrics/{row['model']}/{row['arm']}"
        lines.append(f"- {row['model']} {row['arm']}: [team PPG and errors]({prefix}/bonus_team_ppg_leaderboard.csv), "
                     f"[team-game totals]({prefix}/bonus_team_game_predictions.csv), "
                     f"[game margins]({prefix}/bonus_game_margin_predictions.csv).")
    lines += ["", "## Per-tournament results", "", markdown_table(tournaments)]
    (output_dir / "bonus_metrics_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(ppg_summary.round(4).to_string(index=False))


if __name__ == "__main__":
    main()
