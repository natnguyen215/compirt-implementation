"""Generated Markdown reports for saved CompIRT evaluation artifacts.

Everything a reader can consume without loading pandas. Two products:

* 'experiment_report_markdown' -- the per-run 'experiment_report.md'. It opens
  with the estimation-regime caveats ('evaluation_regime_notes'), then renders
  the Stage 1 and Stage 2 metric rows grouped into themed tables
  ('TOSSUP_METRIC_GROUPS' / 'BONUS_METRIC_GROUPS', with short interpretation
  notes), the buzz-position bias bands, the synergy section (synergy branch
  only), tossup game replay, and calibration by stratum.
* 'write_eval_docs_summary' -- 'docs/summary.md', which consolidates the metric
  CSVs, no-synergy-versus-synergy comparison deltas, and fitted-parameter
  distribution summaries for one evaluation folder.

Metrics absent from every group are never dropped: they collect under "Other
Metrics" in the report and are appended by '_metric_frame' in the summary. The
result-layout helpers ('stage_base_for_evaluation', 'result_root_for_evaluation',
'bonus_stage_name', ...) recover a run's stage directories and regime from the
enforced 'results/compirt/{in_sample,holdout}/...' path. 'METRICS.md' is the
full mathematical contract; the notes here only make the report self-contained.
"""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd
from pandas.errors import EmptyDataError

from compirt_eval.common.report_paths import metrics_path


# Metric groups drive the section layout of 'experiment_report.md' and the row
# order of 'docs/summary.md'. Metrics absent from every group still render,
# collected under "Other Metrics" / appended by '_metric_frame'.
TOSSUP_METRIC_GROUPS: list[tuple[str, list[str]]] = [
    (
        "Buzz Correctness (scored on actual first buzzes)",
        [
            "auc",
            "log_loss",
            "ece",
            "brier",
            "accuracy",
            "all_correct_accuracy",
            "accuracy_lift_over_all_correct",
        ],
    ),
    (
        "Correctness Probability Sharpness",
        [
            "probability_std",
            "probability_p10",
            "probability_p50",
            "probability_p90",
            "mean_predictive_variance",
        ],
    ),
    (
        "Buzz Timing (survival replay over all lineup rows)",
        [
            "integrated_brier_score",
            "joint_tossup_event_log_loss",
            "buzz_position_mae",
            "buzz_position_median_absolute_error",
            "buzz_position_bias",
            "survival_events",
            "joint_tossup_event_log_loss_events",
        ],
    ),
    (
        "First-Buzzer Identity (who buzzes first)",
        [
            "first_buzzer_top1_accuracy",
            "first_buzzer_mean_reciprocal_rank",
            "first_buzzer_log_loss",
            "first_buzzer_events",
        ],
    ),
    (
        "Token Replay: Tossup Outcomes, Games, and Tournament PPG",
        [
            "first_buzzer_player_replay_accuracy",
            "first_buzzer_team_replay_accuracy",
            "tossup_scorer_player_replay_accuracy",
            "tossup_scorer_team_replay_accuracy",
            "tossup_game_winner_accuracy",
            "tossup_game_margin_mae",
            "tossup_game_zero_margin_mae",
            "tournament_player_ppg_spearman",
            "tournament_player_ppg_mae",
            "tournament_player_ppg_top10_overlap",
            "tournament_player_ppg_top10_random_overlap",
            "tournament_player_ppg_top10_adjusted_overlap",
        ],
    ),
]
BONUS_METRIC_GROUPS: list[tuple[str, list[str]]] = [
    (
        "Bonus-Only Team PPG (recorded opportunities)",
        ["tournament_team_bonus_ppg_mae", "tournament_team_bonus_ppg_spearman",
         "bonus_ppg_tournaments", "bonus_ppg_spearman_tournaments",
         "bonus_ppg_games", "bonus_ppg_incomplete_games"],
    ),
    (
        "Bonus-Only Game Margins (recorded opportunities)",
        ["bonus_game_margin_mae", "bonus_game_margin_mae_games"],
    ),
    (
        "Part-Level Correctness",
        [
            "auc",
            "log_loss",
            "ece",
            "brier",
            "part_accuracy",
            "part_accuracy_easy",
            "part_accuracy_medium",
            "part_accuracy_hard",
            "part_accuracy_unknown",
            "part_all_correct_accuracy",
            "accuracy_lift_over_all_correct",
            "part_accuracy_macro_team",
            "part_accuracy_macro_bonus",
            "part_count_easy",
            "part_count_medium",
            "part_count_hard",
            "part_count_unknown",
        ],
    ),
    (
        "Part Probability Sharpness",
        [
            "probability_std",
            "probability_p10",
            "probability_p50",
            "probability_p90",
            "mean_predictive_variance",
        ],
    ),
    (
        "Bonus-Level Score (0/10/20/30 totals and PPB)",
        [
            "exact_acc",
            "ranked_probability_score",
            "bonus_total_score_log_loss",
            "ppb_mae",
            "ranked_probability_score_responses",
            "bonus_total_score_log_loss_responses",
        ],
    ),
]
TOSSUP_METRICS = [name for _, names in TOSSUP_METRIC_GROUPS for name in names]
BONUS_METRICS = [name for _, names in BONUS_METRIC_GROUPS for name in names]
REPORT_HIDDEN_METRICS = {"survival_events_skipped"}

