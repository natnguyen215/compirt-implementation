# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 21.8872 |
| tournament_team_bonus_ppg_spearman | 0.879663 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 462 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 33.386 |
| bonus_game_margin_mae_games | 462 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.891344 |
| log_loss | 0.415845 |
| ece | 0.0178697 |
| brier | 0.132855 |
| part_accuracy | 0.811085 |
| part_accuracy_easy | 0.9038 |
| part_accuracy_medium | 0.69133 |
| part_accuracy_hard | 0.838124 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.519002 |
| accuracy_lift_over_all_correct | 0.292082 |
| part_accuracy_macro_team | 0.814697 |
| part_accuracy_macro_bonus | 0.807711 |
| part_count_easy | 8420 |
| part_count_medium | 8420 |
| part_count_hard | 8420 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.345195 |
| probability_p10 | 0.0569429 |
| probability_p50 | 0.529115 |
| probability_p90 | 0.959424 |
| mean_predictive_variance | 0.130331 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.520665 |
| ranked_probability_score | 0.115119 |
| bonus_total_score_log_loss | 1.00945 |
| ppb_mae | 2.39054 |
| ranked_probability_score_responses | 8420 |
| bonus_total_score_log_loss_responses | 8420 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 8 | 9 | 13.3408 | 0.934148 | 29.8191 |
| 2024-acf-fall-at-cornell | 17 | 18 | 19.4684 | 0.796071 | 32.987 |
| 2024-acf-fall-at-georgia | 21 | 23 | 17.1779 | 0.927226 | 26.6603 |
| 2024-acf-fall-at-illinois | 17 | 19 | 23.7882 | 0.881925 | 34.4152 |
| 2024-acf-fall-at-north-carolina | 18 | 22 | 16.5202 | 0.968508 | 27.8406 |
| 2024-acf-fall-at-ohio-state | 18 | 20 | 18.776 | 0.889463 | 40.6385 |
| 2024-acf-fall-at-rutgers | 15 | 19 | 19.2167 | 0.932143 | 30.9708 |
| 2024-acf-fall-at-washington | 12 | 13 | 20.2669 | 0.725045 | 32.7961 |
| 2024-acf-nationals | 48 | 80 | 18.9866 | 0.896745 | 32.6872 |
| 2024-acf-regionals-berkeley | 6 | 7 | 27.9957 | 0.942857 | 35.0425 |
| 2024-acf-regionals-cornell | 6 | 6 | 32.8331 | 0.6 | 50.6558 |
| 2024-acf-regionals-imperial | 15 | 18 | 21.7834 | 0.882143 | 44.3688 |
| 2024-acf-regionals-jmu | 19 | 23 | 24.5978 | 0.960948 | 32.2494 |
| 2024-acf-regionals-minnesota | 3 | 4 | 27.847 | 0.5 | 28.8712 |
| 2024-acf-regionals-mit | 7 | 4 | 24.978 | 1 | 37.4622 |
| 2024-acf-regionals-nebraska | 11 | 13 | 20.3378 | 0.883829 | 38.8721 |
| 2024-acf-regionals-ohio-state | 7 | 5 | 25.591 | 0.964286 | 29.4117 |
| 2024-acf-regionals-rutgers | 10 | 11 | 23.6188 | 0.975758 | 43.2246 |
| 2024-acf-regionals-vanderbilt | 10 | 9 | 28.2404 | 0.951515 | 45.5149 |
| 2024-acf-winter-at-brandeis | 16 | 16 | 21.0073 | 0.927153 | 19.9921 |
| 2024-acf-winter-at-central-florida | 9 | 10 | 24.3513 | 0.95 | 18.6631 |
| 2024-acf-winter-at-clemson | 15 | 17 | 17.51 | 0.949062 | 33.2105 |
| 2024-acf-winter-at-lehigh | 13 | 12 | 16.4836 | 0.973866 | 40.6514 |
| 2024-acf-winter-at-northwestern | 17 | 18 | 18.6806 | 0.909314 | 29.4579 |
| 2024-acf-winter-at-ohio-state | 16 | 16 | 18.2164 | 0.910835 | 33.7039 |
| 2024-acf-winter-at-online | 15 | 20 | 22.014 | 0.875 | 35.0909 |
| 2024-acf-winter-at-oxford | 17 | 19 | 17.9143 | 0.879755 | 31.6102 |
| 2024-acf-winter-at-ubc | 6 | 6 | 22.3396 | 0.942857 | 24.8934 |
| 2024-acf-winter-at-uc-berkeley | 6 | 5 | 30.8469 | 0.579771 | 53.4908 |

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
| bonus_part_correctness | aggregate | all | 25260 | 0.0178697 | 0.132855 | 0.891344 | 0.415845 |
| bonus_part_correctness | tier | fall | 8160 | 0.0150946 | 0.132716 | 0.887147 | 0.412656 |
| bonus_part_correctness | tier | nationals | 4107 | 0.031072 | 0.130552 | 0.89106 | 0.412937 |
| bonus_part_correctness | tier | regionals | 5280 | 0.0314788 | 0.140244 | 0.880951 | 0.43392 |
| bonus_part_correctness | tier | winter | 7713 | 0.0252534 | 0.129169 | 0.894962 | 0.408393 |
| bonus_part_correctness | category | Current Events | 249 | 0.0542139 | 0.124813 | 0.898631 | 0.403338 |
| bonus_part_correctness | category | Fine Arts | 2934 | 0.0211972 | 0.140793 | 0.878555 | 0.438335 |
| bonus_part_correctness | category | Geography | 459 | 0.0489226 | 0.135599 | 0.879477 | 0.423786 |
| bonus_part_correctness | category | History | 4017 | 0.0222646 | 0.128399 | 0.898076 | 0.401882 |
| bonus_part_correctness | category | Literature | 4047 | 0.0203932 | 0.126331 | 0.899288 | 0.401013 |
| bonus_part_correctness | category | Mythology | 924 | 0.0372562 | 0.141373 | 0.872561 | 0.43512 |
| bonus_part_correctness | category | Other Academic | 237 | 0.0624212 | 0.114481 | 0.924191 | 0.369227 |
| bonus_part_correctness | category | Philosophy | 948 | 0.0338407 | 0.13616 | 0.88447 | 0.429202 |
| bonus_part_correctness | category | Popular Culture | 294 | 0.057901 | 0.130624 | 0.887258 | 0.402816 |
| bonus_part_correctness | category | Religion | 984 | 0.0270957 | 0.125939 | 0.899241 | 0.403428 |
| bonus_part_correctness | category | Science | 3990 | 0.0228557 | 0.132396 | 0.892331 | 0.413551 |
| bonus_part_correctness | category | Social Science | 897 | 0.0403935 | 0.116556 | 0.912547 | 0.371179 |
| bonus_part_correctness | category | Unknown | 5280 | 0.0314788 | 0.140244 | 0.880951 | 0.43392 |
| bonus_part_correctness | difficulty | easy | 8420 | 0.0240898 | 0.0771027 | 0.785194 | 0.268216 |
| bonus_part_correctness | difficulty | hard | 8420 | 0.0311395 | 0.120191 | 0.758009 | 0.389217 |
| bonus_part_correctness | difficulty | medium | 8420 | 0.0412022 | 0.201271 | 0.757932 | 0.590101 |
