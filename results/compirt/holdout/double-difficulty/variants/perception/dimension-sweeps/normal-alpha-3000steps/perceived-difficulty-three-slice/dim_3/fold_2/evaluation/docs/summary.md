# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-3000steps/perceived-difficulty-three-slice/dim_3/fold_2/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-3000steps/perceived-difficulty-three-slice/dim_3/fold_2`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 315039 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.642424 |
| log_loss | 0.526071 |
| ece | 0.0348814 |
| brier | 0.172193 |
| accuracy | 0.76299 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.00118829 |
| probability_std | 0.130481 |
| probability_p10 | 0.577156 |
| probability_p50 | 0.786604 |
| probability_p90 | 0.905972 |
| mean_predictive_variance | 0.165049 |
| integrated_brier_score | 0.102429 |
| joint_tossup_event_log_loss | 6.89836 |
| buzz_position_mae | 0.159907 |
| buzz_position_median_absolute_error | 0.143293 |
| buzz_position_bias | -0.0655287 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.356163 |
| first_buzzer_mean_reciprocal_rank | 0.567239 |
| first_buzzer_log_loss | 1.66271 |
| first_buzzer_events | 9257 |
| first_buzzer_team_top1_accuracy | 0.660257 |
| tossup_scorer_player_top1_accuracy | 0.317484 |
| tossup_scorer_team_top1_accuracy | 0.488486 |
| tossup_game_winner_accuracy | 0.78913 |
| tossup_game_margin_mae | 36.5438 |
| tournament_player_ppg_spearman | 0.697696 |
| tournament_player_ppg_mae | 8.74165 |
| tournament_player_ppg_top10_overlap | 0.665517 |
| neg_auroc | 0.642424 |
| neg_average_precision | 0.364892 |
| neg_precision | 0.487059 |
| neg_recall | 0.0948236 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0568121 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0919313 |
| no_buzz_calibration_error | 0.0788183 |
| no_buzz_brier | 0.0249724 |
| full_pmf_max_mass_error | 1.33227e-15 |
| tossup_outcome_events | 9380 |
| first_buzzer_team_top1_accuracy_events | 9257 |
| tossup_scorer_player_top1_accuracy_events | 9380 |
| tossup_scorer_team_top1_accuracy_events | 9380 |
| tossup_game_winner_accuracy_games | 460 |
| tossup_game_margin_mae_games | 469 |
| tournament_player_ppg_tournaments | 29 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.642424 | 0.526071 | 0.0348814 | 0.172193 | 0.76299 | 0.764178 | -0.00118829 | 0.130481 | 0.577156 | 0.786604 | 0.905972 | 0.165049 |
| tossup_correctness | tier | fall | 2798 | 0.624331 | 0.508263 | 0.0368295 | 0.163418 | 0.784132 | 0.785204 | -0.00107219 | 0.11047 | 0.648189 | 0.824821 | 0.920525 | 0.14692 |
| tossup_correctness | tier | nationals | 1545 | 0.679859 | 0.556465 | 0.0499096 | 0.187687 | 0.719094 | 0.721036 | -0.00194175 | 0.129311 | 0.50109 | 0.681513 | 0.836541 | 0.20391 |
| tossup_correctness | tier | regionals | 2039 | 0.607828 | 0.543434 | 0.0503153 | 0.17827 | 0.758215 | 0.762138 | -0.00392349 | 0.127072 | 0.588562 | 0.795041 | 0.908791 | 0.160924 |
| tossup_correctness | tier | winter | 2875 | 0.654104 | 0.514753 | 0.0255259 | 0.168097 | 0.769391 | 0.768348 | 0.00104348 | 0.128587 | 0.582896 | 0.789773 | 0.90192 | 0.164734 |
| tossup_correctness | category | Current Events | 129 | 0.630882 | 0.610904 | 0.0691786 | 0.211003 | 0.674419 | 0.666667 | 0.00775194 | 0.100406 | 0.580247 | 0.717952 | 0.817844 | 0.197572 |
| tossup_correctness | category | Fine Arts | 1074 | 0.61303 | 0.527541 | 0.0585005 | 0.172588 | 0.763501 | 0.776536 | -0.0130354 | 0.131557 | 0.590954 | 0.798788 | 0.911027 | 0.159463 |
| tossup_correctness | category | Geography | 180 | 0.708317 | 0.611357 | 0.0802482 | 0.21013 | 0.683333 | 0.616667 | 0.0666667 | 0.153172 | 0.470789 | 0.729521 | 0.862436 | 0.191058 |
| tossup_correctness | category | History | 1454 | 0.658542 | 0.526553 | 0.0376303 | 0.173688 | 0.755846 | 0.757909 | -0.00206327 | 0.135652 | 0.547803 | 0.75874 | 0.890075 | 0.177302 |
| tossup_correctness | category | Literature | 1435 | 0.628808 | 0.474803 | 0.034272 | 0.148272 | 0.814634 | 0.810453 | 0.00418118 | 0.115248 | 0.646384 | 0.831842 | 0.937188 | 0.141388 |
| tossup_correctness | category | Mythology | 324 | 0.639584 | 0.498116 | 0.050314 | 0.161408 | 0.777778 | 0.79321 | -0.0154321 | 0.129526 | 0.581171 | 0.770708 | 0.894167 | 0.172589 |
| tossup_correctness | category | Other Academic | 71 | 0.41939 | 0.606082 | 0.1241 | 0.206601 | 0.732394 | 0.760563 | -0.028169 | 0.0955853 | 0.563753 | 0.696255 | 0.821917 | 0.204616 |
| tossup_correctness | category | Philosophy | 310 | 0.677451 | 0.515188 | 0.0335233 | 0.17015 | 0.758065 | 0.76129 | -0.00322581 | 0.119528 | 0.598067 | 0.800421 | 0.904066 | 0.160038 |
| tossup_correctness | category | Popular Culture | 108 | 0.577257 | 0.434209 | 0.16194 | 0.132386 | 0.851852 | 0.888889 | -0.037037 | 0.114337 | 0.577331 | 0.736467 | 0.859115 | 0.185421 |
| tossup_correctness | category | Religion | 361 | 0.622452 | 0.559104 | 0.0468376 | 0.186306 | 0.745152 | 0.742382 | 0.00277008 | 0.142387 | 0.515205 | 0.762013 | 0.887715 | 0.176217 |
| tossup_correctness | category | Science | 1445 | 0.666698 | 0.532118 | 0.0265644 | 0.176091 | 0.748097 | 0.746021 | 0.00207612 | 0.126995 | 0.575094 | 0.781943 | 0.894132 | 0.16903 |
| tossup_correctness | category | Social Science | 327 | 0.695513 | 0.543192 | 0.0519825 | 0.180636 | 0.727829 | 0.718654 | 0.00917431 | 0.12158 | 0.561688 | 0.753507 | 0.861524 | 0.183352 |
| tossup_correctness | category | Unknown | 2039 | 0.607828 | 0.543434 | 0.0503153 | 0.17827 | 0.758215 | 0.762138 | -0.00392349 | 0.127072 | 0.588562 | 0.795041 | 0.908791 | 0.160924 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.608886 | 0.574724 | 0.0951091 | 0.192825 | 0.715847 | 0.743169 | -0.0273224 | 0.129606 | 0.509578 | 0.696192 | 0.821291 | 0.201349 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.625444 | 0.569699 | 0.0453452 | 0.191203 | 0.718325 | 0.728796 | -0.0104712 | 0.132113 | 0.510398 | 0.72957 | 0.8579 | 0.189574 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.654558 | 0.531196 | 0.0255068 | 0.175775 | 0.751675 | 0.752568 | -0.000893256 | 0.129421 | 0.556643 | 0.773137 | 0.88773 | 0.173158 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.646159 | 0.49682 | 0.0362039 | 0.160217 | 0.786435 | 0.786087 | 0.000347826 | 0.124751 | 0.595239 | 0.802046 | 0.909908 | 0.159146 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.63387 | 0.533409 | 0.0375402 | 0.173685 | 0.766057 | 0.764393 | 0.00166389 | 0.128137 | 0.597886 | 0.806301 | 0.921522 | 0.154648 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1197 | -2.34272 | 0.717566 | -4.95237 | -3.55547 | -2.81913 | -2.29879 | -1.82761 | -1.25469 | -0.304037 |
| player | theta_2 | 1197 | -1.42936 | 0.90503 | -4.40294 | -2.98507 | -2.17053 | -1.24768 | -0.64993 | -0.241093 | 0.813157 |
| player | theta_3 | 1197 | -1.16784 | 0.929577 | -4.21845 | -3.0793 | -1.56336 | -0.949181 | -0.466811 | -0.102268 | 0.717036 |
| player | theta_norm | 1197 | 3.24264 | 0.759778 | 1.54272 | 2.13542 | 2.68415 | 3.16262 | 3.75514 | 4.62709 | 5.68843 |
| tossup | start_difficulty_d1 | 1240 | -2.42591 | 1.15467 | -4.66204 | -3.88941 | -3.35916 | -2.79528 | -1.45465 | -0.405332 | 0.308067 |
| tossup | start_difficulty_d2 | 1240 | -1.13889 | 1.36195 | -4.85832 | -3.78866 | -2.07136 | -0.574809 | -0.0956114 | 0.287013 | 1.42626 |
| tossup | start_difficulty_d3 | 1240 | -1.38761 | 1.21574 | -4.06769 | -3.16959 | -2.58374 | -1.17528 | -0.259872 | 0.283287 | 1.63356 |
| tossup | end_difficulty_d1 | 1240 | -3.52356 | 1.27407 | -7.4248 | -5.41473 | -4.45857 | -3.78277 | -2.50516 | -1.35767 | -0.611135 |
| tossup | end_difficulty_d2 | 1240 | -2.18249 | 1.46211 | -8.59068 | -4.85514 | -3.30595 | -1.60253 | -1.05881 | -0.629806 | 0.558188 |
| tossup | end_difficulty_d3 | 1240 | -2.44575 | 1.33441 | -5.98827 | -4.56192 | -3.63021 | -2.24328 | -1.23848 | -0.631461 | 0.806121 |
| tossup | total_drop_d1 | 1240 | 1.09765 | 0.392999 | 0.385052 | 0.681576 | 0.888288 | 1.01704 | 1.19812 | 1.76104 | 4.12988 |
| tossup | total_drop_d2 | 1240 | 1.0436 | 0.281732 | 0.502881 | 0.763388 | 0.925356 | 0.991641 | 1.08989 | 1.45801 | 4.83108 |
| tossup | total_drop_d3 | 1240 | 1.05814 | 0.220018 | 0.618794 | 0.849507 | 0.937266 | 1.00388 | 1.111 | 1.45347 | 3.62052 |
| tossup | drop_share_1_d1 | 1240 | 0.356051 | 0.0477164 | 0.210619 | 0.300432 | 0.322256 | 0.344377 | 0.38255 | 0.444856 | 0.603035 |
| tossup | drop_share_2_d1 | 1240 | 0.33739 | 0.0195403 | 0.253235 | 0.306145 | 0.325441 | 0.337742 | 0.349797 | 0.366209 | 0.463509 |
| tossup | drop_share_3_d1 | 1240 | 0.306559 | 0.0436167 | 0.14373 | 0.228333 | 0.280836 | 0.31432 | 0.337342 | 0.363433 | 0.460324 |
| tossup | drop_share_1_d2 | 1240 | 0.32654 | 0.0352087 | 0.208573 | 0.292269 | 0.307545 | 0.317656 | 0.333801 | 0.397275 | 0.571605 |
| tossup | drop_share_2_d2 | 1240 | 0.343516 | 0.0154118 | 0.268627 | 0.311303 | 0.337402 | 0.345711 | 0.353117 | 0.363369 | 0.416862 |
| tossup | drop_share_3_d2 | 1240 | 0.329945 | 0.031208 | 0.158415 | 0.272333 | 0.319865 | 0.335797 | 0.346686 | 0.366024 | 0.446234 |
| tossup | drop_share_1_d3 | 1240 | 0.334448 | 0.0338191 | 0.251802 | 0.294344 | 0.310315 | 0.324818 | 0.351943 | 0.401958 | 0.472135 |
| tossup | drop_share_2_d3 | 1240 | 0.343405 | 0.0122099 | 0.299008 | 0.322833 | 0.336037 | 0.343708 | 0.350844 | 0.362742 | 0.419958 |
| tossup | drop_share_3_d3 | 1240 | 0.322147 | 0.0323613 | 0.196627 | 0.25557 | 0.305956 | 0.329105 | 0.344954 | 0.361696 | 0.39926 |
| tossup | r_1 | 1240 | 0.50943 | 0.314537 | 0.0411395 | 0.0710538 | 0.200839 | 0.606428 | 0.817575 | 0.897869 | 0.961384 |
| tossup | r_2 | 1240 | 0.213125 | 0.222044 | 0.0198698 | 0.0381561 | 0.0617855 | 0.104315 | 0.254015 | 0.685871 | 0.902831 |
| tossup | r_3 | 1240 | 0.277446 | 0.276364 | 0.0152574 | 0.0338233 | 0.0672797 | 0.127218 | 0.571762 | 0.792405 | 0.896735 |
| tossup | r_norm | 1240 | 0.7742 | 0.0834893 | 0.580005 | 0.632813 | 0.710229 | 0.777738 | 0.839501 | 0.900896 | 0.961782 |
