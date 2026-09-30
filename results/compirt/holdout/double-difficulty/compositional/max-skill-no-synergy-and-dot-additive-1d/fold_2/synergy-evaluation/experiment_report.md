# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 15.9461 |
| tournament_team_bonus_ppg_spearman | 0.881749 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 469 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 27.2483 |
| bonus_game_margin_mae_games | 469 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.894587 |
| log_loss | 0.410589 |
| ece | 0.0157197 |
| brier | 0.130357 |
| part_accuracy | 0.814276 |
| part_accuracy_easy | 0.900081 |
| part_accuracy_medium | 0.698151 |
| part_accuracy_hard | 0.844597 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.519367 |
| accuracy_lift_over_all_correct | 0.294909 |
| part_accuracy_macro_team | 0.817405 |
| part_accuracy_macro_bonus | 0.812415 |
| part_count_easy | 8597 |
| part_count_medium | 8597 |
| part_count_hard | 8597 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.336262 |
| probability_p10 | 0.0713461 |
| probability_p50 | 0.512698 |
| probability_p90 | 0.950365 |
| mean_predictive_variance | 0.13668 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.522624 |
| ranked_probability_score | 0.111215 |
| bonus_total_score_log_loss | 0.984976 |
| ppb_mae | 1.69007 |
| ranked_probability_score_responses | 8597 |
| bonus_total_score_log_loss_responses | 8597 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 8 | 9 | 16.4568 | 0.97619 | 22.8594 |
| 2024-acf-fall-at-cornell | 17 | 18 | 15.9936 | 0.94724 | 28.7487 |
| 2024-acf-fall-at-georgia | 22 | 24 | 12.7024 | 0.9474 | 26.3904 |
| 2024-acf-fall-at-illinois | 19 | 21 | 12.2949 | 0.97193 | 24.4416 |
| 2024-acf-fall-at-north-carolina | 18 | 22 | 15.7991 | 0.956656 | 32.5966 |
| 2024-acf-fall-at-ohio-state | 18 | 19 | 17.432 | 0.970573 | 28.897 |
| 2024-acf-fall-at-rutgers | 16 | 16 | 17.4571 | 0.948455 | 27.501 |
| 2024-acf-fall-at-washington | 13 | 12 | 28.184 | 0.868132 | 25.2738 |
| 2024-acf-nationals | 47 | 79 | 12.1573 | 0.950726 | 25.4902 |
| 2024-acf-regionals-berkeley | 5 | 6 | 8.32272 | 0.872082 | 12.9168 |
| 2024-acf-regionals-cornell | 4 | 7 | 16.2314 | 0.4 | 29.3996 |
| 2024-acf-regionals-imperial | 15 | 18 | 12.2869 | 0.950849 | 18.0376 |
| 2024-acf-regionals-jmu | 18 | 24 | 10.7096 | 0.958678 | 21.8072 |
| 2024-acf-regionals-minnesota | 4 | 4 | 32.1989 | 0.4 | 49.9649 |
| 2024-acf-regionals-mit | 6 | 4 | 16.0575 | 0.942857 | 24.5427 |
| 2024-acf-regionals-nebraska | 12 | 13 | 12.1237 | 0.963224 | 26.6664 |
| 2024-acf-regionals-ohio-state | 6 | 6 | 13.9749 | 0.714286 | 22.4928 |
| 2024-acf-regionals-rutgers | 11 | 11 | 19.9043 | 0.954545 | 30.8075 |
| 2024-acf-regionals-vanderbilt | 10 | 11 | 15.2365 | 0.939394 | 30.3272 |
| 2024-acf-winter-at-brandeis | 20 | 18 | 19.2495 | 0.928921 | 30.2409 |
| 2024-acf-winter-at-central-florida | 9 | 10 | 12.5301 | 0.983333 | 13.8098 |
| 2024-acf-winter-at-clemson | 18 | 17 | 12.29 | 0.944215 | 27.0923 |
| 2024-acf-winter-at-lehigh | 14 | 14 | 12.399 | 0.907491 | 33.8882 |
| 2024-acf-winter-at-northwestern | 20 | 21 | 12.9644 | 0.954494 | 23.0893 |
| 2024-acf-winter-at-ohio-state | 16 | 16 | 16.5508 | 0.963182 | 27.9323 |
| 2024-acf-winter-at-online | 18 | 19 | 18.5046 | 0.900929 | 40.2713 |
| 2024-acf-winter-at-oxford | 17 | 18 | 19.6944 | 0.797791 | 36.793 |
| 2024-acf-winter-at-ubc | 5 | 6 | 7.20283 | 0.9 | 22.4416 |
| 2024-acf-winter-at-uc-berkeley | 6 | 6 | 25.5277 | 0.657143 | 31.935 |

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
| bonus_part_correctness | aggregate | all | 25791 | 0.0157197 | 0.130357 | 0.894587 | 0.410589 |
| bonus_part_correctness | tier | fall | 7995 | 0.026649 | 0.127094 | 0.898172 | 0.397054 |
| bonus_part_correctness | tier | nationals | 4095 | 0.0358629 | 0.131811 | 0.889644 | 0.418709 |
| bonus_part_correctness | tier | regionals | 5580 | 0.023813 | 0.130231 | 0.895408 | 0.410558 |
| bonus_part_correctness | tier | winter | 8121 | 0.0136314 | 0.132924 | 0.889826 | 0.419842 |
| bonus_part_correctness | category | Current Events | 216 | 0.076815 | 0.115696 | 0.917607 | 0.371293 |
| bonus_part_correctness | category | Fine Arts | 2970 | 0.0258984 | 0.139884 | 0.881085 | 0.434199 |
| bonus_part_correctness | category | Geography | 501 | 0.0461097 | 0.133479 | 0.886874 | 0.41983 |
| bonus_part_correctness | category | History | 4068 | 0.0226245 | 0.128797 | 0.897394 | 0.405251 |
| bonus_part_correctness | category | Literature | 4065 | 0.0267236 | 0.124177 | 0.902174 | 0.394144 |
| bonus_part_correctness | category | Mythology | 945 | 0.0474233 | 0.148835 | 0.861519 | 0.451425 |
| bonus_part_correctness | category | Other Academic | 219 | 0.0600781 | 0.141398 | 0.883383 | 0.434535 |
| bonus_part_correctness | category | Philosophy | 963 | 0.0320365 | 0.13377 | 0.88469 | 0.427128 |
| bonus_part_correctness | category | Popular Culture | 288 | 0.0830971 | 0.155662 | 0.856019 | 0.471614 |
| bonus_part_correctness | category | Religion | 1008 | 0.0236484 | 0.127667 | 0.899669 | 0.402002 |
| bonus_part_correctness | category | Science | 4059 | 0.0245345 | 0.129262 | 0.8945 | 0.411646 |
| bonus_part_correctness | category | Social Science | 909 | 0.0381089 | 0.110758 | 0.922106 | 0.355049 |
| bonus_part_correctness | category | Unknown | 5580 | 0.023813 | 0.130231 | 0.895408 | 0.410558 |
| bonus_part_correctness | difficulty | easy | 8597 | 0.0480413 | 0.07793 | 0.806872 | 0.271279 |
| bonus_part_correctness | difficulty | hard | 8597 | 0.0385411 | 0.117626 | 0.764335 | 0.384313 |
| bonus_part_correctness | difficulty | medium | 8597 | 0.0280181 | 0.195517 | 0.770608 | 0.576176 |
