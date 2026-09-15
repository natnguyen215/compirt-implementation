# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-difficulty-three-slice/dim_6/fold_4/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-difficulty-three-slice/dim_6/fold_4`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 6 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 327886 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.657833 |
| log_loss | 0.506599 |
| ece | 0.0185872 |
| brier | 0.164315 |
| accuracy | 0.77918 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | 0.00582524 |
| probability_std | 0.11947 |
| probability_p10 | 0.604476 |
| probability_p50 | 0.793268 |
| probability_p90 | 0.9043 |
| mean_predictive_variance | 0.162154 |
| integrated_brier_score | 0.10022 |
| joint_tossup_event_log_loss | 6.88809 |
| buzz_position_mae | 0.158636 |
| buzz_position_median_absolute_error | 0.144711 |
| buzz_position_bias | -0.063634 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.362567 |
| first_buzzer_mean_reciprocal_rank | 0.5684 |
| first_buzzer_log_loss | 1.67237 |
| first_buzzer_events | 9270 |
| first_buzzer_team_top1_accuracy | 0.643366 |
| tossup_scorer_player_top1_accuracy | 0.321109 |
| tossup_scorer_team_top1_accuracy | 0.494989 |
| tossup_game_winner_accuracy | 0.800875 |
| tossup_game_margin_mae | 33.2407 |
| tournament_player_ppg_spearman | 0.698657 |
| tournament_player_ppg_mae | 8.98954 |
| tournament_player_ppg_top10_overlap | 0.696552 |
| neg_auroc | 0.657833 |
| neg_average_precision | 0.381059 |
| neg_precision | 0.6 |
| neg_recall | 0.0771061 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0555623 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0925704 |
| no_buzz_calibration_error | 0.0808434 |
| no_buzz_brier | 0.025221 |
| full_pmf_max_mass_error | 1.22125e-15 |
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
| tossup_correctness | aggregate | all | 9270 | 0.657833 | 0.506599 | 0.0185872 | 0.164315 | 0.77918 | 0.773355 | 0.00582524 | 0.11947 | 0.604476 | 0.793268 | 0.9043 | 0.162154 |
| tossup_correctness | tier | fall | 2876 | 0.637432 | 0.491877 | 0.0262552 | 0.157371 | 0.794159 | 0.793115 | 0.00104312 | 0.0965715 | 0.683304 | 0.836325 | 0.916052 | 0.141348 |
| tossup_correctness | tier | nationals | 1579 | 0.662353 | 0.55728 | 0.0610856 | 0.186322 | 0.741609 | 0.729576 | 0.0120329 | 0.120185 | 0.515493 | 0.678899 | 0.822492 | 0.206339 |
| tossup_correctness | tier | regionals | 1990 | 0.680832 | 0.5058 | 0.0158145 | 0.164789 | 0.775879 | 0.765829 | 0.0100503 | 0.104381 | 0.616757 | 0.775871 | 0.872193 | 0.172673 |
| tossup_correctness | tier | winter | 2825 | 0.665044 | 0.49382 | 0.0135351 | 0.15875 | 0.787257 | 0.783009 | 0.00424779 | 0.115934 | 0.629158 | 0.814531 | 0.919028 | 0.151229 |
| tossup_correctness | category | Current Events | 123 | 0.681218 | 0.513753 | 0.0465511 | 0.167395 | 0.772358 | 0.764228 | 0.00813008 | 0.115992 | 0.562111 | 0.744769 | 0.845051 | 0.187957 |
| tossup_correctness | category | Fine Arts | 1093 | 0.64674 | 0.515689 | 0.0278241 | 0.168129 | 0.775846 | 0.769442 | 0.00640439 | 0.113477 | 0.625894 | 0.811955 | 0.907922 | 0.154229 |
| tossup_correctness | category | Geography | 191 | 0.75963 | 0.52966 | 0.0576821 | 0.176342 | 0.727749 | 0.691099 | 0.0366492 | 0.1481 | 0.496513 | 0.747747 | 0.879248 | 0.182805 |
| tossup_correctness | category | History | 1469 | 0.680846 | 0.514744 | 0.0220297 | 0.168909 | 0.763785 | 0.758339 | 0.00544588 | 0.119262 | 0.576164 | 0.765688 | 0.890613 | 0.173557 |
| tossup_correctness | category | Literature | 1436 | 0.593835 | 0.483817 | 0.0607267 | 0.151259 | 0.81337 | 0.81546 | -0.00208914 | 0.107408 | 0.666503 | 0.858549 | 0.939186 | 0.130561 |
| tossup_correctness | category | Mythology | 325 | 0.63518 | 0.444186 | 0.0912343 | 0.137739 | 0.833846 | 0.843077 | -0.00923077 | 0.110665 | 0.603865 | 0.776124 | 0.887601 | 0.171449 |
| tossup_correctness | category | Other Academic | 67 | 0.607817 | 0.53452 | 0.108286 | 0.17551 | 0.776119 | 0.791045 | -0.0149254 | 0.114894 | 0.536942 | 0.688946 | 0.819045 | 0.203399 |
| tossup_correctness | category | Philosophy | 322 | 0.622444 | 0.505785 | 0.0228842 | 0.16381 | 0.782609 | 0.785714 | -0.00310559 | 0.111354 | 0.630946 | 0.818827 | 0.915164 | 0.154522 |
| tossup_correctness | category | Popular Culture | 100 | 0.537283 | 0.407521 | 0.120284 | 0.121799 | 0.86 | 0.89 | -0.03 | 0.103682 | 0.627863 | 0.78557 | 0.893656 | 0.166503 |
| tossup_correctness | category | Religion | 365 | 0.666629 | 0.563483 | 0.0445964 | 0.190203 | 0.723288 | 0.723288 | 0 | 0.123929 | 0.594344 | 0.782327 | 0.899566 | 0.166614 |
| tossup_correctness | category | Science | 1456 | 0.657376 | 0.51045 | 0.0336208 | 0.165915 | 0.78022 | 0.76717 | 0.0130495 | 0.129132 | 0.586536 | 0.80032 | 0.907803 | 0.160489 |
| tossup_correctness | category | Social Science | 333 | 0.69433 | 0.534622 | 0.0343361 | 0.178533 | 0.738739 | 0.72973 | 0.00900901 | 0.124289 | 0.580214 | 0.752814 | 0.880431 | 0.180965 |
| tossup_correctness | category | Unknown | 1990 | 0.680832 | 0.5058 | 0.0158145 | 0.164789 | 0.775879 | 0.765829 | 0.0100503 | 0.104381 | 0.616757 | 0.775871 | 0.872193 | 0.172673 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.615091 | 0.548696 | 0.099077 | 0.181366 | 0.765363 | 0.748603 | 0.0167598 | 0.12255 | 0.532723 | 0.716913 | 0.824406 | 0.196952 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.615984 | 0.54574 | 0.0428007 | 0.180462 | 0.752351 | 0.754441 | -0.00208986 | 0.120363 | 0.56211 | 0.748314 | 0.868607 | 0.182289 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.653706 | 0.514718 | 0.0196729 | 0.168142 | 0.773037 | 0.766682 | 0.00635497 | 0.116882 | 0.592029 | 0.778858 | 0.888569 | 0.170136 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.667086 | 0.484216 | 0.0198382 | 0.155557 | 0.797179 | 0.787441 | 0.00973808 | 0.114981 | 0.622623 | 0.806415 | 0.906375 | 0.15703 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.66641 | 0.507877 | 0.0200306 | 0.164026 | 0.775144 | 0.771758 | 0.00338639 | 0.119309 | 0.615952 | 0.811895 | 0.920735 | 0.152733 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1196 | -0.809181 | 0.989672 | -4.63168 | -3.22163 | -0.721674 | -0.429071 | -0.267387 | -0.0518073 | 0.427844 |
| player | theta_2 | 1196 | -1.47155 | 1.00172 | -4.4982 | -3.32869 | -2.1862 | -1.34565 | -0.570701 | -0.15968 | 0.129815 |
| player | theta_3 | 1196 | -0.463065 | 0.313186 | -1.81287 | -1.01455 | -0.641597 | -0.44037 | -0.26394 | -0.0315992 | 0.830852 |
| player | theta_4 | 1196 | -2.05855 | 0.836612 | -4.79255 | -3.47362 | -2.6926 | -1.98057 | -1.43058 | -0.876307 | 0.27759 |
| player | theta_5 | 1196 | -0.677242 | 0.411756 | -2.38963 | -1.40298 | -0.919347 | -0.650721 | -0.389162 | -0.0935034 | 0.674627 |
| player | theta_6 | 1196 | -1.32201 | 1.07243 | -4.88238 | -3.12702 | -2.23616 | -0.91796 | -0.334755 | -0.135407 | 0.501561 |
| player | theta_norm | 1196 | 3.57112 | 0.90748 | 1.48623 | 2.20016 | 2.90832 | 3.46478 | 4.17918 | 5.18401 | 6.35719 |
| tossup | start_difficulty_d1 | 1240 | -1.12299 | 1.35402 | -3.97559 | -3.4892 | -2.73863 | -0.400961 | -0.0999506 | 0.133176 | 0.466973 |
| tossup | start_difficulty_d2 | 1240 | -1.56358 | 1.36837 | -4.38057 | -3.7701 | -2.98382 | -1.12757 | -0.304633 | -0.00121772 | 0.503726 |
| tossup | start_difficulty_d3 | 1240 | -0.217947 | 0.428199 | -2.54302 | -1.12418 | -0.298766 | -0.0973882 | 0.0215841 | 0.189738 | 0.537736 |
| tossup | start_difficulty_d4 | 1240 | -1.85895 | 1.40671 | -5.12801 | -4.23127 | -3.12266 | -1.62504 | -0.597382 | -0.000942821 | 0.393902 |
| tossup | start_difficulty_d5 | 1240 | -0.437044 | 0.669138 | -3.74695 | -1.9803 | -0.601703 | -0.203695 | -0.00602656 | 0.20184 | 0.58322 |
| tossup | start_difficulty_d6 | 1240 | -0.969756 | 1.44019 | -5.03762 | -4.0328 | -0.996811 | -0.269098 | -0.0558267 | 0.142529 | 0.457376 |
| tossup | end_difficulty_d1 | 1240 | -2.19178 | 1.49196 | -6.21677 | -4.94629 | -3.70665 | -1.41161 | -1.08594 | -0.8104 | -0.490833 |
| tossup | end_difficulty_d2 | 1240 | -2.64079 | 1.48447 | -7.49229 | -5.0838 | -3.99067 | -2.18383 | -1.29583 | -0.949052 | -0.342515 |
| tossup | end_difficulty_d3 | 1240 | -1.22474 | 0.491333 | -4.08486 | -2.24705 | -1.3244 | -1.09907 | -0.949938 | -0.756339 | -0.377546 |
| tossup | end_difficulty_d4 | 1240 | -2.91558 | 1.48309 | -7.43939 | -5.43529 | -4.12325 | -2.63338 | -1.59578 | -0.960053 | -0.495545 |
| tossup | end_difficulty_d5 | 1240 | -1.45227 | 0.741648 | -5.29824 | -3.11507 | -1.67254 | -1.20052 | -0.972353 | -0.729427 | -0.263728 |
| tossup | end_difficulty_d6 | 1240 | -1.99356 | 1.50422 | -7.38267 | -5.21189 | -2.11074 | -1.27281 | -1.03193 | -0.787166 | -0.420626 |
| tossup | total_drop_d1 | 1240 | 1.0688 | 0.231661 | 0.622586 | 0.8979 | 0.960165 | 1.00604 | 1.0731 | 1.48896 | 3.36416 |
| tossup | total_drop_d2 | 1240 | 1.07721 | 0.261651 | 0.58705 | 0.854414 | 0.95652 | 1.01297 | 1.1125 | 1.50302 | 4.40404 |
| tossup | total_drop_d3 | 1240 | 1.00679 | 0.0775232 | 0.828756 | 0.92293 | 0.963989 | 0.994069 | 1.03437 | 1.12763 | 1.69678 |
| tossup | total_drop_d4 | 1240 | 1.05663 | 0.240865 | 0.358253 | 0.772718 | 0.942013 | 1.01607 | 1.12518 | 1.47673 | 3.01117 |
| tossup | total_drop_d5 | 1240 | 1.01523 | 0.101607 | 0.846948 | 0.906017 | 0.953433 | 0.993935 | 1.04479 | 1.21076 | 1.63299 |
| tossup | total_drop_d6 | 1240 | 1.0238 | 0.22477 | 0.532064 | 0.786497 | 0.944927 | 0.990245 | 1.04432 | 1.35403 | 3.38202 |
| tossup | drop_share_1_d1 | 1240 | 0.332949 | 0.041129 | 0.277433 | 0.295165 | 0.305599 | 0.315664 | 0.350282 | 0.420089 | 0.529267 |
| tossup | drop_share_2_d1 | 1240 | 0.343441 | 0.0130812 | 0.29459 | 0.320575 | 0.336404 | 0.343705 | 0.351762 | 0.362972 | 0.427386 |
| tossup | drop_share_3_d1 | 1240 | 0.323611 | 0.0366858 | 0.173366 | 0.245104 | 0.310174 | 0.337723 | 0.348089 | 0.359904 | 0.370968 |
| tossup | drop_share_1_d2 | 1240 | 0.33865 | 0.0403024 | 0.274647 | 0.298885 | 0.311528 | 0.324545 | 0.354228 | 0.426685 | 0.560715 |
| tossup | drop_share_2_d2 | 1240 | 0.341661 | 0.0146161 | 0.274607 | 0.316289 | 0.33295 | 0.343158 | 0.351563 | 0.362327 | 0.407458 |
| tossup | drop_share_3_d2 | 1240 | 0.319689 | 0.0345294 | 0.164678 | 0.245525 | 0.305305 | 0.330013 | 0.343151 | 0.357779 | 0.406493 |
| tossup | drop_share_1_d3 | 1240 | 0.309619 | 0.0117301 | 0.281892 | 0.292742 | 0.302261 | 0.308986 | 0.31555 | 0.328151 | 0.382639 |
| tossup | drop_share_2_d3 | 1240 | 0.347281 | 0.00945948 | 0.318456 | 0.331812 | 0.340677 | 0.347388 | 0.353463 | 0.362833 | 0.381475 |
| tossup | drop_share_3_d3 | 1240 | 0.343101 | 0.0127413 | 0.271675 | 0.32182 | 0.336359 | 0.344198 | 0.351372 | 0.361198 | 0.383684 |
| tossup | drop_share_1_d4 | 1240 | 0.342749 | 0.0458107 | 0.241022 | 0.299551 | 0.314382 | 0.329056 | 0.355939 | 0.436059 | 0.625862 |
| tossup | drop_share_2_d4 | 1240 | 0.339251 | 0.0187139 | 0.233694 | 0.30677 | 0.330511 | 0.340986 | 0.350324 | 0.362622 | 0.492759 |
| tossup | drop_share_3_d4 | 1240 | 0.318 | 0.0382224 | 0.129457 | 0.237241 | 0.304685 | 0.327882 | 0.341265 | 0.359365 | 0.437788 |
| tossup | drop_share_1_d5 | 1240 | 0.312795 | 0.0135422 | 0.278274 | 0.294628 | 0.304022 | 0.310877 | 0.31915 | 0.336807 | 0.380952 |
| tossup | drop_share_2_d5 | 1240 | 0.346468 | 0.0096361 | 0.315668 | 0.330197 | 0.339853 | 0.346391 | 0.353407 | 0.361703 | 0.375075 |
| tossup | drop_share_3_d5 | 1240 | 0.340737 | 0.0141903 | 0.26661 | 0.315277 | 0.333479 | 0.341702 | 0.349621 | 0.361762 | 0.383021 |
| tossup | drop_share_1_d6 | 1240 | 0.32393 | 0.0367113 | 0.24032 | 0.29529 | 0.305019 | 0.312893 | 0.324665 | 0.400937 | 0.581429 |
| tossup | drop_share_2_d6 | 1240 | 0.342581 | 0.0161193 | 0.259497 | 0.30978 | 0.336307 | 0.345242 | 0.352588 | 0.3634 | 0.42454 |
| tossup | drop_share_3_d6 | 1240 | 0.333489 | 0.0309455 | 0.141588 | 0.268633 | 0.328749 | 0.340824 | 0.34897 | 0.36113 | 0.432604 |
| tossup | r_1 | 1240 | 0.194439 | 0.237613 | 0.0112816 | 0.020902 | 0.033051 | 0.0493685 | 0.488057 | 0.627398 | 0.761431 |
| tossup | r_2 | 1240 | 0.22588 | 0.230215 | 0.0168859 | 0.0284474 | 0.0565406 | 0.104683 | 0.404785 | 0.677829 | 0.813881 |
| tossup | r_3 | 1240 | 0.051507 | 0.031922 | 0.0119176 | 0.0204486 | 0.030914 | 0.0446579 | 0.0607481 | 0.113103 | 0.272472 |
| tossup | r_4 | 1240 | 0.287503 | 0.270313 | 0.0312306 | 0.0510467 | 0.0863879 | 0.161063 | 0.413549 | 0.79699 | 0.926616 |
| tossup | r_5 | 1240 | 0.0685923 | 0.0405596 | 0.0151655 | 0.0270618 | 0.0411055 | 0.0570036 | 0.0817449 | 0.152972 | 0.28791 |
| tossup | r_6 | 1240 | 0.172079 | 0.212879 | 0.0155934 | 0.0316905 | 0.0475883 | 0.0654631 | 0.137469 | 0.645425 | 0.778164 |
| tossup | r_norm | 1240 | 0.657317 | 0.0819699 | 0.470091 | 0.543918 | 0.59268 | 0.64535 | 0.715081 | 0.804214 | 0.927204 |
