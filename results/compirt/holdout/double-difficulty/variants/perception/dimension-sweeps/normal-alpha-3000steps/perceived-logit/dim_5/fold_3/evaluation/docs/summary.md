# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-3000steps/perceived-logit/dim_5/fold_3/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-3000steps/perceived-logit/dim_5/fold_3`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 336994 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.545439 |
| log_loss | 0.583902 |
| ece | 0.0886575 |
| brier | 0.185395 |
| accuracy | 0.769824 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | -0.000220264 |
| probability_std | 0.111331 |
| probability_p10 | 0.66526 |
| probability_p50 | 0.871392 |
| probability_p90 | 0.941716 |
| mean_predictive_variance | 0.125296 |
| integrated_brier_score | 0.175292 |
| joint_tossup_event_log_loss | 7.71366 |
| buzz_position_mae | 0.33756 |
| buzz_position_median_absolute_error | 0.337853 |
| buzz_position_bias | -0.323793 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |
| first_buzzer_top1_accuracy | 0.353304 |
| first_buzzer_mean_reciprocal_rank | 0.564725 |
| first_buzzer_log_loss | 1.67987 |
| first_buzzer_events | 9080 |
| first_buzzer_team_top1_accuracy | 0.634471 |
| tossup_scorer_player_top1_accuracy | 0.261388 |
| tossup_scorer_team_top1_accuracy | 0.41551 |
| tossup_game_winner_accuracy | 0.719027 |
| tossup_game_margin_mae | 46.7183 |
| tournament_player_ppg_spearman | 0.594757 |
| tournament_player_ppg_mae | 10.6414 |
| tournament_player_ppg_top10_overlap | 0.586207 |
| neg_auroc | 0.545439 |
| neg_average_precision | 0.279314 |
| neg_precision | 0.491228 |
| neg_recall | 0.0268199 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.0307124 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.223176 |
| no_buzz_calibration_error | 0.207992 |
| no_buzz_brier | 0.0664536 |
| full_pmf_max_mass_error | 1.11022e-15 |
| tossup_outcome_events | 9220 |
| first_buzzer_team_top1_accuracy_events | 9080 |
| tossup_scorer_player_top1_accuracy_events | 9220 |
| tossup_scorer_team_top1_accuracy_events | 9220 |
| tossup_game_winner_accuracy_games | 452 |
| tossup_game_margin_mae_games | 461 |
| tournament_player_ppg_tournaments | 29 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.545439 | 0.583902 | 0.0886575 | 0.185395 | 0.769824 | 0.770044 | -0.000220264 | 0.111331 | 0.66526 | 0.871392 | 0.941716 | 0.125296 |
| tossup_correctness | tier | fall | 2817 | 0.534956 | 0.56431 | 0.0834253 | 0.179202 | 0.779908 | 0.781683 | -0.00177494 | 0.0938374 | 0.715352 | 0.871991 | 0.933248 | 0.122688 |
| tossup_correctness | tier | nationals | 1542 | 0.60217 | 0.584068 | 0.0551076 | 0.193934 | 0.734112 | 0.73476 | -0.000648508 | 0.138233 | 0.563422 | 0.773891 | 0.921322 | 0.167658 |
| tossup_correctness | tier | regionals | 1934 | 0.526177 | 0.615035 | 0.104212 | 0.195791 | 0.758014 | 0.75698 | 0.00103413 | 0.113214 | 0.652069 | 0.86072 | 0.944617 | 0.129719 |
| tossup_correctness | tier | winter | 2787 | 0.51549 | 0.582009 | 0.103005 | 0.179716 | 0.787585 | 0.786868 | 0.000717618 | 0.0790238 | 0.767346 | 0.900303 | 0.949787 | 0.101424 |
| tossup_correctness | category | Current Events | 125 | 0.587224 | 0.652369 | 0.144234 | 0.22154 | 0.68 | 0.704 | -0.024 | 0.122637 | 0.624739 | 0.840525 | 0.909147 | 0.145209 |
| tossup_correctness | category | Fine Arts | 1072 | 0.539388 | 0.597839 | 0.105941 | 0.189136 | 0.771455 | 0.770522 | 0.000932836 | 0.106089 | 0.677672 | 0.889934 | 0.944722 | 0.116342 |
| tossup_correctness | category | Geography | 185 | 0.611049 | 0.652731 | 0.130452 | 0.217086 | 0.708108 | 0.702703 | 0.00540541 | 0.115303 | 0.677977 | 0.865593 | 0.930829 | 0.127654 |
| tossup_correctness | category | History | 1443 | 0.559475 | 0.575882 | 0.0717336 | 0.18478 | 0.767152 | 0.765073 | 0.002079 | 0.109248 | 0.655348 | 0.859509 | 0.931805 | 0.131791 |
| tossup_correctness | category | Literature | 1411 | 0.523458 | 0.52433 | 0.0758969 | 0.159516 | 0.810064 | 0.81219 | -0.00212615 | 0.105697 | 0.699241 | 0.892761 | 0.950429 | 0.112667 |
| tossup_correctness | category | Mythology | 320 | 0.542293 | 0.550433 | 0.087719 | 0.172355 | 0.7875 | 0.79375 | -0.00625 | 0.107409 | 0.706964 | 0.890542 | 0.939337 | 0.115542 |
| tossup_correctness | category | Other Academic | 64 | 0.638021 | 0.570313 | 0.108968 | 0.189351 | 0.71875 | 0.75 | -0.03125 | 0.153521 | 0.571616 | 0.855702 | 0.940994 | 0.142578 |
| tossup_correctness | category | Philosophy | 312 | 0.46071 | 0.57387 | 0.113269 | 0.174762 | 0.801282 | 0.801282 | 0 | 0.106612 | 0.687417 | 0.890147 | 0.948897 | 0.115709 |
| tossup_correctness | category | Popular Culture | 104 | 0.489347 | 0.470505 | 0.0674029 | 0.139425 | 0.846154 | 0.846154 | 0 | 0.0798479 | 0.730177 | 0.880617 | 0.92924 | 0.117611 |
| tossup_correctness | category | Religion | 358 | 0.569898 | 0.660649 | 0.137135 | 0.213408 | 0.726257 | 0.726257 | 0 | 0.11503 | 0.673859 | 0.889698 | 0.943713 | 0.116959 |
| tossup_correctness | category | Science | 1431 | 0.5733 | 0.565283 | 0.0739169 | 0.182364 | 0.769392 | 0.765199 | 0.00419287 | 0.112407 | 0.656409 | 0.849048 | 0.930494 | 0.136517 |
| tossup_correctness | category | Social Science | 321 | 0.494438 | 0.661342 | 0.13213 | 0.214153 | 0.728972 | 0.744548 | -0.0155763 | 0.113531 | 0.672938 | 0.878991 | 0.938278 | 0.123114 |
| tossup_correctness | category | Unknown | 1934 | 0.526177 | 0.615035 | 0.104212 | 0.195791 | 0.758014 | 0.75698 | 0.00103413 | 0.113214 | 0.652069 | 0.86072 | 0.944617 | 0.129719 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.485203 | 0.69037 | 0.153216 | 0.231338 | 0.703125 | 0.697917 | 0.00520833 | 0.103524 | 0.649141 | 0.822719 | 0.91423 | 0.150089 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.533257 | 0.626966 | 0.0961672 | 0.206539 | 0.733408 | 0.733408 | 0 | 0.116198 | 0.635589 | 0.838649 | 0.919792 | 0.144356 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.510159 | 0.608808 | 0.0939106 | 0.195975 | 0.753394 | 0.759276 | -0.00588235 | 0.10693 | 0.674129 | 0.858691 | 0.929452 | 0.132585 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.554039 | 0.543503 | 0.0740138 | 0.171158 | 0.790519 | 0.789125 | 0.00139421 | 0.106571 | 0.676902 | 0.871923 | 0.938314 | 0.124377 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.557682 | 0.584635 | 0.0989513 | 0.181917 | 0.777397 | 0.775342 | 0.00205479 | 0.114788 | 0.66229 | 0.897416 | 0.952423 | 0.113249 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | alpha | 1133 | -1.18057 | 0.923774 | -3.36587 | -2.37711 | -1.74586 | -1.32 | -0.827262 | 0.912577 | 2.24544 |
| player | beta | 1133 | -3.82259 | 1.26001 | -7.16805 | -6.50946 | -4.43522 | -3.54725 | -2.83749 | -2.28666 | -1.82488 |
| player | theta_1 | 1133 | 0.780211 | 0.998331 | -2.40349 | -1.05103 | 0.136106 | 0.96939 | 1.51077 | 2.15139 | 3.23097 |
| player | theta_2 | 1133 | 0.756209 | 0.983194 | -2.33868 | -1.01547 | 0.131433 | 0.892179 | 1.43422 | 2.18413 | 3.92966 |
| player | theta_3 | 1133 | 0.721754 | 0.789497 | -2.00992 | -0.780425 | 0.245369 | 0.863703 | 1.29205 | 1.80685 | 2.4607 |
| player | theta_4 | 1133 | 0.632546 | 0.650297 | -1.51526 | -0.663035 | 0.297818 | 0.74464 | 1.07126 | 1.50365 | 3.17864 |
| player | theta_5 | 1133 | 0.678745 | 0.790242 | -2.02304 | -0.827694 | 0.234319 | 0.783676 | 1.21108 | 1.86829 | 2.70776 |
| player | theta_norm | 1133 | 2.38042 | 0.72608 | 0.264777 | 1.11038 | 1.94198 | 2.42401 | 2.8337 | 3.56709 | 5.29233 |
| tossup | start_difficulty_d1 | 1240 | -0.812501 | 0.404217 | -2.04864 | -1.59988 | -1.09044 | -0.748019 | -0.501809 | -0.251988 | -0.0354782 |
| tossup | start_difficulty_d2 | 1240 | -0.814378 | 0.45064 | -2.43127 | -1.62994 | -1.13346 | -0.746705 | -0.472606 | -0.157992 | 0.151272 |
| tossup | start_difficulty_d3 | 1240 | -0.759967 | 0.414972 | -2.26929 | -1.58343 | -0.995566 | -0.668913 | -0.464998 | -0.214881 | 0.116982 |
| tossup | start_difficulty_d4 | 1240 | -0.690772 | 0.307917 | -1.78826 | -1.22389 | -0.885841 | -0.665172 | -0.465843 | -0.215441 | 0.137035 |
| tossup | start_difficulty_d5 | 1240 | -0.724903 | 0.394509 | -2.11069 | -1.47132 | -0.969592 | -0.634387 | -0.441876 | -0.198369 | 0.172439 |
| tossup | end_difficulty_d1 | 1240 | -1.6228 | 0.330446 | -2.65183 | -2.19744 | -1.84258 | -1.60646 | -1.38002 | -1.12922 | -0.667046 |
| tossup | end_difficulty_d2 | 1240 | -1.63907 | 0.404942 | -3.03716 | -2.34029 | -1.92256 | -1.60196 | -1.3464 | -1.03494 | -0.59417 |
| tossup | end_difficulty_d3 | 1240 | -1.5973 | 0.362828 | -2.81397 | -2.27701 | -1.81681 | -1.56016 | -1.33582 | -1.06481 | -0.614294 |
| tossup | end_difficulty_d4 | 1240 | -1.55632 | 0.309199 | -2.63015 | -2.13023 | -1.74928 | -1.53087 | -1.34235 | -1.08822 | -0.566659 |
| tossup | end_difficulty_d5 | 1240 | -1.57637 | 0.360059 | -2.6464 | -2.24866 | -1.79261 | -1.53722 | -1.31576 | -1.05813 | -0.534687 |
| tossup | total_drop_d1 | 1240 | 0.810296 | 0.215398 | 0.27204 | 0.394708 | 0.682992 | 0.827607 | 0.969641 | 1.13312 | 1.34773 |
| tossup | total_drop_d2 | 1240 | 0.82469 | 0.20001 | 0.272215 | 0.44021 | 0.705919 | 0.832645 | 0.953042 | 1.14876 | 1.53886 |
| tossup | total_drop_d3 | 1240 | 0.837333 | 0.190817 | 0.3012 | 0.488876 | 0.729582 | 0.8515 | 0.963215 | 1.13337 | 1.36438 |
| tossup | total_drop_d4 | 1240 | 0.865546 | 0.156418 | 0.296931 | 0.635242 | 0.761025 | 0.848652 | 0.962834 | 1.14365 | 1.56953 |
| tossup | total_drop_d5 | 1240 | 0.851463 | 0.179545 | 0.292089 | 0.505015 | 0.758357 | 0.853646 | 0.963612 | 1.13503 | 1.45509 |
| tossup | drop_share_1_d1 | 1240 | 0.315424 | 0.0204329 | 0.236005 | 0.285578 | 0.303478 | 0.313866 | 0.326658 | 0.349287 | 0.411849 |
| tossup | drop_share_2_d1 | 1240 | 0.331508 | 0.0177157 | 0.260144 | 0.296086 | 0.321846 | 0.334308 | 0.343534 | 0.355627 | 0.375678 |
| tossup | drop_share_3_d1 | 1240 | 0.353068 | 0.024731 | 0.283258 | 0.319556 | 0.338147 | 0.349856 | 0.363515 | 0.400482 | 0.465185 |
| tossup | drop_share_1_d2 | 1240 | 0.314222 | 0.0203947 | 0.227039 | 0.283611 | 0.302043 | 0.313483 | 0.325577 | 0.347393 | 0.407128 |
| tossup | drop_share_2_d2 | 1240 | 0.332623 | 0.0158557 | 0.267931 | 0.302699 | 0.324262 | 0.334729 | 0.343369 | 0.355119 | 0.371633 |
| tossup | drop_share_3_d2 | 1240 | 0.353156 | 0.0229147 | 0.285228 | 0.321135 | 0.338951 | 0.351117 | 0.364233 | 0.396772 | 0.494102 |
| tossup | drop_share_1_d3 | 1240 | 0.315722 | 0.019895 | 0.22244 | 0.287499 | 0.303716 | 0.314982 | 0.325946 | 0.349962 | 0.409834 |
| tossup | drop_share_2_d3 | 1240 | 0.333488 | 0.0156003 | 0.264188 | 0.304418 | 0.324965 | 0.335585 | 0.343875 | 0.355173 | 0.376673 |
| tossup | drop_share_3_d3 | 1240 | 0.35079 | 0.0228769 | 0.291839 | 0.319223 | 0.336585 | 0.3484 | 0.360699 | 0.390662 | 0.471329 |
| tossup | drop_share_1_d4 | 1240 | 0.31355 | 0.0159456 | 0.247516 | 0.288341 | 0.303295 | 0.313066 | 0.324469 | 0.339739 | 0.392988 |
| tossup | drop_share_2_d4 | 1240 | 0.335693 | 0.0132087 | 0.278669 | 0.312883 | 0.327896 | 0.336306 | 0.344199 | 0.35647 | 0.37807 |
| tossup | drop_share_3_d4 | 1240 | 0.350758 | 0.0184004 | 0.274029 | 0.323108 | 0.338438 | 0.349536 | 0.361353 | 0.382705 | 0.432244 |
| tossup | drop_share_1_d5 | 1240 | 0.315636 | 0.0195321 | 0.225513 | 0.288623 | 0.303451 | 0.313936 | 0.325643 | 0.349758 | 0.424966 |
| tossup | drop_share_2_d5 | 1240 | 0.334444 | 0.0142374 | 0.27733 | 0.310169 | 0.326449 | 0.335594 | 0.34355 | 0.355327 | 0.378897 |
| tossup | drop_share_3_d5 | 1240 | 0.349919 | 0.019689 | 0.257585 | 0.319342 | 0.338293 | 0.349636 | 0.360342 | 0.380592 | 0.472397 |
| tossup | r_1 | 1240 | 0.224259 | 0.181642 | 0.0364694 | 0.0675567 | 0.108556 | 0.150318 | 0.26618 | 0.67601 | 0.828225 |
| tossup | r_2 | 1240 | 0.226466 | 0.156619 | 0.0304877 | 0.0585146 | 0.110079 | 0.180488 | 0.293252 | 0.573968 | 0.778616 |
| tossup | r_3 | 1240 | 0.189921 | 0.115644 | 0.0315632 | 0.0598388 | 0.121848 | 0.169185 | 0.209719 | 0.44671 | 0.754316 |
| tossup | r_4 | 1240 | 0.167181 | 0.0716908 | 0.0431579 | 0.065412 | 0.107709 | 0.173844 | 0.215193 | 0.257946 | 0.619706 |
| tossup | r_5 | 1240 | 0.192174 | 0.112289 | 0.0350961 | 0.0591513 | 0.114123 | 0.182606 | 0.232416 | 0.410303 | 0.73046 |
| tossup | r_norm | 1240 | 0.532132 | 0.0891332 | 0.447892 | 0.451211 | 0.461385 | 0.496284 | 0.579726 | 0.728006 | 0.832784 |
