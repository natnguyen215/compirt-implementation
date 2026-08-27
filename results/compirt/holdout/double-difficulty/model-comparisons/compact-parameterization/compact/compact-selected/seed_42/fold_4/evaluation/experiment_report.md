# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.713817 |
| log_loss | 0.500655 |
| ece | 0.0472527 |
| brier | 0.161706 |
| accuracy | 0.770874 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | -0.00248112 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.20847 |
| probability_p10 | 0.441111 |
| probability_p50 | 0.823797 |
| probability_p90 | 0.956027 |
| mean_predictive_variance | 0.14054 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0945328 |
| joint_tossup_event_log_loss | 6.42009 |
| buzz_position_mae | 0.140865 |
| buzz_position_median_absolute_error | 0.120982 |
| buzz_position_bias | -0.0269796 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.389752 |
| first_buzzer_mean_reciprocal_rank | 0.597981 |
| first_buzzer_log_loss | 1.58467 |
| first_buzzer_events | 9270 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.713817 |
| neg_average_precision | 0.428337 |
| neg_precision | 0.490551 |
| neg_recall | 0.28415 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.173034 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.00908625 |
| no_buzz_calibration_error | -0.00264083 |
| no_buzz_brier | 0.010524 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9270 | -0.0269796 | -0.0475081 |
| Q1 (0-.2) | 179 | 0.36906 | 0.36812 |
| Q2 (.2-.4) | 957 | 0.214724 | 0.208946 |
| Q3 (.4-.6) | 2203 | 0.0673997 | 0.0624081 |
| Q4 (.6-.8) | 2978 | -0.0555566 | -0.0538874 |
| Q5 (.8-1) | 2953 | -0.170907 | -0.159669 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.0472527 | 0.161706 | 0.713817 | 0.500655 |
| tossup_correctness | tier | fall | 2876 | 0.0414492 | 0.150282 | 0.7154 | 0.46938 |
| tossup_correctness | tier | nationals | 1579 | 0.0624364 | 0.181715 | 0.707002 | 0.553188 |
| tossup_correctness | tier | regionals | 1990 | 0.0503187 | 0.162201 | 0.73658 | 0.50153 |
| tossup_correctness | tier | winter | 2825 | 0.0582174 | 0.161804 | 0.697236 | 0.502515 |
| tossup_correctness | category | Current Events | 123 | 0.103579 | 0.174418 | 0.730741 | 0.517186 |
| tossup_correctness | category | Fine Arts | 1093 | 0.045472 | 0.156799 | 0.715347 | 0.492294 |
| tossup_correctness | category | Geography | 191 | 0.0685119 | 0.16796 | 0.761299 | 0.516087 |
| tossup_correctness | category | History | 1469 | 0.0531777 | 0.171264 | 0.712979 | 0.51816 |
| tossup_correctness | category | Literature | 1436 | 0.075174 | 0.146879 | 0.693183 | 0.470777 |
| tossup_correctness | category | Mythology | 325 | 0.045073 | 0.126695 | 0.693717 | 0.410691 |
| tossup_correctness | category | Other Academic | 67 | 0.121994 | 0.181834 | 0.579515 | 0.568086 |
| tossup_correctness | category | Philosophy | 322 | 0.0417305 | 0.157877 | 0.710947 | 0.482594 |
| tossup_correctness | category | Popular Culture | 100 | 0.0705026 | 0.105861 | 0.622063 | 0.361192 |
| tossup_correctness | category | Religion | 365 | 0.0759707 | 0.198029 | 0.643002 | 0.588009 |
| tossup_correctness | category | Science | 1456 | 0.0669326 | 0.169504 | 0.694153 | 0.521601 |
| tossup_correctness | category | Social Science | 333 | 0.0495442 | 0.165038 | 0.746868 | 0.505768 |
| tossup_correctness | category | Unknown | 1990 | 0.0503187 | 0.162201 | 0.73658 | 0.50153 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.0726557 | 0.173724 | 0.721061 | 0.528305 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.0613226 | 0.167667 | 0.71319 | 0.51927 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.0530068 | 0.163306 | 0.713995 | 0.505719 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.0398655 | 0.152744 | 0.711233 | 0.479694 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.0662499 | 0.166891 | 0.718428 | 0.510305 |
