# CompIRT Experiment Report

**Evaluation regime: in-sample fit.** Player and question parameters were estimated on the same observations these metrics score, so they are optimization and inspection diagnostics, not generalization estimates.

**Correctness calibration was fit on the scored outcomes.** This run learned a Platt scale/bias on the same split these metrics score, so tossup ECE and log loss are flattered by construction and are not comparable to uncalibrated runs.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.663602 |
| log_loss | 0.512191 |
| ece | 0.0114169 |
| brier | 0.167145 |
| accuracy | 0.770526 |
| all_correct_accuracy | 0.767271 |
| accuracy_lift_over_all_correct | 0.00325583 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.0934659 |
| probability_p10 | 0.645357 |
| probability_p50 | 0.787441 |
| probability_p90 | 0.877345 |
| mean_predictive_variance | 0.16713 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0862266 |
| joint_tossup_event_log_loss | 6.01746 |
| buzz_position_mae | 0.130462 |
| buzz_position_median_absolute_error | 0.110282 |
| buzz_position_bias | -0.00629646 |
| survival_events | 48612 |
| joint_tossup_event_log_loss_events | 48612 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.485996 |
| first_buzzer_mean_reciprocal_rank | 0.6741 |
| first_buzzer_log_loss | 1.33989 |
| first_buzzer_events | 47914 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 47914 | -0.00629646 | -0.026082 |
| Q1 (0-.2) | 943 | 0.371946 | 0.376645 |
| Q2 (.2-.4) | 4869 | 0.220288 | 0.216844 |
| Q3 (.4-.6) | 11467 | 0.0879093 | 0.0841808 |
| Q4 (.6-.8) | 15035 | -0.0270209 | -0.0256992 |
| Q5 (.8-1) | 15600 | -0.149155 | -0.14352 |

## Stage 2: Bonus Metrics

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.936141 |
| log_loss | 0.331058 |
| ece | 0.0382418 |
| brier | 0.10349 |
| part_accuracy | 0.853987 |
| part_all_correct_accuracy | 0.520489 |
| accuracy_lift_over_all_correct | 0.333498 |
| part_accuracy_macro_team | 0.856057 |
| part_accuracy_macro_game | 0.854284 |
| part_accuracy_macro_bonus | 0.861529 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.360323 |
| probability_p10 | 0.0432157 |
| probability_p50 | 0.453928 |
| probability_p90 | 0.969606 |
| mean_predictive_variance | 0.120092 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.61591 |
| ranked_probability_score | 0.0941761 |
| bonus_total_score_log_loss | 0.838958 |
| ppb_mae | 1.52347 |
| ranked_probability_score_responses | 44487 |
| bonus_total_score_log_loss_responses | 44487 |

## Match Winner Simulation

