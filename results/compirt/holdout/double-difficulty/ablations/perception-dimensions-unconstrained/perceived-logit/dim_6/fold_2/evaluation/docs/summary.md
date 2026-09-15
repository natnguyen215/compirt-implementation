# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-logit/dim_6/fold_2/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-logit/dim_6/fold_2`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 6 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 335530 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.555778 |
| log_loss | 0.58019 |
| ece | 0.0869791 |
| brier | 0.186925 |
| accuracy | 0.76245 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.00172842 |
| probability_std | 0.116051 |
| probability_p10 | 0.638431 |
| probability_p50 | 0.854652 |
| probability_p90 | 0.934493 |
| mean_predictive_variance | 0.135235 |
| integrated_brier_score | 0.17324 |
| joint_tossup_event_log_loss | 7.69638 |
| buzz_position_mae | 0.3303 |
| buzz_position_median_absolute_error | 0.329493 |
| buzz_position_bias | -0.315723 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.335638 |
| first_buzzer_mean_reciprocal_rank | 0.550548 |
| first_buzzer_log_loss | 1.68844 |
| first_buzzer_events | 9257 |
| first_buzzer_team_top1_accuracy | 0.635951 |
| tossup_scorer_player_top1_accuracy | 0.267377 |
| tossup_scorer_team_top1_accuracy | 0.392537 |
| tossup_game_winner_accuracy | 0.673913 |
| tossup_game_margin_mae | 47.6668 |
| tournament_player_ppg_spearman | 0.572456 |
| tournament_player_ppg_mae | 10.5361 |
| tournament_player_ppg_top10_overlap | 0.568966 |
| neg_auroc | 0.555778 |
| neg_average_precision | 0.289112 |
| neg_precision | 0.435484 |
| neg_recall | 0.0247366 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.033202 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.219273 |
| no_buzz_calibration_error | 0.206159 |
| no_buzz_brier | 0.0635449 |
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
| tossup_correctness | aggregate | all | 9257 | 0.555778 | 0.58019 | 0.0869791 | 0.186925 | 0.76245 | 0.764178 | -0.00172842 | 0.116051 | 0.638431 | 0.854652 | 0.934493 | 0.135235 |
| tossup_correctness | tier | fall | 2798 | 0.546668 | 0.549366 | 0.0726992 | 0.174397 | 0.783417 | 0.785204 | -0.00178699 | 0.0872564 | 0.735701 | 0.869265 | 0.932091 | 0.12213 |
| tossup_correctness | tier | nationals | 1545 | 0.577718 | 0.606822 | 0.0746548 | 0.204582 | 0.714563 | 0.721036 | -0.00647249 | 0.136181 | 0.54242 | 0.731576 | 0.90622 | 0.17994 |
| tossup_correctness | tier | regionals | 2039 | 0.537184 | 0.586116 | 0.0931348 | 0.188793 | 0.760667 | 0.762138 | -0.00147131 | 0.122115 | 0.614493 | 0.825577 | 0.931368 | 0.147635 |
| tossup_correctness | tier | winter | 2875 | 0.55065 | 0.591674 | 0.104175 | 0.188303 | 0.769043 | 0.768348 | 0.000695652 | 0.0915879 | 0.713113 | 0.884397 | 0.942588 | 0.11517 |
| tossup_correctness | category | Current Events | 129 | 0.540562 | 0.719736 | 0.167941 | 0.245835 | 0.666667 | 0.666667 | 0 | 0.117518 | 0.631211 | 0.846863 | 0.903214 | 0.14686 |
| tossup_correctness | category | Fine Arts | 1074 | 0.56294 | 0.567407 | 0.0921135 | 0.181527 | 0.772812 | 0.776536 | -0.00372439 | 0.113496 | 0.661244 | 0.875861 | 0.938892 | 0.125447 |
| tossup_correctness | category | Geography | 180 | 0.606737 | 0.79859 | 0.220201 | 0.278736 | 0.6 | 0.616667 | -0.0166667 | 0.109745 | 0.650612 | 0.854485 | 0.925097 | 0.136361 |
| tossup_correctness | category | History | 1454 | 0.54878 | 0.589582 | 0.0953668 | 0.191573 | 0.757221 | 0.757909 | -0.000687758 | 0.109578 | 0.649731 | 0.85492 | 0.928191 | 0.135285 |
| tossup_correctness | category | Literature | 1435 | 0.539433 | 0.514218 | 0.0745934 | 0.157757 | 0.81115 | 0.810453 | 0.000696864 | 0.106708 | 0.684091 | 0.87972 | 0.944715 | 0.121316 |
| tossup_correctness | category | Mythology | 324 | 0.554562 | 0.54007 | 0.0904623 | 0.170795 | 0.796296 | 0.79321 | 0.00308642 | 0.112303 | 0.65378 | 0.882039 | 0.936436 | 0.121456 |
| tossup_correctness | category | Other Academic | 71 | 0.297386 | 0.733841 | 0.238509 | 0.237798 | 0.704225 | 0.760563 | -0.056338 | 0.138849 | 0.583674 | 0.846904 | 0.928447 | 0.144571 |
| tossup_correctness | category | Philosophy | 310 | 0.530463 | 0.61607 | 0.117509 | 0.196301 | 0.758065 | 0.76129 | -0.00322581 | 0.112203 | 0.651913 | 0.880451 | 0.945245 | 0.122049 |
| tossup_correctness | category | Popular Culture | 108 | 0.595486 | 0.357455 | 0.0724391 | 0.102891 | 0.87963 | 0.888889 | -0.00925926 | 0.0898783 | 0.734054 | 0.862011 | 0.919626 | 0.127729 |
| tossup_correctness | category | Religion | 361 | 0.570896 | 0.61651 | 0.114646 | 0.201321 | 0.745152 | 0.742382 | 0.00277008 | 0.113423 | 0.651745 | 0.86889 | 0.932816 | 0.127867 |
| tossup_correctness | category | Science | 1445 | 0.584777 | 0.586049 | 0.0782079 | 0.19243 | 0.743253 | 0.746021 | -0.00276817 | 0.119974 | 0.609792 | 0.830779 | 0.925976 | 0.145938 |
| tossup_correctness | category | Social Science | 327 | 0.5895 | 0.637659 | 0.125618 | 0.210135 | 0.724771 | 0.718654 | 0.00611621 | 0.108357 | 0.651712 | 0.858578 | 0.929188 | 0.133151 |
| tossup_correctness | category | Unknown | 2039 | 0.537184 | 0.586116 | 0.0931348 | 0.188793 | 0.760667 | 0.762138 | -0.00147131 | 0.122115 | 0.614493 | 0.825577 | 0.931368 | 0.147635 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.483573 | 0.627478 | 0.105745 | 0.207208 | 0.721311 | 0.743169 | -0.0218579 | 0.116124 | 0.61809 | 0.822244 | 0.907156 | 0.15218 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.53116 | 0.62436 | 0.0924153 | 0.208643 | 0.722513 | 0.728796 | -0.00628272 | 0.111583 | 0.630596 | 0.823866 | 0.90893 | 0.149643 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.545873 | 0.591141 | 0.0826291 | 0.192866 | 0.750335 | 0.752568 | -0.00223314 | 0.108875 | 0.646211 | 0.843644 | 0.921705 | 0.141478 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.558691 | 0.543812 | 0.0830913 | 0.172642 | 0.787478 | 0.786087 | 0.0013913 | 0.115557 | 0.642012 | 0.864203 | 0.932481 | 0.132767 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.565096 | 0.589917 | 0.0933565 | 0.188025 | 0.762729 | 0.764393 | -0.00166389 | 0.12142 | 0.633464 | 0.877514 | 0.945239 | 0.127333 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | alpha | 1197 | -1.0611 | 1.0059 | -3.49963 | -2.40298 | -1.69321 | -1.2286 | -0.688785 | 1.1762 | 2.20665 |
| player | beta | 1197 | -4.08848 | 1.28719 | -7.24234 | -6.64148 | -4.83801 | -3.81335 | -3.06201 | -2.41729 | -2.05135 |
| player | theta_1 | 1197 | 0.630776 | 0.749016 | -2.12947 | -0.841311 | 0.21006 | 0.816561 | 1.15909 | 1.57422 | 2.44692 |
| player | theta_2 | 1197 | 0.701253 | 1.02533 | -2.61555 | -1.141 | -0.0222613 | 0.87398 | 1.50051 | 2.08111 | 3.28451 |
| player | theta_3 | 1197 | 0.66216 | 0.836245 | -2.06654 | -0.875607 | 0.191061 | 0.800354 | 1.22601 | 1.89913 | 2.67447 |
| player | theta_4 | 1197 | 0.643342 | 0.77463 | -1.82115 | -0.875783 | 0.205629 | 0.800303 | 1.21211 | 1.6967 | 2.32672 |
| player | theta_5 | 1197 | 0.575571 | 0.631845 | -1.85489 | -0.737002 | 0.297715 | 0.69247 | 0.956242 | 1.39963 | 2.75884 |
| player | theta_6 | 1197 | 0.584874 | 0.634351 | -1.82602 | -0.733483 | 0.302217 | 0.702736 | 0.964016 | 1.41296 | 2.53986 |
| player | theta_norm | 1197 | 2.34947 | 0.778478 | 0.178417 | 0.944626 | 1.90608 | 2.41775 | 2.83733 | 3.55498 | 5.33231 |
| tossup | start_difficulty_d1 | 1240 | -0.693894 | 0.383873 | -2.04057 | -1.40693 | -0.926605 | -0.673319 | -0.417199 | -0.105821 | 0.266666 |
| tossup | start_difficulty_d2 | 1240 | -0.733523 | 0.420031 | -2.0388 | -1.52674 | -0.989628 | -0.687566 | -0.400037 | -0.162296 | 0.19507 |
| tossup | start_difficulty_d3 | 1240 | -0.706274 | 0.443579 | -2.29333 | -1.59386 | -0.972359 | -0.625358 | -0.381806 | -0.0913942 | 0.315739 |
| tossup | start_difficulty_d4 | 1240 | -0.691299 | 0.416793 | -2.13793 | -1.42554 | -0.955706 | -0.652091 | -0.373516 | -0.0935598 | 0.258361 |
| tossup | start_difficulty_d5 | 1240 | -0.648586 | 0.353261 | -1.66199 | -1.2372 | -0.910136 | -0.650646 | -0.378351 | -0.0756915 | 0.427235 |
| tossup | start_difficulty_d6 | 1240 | -0.656018 | 0.368273 | -1.70409 | -1.27268 | -0.907975 | -0.641837 | -0.37281 | -0.0778617 | 0.328057 |
| tossup | end_difficulty_d1 | 1240 | -1.58723 | 0.343508 | -2.70619 | -2.1845 | -1.80637 | -1.55912 | -1.36609 | -1.03134 | -0.425498 |
| tossup | end_difficulty_d2 | 1240 | -1.59742 | 0.336949 | -2.578 | -2.19423 | -1.81985 | -1.57832 | -1.37336 | -1.06758 | -0.600671 |
| tossup | end_difficulty_d3 | 1240 | -1.59756 | 0.389864 | -2.90478 | -2.31365 | -1.83406 | -1.54639 | -1.32693 | -1.02073 | -0.432222 |
| tossup | end_difficulty_d4 | 1240 | -1.58976 | 0.372933 | -2.85278 | -2.24271 | -1.82877 | -1.57329 | -1.32902 | -0.994799 | -0.547192 |
| tossup | end_difficulty_d5 | 1240 | -1.56006 | 0.335504 | -2.47243 | -2.11453 | -1.7921 | -1.55042 | -1.32918 | -1.01556 | -0.301539 |
| tossup | end_difficulty_d6 | 1240 | -1.56609 | 0.350103 | -2.60901 | -2.17073 | -1.80041 | -1.54225 | -1.33383 | -1.00575 | -0.434495 |
| tossup | total_drop_d1 | 1240 | 0.893338 | 0.185703 | 0.319379 | 0.591898 | 0.771226 | 0.880482 | 1.02714 | 1.18644 | 1.53746 |
| tossup | total_drop_d2 | 1240 | 0.8639 | 0.21579 | 0.313007 | 0.440857 | 0.738747 | 0.876974 | 1.03205 | 1.16773 | 1.42115 |
| tossup | total_drop_d3 | 1240 | 0.891288 | 0.199388 | 0.321261 | 0.53946 | 0.771923 | 0.888232 | 1.02816 | 1.2072 | 1.56247 |
| tossup | total_drop_d4 | 1240 | 0.898456 | 0.187987 | 0.367587 | 0.591307 | 0.77392 | 0.891375 | 1.02685 | 1.21104 | 1.50186 |
| tossup | total_drop_d5 | 1240 | 0.911476 | 0.163632 | 0.471118 | 0.675045 | 0.790528 | 0.885889 | 1.02402 | 1.20498 | 1.42671 |
| tossup | total_drop_d6 | 1240 | 0.910074 | 0.163438 | 0.526389 | 0.676813 | 0.784755 | 0.889073 | 1.02245 | 1.19579 | 1.47801 |
| tossup | drop_share_1_d1 | 1240 | 0.312001 | 0.017449 | 0.241176 | 0.285476 | 0.3008 | 0.311188 | 0.322853 | 0.340351 | 0.399674 |
| tossup | drop_share_2_d1 | 1240 | 0.336782 | 0.0141708 | 0.277668 | 0.312709 | 0.328271 | 0.337813 | 0.34575 | 0.358942 | 0.381904 |
| tossup | drop_share_3_d1 | 1240 | 0.351217 | 0.0184654 | 0.299992 | 0.323901 | 0.339175 | 0.349827 | 0.361229 | 0.382988 | 0.449643 |
| tossup | drop_share_1_d2 | 1240 | 0.313279 | 0.0193558 | 0.245532 | 0.284185 | 0.301049 | 0.312207 | 0.323732 | 0.346262 | 0.407415 |
| tossup | drop_share_2_d2 | 1240 | 0.33483 | 0.0169723 | 0.264558 | 0.300883 | 0.325818 | 0.337287 | 0.34649 | 0.358122 | 0.376807 |
| tossup | drop_share_3_d2 | 1240 | 0.35189 | 0.0225328 | 0.281808 | 0.321747 | 0.337737 | 0.349092 | 0.361719 | 0.395036 | 0.463242 |
| tossup | drop_share_1_d3 | 1240 | 0.312892 | 0.0205934 | 0.237858 | 0.28441 | 0.300426 | 0.311387 | 0.322732 | 0.350758 | 0.413589 |
| tossup | drop_share_2_d3 | 1240 | 0.336725 | 0.0147502 | 0.271187 | 0.311831 | 0.327686 | 0.337432 | 0.346856 | 0.358817 | 0.379627 |
| tossup | drop_share_3_d3 | 1240 | 0.350383 | 0.0199556 | 0.2712 | 0.32022 | 0.339096 | 0.350103 | 0.360208 | 0.381995 | 0.462371 |
| tossup | drop_share_1_d4 | 1240 | 0.31225 | 0.0185159 | 0.227604 | 0.284472 | 0.300482 | 0.311687 | 0.322671 | 0.342416 | 0.388337 |
| tossup | drop_share_2_d4 | 1240 | 0.336708 | 0.0142524 | 0.275019 | 0.312111 | 0.32816 | 0.33787 | 0.346366 | 0.357824 | 0.378819 |
| tossup | drop_share_3_d4 | 1240 | 0.351041 | 0.0194357 | 0.286242 | 0.32434 | 0.338699 | 0.34907 | 0.360224 | 0.383217 | 0.465149 |
| tossup | drop_share_1_d5 | 1240 | 0.311483 | 0.016503 | 0.244868 | 0.285718 | 0.300486 | 0.31105 | 0.32197 | 0.338282 | 0.371043 |
| tossup | drop_share_2_d5 | 1240 | 0.337936 | 0.0129253 | 0.292688 | 0.316234 | 0.329416 | 0.338271 | 0.346547 | 0.358919 | 0.376482 |
| tossup | drop_share_3_d5 | 1240 | 0.350582 | 0.0167511 | 0.297486 | 0.324327 | 0.339086 | 0.350284 | 0.361271 | 0.377667 | 0.41212 |
| tossup | drop_share_1_d6 | 1240 | 0.312184 | 0.0171124 | 0.252698 | 0.286453 | 0.300772 | 0.311363 | 0.323039 | 0.340772 | 0.38104 |
| tossup | drop_share_2_d6 | 1240 | 0.337965 | 0.0128595 | 0.291725 | 0.316719 | 0.329403 | 0.338159 | 0.34676 | 0.358773 | 0.384597 |
| tossup | drop_share_3_d6 | 1240 | 0.34985 | 0.0169291 | 0.2943 | 0.322129 | 0.339046 | 0.34965 | 0.36047 | 0.378697 | 0.410072 |
| tossup | r_1 | 1240 | 0.14958 | 0.0765828 | 0.042545 | 0.0636705 | 0.115089 | 0.143267 | 0.157692 | 0.292854 | 0.686965 |
| tossup | r_2 | 1240 | 0.197927 | 0.162907 | 0.0301879 | 0.0660272 | 0.0993882 | 0.129195 | 0.222384 | 0.616958 | 0.769773 |
| tossup | r_3 | 1240 | 0.169444 | 0.103386 | 0.0348071 | 0.0578694 | 0.115711 | 0.15593 | 0.178453 | 0.398569 | 0.711164 |
| tossup | r_4 | 1240 | 0.167464 | 0.0891702 | 0.0397021 | 0.0639648 | 0.119015 | 0.161029 | 0.185347 | 0.332299 | 0.749463 |
| tossup | r_5 | 1240 | 0.157106 | 0.0471637 | 0.0481751 | 0.0731715 | 0.120767 | 0.168662 | 0.192567 | 0.219516 | 0.365462 |
| tossup | r_6 | 1240 | 0.158479 | 0.0458234 | 0.0478504 | 0.0727606 | 0.122193 | 0.172632 | 0.194487 | 0.212525 | 0.323491 |
| tossup | r_norm | 1240 | 0.465632 | 0.0813537 | 0.408575 | 0.410058 | 0.414613 | 0.423526 | 0.484735 | 0.660544 | 0.776711 |
