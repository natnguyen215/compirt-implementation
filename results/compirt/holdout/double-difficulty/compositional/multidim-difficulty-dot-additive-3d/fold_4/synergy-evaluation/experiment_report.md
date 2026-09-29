# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 15.2865 |
| tournament_team_bonus_ppg_spearman | 0.929041 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 469 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 25.5368 |
| bonus_game_margin_mae_games | 469 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.899925 |
| log_loss | 0.400566 |
| ece | 0.00982557 |
| brier | 0.127176 |
| part_accuracy | 0.819068 |
| part_accuracy_easy | 0.909418 |
| part_accuracy_medium | 0.699606 |
| part_accuracy_hard | 0.848179 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.525555 |
| accuracy_lift_over_all_correct | 0.293513 |
| part_accuracy_macro_team | 0.823131 |
| part_accuracy_macro_bonus | 0.815641 |
| part_count_easy | 8622 |
| part_count_medium | 8622 |
| part_count_hard | 8622 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.353565 |
| probability_p10 | 0.0455769 |
| probability_p50 | 0.504734 |
| probability_p90 | 0.986151 |
| mean_predictive_variance | 0.124684 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.535375 |
| ranked_probability_score | 0.111908 |
| bonus_total_score_log_loss | 0.993092 |
| ppb_mae | 1.63474 |
| ranked_probability_score_responses | 8622 |
| bonus_total_score_log_loss_responses | 8622 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 9 | 8 | 14.2078 | 0.966667 | 33.2045 |
| 2024-acf-fall-at-cornell | 15 | 17 | 10.9767 | 0.954424 | 21.2311 |
| 2024-acf-fall-at-georgia | 24 | 26 | 11.8513 | 0.974538 | 27.1534 |
| 2024-acf-fall-at-illinois | 18 | 22 | 19.0158 | 0.968978 | 29.6971 |
| 2024-acf-fall-at-north-carolina | 18 | 22 | 14.1461 | 0.947011 | 19.6793 |
| 2024-acf-fall-at-ohio-state | 17 | 18 | 11.0502 | 0.9662 | 24.0244 |
| 2024-acf-fall-at-rutgers | 17 | 19 | 17.6204 | 0.933743 | 37.4134 |
| 2024-acf-fall-at-washington | 14 | 13 | 13.5685 | 0.959297 | 28.9876 |
| 2024-acf-nationals | 47 | 81 | 8.66498 | 0.960387 | 19.6001 |
| 2024-acf-regionals-berkeley | 5 | 6 | 14.7651 | 1 | 43.4579 |
| 2024-acf-regionals-cornell | 6 | 6 | 18.8241 | 0.828571 | 38.4581 |
| 2024-acf-regionals-imperial | 15 | 18 | 14.4804 | 0.945487 | 21.1604 |
| 2024-acf-regionals-jmu | 20 | 25 | 12.1246 | 0.946577 | 17.235 |
| 2024-acf-regionals-minnesota | 4 | 4 | 12.1258 | 0.8 | 16.9646 |
| 2024-acf-regionals-mit | 2 | 1 | 13.1924 | 1 | 26.3847 |
| 2024-acf-regionals-nebraska | 9 | 14 | 15.8351 | 0.883333 | 39.2193 |
| 2024-acf-regionals-ohio-state | 7 | 6 | 17.0502 | 0.892857 | 30.041 |
| 2024-acf-regionals-rutgers | 11 | 11 | 15.0254 | 0.963636 | 27.8377 |
| 2024-acf-regionals-vanderbilt | 10 | 10 | 12.9924 | 0.859772 | 16.3924 |
| 2024-acf-winter-at-brandeis | 19 | 18 | 16.1304 | 0.974989 | 23.9922 |
| 2024-acf-winter-at-central-florida | 10 | 10 | 6.1897 | 0.996965 | 13.4511 |
| 2024-acf-winter-at-clemson | 18 | 17 | 12.8655 | 0.980372 | 21.2648 |
| 2024-acf-winter-at-lehigh | 12 | 13 | 18.487 | 0.938705 | 29.5636 |
| 2024-acf-winter-at-northwestern | 20 | 20 | 11.771 | 0.970655 | 24.6338 |
| 2024-acf-winter-at-ohio-state | 18 | 15 | 18.063 | 0.944704 | 23.5169 |
| 2024-acf-winter-at-online | 14 | 19 | 17.8667 | 0.927315 | 23.4599 |
| 2024-acf-winter-at-oxford | 18 | 19 | 16.411 | 0.856995 | 36.9314 |
| 2024-acf-winter-at-ubc | 6 | 6 | 24.9956 | 0.6 | 41.3542 |
| 2024-acf-winter-at-uc-berkeley | 4 | 5 | 33.0104 | 1 | 60.0097 |

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
| bonus_part_correctness | aggregate | all | 25866 | 0.00982557 | 0.127176 | 0.899925 | 0.400566 |
| bonus_part_correctness | tier | fall | 8259 | 0.010622 | 0.127328 | 0.896854 | 0.397985 |
| bonus_part_correctness | tier | nationals | 4167 | 0.0172987 | 0.128706 | 0.894082 | 0.41119 |
| bonus_part_correctness | tier | regionals | 5457 | 0.0178134 | 0.12743 | 0.899838 | 0.399019 |
| bonus_part_correctness | tier | winter | 7983 | 0.0135933 | 0.126048 | 0.901119 | 0.398749 |
| bonus_part_correctness | category | Current Events | 258 | 0.0590678 | 0.141609 | 0.878316 | 0.455158 |
| bonus_part_correctness | category | Fine Arts | 3000 | 0.0222417 | 0.130337 | 0.894954 | 0.409 |
| bonus_part_correctness | category | Geography | 450 | 0.0355771 | 0.124235 | 0.902367 | 0.391245 |
| bonus_part_correctness | category | History | 4116 | 0.013077 | 0.123787 | 0.904362 | 0.390705 |
| bonus_part_correctness | category | Literature | 4092 | 0.0194343 | 0.123593 | 0.90419 | 0.391839 |
| bonus_part_correctness | category | Mythology | 951 | 0.0445434 | 0.129484 | 0.891122 | 0.407415 |
| bonus_part_correctness | category | Other Academic | 276 | 0.0284479 | 0.116448 | 0.913621 | 0.367324 |
| bonus_part_correctness | category | Philosophy | 957 | 0.026623 | 0.131496 | 0.892662 | 0.421426 |
| bonus_part_correctness | category | Popular Culture | 300 | 0.043963 | 0.140601 | 0.876663 | 0.420908 |
| bonus_part_correctness | category | Religion | 1029 | 0.0165747 | 0.125946 | 0.901775 | 0.397252 |
| bonus_part_correctness | category | Science | 4089 | 0.0171597 | 0.131778 | 0.89281 | 0.41604 |
| bonus_part_correctness | category | Social Science | 891 | 0.0233698 | 0.116412 | 0.915131 | 0.362732 |
| bonus_part_correctness | category | Unknown | 5457 | 0.0178134 | 0.12743 | 0.899838 | 0.399019 |
| bonus_part_correctness | difficulty | easy | 8622 | 0.0340647 | 0.0701635 | 0.823021 | 0.242953 |
| bonus_part_correctness | difficulty | hard | 8622 | 0.0341054 | 0.114904 | 0.770532 | 0.379856 |
| bonus_part_correctness | difficulty | medium | 8622 | 0.0223507 | 0.196462 | 0.7684 | 0.57889 |
