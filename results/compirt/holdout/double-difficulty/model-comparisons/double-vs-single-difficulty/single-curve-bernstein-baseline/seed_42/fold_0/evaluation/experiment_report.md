# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.638835 |
| log_loss | 0.718144 |
| ece | 0.184115 |
| brier | 0.234809 |
| accuracy | 0.661216 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | -0.104034 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.291524 |
| probability_p10 | 0.153952 |
| probability_p50 | 0.690127 |
| probability_p90 | 0.947389 |
| mean_predictive_variance | 0.150926 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0952091 |
| joint_tossup_event_log_loss | 6.71176 |
| buzz_position_mae | 0.136818 |
| buzz_position_median_absolute_error | 0.111696 |
| buzz_position_bias | 0.0103454 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.406885 |
| first_buzzer_mean_reciprocal_rank | 0.607346 |
| first_buzzer_log_loss | 1.58327 |
| first_buzzer_events | 9295 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.638835 |
| neg_average_precision | 0.34905 |
| neg_precision | 0.341006 |
| neg_recall | 0.475252 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.1385 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.0621751 |
| no_buzz_calibration_error | 0.0489055 |
| no_buzz_brier | 0.0254401 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9295 | 0.0103454 | -0.00989099 |
| Q1 (0-.2) | 197 | 0.383664 | 0.376564 |
| Q2 (.2-.4) | 985 | 0.233146 | 0.225564 |
| Q3 (.4-.6) | 2251 | 0.103122 | 0.0992244 |
| Q4 (.6-.8) | 2866 | -0.0135539 | -0.0095702 |
| Q5 (.8-1) | 2996 | -0.134297 | -0.124524 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.184115 | 0.234809 | 0.638835 | 0.718144 |
| tossup_correctness | tier | fall | 2933 | 0.202643 | 0.229107 | 0.644985 | 0.698989 |
| tossup_correctness | tier | nationals | 1584 | 0.17434 | 0.244474 | 0.61399 | 0.758786 |
| tossup_correctness | tier | regionals | 1886 | 0.192249 | 0.246195 | 0.637666 | 0.751183 |
| tossup_correctness | tier | winter | 2892 | 0.17854 | 0.227875 | 0.6594 | 0.693763 |
| tossup_correctness | category | Current Events | 124 | 0.199131 | 0.240622 | 0.621922 | 0.750795 |
| tossup_correctness | category | Fine Arts | 1103 | 0.169336 | 0.223324 | 0.658045 | 0.68226 |
| tossup_correctness | category | Geography | 197 | 0.20629 | 0.263366 | 0.651282 | 0.767847 |
| tossup_correctness | category | History | 1491 | 0.173735 | 0.215095 | 0.673292 | 0.671825 |
| tossup_correctness | category | Literature | 1472 | 0.213889 | 0.240232 | 0.570691 | 0.747565 |
| tossup_correctness | category | Mythology | 332 | 0.251975 | 0.239697 | 0.627419 | 0.70891 |
| tossup_correctness | category | Other Academic | 69 | 0.252571 | 0.258965 | 0.567873 | 0.833852 |
| tossup_correctness | category | Philosophy | 324 | 0.194327 | 0.228793 | 0.622394 | 0.690992 |
| tossup_correctness | category | Popular Culture | 102 | 0.34633 | 0.314701 | 0.495502 | 0.876834 |
| tossup_correctness | category | Religion | 372 | 0.202661 | 0.256576 | 0.633418 | 0.763945 |
| tossup_correctness | category | Science | 1487 | 0.147472 | 0.223382 | 0.66061 | 0.683239 |
| tossup_correctness | category | Social Science | 336 | 0.201597 | 0.25168 | 0.635805 | 0.753078 |
| tossup_correctness | category | Unknown | 1886 | 0.192249 | 0.246195 | 0.637666 | 0.751183 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.471672 | 0.423553 | 0.675332 | 1.31684 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.337198 | 0.321815 | 0.667016 | 0.971678 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.241162 | 0.262035 | 0.645196 | 0.778677 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.162357 | 0.216606 | 0.654334 | 0.651759 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.103094 | 0.190752 | 0.647023 | 0.613446 |
