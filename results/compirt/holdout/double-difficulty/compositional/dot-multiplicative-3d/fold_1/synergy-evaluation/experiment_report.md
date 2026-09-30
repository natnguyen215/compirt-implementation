# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 21.945 |
| tournament_team_bonus_ppg_spearman | 0.878676 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 462 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 33.6982 |
| bonus_game_margin_mae_games | 462 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.891132 |
| log_loss | 0.41708 |
| ece | 0.0178111 |
| brier | 0.133046 |
| part_accuracy | 0.809541 |
| part_accuracy_easy | 0.901544 |
| part_accuracy_medium | 0.68943 |
| part_accuracy_hard | 0.837648 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.519002 |
| accuracy_lift_over_all_correct | 0.290538 |
| part_accuracy_macro_team | 0.812938 |
| part_accuracy_macro_bonus | 0.806549 |
| part_count_easy | 8420 |
| part_count_medium | 8420 |
| part_count_hard | 8420 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.351399 |
| probability_p10 | 0.0510679 |
| probability_p50 | 0.53029 |
| probability_p90 | 0.968932 |
| mean_predictive_variance | 0.125945 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.517577 |
| ranked_probability_score | 0.115153 |
| bonus_total_score_log_loss | 1.01246 |
| ppb_mae | 2.38561 |
| ranked_probability_score_responses | 8420 |
| bonus_total_score_log_loss_responses | 8420 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 8 | 9 | 15.5952 | 0.862291 | 32.2392 |
| 2024-acf-fall-at-cornell | 17 | 18 | 20.2569 | 0.796071 | 34.7419 |
| 2024-acf-fall-at-georgia | 21 | 23 | 16.8104 | 0.922027 | 26.9032 |
| 2024-acf-fall-at-illinois | 17 | 19 | 23.636 | 0.881925 | 35.0999 |
| 2024-acf-fall-at-north-carolina | 18 | 22 | 16.1803 | 0.971606 | 27.6565 |
| 2024-acf-fall-at-ohio-state | 18 | 20 | 18.042 | 0.889463 | 40.0369 |
| 2024-acf-fall-at-rutgers | 15 | 19 | 19.2591 | 0.932143 | 31.9663 |
| 2024-acf-fall-at-washington | 12 | 13 | 20.5725 | 0.725045 | 33.1458 |
| 2024-acf-nationals | 48 | 80 | 18.853 | 0.897939 | 32.7255 |
| 2024-acf-regionals-berkeley | 6 | 7 | 27.6541 | 0.942857 | 34.9354 |
| 2024-acf-regionals-cornell | 6 | 6 | 33.1444 | 0.6 | 51.0153 |
| 2024-acf-regionals-imperial | 15 | 18 | 22.3208 | 0.882143 | 45.4421 |
| 2024-acf-regionals-jmu | 19 | 23 | 24.8239 | 0.960948 | 32.7571 |
| 2024-acf-regionals-minnesota | 3 | 4 | 27.3709 | 0.5 | 28.8312 |
| 2024-acf-regionals-mit | 7 | 4 | 23.4648 | 1 | 36.7288 |
| 2024-acf-regionals-nebraska | 11 | 13 | 20.1177 | 0.883829 | 38.9711 |
| 2024-acf-regionals-ohio-state | 7 | 5 | 26.1244 | 0.964286 | 30.1251 |
| 2024-acf-regionals-rutgers | 10 | 11 | 23.8476 | 0.975758 | 43.1645 |
| 2024-acf-regionals-vanderbilt | 10 | 9 | 28.2613 | 0.951515 | 46.3669 |
| 2024-acf-winter-at-brandeis | 16 | 16 | 20.5221 | 0.927153 | 19.8366 |
| 2024-acf-winter-at-central-florida | 9 | 10 | 24.1423 | 0.966667 | 20.1092 |
| 2024-acf-winter-at-clemson | 15 | 17 | 17.4944 | 0.949062 | 33.2588 |
| 2024-acf-winter-at-lehigh | 13 | 12 | 16.4927 | 0.973866 | 39.5014 |
| 2024-acf-winter-at-northwestern | 17 | 18 | 19.3364 | 0.894608 | 31.2023 |
| 2024-acf-winter-at-ohio-state | 16 | 16 | 17.4791 | 0.910835 | 33.0948 |
| 2024-acf-winter-at-online | 15 | 20 | 21.0914 | 0.9 | 33.8914 |
| 2024-acf-winter-at-oxford | 17 | 19 | 18.3328 | 0.896933 | 31.3433 |
| 2024-acf-winter-at-ubc | 6 | 6 | 24.3846 | 0.942857 | 28.3321 |
| 2024-acf-winter-at-uc-berkeley | 6 | 5 | 30.7939 | 0.579771 | 55.1842 |

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
| bonus_part_correctness | aggregate | all | 25260 | 0.0178111 | 0.133046 | 0.891132 | 0.41708 |
| bonus_part_correctness | tier | fall | 8160 | 0.0137829 | 0.132544 | 0.887093 | 0.413912 |
| bonus_part_correctness | tier | nationals | 4107 | 0.0295975 | 0.130121 | 0.892162 | 0.410876 |
| bonus_part_correctness | tier | regionals | 5280 | 0.0331047 | 0.140697 | 0.880692 | 0.435937 |
| bonus_part_correctness | tier | winter | 7713 | 0.027019 | 0.129898 | 0.893963 | 0.410825 |
| bonus_part_correctness | category | Current Events | 249 | 0.0398834 | 0.120572 | 0.90328 | 0.389301 |
| bonus_part_correctness | category | Fine Arts | 2934 | 0.0229823 | 0.142099 | 0.876564 | 0.442448 |
| bonus_part_correctness | category | Geography | 459 | 0.0472267 | 0.135754 | 0.87672 | 0.428351 |
| bonus_part_correctness | category | History | 4017 | 0.0216145 | 0.128001 | 0.898669 | 0.400775 |
| bonus_part_correctness | category | Literature | 4047 | 0.0247003 | 0.126008 | 0.899633 | 0.403218 |
| bonus_part_correctness | category | Mythology | 924 | 0.0423229 | 0.142975 | 0.869209 | 0.440417 |
| bonus_part_correctness | category | Other Academic | 237 | 0.0605645 | 0.112666 | 0.930039 | 0.354714 |
| bonus_part_correctness | category | Philosophy | 948 | 0.0342181 | 0.135877 | 0.885529 | 0.427197 |
| bonus_part_correctness | category | Popular Culture | 294 | 0.0608148 | 0.132363 | 0.884312 | 0.405178 |
| bonus_part_correctness | category | Religion | 984 | 0.018866 | 0.12623 | 0.898621 | 0.4065 |
| bonus_part_correctness | category | Science | 3990 | 0.0202334 | 0.132562 | 0.892242 | 0.413429 |
| bonus_part_correctness | category | Social Science | 897 | 0.03446 | 0.116856 | 0.911796 | 0.374092 |
| bonus_part_correctness | category | Unknown | 5280 | 0.0331047 | 0.140697 | 0.880692 | 0.435937 |
| bonus_part_correctness | difficulty | easy | 8420 | 0.0187745 | 0.0776433 | 0.779021 | 0.271093 |
| bonus_part_correctness | difficulty | hard | 8420 | 0.0309807 | 0.120045 | 0.760856 | 0.388703 |
| bonus_part_correctness | difficulty | medium | 8420 | 0.0460589 | 0.201451 | 0.758484 | 0.591443 |
