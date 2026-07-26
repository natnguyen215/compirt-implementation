# CompIRT Experiment Report

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.669817 |
| log_loss | 0.668453 |
| ece | 0.133223 |
| brier | 0.191571 |
| accuracy | 0.739797 |
| all_correct_accuracy | 0.770352 |
| accuracy_lift_over_all_correct | -0.030555 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.281343 |
| probability_p10 | 0.249335 |
| probability_p50 | 0.82847 |
| probability_p90 | 0.993549 |
| mean_predictive_variance | 0.120807 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0989592 |
| joint_tossup_event_log_loss | 6.5315 |
| buzz_position_mae | 0.143676 |
| buzz_position_median_absolute_error | 0.120099 |
| buzz_position_bias | -0.0338266 |
| survival_events | 65443 |
| joint_tossup_event_log_loss_events | 65443 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.532576 |
| first_buzzer_mean_reciprocal_rank | 0.701978 |
| first_buzzer_log_loss | 1.37835 |
| first_buzzer_events | 64834 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 64834 | -0.0338266 | -0.0427869 |
| Q1 (0-.2) | 1630 | 0.297521 | 0.292844 |
| Q2 (.2-.4) | 7318 | 0.184964 | 0.176655 |
| Q3 (.4-.6) | 15427 | 0.0603513 | 0.0566666 |
| Q4 (.6-.8) | 20477 | -0.0539836 | -0.0466441 |
| Q5 (.8-1) | 19982 | -0.193037 | -0.182743 |

## Stage 2: Bonus Metrics

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.937496 |
| log_loss | 0.40986 |
| ece | 0.0652846 |
| brier | 0.100373 |
| part_accuracy | 0.867337 |
| part_all_correct_accuracy | 0.532399 |
| accuracy_lift_over_all_correct | 0.334938 |
| part_accuracy_macro_team | 0.870562 |
| part_accuracy_macro_bonus | 0.853984 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.408259 |
| probability_p10 | 0.0130806 |
| probability_p50 | 0.770751 |
| probability_p90 | 0.999926 |
| mean_predictive_variance | 0.0744398 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.652959 |
| ranked_probability_score | 0.0973559 |
| bonus_total_score_log_loss | 1.17651 |
| ppb_mae | 2.23292 |
| ranked_probability_score_responses | 60454 |
| bonus_total_score_log_loss_responses | 60454 |

## Synergy Contributions

Each lineup's synergy contribution is the Eq. 10 pairwise sum `sum over pairs i<j of psi_i . psi_j` across its members, added to that team's aggregation logit for every bonus the lineup hears. The `*_synergy_fraction` rows weight each bonus response equally; the `distinct_*` rows count each lineup or team once.

| field | value |
| --- | --- |
| mean_synergy_contribution | 11.0696 |
| median_synergy_contribution | 4.72605 |
| negative_synergy_fraction | 0.285341 |
| positive_synergy_fraction | 0.690277 |

**Read the sign as a fitted offset, not a teamwork measure.** With mostly fixed rosters this term can act as a team-level intercept — for example absorbing the unnormalized Eq. 8 log-sum-exp's growth with roster size — so a predominantly one-signed distribution says as much about the logit's other terms as about the teams. A held-out recombined-roster experiment (Scenario C) is required before interpreting synergy as teamwork.

## Match Winner Simulation