# Short definitions rendered beside the tables where readers encounter these
# less familiar metrics.  Keep the full mathematical contract in METRICS.md;
# these notes make the standalone experiment report interpretable.
METRIC_GROUP_NOTES = {
    "Bonus-Only Team PPG (recorded opportunities)": (
        "Team bonus totals are divided by games played, including zero-bonus games. "
        "MAE averages team PPG errors within tournaments, then weights tournaments equally; "
        "Spearman is also averaged across tournaments with defined correlations. "
        "Predictions use expected points on recorded bonus opportunities."
    ),
    "Bonus-Only Game Margins (recorded opportunities)": (
        "For each complete game, subtract team B's bonus points from team A's. "
        "MAE compares predicted and observed signed margins, weighting games equally. "
        "Predictions use expected points on recorded bonus opportunities."
    ),
    "Buzz Timing (survival replay over all lineup rows)": (
        "The survival replay reconstructs each event's probability that someone "
        "has buzzed by each relative question position. `integrated_brier_score` "
        "measures probability error over that curve (lower is better). "
        "`survival_events` is the number of events reconstructed and scored."
    ),
    "First-Buzzer Identity (who buzzes first)": (
        "These metrics use events with an observed buzz and a complete fitted "
        "roster. `first_buzzer_top1_accuracy` is the fraction where the model's "
        "highest-probability player was the observed first buzzer. "
        "`first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed "
        "buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. "
        "`first_buzzer_log_loss` averages the negative log probability assigned "
        "to the observed buzzer (lower is better), conditional on someone "
        "buzzing. `first_buzzer_events` is the shared denominator."
    ),
    "Token Replay: Tossup Outcomes, Games, and Tournament PPG": (
        "These Stage-1 metrics use literal recorded tossup values, including "
        "post-neg bouncebacks and zero-point late misses. Predicted outcomes "
        "replay every token until a player reaches 0.5 buzz probability, resolve "
        "correctness at 0.5, and continue with the opponent after an early miss. "
        "Games sum replayed tossup points. Full tournament rankings pool "
        "each game's out-of-fold prediction before computing PPG and ranks."
    ),
}

GAME_METRICS = [
    "tossup_game_winner_accuracy",
    "tossup_game_margin_mae",
    "tossup_game_zero_margin_mae",
    "tossup_game_margin_mae_games",
]

STRATUM_REPORT_COLUMNS = [
    "scenario",
    "stratum",
    "value",
    "observations",
    "ece",
    "brier",
    "auc",
    "log_loss",
]


def load_metrics_row(evaluation_dir: Path, filename: str) -> dict[str, object]:
    """Load one metrics CSV row from a nested or flat evaluation layout."""
    path = metrics_path(Path(evaluation_dir), filename)
    frame = _read_csv(path)
    if frame.empty:
        return {}
    return frame.iloc[0].to_dict()


def _metric_frame(row: dict[str, object], names: list[str]) -> pd.DataFrame:
    """Return a vertical metric table in requested order."""
    rows = []
    for name in names:
        if name in row and name not in REPORT_HIDDEN_METRICS:
            rows.append({"metric": name, "value": row[name]})
    for name, value in row.items():
        if name in names or name in REPORT_HIDDEN_METRICS:
            continue
        if pd.notna(pd.to_numeric(value, errors="coerce")):
            rows.append({"metric": name, "value": value})
    return pd.DataFrame(rows)


