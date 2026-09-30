# Compositional bonuses from frozen Stage-1 folds

[Configuration](../configuration.json) · [Pooled metrics](pooled.csv) · [Per-fold metrics](per_fold.csv) · [Fold mean and standard deviation](fold_mean_std.csv)

Source: [saved Stage-1 folds](../../../likelihood-refits/dd-bernstein-332-simplex-locations-terminal-normalized-first-buzz-3000steps).

3000 SVI steps, learning rate 0.01, seed 42; bonus discrimination prior `gamma`. Skills are fixed at the saved Stage-1 medians. All bonus parameters are fit on training games and frozen for held-out replay.

## Bonus model

The base logit is `eta = A_b(R) - beta_b`, using roster-size-unnormalized log-sum-exp aggregation. The compositional arm has no synergy.

Dot-product synergy learns one 1-dimensional vector per player: `s(R) = sum_{i<j} psi_i dot psi_j`.

The additive link uses `eta + s(R)`.

The source Stage-1 fits are reused without refitting. Coverage requires familiar players and parts; lineups are inferred from observed game buzzes. These reused development folds measure frozen matrix infill. They do not establish transfer to new players or a teamwork interpretation of synergy.

## Pooled held-out metrics

Pool predictions across folds before calculating metrics. These values are not averages of fold scores. PPB MAE first averages observed and predicted bonus points within each team, then averages absolute errors across teams. Exact accuracy requires all three part labels to match.

| Model | AUC ↑ | Log loss ↓ | Part accuracy ↑ | Brier ↓ | ECE ↓ | Exact accuracy ↑ | PPB MAE ↓ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| No synergy | 0.890432 | 0.418315 | 0.808345 | 0.133691 | 0.0202508 | 0.511663 | 1.97781 |
| dot, additive, 1D | 0.898148 | 0.404871 | 0.816651 | 0.128568 | 0.0204397 | 0.529508 | 0.943033 |

## Difficulty, bonus-only team PPG and game margins

Difficulty uses declared easy/medium/hard labels. Bonus-only PPG uses expected points on recorded bonus opportunities, divided by games played. Zero-bonus games count; incomplete prediction games are excluded. Pool folds before calculating team PPG, average team absolute errors within each tournament, then macro-average tournament MAE and defined Spearman correlations. Margin MAE averages absolute errors in signed team bonus-score differences across games.

| Model | Easy accuracy ↑ | Medium accuracy ↑ | Hard accuracy ↑ | PPG MAE ↓ | PPG Spearman ↑ | Margin MAE ↓ |
| --- | --- | --- | --- | --- | --- | --- |
| No synergy | 0.906136 | 0.680328 | 0.838571 | 18.0353 | 0.887232 | 33.2264 |
| dot, additive, 1D | 0.907518 | 0.700117 | 0.842319 | 8.2974 | 0.93717 | 26.5344 |

No synergy: [team PPG](compositional/bonus_team_ppg_leaderboard.csv) · [tournament metrics](compositional/bonus_team_ranking_metrics.csv) · [game margins](compositional/bonus_game_margin_predictions.csv)

dot, additive, 1D: [team PPG](synergy/bonus_team_ppg_leaderboard.csv) · [tournament metrics](synergy/bonus_team_ranking_metrics.csv) · [game margins](synergy/bonus_game_margin_predictions.csv)

## Scoring population and checks

| Model | Folds | Parts | Bonuses | Games with bonuses | Teams with bonuses |
| --- | --- | --- | --- | --- | --- |
| No synergy | 5 | 128100 | 42700 | 2332 | 450 |
| dot, additive, 1D | 5 | 128100 | 42700 | 2332 | 450 |

PPG and margin populations also include zero-bonus games and teams; their counts are recorded separately in `pooled.csv`. Per-fold separation checks, dropped-row counts, finite-loss checks, and loss slopes are in `per_fold.csv`. Fold variation is descriptive, not an uncertainty interval. One optimization seed was used; the fixed fitting budget does not establish convergence.

## Fold artifacts

| Fold | Model | Training | Held-out predictions | Evaluation | Checks |
| --- | --- | --- | --- | --- | --- |
| 0 | No synergy | [fit](../fold_0/train/compositional/summary.json) | [predictions](../fold_0/holdout/compositional/bonus_part_predictions.csv) | [report](../fold_0/evaluation/experiment_report.md) | [audit](../fold_0/compositional_checks.json) |
| 0 | dot, additive, 1D | [fit](../fold_0/train/synergy/summary.json) | [predictions](../fold_0/holdout/synergy/bonus_part_predictions.csv) | [report](../fold_0/synergy-evaluation/experiment_report.md) | [audit](../fold_0/synergy_checks.json) |
| 1 | No synergy | [fit](../fold_1/train/compositional/summary.json) | [predictions](../fold_1/holdout/compositional/bonus_part_predictions.csv) | [report](../fold_1/evaluation/experiment_report.md) | [audit](../fold_1/compositional_checks.json) |
| 1 | dot, additive, 1D | [fit](../fold_1/train/synergy/summary.json) | [predictions](../fold_1/holdout/synergy/bonus_part_predictions.csv) | [report](../fold_1/synergy-evaluation/experiment_report.md) | [audit](../fold_1/synergy_checks.json) |
| 2 | No synergy | [fit](../fold_2/train/compositional/summary.json) | [predictions](../fold_2/holdout/compositional/bonus_part_predictions.csv) | [report](../fold_2/evaluation/experiment_report.md) | [audit](../fold_2/compositional_checks.json) |
| 2 | dot, additive, 1D | [fit](../fold_2/train/synergy/summary.json) | [predictions](../fold_2/holdout/synergy/bonus_part_predictions.csv) | [report](../fold_2/synergy-evaluation/experiment_report.md) | [audit](../fold_2/synergy_checks.json) |
| 3 | No synergy | [fit](../fold_3/train/compositional/summary.json) | [predictions](../fold_3/holdout/compositional/bonus_part_predictions.csv) | [report](../fold_3/evaluation/experiment_report.md) | [audit](../fold_3/compositional_checks.json) |
| 3 | dot, additive, 1D | [fit](../fold_3/train/synergy/summary.json) | [predictions](../fold_3/holdout/synergy/bonus_part_predictions.csv) | [report](../fold_3/synergy-evaluation/experiment_report.md) | [audit](../fold_3/synergy_checks.json) |
| 4 | No synergy | [fit](../fold_4/train/compositional/summary.json) | [predictions](../fold_4/holdout/compositional/bonus_part_predictions.csv) | [report](../fold_4/evaluation/experiment_report.md) | [audit](../fold_4/compositional_checks.json) |
| 4 | dot, additive, 1D | [fit](../fold_4/train/synergy/summary.json) | [predictions](../fold_4/holdout/synergy/bonus_part_predictions.csv) | [report](../fold_4/synergy-evaluation/experiment_report.md) | [audit](../fold_4/synergy_checks.json) |
