# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.714192 |
| log_loss | 0.499304 |
| ece | 0.0407638 |
| brier | 0.161098 |
| accuracy | 0.775148 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | 0.00989779 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.187004 |
| probability_p10 | 0.474689 |
| probability_p50 | 0.781274 |
| probability_p90 | 0.949444 |
| mean_predictive_variance | 0.15655 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0936274 |
| joint_tossup_event_log_loss | 6.38816 |
| buzz_position_mae | 0.135259 |
| buzz_position_median_absolute_error | 0.109026 |
| buzz_position_bias | 0.010576 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.401076 |
| first_buzzer_mean_reciprocal_rank | 0.605051 |
| first_buzzer_log_loss | 1.57064 |
| first_buzzer_events | 9295 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.714192 |
| neg_average_precision | 0.456558 |
| neg_precision | 0.541894 |
| neg_recall | 0.272686 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.190229 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.00963837 |
| no_buzz_calibration_error | -0.00363127 |
| no_buzz_brier | 0.0126433 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9295 | 0.010576 | -0.0118029 |
| Q1 (0-.2) | 197 | 0.387722 | 0.383707 |
| Q2 (.2-.4) | 985 | 0.237213 | 0.232289 |
| Q3 (.4-.6) | 2251 | 0.0998904 | 0.0933627 |
| Q4 (.6-.8) | 2866 | -0.0184229 | -0.0189763 |
| Q5 (.8-1) | 2996 | -0.128099 | -0.117928 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.0407638 | 0.161098 | 0.714192 | 0.499304 |
| tossup_correctness | tier | fall | 2933 | 0.0545478 | 0.15116 | 0.708267 | 0.477129 |
| tossup_correctness | tier | nationals | 1584 | 0.0515887 | 0.177911 | 0.711686 | 0.537607 |
| tossup_correctness | tier | regionals | 1886 | 0.0382063 | 0.170118 | 0.713909 | 0.522218 |
| tossup_correctness | tier | winter | 2892 | 0.039001 | 0.156085 | 0.714331 | 0.48587 |
| tossup_correctness | category | Current Events | 124 | 0.123708 | 0.184292 | 0.669788 | 0.566576 |
| tossup_correctness | category | Fine Arts | 1103 | 0.0459587 | 0.158766 | 0.720885 | 0.494221 |
| tossup_correctness | category | Geography | 197 | 0.100908 | 0.171033 | 0.791375 | 0.535302 |
| tossup_correctness | category | History | 1491 | 0.0528422 | 0.151869 | 0.72304 | 0.471032 |
| tossup_correctness | category | Literature | 1472 | 0.0564217 | 0.141137 | 0.708436 | 0.456166 |
| tossup_correctness | category | Mythology | 332 | 0.0698753 | 0.149541 | 0.663859 | 0.475101 |
| tossup_correctness | category | Other Academic | 69 | 0.155699 | 0.175567 | 0.674208 | 0.52205 |
| tossup_correctness | category | Philosophy | 324 | 0.0502321 | 0.148971 | 0.712266 | 0.457426 |
| tossup_correctness | category | Popular Culture | 102 | 0.121854 | 0.153254 | 0.424913 | 0.528813 |
| tossup_correctness | category | Religion | 372 | 0.0687683 | 0.193274 | 0.676768 | 0.566585 |
| tossup_correctness | category | Science | 1487 | 0.054508 | 0.171624 | 0.694907 | 0.522942 |
| tossup_correctness | category | Social Science | 336 | 0.0837599 | 0.172451 | 0.7425 | 0.527444 |
| tossup_correctness | category | Unknown | 1886 | 0.0382063 | 0.170118 | 0.713909 | 0.522218 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.143602 | 0.17426 | 0.711671 | 0.534456 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.0528934 | 0.173961 | 0.715962 | 0.525949 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.0474845 | 0.163844 | 0.701924 | 0.505345 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.04949 | 0.155694 | 0.696353 | 0.491584 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.0256781 | 0.159109 | 0.736671 | 0.491078 |
