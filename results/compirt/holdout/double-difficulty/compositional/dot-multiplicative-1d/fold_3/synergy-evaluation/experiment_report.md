# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 21.05 |
| tournament_team_bonus_ppg_spearman | 0.887429 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 461 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 33.1828 |
| bonus_game_margin_mae_games | 461 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.88939 |
| log_loss | 0.420043 |
| ece | 0.0171095 |
| brier | 0.134237 |
| part_accuracy | 0.807096 |
| part_accuracy_easy | 0.911768 |
| part_accuracy_medium | 0.67191 |
| part_accuracy_hard | 0.837611 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.525685 |
| accuracy_lift_over_all_correct | 0.281411 |
| part_accuracy_macro_team | 0.809743 |
| part_accuracy_macro_bonus | 0.807063 |
| part_count_easy | 8455 |
| part_count_medium | 8455 |
| part_count_hard | 8455 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.343679 |
| probability_p10 | 0.0598063 |
| probability_p50 | 0.542702 |
| probability_p90 | 0.963017 |
| mean_predictive_variance | 0.131006 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.508575 |
| ranked_probability_score | 0.119175 |
| bonus_total_score_log_loss | 1.042 |
| ppb_mae | 2.33161 |
| ranked_probability_score_responses | 8455 |
| bonus_total_score_log_loss_responses | 8455 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 9 | 9 | 13.6109 | 0.966667 | 22.4795 |
| 2024-acf-fall-at-cornell | 16 | 18 | 17.061 | 0.887417 | 35.1353 |
| 2024-acf-fall-at-georgia | 22 | 26 | 21.3345 | 0.945435 | 32.9421 |
| 2024-acf-fall-at-illinois | 16 | 15 | 13.5238 | 0.896908 | 22.4847 |
| 2024-acf-fall-at-north-carolina | 17 | 22 | 20.7661 | 0.896933 | 45.5112 |
| 2024-acf-fall-at-ohio-state | 15 | 20 | 19.6328 | 0.989268 | 32.3014 |
| 2024-acf-fall-at-rutgers | 15 | 19 | 24.9886 | 0.813226 | 45.8206 |
| 2024-acf-fall-at-washington | 12 | 13 | 23.4444 | 0.65035 | 40.3632 |
| 2024-acf-nationals | 46 | 79 | 18.1522 | 0.829703 | 30.7609 |
| 2024-acf-regionals-berkeley | 6 | 5 | 22.1822 | 0.927634 | 30.4759 |
| 2024-acf-regionals-cornell | 5 | 6 | 21.3281 | 0.9 | 18.7783 |
| 2024-acf-regionals-imperial | 15 | 17 | 22.5431 | 0.890081 | 35.335 |
| 2024-acf-regionals-jmu | 19 | 25 | 21.608 | 0.924496 | 27.9431 |
| 2024-acf-regionals-minnesota | 3 | 4 | 31.3753 | 1 | 53.527 |
| 2024-acf-regionals-mit | 4 | 2 | 22.6912 | 0.8 | 20.116 |
| 2024-acf-regionals-nebraska | 11 | 13 | 25.26 | 0.815492 | 40.2547 |
| 2024-acf-regionals-ohio-state | 5 | 6 | 14.4271 | 0.8 | 27.2921 |
| 2024-acf-regionals-rutgers | 11 | 11 | 28.4036 | 0.769934 | 32.8756 |
| 2024-acf-regionals-vanderbilt | 10 | 10 | 10.7694 | 0.987879 | 21.0962 |
| 2024-acf-winter-at-brandeis | 17 | 16 | 22.7548 | 0.966872 | 26.2043 |
| 2024-acf-winter-at-central-florida | 8 | 10 | 22.4894 | 1 | 33.74 |
| 2024-acf-winter-at-clemson | 16 | 17 | 19.4383 | 0.912436 | 27.5116 |
| 2024-acf-winter-at-lehigh | 14 | 14 | 20.294 | 0.981299 | 40.1857 |
| 2024-acf-winter-at-northwestern | 16 | 18 | 18.9633 | 0.943341 | 38.3569 |
| 2024-acf-winter-at-ohio-state | 15 | 17 | 24.1289 | 0.938126 | 35.8566 |
| 2024-acf-winter-at-online | 17 | 19 | 20.2255 | 0.887799 | 32.2957 |
| 2024-acf-winter-at-oxford | 17 | 19 | 19.9589 | 0.828431 | 28.374 |
| 2024-acf-winter-at-ubc | 5 | 6 | 18.7362 | 0.7 | 44.3984 |
| 2024-acf-winter-at-uc-berkeley | 6 | 5 | 30.3582 | 0.885714 | 42.3331 |

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
| bonus_part_correctness | aggregate | all | 25365 | 0.0171095 | 0.134237 | 0.88939 | 0.420043 |
| bonus_part_correctness | tier | fall | 8094 | 0.0211599 | 0.136861 | 0.882397 | 0.425474 |
| bonus_part_correctness | tier | nationals | 4125 | 0.0137875 | 0.137074 | 0.881654 | 0.429665 |
| bonus_part_correctness | tier | regionals | 5247 | 0.0327316 | 0.135798 | 0.888836 | 0.423552 |
| bonus_part_correctness | tier | winter | 7899 | 0.0150508 | 0.129028 | 0.896926 | 0.407123 |
| bonus_part_correctness | category | Current Events | 243 | 0.0823849 | 0.13261 | 0.886111 | 0.428777 |
| bonus_part_correctness | category | Fine Arts | 2937 | 0.0331834 | 0.145693 | 0.871188 | 0.44973 |
| bonus_part_correctness | category | Geography | 456 | 0.0401272 | 0.130004 | 0.889985 | 0.405991 |
| bonus_part_correctness | category | History | 4050 | 0.0176329 | 0.130773 | 0.893469 | 0.410393 |
| bonus_part_correctness | category | Literature | 4029 | 0.0183551 | 0.13252 | 0.891585 | 0.415089 |
| bonus_part_correctness | category | Mythology | 936 | 0.0415047 | 0.1304 | 0.893433 | 0.401765 |
| bonus_part_correctness | category | Other Academic | 255 | 0.0319445 | 0.105183 | 0.924522 | 0.344188 |
| bonus_part_correctness | category | Philosophy | 948 | 0.0606437 | 0.14883 | 0.866167 | 0.452149 |
| bonus_part_correctness | category | Popular Culture | 285 | 0.0770604 | 0.135548 | 0.889747 | 0.414489 |
| bonus_part_correctness | category | Religion | 1014 | 0.0162652 | 0.128152 | 0.897897 | 0.407092 |
| bonus_part_correctness | category | Science | 4059 | 0.0210238 | 0.133434 | 0.888784 | 0.424145 |
| bonus_part_correctness | category | Social Science | 906 | 0.0373915 | 0.120601 | 0.909477 | 0.377892 |
| bonus_part_correctness | category | Unknown | 5247 | 0.0327316 | 0.135798 | 0.888836 | 0.423552 |
| bonus_part_correctness | difficulty | easy | 8455 | 0.0271862 | 0.071628 | 0.791202 | 0.252408 |
| bonus_part_correctness | difficulty | hard | 8455 | 0.0392529 | 0.121501 | 0.749854 | 0.397099 |
| bonus_part_correctness | difficulty | medium | 8455 | 0.0490738 | 0.209581 | 0.738334 | 0.610623 |
