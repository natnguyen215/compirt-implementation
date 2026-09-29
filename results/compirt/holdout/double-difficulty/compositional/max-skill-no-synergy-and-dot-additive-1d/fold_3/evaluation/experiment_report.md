# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 22.8984 |
| tournament_team_bonus_ppg_spearman | 0.899166 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 461 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 36.8745 |
| bonus_game_margin_mae_games | 461 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.886111 |
| log_loss | 0.425649 |
| ece | 0.0147409 |
| brier | 0.13623 |
| part_accuracy | 0.805953 |
| part_accuracy_easy | 0.908457 |
| part_accuracy_medium | 0.676168 |
| part_accuracy_hard | 0.833235 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.525685 |
| accuracy_lift_over_all_correct | 0.280268 |
| part_accuracy_macro_team | 0.808901 |
| part_accuracy_macro_bonus | 0.801772 |
| part_count_easy | 8455 |
| part_count_medium | 8455 |
| part_count_hard | 8455 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.329122 |
| probability_p10 | 0.0754325 |
| probability_p50 | 0.51767 |
| probability_p90 | 0.937143 |
| mean_predictive_variance | 0.141414 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.510112 |
| ranked_probability_score | 0.120886 |
| bonus_total_score_log_loss | 1.04838 |
| ppb_mae | 2.41444 |
| ranked_probability_score_responses | 8455 |
| bonus_total_score_log_loss_responses | 8455 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 9 | 9 | 8.71321 | 1 | 17.4466 |
| 2024-acf-fall-at-cornell | 16 | 18 | 16.8472 | 0.868286 | 39.842 |
| 2024-acf-fall-at-georgia | 22 | 26 | 23.7845 | 0.910942 | 39.5264 |
| 2024-acf-fall-at-illinois | 16 | 15 | 22.1778 | 0.851253 | 37.2462 |
| 2024-acf-fall-at-north-carolina | 17 | 22 | 20.611 | 0.953375 | 36.7736 |
| 2024-acf-fall-at-ohio-state | 15 | 20 | 24.8567 | 0.976746 | 40.6322 |
| 2024-acf-fall-at-rutgers | 15 | 19 | 18.6949 | 0.890081 | 37.0178 |
| 2024-acf-fall-at-washington | 12 | 13 | 22.9256 | 0.853147 | 35.976 |
| 2024-acf-nationals | 46 | 79 | 24.5927 | 0.705374 | 38.8441 |
| 2024-acf-regionals-berkeley | 6 | 5 | 26.5298 | 0.898645 | 41.2355 |
| 2024-acf-regionals-cornell | 5 | 6 | 17.5904 | 0.9 | 20.5602 |
| 2024-acf-regionals-imperial | 15 | 17 | 22.0643 | 0.893655 | 35.9666 |
| 2024-acf-regionals-jmu | 19 | 25 | 23.3169 | 0.882353 | 39.3528 |
| 2024-acf-regionals-minnesota | 3 | 4 | 46.4168 | 1 | 72.3643 |
| 2024-acf-regionals-mit | 4 | 2 | 36.132 | 0.8 | 41.2453 |
| 2024-acf-regionals-nebraska | 11 | 13 | 24.0391 | 0.842827 | 31.328 |
| 2024-acf-regionals-ohio-state | 5 | 6 | 11.0614 | 1 | 27.7976 |
| 2024-acf-regionals-rutgers | 11 | 11 | 33.7838 | 0.810936 | 35.4506 |
| 2024-acf-regionals-vanderbilt | 10 | 10 | 15.9998 | 0.927273 | 28.7219 |
| 2024-acf-winter-at-brandeis | 17 | 16 | 20.1946 | 0.950921 | 28.156 |
| 2024-acf-winter-at-central-florida | 8 | 10 | 27.8187 | 0.97619 | 46.8866 |
| 2024-acf-winter-at-clemson | 16 | 17 | 21.05 | 0.938926 | 35.61 |
| 2024-acf-winter-at-lehigh | 14 | 14 | 18.6621 | 0.968097 | 36.6971 |
| 2024-acf-winter-at-northwestern | 16 | 18 | 16.4029 | 0.972774 | 36.855 |
| 2024-acf-winter-at-ohio-state | 15 | 17 | 28.5598 | 0.880726 | 49.7823 |
| 2024-acf-winter-at-online | 17 | 19 | 19.8129 | 0.93317 | 31.238 |
| 2024-acf-winter-at-oxford | 17 | 19 | 18.872 | 0.904412 | 30.4073 |
| 2024-acf-winter-at-ubc | 5 | 6 | 16.5746 | 0.7 | 38.862 |
| 2024-acf-winter-at-uc-berkeley | 6 | 5 | 35.9691 | 0.885714 | 35.3278 |

