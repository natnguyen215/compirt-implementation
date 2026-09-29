# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 16.1989 |
| tournament_team_bonus_ppg_spearman | 0.924327 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 469 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 26.8784 |
| bonus_game_margin_mae_games | 469 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.898717 |
| log_loss | 0.403453 |
| ece | 0.0163983 |
| brier | 0.128011 |
| part_accuracy | 0.816941 |
| part_accuracy_easy | 0.914985 |
| part_accuracy_medium | 0.691835 |
| part_accuracy_hard | 0.844004 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.525555 |
| accuracy_lift_over_all_correct | 0.291386 |
| part_accuracy_macro_team | 0.821856 |
| part_accuracy_macro_bonus | 0.814579 |
| part_count_easy | 8622 |
| part_count_medium | 8622 |
| part_count_hard | 8622 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.349535 |
| probability_p10 | 0.0539231 |
| probability_p50 | 0.539647 |
| probability_p90 | 0.964559 |
| mean_predictive_variance | 0.1271 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.529344 |
| ranked_probability_score | 0.112895 |
| bonus_total_score_log_loss | 0.999101 |
| ppb_mae | 1.73239 |
| ranked_probability_score_responses | 8622 |
| bonus_total_score_log_loss_responses | 8622 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 9 | 8 | 17.0506 | 0.966667 | 24.8968 |
| 2024-acf-fall-at-cornell | 15 | 17 | 14.0712 | 0.938338 | 23.017 |
| 2024-acf-fall-at-georgia | 24 | 26 | 11.3031 | 0.97715 | 25.7198 |
| 2024-acf-fall-at-illinois | 18 | 22 | 17.3648 | 0.985524 | 32.3302 |
| 2024-acf-fall-at-north-carolina | 18 | 22 | 18.7478 | 0.924141 | 28.4213 |
| 2024-acf-fall-at-ohio-state | 17 | 18 | 12.4944 | 0.971117 | 28.0799 |
| 2024-acf-fall-at-rutgers | 17 | 19 | 18.8811 | 0.938651 | 34.2229 |
| 2024-acf-fall-at-washington | 14 | 13 | 16.3739 | 0.943895 | 31.9176 |
| 2024-acf-nationals | 47 | 81 | 9.66177 | 0.947945 | 20.955 |
| 2024-acf-regionals-berkeley | 5 | 6 | 11.4322 | 1 | 40.5896 |
| 2024-acf-regionals-cornell | 6 | 6 | 20.2233 | 0.828571 | 35.7662 |
| 2024-acf-regionals-imperial | 15 | 18 | 16.1302 | 0.949062 | 21.2095 |
| 2024-acf-regionals-jmu | 20 | 25 | 12.9171 | 0.937547 | 19.4175 |
| 2024-acf-regionals-minnesota | 4 | 4 | 14.2599 | 0.8 | 15.4524 |
| 2024-acf-regionals-mit | 2 | 1 | 15.0667 | 1 | 30.1334 |
| 2024-acf-regionals-nebraska | 9 | 14 | 16.5501 | 0.816667 | 40.429 |
| 2024-acf-regionals-ohio-state | 7 | 6 | 16.6366 | 0.892857 | 33.3479 |
| 2024-acf-regionals-rutgers | 11 | 11 | 13.1759 | 0.963636 | 30.6579 |
| 2024-acf-regionals-vanderbilt | 10 | 10 | 15.8468 | 0.859772 | 15.3132 |
| 2024-acf-winter-at-brandeis | 19 | 18 | 16.5074 | 0.970601 | 24.438 |
| 2024-acf-winter-at-central-florida | 10 | 10 | 8.27278 | 0.984807 | 14.8558 |
| 2024-acf-winter-at-clemson | 18 | 17 | 12.5405 | 0.980372 | 22.2354 |
| 2024-acf-winter-at-lehigh | 12 | 13 | 15.4178 | 0.942208 | 27.6675 |
| 2024-acf-winter-at-northwestern | 20 | 20 | 12.4634 | 0.979684 | 24.9849 |
| 2024-acf-winter-at-ohio-state | 18 | 15 | 23.4297 | 0.924032 | 32.9448 |
| 2024-acf-winter-at-online | 14 | 19 | 16.4206 | 0.927315 | 25.2655 |
| 2024-acf-winter-at-oxford | 18 | 19 | 15.6848 | 0.85493 | 36.7781 |
| 2024-acf-winter-at-ubc | 6 | 6 | 22.8487 | 0.6 | 41.3923 |
| 2024-acf-winter-at-uc-berkeley | 4 | 5 | 37.9937 | 1 | 64.2731 |