| metric | value |
| --- | --- |
| match_winner_accuracy | 0.776235 |
| match_winner_brier | 0.155704 |
| match_games | 3240 |
| match_simulations_per_game | 500 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 64834 | 0.133223 | 0.191571 | 0.669817 | 0.668453 |
| tossup_correctness | tier | fall | 28687 | 0.133683 | 0.171092 | 0.75106 | 0.525142 |
| tossup_correctness | tier | nationals | 8198 | 0.20251 | 0.225031 | 0.651363 | 1.013 |
| tossup_correctness | tier | regionals | 14721 | 0.164183 | 0.220319 | 0.655607 | 0.790723 |
| tossup_correctness | tier | winter | 13228 | 0.100321 | 0.183252 | 0.703698 | 0.629643 |
| tossup_correctness | category | Current Events | 1171 | 0.134311 | 0.171911 | 0.756603 | 0.570472 |
| tossup_correctness | category | Fine Arts | 9692 | 0.141149 | 0.199705 | 0.652141 | 0.69498 |
| tossup_correctness | category | Geography | 1347 | 0.118806 | 0.184526 | 0.698849 | 0.632733 |
| tossup_correctness | category | History | 13047 | 0.131618 | 0.189795 | 0.666087 | 0.67617 |
| tossup_correctness | category | Literature | 12852 | 0.143273 | 0.183363 | 0.64996 | 0.643294 |
| tossup_correctness | category | Mythology | 3054 | 0.124222 | 0.168102 | 0.705059 | 0.578036 |
| tossup_correctness | category | Other Academic | 513 | 0.124548 | 0.176679 | 0.690638 | 0.647893 |
| tossup_correctness | category | Philosophy | 2930 | 0.142794 | 0.190858 | 0.65941 | 0.66904 |
| tossup_correctness | category | Popular Culture | 1165 | 0.260164 | 0.244952 | 0.66899 | 0.737055 |
| tossup_correctness | category | Religion | 3261 | 0.125011 | 0.189044 | 0.684497 | 0.65609 |
| tossup_correctness | category | Science | 12999 | 0.120061 | 0.199671 | 0.683496 | 0.686537 |
| tossup_correctness | category | Social Science | 2803 | 0.131903 | 0.193167 | 0.686885 | 0.717921 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 1630 | 0.31358 | 0.282538 | 0.725332 | 0.861406 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 7318 | 0.25247 | 0.243321 | 0.723624 | 0.780237 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 15427 | 0.149764 | 0.19677 | 0.691476 | 0.664062 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 20477 | 0.0971659 | 0.164683 | 0.671812 | 0.595774 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 19982 | 0.109387 | 0.188737 | 0.660797 | 0.689642 |
| bonus_part_correctness | aggregate | all | 181362 | 0.0652846 | 0.100373 | 0.937496 | 0.40986 |
| bonus_part_correctness | tier | fall | 81663 | 0.0323689 | 0.0890959 | 0.950112 | 0.289359 |
| bonus_part_correctness | tier | nationals | 22782 | 0.154002 | 0.132324 | 0.955671 | 0.626251 |
| bonus_part_correctness | tier | regionals | 39696 | 0.0854964 | 0.108787 | 0.924593 | 0.535914 |
| bonus_part_correctness | tier | winter | 37221 | 0.0795542 | 0.0965872 | 0.944733 | 0.407355 |
| bonus_part_correctness | category | Current Events | 3591 | 0.0519962 | 0.0974345 | 0.937262 | 0.364365 |
| bonus_part_correctness | category | Fine Arts | 27126 | 0.0654763 | 0.100594 | 0.937778 | 0.409021 |
| bonus_part_correctness | category | Geography | 3696 | 0.0747357 | 0.12092 | 0.91337 | 0.493886 |
| bonus_part_correctness | category | History | 36543 | 0.0670268 | 0.101405 | 0.933729 | 0.427056 |
| bonus_part_correctness | category | Literature | 36426 | 0.0680049 | 0.101101 | 0.936969 | 0.421272 |
| bonus_part_correctness | category | Mythology | 8883 | 0.0548625 | 0.0922074 | 0.944473 | 0.37205 |
| bonus_part_correctness | category | Other Academic | 1413 | 0.105833 | 0.112454 | 0.933355 | 0.552474 |
| bonus_part_correctness | category | Philosophy | 7557 | 0.0683832 | 0.0954619 | 0.944996 | 0.393172 |
| bonus_part_correctness | category | Popular Culture | 2745 | 0.0541288 | 0.10322 | 0.928844 | 0.38805 |
| bonus_part_correctness | category | Religion | 9138 | 0.0607025 | 0.0985306 | 0.941816 | 0.378735 |
| bonus_part_correctness | category | Science | 36261 | 0.0626918 | 0.0990824 | 0.939664 | 0.391711 |
| bonus_part_correctness | category | Social Science | 7983 | 0.0690861 | 0.101982 | 0.936825 | 0.421675 |