def _read_csv(path: Path) -> pd.DataFrame:
    """Read a CSV when present, otherwise return an empty frame."""
    if not path.exists():
        return pd.DataFrame()
    try:
        return pd.read_csv(path)
    except EmptyDataError:
        return pd.DataFrame()


def _read_json(path: Path) -> dict[str, object]:
    """Read a JSON object when present."""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def stage_base_for_evaluation(evaluation_dir: Path) -> Path:
    """Return the directory containing pyramidal/compositional/synergy stages."""
    evaluation_dir = Path(evaluation_dir)
    sibling_holdout = evaluation_dir.parent / "holdout"
    if sibling_holdout.is_dir():
        return sibling_holdout
    return evaluation_dir.parent


def result_root_for_evaluation(evaluation_dir: Path) -> Path:
    """Return the result root whose run.log describes this eval folder."""
    evaluation_dir = Path(evaluation_dir)
    if evaluation_dir.parent.name == "holdout":
        return evaluation_dir.parent.parent
    return evaluation_dir.parent


def comparison_path_for_evaluation(evaluation_dir: Path) -> Path:
    """Return the bonus-model comparison CSV path for an evaluation folder."""
    return (
        stage_base_for_evaluation(evaluation_dir)
        / "comparison"
        / "bonus_model_comparison.csv"
    )


def bonus_stage_name(evaluation_dir: Path) -> str:
    """Return the bonus-stage directory used by this eval folder."""
    if Path(evaluation_dir).name == "synergy-evaluation":
        return "synergy"
    return "compositional"


def evaluation_regime_notes(evaluation_dir: Path) -> list[str]:
    """Return caveat sentences stating what the reported metrics measure.

    The regime is inferred from the enforced results tier in the run path
    ('results/compirt/{in_sample,holdout}/...'); the calibration caveat comes
    from the Stage 1 'summary.json'. Rendered at the top of both
    'experiment_report.md' and 'docs/summary.md' so single numbers are never
    read without their estimation context.
    """
    evaluation_dir = Path(evaluation_dir)
    parts = {part.lower() for part in evaluation_dir.parts}
    pyramidal_summary = _read_json(
        stage_base_for_evaluation(evaluation_dir) / "pyramidal" / "summary.json"
    )
    bonus_summary = _read_json(
        stage_base_for_evaluation(evaluation_dir) / bonus_stage_name(evaluation_dir) / "summary.json"
    )
    if pyramidal_summary.get("frozen_predict") or (
        not pyramidal_summary and bonus_summary.get("frozen_predict")
    ):
        notes = [
            "**Evaluation regime: frozen matrix-infill holdout.** Player and "
            "question parameters were fit on the training folds and replayed "
            "on held-out games without fitting any held-out outcomes."
        ]
    elif "in_sample" in parts:
        notes = [
            "**Evaluation regime: in-sample fit.** Player and question "
            "parameters were estimated on the same observations these metrics "
            "score, so they are optimization and inspection diagnostics, not "
            "generalization estimates."
        ]
    elif "holdout" in parts:
        notes = [
            "**Evaluation regime: transductive temporal holdout.** "
            "Returning-player priors come from the training split, but "
            "question parameters are co-estimated on the test-split outcomes "
            "being scored (paper Section 4.2), so these metrics are not fully "
            "inductive predictions of unseen questions."
        ]
    else:
        notes = [
            "**Evaluation regime: unlabeled run layout.** If this run was fit "
            "on the same split it is scored on, read these metrics as "
            "in-sample fit."
        ]
    if pyramidal_summary.get("calibrate_correctness"):
        notes.append(
            "**Correctness calibration was fit on the scored outcomes.** This "
            "run learned a Platt scale/bias on the same split these metrics "
            "score, so tossup ECE and log loss are flattered by construction "
            "and are not comparable to uncalibrated runs."
        )
    return notes


