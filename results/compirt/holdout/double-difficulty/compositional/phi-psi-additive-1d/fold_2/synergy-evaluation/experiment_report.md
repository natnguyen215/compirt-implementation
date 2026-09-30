# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 16.2674 |
| tournament_team_bonus_ppg_spearman | 0.887254 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 469 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 27.3201 |
| bonus_game_margin_mae_games | 469 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.895538 |
| log_loss | 0.409486 |
| ece | 0.0161427 |
| brier | 0.129935 |
| part_accuracy | 0.813966 |
| part_accuracy_easy | 0.900547 |
| part_accuracy_medium | 0.699779 |
| part_accuracy_hard | 0.841573 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.519367 |
| accuracy_lift_over_all_correct | 0.294599 |
| part_accuracy_macro_team | 0.817161 |
| part_accuracy_macro_bonus | 0.81142 |
| part_count_easy | 8597 |
| part_count_medium | 8597 |
| part_count_hard | 8597 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.352007 |
| probability_p10 | 0.0503888 |
| probability_p50 | 0.530818 |
| probability_p90 | 0.96418 |
| mean_predictive_variance | 0.125636 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.525532 |
| ranked_probability_score | 0.111676 |
| bonus_total_score_log_loss | 0.992764 |
| ppb_mae | 1.69763 |
| ranked_probability_score_responses | 8597 |
| bonus_total_score_log_loss_responses | 8597 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 8 | 9 | 14.1967 | 0.97619 | 28.5865 |
| 2024-acf-fall-at-cornell | 17 | 18 | 17.0372 | 0.91043 | 26.3754 |
| 2024-acf-fall-at-georgia | 22 | 24 | 11.8533 | 0.948531 | 22.8704 |
| 2024-acf-fall-at-illinois | 19 | 21 | 11.0993 | 0.980702 | 22.4 |
| 2024-acf-fall-at-north-carolina | 18 | 22 | 14.344 | 0.936017 | 24.1441 |
| 2024-acf-fall-at-ohio-state | 18 | 19 | 17.8874 | 0.971606 | 29.5869 |
| 2024-acf-fall-at-rutgers | 16 | 16 | 15.2979 | 0.966128 | 24.983 |
| 2024-acf-fall-at-washington | 13 | 12 | 22.8617 | 0.901099 | 27.6734 |
| 2024-acf-nationals | 47 | 79 | 10.8357 | 0.962987 | 24.9637 |
| 2024-acf-regionals-berkeley | 5 | 6 | 7.17911 | 0.872082 | 11.2646 |
| 2024-acf-regionals-cornell | 4 | 7 | 24.0285 | 0.4 | 36.2915 |
| 2024-acf-regionals-imperial | 15 | 18 | 13.676 | 0.954424 | 22.4772 |
| 2024-acf-regionals-jmu | 18 | 24 | 9.60144 | 0.926653 | 20.997 |
| 2024-acf-regionals-minnesota | 4 | 4 | 30.0608 | 0.4 | 56.7105 |
| 2024-acf-regionals-mit | 6 | 4 | 24.5675 | 0.942857 | 33.4553 |
| 2024-acf-regionals-nebraska | 12 | 13 | 10.945 | 0.980737 | 24.3282 |
| 2024-acf-regionals-ohio-state | 6 | 6 | 10.2315 | 0.828571 | 12.459 |
| 2024-acf-regionals-rutgers | 11 | 11 | 20.3218 | 0.954545 | 34.7723 |
| 2024-acf-regionals-vanderbilt | 10 | 11 | 18.2778 | 0.939394 | 41.7352 |
| 2024-acf-winter-at-brandeis | 20 | 18 | 19.93 | 0.928169 | 28.3744 |
| 2024-acf-winter-at-central-florida | 9 | 10 | 14.0769 | 1 | 19.8563 |
| 2024-acf-winter-at-clemson | 18 | 17 | 13.6407 | 0.946281 | 30.8958 |
| 2024-acf-winter-at-lehigh | 14 | 14 | 9.56033 | 0.980179 | 23.8266 |
| 2024-acf-winter-at-northwestern | 20 | 21 | 15.3165 | 0.947725 | 25.1174 |
| 2024-acf-winter-at-ohio-state | 16 | 16 | 20.4102 | 0.924891 | 35.3979 |
| 2024-acf-winter-at-online | 18 | 19 | 17.9764 | 0.905057 | 38.8614 |
| 2024-acf-winter-at-oxford | 17 | 18 | 19.3668 | 0.787957 | 38.2037 |
| 2024-acf-winter-at-ubc | 5 | 6 | 9.92043 | 0.9 | 18.5385 |
| 2024-acf-winter-at-uc-berkeley | 6 | 6 | 27.2543 | 0.657143 | 40.3224 |

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
| bonus_part_correctness | aggregate | all | 25791 | 0.0161427 | 0.129935 | 0.895538 | 0.409486 |
| bonus_part_correctness | tier | fall | 7995 | 0.0195429 | 0.125708 | 0.900347 | 0.392229 |
| bonus_part_correctness | tier | nationals | 4095 | 0.0168619 | 0.128259 | 0.894555 | 0.405307 |
| bonus_part_correctness | tier | regionals | 5580 | 0.016085 | 0.130712 | 0.894205 | 0.410352 |
| bonus_part_correctness | tier | winter | 8121 | 0.0251351 | 0.134408 | 0.887958 | 0.427986 |
| bonus_part_correctness | category | Current Events | 216 | 0.0673892 | 0.112946 | 0.919931 | 0.363588 |
| bonus_part_correctness | category | Fine Arts | 2970 | 0.0309991 | 0.139955 | 0.882724 | 0.433678 |
| bonus_part_correctness | category | Geography | 501 | 0.053869 | 0.130453 | 0.896561 | 0.410813 |
| bonus_part_correctness | category | History | 4068 | 0.0160189 | 0.127399 | 0.89872 | 0.403211 |
| bonus_part_correctness | category | Literature | 4065 | 0.0239528 | 0.123732 | 0.903495 | 0.39253 |
| bonus_part_correctness | category | Mythology | 945 | 0.0527235 | 0.150512 | 0.860778 | 0.458548 |
| bonus_part_correctness | category | Other Academic | 219 | 0.0891964 | 0.145927 | 0.879296 | 0.451259 |
| bonus_part_correctness | category | Philosophy | 963 | 0.0210372 | 0.133318 | 0.88852 | 0.423886 |
| bonus_part_correctness | category | Popular Culture | 288 | 0.066622 | 0.153191 | 0.858642 | 0.466944 |
| bonus_part_correctness | category | Religion | 1008 | 0.0235469 | 0.127447 | 0.899055 | 0.403166 |
| bonus_part_correctness | category | Science | 4059 | 0.0228348 | 0.128068 | 0.896002 | 0.409644 |
| bonus_part_correctness | category | Social Science | 909 | 0.0392035 | 0.110166 | 0.923627 | 0.350978 |
| bonus_part_correctness | category | Unknown | 5580 | 0.016085 | 0.130712 | 0.894205 | 0.410352 |
| bonus_part_correctness | difficulty | easy | 8597 | 0.0226231 | 0.0769172 | 0.804622 | 0.264697 |
| bonus_part_correctness | difficulty | hard | 8597 | 0.0333886 | 0.117091 | 0.7688 | 0.38483 |
| bonus_part_correctness | difficulty | medium | 8597 | 0.0316644 | 0.195798 | 0.771433 | 0.57893 |
