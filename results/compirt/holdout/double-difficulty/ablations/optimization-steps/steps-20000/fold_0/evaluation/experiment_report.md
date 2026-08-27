# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.711173 |
| log_loss | 0.491654 |
| ece | 0.00925042 |
| brier | 0.159834 |
| accuracy | 0.777084 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | 0.0118343 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.149566 |
| probability_p10 | 0.559445 |
| probability_p50 | 0.810282 |
| probability_p90 | 0.921223 |
| mean_predictive_variance | 0.154247 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0950597 |
| joint_tossup_event_log_loss | 6.44001 |
| buzz_position_mae | 0.140167 |
| buzz_position_median_absolute_error | 0.11763 |
| buzz_position_bias | -0.00259543 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.376116 |
| first_buzzer_mean_reciprocal_rank | 0.584831 |
| first_buzzer_log_loss | 1.6217 |
| first_buzzer_events | 9295 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.711173 |
| neg_average_precision | 0.445664 |
| neg_precision | 0.589869 |
| neg_recall | 0.165445 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.181142 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.00996735 |
| no_buzz_calibration_error | -0.00330229 |
| no_buzz_brier | 0.0128541 |
| full_pmf_max_mass_error | 1.44329e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9295 | -0.00259543 | -0.0261579 |
| Q1 (0-.2) | 197 | 0.39207 | 0.39478 |
| Q2 (.2-.4) | 985 | 0.24083 | 0.236146 |
| Q3 (.4-.6) | 2251 | 0.0937241 | 0.091359 |
| Q4 (.6-.8) | 2866 | -0.0324866 | -0.0340429 |
| Q5 (.8-1) | 2996 | -0.152352 | -0.146169 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.00925042 | 0.159834 | 0.711173 | 0.491654 |
| tossup_correctness | tier | fall | 2933 | 0.0165286 | 0.148303 | 0.712083 | 0.462936 |
| tossup_correctness | tier | nationals | 1584 | 0.0381553 | 0.179029 | 0.696714 | 0.541264 |
| tossup_correctness | tier | regionals | 1886 | 0.0204834 | 0.170253 | 0.707529 | 0.515574 |
| tossup_correctness | tier | winter | 2892 | 0.0150354 | 0.154221 | 0.719072 | 0.478008 |
| tossup_correctness | category | Current Events | 124 | 0.0864141 | 0.167345 | 0.693028 | 0.516411 |
| tossup_correctness | category | Fine Arts | 1103 | 0.0221931 | 0.160261 | 0.710353 | 0.495509 |
| tossup_correctness | category | Geography | 197 | 0.0722593 | 0.169202 | 0.793124 | 0.512108 |
| tossup_correctness | category | History | 1491 | 0.022963 | 0.150353 | 0.71564 | 0.466448 |
| tossup_correctness | category | Literature | 1472 | 0.0239699 | 0.13742 | 0.730413 | 0.436828 |
| tossup_correctness | category | Mythology | 332 | 0.0416527 | 0.143095 | 0.684588 | 0.453037 |
| tossup_correctness | category | Other Academic | 69 | 0.0984355 | 0.170523 | 0.713801 | 0.510585 |
| tossup_correctness | category | Philosophy | 324 | 0.0277955 | 0.150764 | 0.672824 | 0.472138 |
| tossup_correctness | category | Popular Culture | 102 | 0.0817795 | 0.149613 | 0.441522 | 0.486479 |
| tossup_correctness | category | Religion | 372 | 0.0441663 | 0.184819 | 0.714191 | 0.546703 |
| tossup_correctness | category | Science | 1487 | 0.0272843 | 0.171558 | 0.679819 | 0.521375 |
| tossup_correctness | category | Social Science | 336 | 0.0340912 | 0.178601 | 0.724831 | 0.537835 |
| tossup_correctness | category | Unknown | 1886 | 0.0204834 | 0.170253 | 0.707529 | 0.515574 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.0561357 | 0.168713 | 0.696817 | 0.517907 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.0239895 | 0.17185 | 0.71847 | 0.518133 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.0249746 | 0.162229 | 0.692248 | 0.499529 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.016515 | 0.154581 | 0.696232 | 0.479482 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.0106021 | 0.158526 | 0.73425 | 0.486949 |