def _display_tournament(value: object, evaluation_dir: Path) -> str:
    """Render an empty all-tournament selection in human terms when inferable."""
    if value not in (None, ""):
        return str(value)
    parts = {part.lower() for part in Path(evaluation_dir).parts}
    root_name = result_root_for_evaluation(evaluation_dir).name.lower()
    if "in_sample" in parts and ("all2024" in root_name or "all-2024" in root_name):
        return "all 2024"
    if "in_sample" in parts and "2024" in root_name:
        return "all 2024"
    return "all tournaments"


def _stage_dimensions(summary: dict[str, object]) -> object:
    """Return the single displayed dimensionality for a stage summary."""
    for field in ("dimensions", "topic_dimensions", "skill_dimensions"):
        value = summary.get(field)
        if value not in (None, ""):
            return value
    return None


def _stage_summary_rows(evaluation_dir: Path) -> pd.DataFrame:
    """Build a small table of run variables recoverable from stage summaries."""
    stage_base = stage_base_for_evaluation(evaluation_dir)
    paths = {
        "pyramidal": stage_base / "pyramidal" / "summary.json",
        bonus_stage_name(evaluation_dir): stage_base
        / bonus_stage_name(evaluation_dir)
        / "summary.json",
    }
    rows = []
    for stage, path in paths.items():
        summary = _read_json(path)
        if not summary:
            continue
        rows.append(
            {
                "stage": stage,
                "field": "tournament",
                "value": _display_tournament(summary.get("tournament"), evaluation_dir),
            }
        )
        dimensions = _stage_dimensions(summary)
        if dimensions is not None:
            rows.append({"stage": stage, "field": "dimensions", "value": dimensions})
        for field in (
            "steps",
            "final_loss",
            "calibrate_correctness",
            "synergy_dimensions",
            "synergy_form",
            "topic_vectors",
        ):
            if field in summary:
                rows.append({"stage": stage, "field": field, "value": summary[field]})
    return pd.DataFrame(rows)


def _bonus_scalar_rows(evaluation_dir: Path) -> pd.DataFrame:
    """Return bonus-stage scalars that are useful but not run variables."""
    stage_base = stage_base_for_evaluation(evaluation_dir)
    summary = _read_json(stage_base / bonus_stage_name(evaluation_dir) / "summary.json")
    rows = []
    for field in (
        "tau",
        "mean_synergy_contribution",
        "median_synergy_contribution",
        "negative_synergy_fraction",
        "positive_synergy_fraction",
    ):
        if field in summary:
            rows.append({"field": field, "value": summary[field]})
    return pd.DataFrame(rows)


def _parameter_summary(path: Path) -> pd.DataFrame:
    """Return the saved parameter summary with display-friendly columns."""
    frame = _read_csv(path)
    if frame.empty:
        return frame
    preferred = [
        "group",
        "parameter",
        "observations",
        "mean",
        "standard_deviation",
        "minimum",
        "p05",
        "p25",
        "median",
        "p75",
        "p95",
        "maximum",
    ]
    columns = [column for column in preferred if column in frame.columns]
    columns.extend(column for column in frame.columns if column not in columns)
    return frame[columns]


def _comparison_frame(comparison_csv: Path | None) -> pd.DataFrame:
    """Load no-synergy versus synergy comparison metrics if available."""
    if comparison_csv is None or not Path(comparison_csv).exists():
        return pd.DataFrame()
    return pd.read_csv(comparison_csv)


def _append_table(
    lines: list[str],
    title: str,
    frame: pd.DataFrame,
    empty_text: str,
) -> None:
    """Append a Markdown table or an explicit missing-data note."""
    lines.extend([f"## {title}", ""])
    if frame.empty:
        lines.extend([empty_text, ""])
        return
    lines.extend([markdown_table(frame), ""])


def _format_cell(value: object) -> str:
    """Format one Markdown table cell without optional dependencies."""
    if isinstance(value, (list, tuple, dict)):
        return json.dumps(value, sort_keys=True).replace("|", "\\|")
    if pd.isna(value):
        return ""
    if isinstance(value, float):
        return f"{value:.6g}"
    return str(value).replace("|", "\\|").replace("\n", " ")


def markdown_table(frame: pd.DataFrame) -> str:
    """Render a simple GitHub-flavored Markdown table."""
    columns = [str(column) for column in frame.columns]
    rows = ["| " + " | ".join(columns) + " |"]
    rows.append("| " + " | ".join("---" for _ in columns) + " |")
    for _, row in frame.iterrows():
        rows.append(
            "| "
            + " | ".join(_format_cell(row[column]) for column in frame.columns)
            + " |"
        )
    return "\n".join(rows)


