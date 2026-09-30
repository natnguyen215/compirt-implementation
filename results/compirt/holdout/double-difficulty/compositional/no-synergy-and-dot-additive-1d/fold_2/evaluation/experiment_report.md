# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 21.8599 |
| tournament_team_bonus_ppg_spearman | 0.850797 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 469 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 33.904 |
| bonus_game_margin_mae_games | 469 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.889151 |
| log_loss | 0.420893 |
| ece | 0.0205405 |
| brier | 0.134338 |
| part_accuracy | 0.808732 |
| part_accuracy_easy | 0.899267 |
| part_accuracy_medium | 0.685355 |
| part_accuracy_hard | 0.841573 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.519367 |
| accuracy_lift_over_all_correct | 0.289365 |
| part_accuracy_macro_team | 0.811999 |
| part_accuracy_macro_bonus | 0.806917 |
| part_count_easy | 8597 |
| part_count_medium | 8597 |
| part_count_hard | 8597 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.344958 |
| probability_p10 | 0.0520811 |
| probability_p50 | 0.525891 |
| probability_p90 | 0.956401 |
| mean_predictive_variance | 0.130662 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.512621 |
| ranked_probability_score | 0.116833 |
| bonus_total_score_log_loss | 1.02594 |
| ppb_mae | 2.288 |
| ranked_probability_score_responses | 8597 |
| bonus_total_score_log_loss_responses | 8597 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 8 | 9 | 12.7909 | 0.97619 | 26.0343 |
| 2024-acf-fall-at-cornell | 17 | 18 | 22.9395 | 0.862577 | 33.4751 |
| 2024-acf-fall-at-georgia | 22 | 24 | 20.2495 | 0.91516 | 33.7478 |
| 2024-acf-fall-at-illinois | 19 | 21 | 17.1462 | 0.978947 | 29.7823 |
| 2024-acf-fall-at-north-carolina | 18 | 22 | 13.9427 | 0.960784 | 18.8968 |
| 2024-acf-fall-at-ohio-state | 18 | 19 | 24.2682 | 0.9365 | 30.4033 |
| 2024-acf-fall-at-rutgers | 16 | 16 | 12.7068 | 0.954346 | 18.2272 |
| 2024-acf-fall-at-washington | 13 | 12 | 31.4318 | 0.846154 | 37.8994 |
| 2024-acf-nationals | 47 | 79 | 18.8056 | 0.876815 | 35.6577 |
| 2024-acf-regionals-berkeley | 5 | 6 | 33.721 | 0.974679 | 47.7076 |
| 2024-acf-regionals-cornell | 4 | 7 | 25.1709 | 0.4 | 35.801 |
| 2024-acf-regionals-imperial | 15 | 18 | 18.3595 | 0.927614 | 34.2019 |
| 2024-acf-regionals-jmu | 18 | 24 | 19.3366 | 0.879133 | 31.1884 |
| 2024-acf-regionals-minnesota | 4 | 4 | 27.6099 | 0.8 | 71.1023 |
| 2024-acf-regionals-mit | 6 | 4 | 23.4549 | 0.942857 | 38.6678 |
| 2024-acf-regionals-nebraska | 12 | 13 | 10.6125 | 0.963224 | 20.1933 |
| 2024-acf-regionals-ohio-state | 6 | 6 | 14.3982 | 0.542857 | 20.4802 |
| 2024-acf-regionals-rutgers | 11 | 11 | 29.0137 | 0.963636 | 42.0991 |
| 2024-acf-regionals-vanderbilt | 10 | 11 | 24.3024 | 0.90303 | 50.7329 |
| 2024-acf-winter-at-brandeis | 20 | 18 | 24.8585 | 0.926664 | 39.1491 |
| 2024-acf-winter-at-central-florida | 9 | 10 | 18.9126 | 0.983333 | 27.7547 |
| 2024-acf-winter-at-clemson | 18 | 17 | 20.8724 | 0.879133 | 38.2521 |
| 2024-acf-winter-at-lehigh | 14 | 14 | 21.6442 | 0.973571 | 36.7665 |
| 2024-acf-winter-at-northwestern | 20 | 21 | 13.2629 | 0.962768 | 24.36 |
| 2024-acf-winter-at-ohio-state | 16 | 16 | 26.6933 | 0.893963 | 31.3276 |
| 2024-acf-winter-at-online | 18 | 19 | 25.2662 | 0.907121 | 43.7135 |
| 2024-acf-winter-at-oxford | 17 | 18 | 20.3652 | 0.842045 | 42.0743 |
| 2024-acf-winter-at-ubc | 5 | 6 | 18.3102 | 0.1 | 28.7572 |
| 2024-acf-winter-at-uc-berkeley | 6 | 6 | 43.49 | 0.6 | 67.477 |

