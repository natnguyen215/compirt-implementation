# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.720521 |
| log_loss | 0.494261 |
| ece | 0.0765882 |
| brier | 0.16071 |
| accuracy | 0.777994 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | 0.00463862 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.162716 |
| probability_p10 | 0.467033 |
| probability_p50 | 0.719885 |
| probability_p90 | 0.888786 |
| mean_predictive_variance | 0.184667 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.110038 |
| joint_tossup_event_log_loss | 6.72094 |
| buzz_position_mae | 0.165635 |
| buzz_position_median_absolute_error | 0.1499 |
| buzz_position_bias | -0.0785735 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.345739 |
| first_buzzer_mean_reciprocal_rank | 0.55771 |
| first_buzzer_log_loss | 1.69918 |
| first_buzzer_events | 9270 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.720521 |
| neg_average_precision | 0.454465 |
| neg_precision | 0.518205 |
| neg_recall | 0.29129 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.175526 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0116924 |
| no_buzz_calibration_error | -3.47284e-05 |
| no_buzz_brier | 0.0107158 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9270 | -0.0785735 | -0.096584 |
| Q1 (0-.2) | 179 | 0.345742 | 0.34765 |
| Q2 (.2-.4) | 957 | 0.189217 | 0.181572 |
| Q3 (.4-.6) | 2203 | 0.033651 | 0.0310985 |
| Q4 (.6-.8) | 2978 | -0.106334 | -0.106629 |
| Q5 (.8-1) | 2953 | -0.246805 | -0.243928 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.0765882 | 0.16071 | 0.720521 | 0.494261 |
| tossup_correctness | tier | fall | 2876 | 0.0692704 | 0.150491 | 0.721202 | 0.468693 |
| tossup_correctness | tier | nationals | 1579 | 0.0794378 | 0.180573 | 0.711265 | 0.540656 |
| tossup_correctness | tier | regionals | 1990 | 0.094067 | 0.163405 | 0.737271 | 0.501566 |
| tossup_correctness | tier | winter | 2825 | 0.0745298 | 0.158113 | 0.70622 | 0.489214 |
| tossup_correctness | category | Current Events | 123 | 0.117953 | 0.161164 | 0.77036 | 0.490492 |
| tossup_correctness | category | Fine Arts | 1093 | 0.0677804 | 0.156954 | 0.726525 | 0.486267 |
| tossup_correctness | category | Geography | 191 | 0.087817 | 0.16922 | 0.763867 | 0.516538 |
| tossup_correctness | category | History | 1469 | 0.0569467 | 0.167649 | 0.719304 | 0.508326 |
| tossup_correctness | category | Literature | 1436 | 0.077888 | 0.144862 | 0.701671 | 0.456652 |
| tossup_correctness | category | Mythology | 325 | 0.118842 | 0.145213 | 0.65214 | 0.458011 |
| tossup_correctness | category | Other Academic | 67 | 0.184811 | 0.197124 | 0.59973 | 0.576011 |
| tossup_correctness | category | Philosophy | 322 | 0.0699084 | 0.160126 | 0.691642 | 0.490928 |
| tossup_correctness | category | Popular Culture | 100 | 0.130474 | 0.129077 | 0.409602 | 0.428151 |
| tossup_correctness | category | Religion | 365 | 0.0562644 | 0.18777 | 0.681781 | 0.55965 |
| tossup_correctness | category | Science | 1456 | 0.0813892 | 0.162638 | 0.719048 | 0.499329 |
| tossup_correctness | category | Social Science | 333 | 0.0908657 | 0.169388 | 0.750389 | 0.513779 |
| tossup_correctness | category | Unknown | 1990 | 0.094067 | 0.163405 | 0.737271 | 0.501566 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.128612 | 0.181994 | 0.69801 | 0.544841 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.0935397 | 0.1737 | 0.702358 | 0.52608 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.0710156 | 0.163249 | 0.719662 | 0.500372 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.0773016 | 0.154974 | 0.719004 | 0.480247 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.0742829 | 0.1591 | 0.729502 | 0.490458 |