def _grouped_metric_lines(
    row: dict[str, object], groups: list[tuple[str, list[str]]]
) -> list[str]:
    """Render one metrics row as themed metric/value tables, one per group."""
    lines: list[str] = []
    grouped_names = {name for _, names in groups for name in names}
    for group_title, names in groups:
        present = [
            name
            for name in names
            if name in row and name not in REPORT_HIDDEN_METRICS
        ]
        if not present:
            continue
        frame = pd.DataFrame(
            {"metric": present, "value": [row[name] for name in present]}
        )
        lines.extend([f"### {group_title}", ""])
        note = METRIC_GROUP_NOTES.get(group_title)
        if note:
            lines.extend([note, ""])
        lines.extend([markdown_table(frame), ""])
    leftovers = [
        name
        for name, value in row.items()
        if name not in grouped_names
        and name not in REPORT_HIDDEN_METRICS
        and pd.notna(pd.to_numeric(value, errors="coerce"))
    ]
    if leftovers:
        frame = pd.DataFrame(
            {"metric": leftovers, "value": [row[name] for name in leftovers]}
        )
        lines.extend(["### Other Metrics", "", markdown_table(frame), ""])
    return lines


def _position_bias_lines(evaluation_dir: Path) -> list[str]:
    """Render the signed buzz-position error table, overall and by band."""
    bias = _read_csv(metrics_path(Path(evaluation_dir), "buzz_position_bias.csv"))
    if bias.empty:
        return []
    return [
        "### Buzz-Position Bias",
        "",
        "Signed error is predicted minus observed position, so positive rows "
        "are predicted too late. Opposite-signed errors early and late in the "
        "question can cancel in the overall row; read the bands. Bands bin "
        "by observed position, which conditions on the noisy outcome, so "
        "band values are upper bounds on structural timing bias.",
        "",
        markdown_table(bias),
        "",
    ]


def _synergy_section_lines(evaluation_dir: Path) -> list[str]:
    """Render synergy-contribution scalars with their interpretation caveat.

    Only synergy-branch evaluations get this section. The response-weighted
    scalars come from the stage 'summary.json'; the distinct-lineup and
    distinct-team fractions are recomputed from the saved
    'team_synergy_contributions.csv' so teams that heard many bonuses do not
    dominate the headline fraction.
    """
    evaluation_dir = Path(evaluation_dir)
    if bonus_stage_name(evaluation_dir) != "synergy":
        return []
    stage_dir = stage_base_for_evaluation(evaluation_dir) / "synergy"
    summary = _read_json(stage_dir / "summary.json")
    if "mean_synergy_contribution" not in summary:
        return []
    rows = [
        {"field": field, "value": summary[field]}
        for field in (
            "mean_synergy_contribution",
            "median_synergy_contribution",
            "negative_synergy_fraction",
            "positive_synergy_fraction",
        )
        if field in summary
    ]
    contributions = _read_csv(stage_dir / "team_synergy_contributions.csv")
    if {"team_id", "player_ids", "synergy_contribution"}.issubset(
        contributions.columns
    ):
        lineups = contributions.drop_duplicates(subset=["team_id", "player_ids"])
        team_means = contributions.groupby("team_id")["synergy_contribution"].mean()
        rows.extend(
            [
                {"field": "distinct_lineups", "value": len(lineups)},
                {
                    "field": "negative_fraction_distinct_lineups",
                    "value": float((lineups["synergy_contribution"] < 0).mean()),
                },
                {"field": "distinct_teams", "value": len(team_means)},
                {
                    "field": "negative_fraction_distinct_teams",
                    "value": float((team_means < 0).mean()),
                },
            ]
        )
    formula = (
        "`sum over dimensions d and pairs i<j of phi_id phi_jd (psi_id + psi_jd)`"
        if summary.get("synergy_form", "dot") == "phi-psi" else
        "`sum over pairs i<j of psi_i . psi_j` (Eq. 10)"
    )
    return [
        "## Synergy Contributions",
        "",
        f"Each lineup's synergy contribution is the pairwise sum {formula} "
        "across its members, added to "
        "that team's aggregation logit for every bonus the lineup hears. The "
        "`*_synergy_fraction` rows weight each bonus response equally; the "
        "`distinct_*` rows count each lineup or team once.",
        "",
        markdown_table(pd.DataFrame(rows)),
        "",
        "**Read the sign as a fitted offset, not a teamwork measure.** With "
        "mostly fixed rosters this term can act as a team-level intercept — "
        "for example absorbing the unnormalized Eq. 8 log-sum-exp's growth "
        "with roster size — so a predominantly one-signed distribution says "
        "as much about the logit's other terms as about the teams. A "
        "held-out recombined-roster experiment is required "
        "before interpreting synergy as teamwork.",
        "",
    ]


