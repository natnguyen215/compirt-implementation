# Frozen Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.891023 |
| log_loss | 0.417147 |
| ece | 0.0233032 |
| brier | 0.13338 |
| part_accuracy | 0.809026 |
| part_all_correct_accuracy | 0.519002 |
| accuracy_lift_over_all_correct | 0.290024 |
| part_accuracy_macro_team | 0.812057 |
| part_accuracy_macro_bonus | 0.805723 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.343838 |
| probability_p10 | 0.0587158 |
| probability_p50 | 0.542228 |
| probability_p90 | 0.957796 |
| mean_predictive_variance | 0.131007 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.515202 |
| ranked_probability_score | 0.115706 |
| bonus_total_score_log_loss | 1.01345 |
| ppb_mae | 2.41632 |
| ranked_probability_score_responses | 8420 |
| bonus_total_score_log_loss_responses | 8420 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in the diagnostic CSVs under `csvs/`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part_correctness | aggregate | all | 25260 | 0.0233032 | 0.13338 | 0.891023 | 0.417147 |
| bonus_part_correctness | tier | fall | 8160 | 0.0193744 | 0.132944 | 0.886842 | 0.413321 |
| bonus_part_correctness | tier | nationals | 4107 | 0.0382807 | 0.131175 | 0.891366 | 0.414498 |
| bonus_part_correctness | tier | regionals | 5280 | 0.0366536 | 0.141381 | 0.879643 | 0.437088 |
| bonus_part_correctness | tier | winter | 7713 | 0.0290083 | 0.129537 | 0.894982 | 0.408955 |
| bonus_part_correctness | category | Current Events | 249 | 0.078478 | 0.122212 | 0.902893 | 0.395959 |
| bonus_part_correctness | category | Fine Arts | 2934 | 0.0163961 | 0.141632 | 0.877044 | 0.440824 |
| bonus_part_correctness | category | Geography | 459 | 0.0632518 | 0.132961 | 0.88328 | 0.416087 |
| bonus_part_correctness | category | History | 4017 | 0.0272422 | 0.128774 | 0.898324 | 0.402537 |
| bonus_part_correctness | category | Literature | 4047 | 0.029497 | 0.12711 | 0.898568 | 0.402674 |
| bonus_part_correctness | category | Mythology | 924 | 0.0323469 | 0.141037 | 0.872785 | 0.434644 |
| bonus_part_correctness | category | Other Academic | 237 | 0.0712301 | 0.119662 | 0.920767 | 0.382916 |
| bonus_part_correctness | category | Philosophy | 948 | 0.0442088 | 0.136013 | 0.885542 | 0.429332 |
| bonus_part_correctness | category | Popular Culture | 294 | 0.0659048 | 0.128562 | 0.890941 | 0.39487 |
| bonus_part_correctness | category | Religion | 984 | 0.0285906 | 0.124977 | 0.901904 | 0.39906 |
| bonus_part_correctness | category | Science | 3990 | 0.0276538 | 0.132832 | 0.892535 | 0.414899 |
| bonus_part_correctness | category | Social Science | 897 | 0.0368335 | 0.117709 | 0.911224 | 0.374766 |
| bonus_part_correctness | category | Unknown | 5280 | 0.0366536 | 0.141381 | 0.879643 | 0.437088 |

## Distributions

[Evaluated probabilities, aggregate ability, and synergy contributions](graphs/bonus/bonus_prediction_distributions.png). Aggregate ability is part-weighted; synergy is response-weighted.

[Fitted bonus parameters](graphs/parameters/bonus_part_parameter_distributions.png) describe the training fit. These distributions are across entities, not posterior uncertainty intervals.
