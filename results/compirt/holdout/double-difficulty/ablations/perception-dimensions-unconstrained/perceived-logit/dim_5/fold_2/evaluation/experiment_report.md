# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.552855 |
| log_loss | 0.5906 |
| ece | 0.0925174 |
| brier | 0.188842 |
| accuracy | 0.763746 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.000432105 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.109868 |
| probability_p10 | 0.665827 |
| probability_p50 | 0.870759 |
| probability_p90 | 0.941793 |
| mean_predictive_variance | 0.12529 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.174711 |
| joint_tossup_event_log_loss | 7.73144 |
| buzz_position_mae | 0.335664 |
| buzz_position_median_absolute_error | 0.336204 |
| buzz_position_bias | -0.321998 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.343848 |
| first_buzzer_mean_reciprocal_rank | 0.558609 |
| first_buzzer_log_loss | 1.67591 |
| first_buzzer_events | 9257 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.632494 |
| tossup_scorer_player_top1_accuracy | 0.26887 |
| tossup_scorer_team_top1_accuracy | 0.401919 |
| tossup_game_winner_accuracy | 0.693478 |
| tossup_game_margin_mae | 47.3987 |
| tournament_player_ppg_spearman | 0.597048 |
| tournament_player_ppg_mae | 10.3695 |
| tournament_player_ppg_top10_overlap | 0.582759 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.552855 |
| neg_average_precision | 0.285316 |
| neg_precision | 0.477778 |
| neg_recall | 0.0196977 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0312253 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.22626 |
| no_buzz_calibration_error | 0.213147 |
| no_buzz_brier | 0.0666989 |
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
| overall | 9257 | -0.321998 | -0.336204 |
| Q1 (0-.2) | 183 | 0.184816 | 0.178209 |
| Q2 (.2-.4) | 955 | 0.00770627 | 0.00467373 |
| Q3 (.4-.6) | 2239 | -0.172009 | -0.176275 |
| Q4 (.6-.8) | 2875 | -0.34735 | -0.348353 |
| Q5 (.8-1) | 3005 | -0.545143 | -0.548249 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.0925174 | 0.188842 | 0.552855 | 0.5906 |
| tossup_correctness | tier | fall | 2798 | 0.0809835 | 0.1755 | 0.548163 | 0.554364 |
| tossup_correctness | tier | nationals | 1545 | 0.083886 | 0.206823 | 0.573402 | 0.620731 |
| tossup_correctness | tier | regionals | 2039 | 0.088685 | 0.189772 | 0.539072 | 0.595012 |
| tossup_correctness | tier | winter | 2875 | 0.118629 | 0.191504 | 0.544876 | 0.606546 |
| tossup_correctness | category | Current Events | 129 | 0.176665 | 0.249289 | 0.541374 | 0.730629 |
| tossup_correctness | category | Fine Arts | 1074 | 0.104912 | 0.183899 | 0.552823 | 0.580165 |
| tossup_correctness | category | Geography | 180 | 0.23926 | 0.288156 | 0.597989 | 0.834811 |
| tossup_correctness | category | History | 1454 | 0.0939869 | 0.192641 | 0.547308 | 0.59703 |
| tossup_correctness | category | Literature | 1435 | 0.0766601 | 0.159185 | 0.541706 | 0.519649 |
| tossup_correctness | category | Mythology | 324 | 0.113457 | 0.172724 | 0.562983 | 0.548665 |
| tossup_correctness | category | Other Academic | 71 | 0.224964 | 0.234725 | 0.312636 | 0.738868 |
| tossup_correctness | category | Philosophy | 310 | 0.140512 | 0.200133 | 0.510765 | 0.63732 |
| tossup_correctness | category | Popular Culture | 108 | 0.0374089 | 0.102149 | 0.59375 | 0.354195 |
| tossup_correctness | category | Religion | 361 | 0.138813 | 0.204046 | 0.562009 | 0.63312 |
| tossup_correctness | category | Science | 1445 | 0.0875653 | 0.194822 | 0.572285 | 0.597946 |
| tossup_correctness | category | Social Science | 327 | 0.132696 | 0.214745 | 0.594218 | 0.654224 |
| tossup_correctness | category | Unknown | 2039 | 0.088685 | 0.189772 | 0.539072 | 0.595012 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.111037 | 0.209965 | 0.468867 | 0.647563 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.105396 | 0.211798 | 0.525599 | 0.6373 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.0907473 | 0.194679 | 0.544955 | 0.600923 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.0854891 | 0.173753 | 0.556415 | 0.551214 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.102149 | 0.190347 | 0.561908 | 0.602281 |
