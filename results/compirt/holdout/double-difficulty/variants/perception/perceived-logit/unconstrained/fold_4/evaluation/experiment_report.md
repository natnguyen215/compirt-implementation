# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.548516 |
| log_loss | 0.594461 |
| ece | 0.100641 |
| brier | 0.185733 |
| accuracy | 0.773679 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | 0.000323625 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.0921651 |
| probability_p10 | 0.743276 |
| probability_p50 | 0.892975 |
| probability_p90 | 0.95256 |
| mean_predictive_variance | 0.107189 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.174394 |
| joint_tossup_event_log_loss | 7.78902 |
| buzz_position_mae | 0.340424 |
| buzz_position_median_absolute_error | 0.343535 |
| buzz_position_bias | -0.328039 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.354153 |
| first_buzzer_mean_reciprocal_rank | 0.565077 |
| first_buzzer_log_loss | 1.67743 |
| first_buzzer_events | 9270 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.548516 |
| neg_average_precision | 0.271099 |
| neg_precision | 0.533333 |
| neg_recall | 0.0114231 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0284576 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.238101 |
| no_buzz_calibration_error | 0.226374 |
| no_buzz_brier | 0.0736556 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9270 | -0.328039 | -0.343535 |
| Q1 (0-.2) | 179 | 0.168668 | 0.167751 |
| Q2 (.2-.4) | 957 | 0.00577369 | 0.00195603 |
| Q3 (.4-.6) | 2203 | -0.174933 | -0.178593 |
| Q4 (.6-.8) | 2978 | -0.355271 | -0.354298 |
| Q5 (.8-1) | 2953 | -0.553087 | -0.555293 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.100641 | 0.185733 | 0.548516 | 0.594461 |
| tossup_correctness | tier | fall | 2876 | 0.0935168 | 0.172119 | 0.534589 | 0.554363 |
| tossup_correctness | tier | nationals | 1579 | 0.117152 | 0.210109 | 0.571443 | 0.654171 |
| tossup_correctness | tier | regionals | 1990 | 0.107632 | 0.192074 | 0.53182 | 0.613936 |
| tossup_correctness | tier | winter | 2825 | 0.109028 | 0.1815 | 0.55217 | 0.58819 |
| tossup_correctness | category | Current Events | 123 | 0.105167 | 0.188138 | 0.578136 | 0.583559 |
| tossup_correctness | category | Fine Arts | 1093 | 0.129833 | 0.190734 | 0.54845 | 0.614956 |
| tossup_correctness | category | Geography | 191 | 0.16773 | 0.226043 | 0.646379 | 0.67724 |
| tossup_correctness | category | History | 1469 | 0.106086 | 0.193875 | 0.552641 | 0.611081 |
| tossup_correctness | category | Literature | 1436 | 0.0801582 | 0.157623 | 0.532478 | 0.526028 |
| tossup_correctness | category | Mythology | 325 | 0.059613 | 0.136337 | 0.566767 | 0.454061 |
| tossup_correctness | category | Other Academic | 67 | 0.133047 | 0.170934 | 0.533693 | 0.551695 |
| tossup_correctness | category | Philosophy | 322 | 0.127087 | 0.185284 | 0.4998 | 0.609823 |
| tossup_correctness | category | Popular Culture | 100 | 0.034444 | 0.103306 | 0.533197 | 0.367027 |
| tossup_correctness | category | Religion | 365 | 0.157166 | 0.22225 | 0.555768 | 0.700317 |
| tossup_correctness | category | Science | 1456 | 0.0965438 | 0.187692 | 0.555515 | 0.591019 |
| tossup_correctness | category | Social Science | 333 | 0.149686 | 0.220489 | 0.537952 | 0.687238 |
| tossup_correctness | category | Unknown | 1990 | 0.107632 | 0.192074 | 0.53182 | 0.613936 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.0920792 | 0.188868 | 0.544942 | 0.59311 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.109938 | 0.201983 | 0.473725 | 0.637432 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.0990933 | 0.189901 | 0.541874 | 0.596133 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.086616 | 0.173484 | 0.569699 | 0.557802 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.116088 | 0.189518 | 0.553207 | 0.616339 |
