# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.712858 |
| log_loss | 0.509388 |
| ece | 0.0691841 |
| brier | 0.166773 |
| accuracy | 0.761478 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.00270066 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.197918 |
| probability_p10 | 0.427237 |
| probability_p50 | 0.740351 |
| probability_p90 | 0.941087 |
| mean_predictive_variance | 0.1679 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0957094 |
| joint_tossup_event_log_loss | 6.49792 |
| buzz_position_mae | 0.139434 |
| buzz_position_median_absolute_error | 0.117109 |
| buzz_position_bias | -0.000495518 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.385114 |
| first_buzzer_mean_reciprocal_rank | 0.592452 |
| first_buzzer_log_loss | 1.5996 |
| first_buzzer_events | 9257 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.712858 |
| neg_average_precision | 0.450081 |
| neg_precision | 0.491771 |
| neg_recall | 0.34219 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.131641 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0594064 |
| no_buzz_calibration_error | 0.0462934 |
| no_buzz_brier | 0.0215523 |
| full_pmf_max_mass_error | 1.44329e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9257 | -0.000495518 | -0.0204781 |
| Q1 (0-.2) | 183 | 0.403828 | 0.416677 |
| Q2 (.2-.4) | 955 | 0.239214 | 0.237183 |
| Q3 (.4-.6) | 2239 | 0.09517 | 0.0928017 |
| Q4 (.6-.8) | 2875 | -0.0230423 | -0.0219694 |
| Q5 (.8-1) | 3005 | -0.151007 | -0.144273 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.0691841 | 0.166773 | 0.712858 | 0.509388 |
| tossup_correctness | tier | fall | 2798 | 0.063312 | 0.152166 | 0.734459 | 0.473798 |
| tossup_correctness | tier | nationals | 1545 | 0.0748519 | 0.185243 | 0.711329 | 0.549669 |
| tossup_correctness | tier | regionals | 2039 | 0.0816182 | 0.173807 | 0.690967 | 0.527621 |
| tossup_correctness | tier | winter | 2875 | 0.0638394 | 0.166075 | 0.702283 | 0.509446 |
| tossup_correctness | category | Current Events | 129 | 0.109345 | 0.200779 | 0.706869 | 0.580087 |
| tossup_correctness | category | Fine Arts | 1074 | 0.0932181 | 0.173446 | 0.681615 | 0.527024 |
| tossup_correctness | category | Geography | 180 | 0.073434 | 0.18362 | 0.770727 | 0.543571 |
| tossup_correctness | category | History | 1454 | 0.0693993 | 0.165048 | 0.722104 | 0.506859 |
| tossup_correctness | category | Literature | 1435 | 0.0631879 | 0.145393 | 0.710583 | 0.461314 |
| tossup_correctness | category | Mythology | 324 | 0.0786694 | 0.156992 | 0.677333 | 0.492797 |
| tossup_correctness | category | Other Academic | 71 | 0.108164 | 0.184262 | 0.643791 | 0.557182 |
| tossup_correctness | category | Philosophy | 310 | 0.0688732 | 0.164644 | 0.73202 | 0.49583 |
| tossup_correctness | category | Popular Culture | 108 | 0.150263 | 0.123583 | 0.484375 | 0.425971 |
| tossup_correctness | category | Religion | 361 | 0.10534 | 0.184703 | 0.69736 | 0.55004 |
| tossup_correctness | category | Science | 1445 | 0.045779 | 0.167571 | 0.737641 | 0.505007 |
| tossup_correctness | category | Social Science | 327 | 0.0778014 | 0.178658 | 0.735846 | 0.534217 |
| tossup_correctness | category | Unknown | 2039 | 0.0816182 | 0.173807 | 0.690967 | 0.527621 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.174195 | 0.196887 | 0.74562 | 0.579657 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.109812 | 0.186443 | 0.711656 | 0.558504 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.0675001 | 0.169504 | 0.724755 | 0.514384 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.0635921 | 0.159148 | 0.706329 | 0.487884 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.0573242 | 0.163949 | 0.709108 | 0.50635 |
