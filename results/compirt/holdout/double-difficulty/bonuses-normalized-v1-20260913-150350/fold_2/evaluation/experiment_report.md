# Frozen Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.888976 |
| log_loss | 0.42114 |
| ece | 0.0202859 |
| brier | 0.134456 |
| part_accuracy | 0.807181 |
| part_all_correct_accuracy | 0.519367 |
| accuracy_lift_over_all_correct | 0.287814 |
| part_accuracy_macro_team | 0.810567 |
| part_accuracy_macro_bonus | 0.804731 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.344813 |
| probability_p10 | 0.0528301 |
| probability_p50 | 0.527759 |
| probability_p90 | 0.95619 |
| mean_predictive_variance | 0.130728 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.509131 |
| ranked_probability_score | 0.116926 |
| bonus_total_score_log_loss | 1.02658 |
| ppb_mae | 2.29287 |
| ranked_probability_score_responses | 8597 |
| bonus_total_score_log_loss_responses | 8597 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in the diagnostic CSVs under `csvs/`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part_correctness | aggregate | all | 25791 | 0.0202859 | 0.134456 | 0.888976 | 0.42114 |
| bonus_part_correctness | tier | fall | 7995 | 0.0250118 | 0.12844 | 0.896476 | 0.399748 |
| bonus_part_correctness | tier | nationals | 4095 | 0.0267983 | 0.13594 | 0.882154 | 0.428314 |
| bonus_part_correctness | tier | regionals | 5580 | 0.0202673 | 0.136198 | 0.88588 | 0.425235 |
| bonus_part_correctness | tier | winter | 8121 | 0.0202618 | 0.138433 | 0.882326 | 0.435768 |
| bonus_part_correctness | category | Current Events | 216 | 0.0675549 | 0.11951 | 0.907706 | 0.382352 |
| bonus_part_correctness | category | Fine Arts | 2970 | 0.0261119 | 0.144213 | 0.874892 | 0.446894 |
| bonus_part_correctness | category | Geography | 501 | 0.0653019 | 0.134876 | 0.892181 | 0.428562 |
| bonus_part_correctness | category | History | 4068 | 0.0180266 | 0.129968 | 0.895297 | 0.409976 |
| bonus_part_correctness | category | Literature | 4065 | 0.0268338 | 0.129657 | 0.895163 | 0.408637 |
| bonus_part_correctness | category | Mythology | 945 | 0.0307706 | 0.149897 | 0.858648 | 0.459304 |
| bonus_part_correctness | category | Other Academic | 219 | 0.074532 | 0.145007 | 0.875042 | 0.452849 |
| bonus_part_correctness | category | Philosophy | 963 | 0.034677 | 0.139445 | 0.879176 | 0.437518 |
| bonus_part_correctness | category | Popular Culture | 288 | 0.0835045 | 0.141534 | 0.876029 | 0.428727 |
| bonus_part_correctness | category | Religion | 1008 | 0.0401601 | 0.134554 | 0.891051 | 0.417062 |
| bonus_part_correctness | category | Science | 4059 | 0.0294516 | 0.132782 | 0.890472 | 0.419263 |
| bonus_part_correctness | category | Social Science | 909 | 0.0472555 | 0.117991 | 0.913981 | 0.368681 |
| bonus_part_correctness | category | Unknown | 5580 | 0.0202673 | 0.136198 | 0.88588 | 0.425235 |

## Distributions

[Evaluated probabilities, aggregate ability, and synergy contributions](graphs/bonus/bonus_prediction_distributions.png). Aggregate ability is part-weighted; synergy is response-weighted.

[Fitted bonus parameters](graphs/parameters/bonus_part_parameter_distributions.png) describe the training fit. These distributions are across entities, not posterior uncertainty intervals.
