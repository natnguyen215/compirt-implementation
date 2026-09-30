# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 16.2487 |
| tournament_team_bonus_ppg_spearman | 0.930081 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 462 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 25.5625 |
| bonus_game_margin_mae_games | 462 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.897711 |
| log_loss | 0.405838 |
| ece | 0.0181723 |
| brier | 0.128291 |
| part_accuracy | 0.821417 |
| part_accuracy_easy | 0.907007 |
| part_accuracy_medium | 0.712827 |
| part_accuracy_hard | 0.844418 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.519002 |
| accuracy_lift_over_all_correct | 0.302415 |
| part_accuracy_macro_team | 0.823514 |
| part_accuracy_macro_bonus | 0.819997 |
| part_count_easy | 8420 |
| part_count_medium | 8420 |
| part_count_hard | 8420 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.334624 |
| probability_p10 | 0.0751867 |
| probability_p50 | 0.520602 |
| probability_p90 | 0.94845 |
| mean_predictive_variance | 0.137714 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.542874 |
| ranked_probability_score | 0.109143 |
| bonus_total_score_log_loss | 0.968351 |
| ppb_mae | 1.78462 |
| ranked_probability_score_responses | 8420 |
| bonus_total_score_log_loss_responses | 8420 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 8 | 9 | 15.0415 | 0.99403 | 33.4932 |
| 2024-acf-fall-at-cornell | 17 | 18 | 9.73886 | 0.968062 | 25.726 |
| 2024-acf-fall-at-georgia | 21 | 23 | 14.0258 | 0.957765 | 27.4583 |
| 2024-acf-fall-at-illinois | 17 | 19 | 15.9636 | 0.867165 | 20.3687 |
| 2024-acf-fall-at-north-carolina | 18 | 22 | 15.6631 | 0.946825 | 24.1258 |
| 2024-acf-fall-at-ohio-state | 18 | 20 | 9.53696 | 0.967976 | 22.5821 |
| 2024-acf-fall-at-rutgers | 15 | 19 | 13.5138 | 0.960714 | 22.3875 |
| 2024-acf-fall-at-washington | 12 | 13 | 13.1611 | 0.903679 | 30.0624 |
| 2024-acf-nationals | 48 | 80 | 11.6089 | 0.947246 | 21.7219 |
| 2024-acf-regionals-berkeley | 6 | 7 | 17.1367 | 0.942857 | 20.4149 |
| 2024-acf-regionals-cornell | 6 | 6 | 23.9992 | 0.6 | 40.2226 |
| 2024-acf-regionals-imperial | 15 | 18 | 13.3703 | 0.907143 | 25.7036 |
| 2024-acf-regionals-jmu | 19 | 23 | 11.2631 | 0.978499 | 19.5312 |
| 2024-acf-regionals-minnesota | 3 | 4 | 10.7003 | 1 | 13.523 |
| 2024-acf-regionals-mit | 7 | 4 | 23.9333 | 1 | 22.5058 |
| 2024-acf-regionals-nebraska | 11 | 13 | 21.4042 | 0.91572 | 40.4308 |
| 2024-acf-regionals-ohio-state | 7 | 5 | 19.1243 | 0.964286 | 16.716 |
| 2024-acf-regionals-rutgers | 10 | 11 | 16.4122 | 0.975758 | 23.7625 |
| 2024-acf-regionals-vanderbilt | 10 | 9 | 25.3099 | 0.963636 | 39.0642 |
| 2024-acf-winter-at-brandeis | 16 | 16 | 14.9442 | 0.944813 | 21.2208 |
| 2024-acf-winter-at-central-florida | 9 | 10 | 17.1671 | 0.966667 | 17.9144 |
| 2024-acf-winter-at-clemson | 15 | 17 | 13.5145 | 0.974084 | 27.9843 |
| 2024-acf-winter-at-lehigh | 13 | 12 | 11.8556 | 0.965613 | 23.0901 |
| 2024-acf-winter-at-northwestern | 17 | 18 | 12.7108 | 0.968137 | 22.9256 |
| 2024-acf-winter-at-ohio-state | 16 | 16 | 18.6 | 0.907887 | 31.6447 |
| 2024-acf-winter-at-online | 15 | 20 | 15.1739 | 0.939286 | 28.8839 |
| 2024-acf-winter-at-oxford | 17 | 19 | 16.1533 | 0.906749 | 33.7384 |
| 2024-acf-winter-at-ubc | 6 | 6 | 16.3831 | 1 | 19.5665 |
| 2024-acf-winter-at-uc-berkeley | 6 | 5 | 33.8018 | 0.637748 | 60.3088 |

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
| bonus_part_correctness | aggregate | all | 25260 | 0.0181723 | 0.128291 | 0.897711 | 0.405838 |
| bonus_part_correctness | tier | fall | 8160 | 0.0140042 | 0.128943 | 0.892195 | 0.404213 |
| bonus_part_correctness | tier | nationals | 4107 | 0.0490153 | 0.125717 | 0.899652 | 0.404334 |
| bonus_part_correctness | tier | regionals | 5280 | 0.0292468 | 0.131233 | 0.893182 | 0.41475 |
| bonus_part_correctness | tier | winter | 7713 | 0.0278696 | 0.126958 | 0.899016 | 0.402257 |
| bonus_part_correctness | category | Current Events | 249 | 0.050739 | 0.120003 | 0.910576 | 0.38355 |
| bonus_part_correctness | category | Fine Arts | 2934 | 0.0223944 | 0.139817 | 0.87963 | 0.436723 |
| bonus_part_correctness | category | Geography | 459 | 0.0296663 | 0.136377 | 0.87841 | 0.424036 |
| bonus_part_correctness | category | History | 4017 | 0.0204046 | 0.125351 | 0.902127 | 0.395677 |
| bonus_part_correctness | category | Literature | 4047 | 0.0239497 | 0.121309 | 0.906429 | 0.390147 |
| bonus_part_correctness | category | Mythology | 924 | 0.0279519 | 0.145803 | 0.864972 | 0.449037 |
| bonus_part_correctness | category | Other Academic | 237 | 0.0689973 | 0.119793 | 0.911995 | 0.38697 |
| bonus_part_correctness | category | Philosophy | 948 | 0.0451441 | 0.129479 | 0.895607 | 0.408874 |
| bonus_part_correctness | category | Popular Culture | 294 | 0.0682288 | 0.132918 | 0.882576 | 0.407859 |
| bonus_part_correctness | category | Religion | 984 | 0.0235852 | 0.12558 | 0.90011 | 0.401852 |
| bonus_part_correctness | category | Science | 3990 | 0.0239189 | 0.126286 | 0.901239 | 0.399148 |
| bonus_part_correctness | category | Social Science | 897 | 0.0412557 | 0.109428 | 0.922195 | 0.356269 |
| bonus_part_correctness | category | Unknown | 5280 | 0.0292468 | 0.131233 | 0.893182 | 0.41475 |
| bonus_part_correctness | difficulty | easy | 8420 | 0.0490718 | 0.0761775 | 0.799141 | 0.269148 |
| bonus_part_correctness | difficulty | hard | 8420 | 0.0374414 | 0.116704 | 0.780293 | 0.379431 |
| bonus_part_correctness | difficulty | medium | 8420 | 0.0281569 | 0.191992 | 0.778744 | 0.568935 |
