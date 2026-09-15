# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained-10000-steps/perceived-logit-grid/perceived-logit/dim_6/fold_1/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained-10000-steps/perceived-logit-grid/perceived-logit/dim_6/fold_1`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 6 |
| pyramidal | steps | 10000 |
| pyramidal | final_loss | 324353 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.611127 |
| log_loss | 0.571608 |
| ece | 0.0958603 |
| brier | 0.188624 |
| accuracy | 0.734081 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.0280435 |
| probability_std | 0.165628 |
| probability_p10 | 0.470596 |
| probability_p50 | 0.711647 |
| probability_p90 | 0.908938 |
| mean_predictive_variance | 0.1831 |
| integrated_brier_score | 0.114893 |
| joint_tossup_event_log_loss | 6.85066 |
| buzz_position_mae | 0.188496 |
| buzz_position_median_absolute_error | 0.164881 |
| buzz_position_bias | -0.124673 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |
| first_buzzer_top1_accuracy | 0.387221 |
| first_buzzer_mean_reciprocal_rank | 0.590396 |
| first_buzzer_log_loss | 1.61434 |
| first_buzzer_events | 9093 |
| first_buzzer_team_top1_accuracy | 0.648411 |
| tossup_scorer_player_top1_accuracy | 0.306169 |
| tossup_scorer_team_top1_accuracy | 0.458442 |
| tossup_game_winner_accuracy | 0.774775 |
| tossup_game_margin_mae | 38.8038 |
| tournament_player_ppg_spearman | 0.586736 |
| tournament_player_ppg_mae | 10.5945 |
| tournament_player_ppg_top10_overlap | 0.627586 |
| neg_auroc | 0.611127 |
| neg_average_precision | 0.332861 |
| neg_precision | 0.394366 |
| neg_recall | 0.220065 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.10131 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0906411 |
| no_buzz_calibration_error | 0.074732 |
| no_buzz_brier | 0.0287985 |
| full_pmf_max_mass_error | 1.33227e-15 |
| tossup_outcome_events | 9240 |
| first_buzzer_team_top1_accuracy_events | 9093 |
| tossup_scorer_player_top1_accuracy_events | 9240 |
| tossup_scorer_team_top1_accuracy_events | 9240 |
| tossup_game_winner_accuracy_games | 444 |
| tossup_game_margin_mae_games | 462 |
| tournament_player_ppg_tournaments | 29 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.611127 | 0.571608 | 0.0958603 | 0.188624 | 0.734081 | 0.762125 | -0.0280435 | 0.165628 | 0.470596 | 0.711647 | 0.908938 | 0.1831 |
| tossup_correctness | tier | fall | 2842 | 0.612487 | 0.536619 | 0.0845823 | 0.172129 | 0.772343 | 0.785362 | -0.013019 | 0.154051 | 0.527739 | 0.756084 | 0.937831 | 0.167165 |
| tossup_correctness | tier | nationals | 1564 | 0.62142 | 0.609009 | 0.0864089 | 0.210161 | 0.673913 | 0.718031 | -0.0441176 | 0.169914 | 0.396029 | 0.649391 | 0.837318 | 0.203538 |
| tossup_correctness | tier | regionals | 1937 | 0.608144 | 0.575314 | 0.0975441 | 0.193598 | 0.708312 | 0.758389 | -0.0500774 | 0.160306 | 0.442425 | 0.695699 | 0.861043 | 0.194702 |
| tossup_correctness | tier | winter | 2750 | 0.58854 | 0.583887 | 0.111906 | 0.189917 | 0.746909 | 0.765818 | -0.0189091 | 0.162891 | 0.490877 | 0.713894 | 0.925498 | 0.179773 |
| tossup_correctness | category | Current Events | 126 | 0.653039 | 0.548641 | 0.0997382 | 0.186119 | 0.706349 | 0.769841 | -0.0634921 | 0.182052 | 0.440598 | 0.712969 | 0.919992 | 0.180445 |
| tossup_correctness | category | Fine Arts | 1071 | 0.624346 | 0.572764 | 0.117801 | 0.186059 | 0.742297 | 0.766573 | -0.0242764 | 0.175027 | 0.459068 | 0.694434 | 0.927514 | 0.18296 |
| tossup_correctness | category | Geography | 185 | 0.648948 | 0.599603 | 0.0827466 | 0.207833 | 0.648649 | 0.697297 | -0.0486486 | 0.187576 | 0.420599 | 0.672738 | 0.910802 | 0.186816 |
| tossup_correctness | category | History | 1440 | 0.611324 | 0.570294 | 0.0906192 | 0.188067 | 0.742361 | 0.754167 | -0.0118056 | 0.160865 | 0.49087 | 0.736035 | 0.918767 | 0.177545 |
| tossup_correctness | category | Literature | 1422 | 0.565359 | 0.551739 | 0.127632 | 0.173964 | 0.772855 | 0.814346 | -0.0414909 | 0.166749 | 0.494485 | 0.755569 | 0.936204 | 0.168795 |
| tossup_correctness | category | Mythology | 318 | 0.608908 | 0.546571 | 0.140997 | 0.180712 | 0.77044 | 0.789308 | -0.0188679 | 0.154063 | 0.487641 | 0.672762 | 0.905903 | 0.19124 |
| tossup_correctness | category | Other Academic | 66 | 0.600224 | 0.632674 | 0.117754 | 0.2171 | 0.621212 | 0.712121 | -0.0909091 | 0.160328 | 0.437084 | 0.617283 | 0.826882 | 0.210241 |
| tossup_correctness | category | Philosophy | 311 | 0.678907 | 0.551981 | 0.0812415 | 0.182378 | 0.733119 | 0.745981 | -0.0128617 | 0.175351 | 0.436251 | 0.692176 | 0.909061 | 0.185996 |
| tossup_correctness | category | Popular Culture | 102 | 0.526852 | 0.475215 | 0.17281 | 0.153054 | 0.823529 | 0.882353 | -0.0588235 | 0.152767 | 0.507539 | 0.724901 | 0.902603 | 0.181246 |
| tossup_correctness | category | Religion | 358 | 0.616029 | 0.616648 | 0.0717508 | 0.204935 | 0.709497 | 0.712291 | -0.0027933 | 0.169887 | 0.465844 | 0.725137 | 0.93535 | 0.177988 |
| tossup_correctness | category | Science | 1433 | 0.605679 | 0.584395 | 0.0778158 | 0.194917 | 0.729937 | 0.738311 | -0.00837404 | 0.155186 | 0.493955 | 0.711726 | 0.902375 | 0.184396 |
| tossup_correctness | category | Social Science | 324 | 0.624909 | 0.586623 | 0.0923379 | 0.197486 | 0.719136 | 0.731481 | -0.0123457 | 0.167995 | 0.457238 | 0.695796 | 0.924674 | 0.184794 |
| tossup_correctness | category | Unknown | 1937 | 0.608144 | 0.575314 | 0.0975441 | 0.193598 | 0.708312 | 0.758389 | -0.0500774 | 0.160306 | 0.442425 | 0.695699 | 0.861043 | 0.194702 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.644783 | 0.635051 | 0.190332 | 0.220616 | 0.646707 | 0.712575 | -0.0658683 | 0.182036 | 0.322022 | 0.564828 | 0.809858 | 0.212675 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.57952 | 0.648443 | 0.155674 | 0.226288 | 0.641447 | 0.729167 | -0.0877193 | 0.182118 | 0.366811 | 0.594075 | 0.849774 | 0.206287 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.599354 | 0.601512 | 0.136393 | 0.203107 | 0.706856 | 0.755083 | -0.048227 | 0.171643 | 0.426468 | 0.6562 | 0.883102 | 0.197679 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.611756 | 0.548273 | 0.108539 | 0.179469 | 0.755977 | 0.780942 | -0.0249648 | 0.154025 | 0.494689 | 0.708694 | 0.905561 | 0.184877 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.641892 | 0.546224 | 0.0398383 | 0.174126 | 0.764975 | 0.762029 | 0.00294599 | 0.134175 | 0.579914 | 0.776394 | 0.937624 | 0.162815 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | alpha | 1167 | 0.614862 | 1.48251 | -3.25799 | -2.112 | -0.708277 | 1.45137 | 1.8064 | 2.08782 | 2.58957 |
| player | beta | 1167 | -5.56761 | 1.2268 | -7.84811 | -6.99599 | -6.43736 | -5.94224 | -4.97587 | -2.9209 | -2.00843 |
| player | theta_1 | 1167 | -0.475331 | 1.02629 | -3.41247 | -2.20543 | -1.17055 | -0.492369 | 0.359388 | 1.01885 | 2.4552 |
| player | theta_2 | 1167 | -0.585401 | 1.3646 | -3.52731 | -2.52059 | -1.67499 | -0.759195 | 0.567991 | 1.65546 | 2.59595 |
| player | theta_3 | 1167 | -0.903575 | 1.96426 | -4.65791 | -3.64814 | -2.58738 | -1.32558 | 1.05878 | 2.09772 | 3.41012 |
| player | theta_4 | 1167 | -0.698871 | 1.45241 | -3.79578 | -2.85678 | -1.89084 | -0.817208 | 0.596398 | 1.54008 | 3.00221 |
| player | theta_5 | 1167 | -0.488476 | 0.93763 | -3.58626 | -2.06874 | -1.17044 | -0.426478 | 0.266557 | 0.926782 | 2.07755 |
| player | theta_6 | 1167 | -0.472234 | 0.950273 | -3.15203 | -2.02823 | -1.22349 | -0.446139 | 0.294318 | 0.883004 | 2.34835 |
| player | theta_norm | 1167 | 3.38684 | 1.23369 | 0.391736 | 1.2309 | 2.5458 | 3.40306 | 4.31572 | 5.34824 | 6.66425 |
| tossup | start_difficulty_d1 | 1220 | 0.0850597 | 0.381347 | -1.80425 | -0.542971 | -0.11664 | 0.110505 | 0.334599 | 0.660012 | 1.56329 |
| tossup | start_difficulty_d2 | 1220 | -0.0668124 | 0.651854 | -2.64327 | -1.47058 | -0.315733 | 0.100097 | 0.345089 | 0.69293 | 1.86922 |
| tossup | start_difficulty_d3 | 1220 | -0.158668 | 0.753872 | -2.65101 | -1.70629 | -0.51104 | 0.00256357 | 0.380681 | 0.77174 | 1.83356 |
| tossup | start_difficulty_d4 | 1220 | -0.0638735 | 0.692434 | -2.8381 | -1.66781 | -0.272979 | 0.156611 | 0.352323 | 0.726335 | 1.85662 |
| tossup | start_difficulty_d5 | 1220 | 0.150853 | 0.428057 | -2.06968 | -0.704524 | -0.0113469 | 0.230833 | 0.401734 | 0.694598 | 1.84806 |
| tossup | start_difficulty_d6 | 1220 | 0.173268 | 0.386319 | -1.94401 | -0.546561 | 0.0290912 | 0.243591 | 0.40466 | 0.640071 | 1.34685 |
| tossup | end_difficulty_d1 | 1220 | -1.28945 | 1.32321 | -9.45027 | -4.50968 | -1.26456 | -0.919058 | -0.665076 | -0.331962 | 0.274645 |
| tossup | end_difficulty_d2 | 1220 | -1.75325 | 1.80648 | -11.2072 | -5.93386 | -1.87917 | -0.984649 | -0.668808 | -0.34752 | 0.643031 |
| tossup | end_difficulty_d3 | 1220 | -2.39804 | 2.31017 | -12.1865 | -6.8404 | -4.50315 | -1.21601 | -0.686761 | -0.32355 | 0.475019 |
| tossup | end_difficulty_d4 | 1220 | -1.98721 | 2.16184 | -10.7248 | -6.66574 | -2.41671 | -0.916686 | -0.660155 | -0.33497 | 0.43319 |
| tossup | end_difficulty_d5 | 1220 | -1.09558 | 1.32058 | -11.0271 | -2.94261 | -1.08298 | -0.754404 | -0.556145 | -0.248735 | 0.168458 |
| tossup | end_difficulty_d6 | 1220 | -1.00685 | 1.12712 | -12.4144 | -2.30666 | -1.03157 | -0.743222 | -0.557277 | -0.297028 | 0.127537 |
| tossup | total_drop_d1 | 1220 | 1.37451 | 1.28641 | 0.826283 | 0.907652 | 0.958359 | 1.0038 | 1.07526 | 4.78826 | 10.7534 |
| tossup | total_drop_d2 | 1220 | 1.68644 | 1.60548 | 0.79356 | 0.906258 | 0.957434 | 1.00978 | 1.23657 | 5.57818 | 12.1515 |
| tossup | total_drop_d3 | 1220 | 2.23937 | 2.02812 | 0.796831 | 0.9044 | 0.96843 | 1.05853 | 3.59087 | 6.39471 | 13.73 |
| tossup | total_drop_d4 | 1220 | 1.92333 | 1.91176 | 0.799564 | 0.89712 | 0.954647 | 1.00381 | 1.37874 | 6.47714 | 12.4497 |
| tossup | total_drop_d5 | 1220 | 1.24643 | 1.21099 | 0.805254 | 0.890723 | 0.938516 | 0.97629 | 1.03334 | 1.89189 | 11.8637 |
| tossup | total_drop_d6 | 1220 | 1.18012 | 1.03583 | 0.684601 | 0.892193 | 0.937065 | 0.976644 | 1.03282 | 1.45582 | 12.4308 |
| tossup | drop_share_1_d1 | 1220 | 0.277608 | 0.0494501 | 0.0453132 | 0.128537 | 0.279362 | 0.2899 | 0.299553 | 0.316209 | 0.348816 |
| tossup | drop_share_2_d1 | 1220 | 0.335841 | 0.0455329 | 0.0774699 | 0.233404 | 0.336069 | 0.345441 | 0.354028 | 0.367492 | 0.458733 |
| tossup | drop_share_3_d1 | 1220 | 0.386551 | 0.0903687 | 0.288652 | 0.334851 | 0.351643 | 0.363292 | 0.377186 | 0.639028 | 0.860948 |
| tossup | drop_share_1_d2 | 1220 | 0.265909 | 0.0634797 | 0.0468025 | 0.105778 | 0.271072 | 0.289749 | 0.300299 | 0.317152 | 0.516613 |
| tossup | drop_share_2_d2 | 1220 | 0.330603 | 0.0561842 | 0.0652573 | 0.185169 | 0.332552 | 0.344219 | 0.353422 | 0.370816 | 0.509032 |
| tossup | drop_share_3_d2 | 1220 | 0.403488 | 0.110841 | 0.225764 | 0.330353 | 0.351242 | 0.364229 | 0.384048 | 0.698293 | 0.88794 |
| tossup | drop_share_1_d3 | 1220 | 0.248796 | 0.0778237 | 0.0326619 | 0.089764 | 0.212103 | 0.2844 | 0.297718 | 0.315461 | 0.592788 |
| tossup | drop_share_2_d3 | 1220 | 0.311759 | 0.076729 | 0.0532653 | 0.135489 | 0.318558 | 0.341203 | 0.35304 | 0.371106 | 0.605445 |
| tossup | drop_share_3_d3 | 1220 | 0.439445 | 0.145221 | 0.170966 | 0.331757 | 0.353263 | 0.37155 | 0.456982 | 0.772108 | 0.903127 |
| tossup | drop_share_1_d4 | 1220 | 0.263984 | 0.0664297 | 0.0322328 | 0.105233 | 0.266408 | 0.290249 | 0.299966 | 0.315666 | 0.590974 |
| tossup | drop_share_2_d4 | 1220 | 0.328962 | 0.0597579 | 0.0547897 | 0.17748 | 0.332637 | 0.343457 | 0.354285 | 0.376265 | 0.529553 |
| tossup | drop_share_3_d4 | 1220 | 0.407054 | 0.116089 | 0.193532 | 0.332733 | 0.352238 | 0.363941 | 0.384712 | 0.715318 | 0.912977 |
| tossup | drop_share_1_d5 | 1220 | 0.285982 | 0.0383075 | 0.034895 | 0.236555 | 0.283301 | 0.292804 | 0.302404 | 0.315594 | 0.384763 |
| tossup | drop_share_2_d5 | 1220 | 0.342447 | 0.0339485 | 0.0531579 | 0.321279 | 0.337383 | 0.345837 | 0.354452 | 0.368936 | 0.587329 |
| tossup | drop_share_3_d5 | 1220 | 0.371571 | 0.0646249 | 0.244984 | 0.334615 | 0.350718 | 0.359975 | 0.371099 | 0.41474 | 0.911947 |
| tossup | drop_share_1_d6 | 1220 | 0.287562 | 0.0359861 | 0.0661671 | 0.238985 | 0.284872 | 0.294538 | 0.30328 | 0.315021 | 0.359714 |
| tossup | drop_share_2_d6 | 1220 | 0.341311 | 0.0297145 | 0.0875829 | 0.320593 | 0.336227 | 0.34463 | 0.353434 | 0.366232 | 0.484158 |
| tossup | drop_share_3_d6 | 1220 | 0.371127 | 0.0601233 | 0.28759 | 0.335557 | 0.350525 | 0.359608 | 0.370132 | 0.422554 | 0.838096 |
| tossup | r_1 | 1220 | 0.143403 | 0.110095 | 0.0290093 | 0.0514834 | 0.0799953 | 0.107074 | 0.155137 | 0.430823 | 0.704884 |
| tossup | r_2 | 1220 | 0.194696 | 0.169156 | 0.0252994 | 0.055456 | 0.0839608 | 0.119635 | 0.215321 | 0.57173 | 0.709308 |
| tossup | r_3 | 1220 | 0.24554 | 0.19217 | 0.0277023 | 0.0630605 | 0.0999559 | 0.156928 | 0.399855 | 0.626529 | 0.783434 |
| tossup | r_4 | 1220 | 0.18778 | 0.160295 | 0.0340809 | 0.0514954 | 0.074651 | 0.109084 | 0.271667 | 0.516693 | 0.739512 |
| tossup | r_5 | 1220 | 0.11551 | 0.0802927 | 0.0274543 | 0.0463655 | 0.0669906 | 0.089603 | 0.128659 | 0.311605 | 0.517572 |
| tossup | r_6 | 1220 | 0.113072 | 0.0889056 | 0.0302387 | 0.0447755 | 0.0652609 | 0.0852583 | 0.120795 | 0.321679 | 0.678085 |
| tossup | r_norm | 1220 | 0.541212 | 0.0696878 | 0.411665 | 0.446688 | 0.48975 | 0.52956 | 0.581376 | 0.676067 | 0.78987 |
