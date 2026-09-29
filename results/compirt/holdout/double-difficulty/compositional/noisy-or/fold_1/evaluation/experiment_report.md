# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 21.9052 |
| tournament_team_bonus_ppg_spearman | 0.880364 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 462 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 33.7867 |
| bonus_game_margin_mae_games | 462 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.89129 |
| log_loss | 0.416547 |
| ece | 0.0177061 |
| brier | 0.132917 |
| part_accuracy | 0.809026 |
| part_accuracy_easy | 0.899644 |
| part_accuracy_medium | 0.689905 |
| part_accuracy_hard | 0.83753 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.519002 |
| accuracy_lift_over_all_correct | 0.290024 |
| part_accuracy_macro_team | 0.81287 |
| part_accuracy_macro_bonus | 0.806267 |
| part_count_easy | 8420 |
| part_count_medium | 8420 |
| part_count_hard | 8420 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.357256 |
| probability_p10 | 0.0541649 |
| probability_p50 | 0.50722 |
| probability_p90 | 0.987467 |
| mean_predictive_variance | 0.121922 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.516271 |
| ranked_probability_score | 0.115687 |
| bonus_total_score_log_loss | 1.01789 |
| ppb_mae | 2.38356 |
| ranked_probability_score_responses | 8420 |
| bonus_total_score_log_loss_responses | 8420 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 8 | 9 | 13.4808 | 0.934148 | 30.2141 |
| 2024-acf-fall-at-cornell | 17 | 18 | 19.7376 | 0.803442 | 33.7374 |
| 2024-acf-fall-at-georgia | 21 | 23 | 16.465 | 0.927226 | 25.6341 |
| 2024-acf-fall-at-illinois | 17 | 19 | 23.4925 | 0.881925 | 33.5369 |
| 2024-acf-fall-at-north-carolina | 18 | 22 | 16.655 | 0.969541 | 28.0453 |
| 2024-acf-fall-at-ohio-state | 18 | 20 | 19.1944 | 0.889463 | 41.0042 |
| 2024-acf-fall-at-rutgers | 15 | 19 | 18.1626 | 0.925 | 31.8503 |
| 2024-acf-fall-at-washington | 12 | 13 | 21.5365 | 0.739055 | 33.0351 |
| 2024-acf-nationals | 48 | 80 | 19.3494 | 0.890771 | 33.5951 |
| 2024-acf-regionals-berkeley | 6 | 7 | 28.3422 | 0.942857 | 34.6359 |
| 2024-acf-regionals-cornell | 6 | 6 | 32.4502 | 0.6 | 50.4693 |
| 2024-acf-regionals-imperial | 15 | 18 | 20.7456 | 0.882143 | 43.7173 |
| 2024-acf-regionals-jmu | 19 | 23 | 25.315 | 0.95656 | 34.8111 |
| 2024-acf-regionals-minnesota | 3 | 4 | 30.3201 | 0.5 | 30.4318 |
| 2024-acf-regionals-mit | 7 | 4 | 24.7392 | 1 | 38.0191 |
| 2024-acf-regionals-nebraska | 11 | 13 | 18.4993 | 0.883829 | 38.6245 |
| 2024-acf-regionals-ohio-state | 7 | 5 | 26.5608 | 0.964286 | 31.5202 |
| 2024-acf-regionals-rutgers | 10 | 11 | 25.7807 | 0.975758 | 44.0758 |
| 2024-acf-regionals-vanderbilt | 10 | 9 | 26.0292 | 0.951515 | 42.2094 |
| 2024-acf-winter-at-brandeis | 16 | 16 | 21.167 | 0.927153 | 19.9998 |
| 2024-acf-winter-at-central-florida | 9 | 10 | 23.7527 | 0.966667 | 19.48 |
| 2024-acf-winter-at-clemson | 15 | 17 | 18.713 | 0.949062 | 34.5276 |
| 2024-acf-winter-at-lehigh | 13 | 12 | 15.9856 | 0.973866 | 40.4146 |
| 2024-acf-winter-at-northwestern | 17 | 18 | 18.1698 | 0.911765 | 28.1879 |
| 2024-acf-winter-at-ohio-state | 16 | 16 | 18.396 | 0.910835 | 35.0665 |
| 2024-acf-winter-at-online | 15 | 20 | 21.2065 | 0.875 | 34.5952 |
| 2024-acf-winter-at-oxford | 17 | 19 | 18.9363 | 0.876074 | 32.8023 |
| 2024-acf-winter-at-ubc | 6 | 6 | 23.0361 | 0.942857 | 26.245 |
| 2024-acf-winter-at-uc-berkeley | 6 | 5 | 29.0317 | 0.579771 | 57.0591 |

