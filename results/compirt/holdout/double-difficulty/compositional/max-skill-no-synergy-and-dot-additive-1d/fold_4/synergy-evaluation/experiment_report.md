# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 15.5505 |
| tournament_team_bonus_ppg_spearman | 0.929049 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 469 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 26.3824 |
| bonus_game_margin_mae_games | 469 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.897119 |
| log_loss | 0.407553 |
| ece | 0.01796 |
| brier | 0.128675 |
| part_accuracy | 0.818642 |
| part_accuracy_easy | 0.913825 |
| part_accuracy_medium | 0.695894 |
| part_accuracy_hard | 0.846207 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.525555 |
| accuracy_lift_over_all_correct | 0.293087 |
| part_accuracy_macro_team | 0.823415 |
| part_accuracy_macro_bonus | 0.815093 |
| part_count_easy | 8622 |
| part_count_medium | 8622 |
| part_count_hard | 8622 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.335536 |
| probability_p10 | 0.0739583 |
| probability_p50 | 0.520044 |
| probability_p90 | 0.950202 |
| mean_predictive_variance | 0.137096 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.533751 |
| ranked_probability_score | 0.112219 |
| bonus_total_score_log_loss | 0.995578 |
| ppb_mae | 1.6619 |
| ranked_probability_score_responses | 8622 |
| bonus_total_score_log_loss_responses | 8622 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 9 | 8 | 18.9834 | 0.966667 | 34.6376 |
| 2024-acf-fall-at-cornell | 15 | 17 | 11.8117 | 0.977659 | 19.292 |
| 2024-acf-fall-at-georgia | 24 | 26 | 11.9367 | 0.96888 | 28.7706 |
| 2024-acf-fall-at-illinois | 18 | 22 | 17.2949 | 0.975183 | 29.3247 |
| 2024-acf-fall-at-north-carolina | 18 | 22 | 13.4986 | 0.940773 | 23.135 |
| 2024-acf-fall-at-ohio-state | 17 | 18 | 14.6155 | 0.957595 | 29.8926 |
| 2024-acf-fall-at-rutgers | 17 | 19 | 16.9302 | 0.943559 | 33.847 |
| 2024-acf-fall-at-washington | 14 | 13 | 13.9326 | 0.937294 | 28.3163 |
| 2024-acf-nationals | 47 | 81 | 10.0611 | 0.954021 | 19.7773 |
| 2024-acf-regionals-berkeley | 5 | 6 | 14.0575 | 1 | 40.5943 |
| 2024-acf-regionals-cornell | 6 | 6 | 16.5992 | 0.828571 | 31.6908 |
| 2024-acf-regionals-imperial | 15 | 18 | 14.6279 | 0.940125 | 22.1988 |
| 2024-acf-regionals-jmu | 20 | 25 | 11.1382 | 0.957863 | 18.2289 |
| 2024-acf-regionals-minnesota | 4 | 4 | 17.6311 | 0.8 | 20.2003 |
| 2024-acf-regionals-mit | 2 | 1 | 11.4244 | 1 | 22.8488 |
| 2024-acf-regionals-nebraska | 9 | 14 | 16.1958 | 0.816667 | 38.2361 |
| 2024-acf-regionals-ohio-state | 7 | 6 | 12.6562 | 0.964286 | 28.7926 |
| 2024-acf-regionals-rutgers | 11 | 11 | 17.731 | 0.963636 | 31.0217 |
| 2024-acf-regionals-vanderbilt | 10 | 10 | 15.2967 | 0.859772 | 21.3665 |
| 2024-acf-winter-at-brandeis | 19 | 18 | 17.549 | 0.974112 | 28.6662 |
| 2024-acf-winter-at-central-florida | 10 | 10 | 7.06141 | 0.996965 | 12.7784 |
| 2024-acf-winter-at-clemson | 18 | 17 | 10.3019 | 0.981405 | 22.273 |
| 2024-acf-winter-at-lehigh | 12 | 13 | 17.6626 | 0.942208 | 26.9071 |
| 2024-acf-winter-at-northwestern | 20 | 20 | 13.3319 | 0.96313 | 25.1061 |
| 2024-acf-winter-at-ohio-state | 18 | 15 | 23.6418 | 0.881655 | 33.8351 |
| 2024-acf-winter-at-online | 14 | 19 | 14.7999 | 0.938328 | 22.8125 |
| 2024-acf-winter-at-oxford | 18 | 19 | 16.0913 | 0.85493 | 37.7902 |
| 2024-acf-winter-at-ubc | 6 | 6 | 21.2274 | 0.657143 | 39.1823 |
| 2024-acf-winter-at-uc-berkeley | 4 | 5 | 32.8748 | 1 | 58.1784 |

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
| bonus_part_correctness | aggregate | all | 25866 | 0.01796 | 0.128675 | 0.897119 | 0.407553 |
| bonus_part_correctness | tier | fall | 8259 | 0.0176244 | 0.128787 | 0.894724 | 0.403866 |
| bonus_part_correctness | tier | nationals | 4167 | 0.0406917 | 0.131693 | 0.889998 | 0.420132 |
| bonus_part_correctness | tier | regionals | 5457 | 0.0267001 | 0.12905 | 0.896421 | 0.409947 |
| bonus_part_correctness | tier | winter | 7983 | 0.0208779 | 0.126729 | 0.899748 | 0.403165 |
| bonus_part_correctness | category | Current Events | 258 | 0.0426805 | 0.140831 | 0.875669 | 0.444035 |
| bonus_part_correctness | category | Fine Arts | 3000 | 0.0321063 | 0.133012 | 0.890024 | 0.419453 |
| bonus_part_correctness | category | Geography | 450 | 0.0516433 | 0.127764 | 0.895972 | 0.404534 |
| bonus_part_correctness | category | History | 4116 | 0.0249377 | 0.125174 | 0.902233 | 0.395631 |
| bonus_part_correctness | category | Literature | 4092 | 0.024414 | 0.124241 | 0.903655 | 0.394969 |
| bonus_part_correctness | category | Mythology | 951 | 0.045287 | 0.130984 | 0.888879 | 0.41653 |
| bonus_part_correctness | category | Other Academic | 276 | 0.0423089 | 0.116849 | 0.913463 | 0.375742 |
| bonus_part_correctness | category | Philosophy | 957 | 0.0324534 | 0.132959 | 0.891646 | 0.423228 |
| bonus_part_correctness | category | Popular Culture | 300 | 0.0629584 | 0.141291 | 0.875864 | 0.425913 |
| bonus_part_correctness | category | Religion | 1029 | 0.0218418 | 0.131426 | 0.892621 | 0.415634 |
| bonus_part_correctness | category | Science | 4089 | 0.019444 | 0.132583 | 0.890468 | 0.419477 |
| bonus_part_correctness | category | Social Science | 891 | 0.033033 | 0.116499 | 0.915318 | 0.369849 |
| bonus_part_correctness | category | Unknown | 5457 | 0.0267001 | 0.12905 | 0.896421 | 0.409947 |
| bonus_part_correctness | difficulty | easy | 8622 | 0.0587664 | 0.0706178 | 0.818865 | 0.251831 |
| bonus_part_correctness | difficulty | hard | 8622 | 0.0405405 | 0.116388 | 0.762821 | 0.384622 |
| bonus_part_correctness | difficulty | medium | 8622 | 0.0282391 | 0.199021 | 0.763324 | 0.586206 |