[Team PPG and absolute errors](csvs/bonus_team_ppg_leaderboard.csv); [game bonus margins](csvs/bonus_game_margin_predictions.csv).

### Bonus Distributions

Aggregate ability is part-weighted; synergy is response-weighted. Parameter plots describe fitted training parameters across entities, not posterior uncertainty intervals.

[Evaluated probabilities, aggregate ability, and synergy contributions](graphs/bonus/bonus_prediction_distributions.png).

[Fitted bonus parameters](graphs/parameters/bonus_part_parameter_distributions.png).

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in the diagnostic CSVs under `csvs/`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part_correctness | aggregate | all | 25791 | 0.0205405 | 0.134338 | 0.889151 | 0.420893 |
| bonus_part_correctness | tier | fall | 7995 | 0.0218926 | 0.128116 | 0.896893 | 0.39937 |
| bonus_part_correctness | tier | nationals | 4095 | 0.0265694 | 0.13598 | 0.882254 | 0.428058 |
| bonus_part_correctness | tier | regionals | 5580 | 0.0220422 | 0.136274 | 0.88576 | 0.425574 |
| bonus_part_correctness | tier | winter | 8121 | 0.0232596 | 0.138306 | 0.882588 | 0.435253 |
| bonus_part_correctness | category | Current Events | 216 | 0.0616672 | 0.118614 | 0.908394 | 0.380026 |
| bonus_part_correctness | category | Fine Arts | 2970 | 0.0257776 | 0.143962 | 0.875242 | 0.446317 |
| bonus_part_correctness | category | Geography | 501 | 0.0641793 | 0.134638 | 0.890993 | 0.426669 |
| bonus_part_correctness | category | History | 4068 | 0.0191955 | 0.129518 | 0.895994 | 0.408872 |
| bonus_part_correctness | category | Literature | 4065 | 0.0278412 | 0.130318 | 0.89415 | 0.409765 |
| bonus_part_correctness | category | Mythology | 945 | 0.0354755 | 0.149065 | 0.859873 | 0.456694 |
| bonus_part_correctness | category | Other Academic | 219 | 0.0439056 | 0.145303 | 0.875626 | 0.452336 |
| bonus_part_correctness | category | Philosophy | 963 | 0.038929 | 0.139223 | 0.879271 | 0.43745 |
| bonus_part_correctness | category | Popular Culture | 288 | 0.063884 | 0.141348 | 0.876492 | 0.42808 |
| bonus_part_correctness | category | Religion | 1008 | 0.0384888 | 0.13506 | 0.889925 | 0.41872 |
| bonus_part_correctness | category | Science | 4059 | 0.0283523 | 0.132229 | 0.891153 | 0.418536 |
| bonus_part_correctness | category | Social Science | 909 | 0.042404 | 0.117394 | 0.914244 | 0.367497 |
| bonus_part_correctness | category | Unknown | 5580 | 0.0220422 | 0.136274 | 0.88576 | 0.425574 |
| bonus_part_correctness | difficulty | easy | 8597 | 0.0261443 | 0.0774739 | 0.797144 | 0.268607 |
| bonus_part_correctness | difficulty | hard | 8597 | 0.0397323 | 0.120913 | 0.744929 | 0.396492 |
| bonus_part_correctness | difficulty | medium | 8597 | 0.0418666 | 0.204627 | 0.749779 | 0.59758 |
