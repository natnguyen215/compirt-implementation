# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 16.7507 |
| tournament_team_bonus_ppg_spearman | 0.861881 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 471 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 26.2839 |
| bonus_game_margin_mae_games | 471 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.897662 |
| log_loss | 0.405285 |
| ece | 0.0181944 |
| brier | 0.128872 |
| part_accuracy | 0.815749 |
| part_accuracy_easy | 0.904137 |
| part_accuracy_medium | 0.698466 |
| part_accuracy_hard | 0.844643 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.518437 |
| accuracy_lift_over_all_correct | 0.297312 |
| part_accuracy_macro_team | 0.815647 |
| part_accuracy_macro_bonus | 0.814109 |
| part_count_easy | 8606 |
| part_count_medium | 8606 |
| part_count_hard | 8606 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.350338 |
| probability_p10 | 0.0536329 |
| probability_p50 | 0.541851 |
| probability_p90 | 0.962859 |
| mean_predictive_variance | 0.126564 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.525912 |
| ranked_probability_score | 0.112043 |
| bonus_total_score_log_loss | 0.989939 |
| ppb_mae | 1.88896 |
| ranked_probability_score_responses | 8606 |
| bonus_total_score_log_loss_responses | 8606 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 9 | 9 | 12.9259 | 0.97072 | 39.377 |
| 2024-acf-fall-at-cornell | 17 | 18 | 18.5972 | 0.87362 | 23.9999 |
| 2024-acf-fall-at-georgia | 24 | 25 | 15.1214 | 0.956901 | 29.3113 |
| 2024-acf-fall-at-illinois | 19 | 22 | 17.1909 | 0.92443 | 30.0005 |
| 2024-acf-fall-at-north-carolina | 17 | 22 | 15.8304 | 0.949694 | 25.335 |
| 2024-acf-fall-at-ohio-state | 16 | 20 | 13.7536 | 0.973491 | 21.9119 |
| 2024-acf-fall-at-rutgers | 17 | 19 | 18.8671 | 0.858369 | 36.8393 |
| 2024-acf-fall-at-washington | 14 | 13 | 16.4882 | 0.944936 | 16.4935 |
| 2024-acf-nationals | 46 | 81 | 13.2464 | 0.909209 | 24.6714 |
| 2024-acf-regionals-berkeley | 5 | 6 | 12.9394 | 0.9 | 23.0171 |
| 2024-acf-regionals-cornell | 6 | 6 | 23.7441 | 0.637748 | 34.0888 |
| 2024-acf-regionals-imperial | 14 | 18 | 17.6523 | 0.829483 | 38.9042 |
| 2024-acf-regionals-jmu | 18 | 23 | 14.7595 | 0.875326 | 25.0236 |
| 2024-acf-regionals-minnesota | 3 | 4 | 8.09826 | 1 | 16.7135 |
| 2024-acf-regionals-mit | 5 | 3 | 23.7137 | 0.1 | 29.7714 |
| 2024-acf-regionals-nebraska | 12 | 14 | 16.9742 | 0.942208 | 21.5764 |
| 2024-acf-regionals-ohio-state | 7 | 5 | 19.1799 | 0.964286 | 9.9797 |
| 2024-acf-regionals-rutgers | 11 | 12 | 14.8447 | 0.91572 | 29.7676 |
| 2024-acf-regionals-vanderbilt | 6 | 5 | 32.1994 | 0.695725 | 35.832 |
| 2024-acf-winter-at-brandeis | 16 | 17 | 16.2907 | 0.952941 | 23.5268 |
| 2024-acf-winter-at-central-florida | 11 | 9 | 14.5642 | 0.940649 | 27.18 |
| 2024-acf-winter-at-clemson | 16 | 17 | 16.8058 | 0.935294 | 27.7271 |
| 2024-acf-winter-at-lehigh | 14 | 12 | 13.8515 | 0.962557 | 21.8612 |
| 2024-acf-winter-at-northwestern | 20 | 21 | 10.5732 | 0.964488 | 24.4074 |
| 2024-acf-winter-at-ohio-state | 17 | 18 | 14.2694 | 0.958283 | 24.3478 |
| 2024-acf-winter-at-online | 16 | 19 | 15.6395 | 0.955818 | 22.3855 |
| 2024-acf-winter-at-oxford | 19 | 21 | 12.4462 | 0.94552 | 21.1927 |
| 2024-acf-winter-at-ubc | 5 | 6 | 9.73184 | 0.9 | 21.8921 |
| 2024-acf-winter-at-uc-berkeley | 6 | 6 | 35.4721 | 0.257143 | 49.7381 |

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
| bonus_part_correctness | aggregate | all | 25818 | 0.0181944 | 0.128872 | 0.897662 | 0.405285 |
| bonus_part_correctness | tier | fall | 8415 | 0.0227949 | 0.132211 | 0.890115 | 0.409883 |
| bonus_part_correctness | tier | nationals | 4179 | 0.0323224 | 0.125791 | 0.89735 | 0.401508 |
| bonus_part_correctness | tier | regionals | 5070 | 0.0194953 | 0.129326 | 0.896652 | 0.406119 |
| bonus_part_correctness | tier | winter | 8154 | 0.0207499 | 0.126723 | 0.899805 | 0.401956 |
| bonus_part_correctness | category | Current Events | 258 | 0.0349692 | 0.103404 | 0.926863 | 0.346631 |
| bonus_part_correctness | category | Fine Arts | 3075 | 0.0203782 | 0.135825 | 0.886119 | 0.427256 |
| bonus_part_correctness | category | Geography | 453 | 0.0478535 | 0.131454 | 0.888507 | 0.414767 |
| bonus_part_correctness | category | History | 4176 | 0.0242508 | 0.128997 | 0.897461 | 0.403549 |
| bonus_part_correctness | category | Literature | 4197 | 0.0248595 | 0.119796 | 0.910635 | 0.380027 |
| bonus_part_correctness | category | Mythology | 951 | 0.0278083 | 0.136215 | 0.882394 | 0.420735 |
| bonus_part_correctness | category | Other Academic | 258 | 0.0355023 | 0.107946 | 0.929154 | 0.349866 |
| bonus_part_correctness | category | Philosophy | 969 | 0.0332374 | 0.13547 | 0.885659 | 0.425291 |
| bonus_part_correctness | category | Popular Culture | 303 | 0.104161 | 0.155967 | 0.858973 | 0.455842 |
| bonus_part_correctness | category | Religion | 1041 | 0.0356369 | 0.130645 | 0.895985 | 0.41185 |
| bonus_part_correctness | category | Science | 4152 | 0.0221572 | 0.129575 | 0.89551 | 0.408771 |
| bonus_part_correctness | category | Social Science | 915 | 0.0301331 | 0.127053 | 0.898955 | 0.400797 |
| bonus_part_correctness | category | Unknown | 5070 | 0.0194953 | 0.129326 | 0.896652 | 0.406119 |
| bonus_part_correctness | difficulty | easy | 8606 | 0.0148309 | 0.0749453 | 0.810343 | 0.259989 |
| bonus_part_correctness | difficulty | hard | 8606 | 0.0307257 | 0.114509 | 0.782165 | 0.373916 |
| bonus_part_correctness | difficulty | medium | 8606 | 0.0389004 | 0.197162 | 0.768991 | 0.581949 |