[Team PPG and absolute errors](csvs/bonus_team_ppg_leaderboard.csv); [game bonus margins](csvs/bonus_game_margin_predictions.csv).

### Bonus Distributions

Aggregate ability is part-weighted; synergy is response-weighted. Parameter plots describe fitted training parameters across entities, not posterior uncertainty intervals.

[Evaluated probabilities, aggregate ability, and synergy contributions](graphs/bonus/bonus_prediction_distributions.png).

[Fitted bonus parameters](graphs/parameters/bonus_part_parameter_distributions.png).

[Fitted synergy parameters](graphs/parameters/synergy_parameter_distributions.png).

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in the diagnostic CSVs under `csvs/`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part_correctness | aggregate | all | 25866 | 0.0163983 | 0.128011 | 0.898717 | 0.403453 |
| bonus_part_correctness | tier | fall | 8259 | 0.0226863 | 0.128421 | 0.895915 | 0.400666 |
| bonus_part_correctness | tier | nationals | 4167 | 0.0245092 | 0.128371 | 0.894696 | 0.408028 |
| bonus_part_correctness | tier | regionals | 5457 | 0.017396 | 0.128803 | 0.896616 | 0.407328 |
| bonus_part_correctness | tier | winter | 7983 | 0.0233635 | 0.126857 | 0.900345 | 0.401298 |
| bonus_part_correctness | category | Current Events | 258 | 0.0489904 | 0.142911 | 0.883188 | 0.441624 |
| bonus_part_correctness | category | Fine Arts | 3000 | 0.0293127 | 0.131792 | 0.893719 | 0.412762 |
| bonus_part_correctness | category | Geography | 450 | 0.0416939 | 0.126914 | 0.898794 | 0.400813 |
| bonus_part_correctness | category | History | 4116 | 0.0254846 | 0.1247 | 0.903483 | 0.391743 |
| bonus_part_correctness | category | Literature | 4092 | 0.0209148 | 0.125413 | 0.901756 | 0.396019 |
| bonus_part_correctness | category | Mythology | 951 | 0.050486 | 0.127082 | 0.894466 | 0.40128 |
| bonus_part_correctness | category | Other Academic | 276 | 0.0311414 | 0.116677 | 0.911565 | 0.377255 |
| bonus_part_correctness | category | Philosophy | 957 | 0.0331416 | 0.134065 | 0.889264 | 0.428984 |
| bonus_part_correctness | category | Popular Culture | 300 | 0.0510146 | 0.142044 | 0.877227 | 0.422585 |
| bonus_part_correctness | category | Religion | 1029 | 0.0263417 | 0.125858 | 0.902984 | 0.397157 |
| bonus_part_correctness | category | Science | 4089 | 0.0231616 | 0.130574 | 0.894175 | 0.412592 |
| bonus_part_correctness | category | Social Science | 891 | 0.0306901 | 0.117895 | 0.91338 | 0.368775 |
| bonus_part_correctness | category | Unknown | 5457 | 0.017396 | 0.128803 | 0.896616 | 0.407328 |
| bonus_part_correctness | difficulty | easy | 8622 | 0.0310209 | 0.0682225 | 0.819795 | 0.24029 |
| bonus_part_correctness | difficulty | hard | 8622 | 0.0371347 | 0.116328 | 0.766584 | 0.382774 |
| bonus_part_correctness | difficulty | medium | 8622 | 0.0399641 | 0.199483 | 0.763306 | 0.587293 |
