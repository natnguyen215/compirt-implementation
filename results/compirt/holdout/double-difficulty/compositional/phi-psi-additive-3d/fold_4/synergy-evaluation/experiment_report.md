# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 16.0582 |
| tournament_team_bonus_ppg_spearman | 0.924218 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 469 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 26.8062 |
| bonus_game_margin_mae_games | 469 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.898352 |
| log_loss | 0.404232 |
| ece | 0.0169516 |
| brier | 0.128351 |
| part_accuracy | 0.817289 |
| part_accuracy_easy | 0.914753 |
| part_accuracy_medium | 0.692415 |
| part_accuracy_hard | 0.8447 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.525555 |
| accuracy_lift_over_all_correct | 0.291734 |
| part_accuracy_macro_team | 0.821403 |
| part_accuracy_macro_bonus | 0.814261 |
| part_count_easy | 8622 |
| part_count_medium | 8622 |
| part_count_hard | 8622 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.351899 |
| probability_p10 | 0.052283 |
| probability_p50 | 0.542972 |
| probability_p90 | 0.967008 |
| mean_predictive_variance | 0.12537 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.530271 |
| ranked_probability_score | 0.113221 |
| bonus_total_score_log_loss | 1.00276 |
| ppb_mae | 1.74226 |
| ranked_probability_score_responses | 8622 |
| bonus_total_score_log_loss_responses | 8622 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 9 | 8 | 13.3843 | 0.966667 | 20.5098 |
| 2024-acf-fall-at-cornell | 15 | 17 | 16.1185 | 0.92404 | 22.7696 |
| 2024-acf-fall-at-georgia | 24 | 26 | 12.6403 | 0.97715 | 26.8515 |
| 2024-acf-fall-at-illinois | 18 | 22 | 16.7855 | 0.987593 | 31.5946 |
| 2024-acf-fall-at-north-carolina | 18 | 22 | 18.6141 | 0.917904 | 28.338 |
| 2024-acf-fall-at-ohio-state | 17 | 18 | 13.0284 | 0.963741 | 26.05 |
| 2024-acf-fall-at-rutgers | 17 | 19 | 16.7044 | 0.93497 | 30.5165 |
| 2024-acf-fall-at-washington | 14 | 13 | 16.6377 | 0.943895 | 31.6674 |
| 2024-acf-nationals | 47 | 81 | 9.46955 | 0.95813 | 20.1697 |
| 2024-acf-regionals-berkeley | 5 | 6 | 10.4435 | 1 | 38.563 |
| 2024-acf-regionals-cornell | 6 | 6 | 18.9725 | 0.828571 | 35.9878 |
| 2024-acf-regionals-imperial | 15 | 18 | 16.0596 | 0.945487 | 22.6093 |
| 2024-acf-regionals-jmu | 20 | 25 | 14.6353 | 0.937547 | 23.672 |
| 2024-acf-regionals-minnesota | 4 | 4 | 12.984 | 0.8 | 15.5235 |
| 2024-acf-regionals-mit | 2 | 1 | 11.9635 | 1 | 23.9269 |
| 2024-acf-regionals-nebraska | 9 | 14 | 16.371 | 0.816667 | 40.3281 |
| 2024-acf-regionals-ohio-state | 7 | 6 | 16.7119 | 0.892857 | 32.9647 |
| 2024-acf-regionals-rutgers | 11 | 11 | 13.5202 | 0.972727 | 29.8348 |
| 2024-acf-regionals-vanderbilt | 10 | 10 | 15.9638 | 0.859772 | 17.8228 |
| 2024-acf-winter-at-brandeis | 19 | 18 | 16.1928 | 0.969724 | 24.2932 |
| 2024-acf-winter-at-central-florida | 10 | 10 | 8.14929 | 0.996965 | 18.583 |
| 2024-acf-winter-at-clemson | 18 | 17 | 12.6422 | 0.972108 | 24.2581 |
| 2024-acf-winter-at-lehigh | 12 | 13 | 14.0903 | 0.956219 | 25.9809 |
| 2024-acf-winter-at-northwestern | 20 | 20 | 13.239 | 0.973665 | 27.5522 |
| 2024-acf-winter-at-ohio-state | 18 | 15 | 22.1562 | 0.916797 | 29.0072 |
| 2024-acf-winter-at-online | 14 | 19 | 16.9005 | 0.938328 | 24.5947 |
| 2024-acf-winter-at-oxford | 18 | 19 | 16.2758 | 0.8508 | 37.5548 |
| 2024-acf-winter-at-ubc | 6 | 6 | 24.7845 | 0.6 | 42.4255 |
| 2024-acf-winter-at-uc-berkeley | 4 | 5 | 40.2487 | 1 | 62.8932 |

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
| bonus_part_correctness | aggregate | all | 25866 | 0.0169516 | 0.128351 | 0.898352 | 0.404232 |
| bonus_part_correctness | tier | fall | 8259 | 0.0230379 | 0.128761 | 0.895652 | 0.401618 |
| bonus_part_correctness | tier | nationals | 4167 | 0.0230905 | 0.128484 | 0.894444 | 0.408063 |
| bonus_part_correctness | tier | regionals | 5457 | 0.0179771 | 0.129203 | 0.89617 | 0.407992 |
| bonus_part_correctness | tier | winter | 7983 | 0.0227923 | 0.127275 | 0.899957 | 0.402367 |
| bonus_part_correctness | category | Current Events | 258 | 0.0575181 | 0.142713 | 0.883609 | 0.442158 |
| bonus_part_correctness | category | Fine Arts | 3000 | 0.031661 | 0.132093 | 0.893344 | 0.413981 |
| bonus_part_correctness | category | Geography | 450 | 0.0485121 | 0.127947 | 0.89784 | 0.403934 |
| bonus_part_correctness | category | History | 4116 | 0.0192097 | 0.125262 | 0.902786 | 0.393196 |
| bonus_part_correctness | category | Literature | 4092 | 0.0180073 | 0.125539 | 0.901675 | 0.396239 |
| bonus_part_correctness | category | Mythology | 951 | 0.0458518 | 0.127211 | 0.893662 | 0.400981 |
| bonus_part_correctness | category | Other Academic | 276 | 0.0392114 | 0.114204 | 0.914781 | 0.369991 |
| bonus_part_correctness | category | Philosophy | 957 | 0.029236 | 0.135337 | 0.887897 | 0.431952 |
| bonus_part_correctness | category | Popular Culture | 300 | 0.0601017 | 0.143307 | 0.87624 | 0.42553 |
| bonus_part_correctness | category | Religion | 1029 | 0.0285529 | 0.126574 | 0.902209 | 0.399057 |
| bonus_part_correctness | category | Science | 4089 | 0.0216623 | 0.130779 | 0.894109 | 0.412975 |
| bonus_part_correctness | category | Social Science | 891 | 0.0301737 | 0.117729 | 0.913683 | 0.368231 |
| bonus_part_correctness | category | Unknown | 5457 | 0.0179771 | 0.129203 | 0.89617 | 0.407992 |
| bonus_part_correctness | difficulty | easy | 8622 | 0.0277374 | 0.068288 | 0.818874 | 0.239825 |
| bonus_part_correctness | difficulty | hard | 8622 | 0.0366831 | 0.116248 | 0.766756 | 0.382759 |
| bonus_part_correctness | difficulty | medium | 8622 | 0.043203 | 0.200516 | 0.761592 | 0.590112 |
