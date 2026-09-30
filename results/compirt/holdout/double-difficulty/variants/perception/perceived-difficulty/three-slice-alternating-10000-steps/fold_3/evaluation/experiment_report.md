# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.613718 |
| log_loss | 0.657518 |
| ece | 0.221213 |
| brier | 0.231148 |
| accuracy | 0.628194 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | -0.14185 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.174433 |
| probability_p10 | 0.303068 |
| probability_p50 | 0.564488 |
| probability_p90 | 0.766667 |
| mean_predictive_variance | 0.217189 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0933317 |
| joint_tossup_event_log_loss | 6.70487 |
| buzz_position_mae | 0.137421 |
| buzz_position_median_absolute_error | 0.113318 |
| buzz_position_bias | -0.00585544 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.373568 |
| first_buzzer_mean_reciprocal_rank | 0.582354 |
| first_buzzer_log_loss | 1.64313 |
| first_buzzer_events | 9080 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.613718 |
| neg_average_precision | 0.316013 |
| neg_precision | 0.304374 |
| neg_recall | 0.479885 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.139138 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0484018 |
| no_buzz_calibration_error | 0.0332174 |
| no_buzz_brier | 0.0184381 |
| full_pmf_max_mass_error | 1.22125e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9080 | -0.00585544 | -0.0257133 |
| Q1 (0-.2) | 192 | 0.402525 | 0.409297 |
| Q2 (.2-.4) | 889 | 0.230206 | 0.226826 |
| Q3 (.4-.6) | 2210 | 0.0868246 | 0.0828119 |
| Q4 (.6-.8) | 2869 | -0.0320865 | -0.0292421 |
| Q5 (.8-1) | 2920 | -0.148949 | -0.139182 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.221213 | 0.231148 | 0.613718 | 0.657518 |
| tossup_correctness | tier | fall | 2817 | 0.246388 | 0.237806 | 0.606045 | 0.674905 |
| tossup_correctness | tier | nationals | 1542 | 0.215923 | 0.247567 | 0.588595 | 0.691276 |
| tossup_correctness | tier | regionals | 1934 | 0.174629 | 0.220425 | 0.620538 | 0.633827 |
| tossup_correctness | tier | winter | 2787 | 0.231022 | 0.222775 | 0.630658 | 0.637706 |
| tossup_correctness | category | Current Events | 125 | 0.254361 | 0.268802 | 0.571253 | 0.743675 |
| tossup_correctness | category | Fine Arts | 1072 | 0.21341 | 0.228744 | 0.595514 | 0.649761 |
| tossup_correctness | category | Geography | 185 | 0.234449 | 0.271581 | 0.580699 | 0.745967 |
| tossup_correctness | category | History | 1443 | 0.26632 | 0.247837 | 0.636409 | 0.694047 |
| tossup_correctness | category | Literature | 1411 | 0.212481 | 0.207849 | 0.593935 | 0.605281 |
| tossup_correctness | category | Mythology | 320 | 0.24553 | 0.23583 | 0.585361 | 0.667733 |
| tossup_correctness | category | Other Academic | 64 | 0.233178 | 0.236484 | 0.602865 | 0.665054 |
| tossup_correctness | category | Philosophy | 312 | 0.231491 | 0.211244 | 0.640129 | 0.610877 |
| tossup_correctness | category | Popular Culture | 104 | 0.402952 | 0.316606 | 0.546875 | 0.862028 |
| tossup_correctness | category | Religion | 358 | 0.221369 | 0.24223 | 0.642111 | 0.680913 |
| tossup_correctness | category | Science | 1431 | 0.229939 | 0.23745 | 0.609266 | 0.673709 |
| tossup_correctness | category | Social Science | 321 | 0.225165 | 0.238681 | 0.631799 | 0.67615 |
| tossup_correctness | category | Unknown | 1934 | 0.174629 | 0.220425 | 0.620538 | 0.633827 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.258845 | 0.255994 | 0.700721 | 0.714086 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.251518 | 0.25666 | 0.628058 | 0.713798 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.23693 | 0.239637 | 0.631399 | 0.67835 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.2322 | 0.226301 | 0.617502 | 0.646521 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.186876 | 0.220085 | 0.580409 | 0.631702 |
