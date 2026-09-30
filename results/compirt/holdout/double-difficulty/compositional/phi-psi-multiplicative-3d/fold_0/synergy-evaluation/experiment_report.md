# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 21.7259 |
| tournament_team_bonus_ppg_spearman | 0.794307 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 471 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 33.0209 |
| bonus_game_margin_mae_games | 471 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.890877 |
| log_loss | 0.417012 |
| ece | 0.0129306 |
| brier | 0.133335 |
| part_accuracy | 0.809048 |
| part_accuracy_easy | 0.903207 |
| part_accuracy_medium | 0.683128 |
| part_accuracy_hard | 0.840809 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.518437 |
| accuracy_lift_over_all_correct | 0.290611 |
| part_accuracy_macro_team | 0.809341 |
| part_accuracy_macro_bonus | 0.80652 |
| part_count_easy | 8606 |
| part_count_medium | 8606 |
| part_count_hard | 8606 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.343627 |
| probability_p10 | 0.05604 |
| probability_p50 | 0.526982 |
| probability_p90 | 0.958321 |
| mean_predictive_variance | 0.131438 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.510923 |
| ranked_probability_score | 0.117008 |
| bonus_total_score_log_loss | 1.02213 |
| ppb_mae | 2.34466 |
| ranked_probability_score_responses | 8606 |
| bonus_total_score_log_loss_responses | 8606 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 9 | 9 | 9.2204 | 0.97072 | 37.6927 |
| 2024-acf-fall-at-cornell | 17 | 18 | 24.5017 | 0.855215 | 33.3071 |
| 2024-acf-fall-at-georgia | 24 | 25 | 22.0222 | 0.910754 | 42.278 |
| 2024-acf-fall-at-illinois | 19 | 22 | 21.0641 | 0.905098 | 34.9025 |
| 2024-acf-fall-at-north-carolina | 17 | 22 | 16.2307 | 0.941105 | 25.8947 |
| 2024-acf-fall-at-ohio-state | 16 | 20 | 18.1998 | 0.913109 | 29.123 |
| 2024-acf-fall-at-rutgers | 17 | 19 | 19.7141 | 0.849786 | 36.361 |
| 2024-acf-fall-at-washington | 14 | 13 | 20.7583 | 0.845817 | 35.4216 |
| 2024-acf-nationals | 46 | 81 | 20.2232 | 0.809625 | 31.5289 |
| 2024-acf-regionals-berkeley | 5 | 6 | 34.4492 | 0.8 | 43.0427 |
| 2024-acf-regionals-cornell | 6 | 6 | 25.2228 | 0.579771 | 41.3824 |
| 2024-acf-regionals-imperial | 14 | 18 | 22.272 | 0.833884 | 39.5835 |
| 2024-acf-regionals-jmu | 18 | 23 | 19.4814 | 0.875326 | 28.5681 |
| 2024-acf-regionals-minnesota | 3 | 4 | 29.6425 | 1 | 46.3102 |
| 2024-acf-regionals-mit | 5 | 3 | 35.1815 | -1 | 41.4957 |
| 2024-acf-regionals-nebraska | 12 | 14 | 18.7666 | 0.928198 | 27.4628 |
| 2024-acf-regionals-ohio-state | 7 | 5 | 15.1939 | 0.964286 | 13.3708 |
| 2024-acf-regionals-rutgers | 11 | 12 | 23.4106 | 0.943055 | 34.5773 |
| 2024-acf-regionals-vanderbilt | 6 | 5 | 30.4832 | 0.782691 | 28.5715 |
| 2024-acf-winter-at-brandeis | 16 | 17 | 21.1964 | 0.952941 | 31.5417 |
| 2024-acf-winter-at-central-florida | 11 | 9 | 14.9129 | 0.940649 | 25.4488 |
| 2024-acf-winter-at-clemson | 16 | 17 | 18.0003 | 0.935294 | 30.542 |
| 2024-acf-winter-at-lehigh | 14 | 12 | 16.7845 | 0.949342 | 27.3931 |
| 2024-acf-winter-at-northwestern | 20 | 21 | 20.6146 | 0.941056 | 45.8073 |
| 2024-acf-winter-at-ohio-state | 17 | 18 | 18.3653 | 0.946013 | 23.7072 |
| 2024-acf-winter-at-online | 16 | 19 | 16.5151 | 0.891017 | 26.6374 |
| 2024-acf-winter-at-oxford | 19 | 21 | 15.5945 | 0.913007 | 28.8668 |
| 2024-acf-winter-at-ubc | 5 | 6 | 21.7424 | 0.6 | 39.4283 |
| 2024-acf-winter-at-uc-berkeley | 6 | 6 | 40.2872 | 0.257143 | 64.3734 |

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
| bonus_part_correctness | aggregate | all | 25818 | 0.0129306 | 0.133335 | 0.890877 | 0.417012 |
| bonus_part_correctness | tier | fall | 8415 | 0.0149411 | 0.13611 | 0.883441 | 0.419206 |
| bonus_part_correctness | tier | nationals | 4179 | 0.0361372 | 0.131975 | 0.889475 | 0.417166 |
| bonus_part_correctness | tier | regionals | 5070 | 0.0168747 | 0.133054 | 0.890843 | 0.417879 |
| bonus_part_correctness | tier | winter | 8154 | 0.017615 | 0.131343 | 0.892657 | 0.414131 |
| bonus_part_correctness | category | Current Events | 258 | 0.0599438 | 0.100475 | 0.932572 | 0.338821 |
| bonus_part_correctness | category | Fine Arts | 3075 | 0.0248165 | 0.142726 | 0.876008 | 0.443268 |
| bonus_part_correctness | category | Geography | 453 | 0.0428494 | 0.131844 | 0.889259 | 0.415933 |
| bonus_part_correctness | category | History | 4176 | 0.0208666 | 0.134824 | 0.889028 | 0.41736 |
| bonus_part_correctness | category | Literature | 4197 | 0.0231335 | 0.123208 | 0.906022 | 0.388727 |
| bonus_part_correctness | category | Mythology | 951 | 0.0325203 | 0.143705 | 0.868804 | 0.440977 |
| bonus_part_correctness | category | Other Academic | 258 | 0.0381887 | 0.121277 | 0.907651 | 0.39243 |
| bonus_part_correctness | category | Philosophy | 969 | 0.0283897 | 0.143941 | 0.87283 | 0.447947 |
| bonus_part_correctness | category | Popular Culture | 303 | 0.0679699 | 0.154272 | 0.85444 | 0.451382 |
| bonus_part_correctness | category | Religion | 1041 | 0.0421254 | 0.130838 | 0.894777 | 0.414504 |
| bonus_part_correctness | category | Science | 4152 | 0.0153062 | 0.132564 | 0.890612 | 0.416043 |
| bonus_part_correctness | category | Social Science | 915 | 0.0325149 | 0.133784 | 0.888788 | 0.419842 |
| bonus_part_correctness | category | Unknown | 5070 | 0.0168747 | 0.133054 | 0.890843 | 0.417879 |
| bonus_part_correctness | difficulty | easy | 8606 | 0.0240831 | 0.0775326 | 0.788919 | 0.270327 |
| bonus_part_correctness | difficulty | hard | 8606 | 0.0332295 | 0.118154 | 0.770112 | 0.382761 |
| bonus_part_correctness | difficulty | medium | 8606 | 0.0365067 | 0.204319 | 0.750415 | 0.597949 |
