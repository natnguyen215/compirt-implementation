# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.717269 |
| log_loss | 0.582109 |
| ece | 0.194087 |
| brier | 0.199117 |
| accuracy | 0.690076 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | -0.0832794 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.211419 |
| probability_p10 | 0.279362 |
| probability_p50 | 0.597435 |
| probability_p90 | 0.848632 |
| mean_predictive_variance | 0.199019 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.101197 |
| joint_tossup_event_log_loss | 6.71082 |
| buzz_position_mae | 0.150703 |
| buzz_position_median_absolute_error | 0.133894 |
| buzz_position_bias | -0.0432805 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.349407 |
| first_buzzer_mean_reciprocal_rank | 0.561083 |
| first_buzzer_log_loss | 1.68765 |
| first_buzzer_events | 9270 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.717269 |
| neg_average_precision | 0.446719 |
| neg_precision | 0.381011 |
| neg_recall | 0.588291 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.184969 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0133692 |
| no_buzz_calibration_error | 0.00164207 |
| no_buzz_brier | 0.0110196 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9270 | -0.0432805 | -0.0644584 |
| Q1 (0-.2) | 179 | 0.378453 | 0.379409 |
| Q2 (.2-.4) | 957 | 0.217334 | 0.209406 |
| Q3 (.4-.6) | 2203 | 0.0646689 | 0.0608953 |
| Q4 (.6-.8) | 2978 | -0.071442 | -0.0722743 |
| Q5 (.8-1) | 2953 | -0.205436 | -0.20134 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.194087 | 0.199117 | 0.717269 | 0.582109 |
| tossup_correctness | tier | fall | 2876 | 0.188212 | 0.189009 | 0.718371 | 0.557727 |
| tossup_correctness | tier | nationals | 1579 | 0.176808 | 0.210686 | 0.709667 | 0.610131 |
| tossup_correctness | tier | regionals | 1990 | 0.206582 | 0.202653 | 0.73377 | 0.590629 |
| tossup_correctness | tier | winter | 2825 | 0.201233 | 0.200451 | 0.704694 | 0.585266 |
| tossup_correctness | category | Current Events | 123 | 0.220351 | 0.210595 | 0.746882 | 0.598577 |
| tossup_correctness | category | Fine Arts | 1093 | 0.177709 | 0.188971 | 0.732367 | 0.5588 |
| tossup_correctness | category | Geography | 191 | 0.20322 | 0.208829 | 0.784284 | 0.607198 |
| tossup_correctness | category | History | 1469 | 0.178294 | 0.203844 | 0.706827 | 0.592857 |
| tossup_correctness | category | Literature | 1436 | 0.181835 | 0.18046 | 0.691037 | 0.540084 |
| tossup_correctness | category | Mythology | 325 | 0.22086 | 0.182947 | 0.689709 | 0.544639 |
| tossup_correctness | category | Other Academic | 67 | 0.269325 | 0.229649 | 0.714286 | 0.653677 |
| tossup_correctness | category | Philosophy | 322 | 0.186243 | 0.208138 | 0.660938 | 0.599012 |
| tossup_correctness | category | Popular Culture | 100 | 0.213673 | 0.158817 | 0.558733 | 0.492003 |
| tossup_correctness | category | Religion | 365 | 0.169552 | 0.227014 | 0.652978 | 0.645851 |
| tossup_correctness | category | Science | 1456 | 0.209 | 0.205913 | 0.722056 | 0.598439 |
| tossup_correctness | category | Social Science | 333 | 0.204187 | 0.213815 | 0.73626 | 0.612649 |
| tossup_correctness | category | Unknown | 1990 | 0.206582 | 0.202653 | 0.73377 | 0.590629 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.23313 | 0.220708 | 0.733499 | 0.631186 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.193475 | 0.210754 | 0.697024 | 0.60771 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.18356 | 0.197306 | 0.720752 | 0.577826 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.191373 | 0.193409 | 0.705001 | 0.568602 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.202509 | 0.201145 | 0.729867 | 0.587654 |
