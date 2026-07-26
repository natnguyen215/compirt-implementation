# CompIRT Experiment Report

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.637679 |
| log_loss | 0.76678 |
| ece | 0.21016 |
| brier | 0.24819 |
| accuracy | 0.642181 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | -0.127863 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.290272 |
| probability_p10 | 0.121749 |
| probability_p50 | 0.637131 |
| probability_p90 | 0.921617 |
| mean_predictive_variance | 0.159697 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0944496 |
| joint_tossup_event_log_loss | 6.69696 |
| buzz_position_mae | 0.145242 |
| buzz_position_median_absolute_error | 0.124564 |
| buzz_position_bias | -0.0477531 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.396145 |
| first_buzzer_mean_reciprocal_rank | 0.60188 |
| first_buzzer_log_loss | 1.59285 |
| first_buzzer_events | 9080 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9080 | -0.0477531 | -0.0612559 |
| Q1 (0-.2) | 192 | 0.345212 | 0.348373 |
| Q2 (.2-.4) | 889 | 0.184134 | 0.183156 |
| Q3 (.4-.6) | 2210 | 0.0485488 | 0.0441036 |
| Q4 (.6-.8) | 2869 | -0.0716163 | -0.0671323 |
| Q5 (.8-1) | 2920 | -0.19363 | -0.185317 |

## Stage 2: Bonus Metrics

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.889463 |
| log_loss | 0.420432 |
| ece | 0.0226479 |
| brier | 0.134143 |
| part_accuracy | 0.808279 |
| part_all_correct_accuracy | 0.525685 |
| accuracy_lift_over_all_correct | 0.282594 |
| part_accuracy_macro_team | 0.811087 |
| part_accuracy_macro_bonus | 0.806987 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.328051 |
| probability_p10 | 0.0857029 |
| probability_p50 | 0.476895 |
| probability_p90 | 0.934617 |
| mean_predictive_variance | 0.142368 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.509639 |
| ranked_probability_score | 0.117621 |
| bonus_total_score_log_loss | 1.0228 |
| ppb_mae | 2.34918 |
| ranked_probability_score_responses | 8455 |
| bonus_total_score_log_loss_responses | 8455 |

## Match Winner Simulation

| metric | value |
| --- | --- |
| match_winner_accuracy | 0.800875 |
| match_winner_brier | 0.146666 |
| match_games | 457 |
| match_simulations_per_game | 500 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.21016 | 0.24819 | 0.637679 | 0.76678 |
| tossup_correctness | tier | fall | 2817 | 0.21391 | 0.243871 | 0.638985 | 0.748544 |
| tossup_correctness | tier | nationals | 1542 | 0.187368 | 0.249531 | 0.623414 | 0.740346 |
| tossup_correctness | tier | regionals | 1934 | 0.202499 | 0.246997 | 0.644482 | 0.779849 |
| tossup_correctness | tier | winter | 2787 | 0.231033 | 0.252642 | 0.643257 | 0.790768 |
| tossup_correctness | category | Current Events | 125 | 0.213777 | 0.27333 | 0.596744 | 0.813328 |
| tossup_correctness | category | Fine Arts | 1072 | 0.223139 | 0.265591 | 0.604293 | 0.806802 |
| tossup_correctness | category | Geography | 185 | 0.198363 | 0.274814 | 0.618601 | 0.822988 |
| tossup_correctness | category | History | 1443 | 0.202642 | 0.241363 | 0.657061 | 0.747501 |
| tossup_correctness | category | Literature | 1411 | 0.215021 | 0.23712 | 0.632243 | 0.737746 |
| tossup_correctness | category | Mythology | 320 | 0.286473 | 0.275903 | 0.617872 | 0.809141 |
| tossup_correctness | category | Other Academic | 64 | 0.26394 | 0.249252 | 0.561198 | 0.704674 |
| tossup_correctness | category | Philosophy | 312 | 0.244637 | 0.245076 | 0.659032 | 0.728684 |
| tossup_correctness | category | Popular Culture | 104 | 0.344233 | 0.296968 | 0.576705 | 0.893842 |
| tossup_correctness | category | Religion | 358 | 0.212335 | 0.255117 | 0.663776 | 0.764517 |
| tossup_correctness | category | Science | 1431 | 0.190214 | 0.240351 | 0.63576 | 0.761101 |
| tossup_correctness | category | Social Science | 321 | 0.186725 | 0.238095 | 0.663282 | 0.711997 |
| tossup_correctness | category | Unknown | 1934 | 0.202499 | 0.246997 | 0.644482 | 0.779849 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.442386 | 0.383216 | 0.726325 | 1.22005 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.361767 | 0.334822 | 0.692475 | 1.02958 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.257971 | 0.27142 | 0.657118 | 0.830046 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.179522 | 0.225267 | 0.637546 | 0.69438 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.14985 | 0.217878 | 0.613263 | 0.680219 |
| bonus_part_correctness | aggregate | all | 25365 | 0.0226479 | 0.134143 | 0.889463 | 0.420432 |
| bonus_part_correctness | tier | fall | 8094 | 0.0249189 | 0.134159 | 0.886464 | 0.41875 |
| bonus_part_correctness | tier | nationals | 4125 | 0.0328896 | 0.143469 | 0.873366 | 0.446606 |
| bonus_part_correctness | tier | regionals | 5247 | 0.0245118 | 0.131247 | 0.890857 | 0.415153 |
| bonus_part_correctness | tier | winter | 7899 | 0.0284326 | 0.13118 | 0.894574 | 0.411992 |
| bonus_part_correctness | category | Current Events | 243 | 0.0808582 | 0.124165 | 0.901491 | 0.402143 |
| bonus_part_correctness | category | Fine Arts | 2937 | 0.0254797 | 0.143466 | 0.874036 | 0.445567 |
| bonus_part_correctness | category | Geography | 456 | 0.0670855 | 0.137351 | 0.885645 | 0.426159 |
| bonus_part_correctness | category | History | 4050 | 0.0323387 | 0.133912 | 0.891352 | 0.417696 |
| bonus_part_correctness | category | Literature | 4029 | 0.0360909 | 0.13113 | 0.894771 | 0.412663 |
| bonus_part_correctness | category | Mythology | 936 | 0.0378128 | 0.138851 | 0.875484 | 0.431265 |
| bonus_part_correctness | category | Other Academic | 255 | 0.0569278 | 0.116467 | 0.913855 | 0.375869 |
| bonus_part_correctness | category | Philosophy | 948 | 0.0438187 | 0.152476 | 0.860416 | 0.464115 |
| bonus_part_correctness | category | Popular Culture | 285 | 0.0391069 | 0.132615 | 0.887121 | 0.417157 |
| bonus_part_correctness | category | Religion | 1014 | 0.0360784 | 0.12977 | 0.895609 | 0.40957 |
| bonus_part_correctness | category | Science | 4059 | 0.0257755 | 0.133496 | 0.889994 | 0.418861 |
| bonus_part_correctness | category | Social Science | 906 | 0.0521965 | 0.125384 | 0.903649 | 0.394187 |
| bonus_part_correctness | category | Unknown | 5247 | 0.0245118 | 0.131247 | 0.890857 | 0.415153 |