[Team PPG and absolute errors](csvs/bonus_team_ppg_leaderboard.csv); [game bonus margins](csvs/bonus_game_margin_predictions.csv).

### Bonus Distributions

Aggregate ability is part-weighted; synergy is response-weighted. Parameter plots describe fitted training parameters across entities, not posterior uncertainty intervals.

[Evaluated probabilities, aggregate ability, and synergy contributions](graphs/bonus/bonus_prediction_distributions.png).

[Fitted bonus parameters](graphs/parameters/bonus_part_parameter_distributions.png).

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in the diagnostic CSVs under `csvs/`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part_correctness | aggregate | all | 25365 | 0.0147409 | 0.13623 | 0.886111 | 0.425649 |
| bonus_part_correctness | tier | fall | 8094 | 0.025074 | 0.136115 | 0.884033 | 0.424018 |
| bonus_part_correctness | tier | nationals | 4125 | 0.0161042 | 0.146739 | 0.864009 | 0.458262 |
| bonus_part_correctness | tier | regionals | 5247 | 0.0179423 | 0.136162 | 0.885999 | 0.425629 |
| bonus_part_correctness | tier | winter | 7899 | 0.0202415 | 0.130907 | 0.894921 | 0.410303 |
| bonus_part_correctness | category | Current Events | 243 | 0.0756391 | 0.135414 | 0.884621 | 0.432961 |
| bonus_part_correctness | category | Fine Arts | 2937 | 0.0184908 | 0.149347 | 0.863822 | 0.461385 |
| bonus_part_correctness | category | Geography | 456 | 0.0587925 | 0.13349 | 0.886976 | 0.419277 |
| bonus_part_correctness | category | History | 4050 | 0.023278 | 0.133971 | 0.888774 | 0.419302 |
| bonus_part_correctness | category | Literature | 4029 | 0.0313725 | 0.135539 | 0.887662 | 0.423618 |
| bonus_part_correctness | category | Mythology | 936 | 0.0480145 | 0.131741 | 0.890943 | 0.410965 |
| bonus_part_correctness | category | Other Academic | 255 | 0.0471276 | 0.112862 | 0.913669 | 0.375596 |
| bonus_part_correctness | category | Philosophy | 948 | 0.033306 | 0.152598 | 0.859054 | 0.466653 |
| bonus_part_correctness | category | Popular Culture | 285 | 0.0783369 | 0.135972 | 0.890303 | 0.417917 |
| bonus_part_correctness | category | Religion | 1014 | 0.0271737 | 0.127653 | 0.89827 | 0.405147 |
| bonus_part_correctness | category | Science | 4059 | 0.0187418 | 0.133578 | 0.889916 | 0.418968 |
| bonus_part_correctness | category | Social Science | 906 | 0.0300737 | 0.124524 | 0.904495 | 0.390233 |
| bonus_part_correctness | category | Unknown | 5247 | 0.0179423 | 0.136162 | 0.885999 | 0.425629 |
| bonus_part_correctness | difficulty | easy | 8455 | 0.0575095 | 0.0746449 | 0.789853 | 0.266754 |
| bonus_part_correctness | difficulty | hard | 8455 | 0.0416638 | 0.124717 | 0.736733 | 0.402128 |
| bonus_part_correctness | difficulty | medium | 8455 | 0.0345076 | 0.209329 | 0.736799 | 0.608065 |
