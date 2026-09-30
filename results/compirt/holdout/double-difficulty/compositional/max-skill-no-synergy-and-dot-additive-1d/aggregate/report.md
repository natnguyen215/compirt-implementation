# Compositional bonuses from frozen Stage-1 folds

[Configuration](../configuration.json) · [Pooled metrics](pooled.csv) · [Per-fold metrics](per_fold.csv) · [Fold mean and standard deviation](fold_mean_std.csv)

Source: [saved Stage-1 folds](../../../likelihood-refits/dd-bernstein-332-simplex-locations-terminal-normalized-first-buzz-3000steps).

3000 SVI steps, learning rate 0.01, seed 42; bonus discrimination prior `gamma`. Skills are fixed at the saved Stage-1 medians. All bonus parameters are fit on training games and frozen for held-out replay.

## Bonus model

The base logit is `eta = sum_k alpha_bk * max_i theta_ik - beta_b`. The maximum selects an active teammate separately for each skill dimension, before applying part weights. There is no temperature parameter. The compositional arm has no synergy.

Dot-product synergy learns one 1-dimensional vector per player: `s(R) = sum_{i<j} psi_i dot psi_j`.

The additive link uses `eta + s(R)`.

The source Stage-1 fits are reused without refitting. Coverage requires familiar players and parts; lineups are inferred from observed game buzzes. These reused development folds measure frozen matrix infill. They do not establish transfer to new players or a teamwork interpretation of synergy.

## Pooled held-out metrics

Pool predictions across folds before calculating metrics. These values are not averages of fold scores. PPB MAE first averages observed and predicted bonus points within each team, then averages absolute errors across teams. Exact accuracy requires all three part labels to match.

| Model | AUC ↑ | Log loss ↓ | Part accuracy ↑ | Brier ↓ | ECE ↓ | Exact accuracy ↑ | PPB MAE ↓ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Per-dimension max; No synergy | 0.887376 | 0.423667 | 0.80758 | 0.135272 | 0.0128951 | 0.511054 | 1.96664 |
| Per-dimension max; dot, additive, 1D | 0.896203 | 0.408534 | 0.817853 | 0.129302 | 0.0168757 | 0.532763 | 0.792656 |

## Difficulty, bonus-only team PPG and game margins

Difficulty uses declared easy/medium/hard labels. Bonus-only PPG uses expected points on recorded bonus opportunities, divided by games played. Zero-bonus games count; incomplete prediction games are excluded. Pool folds before calculating team PPG, average team absolute errors within each tournament, then macro-average tournament MAE and defined Spearman correlations. Margin MAE averages absolute errors in signed team bonus-score differences across games.

| Model | Easy accuracy ↑ | Medium accuracy ↑ | Hard accuracy ↑ | PPG MAE ↓ | PPG Spearman ↑ | Margin MAE ↓ |
| --- | --- | --- | --- | --- | --- | --- |
| Per-dimension max; No synergy | 0.902623 | 0.682787 | 0.83733 | 18.5499 | 0.878594 | 35.8518 |
| Per-dimension max; dot, additive, 1D | 0.906745 | 0.7026 | 0.844215 | 7.38107 | 0.939223 | 26.5161 |

Per-dimension max; No synergy: [team PPG](compositional/bonus_team_ppg_leaderboard.csv) · [tournament metrics](compositional/bonus_team_ranking_metrics.csv) · [game margins](compositional/bonus_game_margin_predictions.csv)

Per-dimension max; dot, additive, 1D: [team PPG](synergy/bonus_team_ppg_leaderboard.csv) · [tournament metrics](synergy/bonus_team_ranking_metrics.csv) · [game margins](synergy/bonus_game_margin_predictions.csv)

## Scoring population and checks

| Model | Folds | Parts | Bonuses | Games with bonuses | Teams with bonuses |
| --- | --- | --- | --- | --- | --- |
| Per-dimension max; No synergy | 5 | 128100 | 42700 | 2332 | 450 |
| Per-dimension max; dot, additive, 1D | 5 | 128100 | 42700 | 2332 | 450 |

PPG and margin populations also include zero-bonus games and teams; their counts are recorded separately in `pooled.csv`. Per-fold separation checks, dropped-row counts, finite-loss checks, and loss slopes are in `per_fold.csv`. Fold variation is descriptive, not an uncertainty interval. One optimization seed was used; the fixed fitting budget does not establish convergence.

## Fold artifacts

| Fold | Model | Training | Held-out predictions | Evaluation | Checks |
| --- | --- | --- | --- | --- | --- |
| 0 | Per-dimension max; No synergy | [fit](../fold_0/train/compositional/summary.json) | [predictions](../fold_0/holdout/compositional/bonus_part_predictions.csv) | [report](../fold_0/evaluation/experiment_report.md) | [audit](../fold_0/compositional_checks.json) |
| 0 | Per-dimension max; dot, additive, 1D | [fit](../fold_0/train/synergy/summary.json) | [predictions](../fold_0/holdout/synergy/bonus_part_predictions.csv) | [report](../fold_0/synergy-evaluation/experiment_report.md) | [audit](../fold_0/synergy_checks.json) |
| 1 | Per-dimension max; No synergy | [fit](../fold_1/train/compositional/summary.json) | [predictions](../fold_1/holdout/compositional/bonus_part_predictions.csv) | [report](../fold_1/evaluation/experiment_report.md) | [audit](../fold_1/compositional_checks.json) |
| 1 | Per-dimension max; dot, additive, 1D | [fit](../fold_1/train/synergy/summary.json) | [predictions](../fold_1/holdout/synergy/bonus_part_predictions.csv) | [report](../fold_1/synergy-evaluation/experiment_report.md) | [audit](../fold_1/synergy_checks.json) |
| 2 | Per-dimension max; No synergy | [fit](../fold_2/train/compositional/summary.json) | [predictions](../fold_2/holdout/compositional/bonus_part_predictions.csv) | [report](../fold_2/evaluation/experiment_report.md) | [audit](../fold_2/compositional_checks.json) |
| 2 | Per-dimension max; dot, additive, 1D | [fit](../fold_2/train/synergy/summary.json) | [predictions](../fold_2/holdout/synergy/bonus_part_predictions.csv) | [report](../fold_2/synergy-evaluation/experiment_report.md) | [audit](../fold_2/synergy_checks.json) |
| 3 | Per-dimension max; No synergy | [fit](../fold_3/train/compositional/summary.json) | [predictions](../fold_3/holdout/compositional/bonus_part_predictions.csv) | [report](../fold_3/evaluation/experiment_report.md) | [audit](../fold_3/compositional_checks.json) |
| 3 | Per-dimension max; dot, additive, 1D | [fit](../fold_3/train/synergy/summary.json) | [predictions](../fold_3/holdout/synergy/bonus_part_predictions.csv) | [report](../fold_3/synergy-evaluation/experiment_report.md) | [audit](../fold_3/synergy_checks.json) |
| 4 | Per-dimension max; No synergy | [fit](../fold_4/train/compositional/summary.json) | [predictions](../fold_4/holdout/compositional/bonus_part_predictions.csv) | [report](../fold_4/evaluation/experiment_report.md) | [audit](../fold_4/compositional_checks.json) |
| 4 | Per-dimension max; dot, additive, 1D | [fit](../fold_4/train/synergy/summary.json) | [predictions](../fold_4/holdout/synergy/bonus_part_predictions.csv) | [report](../fold_4/synergy-evaluation/experiment_report.md) | [audit](../fold_4/synergy_checks.json) |