| metric | value |
| --- | --- |
| match_winner_accuracy | 0.803238 |
| match_winner_brier | 0.134394 |
| match_games | 2409 |
| match_simulations_per_game | 500 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 47914 | 0.0114169 | 0.167145 | 0.663602 | 0.512191 |
| tossup_correctness | tier | fall | 14760 | 0.0264963 | 0.154897 | 0.684439 | 0.482364 |
| tossup_correctness | tier | nationals | 7940 | 0.0521448 | 0.191848 | 0.633137 | 0.572932 |
| tossup_correctness | tier | regionals | 10202 | 0.0139978 | 0.171838 | 0.655768 | 0.523878 |
| tossup_correctness | tier | winter | 15012 | 0.0235072 | 0.162932 | 0.675015 | 0.501447 |
| tossup_correctness | category | Current Events | 640 | 0.028778 | 0.183371 | 0.663504 | 0.5501 |
| tossup_correctness | category | Fine Arts | 5640 | 0.00996907 | 0.167219 | 0.6633 | 0.512429 |
| tossup_correctness | category | Geography | 972 | 0.0752848 | 0.208938 | 0.668034 | 0.603658 |
| tossup_correctness | category | History | 7599 | 0.0247385 | 0.16537 | 0.691196 | 0.506183 |
| tossup_correctness | category | Literature | 7469 | 0.0275937 | 0.147948 | 0.636401 | 0.467578 |
| tossup_correctness | category | Mythology | 1692 | 0.0600082 | 0.148787 | 0.660287 | 0.471768 |
| tossup_correctness | category | Other Academic | 357 | 0.040398 | 0.177016 | 0.622691 | 0.538485 |
| tossup_correctness | category | Philosophy | 1649 | 0.0274453 | 0.158697 | 0.672104 | 0.492607 |
| tossup_correctness | category | Popular Culture | 538 | 0.108705 | 0.129102 | 0.598144 | 0.427662 |
| tossup_correctness | category | Religion | 1889 | 0.0353825 | 0.183043 | 0.690078 | 0.547773 |
| tossup_correctness | category | Science | 7556 | 0.028119 | 0.173881 | 0.667362 | 0.528029 |
| tossup_correctness | category | Social Science | 1711 | 0.0358571 | 0.189697 | 0.646793 | 0.567717 |
| tossup_correctness | category | Unknown | 10202 | 0.0139978 | 0.171838 | 0.655768 | 0.523878 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 943 | 0.0837066 | 0.184468 | 0.687133 | 0.553595 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 4869 | 0.0462848 | 0.178713 | 0.686899 | 0.53857 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 11467 | 0.0290967 | 0.167748 | 0.689854 | 0.511788 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 15035 | 0.030005 | 0.155684 | 0.691278 | 0.483619 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 15600 | 0.0503062 | 0.17309 | 0.639725 | 0.529287 |
| bonus_part_correctness | aggregate | all | 133461 | 0.0382418 | 0.10349 | 0.936141 | 0.331058 |
| bonus_part_correctness | tier | fall | 42336 | 0.0302286 | 0.107512 | 0.928006 | 0.339147 |
| bonus_part_correctness | tier | nationals | 21051 | 0.0553168 | 0.0972663 | 0.945336 | 0.317023 |
| bonus_part_correctness | tier | regionals | 27762 | 0.0466617 | 0.0993857 | 0.942261 | 0.321139 |
| bonus_part_correctness | tier | winter | 42312 | 0.03224 | 0.105255 | 0.932698 | 0.336455 |
| bonus_part_correctness | category | Current Events | 1281 | 0.0438493 | 0.101694 | 0.937221 | 0.327924 |
| bonus_part_correctness | category | Fine Arts | 15525 | 0.0372035 | 0.111229 | 0.926043 | 0.353497 |
| bonus_part_correctness | category | Geography | 2427 | 0.0396171 | 0.107246 | 0.929073 | 0.340172 |
| bonus_part_correctness | category | History | 21273 | 0.0356457 | 0.103424 | 0.935543 | 0.329738 |
| bonus_part_correctness | category | Literature | 21312 | 0.0375433 | 0.0980426 | 0.942014 | 0.316391 |
| bonus_part_correctness | category | Mythology | 4923 | 0.034824 | 0.116768 | 0.914763 | 0.364638 |
| bonus_part_correctness | category | Other Academic | 1272 | 0.0417922 | 0.092827 | 0.947165 | 0.302384 |
| bonus_part_correctness | category | Philosophy | 4989 | 0.0411235 | 0.110484 | 0.927718 | 0.351254 |
| bonus_part_correctness | category | Popular Culture | 1536 | 0.0259092 | 0.116581 | 0.91375 | 0.360921 |
| bonus_part_correctness | category | Religion | 5280 | 0.03625 | 0.105348 | 0.93358 | 0.335219 |
| bonus_part_correctness | category | Science | 21183 | 0.0350975 | 0.104277 | 0.934437 | 0.333293 |
| bonus_part_correctness | category | Social Science | 4698 | 0.0326735 | 0.097365 | 0.941775 | 0.310792 |
| bonus_part_correctness | category | Unknown | 27762 | 0.0466617 | 0.0993857 | 0.942261 | 0.321139 |
