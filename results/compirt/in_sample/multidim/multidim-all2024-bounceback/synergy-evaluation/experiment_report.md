# CompIRT Experiment Report

**Evaluation regime: in-sample fit.** Player and question parameters were estimated on the same observations these metrics score, so they are optimization and inspection diagnostics, not generalization estimates.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.700393 |
| log_loss | 0.573395 |
| ece | 0.130664 |
| brier | 0.191409 |
| accuracy | 0.716847 |
| all_correct_accuracy | 0.767271 |
| accuracy_lift_over_all_correct | -0.0504237 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.252523 |
| probability_p10 | 0.245086 |
| probability_p50 | 0.704809 |
| probability_p90 | 0.926538 |
| mean_predictive_variance | 0.165552 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0867061 |
| joint_tossup_event_log_loss | 6.11618 |
| buzz_position_mae | 0.134574 |
| buzz_position_median_absolute_error | 0.11554 |
| buzz_position_bias | -0.0302251 |
| survival_events | 48612 |
| joint_tossup_event_log_loss_events | 48612 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.477647 |
| first_buzzer_mean_reciprocal_rank | 0.667782 |
| first_buzzer_log_loss | 1.36117 |
| first_buzzer_events | 47914 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 47914 | -0.0302251 | -0.0463086 |
| Q1 (0-.2) | 943 | 0.338508 | 0.341074 |
| Q2 (.2-.4) | 4869 | 0.194123 | 0.188057 |
| Q3 (.4-.6) | 11467 | 0.064071 | 0.0601305 |
| Q4 (.6-.8) | 15035 | -0.050435 | -0.0494119 |
| Q5 (.8-1) | 15600 | -0.172373 | -0.16577 |

## Stage 2: Bonus Metrics

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.934156 |
| log_loss | 0.337141 |
| ece | 0.0389809 |
| brier | 0.104816 |
| part_accuracy | 0.852788 |
| part_all_correct_accuracy | 0.520489 |
| accuracy_lift_over_all_correct | 0.332299 |
| part_accuracy_macro_team | 0.855759 |
| part_accuracy_macro_game | 0.853329 |
| part_accuracy_macro_bonus | 0.856721 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.352231 |
| probability_p10 | 0.0544692 |
| probability_p50 | 0.466957 |
| probability_p90 | 0.964735 |
| mean_predictive_variance | 0.125926 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.612471 |
| ranked_probability_score | 0.0936624 |
| bonus_total_score_log_loss | 0.843012 |
| ppb_mae | 0.8459 |
| ranked_probability_score_responses | 44487 |
| bonus_total_score_log_loss_responses | 44487 |

## Synergy Contributions

Each lineup's synergy contribution is the Eq. 10 pairwise sum `sum over pairs i<j of psi_i . psi_j` across its members, added to that team's aggregation logit for every bonus the lineup hears. The `*_synergy_fraction` rows weight each bonus response equally; the `distinct_*` rows count each lineup or team once.

| field | value |
| --- | --- |
| mean_synergy_contribution | -0.586766 |
| median_synergy_contribution | -0.523045 |
| negative_synergy_fraction | 0.737406 |
| positive_synergy_fraction | 0.231191 |

**Read the sign as a fitted offset, not a teamwork measure.** With mostly fixed rosters this term can act as a team-level intercept — for example absorbing the unnormalized Eq. 8 log-sum-exp's growth with roster size — so a predominantly one-signed distribution says as much about the logit's other terms as about the teams. A held-out recombined-roster experiment (Scenario C) is required before interpreting synergy as teamwork.

## Match Winner Simulation

