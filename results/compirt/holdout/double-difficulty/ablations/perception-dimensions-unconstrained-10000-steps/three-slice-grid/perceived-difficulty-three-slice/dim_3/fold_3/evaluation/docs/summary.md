# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained-10000-steps/three-slice-grid/perceived-difficulty-three-slice/dim_3/fold_3/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained-10000-steps/three-slice-grid/perceived-difficulty-three-slice/dim_3/fold_3`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 10000 |
| pyramidal | final_loss | 311099 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.662266 |
| log_loss | 0.513303 |
| ece | 0.0367643 |
| brier | 0.166435 |
| accuracy | 0.775771 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | 0.00572687 |
| probability_std | 0.140157 |
| probability_p10 | 0.550049 |
| probability_p50 | 0.77293 |
| probability_p90 | 0.907223 |
| mean_predictive_variance | 0.168488 |
| integrated_brier_score | 0.101875 |
| joint_tossup_event_log_loss | 6.8543 |
| buzz_position_mae | 0.161087 |
| buzz_position_median_absolute_error | 0.14592 |
| buzz_position_bias | -0.0702069 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |
| first_buzzer_top1_accuracy | 0.355396 |
| first_buzzer_mean_reciprocal_rank | 0.564975 |
| first_buzzer_log_loss | 1.68178 |
| first_buzzer_events | 9080 |
| first_buzzer_team_top1_accuracy | 0.655617 |
| tossup_scorer_player_top1_accuracy | 0.319957 |
| tossup_scorer_team_top1_accuracy | 0.504881 |
| tossup_game_winner_accuracy | 0.780973 |
| tossup_game_margin_mae | 36.4745 |
| tournament_player_ppg_spearman | 0.692163 |
| tournament_player_ppg_mae | 9.12891 |
| tournament_player_ppg_top10_overlap | 0.648276 |
| neg_auroc | 0.662266 |
| neg_average_precision | 0.391128 |
| neg_precision | 0.546099 |
| neg_recall | 0.14751 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.0546649 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.085762 |
| no_buzz_calibration_error | 0.0705776 |
| no_buzz_brier | 0.0243551 |
| full_pmf_max_mass_error | 1.55431e-15 |
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
| tossup_correctness | aggregate | all | 9080 | 0.662266 | 0.513303 | 0.0367643 | 0.166435 | 0.775771 | 0.770044 | 0.00572687 | 0.140157 | 0.550049 | 0.77293 | 0.907223 | 0.168488 |
| tossup_correctness | tier | fall | 2817 | 0.658431 | 0.497977 | 0.0348133 | 0.160214 | 0.784168 | 0.781683 | 0.00248491 | 0.130431 | 0.565616 | 0.785371 | 0.898032 | 0.166356 |
| tossup_correctness | tier | nationals | 1542 | 0.678228 | 0.54867 | 0.0636362 | 0.183678 | 0.739948 | 0.73476 | 0.00518807 | 0.142778 | 0.477196 | 0.689768 | 0.84729 | 0.199441 |
| tossup_correctness | tier | regionals | 1934 | 0.658275 | 0.528364 | 0.0234937 | 0.173428 | 0.759566 | 0.75698 | 0.00258532 | 0.135 | 0.571476 | 0.78066 | 0.912316 | 0.164797 |
| tossup_correctness | tier | winter | 2787 | 0.649627 | 0.498775 | 0.0466456 | 0.15833 | 0.798349 | 0.786868 | 0.0114819 | 0.137761 | 0.582032 | 0.800837 | 0.923268 | 0.156079 |
| tossup_correctness | category | Current Events | 125 | 0.708231 | 0.556381 | 0.0641256 | 0.187874 | 0.688 | 0.704 | -0.016 | 0.13301 | 0.481763 | 0.687121 | 0.819125 | 0.205122 |
| tossup_correctness | category | Fine Arts | 1072 | 0.664482 | 0.508533 | 0.0368887 | 0.166178 | 0.780784 | 0.770522 | 0.0102612 | 0.135641 | 0.559674 | 0.772672 | 0.900081 | 0.169908 |
| tossup_correctness | category | Geography | 185 | 0.770769 | 0.522505 | 0.0870157 | 0.17289 | 0.72973 | 0.702703 | 0.027027 | 0.167238 | 0.388472 | 0.684057 | 0.852047 | 0.201253 |
| tossup_correctness | category | History | 1443 | 0.715705 | 0.500966 | 0.0590844 | 0.163035 | 0.777547 | 0.765073 | 0.012474 | 0.144633 | 0.500148 | 0.730663 | 0.873356 | 0.18654 |
| tossup_correctness | category | Literature | 1411 | 0.57589 | 0.502134 | 0.0589442 | 0.155354 | 0.802977 | 0.81219 | -0.00921332 | 0.121232 | 0.646311 | 0.836437 | 0.944107 | 0.137996 |
| tossup_correctness | category | Mythology | 320 | 0.588881 | 0.521231 | 0.106552 | 0.168172 | 0.778125 | 0.79375 | -0.015625 | 0.135761 | 0.52716 | 0.753016 | 0.876778 | 0.179648 |
| tossup_correctness | category | Other Academic | 64 | 0.604167 | 0.561807 | 0.0966012 | 0.188049 | 0.734375 | 0.75 | -0.015625 | 0.128206 | 0.485182 | 0.703307 | 0.840567 | 0.198371 |
| tossup_correctness | category | Philosophy | 312 | 0.591871 | 0.501066 | 0.0710957 | 0.159864 | 0.807692 | 0.801282 | 0.00641026 | 0.119892 | 0.610083 | 0.785186 | 0.906262 | 0.163244 |
| tossup_correctness | category | Popular Culture | 104 | 0.488636 | 0.489789 | 0.160666 | 0.152862 | 0.846154 | 0.846154 | 0 | 0.116521 | 0.571147 | 0.74965 | 0.864962 | 0.182536 |
| tossup_correctness | category | Religion | 358 | 0.691601 | 0.544838 | 0.0426374 | 0.18289 | 0.731844 | 0.726257 | 0.00558659 | 0.147441 | 0.501114 | 0.742834 | 0.882366 | 0.183604 |
| tossup_correctness | category | Science | 1431 | 0.681194 | 0.50176 | 0.0234277 | 0.162911 | 0.784067 | 0.765199 | 0.0188679 | 0.132197 | 0.573468 | 0.782483 | 0.904759 | 0.165323 |
| tossup_correctness | category | Social Science | 321 | 0.668793 | 0.539198 | 0.0590052 | 0.179183 | 0.753894 | 0.744548 | 0.00934579 | 0.141266 | 0.511538 | 0.721952 | 0.875737 | 0.18643 |
| tossup_correctness | category | Unknown | 1934 | 0.658275 | 0.528364 | 0.0234937 | 0.173428 | 0.759566 | 0.75698 | 0.00258532 | 0.135 | 0.571476 | 0.78066 | 0.912316 | 0.164797 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.714359 | 0.565112 | 0.071276 | 0.190632 | 0.703125 | 0.697917 | 0.00520833 | 0.139749 | 0.439929 | 0.658941 | 0.789714 | 0.211876 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.69254 | 0.536778 | 0.0492336 | 0.178361 | 0.741282 | 0.733408 | 0.00787402 | 0.144898 | 0.478945 | 0.713619 | 0.853719 | 0.193973 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.645299 | 0.534168 | 0.0435562 | 0.174628 | 0.763801 | 0.759276 | 0.00452489 | 0.139 | 0.538419 | 0.761502 | 0.891384 | 0.175788 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.656412 | 0.493518 | 0.0407953 | 0.158264 | 0.792611 | 0.789125 | 0.00348554 | 0.130391 | 0.575335 | 0.784978 | 0.908098 | 0.16458 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.661969 | 0.506398 | 0.0330334 | 0.163041 | 0.783562 | 0.775342 | 0.00821918 | 0.138487 | 0.575752 | 0.800201 | 0.925072 | 0.156191 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1133 | -2.64154 | 0.771619 | -5.13072 | -3.80939 | -3.16533 | -2.66106 | -2.20128 | -1.1915 | 0.292241 |
| player | theta_2 | 1133 | -0.312914 | 0.479169 | -2.31702 | -1.12376 | -0.573386 | -0.287665 | -0.0779592 | 0.494784 | 1.81944 |
| player | theta_3 | 1133 | -0.612135 | 1.09084 | -4.51441 | -3.13714 | -0.594534 | -0.267096 | -0.0652686 | 0.51495 | 1.64796 |
| player | theta_norm | 1133 | 2.99416 | 0.70636 | 1.28746 | 1.94227 | 2.47189 | 2.95557 | 3.45572 | 4.22384 | 5.59452 |
| tossup | start_difficulty_d1 | 1240 | -2.54828 | 1.53356 | -5.54629 | -4.33501 | -3.63608 | -3.18143 | -0.598623 | -0.0147842 | 0.780375 |
| tossup | start_difficulty_d2 | 1240 | -0.105005 | 0.680148 | -2.29786 | -1.45936 | -0.352633 | 0.022775 | 0.251422 | 0.826823 | 2.23709 |
| tossup | start_difficulty_d3 | 1240 | -0.84971 | 1.31385 | -3.92937 | -3.1943 | -2.41133 | -0.152847 | 0.0906372 | 0.421463 | 0.832624 |
| tossup | end_difficulty_d1 | 1240 | -3.6914 | 1.73128 | -10.3115 | -6.07425 | -4.80278 | -4.15135 | -1.68317 | -0.988652 | -0.0253796 |
| tossup | end_difficulty_d2 | 1240 | -1.13191 | 0.843835 | -4.14464 | -2.86727 | -1.38893 | -0.954345 | -0.690027 | -0.0298017 | 1.53905 |
| tossup | end_difficulty_d3 | 1240 | -1.9171 | 1.47922 | -7.57418 | -4.72029 | -3.27008 | -1.1613 | -0.883528 | -0.501316 | -0.00440204 |
| tossup | total_drop_d1 | 1240 | 1.14312 | 0.59445 | 0.362928 | 0.645801 | 0.864279 | 1.01443 | 1.17611 | 2.1842 | 7.16002 |
| tossup | total_drop_d2 | 1240 | 1.0269 | 0.18318 | 0.694527 | 0.837803 | 0.932655 | 0.981188 | 1.05129 | 1.40627 | 2.53355 |
| tossup | total_drop_d3 | 1240 | 1.06739 | 0.312158 | 0.58626 | 0.846172 | 0.945905 | 0.995899 | 1.06516 | 1.57734 | 5.4169 |
| tossup | drop_share_1_d1 | 1240 | 0.35098 | 0.0594331 | 0.201811 | 0.284468 | 0.309608 | 0.335354 | 0.384001 | 0.458305 | 0.638928 |
| tossup | drop_share_2_d1 | 1240 | 0.33742 | 0.0252577 | 0.238803 | 0.301505 | 0.32315 | 0.337404 | 0.350026 | 0.373022 | 0.500321 |
| tossup | drop_share_3_d1 | 1240 | 0.311601 | 0.0532477 | 0.122269 | 0.214389 | 0.280054 | 0.325153 | 0.346787 | 0.383479 | 0.473175 |
| tossup | drop_share_1_d2 | 1240 | 0.308388 | 0.0164622 | 0.266049 | 0.284185 | 0.297784 | 0.306566 | 0.31696 | 0.338105 | 0.396487 |
| tossup | drop_share_2_d2 | 1240 | 0.347844 | 0.0110396 | 0.316935 | 0.330143 | 0.340367 | 0.347672 | 0.354901 | 0.36605 | 0.391438 |
| tossup | drop_share_3_d2 | 1240 | 0.343769 | 0.0176595 | 0.264946 | 0.310051 | 0.334064 | 0.345561 | 0.355533 | 0.369179 | 0.389708 |
| tossup | drop_share_1_d3 | 1240 | 0.323524 | 0.0350593 | 0.247816 | 0.289165 | 0.301339 | 0.311346 | 0.331654 | 0.40005 | 0.528283 |
| tossup | drop_share_2_d3 | 1240 | 0.344761 | 0.0138448 | 0.290864 | 0.322029 | 0.336206 | 0.345066 | 0.353121 | 0.365463 | 0.422064 |
| tossup | drop_share_3_d3 | 1240 | 0.331715 | 0.032937 | 0.180852 | 0.261158 | 0.322388 | 0.34186 | 0.352959 | 0.366045 | 0.391669 |
| tossup | r_1 | 1240 | 0.634217 | 0.345516 | 0.0425962 | 0.0676115 | 0.165851 | 0.816249 | 0.896759 | 0.944816 | 0.978637 |
| tossup | r_2 | 1240 | 0.0862307 | 0.0609898 | 0.010856 | 0.0226686 | 0.0408031 | 0.0645188 | 0.116693 | 0.213054 | 0.308706 |
| tossup | r_3 | 1240 | 0.279553 | 0.332402 | 0.0105075 | 0.0241312 | 0.0436752 | 0.0755836 | 0.701958 | 0.866753 | 0.929082 |
| tossup | r_norm | 1240 | 0.846367 | 0.0699112 | 0.647361 | 0.721512 | 0.79641 | 0.855037 | 0.902404 | 0.945622 | 0.978753 |
