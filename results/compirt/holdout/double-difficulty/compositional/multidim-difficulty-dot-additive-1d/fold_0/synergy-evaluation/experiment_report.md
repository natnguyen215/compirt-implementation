# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 16.1546 |
| tournament_team_bonus_ppg_spearman | 0.876142 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 471 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 25.4274 |
| bonus_game_margin_mae_games | 471 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.899236 |
| log_loss | 0.401861 |
| ece | 0.0113664 |
| brier | 0.127766 |
| part_accuracy | 0.818692 |
| part_accuracy_easy | 0.899605 |
| part_accuracy_medium | 0.708343 |
| part_accuracy_hard | 0.848129 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.518437 |
| accuracy_lift_over_all_correct | 0.300256 |
| part_accuracy_macro_team | 0.818985 |
| part_accuracy_macro_bonus | 0.817135 |
| part_count_easy | 8606 |
| part_count_medium | 8606 |
| part_count_hard | 8606 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.351496 |
| probability_p10 | 0.0491761 |
| probability_p50 | 0.507405 |
| probability_p90 | 0.984481 |
| mean_predictive_variance | 0.125985 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.533697 |
| ranked_probability_score | 0.110712 |
| bonus_total_score_log_loss | 0.981651 |
| ppb_mae | 1.74028 |
| ranked_probability_score_responses | 8606 |
| bonus_total_score_log_loss_responses | 8606 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 9 | 9 | 14.4392 | 0.928878 | 39.0683 |
| 2024-acf-fall-at-cornell | 17 | 18 | 16.8752 | 0.9227 | 26.1324 |
| 2024-acf-fall-at-georgia | 24 | 25 | 13.0061 | 0.946453 | 27.741 |
| 2024-acf-fall-at-illinois | 19 | 22 | 17.9177 | 0.950792 | 28.1054 |
| 2024-acf-fall-at-north-carolina | 17 | 22 | 14.5657 | 0.941105 | 24.8422 |
| 2024-acf-fall-at-ohio-state | 16 | 20 | 13.0492 | 0.972019 | 18.9986 |
| 2024-acf-fall-at-rutgers | 17 | 19 | 16.9661 | 0.870632 | 28.7994 |
| 2024-acf-fall-at-washington | 14 | 13 | 17.027 | 0.867844 | 17.7655 |
| 2024-acf-nationals | 46 | 81 | 10.8146 | 0.916983 | 23.8896 |
| 2024-acf-regionals-berkeley | 5 | 6 | 13.2649 | 0.9 | 29.2089 |
| 2024-acf-regionals-cornell | 6 | 6 | 24.6468 | 0.637748 | 33.5477 |
| 2024-acf-regionals-imperial | 14 | 18 | 14.8436 | 0.866887 | 29.4532 |
| 2024-acf-regionals-jmu | 18 | 23 | 11.7897 | 0.920852 | 23.9706 |
| 2024-acf-regionals-minnesota | 3 | 4 | 7.87793 | 1 | 16.7851 |
| 2024-acf-regionals-mit | 5 | 3 | 23.9941 | 0.5 | 36.0031 |
| 2024-acf-regionals-nebraska | 12 | 14 | 16.8482 | 0.928198 | 23.6348 |
| 2024-acf-regionals-ohio-state | 7 | 5 | 16.8253 | 0.964286 | 11.5638 |
| 2024-acf-regionals-rutgers | 11 | 12 | 14.7018 | 0.902052 | 29.4202 |
| 2024-acf-regionals-vanderbilt | 6 | 5 | 27.2291 | 0.782691 | 37.3706 |
| 2024-acf-winter-at-brandeis | 16 | 17 | 16.6143 | 0.955882 | 23.6092 |
| 2024-acf-winter-at-central-florida | 11 | 9 | 12.1581 | 0.977179 | 28.9935 |
| 2024-acf-winter-at-clemson | 16 | 17 | 14.2933 | 0.932353 | 22.4886 |
| 2024-acf-winter-at-lehigh | 14 | 12 | 15.0421 | 0.947139 | 17.5704 |
| 2024-acf-winter-at-northwestern | 20 | 21 | 9.90614 | 0.970535 | 25.152 |
| 2024-acf-winter-at-ohio-state | 17 | 18 | 13.4475 | 0.965645 | 20.1079 |
| 2024-acf-winter-at-online | 16 | 19 | 16.9904 | 0.933727 | 24.7251 |
| 2024-acf-winter-at-oxford | 19 | 21 | 15.32 | 0.934096 | 27.1866 |
| 2024-acf-winter-at-ubc | 5 | 6 | 14.3111 | 0.7 | 27.3946 |
| 2024-acf-winter-at-uc-berkeley | 6 | 6 | 33.7171 | 0.371429 | 48.3887 |

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
| bonus_part_correctness | aggregate | all | 25818 | 0.0113664 | 0.127766 | 0.899236 | 0.401861 |
| bonus_part_correctness | tier | fall | 8415 | 0.0151631 | 0.129697 | 0.893546 | 0.402098 |
| bonus_part_correctness | tier | nationals | 4179 | 0.0242214 | 0.124875 | 0.898415 | 0.398666 |
| bonus_part_correctness | tier | regionals | 5070 | 0.013689 | 0.127602 | 0.899432 | 0.400407 |
| bonus_part_correctness | tier | winter | 8154 | 0.0196331 | 0.127358 | 0.898939 | 0.404158 |
| bonus_part_correctness | category | Current Events | 258 | 0.0387333 | 0.104226 | 0.930529 | 0.346292 |
| bonus_part_correctness | category | Fine Arts | 3075 | 0.0155462 | 0.134991 | 0.888239 | 0.42286 |
| bonus_part_correctness | category | Geography | 453 | 0.0356533 | 0.130028 | 0.890539 | 0.413291 |
| bonus_part_correctness | category | History | 4176 | 0.017394 | 0.127648 | 0.898784 | 0.401866 |
| bonus_part_correctness | category | Literature | 4197 | 0.0202749 | 0.118891 | 0.912243 | 0.373867 |
| bonus_part_correctness | category | Mythology | 951 | 0.0292208 | 0.134806 | 0.883796 | 0.418885 |
| bonus_part_correctness | category | Other Academic | 258 | 0.0808353 | 0.111889 | 0.924829 | 0.356601 |
| bonus_part_correctness | category | Philosophy | 969 | 0.0309654 | 0.134599 | 0.886729 | 0.424622 |
| bonus_part_correctness | category | Popular Culture | 303 | 0.0596967 | 0.149512 | 0.86198 | 0.435453 |
| bonus_part_correctness | category | Religion | 1041 | 0.0300603 | 0.127768 | 0.89943 | 0.40428 |
| bonus_part_correctness | category | Science | 4152 | 0.018165 | 0.128873 | 0.896842 | 0.406926 |
| bonus_part_correctness | category | Social Science | 915 | 0.0317745 | 0.128864 | 0.896879 | 0.411836 |
| bonus_part_correctness | category | Unknown | 5070 | 0.013689 | 0.127602 | 0.899432 | 0.400407 |
| bonus_part_correctness | difficulty | easy | 8606 | 0.0240471 | 0.0756298 | 0.816545 | 0.261073 |
| bonus_part_correctness | difficulty | hard | 8606 | 0.0332506 | 0.113768 | 0.787689 | 0.371851 |
| bonus_part_correctness | difficulty | medium | 8606 | 0.0224564 | 0.193901 | 0.774042 | 0.572658 |
