# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.726482 |
| log_loss | 0.474423 |
| ece | 0.0131926 |
| brier | 0.153163 |
| accuracy | 0.789428 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | 0.0160734 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.138997 |
| probability_p10 | 0.583669 |
| probability_p50 | 0.810533 |
| probability_p90 | 0.917103 |
| mean_predictive_variance | 0.154731 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.101471 |
| joint_tossup_event_log_loss | 6.61071 |
| buzz_position_mae | 0.150931 |
| buzz_position_median_absolute_error | 0.133605 |
| buzz_position_bias | -0.0437156 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.352535 |
| first_buzzer_mean_reciprocal_rank | 0.563507 |
| first_buzzer_log_loss | 1.68759 |
| first_buzzer_events | 9270 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.726482 |
| neg_average_precision | 0.458837 |
| neg_precision | 0.648703 |
| neg_recall | 0.154688 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.186567 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0137376 |
| no_buzz_calibration_error | 0.00201057 |
| no_buzz_brier | 0.01105 |
| full_pmf_max_mass_error | 1.55431e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9270 | -0.0437156 | -0.0646468 |
| Q1 (0-.2) | 179 | 0.376941 | 0.384842 |
| Q2 (.2-.4) | 957 | 0.218561 | 0.213105 |
| Q3 (.4-.6) | 2203 | 0.0648981 | 0.0605491 |
| Q4 (.6-.8) | 2978 | -0.0719717 | -0.0726966 |
| Q5 (.8-1) | 2953 | -0.206745 | -0.202581 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.0131926 | 0.153163 | 0.726482 | 0.474423 |
| tossup_correctness | tier | fall | 2876 | 0.0117095 | 0.14389 | 0.730007 | 0.451044 |
| tossup_correctness | tier | nationals | 1579 | 0.0360473 | 0.173181 | 0.720913 | 0.523254 |
| tossup_correctness | tier | regionals | 1990 | 0.0241436 | 0.155851 | 0.732062 | 0.480146 |
| tossup_correctness | tier | winter | 2825 | 0.0174357 | 0.14952 | 0.719405 | 0.466898 |
| tossup_correctness | category | Current Events | 123 | 0.0636815 | 0.151037 | 0.764857 | 0.464414 |
| tossup_correctness | category | Fine Arts | 1093 | 0.0234316 | 0.150441 | 0.738871 | 0.468852 |
| tossup_correctness | category | Geography | 191 | 0.0807473 | 0.159267 | 0.797252 | 0.489695 |
| tossup_correctness | category | History | 1469 | 0.0302988 | 0.16351 | 0.72095 | 0.497485 |
| tossup_correctness | category | Literature | 1436 | 0.0168537 | 0.135681 | 0.714587 | 0.432591 |
| tossup_correctness | category | Mythology | 325 | 0.0598518 | 0.127248 | 0.688207 | 0.412229 |
| tossup_correctness | category | Other Academic | 67 | 0.0724296 | 0.157462 | 0.673854 | 0.487071 |
| tossup_correctness | category | Philosophy | 322 | 0.0475642 | 0.15916 | 0.683279 | 0.487599 |
| tossup_correctness | category | Popular Culture | 100 | 0.0648038 | 0.105013 | 0.531154 | 0.364426 |
| tossup_correctness | category | Religion | 365 | 0.0461894 | 0.185732 | 0.670642 | 0.555596 |
| tossup_correctness | category | Science | 1456 | 0.0163406 | 0.155463 | 0.726517 | 0.480654 |
| tossup_correctness | category | Social Science | 333 | 0.0479768 | 0.160391 | 0.749657 | 0.494323 |
| tossup_correctness | category | Unknown | 1990 | 0.0241436 | 0.155851 | 0.732062 | 0.480146 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.0749034 | 0.158483 | 0.763847 | 0.484414 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.01986 | 0.163683 | 0.7029 | 0.501922 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.0283803 | 0.157052 | 0.72524 | 0.483293 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.0153248 | 0.147802 | 0.716029 | 0.462222 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.0181076 | 0.151935 | 0.74016 | 0.470592 |
