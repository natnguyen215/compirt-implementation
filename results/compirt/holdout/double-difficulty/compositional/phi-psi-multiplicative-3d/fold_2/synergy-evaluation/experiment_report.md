# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 22.0258 |
| tournament_team_bonus_ppg_spearman | 0.849534 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 469 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 34.016 |
| bonus_game_margin_mae_games | 469 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.888699 |
| log_loss | 0.420902 |
| ece | 0.01528 |
| brier | 0.134522 |
| part_accuracy | 0.810011 |
| part_accuracy_easy | 0.900896 |
| part_accuracy_medium | 0.687333 |
| part_accuracy_hard | 0.841805 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.519367 |
| accuracy_lift_over_all_correct | 0.290644 |
| part_accuracy_macro_team | 0.813747 |
| part_accuracy_macro_bonus | 0.807446 |
| part_count_easy | 8597 |
| part_count_medium | 8597 |
| part_count_hard | 8597 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.343116 |
| probability_p10 | 0.0543565 |
| probability_p50 | 0.51653 |
| probability_p90 | 0.957773 |
| mean_predictive_variance | 0.132003 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.515645 |
| ranked_probability_score | 0.116759 |
| bonus_total_score_log_loss | 1.02383 |
| ppb_mae | 2.28898 |
| ranked_probability_score_responses | 8597 |
| bonus_total_score_log_loss_responses | 8597 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 8 | 9 | 12.9544 | 0.97619 | 26.1143 |
| 2024-acf-fall-at-cornell | 17 | 18 | 23.4205 | 0.851534 | 34.7426 |
| 2024-acf-fall-at-georgia | 22 | 24 | 20.1013 | 0.909504 | 34.1199 |
| 2024-acf-fall-at-illinois | 19 | 21 | 17.8914 | 0.968421 | 29.8649 |
| 2024-acf-fall-at-north-carolina | 18 | 22 | 13.9189 | 0.950464 | 19.2302 |
| 2024-acf-fall-at-ohio-state | 18 | 19 | 24.5909 | 0.945793 | 30.4761 |
| 2024-acf-fall-at-rutgers | 16 | 16 | 13.9205 | 0.949927 | 20.4319 |
| 2024-acf-fall-at-washington | 13 | 12 | 31.4532 | 0.846154 | 37.7307 |
| 2024-acf-nationals | 47 | 79 | 18.6269 | 0.877971 | 35.092 |
| 2024-acf-regionals-berkeley | 5 | 6 | 34.2615 | 0.974679 | 47.7925 |
| 2024-acf-regionals-cornell | 4 | 7 | 24.475 | 0.4 | 35.8694 |
| 2024-acf-regionals-imperial | 15 | 18 | 18.8881 | 0.927614 | 34.8533 |
| 2024-acf-regionals-jmu | 18 | 24 | 18.7788 | 0.886364 | 31.0211 |
| 2024-acf-regionals-minnesota | 4 | 4 | 27.1112 | 0.8 | 71.42 |
| 2024-acf-regionals-mit | 6 | 4 | 22.8638 | 0.942857 | 37.9172 |
| 2024-acf-regionals-nebraska | 12 | 13 | 10.408 | 0.963224 | 20.8368 |
| 2024-acf-regionals-ohio-state | 6 | 6 | 14.1787 | 0.542857 | 20.2705 |
| 2024-acf-regionals-rutgers | 11 | 11 | 30.7649 | 0.963636 | 44.0653 |
| 2024-acf-regionals-vanderbilt | 10 | 11 | 24.3114 | 0.90303 | 50.5309 |
| 2024-acf-winter-at-brandeis | 20 | 18 | 24.8691 | 0.916134 | 39.1753 |
| 2024-acf-winter-at-central-florida | 9 | 10 | 18.1079 | 0.983333 | 27.8245 |
| 2024-acf-winter-at-clemson | 18 | 17 | 20.0047 | 0.893596 | 35.796 |
| 2024-acf-winter-at-lehigh | 14 | 14 | 22.2052 | 0.973571 | 36.7735 |
| 2024-acf-winter-at-northwestern | 20 | 21 | 14.0286 | 0.962016 | 26.0983 |
| 2024-acf-winter-at-ohio-state | 16 | 16 | 27.3442 | 0.879235 | 31.0365 |
| 2024-acf-winter-at-online | 18 | 19 | 25.3586 | 0.911249 | 43.3272 |
| 2024-acf-winter-at-oxford | 17 | 18 | 20.3009 | 0.837127 | 41.9896 |
| 2024-acf-winter-at-ubc | 5 | 6 | 19.7147 | 0.1 | 29.4466 |
| 2024-acf-winter-at-uc-berkeley | 6 | 6 | 43.8956 | 0.6 | 67.6292 |

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
| bonus_part_correctness | aggregate | all | 25791 | 0.01528 | 0.134522 | 0.888699 | 0.420902 |
| bonus_part_correctness | tier | fall | 7995 | 0.0208366 | 0.128547 | 0.896017 | 0.400048 |
| bonus_part_correctness | tier | nationals | 4095 | 0.0230781 | 0.135885 | 0.881637 | 0.428804 |
| bonus_part_correctness | tier | regionals | 5580 | 0.0236712 | 0.135841 | 0.886635 | 0.424033 |
| bonus_part_correctness | tier | winter | 8121 | 0.0188294 | 0.138809 | 0.881926 | 0.435297 |
| bonus_part_correctness | category | Current Events | 216 | 0.0641496 | 0.117547 | 0.90805 | 0.385276 |
| bonus_part_correctness | category | Fine Arts | 2970 | 0.0339392 | 0.144734 | 0.874557 | 0.44529 |
| bonus_part_correctness | category | Geography | 501 | 0.0548129 | 0.137305 | 0.88295 | 0.434724 |
| bonus_part_correctness | category | History | 4068 | 0.0199335 | 0.130467 | 0.894392 | 0.411311 |
| bonus_part_correctness | category | Literature | 4065 | 0.023076 | 0.13011 | 0.894135 | 0.409801 |
| bonus_part_correctness | category | Mythology | 945 | 0.0242853 | 0.150169 | 0.858329 | 0.456673 |
| bonus_part_correctness | category | Other Academic | 219 | 0.0699295 | 0.144064 | 0.874708 | 0.455132 |
| bonus_part_correctness | category | Philosophy | 963 | 0.0355088 | 0.138622 | 0.879738 | 0.43531 |
| bonus_part_correctness | category | Popular Culture | 288 | 0.077629 | 0.142565 | 0.871553 | 0.430122 |
| bonus_part_correctness | category | Religion | 1008 | 0.03912 | 0.134761 | 0.889496 | 0.417708 |
| bonus_part_correctness | category | Science | 4059 | 0.0266335 | 0.132116 | 0.891419 | 0.417377 |
| bonus_part_correctness | category | Social Science | 909 | 0.0364516 | 0.118447 | 0.912816 | 0.371071 |
| bonus_part_correctness | category | Unknown | 5580 | 0.0236712 | 0.135841 | 0.886635 | 0.424033 |
| bonus_part_correctness | difficulty | easy | 8597 | 0.0312617 | 0.0785153 | 0.791823 | 0.271534 |
| bonus_part_correctness | difficulty | hard | 8597 | 0.0383839 | 0.120878 | 0.748111 | 0.394961 |
| bonus_part_correctness | difficulty | medium | 8597 | 0.0369664 | 0.204171 | 0.749921 | 0.59621 |
