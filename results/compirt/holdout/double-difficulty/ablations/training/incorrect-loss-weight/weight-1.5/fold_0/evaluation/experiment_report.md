# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.715515 |
| log_loss | 0.499773 |
| ece | 0.0572705 |
| brier | 0.163317 |
| accuracy | 0.770199 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | 0.0049489 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.17046 |
| probability_p10 | 0.459719 |
| probability_p50 | 0.748686 |
| probability_p90 | 0.893288 |
| mean_predictive_variance | 0.177688 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.102098 |
| joint_tossup_event_log_loss | 6.63007 |
| buzz_position_mae | 0.152543 |
| buzz_position_median_absolute_error | 0.135938 |
| buzz_position_bias | -0.0426747 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.353954 |
| first_buzzer_mean_reciprocal_rank | 0.567614 |
| first_buzzer_log_loss | 1.66681 |
| first_buzzer_events | 9295 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.715515 |
| neg_average_precision | 0.446181 |
| neg_precision | 0.518791 |
| neg_recall | 0.291017 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.188231 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.0159933 |
| no_buzz_calibration_error | 0.00272364 |
| no_buzz_brier | 0.0131 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9295 | -0.0426747 | -0.0643215 |
| Q1 (0-.2) | 197 | 0.369751 | 0.368099 |
| Q2 (.2-.4) | 985 | 0.214117 | 0.208699 |
| Q3 (.4-.6) | 2251 | 0.0633213 | 0.0603149 |
| Q4 (.6-.8) | 2866 | -0.0722744 | -0.0733589 |
| Q5 (.8-1) | 2996 | -0.205543 | -0.202265 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.0572705 | 0.163317 | 0.715515 | 0.499773 |
| tossup_correctness | tier | fall | 2933 | 0.0729176 | 0.154696 | 0.712919 | 0.478857 |
| tossup_correctness | tier | nationals | 1584 | 0.0386417 | 0.176515 | 0.709888 | 0.532192 |
| tossup_correctness | tier | regionals | 1886 | 0.0512285 | 0.173386 | 0.70924 | 0.522395 |
| tossup_correctness | tier | winter | 2892 | 0.0578476 | 0.158264 | 0.720543 | 0.488476 |
| tossup_correctness | category | Current Events | 124 | 0.0889277 | 0.179712 | 0.681235 | 0.54275 |
| tossup_correctness | category | Fine Arts | 1103 | 0.0480042 | 0.164396 | 0.710479 | 0.50356 |
| tossup_correctness | category | Geography | 197 | 0.0931187 | 0.173555 | 0.785897 | 0.528858 |
| tossup_correctness | category | History | 1491 | 0.075407 | 0.15538 | 0.72384 | 0.479882 |
| tossup_correctness | category | Literature | 1472 | 0.0569773 | 0.139517 | 0.729586 | 0.444445 |
| tossup_correctness | category | Mythology | 332 | 0.0725784 | 0.146557 | 0.693787 | 0.462539 |
| tossup_correctness | category | Other Academic | 69 | 0.0662365 | 0.170981 | 0.684389 | 0.519205 |
| tossup_correctness | category | Philosophy | 324 | 0.0822276 | 0.155924 | 0.695575 | 0.48223 |
| tossup_correctness | category | Popular Culture | 102 | 0.107755 | 0.154987 | 0.442907 | 0.49589 |
| tossup_correctness | category | Religion | 372 | 0.0500791 | 0.183416 | 0.717487 | 0.543449 |
| tossup_correctness | category | Science | 1487 | 0.0611615 | 0.175173 | 0.690078 | 0.526845 |
| tossup_correctness | category | Social Science | 336 | 0.0561557 | 0.180609 | 0.726483 | 0.540834 |
| tossup_correctness | category | Unknown | 1886 | 0.0512285 | 0.173386 | 0.70924 | 0.522395 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.122894 | 0.176288 | 0.691247 | 0.544485 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.0439976 | 0.174259 | 0.715904 | 0.523993 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.0547117 | 0.165052 | 0.701159 | 0.504721 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.0588849 | 0.157448 | 0.703087 | 0.486413 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.0612605 | 0.163177 | 0.736586 | 0.497933 |
