# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-3000steps/perceived-difficulty-three-slice/dim_1/fold_4/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-3000steps/perceived-difficulty-three-slice/dim_1/fold_4`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 1 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 300531 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.587846 |
| log_loss | 0.54432 |
| ece | 0.0630534 |
| brier | 0.178911 |
| accuracy | 0.759008 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | -0.0143474 |
| probability_std | 0.134458 |
| probability_p10 | 0.563781 |
| probability_p50 | 0.77891 |
| probability_p90 | 0.909806 |
| mean_predictive_variance | 0.166907 |
| integrated_brier_score | 0.105897 |
| joint_tossup_event_log_loss | 7.02497 |
| buzz_position_mae | 0.164522 |
| buzz_position_median_absolute_error | 0.150686 |
| buzz_position_bias | -0.0640262 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.302913 |
| first_buzzer_mean_reciprocal_rank | 0.522182 |
| first_buzzer_log_loss | 1.75851 |
| first_buzzer_events | 9270 |
| first_buzzer_team_top1_accuracy | 0.618662 |
| tossup_scorer_player_top1_accuracy | 0.276652 |
| tossup_scorer_team_top1_accuracy | 0.45565 |
| tossup_game_winner_accuracy | 0.730853 |
| tossup_game_margin_mae | 39.177 |
| tournament_player_ppg_spearman | 0.617237 |
| tournament_player_ppg_mae | 10.4355 |
| tournament_player_ppg_top10_overlap | 0.610345 |
| neg_auroc | 0.587846 |
| neg_average_precision | 0.290012 |
| neg_precision | 0.35512 |
| neg_recall | 0.0775821 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0577407 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0888938 |
| no_buzz_calibration_error | 0.0771667 |
| no_buzz_brier | 0.0231966 |
| full_pmf_max_mass_error | 1.33227e-15 |
| tossup_outcome_events | 9380 |
| first_buzzer_team_top1_accuracy_events | 9270 |
| tossup_scorer_player_top1_accuracy_events | 9380 |
| tossup_scorer_team_top1_accuracy_events | 9380 |
| tossup_game_winner_accuracy_games | 457 |
| tossup_game_margin_mae_games | 469 |
| tournament_player_ppg_tournaments | 29 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.587846 | 0.54432 | 0.0630534 | 0.178911 | 0.759008 | 0.773355 | -0.0143474 | 0.134458 | 0.563781 | 0.77891 | 0.909806 | 0.166907 |
| tossup_correctness | tier | fall | 2876 | 0.571341 | 0.533929 | 0.0838459 | 0.174605 | 0.769124 | 0.793115 | -0.0239917 | 0.142321 | 0.537485 | 0.767682 | 0.905053 | 0.171571 |
| tossup_correctness | tier | nationals | 1579 | 0.624652 | 0.581887 | 0.0673327 | 0.194726 | 0.727676 | 0.729576 | -0.00189994 | 0.133048 | 0.588619 | 0.801936 | 0.921868 | 0.156043 |
| tossup_correctness | tier | regionals | 1990 | 0.592597 | 0.55011 | 0.0609593 | 0.181535 | 0.749749 | 0.765829 | -0.0160804 | 0.132949 | 0.556297 | 0.764184 | 0.892329 | 0.174389 |
| tossup_correctness | tier | winter | 2825 | 0.588947 | 0.529823 | 0.0570037 | 0.172606 | 0.772743 | 0.783009 | -0.0102655 | 0.124984 | 0.592007 | 0.784685 | 0.914511 | 0.162961 |
| tossup_correctness | category | Current Events | 123 | 0.60675 | 0.569946 | 0.121234 | 0.192034 | 0.723577 | 0.764228 | -0.0406504 | 0.154533 | 0.433773 | 0.673502 | 0.851852 | 0.200179 |
| tossup_correctness | category | Fine Arts | 1093 | 0.597475 | 0.54424 | 0.0629875 | 0.178349 | 0.768527 | 0.769442 | -0.000914913 | 0.107262 | 0.662784 | 0.823847 | 0.921258 | 0.146142 |
| tossup_correctness | category | Geography | 191 | 0.749615 | 0.538874 | 0.10432 | 0.179655 | 0.717277 | 0.691099 | 0.026178 | 0.146336 | 0.501702 | 0.713009 | 0.8789 | 0.189302 |
| tossup_correctness | category | History | 1469 | 0.59357 | 0.562906 | 0.0601917 | 0.189283 | 0.724302 | 0.758339 | -0.0340368 | 0.139602 | 0.519239 | 0.742927 | 0.885197 | 0.181449 |
| tossup_correctness | category | Literature | 1436 | 0.5585 | 0.497596 | 0.0625352 | 0.155189 | 0.812674 | 0.81546 | -0.00278552 | 0.0999596 | 0.694909 | 0.854009 | 0.942262 | 0.129252 |
| tossup_correctness | category | Mythology | 325 | 0.532417 | 0.49905 | 0.125865 | 0.161661 | 0.787692 | 0.843077 | -0.0553846 | 0.130203 | 0.544072 | 0.732194 | 0.889732 | 0.185866 |
| tossup_correctness | category | Other Academic | 67 | 0.566038 | 0.567161 | 0.120354 | 0.185725 | 0.746269 | 0.791045 | -0.0447761 | 0.144048 | 0.499657 | 0.728243 | 0.873521 | 0.188549 |
| tossup_correctness | category | Philosophy | 322 | 0.624678 | 0.511663 | 0.0465009 | 0.165497 | 0.779503 | 0.785714 | -0.00621118 | 0.104713 | 0.67152 | 0.828252 | 0.924572 | 0.142467 |
| tossup_correctness | category | Popular Culture | 100 | 0.594484 | 0.538338 | 0.27873 | 0.176871 | 0.76 | 0.89 | -0.13 | 0.175695 | 0.399582 | 0.688376 | 0.855909 | 0.198198 |
| tossup_correctness | category | Religion | 365 | 0.597772 | 0.609448 | 0.0840146 | 0.207792 | 0.693151 | 0.723288 | -0.030137 | 0.137583 | 0.565412 | 0.797229 | 0.916185 | 0.159456 |
| tossup_correctness | category | Science | 1456 | 0.571614 | 0.55129 | 0.085563 | 0.182147 | 0.771291 | 0.76717 | 0.00412088 | 0.127891 | 0.545528 | 0.73326 | 0.876817 | 0.186549 |
| tossup_correctness | category | Social Science | 333 | 0.566895 | 0.594241 | 0.0627164 | 0.199578 | 0.714715 | 0.72973 | -0.015015 | 0.127442 | 0.564049 | 0.756967 | 0.892174 | 0.177107 |
| tossup_correctness | category | Unknown | 1990 | 0.592597 | 0.55011 | 0.0609593 | 0.181535 | 0.749749 | 0.765829 | -0.0160804 | 0.132949 | 0.556297 | 0.764184 | 0.892329 | 0.174389 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.566003 | 0.59529 | 0.145329 | 0.20164 | 0.72067 | 0.748603 | -0.027933 | 0.140235 | 0.430676 | 0.669293 | 0.804376 | 0.210527 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.523964 | 0.610936 | 0.1106 | 0.209578 | 0.6907 | 0.754441 | -0.0637409 | 0.144372 | 0.468347 | 0.685812 | 0.845065 | 0.200814 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.57865 | 0.55634 | 0.0738245 | 0.185132 | 0.745347 | 0.766682 | -0.0213345 | 0.132049 | 0.530023 | 0.732704 | 0.871298 | 0.186789 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.601665 | 0.516387 | 0.0504527 | 0.167643 | 0.780725 | 0.787441 | -0.00671592 | 0.12219 | 0.591033 | 0.788471 | 0.905474 | 0.164226 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.61148 | 0.538845 | 0.0553259 | 0.174317 | 0.771758 | 0.771758 | 0 | 0.114824 | 0.650533 | 0.834211 | 0.932196 | 0.141145 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1196 | -2.26247 | 0.627631 | -4.38179 | -3.3132 | -2.67715 | -2.24476 | -1.82979 | -1.23089 | -0.448489 |
| player | theta_norm | 1196 | 2.26247 | 0.627631 | 0.448489 | 1.23089 | 1.82979 | 2.24476 | 2.67715 | 3.3132 | 4.38179 |
| tossup | start_difficulty_d1 | 1240 | -2.96058 | 0.43129 | -4.17614 | -3.61155 | -3.27229 | -2.98824 | -2.67072 | -2.229 | -1.4326 |
| tossup | end_difficulty_d1 | 1240 | -3.96079 | 0.689196 | -7.05797 | -5.13092 | -4.3921 | -3.93033 | -3.48905 | -2.89933 | -2.00148 |
| tossup | total_drop_d1 | 1240 | 1.00021 | 0.413069 | 0.351121 | 0.528814 | 0.715436 | 0.91604 | 1.16728 | 1.74935 | 3.83577 |
| tossup | drop_share_1_d1 | 1240 | 0.370457 | 0.0604095 | 0.178602 | 0.27286 | 0.330502 | 0.373389 | 0.409292 | 0.470598 | 0.562998 |
| tossup | drop_share_2_d1 | 1240 | 0.332 | 0.0249538 | 0.251153 | 0.297589 | 0.317256 | 0.32983 | 0.341834 | 0.376311 | 0.519963 |
| tossup | drop_share_3_d1 | 1240 | 0.297543 | 0.0603118 | 0.133915 | 0.206417 | 0.256006 | 0.292804 | 0.335322 | 0.404266 | 0.498381 |
| tossup | r_1 | 1240 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| tossup | r_norm | 1240 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
