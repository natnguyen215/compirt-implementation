# CompIRT Experiment Report

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.62571 |
| log_loss | 0.824752 |
| ece | 0.219196 |
| brier | 0.262063 |
| accuracy | 0.623667 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.138458 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.295596 |
| probability_p10 | 0.104138 |
| probability_p50 | 0.621281 |
| probability_p90 | 0.915539 |
| mean_predictive_variance | 0.158709 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0952366 |
| joint_tossup_event_log_loss | 6.80028 |
| buzz_position_mae | 0.145832 |
| buzz_position_median_absolute_error | 0.124799 |
| buzz_position_bias | -0.0444516 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.388981 |
| first_buzzer_mean_reciprocal_rank | 0.5956 |
| first_buzzer_log_loss | 1.63493 |
| first_buzzer_events | 9093 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9093 | -0.0444516 | -0.058204 |
| Q1 (0-.2) | 167 | 0.347023 | 0.368727 |
| Q2 (.2-.4) | 912 | 0.194858 | 0.1932 |
| Q3 (.4-.6) | 2115 | 0.0586627 | 0.0573283 |
| Q4 (.6-.8) | 2844 | -0.0606665 | -0.0557102 |
| Q5 (.8-1) | 3055 | -0.193584 | -0.186144 |

## Stage 2: Bonus Metrics

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.886937 |
| log_loss | 0.424365 |
| ece | 0.0171191 |
| brier | 0.13514 |
| part_accuracy | 0.807601 |
| part_all_correct_accuracy | 0.519002 |
| accuracy_lift_over_all_correct | 0.288599 |
| part_accuracy_macro_team | 0.811346 |
| part_accuracy_macro_bonus | 0.80443 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.326577 |
| probability_p10 | 0.0855848 |
| probability_p50 | 0.472889 |
| probability_p90 | 0.930805 |
| mean_predictive_variance | 0.143341 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.516033 |
| ranked_probability_score | 0.115895 |
| bonus_total_score_log_loss | 1.01453 |
| ppb_mae | 2.37596 |
| ranked_probability_score_responses | 8420 |
| bonus_total_score_log_loss_responses | 8420 |

## Match Winner Simulation

| metric | value |
| --- | --- |
| match_winner_accuracy | 0.755459 |
| match_winner_brier | 0.160192 |
| match_games | 458 |
| match_simulations_per_game | 500 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.219196 | 0.262063 | 0.62571 | 0.824752 |
| tossup_correctness | tier | fall | 2842 | 0.223092 | 0.253613 | 0.634413 | 0.800585 |
| tossup_correctness | tier | nationals | 1564 | 0.195418 | 0.260967 | 0.607602 | 0.792163 |
| tossup_correctness | tier | regionals | 1937 | 0.208392 | 0.255233 | 0.629286 | 0.799011 |
| tossup_correctness | tier | winter | 2750 | 0.246845 | 0.276229 | 0.631682 | 0.886394 |
| tossup_correctness | category | Current Events | 126 | 0.316818 | 0.323889 | 0.561678 | 1.06723 |
| tossup_correctness | category | Fine Arts | 1071 | 0.243028 | 0.273006 | 0.629734 | 0.857282 |
| tossup_correctness | category | Geography | 185 | 0.244004 | 0.29594 | 0.625692 | 0.888883 |
| tossup_correctness | category | History | 1440 | 0.213543 | 0.257529 | 0.622616 | 0.79732 |
| tossup_correctness | category | Literature | 1422 | 0.228826 | 0.253449 | 0.610084 | 0.828703 |
| tossup_correctness | category | Mythology | 318 | 0.272848 | 0.274509 | 0.602902 | 0.825482 |
| tossup_correctness | category | Other Academic | 66 | 0.221402 | 0.23981 | 0.702128 | 0.762023 |
| tossup_correctness | category | Philosophy | 311 | 0.205007 | 0.258306 | 0.665757 | 0.827232 |
| tossup_correctness | category | Popular Culture | 102 | 0.406935 | 0.34659 | 0.466667 | 1.1214 |
| tossup_correctness | category | Religion | 358 | 0.179454 | 0.256361 | 0.649876 | 0.793317 |
| tossup_correctness | category | Science | 1433 | 0.210599 | 0.260481 | 0.622725 | 0.822897 |
| tossup_correctness | category | Social Science | 324 | 0.23158 | 0.263902 | 0.627528 | 0.804017 |
| tossup_correctness | category | Unknown | 1937 | 0.208392 | 0.255233 | 0.629286 | 0.799011 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.453617 | 0.427139 | 0.643557 | 1.34686 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.387229 | 0.366082 | 0.640571 | 1.19325 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.273322 | 0.285366 | 0.645061 | 0.881647 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.200848 | 0.239838 | 0.628457 | 0.749354 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.143843 | 0.226544 | 0.622782 | 0.717007 |
| bonus_part_correctness | aggregate | all | 25260 | 0.0171191 | 0.13514 | 0.886937 | 0.424365 |
| bonus_part_correctness | tier | fall | 8160 | 0.0411483 | 0.135507 | 0.884438 | 0.422801 |
| bonus_part_correctness | tier | nationals | 4107 | 0.0217494 | 0.138976 | 0.873269 | 0.439212 |
| bonus_part_correctness | tier | regionals | 5280 | 0.0162643 | 0.136242 | 0.883969 | 0.427312 |
| bonus_part_correctness | tier | winter | 7713 | 0.0219283 | 0.131956 | 0.890536 | 0.416097 |
| bonus_part_correctness | category | Current Events | 249 | 0.0730819 | 0.130024 | 0.897792 | 0.41237 |
| bonus_part_correctness | category | Fine Arts | 2934 | 0.023952 | 0.141509 | 0.876934 | 0.44197 |
| bonus_part_correctness | category | Geography | 459 | 0.0758463 | 0.135976 | 0.88505 | 0.425456 |
| bonus_part_correctness | category | History | 4017 | 0.0375936 | 0.135128 | 0.888118 | 0.421894 |
| bonus_part_correctness | category | Literature | 4047 | 0.0256455 | 0.129182 | 0.892529 | 0.411888 |
| bonus_part_correctness | category | Mythology | 924 | 0.037289 | 0.144112 | 0.869283 | 0.443912 |
| bonus_part_correctness | category | Other Academic | 237 | 0.055229 | 0.122918 | 0.903937 | 0.396434 |
| bonus_part_correctness | category | Philosophy | 948 | 0.0498863 | 0.143148 | 0.87124 | 0.447366 |
| bonus_part_correctness | category | Popular Culture | 294 | 0.114644 | 0.139712 | 0.893413 | 0.426747 |
| bonus_part_correctness | category | Religion | 984 | 0.0325488 | 0.134466 | 0.889832 | 0.422782 |
| bonus_part_correctness | category | Science | 3990 | 0.023845 | 0.13448 | 0.888164 | 0.422558 |
| bonus_part_correctness | category | Social Science | 897 | 0.0379863 | 0.123456 | 0.903526 | 0.391494 |
| bonus_part_correctness | category | Unknown | 5280 | 0.0162643 | 0.136242 | 0.883969 | 0.427312 |
