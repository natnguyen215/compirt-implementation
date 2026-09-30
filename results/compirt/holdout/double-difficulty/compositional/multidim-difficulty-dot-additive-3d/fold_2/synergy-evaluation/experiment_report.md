# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 15.2401 |
| tournament_team_bonus_ppg_spearman | 0.884788 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 469 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 26.5328 |
| bonus_game_margin_mae_games | 469 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.896472 |
| log_loss | 0.406529 |
| ece | 0.0121271 |
| brier | 0.129608 |
| part_accuracy | 0.814082 |
| part_accuracy_easy | 0.892986 |
| part_accuracy_medium | 0.704199 |
| part_accuracy_hard | 0.845062 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.519367 |
| accuracy_lift_over_all_correct | 0.294715 |
| part_accuracy_macro_team | 0.818637 |
| part_accuracy_macro_bonus | 0.812934 |
| part_count_easy | 8597 |
| part_count_medium | 8597 |
| part_count_hard | 8597 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.355329 |
| probability_p10 | 0.0402509 |
| probability_p50 | 0.498095 |
| probability_p90 | 0.984224 |
| mean_predictive_variance | 0.123574 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.526346 |
| ranked_probability_score | 0.111413 |
| bonus_total_score_log_loss | 0.987652 |
| ppb_mae | 1.60318 |
| ranked_probability_score_responses | 8597 |
| bonus_total_score_log_loss_responses | 8597 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 8 | 9 | 20.4706 | 0.809524 | 32.6481 |
| 2024-acf-fall-at-cornell | 17 | 18 | 13.8601 | 0.970553 | 24.9465 |
| 2024-acf-fall-at-georgia | 22 | 24 | 12.1334 | 0.955318 | 25.7908 |
| 2024-acf-fall-at-illinois | 19 | 21 | 11.9872 | 0.964912 | 24.8482 |
| 2024-acf-fall-at-north-carolina | 18 | 22 | 14.7473 | 0.950464 | 27.751 |
| 2024-acf-fall-at-ohio-state | 18 | 19 | 15.1762 | 0.974703 | 27.2231 |
| 2024-acf-fall-at-rutgers | 16 | 16 | 15.7169 | 0.970546 | 24.8514 |
| 2024-acf-fall-at-washington | 13 | 12 | 24.4777 | 0.917582 | 28.4587 |
| 2024-acf-nationals | 47 | 79 | 9.69151 | 0.965242 | 24.33 |
| 2024-acf-regionals-berkeley | 5 | 6 | 7.25491 | 0.872082 | 9.65837 |
| 2024-acf-regionals-cornell | 4 | 7 | 22.2411 | 0.4 | 36.3402 |
| 2024-acf-regionals-imperial | 15 | 18 | 9.46274 | 0.966935 | 18.0183 |
| 2024-acf-regionals-jmu | 18 | 24 | 10.5021 | 0.958678 | 22.4186 |
| 2024-acf-regionals-minnesota | 4 | 4 | 29.0167 | 0.4 | 51.0653 |
| 2024-acf-regionals-mit | 6 | 4 | 15.2088 | 0.942857 | 23.6126 |
| 2024-acf-regionals-nebraska | 12 | 13 | 11.2435 | 0.952716 | 29.6946 |
| 2024-acf-regionals-ohio-state | 6 | 6 | 11.1025 | 0.828571 | 14.9963 |
| 2024-acf-regionals-rutgers | 11 | 11 | 15.4885 | 0.954545 | 26.7637 |
| 2024-acf-regionals-vanderbilt | 10 | 11 | 14.9436 | 0.939394 | 30.5968 |
| 2024-acf-winter-at-brandeis | 20 | 18 | 18.2399 | 0.940955 | 28.6683 |
| 2024-acf-winter-at-central-florida | 9 | 10 | 12.3527 | 0.983333 | 16.0065 |
| 2024-acf-winter-at-clemson | 18 | 17 | 12.682 | 0.947315 | 27.8068 |
| 2024-acf-winter-at-lehigh | 14 | 14 | 7.67079 | 0.969165 | 18.2371 |
| 2024-acf-winter-at-northwestern | 20 | 21 | 13.4498 | 0.962768 | 22.6437 |
| 2024-acf-winter-at-ohio-state | 16 | 16 | 19.8175 | 0.954346 | 30.5387 |
| 2024-acf-winter-at-online | 18 | 19 | 19.0481 | 0.909185 | 39.8856 |
| 2024-acf-winter-at-oxford | 17 | 18 | 20.38 | 0.740016 | 39.6966 |
| 2024-acf-winter-at-ubc | 5 | 6 | 6.24141 | 0.9 | 20.8796 |
| 2024-acf-winter-at-uc-berkeley | 6 | 6 | 27.3544 | 0.657143 | 37.4921 |

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
| bonus_part_correctness | aggregate | all | 25791 | 0.0121271 | 0.129608 | 0.896472 | 0.406529 |
| bonus_part_correctness | tier | fall | 7995 | 0.0122832 | 0.125816 | 0.900151 | 0.391185 |
| bonus_part_correctness | tier | nationals | 4095 | 0.0154421 | 0.128016 | 0.895117 | 0.404103 |
| bonus_part_correctness | tier | regionals | 5580 | 0.019485 | 0.129621 | 0.896156 | 0.404776 |
| bonus_part_correctness | tier | winter | 8121 | 0.0216169 | 0.134135 | 0.889126 | 0.424062 |
| bonus_part_correctness | category | Current Events | 216 | 0.0376462 | 0.1093 | 0.923633 | 0.349532 |
| bonus_part_correctness | category | Fine Arts | 2970 | 0.0290802 | 0.139481 | 0.882436 | 0.431738 |
| bonus_part_correctness | category | Geography | 501 | 0.0373396 | 0.132142 | 0.891807 | 0.413562 |
| bonus_part_correctness | category | History | 4068 | 0.0166187 | 0.128031 | 0.899093 | 0.400055 |
| bonus_part_correctness | category | Literature | 4065 | 0.0226155 | 0.124247 | 0.90202 | 0.394152 |
| bonus_part_correctness | category | Mythology | 945 | 0.0379051 | 0.148109 | 0.862655 | 0.449856 |
| bonus_part_correctness | category | Other Academic | 219 | 0.0749981 | 0.146984 | 0.877377 | 0.452699 |
| bonus_part_correctness | category | Philosophy | 963 | 0.0385185 | 0.133352 | 0.888377 | 0.424602 |
| bonus_part_correctness | category | Popular Culture | 288 | 0.0850446 | 0.15176 | 0.860751 | 0.455609 |
| bonus_part_correctness | category | Religion | 1008 | 0.0348324 | 0.12618 | 0.90111 | 0.400651 |
| bonus_part_correctness | category | Science | 4059 | 0.025052 | 0.127859 | 0.898262 | 0.406367 |
| bonus_part_correctness | category | Social Science | 909 | 0.0322162 | 0.108936 | 0.923412 | 0.345297 |
| bonus_part_correctness | category | Unknown | 5580 | 0.019485 | 0.129621 | 0.896156 | 0.404776 |
| bonus_part_correctness | difficulty | easy | 8597 | 0.0297471 | 0.078691 | 0.815947 | 0.266607 |
| bonus_part_correctness | difficulty | hard | 8597 | 0.0340582 | 0.116158 | 0.773172 | 0.381583 |
| bonus_part_correctness | difficulty | medium | 8597 | 0.0204581 | 0.193975 | 0.773317 | 0.571397 |
