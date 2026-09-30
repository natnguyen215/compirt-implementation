# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 16.2307 |
| tournament_team_bonus_ppg_spearman | 0.88186 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 469 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 27.4783 |
| bonus_game_margin_mae_games | 469 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.895821 |
| log_loss | 0.409014 |
| ece | 0.0149696 |
| brier | 0.12973 |
| part_accuracy | 0.815944 |
| part_accuracy_easy | 0.901128 |
| part_accuracy_medium | 0.701989 |
| part_accuracy_hard | 0.844713 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.519367 |
| accuracy_lift_over_all_correct | 0.296576 |
| part_accuracy_macro_team | 0.819011 |
| part_accuracy_macro_bonus | 0.813643 |
| part_count_easy | 8597 |
| part_count_medium | 8597 |
| part_count_hard | 8597 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.354666 |
| probability_p10 | 0.0466013 |
| probability_p50 | 0.524949 |
| probability_p90 | 0.965426 |
| mean_predictive_variance | 0.123896 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.529952 |
| ranked_probability_score | 0.111466 |
| bonus_total_score_log_loss | 0.992056 |
| ppb_mae | 1.6858 |
| ranked_probability_score_responses | 8597 |
| bonus_total_score_log_loss_responses | 8597 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 8 | 9 | 17.0706 | 0.928571 | 27.5036 |
| 2024-acf-fall-at-cornell | 17 | 18 | 14.5769 | 0.961964 | 23.6917 |
| 2024-acf-fall-at-georgia | 22 | 24 | 12.9195 | 0.941743 | 24.1475 |
| 2024-acf-fall-at-illinois | 19 | 21 | 13.5504 | 0.975439 | 29.8128 |
| 2024-acf-fall-at-north-carolina | 18 | 22 | 14.5305 | 0.942208 | 25.3243 |
| 2024-acf-fall-at-ohio-state | 18 | 19 | 15.0374 | 0.972638 | 26.4027 |
| 2024-acf-fall-at-rutgers | 16 | 16 | 14.2103 | 0.974964 | 24.6429 |
| 2024-acf-fall-at-washington | 13 | 12 | 23.0374 | 0.917582 | 28.7637 |
| 2024-acf-nationals | 47 | 79 | 10.8428 | 0.963912 | 24.6698 |
| 2024-acf-regionals-berkeley | 5 | 6 | 5.26616 | 0.872082 | 11.7224 |
| 2024-acf-regionals-cornell | 4 | 7 | 20.5841 | 0.4 | 31.1754 |
| 2024-acf-regionals-imperial | 15 | 18 | 13.489 | 0.954424 | 22.5672 |
| 2024-acf-regionals-jmu | 18 | 24 | 9.73456 | 0.923554 | 21.6357 |
| 2024-acf-regionals-minnesota | 4 | 4 | 32.1233 | 0.2 | 62.3903 |
| 2024-acf-regionals-mit | 6 | 4 | 23.7402 | 0.942857 | 37.6138 |
| 2024-acf-regionals-nebraska | 12 | 13 | 9.0659 | 0.987742 | 24.3226 |
| 2024-acf-regionals-ohio-state | 6 | 6 | 11.1834 | 0.828571 | 14.5444 |
| 2024-acf-regionals-rutgers | 11 | 11 | 19.7302 | 0.954545 | 32.6518 |
| 2024-acf-regionals-vanderbilt | 10 | 11 | 18.2067 | 0.939394 | 40.7843 |
| 2024-acf-winter-at-brandeis | 20 | 18 | 18.8087 | 0.940955 | 27.1095 |
| 2024-acf-winter-at-central-florida | 9 | 10 | 14.4326 | 0.983333 | 19.8106 |
| 2024-acf-winter-at-clemson | 18 | 17 | 13.2858 | 0.951447 | 29.0364 |
| 2024-acf-winter-at-lehigh | 14 | 14 | 8.23921 | 0.980179 | 22.015 |
| 2024-acf-winter-at-northwestern | 20 | 21 | 15.6297 | 0.943964 | 25.4814 |
| 2024-acf-winter-at-ohio-state | 16 | 16 | 19.5201 | 0.927836 | 33.2655 |
| 2024-acf-winter-at-online | 18 | 19 | 22.0064 | 0.896801 | 42.1562 |
| 2024-acf-winter-at-oxford | 17 | 18 | 20.7417 | 0.810084 | 40.1075 |
| 2024-acf-winter-at-ubc | 5 | 6 | 9.19438 | 0.9 | 18.3255 |
| 2024-acf-winter-at-uc-berkeley | 6 | 6 | 29.932 | 0.657143 | 41.1891 |

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
| bonus_part_correctness | aggregate | all | 25791 | 0.0149696 | 0.12973 | 0.895821 | 0.409014 |
| bonus_part_correctness | tier | fall | 7995 | 0.0201977 | 0.125388 | 0.90065 | 0.391963 |
| bonus_part_correctness | tier | nationals | 4095 | 0.0165765 | 0.128155 | 0.894597 | 0.40485 |
| bonus_part_correctness | tier | regionals | 5580 | 0.0182423 | 0.130431 | 0.894639 | 0.409901 |
| bonus_part_correctness | tier | winter | 8121 | 0.024167 | 0.134317 | 0.88841 | 0.427289 |
| bonus_part_correctness | category | Current Events | 216 | 0.0627529 | 0.111585 | 0.920878 | 0.358763 |
| bonus_part_correctness | category | Fine Arts | 2970 | 0.0336683 | 0.14018 | 0.882762 | 0.434081 |
| bonus_part_correctness | category | Geography | 501 | 0.0439315 | 0.127328 | 0.900795 | 0.402633 |
| bonus_part_correctness | category | History | 4068 | 0.0135685 | 0.126762 | 0.899553 | 0.401482 |
| bonus_part_correctness | category | Literature | 4065 | 0.0245142 | 0.124552 | 0.902048 | 0.395351 |
| bonus_part_correctness | category | Mythology | 945 | 0.056373 | 0.150878 | 0.861069 | 0.45836 |
| bonus_part_correctness | category | Other Academic | 219 | 0.0766718 | 0.145923 | 0.87988 | 0.451696 |
| bonus_part_correctness | category | Philosophy | 963 | 0.0238372 | 0.132395 | 0.889444 | 0.421303 |
| bonus_part_correctness | category | Popular Culture | 288 | 0.0731951 | 0.153414 | 0.85715 | 0.470926 |
| bonus_part_correctness | category | Religion | 1008 | 0.0295933 | 0.128483 | 0.898209 | 0.405472 |
| bonus_part_correctness | category | Science | 4059 | 0.0260833 | 0.127147 | 0.897436 | 0.406824 |
| bonus_part_correctness | category | Social Science | 909 | 0.036502 | 0.110058 | 0.922647 | 0.351414 |
| bonus_part_correctness | category | Unknown | 5580 | 0.0182423 | 0.130431 | 0.894639 | 0.409901 |
| bonus_part_correctness | difficulty | easy | 8597 | 0.0223175 | 0.0766144 | 0.805523 | 0.263741 |
| bonus_part_correctness | difficulty | hard | 8597 | 0.0301028 | 0.116592 | 0.76753 | 0.383827 |
| bonus_part_correctness | difficulty | medium | 8597 | 0.0337237 | 0.195984 | 0.771297 | 0.579472 |