| metric | value |
| --- | --- |
| match_winner_accuracy | 0.81071 |
| match_winner_brier | 0.127923 |
| match_games | 2409 |
| match_simulations_per_game | 500 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 47914 | 0.130664 | 0.191409 | 0.700393 | 0.573395 |
| tossup_correctness | tier | fall | 14760 | 0.138184 | 0.183068 | 0.709766 | 0.550494 |
| tossup_correctness | tier | nationals | 7940 | 0.103321 | 0.200601 | 0.681576 | 0.59896 |
| tossup_correctness | tier | regionals | 10202 | 0.130243 | 0.195191 | 0.696916 | 0.587214 |
| tossup_correctness | tier | winter | 15012 | 0.146072 | 0.192178 | 0.710562 | 0.573 |
| tossup_correctness | category | Current Events | 640 | 0.149833 | 0.216164 | 0.667885 | 0.632752 |
| tossup_correctness | category | Fine Arts | 5640 | 0.130906 | 0.191796 | 0.706464 | 0.570029 |
| tossup_correctness | category | Geography | 972 | 0.126616 | 0.221443 | 0.695818 | 0.636075 |
| tossup_correctness | category | History | 7599 | 0.120783 | 0.180789 | 0.723043 | 0.546216 |
| tossup_correctness | category | Literature | 7469 | 0.140158 | 0.18603 | 0.673561 | 0.563151 |
| tossup_correctness | category | Mythology | 1692 | 0.191896 | 0.198416 | 0.667496 | 0.594701 |
| tossup_correctness | category | Other Academic | 357 | 0.169638 | 0.206225 | 0.689315 | 0.605896 |
| tossup_correctness | category | Philosophy | 1649 | 0.138835 | 0.186425 | 0.716186 | 0.554077 |
| tossup_correctness | category | Popular Culture | 538 | 0.283555 | 0.235957 | 0.591044 | 0.682558 |
| tossup_correctness | category | Religion | 1889 | 0.120802 | 0.198482 | 0.71006 | 0.58871 |
| tossup_correctness | category | Science | 7556 | 0.110863 | 0.188518 | 0.704125 | 0.564972 |
| tossup_correctness | category | Social Science | 1711 | 0.120958 | 0.19764 | 0.707738 | 0.586451 |
| tossup_correctness | category | Unknown | 10202 | 0.130243 | 0.195191 | 0.696916 | 0.587214 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 943 | 0.371424 | 0.322584 | 0.731444 | 0.924429 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 4869 | 0.286839 | 0.262255 | 0.735459 | 0.753998 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 11467 | 0.195524 | 0.210457 | 0.723392 | 0.617188 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 15035 | 0.119634 | 0.171053 | 0.722738 | 0.516647 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 15600 | 0.0504597 | 0.166985 | 0.695734 | 0.518309 |
| bonus_part_correctness | aggregate | all | 133461 | 0.0389809 | 0.104816 | 0.934156 | 0.337141 |
| bonus_part_correctness | tier | fall | 42336 | 0.0321918 | 0.110348 | 0.924027 | 0.350733 |
| bonus_part_correctness | tier | nationals | 21051 | 0.0581231 | 0.09878 | 0.943506 | 0.321462 |
| bonus_part_correctness | tier | regionals | 27762 | 0.048858 | 0.100224 | 0.941325 | 0.325344 |
| bonus_part_correctness | tier | winter | 42312 | 0.0326926 | 0.105297 | 0.931853 | 0.339083 |
| bonus_part_correctness | category | Current Events | 1281 | 0.0387125 | 0.102868 | 0.934845 | 0.334233 |
| bonus_part_correctness | category | Fine Arts | 15525 | 0.0360238 | 0.112679 | 0.923454 | 0.359311 |
| bonus_part_correctness | category | Geography | 2427 | 0.0397364 | 0.108569 | 0.926068 | 0.345887 |
| bonus_part_correctness | category | History | 21273 | 0.0369347 | 0.105532 | 0.93259 | 0.338313 |
| bonus_part_correctness | category | Literature | 21312 | 0.039575 | 0.101034 | 0.938418 | 0.326987 |
| bonus_part_correctness | category | Mythology | 4923 | 0.0388573 | 0.115261 | 0.916646 | 0.363693 |
| bonus_part_correctness | category | Other Academic | 1272 | 0.0465913 | 0.0931649 | 0.946737 | 0.305945 |
| bonus_part_correctness | category | Philosophy | 4989 | 0.0454535 | 0.108785 | 0.930028 | 0.348417 |
| bonus_part_correctness | category | Popular Culture | 1536 | 0.0311905 | 0.122529 | 0.904175 | 0.379762 |
| bonus_part_correctness | category | Religion | 5280 | 0.0383389 | 0.103051 | 0.93563 | 0.332238 |
| bonus_part_correctness | category | Science | 21183 | 0.0353766 | 0.106149 | 0.931481 | 0.34097 |
| bonus_part_correctness | category | Social Science | 4698 | 0.0358686 | 0.0966438 | 0.942173 | 0.313583 |
| bonus_part_correctness | category | Unknown | 27762 | 0.048858 | 0.100224 | 0.941325 | 0.325344 |