def _stratum_table_lines(evaluation_dir: Path) -> list[str]:
    """Render the trimmed calibration-by-stratum table for the report."""
    diagnostics = _read_csv(
        metrics_path(Path(evaluation_dir), "prediction_diagnostics_by_stratum.csv")
    )
    if diagnostics.empty:
        diagnostics = _read_csv(
            metrics_path(
                Path(evaluation_dir),
                "tossup_prediction_diagnostics_by_stratum.csv",
            )
        )
    if diagnostics.empty:
        diagnostics = _read_csv(
            metrics_path(Path(evaluation_dir), "bonus_prediction_diagnostics_by_stratum.csv")
        )
    lines = ["## Calibration By Stratum", ""]
    if diagnostics.empty:
        lines.extend(["No stratified prediction diagnostics CSV was found.", ""])
        return lines
    columns = [
        column for column in STRATUM_REPORT_COLUMNS if column in diagnostics.columns
    ]
    lines.extend(
        [
            "Strata are fixed bands, not equal-count quantiles; read each row "
            "against its `observations` count. Sharpness columns stay in "
            "the diagnostic CSVs under `csvs/`.",
            "",
            markdown_table(diagnostics[columns]),
            "",
        ]
    )
    return lines


def experiment_report_markdown(
    evaluation_dir: Path,
    tossup: dict[str, object] | None,
    bonus: dict[str, object] | None,
    game: dict[str, object] | None = None,
    title: str = "CompIRT Experiment Report",
) -> str:
    """Render the readable per-run report from already-computed metric rows.

    Sections: regime caveats, grouped Stage 1/Stage 2 metric tables with the
    buzz-position bias bands, synergy contributions (synergy branch only),
    tossup game replay, and calibration by stratum; figures stay in
    'graphs/'. 'game=None' omits the game section entirely
    (evaluators that do not provide game summaries); an empty dict renders it with a
    skipped note.
    """
    lines = [f"# {title}", ""]
    for note in evaluation_regime_notes(evaluation_dir):
        lines.extend([note, ""])
    if tossup is not None:
        lines.extend(["## Stage 1: Tossup Metrics", ""])
        lines.extend(_grouped_metric_lines(tossup, TOSSUP_METRIC_GROUPS))
        lines.extend(_position_bias_lines(evaluation_dir))
    if bonus is not None:
        lines.extend(["## Stage 2: Bonus Metrics", ""])
        lines.extend(_grouped_metric_lines(bonus, BONUS_METRIC_GROUPS))
        bonus_rankings = _read_csv(metrics_path(evaluation_dir, "bonus_team_ranking_metrics.csv"))
        if not bonus_rankings.empty:
            lines.extend(["### Bonus-Only PPG by Tournament", "", markdown_table(bonus_rankings), "",
                          "[Team PPG and absolute errors](csvs/bonus_team_ppg_leaderboard.csv); "
                          "[game bonus margins](csvs/bonus_game_margin_predictions.csv).", ""])
        lines.extend(_synergy_section_lines(evaluation_dir))
    if game is not None:
        lines.extend(["## Tossup Game Replay", ""])
        if game:
            lines.extend([markdown_table(_metric_frame(game, GAME_METRICS)), ""])
        else:
            lines.extend(["Tossup game replay was unavailable.", ""])
    lines.extend(_stratum_table_lines(evaluation_dir))
    return "\n".join(lines).rstrip() + "\n"


