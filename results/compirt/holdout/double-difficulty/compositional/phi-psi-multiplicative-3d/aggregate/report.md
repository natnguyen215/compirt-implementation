# Compositional bonuses from frozen Stage-1 folds

[Configuration](../configuration.json) · [Pooled metrics](pooled.csv) · [Per-fold metrics](per_fold.csv) · [Fold mean and standard deviation](fold_mean_std.csv)

Source: [saved Stage-1 folds](../../../likelihood-refits/dd-bernstein-332-simplex-locations-terminal-normalized-first-buzz-3000steps).

3000 SVI steps, learning rate 0.01, seed 42; bonus discrimination prior `gamma`. Skills are fixed at the saved Stage-1 medians. All bonus parameters are fit on training games and frozen for held-out replay.

## Bonus model

The base logit is `eta = A_b(R) - beta_b`, using roster-size-unnormalized log-sum-exp aggregation. The compositional arm has no synergy.

Phi-psi synergy learns two 3-dimensional vectors per player: `s(R) = sum_d sum_{i<j} phi_id * phi_jd * (psi_id + psi_jd)`.

The multiplicative link uses `eta * (1 + s(R))`. The multiplier is unconstrained; values below zero reverse the base logit's sign.

The source Stage-1 fits are reused without refitting. Coverage requires familiar players and parts; lineups are inferred from observed game buzzes. These reused development folds measure frozen matrix infill. They do not establish transfer to new players or a teamwork interpretation of synergy.

## Pooled held-out metrics

Pool predictions across folds before calculating metrics. These values are not averages of fold scores. PPB MAE first averages observed and predicted bonus points within each team, then averages absolute errors across teams. Exact accuracy requires all three part labels to match.

| Model | AUC ↑ | Log loss ↓ | Part accuracy ↑ | Brier ↓ | ECE ↓ | Exact accuracy ↑ | PPB MAE ↓ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| phi-psi, multiplicative, 3D | 0.89034 | 0.417787 | 0.809149 | 0.133556 | 0.0151117 | 0.513138 | 1.9578 |

## Difficulty, bonus-only team PPG and game margins

Difficulty uses declared easy/medium/hard labels. Bonus-only PPG uses expected points on recorded bonus opportunities, divided by games played. Zero-bonus games count; incomplete prediction games are excluded. Pool folds before calculating team PPG, average team absolute errors within each tournament, then macro-average tournament MAE and defined Spearman correlations. Margin MAE averages absolute errors in signed team bonus-score differences across games.

| Model | Easy accuracy ↑ | Medium accuracy ↑ | Hard accuracy ↑ | PPG MAE ↓ | PPG Spearman ↑ | Margin MAE ↓ |
| --- | --- | --- | --- | --- | --- | --- |
| phi-psi, multiplicative, 3D | 0.906628 | 0.681897 | 0.838923 | 18.0476 | 0.883945 | 33.3571 |

phi-psi, multiplicative, 3D: [team PPG](synergy/bonus_team_ppg_leaderboard.csv) · [tournament metrics](synergy/bonus_team_ranking_metrics.csv) · [game margins](synergy/bonus_game_margin_predictions.csv)

## Scoring population and checks

| Model | Folds | Parts | Bonuses | Games with bonuses | Teams with bonuses |
| --- | --- | --- | --- | --- | --- |
| phi-psi, multiplicative, 3D | 5 | 128100 | 42700 | 2332 | 450 |

PPG and margin populations also include zero-bonus games and teams; their counts are recorded separately in `pooled.csv`. Per-fold separation checks, dropped-row counts, finite-loss checks, and loss slopes are in `per_fold.csv`. Fold variation is descriptive, not an uncertainty interval. One optimization seed was used; the fixed fitting budget does not establish convergence.

## Fold artifacts

| Fold | Model | Training | Held-out predictions | Evaluation | Checks |
| --- | --- | --- | --- | --- | --- |
| 0 | phi-psi, multiplicative, 3D | [fit](../fold_0/train/synergy/summary.json) | [predictions](../fold_0/holdout/synergy/bonus_part_predictions.csv) | [report](../fold_0/synergy-evaluation/experiment_report.md) | [audit](../fold_0/synergy_checks.json) |
| 1 | phi-psi, multiplicative, 3D | [fit](../fold_1/train/synergy/summary.json) | [predictions](../fold_1/holdout/synergy/bonus_part_predictions.csv) | [report](../fold_1/synergy-evaluation/experiment_report.md) | [audit](../fold_1/synergy_checks.json) |
| 2 | phi-psi, multiplicative, 3D | [fit](../fold_2/train/synergy/summary.json) | [predictions](../fold_2/holdout/synergy/bonus_part_predictions.csv) | [report](../fold_2/synergy-evaluation/experiment_report.md) | [audit](../fold_2/synergy_checks.json) |
| 3 | phi-psi, multiplicative, 3D | [fit](../fold_3/train/synergy/summary.json) | [predictions](../fold_3/holdout/synergy/bonus_part_predictions.csv) | [report](../fold_3/synergy-evaluation/experiment_report.md) | [audit](../fold_3/synergy_checks.json) |
| 4 | phi-psi, multiplicative, 3D | [fit](../fold_4/train/synergy/summary.json) | [predictions](../fold_4/holdout/synergy/bonus_part_predictions.csv) | [report](../fold_4/synergy-evaluation/experiment_report.md) | [audit](../fold_4/synergy_checks.json) |
