# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 23.8717 |
| tournament_team_bonus_ppg_spearman | 0.877058 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 462 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 35.1011 |
| bonus_game_margin_mae_games | 462 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.887485 |
| log_loss | 0.423292 |
| ece | 0.014179 |
| brier | 0.135149 |
| part_accuracy | 0.807918 |
| part_accuracy_easy | 0.901425 |
| part_accuracy_medium | 0.686223 |
| part_accuracy_hard | 0.836105 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.519002 |
| accuracy_lift_over_all_correct | 0.288915 |
| part_accuracy_macro_team | 0.81094 |
| part_accuracy_macro_bonus | 0.803391 |
| part_count_easy | 8420 |
| part_count_medium | 8420 |
| part_count_hard | 8420 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.329433 |
| probability_p10 | 0.07609 |
| probability_p50 | 0.510132 |
| probability_p90 | 0.939537 |
| mean_predictive_variance | 0.141291 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.514608 |
| ranked_probability_score | 0.117051 |
| bonus_total_score_log_loss | 1.02126 |
| ppb_mae | 2.53422 |
| ranked_probability_score_responses | 8420 |
| bonus_total_score_log_loss_responses | 8420 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 8 | 9 | 32.9473 | 0.886243 | 40.8937 |
| 2024-acf-fall-at-cornell | 17 | 18 | 12.4065 | 0.900494 | 27.9567 |
| 2024-acf-fall-at-georgia | 21 | 23 | 18.9864 | 0.924627 | 33.2472 |
| 2024-acf-fall-at-illinois | 17 | 19 | 29.9631 | 0.916365 | 40.3556 |
| 2024-acf-fall-at-north-carolina | 18 | 22 | 13.4931 | 0.951988 | 26.8627 |
| 2024-acf-fall-at-ohio-state | 18 | 20 | 21.0704 | 0.950414 | 38.4528 |
| 2024-acf-fall-at-rutgers | 15 | 19 | 22.0259 | 0.946429 | 31.0778 |
| 2024-acf-fall-at-washington | 12 | 13 | 23.0767 | 0.65149 | 29.0926 |
| 2024-acf-nationals | 48 | 80 | 21.9228 | 0.874644 | 33.1073 |
| 2024-acf-regionals-berkeley | 6 | 7 | 29.994 | 0.885714 | 42.2575 |
| 2024-acf-regionals-cornell | 6 | 6 | 29.9272 | 0.657143 | 41.1599 |
| 2024-acf-regionals-imperial | 15 | 18 | 27.1265 | 0.853571 | 54.4608 |
| 2024-acf-regionals-jmu | 19 | 23 | 26.7551 | 0.897762 | 41.8803 |
| 2024-acf-regionals-minnesota | 3 | 4 | 33.0283 | 0.5 | 46.7573 |
| 2024-acf-regionals-mit | 7 | 4 | 30.8334 | 0.964286 | 38.1575 |
| 2024-acf-regionals-nebraska | 11 | 13 | 20.4791 | 0.947611 | 40.206 |
| 2024-acf-regionals-ohio-state | 7 | 5 | 28.251 | 0.928571 | 26.9225 |
| 2024-acf-regionals-rutgers | 10 | 11 | 27.3914 | 0.975758 | 36.3725 |
| 2024-acf-regionals-vanderbilt | 10 | 9 | 20.0901 | 0.975758 | 28.9912 |
| 2024-acf-winter-at-brandeis | 16 | 16 | 22.1565 | 0.934511 | 24.7545 |
| 2024-acf-winter-at-central-florida | 9 | 10 | 21.8505 | 0.966667 | 19.8881 |
| 2024-acf-winter-at-clemson | 15 | 17 | 24.9028 | 0.945487 | 39.8927 |
| 2024-acf-winter-at-lehigh | 13 | 12 | 22.2217 | 0.902339 | 40.0242 |
| 2024-acf-winter-at-northwestern | 17 | 18 | 15.9215 | 0.931373 | 21.786 |
| 2024-acf-winter-at-ohio-state | 16 | 16 | 22.91 | 0.87841 | 33.8924 |
| 2024-acf-winter-at-online | 15 | 20 | 25.2656 | 0.867857 | 40.8352 |
| 2024-acf-winter-at-oxford | 17 | 19 | 20.0108 | 0.895706 | 33.994 |
| 2024-acf-winter-at-ubc | 6 | 6 | 24.9353 | 0.885714 | 52.1331 |
| 2024-acf-winter-at-uc-berkeley | 6 | 5 | 22.3353 | 0.637748 | 45.8347 |

