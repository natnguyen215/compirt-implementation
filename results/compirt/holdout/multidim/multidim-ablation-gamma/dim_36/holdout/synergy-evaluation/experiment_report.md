# CompIRT Experiment Report

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.676358 |
| log_loss | 0.658078 |
| ece | 0.132195 |
| brier | 0.193176 |
| accuracy | 0.736034 |
| all_correct_accuracy | 0.770352 |
| accuracy_lift_over_all_correct | -0.0343184 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.283129 |
| probability_p10 | 0.234268 |
| probability_p50 | 0.807754 |
| probability_p90 | 0.987317 |
| mean_predictive_variance | 0.126714 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0955928 |
| joint_tossup_event_log_loss | 6.49996 |
| buzz_position_mae | 0.139751 |
| buzz_position_median_absolute_error | 0.116545 |
| buzz_position_bias | -0.0289697 |
| survival_events | 65443 |
| joint_tossup_event_log_loss_events | 65443 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.535059 |
| first_buzzer_mean_reciprocal_rank | 0.704524 |
| first_buzzer_log_loss | 1.38691 |
| first_buzzer_events | 64834 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 64834 | -0.0289697 | -0.0402144 |
| Q1 (0-.2) | 1630 | 0.301584 | 0.295255 |
| Q2 (.2-.4) | 7318 | 0.185439 | 0.177059 |
| Q3 (.4-.6) | 15427 | 0.0633652 | 0.0583857 |
| Q4 (.6-.8) | 20477 | -0.0479785 | -0.0448774 |
| Q5 (.8-1) | 19982 | -0.186264 | -0.179019 |

## Stage 2: Bonus Metrics

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.937858 |
| log_loss | 0.380232 |
| ece | 0.0534204 |
| brier | 0.098487 |
| part_accuracy | 0.868572 |
| part_all_correct_accuracy | 0.532399 |
| accuracy_lift_over_all_correct | 0.336173 |
| part_accuracy_macro_team | 0.872746 |
| part_accuracy_macro_bonus | 0.864666 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.399966 |
| probability_p10 | 0.0216508 |
| probability_p50 | 0.722086 |
| probability_p90 | 0.999519 |
| mean_predictive_variance | 0.0829661 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.654647 |
| ranked_probability_score | 0.0953221 |
| bonus_total_score_log_loss | 1.06499 |
| ppb_mae | 2.00028 |
| ranked_probability_score_responses | 60454 |
| bonus_total_score_log_loss_responses | 60454 |

## Synergy Contributions

Each lineup's synergy contribution is the Eq. 10 pairwise sum `sum over pairs i<j of psi_i . psi_j` across its members, added to that team's aggregation logit for every bonus the lineup hears. The `*_synergy_fraction` rows weight each bonus response equally; the `distinct_*` rows count each lineup or team once.

| field | value |
| --- | --- |
| mean_synergy_contribution | 7.26442 |
| median_synergy_contribution | 2.07709 |
| negative_synergy_fraction | 0.366841 |
| positive_synergy_fraction | 0.608777 |

**Read the sign as a fitted offset, not a teamwork measure.** With mostly fixed rosters this term can act as a team-level intercept — for example absorbing the unnormalized Eq. 8 log-sum-exp's growth with roster size — so a predominantly one-signed distribution says as much about the logit's other terms as about the teams. A held-out recombined-roster experiment (Scenario C) is required before interpreting synergy as teamwork.

## Match Winner Simulation

