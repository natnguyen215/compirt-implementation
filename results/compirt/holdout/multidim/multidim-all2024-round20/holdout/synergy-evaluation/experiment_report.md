# CompIRT Experiment Report

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.691036 |
| log_loss | 0.596193 |
| ece | 0.133886 |
| brier | 0.200237 |
| accuracy | 0.70701 |
| all_correct_accuracy | 0.754791 |
| accuracy_lift_over_all_correct | -0.0477816 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.249098 |
| probability_p10 | 0.235105 |
| probability_p50 | 0.68194 |
| probability_p90 | 0.910628 |
| mean_predictive_variance | 0.172049 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0809954 |
| joint_tossup_event_log_loss | 6.10918 |
| buzz_position_mae | 0.129597 |
| buzz_position_median_absolute_error | 0.109263 |
| buzz_position_bias | -0.0479821 |
| survival_events | 7740 |
| joint_tossup_event_log_loss_events | 7740 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.490024 |
| first_buzzer_mean_reciprocal_rank | 0.677516 |
| first_buzzer_log_loss | 1.35285 |
| first_buzzer_events | 7618 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 7618 | -0.0479821 | -0.0567994 |
| Q1 (0-.2) | 125 | 0.285846 | 0.268524 |
| Q2 (.2-.4) | 769 | 0.160893 | 0.155704 |
| Q3 (.4-.6) | 1822 | 0.0391632 | 0.0344518 |
| Q4 (.6-.8) | 2322 | -0.0574331 | -0.0536443 |
| Q5 (.8-1) | 2580 | -0.17945 | -0.174396 |

## Stage 2: Bonus Metrics

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.950372 |
| log_loss | 0.337456 |
| ece | 0.096014 |
| brier | 0.101071 |
| part_accuracy | 0.869105 |
| part_all_correct_accuracy | 0.509829 |
| accuracy_lift_over_all_correct | 0.359276 |
| part_accuracy_macro_team | 0.87753 |
| part_accuracy_macro_game | 0.869829 |
| part_accuracy_macro_bonus | 0.879982 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.318428 |
| probability_p10 | 0.0639274 |
| probability_p50 | 0.422935 |
| probability_p90 | 0.903017 |
| mean_predictive_variance | 0.146904 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.65438 |
| ranked_probability_score | 0.0906584 |
| bonus_total_score_log_loss | 0.831634 |
| ppb_mae | 1.8091 |
| ranked_probability_score_responses | 7054 |
| bonus_total_score_log_loss_responses | 7054 |

## Synergy Contributions

Each lineup's synergy contribution is the Eq. 10 pairwise sum `sum over pairs i<j of psi_i . psi_j` across its members, added to that team's aggregation logit for every bonus the lineup hears. The `*_synergy_fraction` rows weight each bonus response equally; the `distinct_*` rows count each lineup or team once.

| field | value |
| --- | --- |
| mean_synergy_contribution | -0.486045 |
| median_synergy_contribution | -0.331023 |
| negative_synergy_fraction | 0.730082 |
| positive_synergy_fraction | 0.240573 |

**Read the sign as a fitted offset, not a teamwork measure.** With mostly fixed rosters this term can act as a team-level intercept — for example absorbing the unnormalized Eq. 8 log-sum-exp's growth with roster size — so a predominantly one-signed distribution says as much about the logit's other terms as about the teams. A held-out recombined-roster experiment (Scenario C) is required before interpreting synergy as teamwork.

## Match Winner Simulation

