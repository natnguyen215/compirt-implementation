# Frozen Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.897054 |
| log_loss | 0.407488 |
| ece | 0.0216992 |
| brier | 0.129202 |
| part_accuracy | 0.816677 |
| part_all_correct_accuracy | 0.525685 |
| accuracy_lift_over_all_correct | 0.290992 |
| part_accuracy_macro_team | 0.819098 |
| part_accuracy_macro_bonus | 0.817182 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.348319 |
| probability_p10 | 0.0567198 |
| probability_p50 | 0.557923 |
| probability_p90 | 0.965891 |
| mean_predictive_variance | 0.127482 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.529154 |
| ranked_probability_score | 0.113688 |
| bonus_total_score_log_loss | 1.00741 |
| ppb_mae | 1.72069 |
| ranked_probability_score_responses | 8455 |
| bonus_total_score_log_loss_responses | 8455 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in the diagnostic CSVs under `csvs/`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part_correctness | aggregate | all | 25365 | 0.0216992 | 0.129202 | 0.897054 | 0.407488 |
| bonus_part_correctness | tier | fall | 8094 | 0.0278915 | 0.135999 | 0.884716 | 0.426342 |
| bonus_part_correctness | tier | nationals | 4125 | 0.023533 | 0.129445 | 0.894105 | 0.409815 |
| bonus_part_correctness | tier | regionals | 5247 | 0.026903 | 0.127256 | 0.899465 | 0.402875 |
| bonus_part_correctness | tier | winter | 7899 | 0.0238958 | 0.123402 | 0.906207 | 0.390016 |
| bonus_part_correctness | category | Current Events | 243 | 0.059747 | 0.140006 | 0.88374 | 0.437587 |
| bonus_part_correctness | category | Fine Arts | 2937 | 0.0396276 | 0.139331 | 0.881357 | 0.437038 |
| bonus_part_correctness | category | Geography | 456 | 0.0371733 | 0.129598 | 0.892114 | 0.402087 |
| bonus_part_correctness | category | History | 4050 | 0.020787 | 0.126609 | 0.900296 | 0.3982 |
| bonus_part_correctness | category | Literature | 4029 | 0.0196316 | 0.12502 | 0.901937 | 0.398297 |
| bonus_part_correctness | category | Mythology | 936 | 0.0461641 | 0.130548 | 0.892827 | 0.406358 |
| bonus_part_correctness | category | Other Academic | 255 | 0.0389135 | 0.104734 | 0.92843 | 0.342759 |
| bonus_part_correctness | category | Philosophy | 948 | 0.0217788 | 0.135868 | 0.888191 | 0.418786 |
| bonus_part_correctness | category | Popular Culture | 285 | 0.0694766 | 0.147971 | 0.877121 | 0.449223 |
| bonus_part_correctness | category | Religion | 1014 | 0.0383174 | 0.124802 | 0.901531 | 0.401606 |
| bonus_part_correctness | category | Science | 4059 | 0.0237137 | 0.133118 | 0.891455 | 0.419319 |
| bonus_part_correctness | category | Social Science | 906 | 0.0363826 | 0.114718 | 0.918556 | 0.363454 |
| bonus_part_correctness | category | Unknown | 5247 | 0.026903 | 0.127256 | 0.899465 | 0.402875 |

## Distributions

[Evaluated probabilities, aggregate ability, and synergy contributions](graphs/bonus/bonus_prediction_distributions.png). Aggregate ability is part-weighted; synergy is response-weighted.

[Fitted bonus parameters](graphs/parameters/bonus_part_parameter_distributions.png) describe the training fit. These distributions are across entities, not posterior uncertainty intervals.

[Synergy parameters](graphs/parameters/synergy_parameter_distributions.png).
