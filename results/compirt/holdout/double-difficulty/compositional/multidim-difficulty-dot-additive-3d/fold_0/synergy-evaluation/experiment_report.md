# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 15.9316 |
| tournament_team_bonus_ppg_spearman | 0.879414 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 471 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 25.3058 |
| bonus_game_margin_mae_games | 471 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.899357 |
| log_loss | 0.402038 |
| ece | 0.0107842 |
| brier | 0.127667 |
| part_accuracy | 0.818383 |
| part_accuracy_easy | 0.90007 |
| part_accuracy_medium | 0.708343 |
| part_accuracy_hard | 0.846735 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.518437 |
| accuracy_lift_over_all_correct | 0.299946 |
| part_accuracy_macro_team | 0.819373 |
| part_accuracy_macro_bonus | 0.817303 |
| part_count_easy | 8606 |
| part_count_medium | 8606 |
| part_count_hard | 8606 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.354036 |
| probability_p10 | 0.0451723 |
| probability_p50 | 0.513261 |
| probability_p90 | 0.984773 |
| mean_predictive_variance | 0.124171 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.532187 |
| ranked_probability_score | 0.110632 |
| bonus_total_score_log_loss | 0.98273 |
| ppb_mae | 1.70607 |
| ranked_probability_score_responses | 8606 |
| bonus_total_score_log_loss_responses | 8606 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 9 | 9 | 14.4792 | 0.928878 | 37.8553 |
| 2024-acf-fall-at-cornell | 17 | 18 | 15.2548 | 0.946013 | 25.9291 |
| 2024-acf-fall-at-georgia | 24 | 25 | 13.4199 | 0.945147 | 29.3517 |
| 2024-acf-fall-at-illinois | 19 | 22 | 17.578 | 0.942005 | 28.915 |
| 2024-acf-fall-at-north-carolina | 17 | 22 | 12.7045 | 0.944786 | 23.7837 |
| 2024-acf-fall-at-ohio-state | 16 | 20 | 13.1618 | 0.972019 | 19.5241 |
| 2024-acf-fall-at-rutgers | 17 | 19 | 17.3111 | 0.8645 | 30.6792 |
| 2024-acf-fall-at-washington | 14 | 13 | 16.9088 | 0.925112 | 18.6829 |
| 2024-acf-nationals | 46 | 81 | 10.3446 | 0.9234 | 23.2704 |
| 2024-acf-regionals-berkeley | 5 | 6 | 13.2678 | 0.9 | 28.8711 |
| 2024-acf-regionals-cornell | 6 | 6 | 25.5819 | 0.637748 | 36.0793 |
| 2024-acf-regionals-imperial | 14 | 18 | 14.7989 | 0.873488 | 29.3655 |
| 2024-acf-regionals-jmu | 18 | 23 | 11.2264 | 0.904297 | 25.1246 |
| 2024-acf-regionals-minnesota | 3 | 4 | 6.42973 | 1 | 12.916 |
| 2024-acf-regionals-mit | 5 | 3 | 26.3639 | 0.7 | 33.6521 |
| 2024-acf-regionals-nebraska | 12 | 14 | 14.9613 | 0.928198 | 20.5753 |
| 2024-acf-regionals-ohio-state | 7 | 5 | 16.3512 | 0.964286 | 10.9244 |
| 2024-acf-regionals-rutgers | 11 | 12 | 14.6256 | 0.911164 | 31.0358 |
| 2024-acf-regionals-vanderbilt | 6 | 5 | 27.0276 | 0.782691 | 34.9852 |
| 2024-acf-winter-at-brandeis | 16 | 17 | 17.1118 | 0.955882 | 25.3602 |
| 2024-acf-winter-at-central-florida | 11 | 9 | 13.1623 | 0.977179 | 31.0978 |
| 2024-acf-winter-at-clemson | 16 | 17 | 14.6767 | 0.929412 | 22.1931 |
| 2024-acf-winter-at-lehigh | 14 | 12 | 13.5221 | 0.958152 | 13.8461 |
| 2024-acf-winter-at-northwestern | 20 | 21 | 10.078 | 0.970535 | 24.2765 |
| 2024-acf-winter-at-ohio-state | 17 | 18 | 13.0458 | 0.973007 | 19.3632 |
| 2024-acf-winter-at-online | 16 | 19 | 15.9447 | 0.9352 | 23.1431 |
| 2024-acf-winter-at-oxford | 19 | 21 | 15.3657 | 0.93849 | 26.836 |
| 2024-acf-winter-at-ubc | 5 | 6 | 12.69 | 0.5 | 26.5557 |
| 2024-acf-winter-at-uc-berkeley | 6 | 6 | 34.6225 | 0.371429 | 50.516 |

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
| bonus_part_correctness | aggregate | all | 25818 | 0.0107842 | 0.127667 | 0.899357 | 0.402038 |
| bonus_part_correctness | tier | fall | 8415 | 0.0161122 | 0.129821 | 0.893471 | 0.403028 |
| bonus_part_correctness | tier | nationals | 4179 | 0.0239626 | 0.124576 | 0.898813 | 0.39785 |
| bonus_part_correctness | tier | regionals | 5070 | 0.0143613 | 0.127217 | 0.899801 | 0.39997 |
| bonus_part_correctness | tier | winter | 8154 | 0.0190222 | 0.127309 | 0.89901 | 0.404447 |
| bonus_part_correctness | category | Current Events | 258 | 0.0419721 | 0.104545 | 0.929026 | 0.346913 |
| bonus_part_correctness | category | Fine Arts | 3075 | 0.0145839 | 0.13439 | 0.889099 | 0.421622 |
| bonus_part_correctness | category | Geography | 453 | 0.0247675 | 0.130335 | 0.890173 | 0.41459 |
| bonus_part_correctness | category | History | 4176 | 0.0157323 | 0.127929 | 0.898579 | 0.402522 |
| bonus_part_correctness | category | Literature | 4197 | 0.0217945 | 0.118175 | 0.912986 | 0.372551 |
| bonus_part_correctness | category | Mythology | 951 | 0.0348992 | 0.134232 | 0.88484 | 0.41756 |
| bonus_part_correctness | category | Other Academic | 258 | 0.0690388 | 0.111792 | 0.924829 | 0.356555 |
| bonus_part_correctness | category | Philosophy | 969 | 0.0277388 | 0.134979 | 0.886452 | 0.426107 |
| bonus_part_correctness | category | Popular Culture | 303 | 0.0725541 | 0.151806 | 0.860823 | 0.440133 |
| bonus_part_correctness | category | Religion | 1041 | 0.0305939 | 0.128331 | 0.898724 | 0.40686 |
| bonus_part_correctness | category | Science | 4152 | 0.0192196 | 0.129145 | 0.896413 | 0.408405 |
| bonus_part_correctness | category | Social Science | 915 | 0.0363354 | 0.129571 | 0.895789 | 0.414263 |
| bonus_part_correctness | category | Unknown | 5070 | 0.0143613 | 0.127217 | 0.899801 | 0.39997 |
| bonus_part_correctness | difficulty | easy | 8606 | 0.0234278 | 0.0752687 | 0.817401 | 0.2602 |
| bonus_part_correctness | difficulty | hard | 8606 | 0.0333641 | 0.113856 | 0.787742 | 0.372556 |
| bonus_part_correctness | difficulty | medium | 8606 | 0.025245 | 0.193877 | 0.77458 | 0.573357 |
