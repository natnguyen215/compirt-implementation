# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 21.9079 |
| tournament_team_bonus_ppg_spearman | 0.879954 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 462 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 33.5015 |
| bonus_game_margin_mae_games | 462 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.891171 |
| log_loss | 0.416012 |
| ece | 0.0178447 |
| brier | 0.132909 |
| part_accuracy | 0.810768 |
| part_accuracy_easy | 0.9038 |
| part_accuracy_medium | 0.690974 |
| part_accuracy_hard | 0.83753 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.519002 |
| accuracy_lift_over_all_correct | 0.291766 |
| part_accuracy_macro_team | 0.814463 |
| part_accuracy_macro_bonus | 0.807721 |
| part_count_easy | 8420 |
| part_count_medium | 8420 |
| part_count_hard | 8420 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.344229 |
| probability_p10 | 0.0571274 |
| probability_p50 | 0.529071 |
| probability_p90 | 0.959916 |
| mean_predictive_variance | 0.130987 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.520784 |
| ranked_probability_score | 0.11506 |
| bonus_total_score_log_loss | 1.00796 |
| ppb_mae | 2.38938 |
| ranked_probability_score_responses | 8420 |
| bonus_total_score_log_loss_responses | 8420 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 8 | 9 | 13.1837 | 0.934148 | 30.194 |
| 2024-acf-fall-at-cornell | 17 | 18 | 19.9311 | 0.796071 | 33.6762 |
| 2024-acf-fall-at-georgia | 21 | 23 | 17.2756 | 0.927226 | 26.9754 |
| 2024-acf-fall-at-illinois | 17 | 19 | 24.132 | 0.881925 | 34.9016 |
| 2024-acf-fall-at-north-carolina | 18 | 22 | 16.4575 | 0.971606 | 27.8669 |
| 2024-acf-fall-at-ohio-state | 18 | 20 | 18.1915 | 0.889463 | 40.7211 |
| 2024-acf-fall-at-rutgers | 15 | 19 | 18.7545 | 0.932143 | 31.8845 |
| 2024-acf-fall-at-washington | 12 | 13 | 20.2136 | 0.725045 | 32.8721 |
| 2024-acf-nationals | 48 | 80 | 18.8673 | 0.897179 | 32.6754 |
| 2024-acf-regionals-berkeley | 6 | 7 | 28.3683 | 0.942857 | 35.2149 |
| 2024-acf-regionals-cornell | 6 | 6 | 33.0385 | 0.6 | 50.5704 |
| 2024-acf-regionals-imperial | 15 | 18 | 21.6941 | 0.882143 | 44.2806 |
| 2024-acf-regionals-jmu | 19 | 23 | 24.4829 | 0.960948 | 32.178 |
| 2024-acf-regionals-minnesota | 3 | 4 | 27.8293 | 0.5 | 29.0461 |
| 2024-acf-regionals-mit | 7 | 4 | 24.895 | 1 | 37.9667 |
| 2024-acf-regionals-nebraska | 11 | 13 | 20.2526 | 0.883829 | 38.6965 |
| 2024-acf-regionals-ohio-state | 7 | 5 | 25.4669 | 0.964286 | 29.4261 |
| 2024-acf-regionals-rutgers | 10 | 11 | 23.8353 | 0.975758 | 43.5715 |
| 2024-acf-regionals-vanderbilt | 10 | 9 | 28.2476 | 0.951515 | 45.3472 |
| 2024-acf-winter-at-brandeis | 16 | 16 | 20.8912 | 0.927153 | 19.9042 |
| 2024-acf-winter-at-central-florida | 9 | 10 | 24.5188 | 0.95 | 19.0363 |
| 2024-acf-winter-at-clemson | 15 | 17 | 17.6582 | 0.949062 | 33.4449 |
| 2024-acf-winter-at-lehigh | 13 | 12 | 16.4971 | 0.973866 | 39.9581 |
| 2024-acf-winter-at-northwestern | 17 | 18 | 18.8552 | 0.909314 | 29.6604 |
| 2024-acf-winter-at-ohio-state | 16 | 16 | 18.0919 | 0.910835 | 33.37 |
| 2024-acf-winter-at-online | 15 | 20 | 21.9805 | 0.875 | 35.088 |
| 2024-acf-winter-at-oxford | 17 | 19 | 17.9865 | 0.884663 | 31.7734 |
| 2024-acf-winter-at-ubc | 6 | 6 | 22.6522 | 0.942857 | 25.0147 |
| 2024-acf-winter-at-uc-berkeley | 6 | 5 | 31.0814 | 0.579771 | 53.7153 |

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
| bonus_part_correctness | aggregate | all | 25260 | 0.0178447 | 0.132909 | 0.891171 | 0.416012 |
| bonus_part_correctness | tier | fall | 8160 | 0.0149132 | 0.132795 | 0.886877 | 0.412985 |
| bonus_part_correctness | tier | nationals | 4107 | 0.0290038 | 0.130469 | 0.891253 | 0.41218 |
| bonus_part_correctness | tier | regionals | 5280 | 0.0299518 | 0.140124 | 0.881054 | 0.433165 |
| bonus_part_correctness | tier | winter | 7713 | 0.0265969 | 0.12939 | 0.894324 | 0.409513 |
| bonus_part_correctness | category | Current Events | 249 | 0.0516843 | 0.124918 | 0.897727 | 0.403377 |
| bonus_part_correctness | category | Fine Arts | 2934 | 0.0199729 | 0.141125 | 0.87801 | 0.439272 |
| bonus_part_correctness | category | Geography | 459 | 0.0509864 | 0.136088 | 0.87839 | 0.426552 |
| bonus_part_correctness | category | History | 4017 | 0.0225272 | 0.128458 | 0.897916 | 0.402184 |
| bonus_part_correctness | category | Literature | 4047 | 0.0206195 | 0.126169 | 0.899406 | 0.400867 |
| bonus_part_correctness | category | Mythology | 924 | 0.0386453 | 0.141356 | 0.872099 | 0.434865 |
| bonus_part_correctness | category | Other Academic | 237 | 0.0627845 | 0.113644 | 0.926829 | 0.365256 |
| bonus_part_correctness | category | Philosophy | 948 | 0.0353915 | 0.136126 | 0.885258 | 0.427824 |
| bonus_part_correctness | category | Popular Culture | 294 | 0.0694512 | 0.130923 | 0.886258 | 0.404233 |
| bonus_part_correctness | category | Religion | 984 | 0.0261616 | 0.125916 | 0.899678 | 0.403052 |
| bonus_part_correctness | category | Science | 3990 | 0.0242089 | 0.132561 | 0.891847 | 0.414143 |
| bonus_part_correctness | category | Social Science | 897 | 0.0413416 | 0.117364 | 0.910846 | 0.375231 |
| bonus_part_correctness | category | Unknown | 5280 | 0.0299518 | 0.140124 | 0.881054 | 0.433165 |
| bonus_part_correctness | difficulty | easy | 8420 | 0.0254208 | 0.0772963 | 0.783931 | 0.26884 |
| bonus_part_correctness | difficulty | hard | 8420 | 0.0330917 | 0.120373 | 0.757209 | 0.389754 |
| bonus_part_correctness | difficulty | medium | 8420 | 0.0400102 | 0.201059 | 0.758117 | 0.589443 |
