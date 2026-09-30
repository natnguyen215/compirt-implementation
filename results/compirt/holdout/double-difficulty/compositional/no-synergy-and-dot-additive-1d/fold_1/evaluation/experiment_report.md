# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 21.8525 |
| tournament_team_bonus_ppg_spearman | 0.879022 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 462 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 33.3945 |
| bonus_game_margin_mae_games | 462 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.891286 |
| log_loss | 0.41665 |
| ece | 0.0219135 |
| brier | 0.133151 |
| part_accuracy | 0.809026 |
| part_accuracy_easy | 0.903682 |
| part_accuracy_medium | 0.686817 |
| part_accuracy_hard | 0.83658 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.519002 |
| accuracy_lift_over_all_correct | 0.290024 |
| part_accuracy_macro_team | 0.812639 |
| part_accuracy_macro_bonus | 0.805621 |
| part_count_easy | 8420 |
| part_count_medium | 8420 |
| part_count_hard | 8420 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.344153 |
| probability_p10 | 0.0583156 |
| probability_p50 | 0.541318 |
| probability_p90 | 0.958199 |
| mean_predictive_variance | 0.130843 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.516152 |
| ranked_probability_score | 0.115547 |
| bonus_total_score_log_loss | 1.01255 |
| ppb_mae | 2.41051 |
| ranked_probability_score_responses | 8420 |
| bonus_total_score_log_loss_responses | 8420 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 8 | 9 | 13.0701 | 0.934148 | 29.2707 |
| 2024-acf-fall-at-cornell | 17 | 18 | 19.4426 | 0.796071 | 32.788 |
| 2024-acf-fall-at-georgia | 21 | 23 | 16.725 | 0.930475 | 26.2068 |
| 2024-acf-fall-at-illinois | 17 | 19 | 23.5809 | 0.888075 | 33.6425 |
| 2024-acf-fall-at-north-carolina | 18 | 22 | 16.8816 | 0.95715 | 28.065 |
| 2024-acf-fall-at-ohio-state | 18 | 20 | 19.4111 | 0.869835 | 40.2058 |
| 2024-acf-fall-at-rutgers | 15 | 19 | 17.9328 | 0.925 | 30.2085 |
| 2024-acf-fall-at-washington | 12 | 13 | 20.7379 | 0.739055 | 32.8659 |
| 2024-acf-nationals | 48 | 80 | 19.6896 | 0.895333 | 33.4406 |
| 2024-acf-regionals-berkeley | 6 | 7 | 26.9577 | 0.942857 | 34.5855 |
| 2024-acf-regionals-cornell | 6 | 6 | 32.5456 | 0.6 | 50.263 |
| 2024-acf-regionals-imperial | 15 | 18 | 21.8941 | 0.882143 | 43.896 |
| 2024-acf-regionals-jmu | 19 | 23 | 25.8308 | 0.960948 | 33.7767 |
| 2024-acf-regionals-minnesota | 3 | 4 | 26.6798 | 0.5 | 28.5774 |
| 2024-acf-regionals-mit | 7 | 4 | 24.4477 | 1 | 37.3757 |
| 2024-acf-regionals-nebraska | 11 | 13 | 20.9531 | 0.883829 | 39.2716 |
| 2024-acf-regionals-ohio-state | 7 | 5 | 25.5959 | 0.964286 | 28.8413 |
| 2024-acf-regionals-rutgers | 10 | 11 | 23.0039 | 0.975758 | 42.1304 |
| 2024-acf-regionals-vanderbilt | 10 | 9 | 28.6462 | 0.951515 | 46.3394 |
| 2024-acf-winter-at-brandeis | 16 | 16 | 21.1453 | 0.927153 | 19.4947 |
| 2024-acf-winter-at-central-florida | 9 | 10 | 25.2306 | 0.95 | 20.1794 |
| 2024-acf-winter-at-clemson | 15 | 17 | 17.4176 | 0.949062 | 33.5967 |
| 2024-acf-winter-at-lehigh | 13 | 12 | 15.7886 | 0.973866 | 39.1909 |
| 2024-acf-winter-at-northwestern | 17 | 18 | 18.8221 | 0.906863 | 28.4573 |
| 2024-acf-winter-at-ohio-state | 16 | 16 | 18.1563 | 0.910835 | 33.2891 |
| 2024-acf-winter-at-online | 15 | 20 | 21.5623 | 0.875 | 34.8877 |
| 2024-acf-winter-at-oxford | 17 | 19 | 18.5775 | 0.879755 | 31.7578 |
| 2024-acf-winter-at-ubc | 6 | 6 | 22.9469 | 0.942857 | 24.5898 |
| 2024-acf-winter-at-uc-berkeley | 6 | 5 | 30.0499 | 0.579771 | 55.2508 |