| metric | value |
| --- | --- |
| match_winner_accuracy | 0.758025 |
| match_winner_brier | 0.170224 |
| match_games | 3240 |
| match_simulations_per_game | 500 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 64834 | 0.132195 | 0.193176 | 0.676358 | 0.658078 |
| tossup_correctness | tier | fall | 28687 | 0.14041 | 0.174393 | 0.746364 | 0.535053 |
| tossup_correctness | tier | nationals | 8198 | 0.184824 | 0.217161 | 0.637351 | 0.95353 |
| tossup_correctness | tier | regionals | 14721 | 0.1525 | 0.231486 | 0.654379 | 0.818273 |
| tossup_correctness | tier | winter | 13228 | 0.0981878 | 0.176409 | 0.710533 | 0.563498 |
| tossup_correctness | category | Current Events | 1171 | 0.159227 | 0.197878 | 0.71221 | 0.672615 |
| tossup_correctness | category | Fine Arts | 9692 | 0.139747 | 0.201138 | 0.658504 | 0.693334 |
| tossup_correctness | category | Geography | 1347 | 0.121615 | 0.192908 | 0.713186 | 0.661983 |
| tossup_correctness | category | History | 13047 | 0.130913 | 0.187857 | 0.680635 | 0.647809 |
| tossup_correctness | category | Literature | 12852 | 0.14011 | 0.183252 | 0.657572 | 0.616112 |
| tossup_correctness | category | Mythology | 3054 | 0.123506 | 0.169819 | 0.721251 | 0.578294 |
| tossup_correctness | category | Other Academic | 513 | 0.136227 | 0.195788 | 0.674329 | 0.729803 |
| tossup_correctness | category | Philosophy | 2930 | 0.133206 | 0.190848 | 0.656771 | 0.653125 |
| tossup_correctness | category | Popular Culture | 1165 | 0.275308 | 0.256792 | 0.646766 | 0.768637 |
| tossup_correctness | category | Religion | 3261 | 0.139664 | 0.193863 | 0.684638 | 0.644364 |
| tossup_correctness | category | Science | 12999 | 0.113811 | 0.200313 | 0.690202 | 0.682454 |
| tossup_correctness | category | Social Science | 2803 | 0.118651 | 0.20113 | 0.685085 | 0.704386 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 1630 | 0.314395 | 0.268418 | 0.76308 | 0.805509 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 7318 | 0.253375 | 0.244562 | 0.73588 | 0.761904 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 15427 | 0.14958 | 0.199226 | 0.702156 | 0.64574 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 20477 | 0.0973873 | 0.16854 | 0.677988 | 0.59823 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 19982 | 0.103856 | 0.188793 | 0.660105 | 0.678885 |
| bonus_part_correctness | aggregate | all | 181362 | 0.0534204 | 0.098487 | 0.937858 | 0.380232 |
| bonus_part_correctness | tier | fall | 81663 | 0.0202029 | 0.0866401 | 0.952335 | 0.280447 |
| bonus_part_correctness | tier | nationals | 22782 | 0.166135 | 0.137376 | 0.956051 | 0.606203 |
| bonus_part_correctness | tier | regionals | 39696 | 0.0742996 | 0.104976 | 0.92891 | 0.457687 |
| bonus_part_correctness | tier | winter | 37221 | 0.0637327 | 0.0937559 | 0.9423 | 0.378243 |
| bonus_part_correctness | category | Current Events | 3591 | 0.0392553 | 0.0959615 | 0.936506 | 0.34586 |
| bonus_part_correctness | category | Fine Arts | 27126 | 0.053131 | 0.0988033 | 0.93797 | 0.377394 |
| bonus_part_correctness | category | Geography | 3696 | 0.0629455 | 0.118408 | 0.914254 | 0.459289 |
| bonus_part_correctness | category | History | 36543 | 0.0556778 | 0.100211 | 0.934018 | 0.396571 |
| bonus_part_correctness | category | Literature | 36426 | 0.0552954 | 0.097949 | 0.938231 | 0.386111 |
| bonus_part_correctness | category | Mythology | 8883 | 0.0418235 | 0.0905539 | 0.944178 | 0.345737 |
| bonus_part_correctness | category | Other Academic | 1413 | 0.101357 | 0.115081 | 0.929604 | 0.519041 |
| bonus_part_correctness | category | Philosophy | 7557 | 0.0586466 | 0.0946172 | 0.942993 | 0.374571 |
| bonus_part_correctness | category | Popular Culture | 2745 | 0.0421637 | 0.0991861 | 0.932496 | 0.360224 |
| bonus_part_correctness | category | Religion | 9138 | 0.0508408 | 0.0961345 | 0.942553 | 0.35072 |
| bonus_part_correctness | category | Science | 36261 | 0.053165 | 0.0973746 | 0.940187 | 0.365612 |
| bonus_part_correctness | category | Social Science | 7983 | 0.0598421 | 0.100949 | 0.936115 | 0.393347 |
