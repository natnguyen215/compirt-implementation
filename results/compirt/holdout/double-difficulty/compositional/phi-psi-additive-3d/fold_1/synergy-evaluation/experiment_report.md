# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 16.8128 |
| tournament_team_bonus_ppg_spearman | 0.927203 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 462 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 25.9984 |
| bonus_game_margin_mae_games | 462 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.89933 |
| log_loss | 0.402107 |
| ece | 0.0182379 |
| brier | 0.127602 |
| part_accuracy | 0.818171 |
| part_accuracy_easy | 0.9038 |
| part_accuracy_medium | 0.707363 |
| part_accuracy_hard | 0.843349 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.519002 |
| accuracy_lift_over_all_correct | 0.299169 |
| part_accuracy_macro_team | 0.820889 |
| part_accuracy_macro_bonus | 0.815716 |
| part_count_easy | 8420 |
| part_count_medium | 8420 |
| part_count_hard | 8420 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.352901 |
| probability_p10 | 0.0517347 |
| probability_p50 | 0.542288 |
| probability_p90 | 0.965546 |
| mean_predictive_variance | 0.124741 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.533135 |
| ranked_probability_score | 0.109496 |
| bonus_total_score_log_loss | 0.971693 |
| ppb_mae | 1.82465 |
| ranked_probability_score_responses | 8420 |
| bonus_total_score_log_loss_responses | 8420 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 8 | 9 | 18.7687 | 0.862291 | 26.6605 |
| 2024-acf-fall-at-cornell | 17 | 18 | 11.3112 | 0.948406 | 24.9661 |
| 2024-acf-fall-at-georgia | 21 | 23 | 14.6904 | 0.952567 | 23.89 |
| 2024-acf-fall-at-illinois | 17 | 19 | 17.2118 | 0.880695 | 23.0153 |
| 2024-acf-fall-at-north-carolina | 18 | 22 | 16.8451 | 0.964378 | 29.5919 |
| 2024-acf-fall-at-ohio-state | 18 | 20 | 8.72122 | 0.975207 | 22.5948 |
| 2024-acf-fall-at-rutgers | 15 | 19 | 12.8413 | 0.957143 | 20.1469 |
| 2024-acf-fall-at-washington | 12 | 13 | 13.0526 | 0.921192 | 23.0068 |
| 2024-acf-nationals | 48 | 80 | 12.678 | 0.961473 | 24.2921 |
| 2024-acf-regionals-berkeley | 6 | 7 | 13.0225 | 0.942857 | 20.1515 |
| 2024-acf-regionals-cornell | 6 | 6 | 30.7356 | 0.6 | 47.2046 |
| 2024-acf-regionals-imperial | 15 | 18 | 14.4914 | 0.907143 | 27.7377 |
| 2024-acf-regionals-jmu | 19 | 23 | 12.2806 | 0.980255 | 21.1124 |
| 2024-acf-regionals-minnesota | 3 | 4 | 12.4664 | 1 | 18.0624 |
| 2024-acf-regionals-mit | 7 | 4 | 22.0183 | 1 | 29.6275 |
| 2024-acf-regionals-nebraska | 11 | 13 | 24.2273 | 0.897497 | 41.182 |
| 2024-acf-regionals-ohio-state | 7 | 5 | 18.1106 | 0.964286 | 18.8956 |
| 2024-acf-regionals-rutgers | 10 | 11 | 15.8848 | 0.975758 | 27.6238 |
| 2024-acf-regionals-vanderbilt | 10 | 9 | 26.4747 | 0.963636 | 43.2129 |
| 2024-acf-winter-at-brandeis | 16 | 16 | 16.494 | 0.947756 | 21.8137 |
| 2024-acf-winter-at-central-florida | 9 | 10 | 16.2111 | 0.983333 | 11.9831 |
| 2024-acf-winter-at-clemson | 15 | 17 | 14.2085 | 0.959786 | 29.5632 |
| 2024-acf-winter-at-lehigh | 13 | 12 | 13.1547 | 0.976617 | 20.6918 |
| 2024-acf-winter-at-northwestern | 17 | 18 | 14.6176 | 0.970588 | 21.4419 |
| 2024-acf-winter-at-ohio-state | 16 | 16 | 16.9862 | 0.915256 | 30.3459 |
| 2024-acf-winter-at-online | 15 | 20 | 17.4867 | 0.917857 | 29.0683 |
| 2024-acf-winter-at-oxford | 17 | 19 | 14.4572 | 0.925154 | 30.3561 |
| 2024-acf-winter-at-ubc | 6 | 6 | 13.8199 | 1 | 14.3449 |
| 2024-acf-winter-at-uc-berkeley | 6 | 5 | 34.3042 | 0.637748 | 69.8108 |

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
| bonus_part_correctness | aggregate | all | 25260 | 0.0182379 | 0.127602 | 0.89933 | 0.402107 |
| bonus_part_correctness | tier | fall | 8160 | 0.0158127 | 0.128262 | 0.893974 | 0.4023 |
| bonus_part_correctness | tier | nationals | 4107 | 0.0330715 | 0.123577 | 0.901937 | 0.393783 |
| bonus_part_correctness | tier | regionals | 5280 | 0.0253581 | 0.132056 | 0.892791 | 0.413264 |
| bonus_part_correctness | tier | winter | 7713 | 0.0250538 | 0.125999 | 0.900905 | 0.398698 |
| bonus_part_correctness | category | Current Events | 249 | 0.051031 | 0.125199 | 0.901278 | 0.404815 |
| bonus_part_correctness | category | Fine Arts | 2934 | 0.0273065 | 0.137113 | 0.884553 | 0.428831 |
| bonus_part_correctness | category | Geography | 459 | 0.0365752 | 0.137562 | 0.877384 | 0.427102 |
| bonus_part_correctness | category | History | 4017 | 0.0217302 | 0.124148 | 0.904637 | 0.390072 |
| bonus_part_correctness | category | Literature | 4047 | 0.0179908 | 0.120925 | 0.907469 | 0.386257 |
| bonus_part_correctness | category | Mythology | 924 | 0.0401109 | 0.142459 | 0.872005 | 0.439206 |
| bonus_part_correctness | category | Other Academic | 237 | 0.0810379 | 0.117651 | 0.919127 | 0.378584 |
| bonus_part_correctness | category | Philosophy | 948 | 0.0295111 | 0.127171 | 0.898478 | 0.403029 |
| bonus_part_correctness | category | Popular Culture | 294 | 0.0447967 | 0.13611 | 0.875473 | 0.417918 |
| bonus_part_correctness | category | Religion | 984 | 0.0247843 | 0.123963 | 0.904024 | 0.395512 |
| bonus_part_correctness | category | Science | 3990 | 0.020712 | 0.125434 | 0.902515 | 0.39632 |
| bonus_part_correctness | category | Social Science | 897 | 0.0309997 | 0.110078 | 0.920683 | 0.355708 |
| bonus_part_correctness | category | Unknown | 5280 | 0.0253581 | 0.132056 | 0.892791 | 0.413264 |
| bonus_part_correctness | difficulty | easy | 8420 | 0.0163414 | 0.0744026 | 0.804777 | 0.258486 |
| bonus_part_correctness | difficulty | hard | 8420 | 0.0274765 | 0.116133 | 0.778982 | 0.378074 |
| bonus_part_correctness | difficulty | medium | 8420 | 0.0416088 | 0.192271 | 0.780323 | 0.569761 |