[Team PPG and absolute errors](csvs/bonus_team_ppg_leaderboard.csv); [game bonus margins](csvs/bonus_game_margin_predictions.csv).

### Bonus Distributions

Aggregate ability is part-weighted; synergy is response-weighted. Parameter plots describe fitted training parameters across entities, not posterior uncertainty intervals.

[Evaluated probabilities, aggregate ability, and synergy contributions](graphs/bonus/bonus_prediction_distributions.png).

[Fitted bonus parameters](graphs/parameters/bonus_part_parameter_distributions.png).

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in the diagnostic CSVs under `csvs/`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part_correctness | aggregate | all | 25260 | 0.0219135 | 0.133151 | 0.891286 | 0.41665 |
| bonus_part_correctness | tier | fall | 8160 | 0.0191149 | 0.132883 | 0.887034 | 0.412858 |
| bonus_part_correctness | tier | nationals | 4107 | 0.0365241 | 0.130505 | 0.892252 | 0.412913 |
| bonus_part_correctness | tier | regionals | 5280 | 0.0309061 | 0.140686 | 0.880798 | 0.435244 |
| bonus_part_correctness | tier | winter | 7713 | 0.0258498 | 0.129684 | 0.894477 | 0.409923 |
| bonus_part_correctness | category | Current Events | 249 | 0.0599667 | 0.122067 | 0.902118 | 0.396858 |
| bonus_part_correctness | category | Fine Arts | 2934 | 0.0194874 | 0.141286 | 0.877778 | 0.439859 |
| bonus_part_correctness | category | Geography | 459 | 0.0546568 | 0.131766 | 0.884869 | 0.41236 |
| bonus_part_correctness | category | History | 4017 | 0.0263314 | 0.128576 | 0.898484 | 0.402146 |
| bonus_part_correctness | category | Literature | 4047 | 0.0237706 | 0.126807 | 0.898686 | 0.402191 |
| bonus_part_correctness | category | Mythology | 924 | 0.0366039 | 0.142094 | 0.871782 | 0.436919 |
| bonus_part_correctness | category | Other Academic | 237 | 0.0720135 | 0.118516 | 0.921623 | 0.379931 |
| bonus_part_correctness | category | Philosophy | 948 | 0.0453209 | 0.137022 | 0.882956 | 0.433033 |
| bonus_part_correctness | category | Popular Culture | 294 | 0.0581921 | 0.129036 | 0.890941 | 0.39562 |
| bonus_part_correctness | category | Religion | 984 | 0.0187041 | 0.124949 | 0.901623 | 0.399708 |
| bonus_part_correctness | category | Science | 3990 | 0.0262357 | 0.132822 | 0.892449 | 0.414719 |
| bonus_part_correctness | category | Social Science | 897 | 0.0336333 | 0.117444 | 0.91116 | 0.374735 |
| bonus_part_correctness | category | Unknown | 5280 | 0.0309061 | 0.140686 | 0.880798 | 0.435244 |
| bonus_part_correctness | difficulty | easy | 8420 | 0.0217382 | 0.0764459 | 0.789731 | 0.266603 |
| bonus_part_correctness | difficulty | hard | 8420 | 0.0348771 | 0.120709 | 0.756033 | 0.391294 |
| bonus_part_correctness | difficulty | medium | 8420 | 0.0470646 | 0.202296 | 0.75652 | 0.592053 |