def _summary_sections(
    evaluation_dir: Path,
    comparison_csv: Path | None,
    include_bonus: bool = True,
) -> list[tuple[str, pd.DataFrame, str]]:
    """Collect report tables separately from their Markdown rendering."""
    csv_dir = evaluation_dir / "csvs"
    diagnostics = _read_csv(csv_dir / "prediction_diagnostics_by_stratum.csv")
    if diagnostics.empty:
        diagnostics = _read_csv(
            csv_dir / "tossup_prediction_diagnostics_by_stratum.csv"
        )
    if diagnostics.empty:
        diagnostics = _read_csv(csv_dir / "bonus_prediction_diagnostics_by_stratum.csv")
    sections = [
        (
            "Run Variables And Stage Scalars",
            _stage_summary_rows(evaluation_dir),
            "No stage summary JSON files were found for this evaluation folder.",
        ),
        (
            "Bonus Stage Scalars",
            _bonus_scalar_rows(evaluation_dir),
            "No bonus-stage scalar summary values were found.",
        ),
        (
            "Stage 2 Bonus Metrics",
            _metric_frame(
                load_metrics_row(evaluation_dir, "bonus_metrics.csv"), BONUS_METRICS
            ),
            "No bonus metrics CSV was found.",
        ),
        (
            "Bonus-Only PPG by Tournament",
            _read_csv(csv_dir / "bonus_team_ranking_metrics.csv"),
            "No tournament bonus PPG metrics CSV was found.",
        ),
        (
            "Stage 1 Tossup Metrics",
            _metric_frame(
                load_metrics_row(evaluation_dir, "tossup_metrics.csv"),
                TOSSUP_METRICS,
            ),
            "No tossup metrics CSV was found.",
        ),
        (
            "Tossup Game Replay",
            _metric_frame(
                load_metrics_row(evaluation_dir, "game_metrics.csv"), GAME_METRICS
            ),
            "No tossup game replay metrics CSV was found.",
        ),
        (
            "Calibration And Sharpness By Stratum",
            diagnostics,
            "No stratified prediction diagnostics CSV was found.",
        ),
        (
            "No-Synergy Versus Synergy Deltas",
            _comparison_frame(comparison_csv),
            "No bonus model comparison CSV was found.",
        ),
        (
            "Pyramidal Player And Tossup Parameters",
            _parameter_summary(
                csv_dir / "pyramidal_parameter_distribution_summary.csv"
            ),
            "No pyramidal parameter distribution summary CSV was found.",
        ),
        (
            "Bonus And Synergy Parameters",
            _parameter_summary(csv_dir / "bonus_parameter_distribution_summary.csv"),
            "No bonus parameter distribution summary CSV was found.",
        ),
    ]
    if include_bonus:
        return sections
    bonus_titles = {
        "Bonus-Only PPG by Tournament",
        "Bonus Stage Scalars",
        "Stage 2 Bonus Metrics",
        "No-Synergy Versus Synergy Deltas",
        "Bonus And Synergy Parameters",
    }
    return [section for section in sections if section[0] not in bonus_titles]


def write_eval_docs_summary(
    evaluation_dir: Path,
    comparison_csv: Path | None = None,
    include_bonus: bool = True,
) -> Path:
    """Create 'docs/summary.md' for one evaluation or synergy-evaluation folder."""
    evaluation_dir = Path(evaluation_dir)
    if comparison_csv is None:
        candidate = comparison_path_for_evaluation(evaluation_dir)
        comparison_csv = candidate if candidate.exists() else None

    docs_dir = evaluation_dir / "docs"
    docs_dir.mkdir(parents=True, exist_ok=True)
    output_path = docs_dir / "summary.md"

    lines = [
        "# CompIRT Evaluation Summary",
        "",
        f"Evaluation folder: `{evaluation_dir}`",
        f"Result root: `{result_root_for_evaluation(evaluation_dir)}`",
        "",
        (
            "This file consolidates the metric CSVs and fitted-parameter "
            "distribution summaries for quick review."
            if not include_bonus
            else
            "This file consolidates the metric CSVs, bonus-model comparison "
            "deltas, and fitted-parameter distribution summaries for quick review."
        ),
        "",
    ]
    for note in evaluation_regime_notes(evaluation_dir):
        lines.extend([note, ""])
    for title, frame, empty_text in _summary_sections(
        evaluation_dir, comparison_csv, include_bonus
    ):
        _append_table(lines, title, frame, empty_text)

    output_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return output_path
