# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.706208 |
| log_loss | 0.495005 |
| ece | 0.0144942 |
| brier | 0.161023 |
| accuracy | 0.773829 |
| all_correct_accuracy | 0.765912 |
| accuracy_lift_over_all_correct | 0.0079162 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.149322 |
| probability_p10 | 0.56271 |
| probability_p50 | 0.814535 |
| probability_p90 | 0.923032 |
| mean_predictive_variance | 0.152733 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0895632 |
| joint_tossup_event_log_loss | 5.53235 |
| buzz_position_mae | 0.15854 |
| buzz_position_median_absolute_error | 0.139931 |
| buzz_position_bias | -0.0484326 |
| survival_events | 31097 |
| joint_tossup_event_log_loss_events | 31097 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.336399 |
| first_buzzer_mean_reciprocal_rank | 0.552198 |
| first_buzzer_log_loss | 1.70626 |
| first_buzzer_events | 25012 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.706208 |
| neg_average_precision | 0.431942 |
| neg_precision | 0.561262 |
| neg_recall | 0.15491 |
| full_pmf_events | 31097 |
| full_pmf_final_decile_mass | 0.142682 |
| no_buzz_observed_rate | 0.195678 |
| no_buzz_predicted_rate | 0.20498 |
| no_buzz_calibration_error | 0.00930209 |
| no_buzz_brier | 0.0430429 |
| full_pmf_max_mass_error | 1.55431e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 25012 | -0.0484326 | -0.0672996 |
| Q1 (0-.2) | 528 | 0.383052 | 0.391509 |
| Q2 (.2-.4) | 2578 | 0.227095 | 0.227273 |
| Q3 (.4-.6) | 5735 | 0.0693406 | 0.0657248 |
| Q4 (.6-.8) | 8078 | -0.073124 | -0.0739558 |
| Q5 (.8-1) | 8093 | -0.223165 | -0.219987 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 25012 | 0.0144942 | 0.161023 | 0.706208 | 0.495005 |
| tossup_correctness | tier | bowl | 662 | 0.0473674 | 0.153519 | 0.747345 | 0.471974 |
| tossup_correctness | tier | fall | 8465 | 0.00970563 | 0.147985 | 0.713581 | 0.462485 |
| tossup_correctness | tier | nationals | 4755 | 0.0411806 | 0.178958 | 0.700561 | 0.538617 |
| tossup_correctness | tier | open | 496 | 0.0954135 | 0.198548 | 0.666383 | 0.594462 |
| tossup_correctness | tier | regionals | 4868 | 0.01994 | 0.167 | 0.712567 | 0.508502 |
| tossup_correctness | tier | winter | 5766 | 0.0167783 | 0.157962 | 0.691619 | 0.489478 |
| tossup_correctness | category | Current Events | 417 | 0.0524707 | 0.155164 | 0.730412 | 0.479544 |
| tossup_correctness | category | Fine Arts | 3441 | 0.0178812 | 0.159972 | 0.713417 | 0.492728 |
| tossup_correctness | category | Geography | 508 | 0.0396918 | 0.165723 | 0.726894 | 0.504513 |
| tossup_correctness | category | History | 4651 | 0.0149092 | 0.162228 | 0.707416 | 0.496161 |
| tossup_correctness | category | Literature | 4591 | 0.0107939 | 0.14046 | 0.720567 | 0.444871 |
| tossup_correctness | category | Mythology | 1017 | 0.0255871 | 0.152924 | 0.678226 | 0.478459 |
| tossup_correctness | category | Other Academic | 231 | 0.0645051 | 0.190014 | 0.583416 | 0.569499 |
| tossup_correctness | category | Philosophy | 1044 | 0.016585 | 0.153078 | 0.69563 | 0.474533 |
| tossup_correctness | category | Popular Culture | 346 | 0.0386718 | 0.12571 | 0.623692 | 0.412484 |
| tossup_correctness | category | Religion | 1136 | 0.0427653 | 0.174732 | 0.670579 | 0.533233 |
| tossup_correctness | category | Science | 4632 | 0.0295738 | 0.180335 | 0.690501 | 0.542021 |
| tossup_correctness | category | Social Science | 1032 | 0.0233068 | 0.165171 | 0.697893 | 0.506741 |
| tossup_correctness | category | Unknown | 1966 | 0.0211796 | 0.16368 | 0.715208 | 0.500336 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 528 | 0.0368375 | 0.165601 | 0.69726 | 0.505571 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 2578 | 0.03027 | 0.178709 | 0.692356 | 0.537758 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 5735 | 0.0173095 | 0.161991 | 0.709696 | 0.496722 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 8078 | 0.0171203 | 0.155345 | 0.689527 | 0.482899 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 8093 | 0.0114964 | 0.160073 | 0.72142 | 0.491565 |
