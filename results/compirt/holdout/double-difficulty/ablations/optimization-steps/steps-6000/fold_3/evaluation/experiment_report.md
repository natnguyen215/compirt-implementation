# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.710089 |
| log_loss | 0.485884 |
| ece | 0.0101994 |
| brier | 0.157034 |
| accuracy | 0.786233 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | 0.0161894 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.14651 |
| probability_p10 | 0.570171 |
| probability_p50 | 0.811429 |
| probability_p90 | 0.919877 |
| mean_predictive_variance | 0.153504 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0965134 |
| joint_tossup_event_log_loss | 6.48261 |
| buzz_position_mae | 0.144199 |
| buzz_position_median_absolute_error | 0.124756 |
| buzz_position_bias | -0.029509 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.356388 |
| first_buzzer_mean_reciprocal_rank | 0.572565 |
| first_buzzer_log_loss | 1.65089 |
| first_buzzer_events | 9080 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.710089 |
| neg_average_precision | 0.449192 |
| neg_precision | 0.640535 |
| neg_recall | 0.160441 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.177644 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0124632 |
| no_buzz_calibration_error | -0.00272119 |
| no_buzz_brier | 0.0137387 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9080 | -0.029509 | -0.0524321 |
| Q1 (0-.2) | 192 | 0.396669 | 0.405186 |
| Q2 (.2-.4) | 889 | 0.219447 | 0.215698 |
| Q3 (.4-.6) | 2210 | 0.0692779 | 0.0663944 |
| Q4 (.6-.8) | 2869 | -0.0591261 | -0.0569214 |
| Q5 (.8-1) | 2920 | -0.178994 | -0.171559 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.0101994 | 0.157034 | 0.710089 | 0.485884 |
| tossup_correctness | tier | fall | 2817 | 0.0128125 | 0.153369 | 0.70226 | 0.478172 |
| tossup_correctness | tier | nationals | 1542 | 0.0256931 | 0.169455 | 0.726379 | 0.513146 |
| tossup_correctness | tier | regionals | 1934 | 0.02032 | 0.161735 | 0.717172 | 0.496535 |
| tossup_correctness | tier | winter | 2787 | 0.0227626 | 0.150604 | 0.699518 | 0.471205 |
| tossup_correctness | category | Current Events | 125 | 0.0643159 | 0.17868 | 0.754607 | 0.528031 |
| tossup_correctness | category | Fine Arts | 1072 | 0.0113531 | 0.151594 | 0.729429 | 0.472016 |
| tossup_correctness | category | Geography | 185 | 0.0568138 | 0.159942 | 0.78042 | 0.489866 |
| tossup_correctness | category | History | 1443 | 0.0226117 | 0.159997 | 0.723259 | 0.488166 |
| tossup_correctness | category | Literature | 1411 | 0.0302238 | 0.14458 | 0.661217 | 0.459492 |
| tossup_correctness | category | Mythology | 320 | 0.0429158 | 0.152485 | 0.656407 | 0.484838 |
| tossup_correctness | category | Other Academic | 64 | 0.117602 | 0.190544 | 0.639323 | 0.566639 |
| tossup_correctness | category | Philosophy | 312 | 0.0316985 | 0.148697 | 0.658 | 0.468367 |
| tossup_correctness | category | Popular Culture | 104 | 0.0546102 | 0.125255 | 0.620739 | 0.418735 |
| tossup_correctness | category | Religion | 358 | 0.0397747 | 0.179583 | 0.712637 | 0.536365 |
| tossup_correctness | category | Science | 1431 | 0.0282717 | 0.158686 | 0.701797 | 0.490798 |
| tossup_correctness | category | Social Science | 321 | 0.0308644 | 0.161936 | 0.724615 | 0.500593 |
| tossup_correctness | category | Unknown | 1934 | 0.02032 | 0.161735 | 0.717172 | 0.496535 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.0570462 | 0.18297 | 0.747813 | 0.540535 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.0276371 | 0.163323 | 0.749223 | 0.498182 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.0307157 | 0.168023 | 0.684859 | 0.514977 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.0184255 | 0.150755 | 0.694506 | 0.470943 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.0167694 | 0.151267 | 0.726726 | 0.471208 |
