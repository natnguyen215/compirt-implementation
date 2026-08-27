# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.667227 |
| log_loss | 0.549899 |
| ece | 0.105784 |
| brier | 0.184749 |
| accuracy | 0.719894 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.0422303 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.177595 |
| probability_p10 | 0.412096 |
| probability_p50 | 0.672174 |
| probability_p90 | 0.889638 |
| mean_predictive_variance | 0.192537 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.102317 |
| joint_tossup_event_log_loss | 6.65373 |
| buzz_position_mae | 0.156229 |
| buzz_position_median_absolute_error | 0.139128 |
| buzz_position_bias | -0.0639178 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.323766 |
| first_buzzer_mean_reciprocal_rank | 0.540484 |
| first_buzzer_log_loss | 1.72544 |
| first_buzzer_events | 9093 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.667227 |
| neg_average_precision | 0.382394 |
| neg_precision | 0.394505 |
| neg_recall | 0.331946 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.160044 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.00647949 |
| no_buzz_calibration_error | -0.0094296 |
| no_buzz_brier | 0.0150098 |
| full_pmf_max_mass_error | 1.44329e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9093 | -0.0639178 | -0.0814874 |
| Q1 (0-.2) | 167 | 0.358769 | 0.366951 |
| Q2 (.2-.4) | 912 | 0.198683 | 0.197199 |
| Q3 (.4-.6) | 2115 | 0.0466084 | 0.0420728 |
| Q4 (.6-.8) | 2844 | -0.0859233 | -0.0852414 |
| Q5 (.8-1) | 3055 | -0.22145 | -0.214615 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.105784 | 0.184749 | 0.667227 | 0.549899 |
| tossup_correctness | tier | fall | 2842 | 0.0900394 | 0.168065 | 0.690569 | 0.508998 |
| tossup_correctness | tier | nationals | 1564 | 0.0915099 | 0.197149 | 0.660282 | 0.580831 |
| tossup_correctness | tier | regionals | 1937 | 0.128384 | 0.195443 | 0.648239 | 0.575436 |
| tossup_correctness | tier | winter | 2750 | 0.114313 | 0.187407 | 0.656852 | 0.556588 |
| tossup_correctness | category | Current Events | 126 | 0.171658 | 0.198494 | 0.684323 | 0.577703 |
| tossup_correctness | category | Fine Arts | 1071 | 0.105655 | 0.179064 | 0.68199 | 0.536372 |
| tossup_correctness | category | Geography | 185 | 0.161432 | 0.203451 | 0.700305 | 0.591262 |
| tossup_correctness | category | History | 1440 | 0.0929055 | 0.186553 | 0.666516 | 0.551469 |
| tossup_correctness | category | Literature | 1422 | 0.111935 | 0.161662 | 0.660458 | 0.497735 |
| tossup_correctness | category | Mythology | 318 | 0.122862 | 0.170701 | 0.639948 | 0.52638 |
| tossup_correctness | category | Other Academic | 66 | 0.146527 | 0.181455 | 0.730123 | 0.547751 |
| tossup_correctness | category | Philosophy | 311 | 0.0983339 | 0.194739 | 0.631766 | 0.570386 |
| tossup_correctness | category | Popular Culture | 102 | 0.111196 | 0.122327 | 0.535185 | 0.411789 |
| tossup_correctness | category | Religion | 358 | 0.10052 | 0.202778 | 0.660499 | 0.593758 |
| tossup_correctness | category | Science | 1433 | 0.0936994 | 0.192597 | 0.65814 | 0.56767 |
| tossup_correctness | category | Social Science | 324 | 0.0905457 | 0.186781 | 0.704156 | 0.54974 |
| tossup_correctness | category | Unknown | 1937 | 0.128384 | 0.195443 | 0.648239 | 0.575436 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.0741232 | 0.197397 | 0.652136 | 0.590842 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.0446658 | 0.174551 | 0.70972 | 0.52996 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.0432176 | 0.164712 | 0.720563 | 0.502938 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.115564 | 0.178752 | 0.667432 | 0.53598 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.169664 | 0.206556 | 0.641817 | 0.599081 |
