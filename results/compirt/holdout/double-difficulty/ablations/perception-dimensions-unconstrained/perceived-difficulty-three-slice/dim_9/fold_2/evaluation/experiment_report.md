# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.659816 |
| log_loss | 0.516268 |
| ece | 0.0158539 |
| brier | 0.168721 |
| accuracy | 0.768608 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | 0.00442908 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.109551 |
| probability_p10 | 0.62005 |
| probability_p50 | 0.793076 |
| probability_p90 | 0.895646 |
| mean_predictive_variance | 0.163329 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.101818 |
| joint_tossup_event_log_loss | 6.88314 |
| buzz_position_mae | 0.161311 |
| buzz_position_median_absolute_error | 0.14566 |
| buzz_position_bias | -0.0695725 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.355515 |
| first_buzzer_mean_reciprocal_rank | 0.567765 |
| first_buzzer_log_loss | 1.66024 |
| first_buzzer_events | 9257 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.659177 |
| tossup_scorer_player_top1_accuracy | 0.326013 |
| tossup_scorer_team_top1_accuracy | 0.501279 |
| tossup_game_winner_accuracy | 0.791304 |
| tossup_game_margin_mae | 35.8221 |
| tournament_player_ppg_spearman | 0.692298 |
| tournament_player_ppg_mae | 8.77418 |
| tournament_player_ppg_top10_overlap | 0.644828 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.659816 |
| neg_average_precision | 0.385001 |
| neg_precision | 0.608466 |
| neg_recall | 0.0526798 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0547535 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0921368 |
| no_buzz_calibration_error | 0.0790238 |
| no_buzz_brier | 0.0255927 |
| full_pmf_max_mass_error | 1.33227e-15 |
| tossup_outcome_events | 9380 |
| first_buzzer_team_top1_accuracy_events | 9257 |
| tossup_scorer_player_top1_accuracy_events | 9380 |
| tossup_scorer_team_top1_accuracy_events | 9380 |
| tossup_game_winner_accuracy_games | 460 |
| tossup_game_margin_mae_games | 469 |
| tournament_player_ppg_tournaments | 29 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9257 | -0.0695725 | -0.0845406 |
| Q1 (0-.2) | 183 | 0.376754 | 0.386002 |
| Q2 (.2-.4) | 955 | 0.201319 | 0.203084 |
| Q3 (.4-.6) | 2239 | 0.0468206 | 0.0468785 |
| Q4 (.6-.8) | 2875 | -0.0923098 | -0.0867003 |
| Q5 (.8-1) | 3005 | -0.247813 | -0.247925 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.0158539 | 0.168721 | 0.659816 | 0.516268 |
| tossup_correctness | tier | fall | 2798 | 0.010455 | 0.158183 | 0.663404 | 0.490989 |
| tossup_correctness | tier | nationals | 1545 | 0.0449163 | 0.187606 | 0.677048 | 0.557629 |
| tossup_correctness | tier | regionals | 2039 | 0.026286 | 0.171836 | 0.636283 | 0.524771 |
| tossup_correctness | tier | winter | 2875 | 0.0311686 | 0.166617 | 0.661332 | 0.512611 |
| tossup_correctness | category | Current Events | 129 | 0.0661875 | 0.211094 | 0.659275 | 0.611587 |
| tossup_correctness | category | Fine Arts | 1074 | 0.0256389 | 0.167019 | 0.640613 | 0.512207 |
| tossup_correctness | category | Geography | 180 | 0.113966 | 0.214965 | 0.717326 | 0.626629 |
| tossup_correctness | category | History | 1454 | 0.0246514 | 0.172542 | 0.65765 | 0.524004 |
| tossup_correctness | category | Literature | 1435 | 0.035516 | 0.145992 | 0.637604 | 0.466402 |
| tossup_correctness | category | Mythology | 324 | 0.0388866 | 0.156747 | 0.643127 | 0.488289 |
| tossup_correctness | category | Other Academic | 71 | 0.146024 | 0.200736 | 0.415033 | 0.595556 |
| tossup_correctness | category | Philosophy | 310 | 0.0288986 | 0.170042 | 0.673271 | 0.51576 |
| tossup_correctness | category | Popular Culture | 108 | 0.120517 | 0.12086 | 0.546875 | 0.407425 |
| tossup_correctness | category | Religion | 361 | 0.0218649 | 0.181506 | 0.641069 | 0.545459 |
| tossup_correctness | category | Science | 1445 | 0.0369747 | 0.172242 | 0.69981 | 0.521836 |
| tossup_correctness | category | Social Science | 327 | 0.0470189 | 0.185252 | 0.681591 | 0.552761 |
| tossup_correctness | category | Unknown | 2039 | 0.026286 | 0.171836 | 0.636283 | 0.524771 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.0606656 | 0.192975 | 0.599969 | 0.574876 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.0244194 | 0.186081 | 0.65337 | 0.556495 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.0113985 | 0.172187 | 0.675743 | 0.522567 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.0243331 | 0.15815 | 0.654055 | 0.491449 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.024841 | 0.169256 | 0.656668 | 0.518966 |
