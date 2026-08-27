# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.707779 |
| log_loss | 0.498623 |
| ece | 0.0180801 |
| brier | 0.162417 |
| accuracy | 0.770981 |
| all_correct_accuracy | 0.761865 |
| accuracy_lift_over_all_correct | 0.0091152 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.14743 |
| probability_p10 | 0.569162 |
| probability_p50 | 0.81452 |
| probability_p90 | 0.92482 |
| mean_predictive_variance | 0.152246 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0895238 |
| joint_tossup_event_log_loss | 5.5266 |
| buzz_position_mae | 0.158461 |
| buzz_position_median_absolute_error | 0.140826 |
| buzz_position_bias | -0.0503752 |
| survival_events | 31725 |
| joint_tossup_event_log_loss_events | 31725 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.33239 |
| first_buzzer_mean_reciprocal_rank | 0.547817 |
| first_buzzer_log_loss | 1.71447 |
| first_buzzer_events | 25452 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.707779 |
| neg_average_precision | 0.441064 |
| neg_precision | 0.57455 |
| neg_recall | 0.1475 |
| full_pmf_events | 31725 |
| full_pmf_final_decile_mass | 0.14095 |
| no_buzz_observed_rate | 0.19773 |
| no_buzz_predicted_rate | 0.208477 |
| no_buzz_calibration_error | 0.0107463 |
| no_buzz_brier | 0.0437828 |
| full_pmf_max_mass_error | 1.55431e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 25452 | -0.0503752 | -0.0680295 |
| Q1 (0-.2) | 539 | 0.374244 | 0.373788 |
| Q2 (.2-.4) | 2579 | 0.221361 | 0.221172 |
| Q3 (.4-.6) | 6051 | 0.0670832 | 0.0634268 |
| Q4 (.6-.8) | 8052 | -0.0738739 | -0.0756361 |
| Q5 (.8-1) | 8231 | -0.226685 | -0.224015 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 25452 | 0.0180801 | 0.162417 | 0.707779 | 0.498623 |
| tossup_correctness | tier | bowl | 653 | 0.0620516 | 0.178375 | 0.704281 | 0.53669 |
| tossup_correctness | tier | fall | 8640 | 0.00730839 | 0.151074 | 0.714877 | 0.469679 |
| tossup_correctness | tier | nationals | 4758 | 0.0462362 | 0.177504 | 0.700305 | 0.537423 |
| tossup_correctness | tier | open | 515 | 0.0654329 | 0.184682 | 0.641326 | 0.564961 |
| tossup_correctness | tier | regionals | 4965 | 0.0208507 | 0.166982 | 0.723126 | 0.506803 |
| tossup_correctness | tier | winter | 5921 | 0.0137513 | 0.159321 | 0.695705 | 0.492854 |
| tossup_correctness | category | Current Events | 414 | 0.0230872 | 0.161341 | 0.710159 | 0.49633 |
| tossup_correctness | category | Fine Arts | 3509 | 0.0155368 | 0.156399 | 0.712762 | 0.485686 |
| tossup_correctness | category | Geography | 524 | 0.0511704 | 0.181471 | 0.697174 | 0.548787 |
| tossup_correctness | category | History | 4719 | 0.0244281 | 0.164263 | 0.705715 | 0.501415 |
| tossup_correctness | category | Literature | 4632 | 0.0196787 | 0.143252 | 0.719114 | 0.451196 |
| tossup_correctness | category | Mythology | 1039 | 0.0278232 | 0.153534 | 0.714565 | 0.474627 |
| tossup_correctness | category | Other Academic | 227 | 0.0869765 | 0.191478 | 0.649714 | 0.576891 |
| tossup_correctness | category | Philosophy | 1056 | 0.0171655 | 0.156814 | 0.72923 | 0.483285 |
| tossup_correctness | category | Popular Culture | 364 | 0.0533873 | 0.130379 | 0.615028 | 0.431779 |
| tossup_correctness | category | Religion | 1154 | 0.0233674 | 0.176264 | 0.68787 | 0.534282 |
| tossup_correctness | category | Science | 4693 | 0.0243756 | 0.177734 | 0.692465 | 0.536459 |
| tossup_correctness | category | Social Science | 1045 | 0.043783 | 0.184765 | 0.688773 | 0.55694 |
| tossup_correctness | category | Unknown | 2076 | 0.0197128 | 0.162719 | 0.712827 | 0.496029 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 539 | 0.0395481 | 0.174387 | 0.714316 | 0.528664 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 2579 | 0.0293257 | 0.17425 | 0.697185 | 0.525689 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 6051 | 0.0228 | 0.165321 | 0.701758 | 0.505638 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 8052 | 0.00932 | 0.150865 | 0.706034 | 0.471422 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 8231 | 0.0245684 | 0.167091 | 0.7122 | 0.509629 |
