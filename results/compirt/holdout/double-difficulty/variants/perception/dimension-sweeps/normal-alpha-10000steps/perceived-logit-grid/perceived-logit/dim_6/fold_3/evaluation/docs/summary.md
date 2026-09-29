# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-10000steps/perceived-logit-grid/perceived-logit/dim_6/fold_3/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-10000steps/perceived-logit-grid/perceived-logit/dim_6/fold_3`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 6 |
| pyramidal | steps | 10000 |
| pyramidal | final_loss | 325470 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.611071 |
| log_loss | 0.563457 |
| ece | 0.0993276 |
| brier | 0.185496 |
| accuracy | 0.743943 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | -0.0261013 |
| probability_std | 0.16523 |
| probability_p10 | 0.474336 |
| probability_p50 | 0.713906 |
| probability_p90 | 0.909059 |
| mean_predictive_variance | 0.183116 |
| integrated_brier_score | 0.114855 |
| joint_tossup_event_log_loss | 6.83702 |
| buzz_position_mae | 0.189555 |
| buzz_position_median_absolute_error | 0.165213 |
| buzz_position_bias | -0.126364 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |
| first_buzzer_top1_accuracy | 0.39207 |
| first_buzzer_mean_reciprocal_rank | 0.596708 |
| first_buzzer_log_loss | 1.59862 |
| first_buzzer_events | 9080 |
| first_buzzer_team_top1_accuracy | 0.658921 |
| tossup_scorer_player_top1_accuracy | 0.300542 |
| tossup_scorer_team_top1_accuracy | 0.459328 |
| tossup_game_winner_accuracy | 0.774336 |
| tossup_game_margin_mae | 41.4372 |
| tournament_player_ppg_spearman | 0.593661 |
| tournament_player_ppg_mae | 10.8186 |
| tournament_player_ppg_top10_overlap | 0.634483 |
| neg_auroc | 0.611071 |
| neg_average_precision | 0.326495 |
| neg_precision | 0.395225 |
| neg_recall | 0.21408 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.0974807 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0916369 |
| no_buzz_calibration_error | 0.0764525 |
| no_buzz_brier | 0.0271094 |
| full_pmf_max_mass_error | 1.22125e-15 |
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
| tossup_correctness | aggregate | all | 9080 | 0.611071 | 0.563457 | 0.0993276 | 0.185496 | 0.743943 | 0.770044 | -0.0261013 | 0.16523 | 0.474336 | 0.713906 | 0.909059 | 0.183116 |
| tossup_correctness | tier | fall | 2817 | 0.589491 | 0.548005 | 0.087827 | 0.175074 | 0.776358 | 0.781683 | -0.00532481 | 0.148551 | 0.547795 | 0.762646 | 0.940005 | 0.164986 |
| tossup_correctness | tier | nationals | 1542 | 0.625237 | 0.603862 | 0.112472 | 0.207821 | 0.681582 | 0.73476 | -0.0531777 | 0.165086 | 0.386271 | 0.640994 | 0.824897 | 0.207559 |
| tossup_correctness | tier | regionals | 1934 | 0.627969 | 0.56699 | 0.0981857 | 0.191858 | 0.713547 | 0.75698 | -0.0434333 | 0.164772 | 0.431747 | 0.681151 | 0.867293 | 0.196102 |
| tossup_correctness | tier | winter | 2787 | 0.593396 | 0.554269 | 0.11189 | 0.179263 | 0.766774 | 0.786868 | -0.0200933 | 0.160496 | 0.500361 | 0.72344 | 0.920689 | 0.178906 |
| tossup_correctness | category | Current Events | 125 | 0.586609 | 0.611422 | 0.110321 | 0.210209 | 0.688 | 0.704 | -0.016 | 0.143687 | 0.502416 | 0.695654 | 0.861491 | 0.195706 |
| tossup_correctness | category | Fine Arts | 1072 | 0.578235 | 0.581073 | 0.113708 | 0.191707 | 0.727612 | 0.770522 | -0.0429104 | 0.164186 | 0.489026 | 0.708239 | 0.928844 | 0.182177 |
| tossup_correctness | category | Geography | 185 | 0.619161 | 0.612071 | 0.0881306 | 0.209201 | 0.675676 | 0.702703 | -0.027027 | 0.163431 | 0.47615 | 0.696083 | 0.910612 | 0.186036 |
| tossup_correctness | category | History | 1443 | 0.631052 | 0.547993 | 0.0811275 | 0.180213 | 0.756757 | 0.765073 | -0.00831601 | 0.164564 | 0.489621 | 0.726745 | 0.912235 | 0.178714 |
| tossup_correctness | category | Literature | 1411 | 0.591663 | 0.548283 | 0.128979 | 0.173636 | 0.774628 | 0.81219 | -0.037562 | 0.169177 | 0.484549 | 0.736098 | 0.930014 | 0.173846 |
| tossup_correctness | category | Mythology | 320 | 0.587032 | 0.569215 | 0.140628 | 0.185445 | 0.7625 | 0.79375 | -0.03125 | 0.16948 | 0.471323 | 0.704573 | 0.912908 | 0.184644 |
| tossup_correctness | category | Other Academic | 64 | 0.736979 | 0.520626 | 0.133577 | 0.172888 | 0.796875 | 0.75 | 0.046875 | 0.156509 | 0.500005 | 0.646946 | 0.864093 | 0.202416 |
| tossup_correctness | category | Philosophy | 312 | 0.560323 | 0.571451 | 0.141624 | 0.185412 | 0.746795 | 0.801282 | -0.0544872 | 0.16875 | 0.473517 | 0.721782 | 0.929777 | 0.179205 |
| tossup_correctness | category | Popular Culture | 104 | 0.509943 | 0.538444 | 0.184319 | 0.170777 | 0.75 | 0.846154 | -0.0961538 | 0.1685 | 0.485718 | 0.737014 | 0.916442 | 0.174891 |
| tossup_correctness | category | Religion | 358 | 0.590777 | 0.60442 | 0.112409 | 0.201856 | 0.726257 | 0.726257 | 0 | 0.172493 | 0.484476 | 0.718509 | 0.944158 | 0.175005 |
| tossup_correctness | category | Science | 1431 | 0.627337 | 0.547961 | 0.0850432 | 0.178887 | 0.770091 | 0.765199 | 0.00489168 | 0.153255 | 0.506956 | 0.720617 | 0.907272 | 0.181403 |
| tossup_correctness | category | Social Science | 321 | 0.591744 | 0.599397 | 0.114424 | 0.197651 | 0.719626 | 0.744548 | -0.0249221 | 0.16679 | 0.468025 | 0.716003 | 0.92591 | 0.179737 |
| tossup_correctness | category | Unknown | 1934 | 0.627969 | 0.56699 | 0.0981857 | 0.191858 | 0.713547 | 0.75698 | -0.0434333 | 0.164772 | 0.431747 | 0.681151 | 0.867293 | 0.196102 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.602934 | 0.683169 | 0.200974 | 0.241567 | 0.604167 | 0.697917 | -0.09375 | 0.199018 | 0.273371 | 0.554044 | 0.804428 | 0.20787 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.61406 | 0.630753 | 0.159518 | 0.217705 | 0.667042 | 0.733408 | -0.0663667 | 0.185299 | 0.334451 | 0.610865 | 0.845891 | 0.205584 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.588192 | 0.601873 | 0.144978 | 0.20138 | 0.722172 | 0.759276 | -0.0371041 | 0.168344 | 0.436853 | 0.663796 | 0.88885 | 0.196036 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.599925 | 0.545986 | 0.113151 | 0.1782 | 0.763332 | 0.789125 | -0.025793 | 0.151834 | 0.505444 | 0.709964 | 0.910672 | 0.184636 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.650391 | 0.523188 | 0.0437327 | 0.167151 | 0.773973 | 0.775342 | -0.00136986 | 0.134982 | 0.581507 | 0.774248 | 0.934913 | 0.163376 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | alpha | 1133 | 0.591899 | 1.49347 | -3.31876 | -2.0657 | -0.792503 | 1.42186 | 1.80466 | 2.12487 | 2.55066 |
| player | beta | 1133 | -5.53492 | 1.22896 | -7.88729 | -7.01267 | -6.38966 | -5.88366 | -4.92188 | -2.97797 | -2.09491 |
| player | theta_1 | 1133 | -0.511467 | 1.2094 | -3.29399 | -2.30241 | -1.56508 | -0.6252 | 0.589718 | 1.36544 | 2.94837 |
| player | theta_2 | 1133 | -0.611955 | 1.41767 | -3.49348 | -2.68822 | -1.77776 | -0.776485 | 0.638278 | 1.6379 | 2.32881 |
| player | theta_3 | 1133 | -0.855205 | 1.90673 | -4.49525 | -3.50976 | -2.54152 | -1.19681 | 1.0766 | 2.01818 | 4.02465 |
| player | theta_4 | 1133 | -0.467768 | 1.10514 | -3.26683 | -2.26946 | -1.24775 | -0.526868 | 0.41178 | 1.39473 | 2.46787 |
| player | theta_5 | 1133 | -0.733256 | 1.35373 | -4.40383 | -2.93631 | -1.8228 | -0.613324 | 0.307016 | 1.40674 | 3.41185 |
| player | theta_6 | 1133 | -0.419512 | 0.858261 | -3.62019 | -1.95541 | -1.05143 | -0.332636 | 0.273931 | 0.786093 | 1.99572 |
| player | theta_norm | 1133 | 3.40994 | 1.25002 | 0.317383 | 1.23 | 2.53302 | 3.39136 | 4.33583 | 5.3548 | 6.88163 |
| tossup | start_difficulty_d1 | 1240 | 0.0161006 | 0.477603 | -2.08614 | -0.890037 | -0.230284 | 0.0687747 | 0.328431 | 0.679305 | 1.4942 |
| tossup | start_difficulty_d2 | 1240 | -0.0994548 | 0.653791 | -2.29719 | -1.5239 | -0.345808 | 0.0608309 | 0.328829 | 0.678959 | 1.70648 |
| tossup | start_difficulty_d3 | 1240 | -0.147578 | 0.719664 | -2.48044 | -1.66869 | -0.438642 | 0.00523741 | 0.347463 | 0.740681 | 1.63554 |
| tossup | start_difficulty_d4 | 1240 | 0.0309561 | 0.608967 | -2.32236 | -1.55608 | -0.111784 | 0.219924 | 0.388024 | 0.648028 | 1.12214 |
| tossup | start_difficulty_d5 | 1240 | 0.0144791 | 0.531326 | -1.98874 | -1.15356 | -0.206039 | 0.125818 | 0.315496 | 0.70079 | 1.8382 |
| tossup | start_difficulty_d6 | 1240 | 0.164397 | 0.392751 | -1.77884 | -0.574921 | 0.0193775 | 0.236062 | 0.392356 | 0.662614 | 1.27885 |
| tossup | end_difficulty_d1 | 1240 | -1.39328 | 1.35985 | -10.2305 | -4.67062 | -1.45312 | -0.990187 | -0.686038 | -0.327559 | 0.264505 |
| tossup | end_difficulty_d2 | 1240 | -1.86802 | 1.8497 | -10.8927 | -5.89799 | -2.22908 | -1.07465 | -0.699755 | -0.404591 | 0.148014 |
| tossup | end_difficulty_d3 | 1240 | -2.23401 | 2.21823 | -11.4836 | -6.63403 | -3.76998 | -1.18438 | -0.690994 | -0.346192 | 0.457002 |
| tossup | end_difficulty_d4 | 1240 | -1.23565 | 1.43366 | -12.0436 | -4.79855 | -1.21646 | -0.76537 | -0.559777 | -0.276503 | 0.247999 |
| tossup | end_difficulty_d5 | 1240 | -1.91812 | 2.23946 | -13.9605 | -7.2008 | -1.67596 | -0.94706 | -0.691429 | -0.412748 | 0.382731 |
| tossup | end_difficulty_d6 | 1240 | -0.936945 | 0.865984 | -9.09382 | -2.10778 | -1.02726 | -0.739513 | -0.563197 | -0.243045 | 0.462941 |
| tossup | total_drop_d1 | 1240 | 1.40938 | 1.25351 | 0.81687 | 0.903855 | 0.958885 | 1.01042 | 1.11686 | 4.65028 | 9.96366 |
| tossup | total_drop_d2 | 1240 | 1.76857 | 1.66597 | 0.818507 | 0.904134 | 0.96199 | 1.0232 | 1.32468 | 5.57419 | 12.0801 |
| tossup | total_drop_d3 | 1240 | 2.08644 | 1.95546 | 0.823613 | 0.903964 | 0.964723 | 1.04829 | 2.59776 | 6.4076 | 12.4733 |
| tossup | total_drop_d4 | 1240 | 1.26661 | 1.03087 | 0.808496 | 0.886156 | 0.937533 | 0.982197 | 1.063 | 3.25479 | 10.583 |
| tossup | total_drop_d5 | 1240 | 1.9326 | 2.18471 | 0.807244 | 0.904255 | 0.959588 | 1.0077 | 1.18476 | 7.1689 | 14.9854 |
| tossup | total_drop_d6 | 1240 | 1.10134 | 0.736562 | 0.685039 | 0.886458 | 0.934106 | 0.976039 | 1.03112 | 1.33443 | 9.49775 |
| tossup | drop_share_1_d1 | 1240 | 0.275329 | 0.0517837 | 0.0548622 | 0.129351 | 0.276496 | 0.288892 | 0.299689 | 0.316936 | 0.392205 |
| tossup | drop_share_2_d1 | 1240 | 0.334552 | 0.0469766 | 0.0804261 | 0.20678 | 0.335299 | 0.344819 | 0.354147 | 0.368066 | 0.517077 |
| tossup | drop_share_3_d1 | 1240 | 0.390119 | 0.0938371 | 0.250933 | 0.333662 | 0.351877 | 0.363428 | 0.379301 | 0.663327 | 0.864712 |
| tossup | drop_share_1_d2 | 1240 | 0.262351 | 0.0672849 | 0.0420865 | 0.104202 | 0.267397 | 0.288652 | 0.300278 | 0.318065 | 0.549776 |
| tossup | drop_share_2_d2 | 1240 | 0.326159 | 0.0608375 | 0.0620583 | 0.163244 | 0.330548 | 0.343383 | 0.353152 | 0.370396 | 0.532509 |
| tossup | drop_share_3_d2 | 1240 | 0.41149 | 0.120786 | 0.228419 | 0.331021 | 0.351386 | 0.36488 | 0.386184 | 0.734081 | 0.889158 |
| tossup | drop_share_1_d3 | 1240 | 0.253132 | 0.0738207 | 0.0356776 | 0.0895007 | 0.241121 | 0.28536 | 0.299168 | 0.315208 | 0.476502 |
| tossup | drop_share_2_d3 | 1240 | 0.316317 | 0.0733658 | 0.0535203 | 0.130818 | 0.324166 | 0.342429 | 0.352753 | 0.370592 | 0.598344 |
| tossup | drop_share_3_d3 | 1240 | 0.430551 | 0.139581 | 0.205512 | 0.331111 | 0.353177 | 0.369266 | 0.418857 | 0.775328 | 0.908545 |
| tossup | drop_share_1_d4 | 1240 | 0.285123 | 0.0383417 | 0.0583852 | 0.20645 | 0.282557 | 0.292785 | 0.302211 | 0.314837 | 0.484613 |
| tossup | drop_share_2_d4 | 1240 | 0.343327 | 0.030711 | 0.0944085 | 0.316987 | 0.337049 | 0.345018 | 0.35418 | 0.370512 | 0.542373 |
| tossup | drop_share_3_d4 | 1240 | 0.371551 | 0.0579041 | 0.244457 | 0.334592 | 0.351371 | 0.36154 | 0.372116 | 0.435105 | 0.847206 |
| tossup | drop_share_1_d5 | 1240 | 0.267422 | 0.0651613 | 0.0326893 | 0.104439 | 0.275096 | 0.290572 | 0.301755 | 0.315924 | 0.476415 |
| tossup | drop_share_2_d5 | 1240 | 0.328354 | 0.059591 | 0.0535962 | 0.169207 | 0.333213 | 0.344826 | 0.354859 | 0.372721 | 0.598523 |
| tossup | drop_share_3_d5 | 1240 | 0.404224 | 0.11753 | 0.22201 | 0.33301 | 0.349898 | 0.361123 | 0.379452 | 0.730185 | 0.913714 |
| tossup | drop_share_1_d6 | 1240 | 0.290839 | 0.0272609 | 0.0625848 | 0.261005 | 0.285354 | 0.294784 | 0.303773 | 0.314559 | 0.365724 |
| tossup | drop_share_2_d6 | 1240 | 0.343688 | 0.0237549 | 0.106356 | 0.325322 | 0.337265 | 0.345067 | 0.353991 | 0.366026 | 0.423514 |
| tossup | drop_share_3_d6 | 1240 | 0.365473 | 0.0448905 | 0.298724 | 0.334816 | 0.350044 | 0.359919 | 0.370091 | 0.394452 | 0.83106 |
| tossup | r_1 | 1240 | 0.158143 | 0.123085 | 0.0312015 | 0.060422 | 0.0858879 | 0.116307 | 0.16643 | 0.471524 | 0.72262 |
| tossup | r_2 | 1240 | 0.203864 | 0.177834 | 0.0367621 | 0.0589583 | 0.0848257 | 0.121015 | 0.243935 | 0.592379 | 0.734599 |
| tossup | r_3 | 1240 | 0.229953 | 0.183294 | 0.0286423 | 0.0620678 | 0.0967689 | 0.144446 | 0.356309 | 0.607916 | 0.76411 |
| tossup | r_4 | 1240 | 0.133029 | 0.11322 | 0.0271342 | 0.0454187 | 0.0660205 | 0.0947134 | 0.141296 | 0.422097 | 0.704484 |
| tossup | r_5 | 1240 | 0.166862 | 0.136368 | 0.0302498 | 0.0512941 | 0.0767633 | 0.103153 | 0.196907 | 0.466631 | 0.642803 |
| tossup | r_6 | 1240 | 0.108149 | 0.0768663 | 0.0263093 | 0.042114 | 0.0625394 | 0.0838833 | 0.122615 | 0.26741 | 0.708144 |
| tossup | r_norm | 1240 | 0.537908 | 0.070305 | 0.412845 | 0.440944 | 0.483467 | 0.524362 | 0.586745 | 0.663544 | 0.772039 |
