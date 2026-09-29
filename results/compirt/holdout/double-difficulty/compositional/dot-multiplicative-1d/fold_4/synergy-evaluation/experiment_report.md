# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 22.0499 |
| tournament_team_bonus_ppg_spearman | 0.90889 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 469 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 33.0954 |
| bonus_game_margin_mae_games | 469 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.890885 |
| log_loss | 0.416853 |
| ece | 0.0161637 |
| brier | 0.133423 |
| part_accuracy | 0.807624 |
| part_accuracy_easy | 0.913129 |
| part_accuracy_medium | 0.673278 |
| part_accuracy_hard | 0.836465 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.525555 |
| accuracy_lift_over_all_correct | 0.282069 |
| part_accuracy_macro_team | 0.811226 |
| part_accuracy_macro_bonus | 0.804172 |
| part_count_easy | 8622 |
| part_count_medium | 8622 |
| part_count_hard | 8622 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.346039 |
| probability_p10 | 0.0561926 |
| probability_p50 | 0.536393 |
| probability_p90 | 0.964112 |
| mean_predictive_variance | 0.129514 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.508119 |
| ranked_probability_score | 0.118647 |
| bonus_total_score_log_loss | 1.03626 |
| ppb_mae | 2.35478 |
| ranked_probability_score_responses | 8622 |
| bonus_total_score_log_loss_responses | 8622 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 9 | 8 | 17.6588 | 0.966667 | 20.205 |
| 2024-acf-fall-at-cornell | 15 | 17 | 17.8012 | 0.872208 | 21.1956 |
| 2024-acf-fall-at-georgia | 24 | 26 | 16.7606 | 0.935365 | 32.0769 |
| 2024-acf-fall-at-illinois | 18 | 22 | 17.6153 | 0.993797 | 30.5957 |
| 2024-acf-fall-at-north-carolina | 18 | 22 | 23.311 | 0.930378 | 27.283 |
| 2024-acf-fall-at-ohio-state | 17 | 18 | 22.2301 | 0.897361 | 37.8918 |
| 2024-acf-fall-at-rutgers | 17 | 19 | 24.319 | 0.904295 | 42.9769 |
| 2024-acf-fall-at-washington | 14 | 13 | 20.0531 | 0.937294 | 29.9132 |
| 2024-acf-nationals | 47 | 81 | 17.1892 | 0.899737 | 30.7124 |
| 2024-acf-regionals-berkeley | 5 | 6 | 34.9924 | 1 | 70.6353 |
| 2024-acf-regionals-cornell | 6 | 6 | 25.7518 | 0.771429 | 44.76 |
| 2024-acf-regionals-imperial | 15 | 18 | 25.3849 | 0.934764 | 28.5424 |
| 2024-acf-regionals-jmu | 20 | 25 | 21.7539 | 0.939052 | 27.5583 |
| 2024-acf-regionals-minnesota | 4 | 4 | 13.4818 | 0.8 | 19.1773 |
| 2024-acf-regionals-mit | 2 | 1 | 20.12 | 1 | 40.24 |
| 2024-acf-regionals-nebraska | 9 | 14 | 24.2648 | 0.8 | 47.6891 |
| 2024-acf-regionals-ohio-state | 7 | 6 | 18.323 | 0.892857 | 34.6913 |
| 2024-acf-regionals-rutgers | 11 | 11 | 19.6544 | 0.954545 | 35.9462 |
| 2024-acf-regionals-vanderbilt | 10 | 10 | 23.6372 | 0.762209 | 33.9769 |
| 2024-acf-winter-at-brandeis | 19 | 18 | 27.8385 | 0.967091 | 39.5547 |
| 2024-acf-winter-at-central-florida | 10 | 10 | 7.96682 | 0.996965 | 20.4895 |
| 2024-acf-winter-at-clemson | 18 | 17 | 19.216 | 0.932852 | 36.827 |
| 2024-acf-winter-at-lehigh | 12 | 13 | 26.1134 | 0.935203 | 36.9428 |
| 2024-acf-winter-at-northwestern | 20 | 20 | 18.6731 | 0.960873 | 28.2171 |
| 2024-acf-winter-at-ohio-state | 18 | 15 | 22.5575 | 0.938502 | 26.3893 |
| 2024-acf-winter-at-online | 14 | 19 | 16.7916 | 0.929518 | 28.4288 |
| 2024-acf-winter-at-oxford | 18 | 19 | 19.3367 | 0.847703 | 40.8292 |
| 2024-acf-winter-at-ubc | 6 | 6 | 29.8321 | 0.657143 | 45.1605 |
| 2024-acf-winter-at-uc-berkeley | 4 | 5 | 46.8194 | 1 | 64.8028 |

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
| bonus_part_correctness | aggregate | all | 25866 | 0.0161637 | 0.133423 | 0.890885 | 0.416853 |
| bonus_part_correctness | tier | fall | 8259 | 0.0164712 | 0.131847 | 0.890265 | 0.408776 |
| bonus_part_correctness | tier | nationals | 4167 | 0.0279295 | 0.136991 | 0.8832 | 0.428844 |
| bonus_part_correctness | tier | regionals | 5457 | 0.0184465 | 0.135531 | 0.887708 | 0.42213 |
| bonus_part_correctness | tier | winter | 7983 | 0.0201092 | 0.131749 | 0.892625 | 0.415344 |
| bonus_part_correctness | category | Current Events | 258 | 0.0534978 | 0.140684 | 0.884632 | 0.43399 |
| bonus_part_correctness | category | Fine Arts | 3000 | 0.024198 | 0.138204 | 0.883604 | 0.428454 |
| bonus_part_correctness | category | Geography | 450 | 0.0474865 | 0.135188 | 0.889719 | 0.416641 |
| bonus_part_correctness | category | History | 4116 | 0.0190423 | 0.128733 | 0.897305 | 0.40306 |
| bonus_part_correctness | category | Literature | 4092 | 0.0219461 | 0.131329 | 0.892869 | 0.412307 |
| bonus_part_correctness | category | Mythology | 951 | 0.0457197 | 0.132526 | 0.885012 | 0.415169 |
| bonus_part_correctness | category | Other Academic | 276 | 0.0360764 | 0.120601 | 0.910879 | 0.379832 |
| bonus_part_correctness | category | Philosophy | 957 | 0.0447929 | 0.142779 | 0.877055 | 0.445653 |
| bonus_part_correctness | category | Popular Culture | 300 | 0.0534751 | 0.130425 | 0.890435 | 0.397294 |
| bonus_part_correctness | category | Religion | 1029 | 0.0416751 | 0.130675 | 0.897158 | 0.406792 |
| bonus_part_correctness | category | Science | 4089 | 0.021353 | 0.135273 | 0.887057 | 0.425394 |
| bonus_part_correctness | category | Social Science | 891 | 0.0436153 | 0.123265 | 0.902555 | 0.386561 |
| bonus_part_correctness | category | Unknown | 5457 | 0.0184465 | 0.135531 | 0.887708 | 0.42213 |
| bonus_part_correctness | difficulty | easy | 8622 | 0.0325514 | 0.0708469 | 0.797794 | 0.249358 |
| bonus_part_correctness | difficulty | hard | 8622 | 0.0413765 | 0.121327 | 0.748987 | 0.394674 |
| bonus_part_correctness | difficulty | medium | 8622 | 0.0484543 | 0.208094 | 0.741926 | 0.606529 |