[Team PPG and absolute errors](csvs/bonus_team_ppg_leaderboard.csv); [game bonus margins](csvs/bonus_game_margin_predictions.csv).

### Bonus Distributions

Aggregate ability is part-weighted; synergy is response-weighted. Parameter plots describe fitted training parameters across entities, not posterior uncertainty intervals.

[Evaluated probabilities, aggregate ability, and synergy contributions](graphs/bonus/bonus_prediction_distributions.png).

[Fitted bonus parameters](graphs/parameters/bonus_part_parameter_distributions.png).

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in the diagnostic CSVs under `csvs/`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part_correctness | aggregate | all | 25260 | 0.014179 | 0.135149 | 0.887485 | 0.423292 |
| bonus_part_correctness | tier | fall | 8160 | 0.0274869 | 0.134756 | 0.88387 | 0.420547 |
| bonus_part_correctness | tier | nationals | 4107 | 0.0360008 | 0.134153 | 0.88485 | 0.424245 |
| bonus_part_correctness | tier | regionals | 5280 | 0.0268513 | 0.143766 | 0.873214 | 0.446149 |
| bonus_part_correctness | tier | winter | 7713 | 0.0222557 | 0.130197 | 0.894398 | 0.410043 |
| bonus_part_correctness | category | Current Events | 249 | 0.0426495 | 0.13263 | 0.885718 | 0.42537 |
| bonus_part_correctness | category | Fine Arts | 2934 | 0.0152013 | 0.143736 | 0.873283 | 0.445755 |
| bonus_part_correctness | category | Geography | 459 | 0.045778 | 0.13148 | 0.888028 | 0.411191 |
| bonus_part_correctness | category | History | 4017 | 0.0247837 | 0.128107 | 0.898424 | 0.404205 |
| bonus_part_correctness | category | Literature | 4047 | 0.0209302 | 0.129492 | 0.89501 | 0.40962 |
| bonus_part_correctness | category | Mythology | 924 | 0.0273307 | 0.147915 | 0.859713 | 0.453138 |
| bonus_part_correctness | category | Other Academic | 237 | 0.0600174 | 0.120652 | 0.916631 | 0.386031 |
| bonus_part_correctness | category | Philosophy | 948 | 0.0422804 | 0.138949 | 0.879649 | 0.435258 |
| bonus_part_correctness | category | Popular Culture | 294 | 0.0837034 | 0.130223 | 0.893519 | 0.399996 |
| bonus_part_correctness | category | Religion | 984 | 0.040376 | 0.128713 | 0.897327 | 0.407403 |
| bonus_part_correctness | category | Science | 3990 | 0.0219899 | 0.133432 | 0.890635 | 0.418339 |
| bonus_part_correctness | category | Social Science | 897 | 0.0295141 | 0.118953 | 0.909832 | 0.381615 |
| bonus_part_correctness | category | Unknown | 5280 | 0.0268513 | 0.143766 | 0.873214 | 0.446149 |
| bonus_part_correctness | difficulty | easy | 8420 | 0.0535269 | 0.0795006 | 0.78355 | 0.279211 |
| bonus_part_correctness | difficulty | hard | 8420 | 0.0331759 | 0.122437 | 0.750527 | 0.395725 |
| bonus_part_correctness | difficulty | medium | 8420 | 0.0325734 | 0.20351 | 0.750744 | 0.594942 |
