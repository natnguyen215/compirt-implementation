# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-difficulty-three-slice/dim_2/fold_4/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-difficulty-three-slice/dim_2/fold_4`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 2 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 309251 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.612851 |
| log_loss | 0.534115 |
| ece | 0.0554665 |
| brier | 0.174412 |
| accuracy | 0.763862 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | -0.00949299 |
| probability_std | 0.138368 |
| probability_p10 | 0.565978 |
| probability_p50 | 0.78475 |
| probability_p90 | 0.917156 |
| mean_predictive_variance | 0.163373 |
| integrated_brier_score | 0.10304 |
| joint_tossup_event_log_loss | 6.96327 |
| buzz_position_mae | 0.16132 |
| buzz_position_median_absolute_error | 0.147566 |
| buzz_position_bias | -0.064217 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.338188 |
| first_buzzer_mean_reciprocal_rank | 0.550208 |
| first_buzzer_log_loss | 1.71256 |
| first_buzzer_events | 9270 |
| first_buzzer_team_top1_accuracy | 0.637864 |
| tossup_scorer_player_top1_accuracy | 0.299041 |
| tossup_scorer_team_top1_accuracy | 0.472814 |
| tossup_game_winner_accuracy | 0.785558 |
| tossup_game_margin_mae | 34.7412 |
| tournament_player_ppg_spearman | 0.674601 |
| tournament_player_ppg_mae | 9.30955 |
| tournament_player_ppg_top10_overlap | 0.668966 |
| neg_auroc | 0.612851 |
| neg_average_precision | 0.317902 |
| neg_precision | 0.411647 |
| neg_recall | 0.0975726 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0564033 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0882772 |
| no_buzz_calibration_error | 0.0765501 |
| no_buzz_brier | 0.0237849 |
| full_pmf_max_mass_error | 1.44329e-15 |
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
| tossup_correctness | aggregate | all | 9270 | 0.612851 | 0.534115 | 0.0554665 | 0.174412 | 0.763862 | 0.773355 | -0.00949299 | 0.138368 | 0.565978 | 0.78475 | 0.917156 | 0.163373 |
| tossup_correctness | tier | fall | 2876 | 0.574598 | 0.527963 | 0.0751238 | 0.169388 | 0.778512 | 0.793115 | -0.0146036 | 0.13245 | 0.603576 | 0.819361 | 0.932838 | 0.148129 |
| tossup_correctness | tier | nationals | 1579 | 0.63647 | 0.569336 | 0.0568244 | 0.192208 | 0.723876 | 0.729576 | -0.00569981 | 0.142306 | 0.474371 | 0.690621 | 0.851996 | 0.198326 |
| tossup_correctness | tier | regionals | 1990 | 0.617088 | 0.540263 | 0.0438356 | 0.177288 | 0.757789 | 0.765829 | -0.0080402 | 0.132478 | 0.58992 | 0.793984 | 0.915126 | 0.1601 |
| tossup_correctness | tier | winter | 2825 | 0.621999 | 0.516362 | 0.0431809 | 0.167554 | 0.775575 | 0.783009 | -0.00743363 | 0.128034 | 0.589785 | 0.78834 | 0.913844 | 0.16166 |
| tossup_correctness | category | Current Events | 123 | 0.601981 | 0.563963 | 0.115977 | 0.18725 | 0.756098 | 0.764228 | -0.00813008 | 0.138621 | 0.487922 | 0.680039 | 0.84653 | 0.199214 |
| tossup_correctness | category | Fine Arts | 1093 | 0.601188 | 0.541878 | 0.0598636 | 0.176685 | 0.768527 | 0.769442 | -0.000914913 | 0.12258 | 0.619677 | 0.816861 | 0.924614 | 0.148544 |
| tossup_correctness | category | Geography | 191 | 0.724448 | 0.555663 | 0.0705236 | 0.187825 | 0.706806 | 0.691099 | 0.0157068 | 0.151599 | 0.493728 | 0.72481 | 0.882356 | 0.186747 |
| tossup_correctness | category | History | 1469 | 0.636903 | 0.541117 | 0.0490337 | 0.180328 | 0.734513 | 0.758339 | -0.0238257 | 0.138055 | 0.517809 | 0.730165 | 0.8807 | 0.185643 |
| tossup_correctness | category | Literature | 1436 | 0.567246 | 0.500779 | 0.062124 | 0.154972 | 0.809889 | 0.81546 | -0.00557103 | 0.11461 | 0.671842 | 0.862508 | 0.950355 | 0.12792 |
| tossup_correctness | category | Mythology | 325 | 0.580077 | 0.485658 | 0.1249 | 0.156477 | 0.806154 | 0.843077 | -0.0369231 | 0.130932 | 0.533275 | 0.732658 | 0.887624 | 0.185256 |
| tossup_correctness | category | Other Academic | 67 | 0.580863 | 0.571129 | 0.160832 | 0.18927 | 0.776119 | 0.791045 | -0.0149254 | 0.128774 | 0.498589 | 0.664638 | 0.813617 | 0.208391 |
| tossup_correctness | category | Philosophy | 322 | 0.636822 | 0.505583 | 0.0355823 | 0.163753 | 0.785714 | 0.785714 | 0 | 0.117162 | 0.650425 | 0.816051 | 0.93103 | 0.146022 |
| tossup_correctness | category | Popular Culture | 100 | 0.59142 | 0.500421 | 0.237315 | 0.16093 | 0.78 | 0.89 | -0.11 | 0.177808 | 0.448915 | 0.720725 | 0.884529 | 0.185934 |
| tossup_correctness | category | Religion | 365 | 0.611724 | 0.59877 | 0.0784629 | 0.203245 | 0.70137 | 0.723288 | -0.0219178 | 0.141597 | 0.565293 | 0.788297 | 0.912831 | 0.162944 |
| tossup_correctness | category | Science | 1456 | 0.616414 | 0.53266 | 0.067182 | 0.174194 | 0.769231 | 0.76717 | 0.00206044 | 0.139789 | 0.539298 | 0.76025 | 0.884804 | 0.176354 |
| tossup_correctness | category | Social Science | 333 | 0.608596 | 0.574432 | 0.057323 | 0.193283 | 0.726727 | 0.72973 | -0.003003 | 0.126555 | 0.545555 | 0.750782 | 0.873277 | 0.182894 |
| tossup_correctness | category | Unknown | 1990 | 0.617088 | 0.540263 | 0.0438356 | 0.177288 | 0.757789 | 0.765829 | -0.0080402 | 0.132478 | 0.58992 | 0.793984 | 0.915126 | 0.1601 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.585904 | 0.582902 | 0.135854 | 0.19572 | 0.743017 | 0.748603 | -0.00558659 | 0.145228 | 0.46987 | 0.680088 | 0.836174 | 0.202843 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.545706 | 0.597188 | 0.0977456 | 0.202499 | 0.704284 | 0.754441 | -0.0501567 | 0.148114 | 0.467629 | 0.717232 | 0.856919 | 0.191906 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.605608 | 0.544413 | 0.060905 | 0.179595 | 0.75261 | 0.766682 | -0.0140717 | 0.133917 | 0.544899 | 0.751499 | 0.887066 | 0.178039 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.621712 | 0.508607 | 0.0468307 | 0.164207 | 0.786434 | 0.787441 | -0.00100739 | 0.128857 | 0.596481 | 0.798178 | 0.917012 | 0.158728 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.633064 | 0.528759 | 0.0460514 | 0.170443 | 0.770064 | 0.771758 | -0.00169319 | 0.13208 | 0.610958 | 0.823564 | 0.935594 | 0.145476 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1196 | -2.06658 | 0.854034 | -4.46094 | -3.40648 | -2.69611 | -2.14108 | -1.34798 | -0.714779 | 0.0143676 |
| player | theta_2 | 1196 | -1.80075 | 0.899441 | -4.53466 | -3.28773 | -2.41108 | -1.82673 | -1.03461 | -0.446169 | 0.36287 |
| player | theta_norm | 1196 | 2.92529 | 0.7026 | 1.19691 | 1.82633 | 2.41593 | 2.87725 | 3.41832 | 4.13709 | 4.99296 |
| tossup | start_difficulty_d1 | 1240 | -2.18128 | 1.21158 | -4.65326 | -3.77493 | -3.25546 | -2.49264 | -1.07198 | -0.195392 | 0.438445 |
| tossup | start_difficulty_d2 | 1240 | -1.96071 | 1.19647 | -4.59708 | -3.65129 | -2.93527 | -2.24255 | -0.865644 | -0.00621346 | 1.8965 |
| tossup | end_difficulty_d1 | 1240 | -3.26271 | 1.36077 | -8.29323 | -5.27909 | -4.27699 | -3.45396 | -2.05812 | -1.12632 | -0.459545 |
| tossup | end_difficulty_d2 | 1240 | -3.01021 | 1.30615 | -6.55422 | -4.97722 | -3.97493 | -3.27394 | -1.8666 | -0.939317 | 1.13655 |
| tossup | total_drop_d1 | 1240 | 1.08143 | 0.436182 | 0.339983 | 0.661961 | 0.877214 | 0.986946 | 1.16387 | 1.75059 | 5.55644 |
| tossup | total_drop_d2 | 1240 | 1.0495 | 0.313157 | 0.510552 | 0.6681 | 0.889127 | 0.986615 | 1.1304 | 1.58445 | 3.12415 |
| tossup | drop_share_1_d1 | 1240 | 0.35038 | 0.0490422 | 0.216351 | 0.295053 | 0.317508 | 0.336694 | 0.375776 | 0.443423 | 0.597503 |
| tossup | drop_share_2_d1 | 1240 | 0.338293 | 0.0192266 | 0.254116 | 0.306259 | 0.327587 | 0.339159 | 0.349963 | 0.36326 | 0.510492 |
| tossup | drop_share_3_d1 | 1240 | 0.311328 | 0.0445247 | 0.142588 | 0.226921 | 0.28646 | 0.319844 | 0.340654 | 0.370093 | 0.448707 |
| tossup | drop_share_1_d2 | 1240 | 0.344793 | 0.0445985 | 0.212646 | 0.291255 | 0.31587 | 0.33502 | 0.366881 | 0.423444 | 0.682781 |
| tossup | drop_share_2_d2 | 1240 | 0.33977 | 0.0179282 | 0.210514 | 0.309237 | 0.330826 | 0.341188 | 0.349709 | 0.364146 | 0.431403 |
| tossup | drop_share_3_d2 | 1240 | 0.315437 | 0.0423828 | 0.106705 | 0.240668 | 0.292144 | 0.322588 | 0.342138 | 0.372461 | 0.456047 |
| tossup | r_1 | 1240 | 0.525496 | 0.348164 | 0.0329116 | 0.0667181 | 0.178393 | 0.58175 | 0.880472 | 0.946272 | 0.973059 |
| tossup | r_2 | 1240 | 0.474504 | 0.348164 | 0.0269412 | 0.0537277 | 0.119528 | 0.41825 | 0.821607 | 0.933282 | 0.967088 |
| tossup | r_norm | 1240 | 0.859773 | 0.0658408 | 0.707166 | 0.743573 | 0.808743 | 0.865695 | 0.916415 | 0.953024 | 0.973432 |
