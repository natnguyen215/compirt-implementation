# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained-10000-steps/three-slice-grid/perceived-difficulty-three-slice/dim_6/fold_3/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained-10000-steps/three-slice-grid/perceived-difficulty-three-slice/dim_6/fold_3`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 6 |
| pyramidal | steps | 10000 |
| pyramidal | final_loss | 321951 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.665471 |
| log_loss | 0.510063 |
| ece | 0.0272607 |
| brier | 0.164963 |
| accuracy | 0.77533 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | 0.00528634 |
| probability_std | 0.13254 |
| probability_p10 | 0.570421 |
| probability_p50 | 0.777698 |
| probability_p90 | 0.906246 |
| mean_predictive_variance | 0.167325 |
| integrated_brier_score | 0.100632 |
| joint_tossup_event_log_loss | 6.85329 |
| buzz_position_mae | 0.159808 |
| buzz_position_median_absolute_error | 0.145282 |
| buzz_position_bias | -0.0670675 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |
| first_buzzer_top1_accuracy | 0.349449 |
| first_buzzer_mean_reciprocal_rank | 0.561493 |
| first_buzzer_log_loss | 1.68732 |
| first_buzzer_events | 9080 |
| first_buzzer_team_top1_accuracy | 0.656057 |
| tossup_scorer_player_top1_accuracy | 0.315184 |
| tossup_scorer_team_top1_accuracy | 0.508568 |
| tossup_game_winner_accuracy | 0.825221 |
| tossup_game_margin_mae | 35.4755 |
| tournament_player_ppg_spearman | 0.711959 |
| tournament_player_ppg_mae | 8.87736 |
| tournament_player_ppg_top10_overlap | 0.668966 |
| neg_auroc | 0.665471 |
| neg_average_precision | 0.401484 |
| neg_precision | 0.554795 |
| neg_recall | 0.116379 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.0554361 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.090475 |
| no_buzz_calibration_error | 0.0752906 |
| no_buzz_brier | 0.0255715 |
| full_pmf_max_mass_error | 1.33227e-15 |
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
| tossup_correctness | aggregate | all | 9080 | 0.665471 | 0.510063 | 0.0272607 | 0.164963 | 0.77533 | 0.770044 | 0.00528634 | 0.13254 | 0.570421 | 0.777698 | 0.906246 | 0.167325 |
| tossup_correctness | tier | fall | 2817 | 0.655273 | 0.49734 | 0.0261952 | 0.159791 | 0.782748 | 0.781683 | 0.00106496 | 0.122301 | 0.598224 | 0.797837 | 0.904629 | 0.161511 |
| tossup_correctness | tier | nationals | 1542 | 0.706983 | 0.537379 | 0.0643725 | 0.178751 | 0.739948 | 0.73476 | 0.00518807 | 0.13079 | 0.493852 | 0.681988 | 0.827769 | 0.203636 |
| tossup_correctness | tier | regionals | 1934 | 0.666834 | 0.520075 | 0.0197921 | 0.17066 | 0.763702 | 0.75698 | 0.00672182 | 0.123617 | 0.575722 | 0.767084 | 0.887787 | 0.173979 |
| tossup_correctness | tier | winter | 2787 | 0.644152 | 0.500862 | 0.0344001 | 0.15861 | 0.795479 | 0.786868 | 0.00861141 | 0.128427 | 0.616148 | 0.816438 | 0.930115 | 0.148494 |
| tossup_correctness | category | Current Events | 125 | 0.734337 | 0.54269 | 0.11437 | 0.181583 | 0.696 | 0.704 | -0.008 | 0.124368 | 0.509049 | 0.703935 | 0.820007 | 0.202136 |
| tossup_correctness | category | Fine Arts | 1072 | 0.654496 | 0.511095 | 0.0418652 | 0.166588 | 0.778918 | 0.770522 | 0.00839552 | 0.131451 | 0.573128 | 0.779501 | 0.905175 | 0.165456 |
| tossup_correctness | category | Geography | 185 | 0.773706 | 0.515379 | 0.0694513 | 0.170125 | 0.735135 | 0.702703 | 0.0324324 | 0.159686 | 0.426444 | 0.704345 | 0.861312 | 0.195483 |
| tossup_correctness | category | History | 1443 | 0.716419 | 0.493516 | 0.0359617 | 0.159945 | 0.777547 | 0.765073 | 0.012474 | 0.127718 | 0.553878 | 0.757027 | 0.876414 | 0.179377 |
| tossup_correctness | category | Literature | 1411 | 0.583236 | 0.499498 | 0.051327 | 0.153291 | 0.80652 | 0.81219 | -0.00566974 | 0.115187 | 0.663781 | 0.848652 | 0.949751 | 0.131596 |
| tossup_correctness | category | Mythology | 320 | 0.600453 | 0.508735 | 0.0752732 | 0.162848 | 0.7875 | 0.79375 | -0.00625 | 0.121142 | 0.579614 | 0.774066 | 0.883378 | 0.173681 |
| tossup_correctness | category | Other Academic | 64 | 0.589844 | 0.551561 | 0.0908399 | 0.181971 | 0.78125 | 0.75 | 0.03125 | 0.106141 | 0.588575 | 0.730771 | 0.864721 | 0.189587 |
| tossup_correctness | category | Philosophy | 312 | 0.592 | 0.501478 | 0.0482218 | 0.159699 | 0.791667 | 0.801282 | -0.00961538 | 0.119808 | 0.61417 | 0.805707 | 0.916217 | 0.157369 |
| tossup_correctness | category | Popular Culture | 104 | 0.512784 | 0.474964 | 0.113008 | 0.147114 | 0.846154 | 0.846154 | 0 | 0.107885 | 0.610818 | 0.773287 | 0.88277 | 0.173212 |
| tossup_correctness | category | Religion | 358 | 0.688108 | 0.543816 | 0.0264494 | 0.181906 | 0.723464 | 0.726257 | -0.0027933 | 0.13474 | 0.556352 | 0.76052 | 0.893256 | 0.177069 |
| tossup_correctness | category | Science | 1431 | 0.673448 | 0.508836 | 0.0363871 | 0.165907 | 0.775681 | 0.765199 | 0.0104822 | 0.142431 | 0.539054 | 0.772882 | 0.90219 | 0.169731 |
| tossup_correctness | category | Social Science | 321 | 0.678947 | 0.53194 | 0.0326188 | 0.176154 | 0.744548 | 0.744548 | 0 | 0.129569 | 0.552171 | 0.741767 | 0.876365 | 0.18197 |
| tossup_correctness | category | Unknown | 1934 | 0.666834 | 0.520075 | 0.0197921 | 0.17066 | 0.763702 | 0.75698 | 0.00672182 | 0.123617 | 0.575722 | 0.767084 | 0.887787 | 0.173979 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.718219 | 0.559058 | 0.0511495 | 0.188215 | 0.713542 | 0.697917 | 0.015625 | 0.129358 | 0.489433 | 0.656954 | 0.800627 | 0.210092 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.692844 | 0.535214 | 0.0374363 | 0.177939 | 0.744657 | 0.733408 | 0.0112486 | 0.135229 | 0.510673 | 0.720107 | 0.85532 | 0.191467 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.642098 | 0.533651 | 0.0342472 | 0.174021 | 0.759729 | 0.759276 | 0.000452489 | 0.130346 | 0.566803 | 0.768397 | 0.890926 | 0.173377 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.656327 | 0.491004 | 0.0333729 | 0.15719 | 0.792262 | 0.789125 | 0.00313698 | 0.122446 | 0.596358 | 0.789193 | 0.908188 | 0.163114 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.672224 | 0.500058 | 0.0307017 | 0.160266 | 0.783904 | 0.775342 | 0.00856164 | 0.134723 | 0.581698 | 0.799938 | 0.923013 | 0.15672 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1133 | -0.693561 | 1.07912 | -4.92384 | -3.34284 | -0.471547 | -0.245744 | -0.138654 | 0.0109166 | 0.336654 |
| player | theta_2 | 1133 | -1.03984 | 1.2642 | -4.61581 | -3.55759 | -2.157 | -0.295783 | -0.153711 | -0.0106211 | 0.486172 |
| player | theta_3 | 1133 | -0.269267 | 0.289752 | -1.74215 | -0.792687 | -0.409783 | -0.226105 | -0.112878 | 0.159603 | 0.899291 |
| player | theta_4 | 1133 | -2.13001 | 1.1767 | -5.32544 | -3.69666 | -2.98151 | -2.42543 | -1.0916 | -0.129469 | 0.69913 |
| player | theta_5 | 1133 | -0.30181 | 0.359515 | -1.44294 | -0.845599 | -0.508841 | -0.304069 | -0.146439 | 0.323476 | 1.5788 |
| player | theta_6 | 1133 | -0.253434 | 0.32243 | -1.897 | -0.753918 | -0.410869 | -0.238058 | -0.101636 | 0.260042 | 1.58988 |
| player | theta_norm | 1133 | 3.16809 | 0.866868 | 1.25236 | 1.9367 | 2.53443 | 3.08255 | 3.7164 | 4.71381 | 6.10119 |
| tossup | start_difficulty_d1 | 1240 | -0.973075 | 1.44713 | -4.35179 | -3.59209 | -2.68746 | -0.132766 | 0.0384964 | 0.232377 | 0.457848 |
| tossup | start_difficulty_d2 | 1240 | -0.998689 | 1.53379 | -4.73999 | -3.92364 | -2.71832 | -0.157756 | 0.0176897 | 0.183698 | 0.485302 |
| tossup | start_difficulty_d3 | 1240 | -0.00473536 | 0.208622 | -1.21487 | -0.411875 | -0.0834897 | 0.0305329 | 0.119087 | 0.256112 | 0.540169 |
| tossup | start_difficulty_d4 | 1240 | -1.75979 | 1.88487 | -5.76625 | -4.50124 | -3.67452 | -0.434878 | -0.0348555 | 0.184995 | 0.506365 |
| tossup | start_difficulty_d5 | 1240 | -0.0498603 | 0.435104 | -2.07582 | -0.997912 | -0.160429 | 0.0507852 | 0.206968 | 0.406119 | 1.05862 |
| tossup | start_difficulty_d6 | 1240 | -0.00819238 | 0.265443 | -1.71721 | -0.503791 | -0.102917 | 0.0317791 | 0.158064 | 0.318292 | 0.680388 |
| tossup | end_difficulty_d1 | 1240 | -2.05449 | 1.62293 | -7.25248 | -5.18959 | -3.56045 | -1.14191 | -0.950097 | -0.722862 | -0.426797 |
| tossup | end_difficulty_d2 | 1240 | -2.07373 | 1.71437 | -9.67087 | -5.50392 | -3.51214 | -1.15931 | -0.964477 | -0.772659 | -0.422478 |
| tossup | end_difficulty_d3 | 1240 | -1.00097 | 0.250566 | -2.56765 | -1.46349 | -1.0982 | -0.965482 | -0.851605 | -0.690419 | -0.325122 |
| tossup | end_difficulty_d4 | 1240 | -2.83369 | 2.02688 | -9.68462 | -6.01793 | -4.75633 | -1.51168 | -1.03054 | -0.766192 | -0.394171 |
| tossup | end_difficulty_d5 | 1240 | -1.05905 | 0.52684 | -3.62954 | -2.18759 | -1.18114 | -0.937415 | -0.754328 | -0.522206 | 0.238315 |
| tossup | end_difficulty_d6 | 1240 | -1.00622 | 0.311888 | -2.9367 | -1.55892 | -1.12732 | -0.963719 | -0.808507 | -0.630455 | -0.232474 |
| tossup | total_drop_d1 | 1240 | 1.08141 | 0.304434 | 0.564035 | 0.865014 | 0.961427 | 1.00316 | 1.0583 | 1.66992 | 3.9799 |
| tossup | total_drop_d2 | 1240 | 1.07504 | 0.376286 | 0.510176 | 0.846353 | 0.956576 | 0.996812 | 1.05061 | 1.62437 | 5.68524 |
| tossup | total_drop_d3 | 1240 | 0.996233 | 0.0555434 | 0.865291 | 0.921769 | 0.959602 | 0.990188 | 1.0222 | 1.08433 | 1.4361 |
| tossup | total_drop_d4 | 1240 | 1.0739 | 0.444486 | 0.379549 | 0.663478 | 0.927488 | 0.997423 | 1.07441 | 1.77509 | 5.53075 |
| tossup | total_drop_d5 | 1240 | 1.00919 | 0.102587 | 0.820307 | 0.903167 | 0.950658 | 0.989228 | 1.03659 | 1.19655 | 1.71532 |
| tossup | total_drop_d6 | 1240 | 0.998029 | 0.0594366 | 0.842881 | 0.911607 | 0.962187 | 0.992107 | 1.02908 | 1.10971 | 1.27489 |
| tossup | drop_share_1_d1 | 1240 | 0.328472 | 0.0421934 | 0.253833 | 0.289881 | 0.301749 | 0.311784 | 0.342906 | 0.415762 | 0.532983 |
| tossup | drop_share_2_d1 | 1240 | 0.344405 | 0.0142307 | 0.28634 | 0.320018 | 0.335934 | 0.345167 | 0.35351 | 0.365899 | 0.41712 |
| tossup | drop_share_3_d1 | 1240 | 0.327123 | 0.038234 | 0.165517 | 0.246318 | 0.320718 | 0.341593 | 0.351357 | 0.362575 | 0.384662 |
| tossup | drop_share_1_d2 | 1240 | 0.328926 | 0.0464724 | 0.23931 | 0.290365 | 0.302984 | 0.312246 | 0.331483 | 0.424608 | 0.652278 |
| tossup | drop_share_2_d2 | 1240 | 0.342608 | 0.0161245 | 0.213257 | 0.315746 | 0.334838 | 0.343885 | 0.35264 | 0.363915 | 0.454085 |
| tossup | drop_share_3_d2 | 1240 | 0.328466 | 0.0388626 | 0.127524 | 0.237086 | 0.325672 | 0.341227 | 0.35111 | 0.363251 | 0.411509 |
| tossup | drop_share_1_d3 | 1240 | 0.306341 | 0.0105889 | 0.273679 | 0.289023 | 0.299275 | 0.306327 | 0.313372 | 0.323863 | 0.347859 |
| tossup | drop_share_2_d3 | 1240 | 0.347154 | 0.0106277 | 0.309152 | 0.329474 | 0.340058 | 0.347068 | 0.354122 | 0.364544 | 0.38178 |
| tossup | drop_share_3_d3 | 1240 | 0.346506 | 0.011477 | 0.30883 | 0.327068 | 0.338942 | 0.346631 | 0.354514 | 0.365413 | 0.381759 |
| tossup | drop_share_1_d4 | 1240 | 0.339511 | 0.0610444 | 0.206338 | 0.287507 | 0.30287 | 0.316383 | 0.36507 | 0.458867 | 0.683592 |
| tossup | drop_share_2_d4 | 1240 | 0.338843 | 0.0255154 | 0.204411 | 0.296822 | 0.326657 | 0.341377 | 0.353183 | 0.368831 | 0.509309 |
| tossup | drop_share_3_d4 | 1240 | 0.321646 | 0.0512723 | 0.109056 | 0.214036 | 0.304013 | 0.338327 | 0.351574 | 0.374045 | 0.469209 |
| tossup | drop_share_1_d5 | 1240 | 0.306866 | 0.0133881 | 0.274946 | 0.287567 | 0.298279 | 0.305687 | 0.314189 | 0.330288 | 0.3825 |
| tossup | drop_share_2_d5 | 1240 | 0.347627 | 0.0108765 | 0.308301 | 0.329974 | 0.340026 | 0.347595 | 0.355264 | 0.365396 | 0.382437 |
| tossup | drop_share_3_d5 | 1240 | 0.345506 | 0.0140818 | 0.271222 | 0.321121 | 0.337842 | 0.346805 | 0.354568 | 0.366812 | 0.384101 |
| tossup | drop_share_1_d6 | 1240 | 0.306455 | 0.0114635 | 0.272784 | 0.28813 | 0.298703 | 0.306348 | 0.313833 | 0.325519 | 0.356609 |
| tossup | drop_share_2_d6 | 1240 | 0.346849 | 0.0106704 | 0.312708 | 0.329689 | 0.33942 | 0.346807 | 0.35438 | 0.36403 | 0.38001 |
| tossup | drop_share_3_d6 | 1240 | 0.346696 | 0.0113304 | 0.304253 | 0.32765 | 0.339558 | 0.346643 | 0.354516 | 0.365002 | 0.386695 |
| tossup | r_1 | 1240 | 0.210995 | 0.268555 | 0.010638 | 0.0211352 | 0.0325458 | 0.0454171 | 0.559048 | 0.690195 | 0.789478 |
| tossup | r_2 | 1240 | 0.223654 | 0.290903 | 0.0118885 | 0.0232249 | 0.0356405 | 0.0611212 | 0.580998 | 0.771337 | 0.890393 |
| tossup | r_3 | 1240 | 0.0505539 | 0.0292891 | 0.00979004 | 0.0196557 | 0.0315462 | 0.0432334 | 0.0603389 | 0.109027 | 0.257047 |
| tossup | r_4 | 1240 | 0.389571 | 0.355023 | 0.0238056 | 0.0413601 | 0.0633618 | 0.114404 | 0.769184 | 0.878384 | 0.94733 |
| tossup | r_5 | 1240 | 0.0638393 | 0.0342009 | 0.0101549 | 0.0241243 | 0.0422827 | 0.0585735 | 0.0741447 | 0.133598 | 0.249136 |
| tossup | r_6 | 1240 | 0.0613866 | 0.0320599 | 0.00979658 | 0.0235195 | 0.0395887 | 0.0554366 | 0.0745739 | 0.119595 | 0.266075 |
| tossup | r_norm | 1240 | 0.731241 | 0.0872393 | 0.500243 | 0.599594 | 0.658254 | 0.727248 | 0.79607 | 0.881399 | 0.947624 |