[Team PPG and absolute errors](csvs/bonus_team_ppg_leaderboard.csv); [game bonus margins](csvs/bonus_game_margin_predictions.csv).

### Bonus Distributions

Aggregate ability is part-weighted; synergy is response-weighted. Parameter plots describe fitted training parameters across entities, not posterior uncertainty intervals.

[Evaluated probabilities, aggregate ability, and synergy contributions](graphs/bonus/bonus_prediction_distributions.png).

[Fitted bonus parameters](graphs/parameters/bonus_part_parameter_distributions.png).

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in the diagnostic CSVs under `csvs/`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part_correctness | aggregate | all | 25260 | 0.0177061 | 0.132917 | 0.89129 | 0.416547 |
| bonus_part_correctness | tier | fall | 8160 | 0.0185572 | 0.132955 | 0.886962 | 0.414609 |
| bonus_part_correctness | tier | nationals | 4107 | 0.0272303 | 0.130452 | 0.889795 | 0.415689 |
| bonus_part_correctness | tier | regionals | 5280 | 0.0297362 | 0.140253 | 0.881048 | 0.433787 |
| bonus_part_correctness | tier | winter | 7713 | 0.017904 | 0.129169 | 0.895014 | 0.407251 |
| bonus_part_correctness | category | Current Events | 249 | 0.0571668 | 0.123874 | 0.898954 | 0.404555 |
| bonus_part_correctness | category | Fine Arts | 2934 | 0.0260578 | 0.142642 | 0.875996 | 0.443098 |
| bonus_part_correctness | category | Geography | 459 | 0.0543766 | 0.135516 | 0.881509 | 0.421127 |
| bonus_part_correctness | category | History | 4017 | 0.0171606 | 0.127046 | 0.899689 | 0.398578 |
| bonus_part_correctness | category | Literature | 4047 | 0.0227551 | 0.126311 | 0.898752 | 0.405939 |
| bonus_part_correctness | category | Mythology | 924 | 0.0350779 | 0.141846 | 0.871965 | 0.434208 |
| bonus_part_correctness | category | Other Academic | 237 | 0.0684965 | 0.115374 | 0.92255 | 0.373077 |
| bonus_part_correctness | category | Philosophy | 948 | 0.032395 | 0.136098 | 0.883076 | 0.428226 |
| bonus_part_correctness | category | Popular Culture | 294 | 0.0581841 | 0.13154 | 0.885574 | 0.397748 |
| bonus_part_correctness | category | Religion | 984 | 0.036004 | 0.125138 | 0.902201 | 0.399026 |
| bonus_part_correctness | category | Science | 3990 | 0.0183992 | 0.132621 | 0.892184 | 0.4136 |
| bonus_part_correctness | category | Social Science | 897 | 0.0379482 | 0.117588 | 0.910598 | 0.376971 |
| bonus_part_correctness | category | Unknown | 5280 | 0.0297362 | 0.140253 | 0.881048 | 0.433787 |
| bonus_part_correctness | difficulty | easy | 8420 | 0.027078 | 0.0776344 | 0.79009 | 0.271351 |
| bonus_part_correctness | difficulty | hard | 8420 | 0.0251661 | 0.119445 | 0.758159 | 0.387826 |
| bonus_part_correctness | difficulty | medium | 8420 | 0.042428 | 0.201672 | 0.756479 | 0.590463 |