| metric | value |
| --- | --- |
| match_winner_accuracy | 0.75 |
| match_winner_brier | 0.162926 |
| match_games | 384 |
| match_simulations_per_game | 500 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 7618 | 0.133886 | 0.200237 | 0.691036 | 0.596193 |
| tossup_correctness | tier | fall | 2044 | 0.159288 | 0.204428 | 0.688582 | 0.604007 |
| tossup_correctness | tier | nationals | 1870 | 0.110468 | 0.217795 | 0.65859 | 0.643291 |
| tossup_correctness | tier | regionals | 1376 | 0.123589 | 0.181342 | 0.727185 | 0.546883 |
| tossup_correctness | tier | winter | 2328 | 0.162051 | 0.19362 | 0.71947 | 0.580645 |
| tossup_correctness | category | Current Events | 95 | 0.193034 | 0.219976 | 0.647715 | 0.630094 |
| tossup_correctness | category | Fine Arts | 936 | 0.165827 | 0.209083 | 0.685671 | 0.619078 |
| tossup_correctness | category | Geography | 182 | 0.128629 | 0.248373 | 0.639031 | 0.695349 |
| tossup_correctness | category | History | 1258 | 0.137405 | 0.214777 | 0.657603 | 0.636513 |
| tossup_correctness | category | Literature | 1229 | 0.131428 | 0.190012 | 0.692454 | 0.573148 |
| tossup_correctness | category | Mythology | 269 | 0.219128 | 0.202232 | 0.662831 | 0.601796 |
| tossup_correctness | category | Other Academic | 75 | 0.187369 | 0.232933 | 0.583686 | 0.694079 |
| tossup_correctness | category | Philosophy | 257 | 0.139065 | 0.208433 | 0.665344 | 0.619557 |
| tossup_correctness | category | Popular Culture | 73 | 0.329785 | 0.269316 | 0.640762 | 0.77683 |
| tossup_correctness | category | Religion | 314 | 0.120118 | 0.191399 | 0.725397 | 0.566584 |
| tossup_correctness | category | Science | 1252 | 0.109677 | 0.196341 | 0.703939 | 0.587487 |
| tossup_correctness | category | Social Science | 302 | 0.156256 | 0.196496 | 0.714956 | 0.57937 |
| tossup_correctness | category | Unknown | 1376 | 0.123589 | 0.181342 | 0.727185 | 0.546883 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 125 | 0.309199 | 0.286589 | 0.715366 | 0.802629 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 769 | 0.288615 | 0.262748 | 0.745946 | 0.753157 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 1822 | 0.204327 | 0.220032 | 0.697293 | 0.648229 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2322 | 0.109272 | 0.181753 | 0.714774 | 0.544207 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2580 | 0.0626942 | 0.180077 | 0.677748 | 0.549446 |
| bonus_part_correctness | aggregate | all | 21162 | 0.096014 | 0.101071 | 0.950372 | 0.337456 |
| bonus_part_correctness | tier | fall | 5877 | 0.0974791 | 0.104783 | 0.94427 | 0.351657 |
| bonus_part_correctness | tier | nationals | 4923 | 0.0608784 | 0.0951556 | 0.946681 | 0.311085 |
| bonus_part_correctness | tier | regionals | 3873 | 0.120575 | 0.098915 | 0.959981 | 0.332733 |
| bonus_part_correctness | tier | winter | 6489 | 0.11791 | 0.103484 | 0.952876 | 0.347418 |
| bonus_part_correctness | category | Current Events | 189 | 0.133519 | 0.0917641 | 0.964778 | 0.319765 |
| bonus_part_correctness | category | Fine Arts | 2508 | 0.0881022 | 0.108724 | 0.941309 | 0.356952 |
| bonus_part_correctness | category | Geography | 363 | 0.108781 | 0.105313 | 0.948083 | 0.348042 |
| bonus_part_correctness | category | History | 3456 | 0.0935288 | 0.104714 | 0.94476 | 0.347143 |
| bonus_part_correctness | category | Literature | 3555 | 0.0899118 | 0.0975041 | 0.952436 | 0.328382 |
| bonus_part_correctness | category | Mythology | 777 | 0.102924 | 0.107371 | 0.939167 | 0.358299 |
| bonus_part_correctness | category | Other Academic | 249 | 0.0969429 | 0.0808033 | 0.964711 | 0.275568 |
| bonus_part_correctness | category | Philosophy | 858 | 0.0900735 | 0.0934524 | 0.957101 | 0.313674 |
| bonus_part_correctness | category | Popular Culture | 204 | 0.086462 | 0.100617 | 0.937857 | 0.329408 |
| bonus_part_correctness | category | Religion | 870 | 0.0858637 | 0.105582 | 0.941502 | 0.348156 |
| bonus_part_correctness | category | Science | 3468 | 0.0920057 | 0.100448 | 0.949688 | 0.33604 |
| bonus_part_correctness | category | Social Science | 792 | 0.0850555 | 0.0941069 | 0.952602 | 0.317924 |
| bonus_part_correctness | category | Unknown | 3873 | 0.120575 | 0.098915 | 0.959981 | 0.332733 |
