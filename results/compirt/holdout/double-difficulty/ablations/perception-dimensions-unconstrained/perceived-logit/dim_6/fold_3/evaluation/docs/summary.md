# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-logit/dim_6/fold_3/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-logit/dim_6/fold_3`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 6 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 336747 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.553538 |
| log_loss | 0.571831 |
| ece | 0.0850872 |
| brier | 0.183348 |
| accuracy | 0.769493 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | -0.000550661 |
| probability_std | 0.116415 |
| probability_p10 | 0.640385 |
| probability_p50 | 0.855904 |
| probability_p90 | 0.934293 |
| mean_predictive_variance | 0.135135 |
| integrated_brier_score | 0.174892 |
| joint_tossup_event_log_loss | 7.69023 |
| buzz_position_mae | 0.332779 |
| buzz_position_median_absolute_error | 0.332347 |
| buzz_position_bias | -0.318017 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |
| first_buzzer_top1_accuracy | 0.334912 |
| first_buzzer_mean_reciprocal_rank | 0.549773 |
| first_buzzer_log_loss | 1.70598 |
| first_buzzer_events | 9080 |
| first_buzzer_team_top1_accuracy | 0.627863 |
| tossup_scorer_player_top1_accuracy | 0.25987 |
| tossup_scorer_team_top1_accuracy | 0.410304 |
| tossup_game_winner_accuracy | 0.712389 |
| tossup_game_margin_mae | 47.2342 |
| tournament_player_ppg_spearman | 0.560641 |
| tournament_player_ppg_mae | 10.9088 |
| tournament_player_ppg_top10_overlap | 0.544828 |
| neg_auroc | 0.553538 |
| neg_average_precision | 0.287364 |
| neg_precision | 0.48 |
| neg_recall | 0.0287356 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.0326116 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.213868 |
| no_buzz_calibration_error | 0.198684 |
| no_buzz_brier | 0.0620756 |
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
| tossup_correctness | aggregate | all | 9080 | 0.553538 | 0.571831 | 0.0850872 | 0.183348 | 0.769493 | 0.770044 | -0.000550661 | 0.116415 | 0.640385 | 0.855904 | 0.934293 | 0.135135 |
| tossup_correctness | tier | fall | 2817 | 0.541892 | 0.557577 | 0.0778814 | 0.178023 | 0.780263 | 0.781683 | -0.00141995 | 0.0975957 | 0.693392 | 0.865514 | 0.92927 | 0.127707 |
| tossup_correctness | tier | nationals | 1542 | 0.608845 | 0.577575 | 0.0684536 | 0.192926 | 0.734112 | 0.73476 | -0.000648508 | 0.135957 | 0.536907 | 0.71632 | 0.899466 | 0.185694 |
| tossup_correctness | tier | regionals | 1934 | 0.528315 | 0.599486 | 0.107749 | 0.193766 | 0.755429 | 0.75698 | -0.00155119 | 0.114216 | 0.636261 | 0.83274 | 0.932685 | 0.143228 |
| tossup_correctness | tier | winter | 2787 | 0.531959 | 0.563868 | 0.0868166 | 0.176201 | 0.787944 | 0.786868 | 0.00107643 | 0.0804993 | 0.746702 | 0.891053 | 0.942575 | 0.109053 |
| tossup_correctness | category | Current Events | 125 | 0.601658 | 0.63134 | 0.135895 | 0.216544 | 0.704 | 0.704 | 0 | 0.12684 | 0.592396 | 0.823272 | 0.899205 | 0.156658 |
| tossup_correctness | category | Fine Arts | 1072 | 0.544851 | 0.586209 | 0.105235 | 0.18748 | 0.771455 | 0.770522 | 0.000932836 | 0.114544 | 0.653052 | 0.877917 | 0.938701 | 0.125346 |
| tossup_correctness | category | Geography | 185 | 0.662378 | 0.614483 | 0.111865 | 0.206444 | 0.713514 | 0.702703 | 0.0108108 | 0.119872 | 0.637569 | 0.861047 | 0.919954 | 0.137323 |
| tossup_correctness | category | History | 1443 | 0.577161 | 0.560392 | 0.0653759 | 0.18103 | 0.767845 | 0.765073 | 0.002772 | 0.112414 | 0.634382 | 0.848463 | 0.924347 | 0.139994 |
| tossup_correctness | category | Literature | 1411 | 0.526183 | 0.521164 | 0.0784126 | 0.159852 | 0.807938 | 0.81219 | -0.0042523 | 0.113954 | 0.665064 | 0.882298 | 0.945485 | 0.121535 |
| tossup_correctness | category | Mythology | 320 | 0.540444 | 0.54606 | 0.0680803 | 0.172249 | 0.784375 | 0.79375 | -0.009375 | 0.113413 | 0.673569 | 0.877993 | 0.933557 | 0.125116 |
| tossup_correctness | category | Other Academic | 64 | 0.640625 | 0.564199 | 0.0737817 | 0.185085 | 0.734375 | 0.75 | -0.015625 | 0.149724 | 0.571597 | 0.828406 | 0.931934 | 0.153007 |
| tossup_correctness | category | Philosophy | 312 | 0.474194 | 0.563062 | 0.119524 | 0.173235 | 0.801282 | 0.801282 | 0 | 0.115363 | 0.640531 | 0.875378 | 0.943528 | 0.125588 |
| tossup_correctness | category | Popular Culture | 104 | 0.488636 | 0.46429 | 0.0636829 | 0.139737 | 0.836538 | 0.846154 | -0.00961538 | 0.084673 | 0.70583 | 0.865332 | 0.921114 | 0.128531 |
| tossup_correctness | category | Religion | 358 | 0.578807 | 0.641249 | 0.115332 | 0.210107 | 0.726257 | 0.726257 | 0 | 0.118902 | 0.650632 | 0.87514 | 0.932834 | 0.127068 |
| tossup_correctness | category | Science | 1431 | 0.581618 | 0.555888 | 0.071231 | 0.180571 | 0.77079 | 0.765199 | 0.0055905 | 0.119542 | 0.626731 | 0.838105 | 0.921613 | 0.144203 |
| tossup_correctness | category | Social Science | 321 | 0.496887 | 0.647796 | 0.134695 | 0.211455 | 0.725857 | 0.744548 | -0.0186916 | 0.11675 | 0.634977 | 0.864191 | 0.928137 | 0.133765 |
| tossup_correctness | category | Unknown | 1934 | 0.528315 | 0.599486 | 0.107749 | 0.193766 | 0.755429 | 0.75698 | -0.00155119 | 0.114216 | 0.636261 | 0.83274 | 0.932685 | 0.143228 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.494725 | 0.670948 | 0.143743 | 0.227801 | 0.692708 | 0.697917 | -0.00520833 | 0.106915 | 0.623158 | 0.810627 | 0.89741 | 0.16081 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.551254 | 0.608757 | 0.0925657 | 0.202729 | 0.734533 | 0.733408 | 0.00112486 | 0.122298 | 0.599985 | 0.821954 | 0.90507 | 0.155007 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.515867 | 0.598364 | 0.0911883 | 0.194469 | 0.753846 | 0.759276 | -0.00542986 | 0.111832 | 0.646231 | 0.84577 | 0.922267 | 0.141419 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.559871 | 0.535362 | 0.0754695 | 0.169668 | 0.789125 | 0.789125 | 0 | 0.111687 | 0.649525 | 0.858138 | 0.930844 | 0.134689 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.568736 | 0.569821 | 0.0917569 | 0.179548 | 0.77774 | 0.775342 | 0.00239726 | 0.119472 | 0.645858 | 0.883035 | 0.94593 | 0.123077 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | alpha | 1133 | -1.03042 | 1.03246 | -3.51751 | -2.388 | -1.68047 | -1.21573 | -0.635544 | 1.23629 | 2.23881 |
| player | beta | 1133 | -4.15182 | 1.30465 | -7.2905 | -6.71815 | -4.93786 | -3.89197 | -3.10589 | -2.50474 | -2.01376 |
| player | theta_1 | 1133 | 0.614366 | 0.698329 | -1.92928 | -0.815316 | 0.254814 | 0.790564 | 1.10898 | 1.44429 | 2.43902 |
| player | theta_2 | 1133 | 0.68218 | 0.974162 | -2.57003 | -1.142 | 0.0525152 | 0.902546 | 1.4356 | 1.93263 | 3.04685 |
| player | theta_3 | 1133 | 0.642535 | 0.810076 | -2.12549 | -0.892902 | 0.146 | 0.782364 | 1.22544 | 1.78475 | 2.62485 |
| player | theta_4 | 1133 | 0.636249 | 0.780687 | -1.88437 | -0.866147 | 0.171625 | 0.740389 | 1.19727 | 1.72955 | 2.57388 |
| player | theta_5 | 1133 | 0.579496 | 0.709276 | -1.95494 | -0.790179 | 0.179793 | 0.712945 | 1.03925 | 1.55614 | 2.74152 |
| player | theta_6 | 1133 | 0.589078 | 0.64542 | -2.05198 | -0.691111 | 0.297173 | 0.728578 | 1.00601 | 1.41698 | 2.35157 |
| player | theta_norm | 1133 | 2.31009 | 0.791302 | 0.0763163 | 0.935903 | 1.79284 | 2.39576 | 2.82192 | 3.49252 | 5.20098 |
| tossup | start_difficulty_d1 | 1240 | -0.691286 | 0.377145 | -1.8605 | -1.34945 | -0.935056 | -0.696621 | -0.407997 | -0.0882651 | 0.289879 |
| tossup | start_difficulty_d2 | 1240 | -0.714399 | 0.401825 | -1.95332 | -1.43212 | -0.975865 | -0.709283 | -0.376548 | -0.135843 | 0.347341 |
| tossup | start_difficulty_d3 | 1240 | -0.704059 | 0.445954 | -2.09216 | -1.55627 | -0.972647 | -0.642375 | -0.385858 | -0.0615186 | 0.363288 |
| tossup | start_difficulty_d4 | 1240 | -0.68765 | 0.400402 | -1.88945 | -1.33678 | -0.988292 | -0.674064 | -0.36685 | -0.0724076 | 0.30461 |
| tossup | start_difficulty_d5 | 1240 | -0.656834 | 0.36995 | -1.69213 | -1.2641 | -0.927344 | -0.666221 | -0.369193 | -0.0451596 | 0.459662 |
| tossup | start_difficulty_d6 | 1240 | -0.659468 | 0.380392 | -1.86039 | -1.29879 | -0.930809 | -0.643412 | -0.363469 | -0.0587581 | 0.365438 |
| tossup | end_difficulty_d1 | 1240 | -1.59347 | 0.339798 | -2.58152 | -2.17808 | -1.81509 | -1.57093 | -1.38427 | -1.03414 | -0.394634 |
| tossup | end_difficulty_d2 | 1240 | -1.59104 | 0.325097 | -2.534 | -2.12984 | -1.80968 | -1.58718 | -1.38256 | -1.06769 | -0.360701 |
| tossup | end_difficulty_d3 | 1240 | -1.60265 | 0.390298 | -2.8681 | -2.32685 | -1.84668 | -1.55533 | -1.34733 | -0.99736 | -0.366866 |
| tossup | end_difficulty_d4 | 1240 | -1.59294 | 0.36048 | -2.6628 | -2.20091 | -1.83991 | -1.58026 | -1.34706 | -1.00123 | -0.483345 |
| tossup | end_difficulty_d5 | 1240 | -1.5711 | 0.338136 | -2.5111 | -2.10467 | -1.81927 | -1.56782 | -1.34121 | -0.985379 | -0.262786 |
| tossup | end_difficulty_d6 | 1240 | -1.57448 | 0.353456 | -2.61867 | -2.19586 | -1.81229 | -1.54211 | -1.34585 | -1.0178 | -0.379267 |
| tossup | total_drop_d1 | 1240 | 0.902183 | 0.182304 | 0.353071 | 0.629203 | 0.764791 | 0.88452 | 1.03611 | 1.20092 | 1.52193 |
| tossup | total_drop_d2 | 1240 | 0.876639 | 0.209923 | 0.298411 | 0.465603 | 0.750413 | 0.886612 | 1.03815 | 1.18101 | 1.55437 |
| tossup | total_drop_d3 | 1240 | 0.898588 | 0.200743 | 0.330018 | 0.5459 | 0.776392 | 0.894762 | 1.0358 | 1.21159 | 1.57376 |
| tossup | total_drop_d4 | 1240 | 0.905292 | 0.192711 | 0.371276 | 0.587015 | 0.779558 | 0.903904 | 1.03821 | 1.21802 | 1.49764 |
| tossup | total_drop_d5 | 1240 | 0.91427 | 0.175801 | 0.35688 | 0.656341 | 0.786399 | 0.89847 | 1.03598 | 1.21808 | 1.51251 |
| tossup | total_drop_d6 | 1240 | 0.915015 | 0.170057 | 0.42646 | 0.67882 | 0.779945 | 0.894801 | 1.03504 | 1.21295 | 1.46432 |
| tossup | drop_share_1_d1 | 1240 | 0.311567 | 0.0174766 | 0.237775 | 0.285326 | 0.300028 | 0.310649 | 0.322577 | 0.341336 | 0.383653 |
| tossup | drop_share_2_d1 | 1240 | 0.33728 | 0.0135654 | 0.277817 | 0.314693 | 0.328779 | 0.33757 | 0.345997 | 0.359542 | 0.38202 |
| tossup | drop_share_3_d1 | 1240 | 0.351152 | 0.0179808 | 0.291981 | 0.323451 | 0.339179 | 0.350343 | 0.361719 | 0.381371 | 0.442012 |
| tossup | drop_share_1_d2 | 1240 | 0.312184 | 0.0183227 | 0.25163 | 0.284286 | 0.300252 | 0.311466 | 0.323519 | 0.342688 | 0.395491 |
| tossup | drop_share_2_d2 | 1240 | 0.335617 | 0.016418 | 0.257468 | 0.303348 | 0.326442 | 0.337635 | 0.346859 | 0.35871 | 0.384571 |
| tossup | drop_share_3_d2 | 1240 | 0.352199 | 0.0211843 | 0.295092 | 0.32316 | 0.338157 | 0.349787 | 0.362263 | 0.392362 | 0.444047 |
| tossup | drop_share_1_d3 | 1240 | 0.312111 | 0.0202517 | 0.242554 | 0.282297 | 0.29974 | 0.310033 | 0.322215 | 0.34937 | 0.408995 |
| tossup | drop_share_2_d3 | 1240 | 0.337009 | 0.0147895 | 0.273239 | 0.311775 | 0.327792 | 0.338195 | 0.34695 | 0.359447 | 0.381312 |
| tossup | drop_share_3_d3 | 1240 | 0.35088 | 0.0198511 | 0.277363 | 0.320506 | 0.339056 | 0.350454 | 0.360651 | 0.384254 | 0.462337 |
| tossup | drop_share_1_d4 | 1240 | 0.311509 | 0.0187676 | 0.237302 | 0.282093 | 0.29972 | 0.310808 | 0.322571 | 0.343699 | 0.394077 |
| tossup | drop_share_2_d4 | 1240 | 0.33692 | 0.0143132 | 0.280819 | 0.312015 | 0.32839 | 0.337843 | 0.346875 | 0.357948 | 0.378178 |
| tossup | drop_share_3_d4 | 1240 | 0.351571 | 0.0196369 | 0.289081 | 0.324282 | 0.339187 | 0.350272 | 0.361301 | 0.384738 | 0.456092 |
| tossup | drop_share_1_d5 | 1240 | 0.310821 | 0.0171426 | 0.252475 | 0.283631 | 0.299365 | 0.311018 | 0.322105 | 0.338294 | 0.367278 |
| tossup | drop_share_2_d5 | 1240 | 0.337794 | 0.0134625 | 0.288895 | 0.314205 | 0.329239 | 0.338455 | 0.347007 | 0.358683 | 0.377803 |
| tossup | drop_share_3_d5 | 1240 | 0.351385 | 0.0176098 | 0.300424 | 0.323539 | 0.338958 | 0.351444 | 0.362063 | 0.380906 | 0.424427 |
| tossup | drop_share_1_d6 | 1240 | 0.311788 | 0.0177305 | 0.256404 | 0.284163 | 0.30017 | 0.310671 | 0.323052 | 0.340382 | 0.380089 |
| tossup | drop_share_2_d6 | 1240 | 0.338072 | 0.0130672 | 0.289701 | 0.316369 | 0.329442 | 0.338274 | 0.346904 | 0.35921 | 0.387022 |
| tossup | drop_share_3_d6 | 1240 | 0.350139 | 0.0171963 | 0.283162 | 0.321947 | 0.339276 | 0.350107 | 0.360807 | 0.378584 | 0.410775 |
| tossup | r_1 | 1240 | 0.144145 | 0.0580278 | 0.0434102 | 0.0727988 | 0.117439 | 0.141096 | 0.157507 | 0.232774 | 0.665802 |
| tossup | r_2 | 1240 | 0.188974 | 0.152274 | 0.0403868 | 0.0701038 | 0.10347 | 0.127187 | 0.193494 | 0.57991 | 0.763216 |
| tossup | r_3 | 1240 | 0.17008 | 0.0981624 | 0.0411481 | 0.0600181 | 0.118443 | 0.15593 | 0.179607 | 0.388964 | 0.725256 |
| tossup | r_4 | 1240 | 0.169539 | 0.0870908 | 0.0382715 | 0.0659977 | 0.125387 | 0.165396 | 0.186029 | 0.318047 | 0.707268 |
| tossup | r_5 | 1240 | 0.166198 | 0.061333 | 0.0435983 | 0.0703257 | 0.123605 | 0.168716 | 0.199256 | 0.258294 | 0.611512 |
| tossup | r_6 | 1240 | 0.161064 | 0.0460602 | 0.0465837 | 0.0718734 | 0.131154 | 0.174765 | 0.193263 | 0.214526 | 0.380829 |
| tossup | r_norm | 1240 | 0.460273 | 0.0741263 | 0.408614 | 0.410282 | 0.414507 | 0.423993 | 0.472335 | 0.639795 | 0.770617 |
