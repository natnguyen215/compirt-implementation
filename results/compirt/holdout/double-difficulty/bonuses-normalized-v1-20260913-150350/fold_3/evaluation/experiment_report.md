# Frozen Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.889611 |
| log_loss | 0.42007 |
| ece | 0.0233364 |
| brier | 0.134273 |
| part_accuracy | 0.80686 |
| part_all_correct_accuracy | 0.525685 |
| accuracy_lift_over_all_correct | 0.281175 |
| part_accuracy_macro_team | 0.809365 |
| part_accuracy_macro_bonus | 0.807186 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.34092 |
| probability_p10 | 0.0609047 |
| probability_p50 | 0.548612 |
| probability_p90 | 0.956359 |
| mean_predictive_variance | 0.132814 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.508338 |
| ranked_probability_score | 0.119254 |
| bonus_total_score_log_loss | 1.04185 |
| ppb_mae | 2.36139 |
| ranked_probability_score_responses | 8455 |
| bonus_total_score_log_loss_responses | 8455 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in the diagnostic CSVs under `csvs/`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part_correctness | aggregate | all | 25365 | 0.0233364 | 0.134273 | 0.889611 | 0.42007 |
| bonus_part_correctness | tier | fall | 8094 | 0.0257073 | 0.136843 | 0.882958 | 0.424858 |
| bonus_part_correctness | tier | nationals | 4125 | 0.0357331 | 0.138093 | 0.879727 | 0.434666 |
| bonus_part_correctness | tier | regionals | 5247 | 0.0346322 | 0.13575 | 0.888803 | 0.423432 |
| bonus_part_correctness | tier | winter | 7899 | 0.0223344 | 0.128662 | 0.897563 | 0.405307 |
| bonus_part_correctness | category | Current Events | 243 | 0.0605234 | 0.130413 | 0.89336 | 0.419864 |
| bonus_part_correctness | category | Fine Arts | 2937 | 0.0312135 | 0.145998 | 0.870161 | 0.453209 |
| bonus_part_correctness | category | Geography | 456 | 0.0418582 | 0.129958 | 0.89105 | 0.4055 |
| bonus_part_correctness | category | History | 4050 | 0.0201205 | 0.130565 | 0.894399 | 0.409703 |
| bonus_part_correctness | category | Literature | 4029 | 0.0211745 | 0.133187 | 0.890324 | 0.417582 |
| bonus_part_correctness | category | Mythology | 936 | 0.0493923 | 0.131506 | 0.891965 | 0.406216 |
| bonus_part_correctness | category | Other Academic | 255 | 0.0732485 | 0.105488 | 0.923344 | 0.356001 |
| bonus_part_correctness | category | Philosophy | 948 | 0.0368073 | 0.149721 | 0.865085 | 0.454417 |
| bonus_part_correctness | category | Popular Culture | 285 | 0.0724731 | 0.13531 | 0.892778 | 0.41275 |
| bonus_part_correctness | category | Religion | 1014 | 0.0339695 | 0.128341 | 0.896473 | 0.409574 |
| bonus_part_correctness | category | Science | 4059 | 0.0220878 | 0.132827 | 0.890628 | 0.418288 |
| bonus_part_correctness | category | Social Science | 906 | 0.0351483 | 0.119899 | 0.910851 | 0.376392 |
| bonus_part_correctness | category | Unknown | 5247 | 0.0346322 | 0.13575 | 0.888803 | 0.423432 |

## Distributions

[Evaluated probabilities, aggregate ability, and synergy contributions](graphs/bonus/bonus_prediction_distributions.png). Aggregate ability is part-weighted; synergy is response-weighted.

[Fitted bonus parameters](graphs/parameters/bonus_part_parameter_distributions.png) describe the training fit. These distributions are across entities, not posterior uncertainty intervals.
