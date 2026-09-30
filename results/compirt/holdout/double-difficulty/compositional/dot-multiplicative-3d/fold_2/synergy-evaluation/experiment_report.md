# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 22.097 |
| tournament_team_bonus_ppg_spearman | 0.844955 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 469 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 33.9984 |
| bonus_game_margin_mae_games | 469 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.888583 |
| log_loss | 0.421627 |
| ece | 0.0142674 |
| brier | 0.134661 |
| part_accuracy | 0.808383 |
| part_accuracy_easy | 0.900314 |
| part_accuracy_medium | 0.684657 |
| part_accuracy_hard | 0.840177 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.519367 |
| accuracy_lift_over_all_correct | 0.289016 |
| part_accuracy_macro_team | 0.811257 |
| part_accuracy_macro_bonus | 0.805501 |
| part_count_easy | 8597 |
| part_count_medium | 8597 |
| part_count_hard | 8597 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.348724 |
| probability_p10 | 0.0497473 |
| probability_p50 | 0.519348 |
| probability_p90 | 0.96614 |
| mean_predictive_variance | 0.12806 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.510992 |
| ranked_probability_score | 0.116971 |
| bonus_total_score_log_loss | 1.02777 |
| ppb_mae | 2.29589 |
| ranked_probability_score_responses | 8597 |
| bonus_total_score_log_loss_responses | 8597 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 8 | 9 | 13.3006 | 0.97619 | 25.6899 |
| 2024-acf-fall-at-cornell | 17 | 18 | 24.1267 | 0.852761 | 35.3852 |
| 2024-acf-fall-at-georgia | 22 | 24 | 20.5983 | 0.91516 | 34.5506 |
| 2024-acf-fall-at-illinois | 19 | 21 | 17.9206 | 0.968421 | 29.6155 |
| 2024-acf-fall-at-north-carolina | 18 | 22 | 14.2601 | 0.954592 | 18.7951 |
| 2024-acf-fall-at-ohio-state | 18 | 19 | 24.7477 | 0.945793 | 30.9855 |
| 2024-acf-fall-at-rutgers | 16 | 16 | 14.4363 | 0.949927 | 21.8596 |
| 2024-acf-fall-at-washington | 13 | 12 | 31.6483 | 0.851648 | 37.5404 |
| 2024-acf-nationals | 47 | 79 | 18.4248 | 0.882945 | 35.0829 |
| 2024-acf-regionals-berkeley | 5 | 6 | 33.8707 | 0.872082 | 47.4961 |
| 2024-acf-regionals-cornell | 4 | 7 | 25.0318 | 0.4 | 37.5082 |
| 2024-acf-regionals-imperial | 15 | 18 | 18.8715 | 0.927614 | 34.1201 |
| 2024-acf-regionals-jmu | 18 | 24 | 18.5466 | 0.886364 | 30.5036 |
| 2024-acf-regionals-minnesota | 4 | 4 | 27.0056 | 0.8 | 70.7927 |
| 2024-acf-regionals-mit | 6 | 4 | 22.8974 | 0.942857 | 38.0046 |
| 2024-acf-regionals-nebraska | 12 | 13 | 10.4136 | 0.956219 | 20.0437 |
| 2024-acf-regionals-ohio-state | 6 | 6 | 14.4425 | 0.542857 | 20.1977 |
| 2024-acf-regionals-rutgers | 11 | 11 | 30.7646 | 0.936364 | 43.6139 |
| 2024-acf-regionals-vanderbilt | 10 | 11 | 24.773 | 0.90303 | 50.4112 |
| 2024-acf-winter-at-brandeis | 20 | 18 | 24.7079 | 0.920647 | 39.1953 |
| 2024-acf-winter-at-central-florida | 9 | 10 | 17.4642 | 0.983333 | 26.4017 |
| 2024-acf-winter-at-clemson | 18 | 17 | 20.5484 | 0.872934 | 36.1447 |
| 2024-acf-winter-at-lehigh | 14 | 14 | 21.6807 | 0.966963 | 36.2483 |
| 2024-acf-winter-at-northwestern | 20 | 21 | 14.318 | 0.965025 | 25.9643 |
| 2024-acf-winter-at-ohio-state | 16 | 16 | 27.0088 | 0.893963 | 31.3647 |
| 2024-acf-winter-at-online | 18 | 19 | 25.4832 | 0.898865 | 43.4344 |
| 2024-acf-winter-at-oxford | 17 | 18 | 19.5122 | 0.837127 | 41.9128 |
| 2024-acf-winter-at-ubc | 5 | 6 | 19.8411 | 0.1 | 30.5412 |
| 2024-acf-winter-at-uc-berkeley | 6 | 6 | 44.1674 | 0.6 | 67.5758 |

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
| bonus_part_correctness | aggregate | all | 25791 | 0.0142674 | 0.134661 | 0.888583 | 0.421627 |
| bonus_part_correctness | tier | fall | 7995 | 0.015368 | 0.129134 | 0.894875 | 0.401448 |
| bonus_part_correctness | tier | nationals | 4095 | 0.0240976 | 0.13583 | 0.882147 | 0.427752 |
| bonus_part_correctness | tier | regionals | 5580 | 0.0173618 | 0.13538 | 0.887138 | 0.423249 |
| bonus_part_correctness | tier | winter | 8121 | 0.027451 | 0.13902 | 0.882046 | 0.437291 |
| bonus_part_correctness | category | Current Events | 216 | 0.0485861 | 0.118113 | 0.910375 | 0.3861 |
| bonus_part_correctness | category | Fine Arts | 2970 | 0.0288636 | 0.144205 | 0.87558 | 0.444257 |
| bonus_part_correctness | category | Geography | 501 | 0.0565808 | 0.137771 | 0.88422 | 0.435015 |
| bonus_part_correctness | category | History | 4068 | 0.0144962 | 0.131341 | 0.892856 | 0.414794 |
| bonus_part_correctness | category | Literature | 4065 | 0.0330517 | 0.130529 | 0.89333 | 0.41165 |
| bonus_part_correctness | category | Mythology | 945 | 0.0230327 | 0.149722 | 0.859849 | 0.454475 |
| bonus_part_correctness | category | Other Academic | 219 | 0.0643559 | 0.14462 | 0.876627 | 0.457718 |
| bonus_part_correctness | category | Philosophy | 963 | 0.0332602 | 0.139263 | 0.878943 | 0.437441 |
| bonus_part_correctness | category | Popular Culture | 288 | 0.051988 | 0.14369 | 0.872222 | 0.429081 |
| bonus_part_correctness | category | Religion | 1008 | 0.0313658 | 0.135689 | 0.88887 | 0.420754 |
| bonus_part_correctness | category | Science | 4059 | 0.0239937 | 0.132185 | 0.891415 | 0.417952 |
| bonus_part_correctness | category | Social Science | 909 | 0.0358043 | 0.118747 | 0.912694 | 0.369418 |
| bonus_part_correctness | category | Unknown | 5580 | 0.0173618 | 0.13538 | 0.887138 | 0.423249 |
| bonus_part_correctness | difficulty | easy | 8597 | 0.0259182 | 0.0785433 | 0.789643 | 0.270985 |
| bonus_part_correctness | difficulty | hard | 8597 | 0.0375553 | 0.121029 | 0.749277 | 0.395958 |
| bonus_part_correctness | difficulty | medium | 8597 | 0.0400401 | 0.204411 | 0.750493 | 0.59794 |
