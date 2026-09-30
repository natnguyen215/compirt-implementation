# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 21.8973 |
| tournament_team_bonus_ppg_spearman | 0.878546 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 462 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 33.5497 |
| bonus_game_margin_mae_games | 462 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.89082 |
| log_loss | 0.417543 |
| ece | 0.018305 |
| brier | 0.133173 |
| part_accuracy | 0.809343 |
| part_accuracy_easy | 0.903207 |
| part_accuracy_medium | 0.687173 |
| part_accuracy_hard | 0.837648 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.519002 |
| accuracy_lift_over_all_correct | 0.29034 |
| part_accuracy_macro_team | 0.812576 |
| part_accuracy_macro_bonus | 0.806246 |
| part_count_easy | 8420 |
| part_count_medium | 8420 |
| part_count_hard | 8420 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.348751 |
| probability_p10 | 0.054715 |
| probability_p50 | 0.532905 |
| probability_p90 | 0.964951 |
| mean_predictive_variance | 0.127754 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.51639 |
| ranked_probability_score | 0.115239 |
| bonus_total_score_log_loss | 1.01284 |
| ppb_mae | 2.39487 |
| ranked_probability_score_responses | 8420 |
| bonus_total_score_log_loss_responses | 8420 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 8 | 9 | 14.4356 | 0.862291 | 31.155 |
| 2024-acf-fall-at-cornell | 17 | 18 | 20.1431 | 0.796071 | 34.4342 |
| 2024-acf-fall-at-georgia | 21 | 23 | 16.8639 | 0.927226 | 26.7418 |
| 2024-acf-fall-at-illinois | 17 | 19 | 23.8232 | 0.881925 | 34.7272 |
| 2024-acf-fall-at-north-carolina | 18 | 22 | 16.5211 | 0.971606 | 27.8459 |
| 2024-acf-fall-at-ohio-state | 18 | 20 | 18.06 | 0.889463 | 39.9582 |
| 2024-acf-fall-at-rutgers | 15 | 19 | 18.979 | 0.932143 | 31.7754 |
| 2024-acf-fall-at-washington | 12 | 13 | 20.6297 | 0.725045 | 32.9416 |
| 2024-acf-nationals | 48 | 80 | 18.9705 | 0.899514 | 32.6628 |
| 2024-acf-regionals-berkeley | 6 | 7 | 27.4042 | 0.942857 | 35.1398 |
| 2024-acf-regionals-cornell | 6 | 6 | 33.3304 | 0.6 | 51.4481 |
| 2024-acf-regionals-imperial | 15 | 18 | 22.2166 | 0.882143 | 44.729 |
| 2024-acf-regionals-jmu | 19 | 23 | 24.7729 | 0.960948 | 32.4013 |
| 2024-acf-regionals-minnesota | 3 | 4 | 27.0073 | 0.5 | 28.3549 |
| 2024-acf-regionals-mit | 7 | 4 | 23.8494 | 1 | 36.7995 |
| 2024-acf-regionals-nebraska | 11 | 13 | 20.4722 | 0.883829 | 38.6522 |
| 2024-acf-regionals-ohio-state | 7 | 5 | 26.1581 | 0.964286 | 29.7891 |
| 2024-acf-regionals-rutgers | 10 | 11 | 23.5369 | 0.975758 | 42.695 |
| 2024-acf-regionals-vanderbilt | 10 | 9 | 28.5454 | 0.951515 | 46.5939 |
| 2024-acf-winter-at-brandeis | 16 | 16 | 20.809 | 0.927153 | 19.638 |
| 2024-acf-winter-at-central-florida | 9 | 10 | 24.4637 | 0.95 | 19.5112 |
| 2024-acf-winter-at-clemson | 15 | 17 | 17.3341 | 0.949062 | 33.0695 |
| 2024-acf-winter-at-lehigh | 13 | 12 | 16.5544 | 0.973866 | 39.6761 |
| 2024-acf-winter-at-northwestern | 17 | 18 | 19.2059 | 0.892157 | 30.9939 |
| 2024-acf-winter-at-ohio-state | 16 | 16 | 17.7265 | 0.910835 | 33.116 |
| 2024-acf-winter-at-online | 15 | 20 | 21.5354 | 0.9 | 34.609 |
| 2024-acf-winter-at-oxford | 17 | 19 | 17.9777 | 0.905522 | 31.7177 |
| 2024-acf-winter-at-ubc | 6 | 6 | 23.1332 | 0.942857 | 26.6961 |
| 2024-acf-winter-at-uc-berkeley | 6 | 5 | 30.5623 | 0.579771 | 54.3388 |

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
| bonus_part_correctness | aggregate | all | 25260 | 0.018305 | 0.133173 | 0.89082 | 0.417543 |
| bonus_part_correctness | tier | fall | 8160 | 0.0141812 | 0.132586 | 0.887186 | 0.4134 |
| bonus_part_correctness | tier | nationals | 4107 | 0.0319839 | 0.130075 | 0.892171 | 0.411315 |
| bonus_part_correctness | tier | regionals | 5280 | 0.0325237 | 0.140732 | 0.880633 | 0.435201 |
| bonus_part_correctness | tier | winter | 7713 | 0.028068 | 0.130271 | 0.892918 | 0.413153 |
| bonus_part_correctness | category | Current Events | 249 | 0.0356089 | 0.120885 | 0.90399 | 0.389533 |
| bonus_part_correctness | category | Fine Arts | 2934 | 0.0178249 | 0.142093 | 0.876146 | 0.443446 |
| bonus_part_correctness | category | Geography | 459 | 0.0328857 | 0.134898 | 0.877445 | 0.426583 |
| bonus_part_correctness | category | History | 4017 | 0.0259651 | 0.12857 | 0.897879 | 0.403212 |
| bonus_part_correctness | category | Literature | 4047 | 0.0229153 | 0.12628 | 0.899055 | 0.403732 |
| bonus_part_correctness | category | Mythology | 924 | 0.043201 | 0.143224 | 0.869522 | 0.440046 |
| bonus_part_correctness | category | Other Academic | 237 | 0.0658119 | 0.113944 | 0.927899 | 0.358974 |
| bonus_part_correctness | category | Philosophy | 948 | 0.038493 | 0.136475 | 0.884087 | 0.430359 |
| bonus_part_correctness | category | Popular Culture | 294 | 0.0540023 | 0.131401 | 0.8871 | 0.401792 |
| bonus_part_correctness | category | Religion | 984 | 0.0234864 | 0.126541 | 0.898034 | 0.406517 |
| bonus_part_correctness | category | Science | 3990 | 0.0209951 | 0.132272 | 0.892539 | 0.413245 |
| bonus_part_correctness | category | Social Science | 897 | 0.0430574 | 0.116856 | 0.910986 | 0.37363 |
| bonus_part_correctness | category | Unknown | 5280 | 0.0325237 | 0.140732 | 0.880633 | 0.435201 |
| bonus_part_correctness | difficulty | easy | 8420 | 0.0204005 | 0.077421 | 0.778927 | 0.270722 |
| bonus_part_correctness | difficulty | hard | 8420 | 0.0315099 | 0.120335 | 0.758186 | 0.389597 |
| bonus_part_correctness | difficulty | medium | 8420 | 0.04732 | 0.201764 | 0.757874 | 0.592309 |
