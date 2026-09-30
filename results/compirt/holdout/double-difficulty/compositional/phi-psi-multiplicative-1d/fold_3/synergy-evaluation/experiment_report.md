# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 20.9666 |
| tournament_team_bonus_ppg_spearman | 0.888953 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 461 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 33.0654 |
| bonus_game_margin_mae_games | 461 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.89004 |
| log_loss | 0.418627 |
| ece | 0.0180694 |
| brier | 0.133738 |
| part_accuracy | 0.807136 |
| part_accuracy_easy | 0.912005 |
| part_accuracy_medium | 0.674039 |
| part_accuracy_hard | 0.835364 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.525685 |
| accuracy_lift_over_all_correct | 0.281451 |
| part_accuracy_macro_team | 0.809654 |
| part_accuracy_macro_bonus | 0.80684 |
| part_count_easy | 8455 |
| part_count_medium | 8455 |
| part_count_hard | 8455 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.341863 |
| probability_p10 | 0.0606878 |
| probability_p50 | 0.538339 |
| probability_p90 | 0.958784 |
| mean_predictive_variance | 0.13239 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.507629 |
| ranked_probability_score | 0.118803 |
| bonus_total_score_log_loss | 1.03783 |
| ppb_mae | 2.32229 |
| ranked_probability_score_responses | 8455 |
| bonus_total_score_log_loss_responses | 8455 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 9 | 9 | 12.9019 | 0.966667 | 20.4726 |
| 2024-acf-fall-at-cornell | 16 | 18 | 16.6083 | 0.887417 | 35.306 |
| 2024-acf-fall-at-georgia | 22 | 26 | 21.0215 | 0.946 | 32.4738 |
| 2024-acf-fall-at-illinois | 16 | 15 | 13.8856 | 0.896908 | 23.5925 |
| 2024-acf-fall-at-north-carolina | 17 | 22 | 20.9692 | 0.896933 | 45.2502 |
| 2024-acf-fall-at-ohio-state | 15 | 20 | 19.6165 | 0.989268 | 32.2069 |
| 2024-acf-fall-at-rutgers | 15 | 19 | 24.8852 | 0.813226 | 44.619 |
| 2024-acf-fall-at-washington | 12 | 13 | 23.473 | 0.699301 | 40.0094 |
| 2024-acf-nationals | 46 | 79 | 18.1325 | 0.833714 | 30.5872 |
| 2024-acf-regionals-berkeley | 6 | 5 | 21.9667 | 0.927634 | 31.6445 |
| 2024-acf-regionals-cornell | 5 | 6 | 21.2804 | 0.9 | 19.5828 |
| 2024-acf-regionals-imperial | 15 | 17 | 21.4082 | 0.882932 | 33.5249 |
| 2024-acf-regionals-jmu | 19 | 25 | 21.2131 | 0.924496 | 27.5814 |
| 2024-acf-regionals-minnesota | 3 | 4 | 32.5012 | 1 | 55.2449 |
| 2024-acf-regionals-mit | 4 | 2 | 21.9926 | 0.8 | 19.5854 |
| 2024-acf-regionals-nebraska | 11 | 13 | 25.1418 | 0.824604 | 39.6028 |
| 2024-acf-regionals-ohio-state | 5 | 6 | 14.803 | 0.8 | 27.0338 |
| 2024-acf-regionals-rutgers | 11 | 11 | 28.6378 | 0.769934 | 32.2054 |
| 2024-acf-regionals-vanderbilt | 10 | 10 | 10.502 | 0.987879 | 21.0967 |
| 2024-acf-winter-at-brandeis | 17 | 16 | 22.9751 | 0.960737 | 26.4929 |
| 2024-acf-winter-at-central-florida | 8 | 10 | 21.9434 | 1 | 34.5679 |
| 2024-acf-winter-at-clemson | 16 | 17 | 19.3182 | 0.908021 | 27.2572 |
| 2024-acf-winter-at-lehigh | 14 | 14 | 19.9982 | 0.981299 | 40.7959 |
| 2024-acf-winter-at-northwestern | 16 | 18 | 18.4344 | 0.931568 | 38.3049 |
| 2024-acf-winter-at-ohio-state | 15 | 17 | 24.6099 | 0.938126 | 36.739 |
| 2024-acf-winter-at-online | 17 | 19 | 20.6244 | 0.898835 | 32.2486 |
| 2024-acf-winter-at-oxford | 17 | 19 | 20.9223 | 0.828431 | 30.0368 |
| 2024-acf-winter-at-ubc | 5 | 6 | 18.6314 | 0.7 | 44.1697 |
| 2024-acf-winter-at-uc-berkeley | 6 | 5 | 29.6334 | 0.885714 | 39.4168 |

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
| bonus_part_correctness | aggregate | all | 25365 | 0.0180694 | 0.133738 | 0.89004 | 0.418627 |
| bonus_part_correctness | tier | fall | 8094 | 0.0217342 | 0.136601 | 0.882761 | 0.424893 |
| bonus_part_correctness | tier | nationals | 4125 | 0.0184427 | 0.136143 | 0.882693 | 0.427917 |
| bonus_part_correctness | tier | regionals | 5247 | 0.0316014 | 0.134989 | 0.889355 | 0.421356 |
| bonus_part_correctness | tier | winter | 7899 | 0.0186297 | 0.128717 | 0.897247 | 0.405543 |
| bonus_part_correctness | category | Current Events | 243 | 0.0679464 | 0.130859 | 0.889431 | 0.419104 |
| bonus_part_correctness | category | Fine Arts | 2937 | 0.0272843 | 0.14498 | 0.872274 | 0.448454 |
| bonus_part_correctness | category | Geography | 456 | 0.0412902 | 0.13224 | 0.887856 | 0.411633 |
| bonus_part_correctness | category | History | 4050 | 0.0162662 | 0.130489 | 0.89401 | 0.410379 |
| bonus_part_correctness | category | Literature | 4029 | 0.020491 | 0.132899 | 0.890868 | 0.416625 |
| bonus_part_correctness | category | Mythology | 936 | 0.0460006 | 0.130654 | 0.892338 | 0.404752 |
| bonus_part_correctness | category | Other Academic | 255 | 0.0517287 | 0.102647 | 0.929174 | 0.335975 |
| bonus_part_correctness | category | Philosophy | 948 | 0.036206 | 0.147612 | 0.867898 | 0.450184 |
| bonus_part_correctness | category | Popular Culture | 285 | 0.0700393 | 0.130899 | 0.897576 | 0.402998 |
| bonus_part_correctness | category | Religion | 1014 | 0.0270939 | 0.127155 | 0.899021 | 0.403731 |
| bonus_part_correctness | category | Science | 4059 | 0.0191887 | 0.132673 | 0.890023 | 0.4195 |
| bonus_part_correctness | category | Social Science | 906 | 0.0379475 | 0.120287 | 0.909682 | 0.377565 |
| bonus_part_correctness | category | Unknown | 5247 | 0.0316014 | 0.134989 | 0.889355 | 0.421356 |
| bonus_part_correctness | difficulty | easy | 8455 | 0.0289797 | 0.071252 | 0.796906 | 0.251312 |
| bonus_part_correctness | difficulty | hard | 8455 | 0.0383917 | 0.121568 | 0.746893 | 0.396877 |
| bonus_part_correctness | difficulty | medium | 8455 | 0.0443805 | 0.208395 | 0.740562 | 0.607693 |
