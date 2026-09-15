# Frozen Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.891441 |
| log_loss | 0.416593 |
| ece | 0.0195634 |
| brier | 0.133171 |
| part_accuracy | 0.809164 |
| part_all_correct_accuracy | 0.518437 |
| accuracy_lift_over_all_correct | 0.290727 |
| part_accuracy_macro_team | 0.809183 |
| part_accuracy_macro_bonus | 0.80652 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.34446 |
| probability_p10 | 0.0556049 |
| probability_p50 | 0.53525 |
| probability_p90 | 0.956073 |
| mean_predictive_variance | 0.130762 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.512201 |
| ranked_probability_score | 0.11697 |
| bonus_total_score_log_loss | 1.0224 |
| ppb_mae | 2.35188 |
| ranked_probability_score_responses | 8606 |
| bonus_total_score_log_loss_responses | 8606 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in the diagnostic CSVs under `csvs/`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part_correctness | aggregate | all | 25818 | 0.0195634 | 0.133171 | 0.891441 | 0.416593 |
| bonus_part_correctness | tier | fall | 8415 | 0.0222046 | 0.135177 | 0.885355 | 0.417159 |
| bonus_part_correctness | tier | nationals | 4179 | 0.0483447 | 0.132577 | 0.889733 | 0.418639 |
| bonus_part_correctness | tier | regionals | 5070 | 0.0219192 | 0.133201 | 0.890793 | 0.417262 |
| bonus_part_correctness | tier | winter | 8154 | 0.0187211 | 0.131386 | 0.892735 | 0.414546 |
| bonus_part_correctness | category | Current Events | 258 | 0.0578499 | 0.100022 | 0.931671 | 0.341814 |
| bonus_part_correctness | category | Fine Arts | 3075 | 0.0218588 | 0.142047 | 0.877131 | 0.44147 |
| bonus_part_correctness | category | Geography | 453 | 0.0423496 | 0.132601 | 0.888873 | 0.416819 |
| bonus_part_correctness | category | History | 4176 | 0.0269624 | 0.134912 | 0.889207 | 0.417894 |
| bonus_part_correctness | category | Literature | 4197 | 0.0272381 | 0.123226 | 0.90564 | 0.390233 |
| bonus_part_correctness | category | Mythology | 951 | 0.0349584 | 0.143797 | 0.869858 | 0.439493 |
| bonus_part_correctness | category | Other Academic | 258 | 0.0407881 | 0.117736 | 0.911915 | 0.380033 |
| bonus_part_correctness | category | Philosophy | 969 | 0.0294812 | 0.143013 | 0.876247 | 0.441661 |
| bonus_part_correctness | category | Popular Culture | 303 | 0.0846577 | 0.153365 | 0.860037 | 0.447551 |
| bonus_part_correctness | category | Religion | 1041 | 0.042639 | 0.131735 | 0.894028 | 0.416998 |
| bonus_part_correctness | category | Science | 4152 | 0.021443 | 0.131977 | 0.891778 | 0.415102 |
| bonus_part_correctness | category | Social Science | 915 | 0.0381724 | 0.133716 | 0.88854 | 0.421258 |
| bonus_part_correctness | category | Unknown | 5070 | 0.0219192 | 0.133201 | 0.890793 | 0.417262 |

## Distributions

[Evaluated probabilities, aggregate ability, and synergy contributions](graphs/bonus/bonus_prediction_distributions.png). Aggregate ability is part-weighted; synergy is response-weighted.

[Fitted bonus parameters](graphs/parameters/bonus_part_parameter_distributions.png) describe the training fit. These distributions are across entities, not posterior uncertainty intervals.
