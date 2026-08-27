# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.706841 |
| log_loss | 0.513677 |
| ece | 0.0559149 |
| brier | 0.166219 |
| accuracy | 0.766649 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | 0.0013986 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.209246 |
| probability_p10 | 0.441545 |
| probability_p50 | 0.82909 |
| probability_p90 | 0.95834 |
| mean_predictive_variance | 0.138585 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0947871 |
| joint_tossup_event_log_loss | 6.40662 |
| buzz_position_mae | 0.140909 |
| buzz_position_median_absolute_error | 0.120541 |
| buzz_position_bias | -0.0259399 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.403981 |
| first_buzzer_mean_reciprocal_rank | 0.608249 |
| first_buzzer_log_loss | 1.55604 |
| first_buzzer_events | 9295 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.706841 |
| neg_average_precision | 0.437453 |
| neg_precision | 0.505376 |
| neg_recall | 0.280018 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.175101 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.00948875 |
| no_buzz_calibration_error | -0.00378089 |
| no_buzz_brier | 0.0126108 |
| full_pmf_max_mass_error | 1.66533e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9295 | -0.0259399 | -0.0471137 |
| Q1 (0-.2) | 197 | 0.362966 | 0.359966 |
| Q2 (.2-.4) | 985 | 0.208199 | 0.195556 |
| Q3 (.4-.6) | 2251 | 0.0653147 | 0.0605363 |
| Q4 (.6-.8) | 2866 | -0.0559171 | -0.057503 |
| Q5 (.8-1) | 2996 | -0.168377 | -0.160941 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.0559149 | 0.166219 | 0.706841 | 0.513677 |
| tossup_correctness | tier | fall | 2933 | 0.0550485 | 0.15603 | 0.698766 | 0.486546 |
| tossup_correctness | tier | nationals | 1584 | 0.0571169 | 0.177816 | 0.714547 | 0.545271 |
| tossup_correctness | tier | regionals | 1886 | 0.0579484 | 0.175558 | 0.707082 | 0.538117 |
| tossup_correctness | tier | winter | 2892 | 0.0606864 | 0.164111 | 0.70664 | 0.50795 |
| tossup_correctness | category | Current Events | 124 | 0.150173 | 0.188001 | 0.654873 | 0.582032 |
| tossup_correctness | category | Fine Arts | 1103 | 0.0470718 | 0.160785 | 0.714957 | 0.500561 |
| tossup_correctness | category | Geography | 197 | 0.0924618 | 0.184859 | 0.752098 | 0.559995 |
| tossup_correctness | category | History | 1491 | 0.0453793 | 0.154549 | 0.727989 | 0.478157 |
| tossup_correctness | category | Literature | 1472 | 0.0659495 | 0.149896 | 0.702763 | 0.478101 |
| tossup_correctness | category | Mythology | 332 | 0.0622155 | 0.15347 | 0.63172 | 0.486122 |
| tossup_correctness | category | Other Academic | 69 | 0.074948 | 0.155163 | 0.774887 | 0.467644 |
| tossup_correctness | category | Philosophy | 324 | 0.0569072 | 0.152072 | 0.683279 | 0.470937 |
| tossup_correctness | category | Popular Culture | 102 | 0.095225 | 0.145525 | 0.46436 | 0.506055 |
| tossup_correctness | category | Religion | 372 | 0.0803382 | 0.199488 | 0.672384 | 0.583804 |
| tossup_correctness | category | Science | 1487 | 0.089367 | 0.180419 | 0.684634 | 0.54871 |
| tossup_correctness | category | Social Science | 336 | 0.0551071 | 0.17109 | 0.750932 | 0.528171 |
| tossup_correctness | category | Unknown | 1886 | 0.0579484 | 0.175558 | 0.707082 | 0.538117 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.0802044 | 0.166541 | 0.690716 | 0.535136 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.0689521 | 0.175308 | 0.715226 | 0.534532 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.0652893 | 0.16776 | 0.694172 | 0.519385 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.0574945 | 0.160512 | 0.701572 | 0.49781 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.0573139 | 0.167512 | 0.722741 | 0.516301 |
