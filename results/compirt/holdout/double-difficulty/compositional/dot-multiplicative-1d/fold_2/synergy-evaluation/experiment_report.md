# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 22.0524 |
| tournament_team_bonus_ppg_spearman | 0.845633 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 469 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 33.9532 |
| bonus_game_margin_mae_games | 469 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.888627 |
| log_loss | 0.421291 |
| ece | 0.0157009 |
| brier | 0.134603 |
| part_accuracy | 0.807762 |
| part_accuracy_easy | 0.900081 |
| part_accuracy_medium | 0.682913 |
| part_accuracy_hard | 0.840293 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.519367 |
| accuracy_lift_over_all_correct | 0.288395 |
| part_accuracy_macro_team | 0.810282 |
| part_accuracy_macro_bonus | 0.805155 |
| part_count_easy | 8597 |
| part_count_medium | 8597 |
| part_count_hard | 8597 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.346651 |
| probability_p10 | 0.0530688 |
| probability_p50 | 0.521892 |
| probability_p90 | 0.962658 |
| mean_predictive_variance | 0.129466 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.508782 |
| ranked_probability_score | 0.116927 |
| bonus_total_score_log_loss | 1.02693 |
| ppb_mae | 2.29758 |
| ranked_probability_score_responses | 8597 |
| bonus_total_score_log_loss_responses | 8597 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 8 | 9 | 13.2804 | 0.97619 | 26.1426 |
| 2024-acf-fall-at-cornell | 17 | 18 | 23.9831 | 0.852761 | 34.8628 |
| 2024-acf-fall-at-georgia | 22 | 24 | 20.599 | 0.91516 | 34.4384 |
| 2024-acf-fall-at-illinois | 19 | 21 | 17.9016 | 0.968421 | 29.8779 |
| 2024-acf-fall-at-north-carolina | 18 | 22 | 14.3525 | 0.954592 | 18.8872 |
| 2024-acf-fall-at-ohio-state | 18 | 19 | 24.6478 | 0.945793 | 30.6612 |
| 2024-acf-fall-at-rutgers | 16 | 16 | 14.2103 | 0.949927 | 21.1176 |
| 2024-acf-fall-at-washington | 13 | 12 | 31.5998 | 0.862637 | 37.3706 |
| 2024-acf-nationals | 47 | 79 | 18.3644 | 0.878434 | 35.2417 |
| 2024-acf-regionals-berkeley | 5 | 6 | 33.514 | 0.872082 | 47.6039 |
| 2024-acf-regionals-cornell | 4 | 7 | 25.0126 | 0.4 | 37.5476 |
| 2024-acf-regionals-imperial | 15 | 18 | 18.9417 | 0.927614 | 34.0462 |
| 2024-acf-regionals-jmu | 18 | 24 | 18.745 | 0.886364 | 30.4276 |
| 2024-acf-regionals-minnesota | 4 | 4 | 27.2728 | 0.8 | 70.7996 |
| 2024-acf-regionals-mit | 6 | 4 | 22.8879 | 0.942857 | 37.9925 |
| 2024-acf-regionals-nebraska | 12 | 13 | 10.1973 | 0.963224 | 19.7476 |
| 2024-acf-regionals-ohio-state | 6 | 6 | 14.4339 | 0.542857 | 19.8562 |
| 2024-acf-regionals-rutgers | 11 | 11 | 30.6236 | 0.936364 | 43.3948 |
| 2024-acf-regionals-vanderbilt | 10 | 11 | 24.7545 | 0.90303 | 50.8313 |
| 2024-acf-winter-at-brandeis | 20 | 18 | 24.6367 | 0.923656 | 38.9394 |
| 2024-acf-winter-at-central-florida | 9 | 10 | 18.3087 | 0.983333 | 26.7884 |
| 2024-acf-winter-at-clemson | 18 | 17 | 20.6217 | 0.883265 | 36.4318 |
| 2024-acf-winter-at-lehigh | 14 | 14 | 21.5323 | 0.966963 | 36.1904 |
| 2024-acf-winter-at-northwestern | 20 | 21 | 14.013 | 0.962016 | 25.7963 |
| 2024-acf-winter-at-ohio-state | 16 | 16 | 27.0241 | 0.893963 | 31.3155 |
| 2024-acf-winter-at-online | 18 | 19 | 25.4773 | 0.894737 | 43.4024 |
| 2024-acf-winter-at-oxford | 17 | 18 | 19.813 | 0.837127 | 42.0747 |
| 2024-acf-winter-at-ubc | 5 | 6 | 19.2339 | 0.1 | 29.7619 |
| 2024-acf-winter-at-uc-berkeley | 6 | 6 | 43.5378 | 0.6 | 66.9325 |

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
| bonus_part_correctness | aggregate | all | 25791 | 0.0157009 | 0.134603 | 0.888627 | 0.421291 |
| bonus_part_correctness | tier | fall | 7995 | 0.0169384 | 0.128851 | 0.89563 | 0.400279 |
| bonus_part_correctness | tier | nationals | 4095 | 0.0225772 | 0.135799 | 0.882164 | 0.427624 |
| bonus_part_correctness | tier | regionals | 5580 | 0.0190302 | 0.135402 | 0.887091 | 0.423132 |
| bonus_part_correctness | tier | winter | 8121 | 0.0221513 | 0.139114 | 0.881467 | 0.437518 |
| bonus_part_correctness | category | Current Events | 216 | 0.0472752 | 0.117956 | 0.909772 | 0.384347 |
| bonus_part_correctness | category | Fine Arts | 2970 | 0.0281512 | 0.14422 | 0.875396 | 0.44449 |
| bonus_part_correctness | category | Geography | 501 | 0.0683303 | 0.138339 | 0.883373 | 0.436471 |
| bonus_part_correctness | category | History | 4068 | 0.0143389 | 0.131184 | 0.893323 | 0.413546 |
| bonus_part_correctness | category | Literature | 4065 | 0.0302017 | 0.130607 | 0.893101 | 0.411769 |
| bonus_part_correctness | category | Mythology | 945 | 0.0231891 | 0.149707 | 0.859802 | 0.454901 |
| bonus_part_correctness | category | Other Academic | 219 | 0.0610518 | 0.144453 | 0.87621 | 0.456724 |
| bonus_part_correctness | category | Philosophy | 963 | 0.0310528 | 0.138775 | 0.879241 | 0.436631 |
| bonus_part_correctness | category | Popular Culture | 288 | 0.0488718 | 0.1436 | 0.873251 | 0.42783 |
| bonus_part_correctness | category | Religion | 1008 | 0.0335383 | 0.135372 | 0.889236 | 0.419734 |
| bonus_part_correctness | category | Science | 4059 | 0.0266347 | 0.132018 | 0.891558 | 0.417122 |
| bonus_part_correctness | category | Social Science | 909 | 0.035731 | 0.118691 | 0.912421 | 0.370384 |
| bonus_part_correctness | category | Unknown | 5580 | 0.0190302 | 0.135402 | 0.887091 | 0.423132 |
| bonus_part_correctness | difficulty | easy | 8597 | 0.0266345 | 0.0781535 | 0.791827 | 0.269973 |
| bonus_part_correctness | difficulty | hard | 8597 | 0.0387774 | 0.121297 | 0.746659 | 0.396434 |
| bonus_part_correctness | difficulty | medium | 8597 | 0.0391105 | 0.204359 | 0.750461 | 0.597465 |
