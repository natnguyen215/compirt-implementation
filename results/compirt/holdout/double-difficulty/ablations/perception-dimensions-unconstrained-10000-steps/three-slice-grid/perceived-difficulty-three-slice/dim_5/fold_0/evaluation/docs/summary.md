# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained-10000-steps/three-slice-grid/perceived-difficulty-three-slice/dim_5/fold_0/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained-10000-steps/three-slice-grid/perceived-difficulty-three-slice/dim_5/fold_0`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 10000 |
| pyramidal | final_loss | 315799 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.665476 |
| log_loss | 0.515624 |
| ece | 0.0226483 |
| brier | 0.168011 |
| accuracy | 0.769769 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | 0.00451856 |
| probability_std | 0.131818 |
| probability_p10 | 0.568857 |
| probability_p50 | 0.778818 |
| probability_p90 | 0.903608 |
| mean_predictive_variance | 0.167879 |
| integrated_brier_score | 0.10277 |
| joint_tossup_event_log_loss | 6.95409 |
| buzz_position_mae | 0.161718 |
| buzz_position_median_absolute_error | 0.148127 |
| buzz_position_bias | -0.065302 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |
| first_buzzer_top1_accuracy | 0.350296 |
| first_buzzer_mean_reciprocal_rank | 0.563246 |
| first_buzzer_log_loss | 1.69001 |
| first_buzzer_events | 9295 |
| first_buzzer_team_top1_accuracy | 0.643249 |
| tossup_scorer_player_top1_accuracy | 0.322399 |
| tossup_scorer_team_top1_accuracy | 0.489915 |
| tossup_game_winner_accuracy | 0.786344 |
| tossup_game_margin_mae | 35.0561 |
| tournament_player_ppg_spearman | 0.677706 |
| tournament_player_ppg_mae | 9.32214 |
| tournament_player_ppg_top10_overlap | 0.631034 |
| neg_auroc | 0.665476 |
| neg_average_precision | 0.389791 |
| neg_precision | 0.545064 |
| neg_recall | 0.116407 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.056148 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.0922817 |
| no_buzz_calibration_error | 0.0790121 |
| no_buzz_brier | 0.0258079 |
| full_pmf_max_mass_error | 1.33227e-15 |
| tossup_outcome_events | 9420 |
| first_buzzer_team_top1_accuracy_events | 9295 |
| tossup_scorer_player_top1_accuracy_events | 9420 |
| tossup_scorer_team_top1_accuracy_events | 9420 |
| tossup_game_winner_accuracy_games | 454 |
| tossup_game_margin_mae_games | 471 |
| tournament_player_ppg_tournaments | 29 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.665476 | 0.515624 | 0.0226483 | 0.168011 | 0.769769 | 0.76525 | 0.00451856 | 0.131818 | 0.568857 | 0.778818 | 0.903608 | 0.167879 |
| tossup_correctness | tier | fall | 2933 | 0.65791 | 0.487919 | 0.0322961 | 0.156711 | 0.793727 | 0.791681 | 0.00204569 | 0.127336 | 0.584901 | 0.793544 | 0.898075 | 0.163992 |
| tossup_correctness | tier | nationals | 1584 | 0.686631 | 0.549712 | 0.049977 | 0.183743 | 0.737374 | 0.724747 | 0.0126263 | 0.131636 | 0.498721 | 0.6934 | 0.836335 | 0.201098 |
| tossup_correctness | tier | regionals | 1886 | 0.639788 | 0.547234 | 0.0299287 | 0.18151 | 0.747084 | 0.746023 | 0.00106045 | 0.126959 | 0.58978 | 0.779665 | 0.914621 | 0.165237 |
| tossup_correctness | tier | winter | 2892 | 0.67419 | 0.504438 | 0.0200778 | 0.162049 | 0.778008 | 0.773167 | 0.00484094 | 0.123683 | 0.614881 | 0.808144 | 0.918224 | 0.15535 |
| tossup_correctness | category | Current Events | 124 | 0.681582 | 0.529371 | 0.0877062 | 0.174234 | 0.782258 | 0.75 | 0.0322581 | 0.136404 | 0.497038 | 0.705201 | 0.828775 | 0.199783 |
| tossup_correctness | category | Fine Arts | 1103 | 0.637704 | 0.533539 | 0.0321516 | 0.174766 | 0.761559 | 0.759746 | 0.00181324 | 0.128351 | 0.57112 | 0.78121 | 0.903777 | 0.167514 |
| tossup_correctness | category | Geography | 197 | 0.729953 | 0.559292 | 0.0527233 | 0.18995 | 0.695431 | 0.670051 | 0.0253807 | 0.157219 | 0.432552 | 0.671155 | 0.859419 | 0.198885 |
| tossup_correctness | category | History | 1491 | 0.703215 | 0.480999 | 0.0504178 | 0.154177 | 0.792086 | 0.787391 | 0.00469484 | 0.123158 | 0.563988 | 0.761836 | 0.879581 | 0.177966 |
| tossup_correctness | category | Literature | 1472 | 0.63234 | 0.484583 | 0.036041 | 0.151081 | 0.806386 | 0.804348 | 0.00203804 | 0.110056 | 0.665322 | 0.844214 | 0.935434 | 0.135254 |
| tossup_correctness | category | Mythology | 332 | 0.6592 | 0.473642 | 0.0706561 | 0.151307 | 0.798193 | 0.813253 | -0.0150602 | 0.116813 | 0.58559 | 0.756311 | 0.883249 | 0.177502 |
| tossup_correctness | category | Other Academic | 69 | 0.579186 | 0.564621 | 0.108352 | 0.18761 | 0.768116 | 0.753623 | 0.0144928 | 0.0979103 | 0.527382 | 0.680466 | 0.811534 | 0.208818 |
| tossup_correctness | category | Philosophy | 324 | 0.673418 | 0.472341 | 0.0374897 | 0.150909 | 0.808642 | 0.799383 | 0.00925926 | 0.119782 | 0.598873 | 0.789398 | 0.901737 | 0.164344 |
| tossup_correctness | category | Popular Culture | 102 | 0.478201 | 0.510299 | 0.135421 | 0.16397 | 0.813725 | 0.833333 | -0.0196078 | 0.112431 | 0.578042 | 0.748115 | 0.84647 | 0.183641 |
| tossup_correctness | category | Religion | 372 | 0.678521 | 0.562637 | 0.0590283 | 0.191135 | 0.717742 | 0.709677 | 0.00806452 | 0.137493 | 0.523852 | 0.736895 | 0.873133 | 0.185705 |
| tossup_correctness | category | Science | 1487 | 0.690943 | 0.515273 | 0.0187142 | 0.169315 | 0.763954 | 0.752522 | 0.0114324 | 0.141477 | 0.530315 | 0.772113 | 0.891555 | 0.17306 |
| tossup_correctness | category | Social Science | 336 | 0.688136 | 0.562629 | 0.0552905 | 0.18928 | 0.708333 | 0.702381 | 0.00595238 | 0.131026 | 0.533768 | 0.729437 | 0.851339 | 0.190168 |
| tossup_correctness | category | Unknown | 1886 | 0.639788 | 0.547234 | 0.0299287 | 0.18151 | 0.747084 | 0.746023 | 0.00106045 | 0.126959 | 0.58978 | 0.779665 | 0.914621 | 0.165237 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.614854 | 0.577427 | 0.0753421 | 0.19408 | 0.736041 | 0.736041 | 0 | 0.134892 | 0.504218 | 0.688065 | 0.827235 | 0.203182 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.662931 | 0.54745 | 0.0317635 | 0.182303 | 0.744162 | 0.735025 | 0.00913706 | 0.134593 | 0.51059 | 0.728217 | 0.865087 | 0.188878 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.675707 | 0.506178 | 0.0307783 | 0.164491 | 0.776988 | 0.769436 | 0.0075522 | 0.125716 | 0.566966 | 0.76731 | 0.883869 | 0.174209 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.664869 | 0.494146 | 0.0270226 | 0.159465 | 0.782973 | 0.78402 | -0.00104676 | 0.126784 | 0.590717 | 0.791113 | 0.905609 | 0.162575 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.66423 | 0.528739 | 0.0225442 | 0.172417 | 0.76235 | 0.756008 | 0.00634179 | 0.133481 | 0.58075 | 0.794985 | 0.922164 | 0.158972 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1186 | -0.664218 | 1.05697 | -4.56999 | -3.25978 | -0.493984 | -0.247222 | -0.138855 | 0.0729059 | 1.00185 |
| player | theta_2 | 1186 | -2.65095 | 0.828991 | -5.25276 | -3.8913 | -3.18718 | -2.69081 | -2.18416 | -0.792309 | 0.186602 |
| player | theta_3 | 1186 | -0.249392 | 0.285614 | -1.54453 | -0.74375 | -0.380814 | -0.230231 | -0.112919 | 0.192548 | 1.03318 |
| player | theta_4 | 1186 | -0.276136 | 0.374096 | -1.68694 | -0.835612 | -0.487237 | -0.272916 | -0.10732 | 0.393033 | 1.51672 |
| player | theta_5 | 1186 | -0.265341 | 0.417959 | -1.89642 | -0.940656 | -0.464719 | -0.259866 | -0.0825173 | 0.427917 | 1.63701 |
| player | theta_norm | 1186 | 3.04909 | 0.761508 | 1.41751 | 1.94644 | 2.49896 | 2.97689 | 3.52737 | 4.43503 | 5.85916 |
| tossup | start_difficulty_d1 | 1240 | -0.934357 | 1.41201 | -4.11822 | -3.4633 | -2.60061 | -0.1336 | 0.0573317 | 0.256187 | 0.550432 |
| tossup | start_difficulty_d2 | 1240 | -2.63627 | 1.63636 | -6.30892 | -4.45071 | -3.7849 | -3.34425 | -0.418098 | 0.0148293 | 0.579529 |
| tossup | start_difficulty_d3 | 1240 | -0.010552 | 0.327065 | -1.57762 | -0.653072 | -0.106645 | 0.0356188 | 0.172239 | 0.399437 | 1.05216 |
| tossup | start_difficulty_d4 | 1240 | -0.0273422 | 0.422422 | -2.04387 | -0.935357 | -0.121338 | 0.0412466 | 0.175773 | 0.456566 | 1.4827 |
| tossup | start_difficulty_d5 | 1240 | -0.0438272 | 0.399224 | -1.76338 | -0.867646 | -0.211824 | 0.0384974 | 0.209581 | 0.452015 | 0.955741 |
| tossup | end_difficulty_d1 | 1240 | -2.02206 | 1.60657 | -7.68301 | -5.11046 | -3.51317 | -1.14047 | -0.919018 | -0.690266 | -0.356094 |
| tossup | end_difficulty_d2 | 1240 | -3.80731 | 1.86894 | -11.3562 | -6.3186 | -5.00575 | -4.3356 | -1.45562 | -0.956089 | -0.22752 |
| tossup | end_difficulty_d3 | 1240 | -1.01259 | 0.414933 | -3.51182 | -1.76842 | -1.12817 | -0.94711 | -0.78203 | -0.524076 | 0.243196 |
| tossup | end_difficulty_d4 | 1240 | -1.03037 | 0.509193 | -3.67617 | -2.10685 | -1.13545 | -0.943711 | -0.792218 | -0.454026 | 0.670138 |
| tossup | end_difficulty_d5 | 1240 | -1.05183 | 0.487869 | -3.49123 | -2.06505 | -1.2482 | -0.941877 | -0.736194 | -0.4687 | 0.113156 |
| tossup | total_drop_d1 | 1240 | 1.0877 | 0.340236 | 0.596168 | 0.88097 | 0.959195 | 1.00066 | 1.05644 | 1.66978 | 4.36682 |
| tossup | total_drop_d2 | 1240 | 1.17104 | 0.643802 | 0.373207 | 0.650744 | 0.876715 | 1.00673 | 1.19994 | 2.3162 | 7.7266 |
| tossup | total_drop_d3 | 1240 | 1.00204 | 0.100394 | 0.804265 | 0.901168 | 0.951203 | 0.986741 | 1.02627 | 1.13918 | 1.99135 |
| tossup | total_drop_d4 | 1240 | 1.00303 | 0.0989937 | 0.762969 | 0.895972 | 0.951254 | 0.98657 | 1.02833 | 1.16641 | 1.80811 |
| tossup | total_drop_d5 | 1240 | 1.00801 | 0.10034 | 0.797238 | 0.895704 | 0.946284 | 0.986428 | 1.04205 | 1.20491 | 1.86071 |
| tossup | drop_share_1_d1 | 1240 | 0.327672 | 0.0400381 | 0.257584 | 0.290297 | 0.301747 | 0.312333 | 0.338007 | 0.411615 | 0.496201 |
| tossup | drop_share_2_d1 | 1240 | 0.344336 | 0.013732 | 0.288657 | 0.32009 | 0.33612 | 0.345128 | 0.353077 | 0.364032 | 0.419191 |
| tossup | drop_share_3_d1 | 1240 | 0.327992 | 0.0368615 | 0.175141 | 0.247921 | 0.318645 | 0.340968 | 0.351445 | 0.36452 | 0.395516 |
| tossup | drop_share_1_d2 | 1240 | 0.358437 | 0.0653796 | 0.161413 | 0.287408 | 0.310606 | 0.344092 | 0.391687 | 0.485796 | 0.657269 |
| tossup | drop_share_2_d2 | 1240 | 0.335394 | 0.0265888 | 0.215393 | 0.296165 | 0.32025 | 0.335762 | 0.349345 | 0.373162 | 0.523697 |
| tossup | drop_share_3_d2 | 1240 | 0.306169 | 0.0564522 | 0.119342 | 0.197494 | 0.273547 | 0.320691 | 0.346233 | 0.376089 | 0.461198 |
| tossup | drop_share_1_d3 | 1240 | 0.305756 | 0.0113834 | 0.269924 | 0.28725 | 0.297784 | 0.30594 | 0.312866 | 0.324594 | 0.342611 |
| tossup | drop_share_2_d3 | 1240 | 0.347155 | 0.0110728 | 0.307381 | 0.329792 | 0.339501 | 0.346891 | 0.354609 | 0.365538 | 0.387255 |
| tossup | drop_share_3_d3 | 1240 | 0.347089 | 0.0121993 | 0.301381 | 0.327075 | 0.339603 | 0.347119 | 0.354809 | 0.366527 | 0.383737 |
| tossup | drop_share_1_d4 | 1240 | 0.306815 | 0.0127984 | 0.274817 | 0.28921 | 0.297967 | 0.305577 | 0.314104 | 0.328114 | 0.381573 |
| tossup | drop_share_2_d4 | 1240 | 0.347438 | 0.0105497 | 0.318412 | 0.330103 | 0.340681 | 0.347129 | 0.354195 | 0.365314 | 0.382014 |
| tossup | drop_share_3_d4 | 1240 | 0.345747 | 0.0135763 | 0.267758 | 0.323123 | 0.338042 | 0.346606 | 0.354843 | 0.364862 | 0.391952 |
| tossup | drop_share_1_d5 | 1240 | 0.306717 | 0.0125165 | 0.268866 | 0.287878 | 0.298513 | 0.305862 | 0.314186 | 0.327827 | 0.370867 |
| tossup | drop_share_2_d5 | 1240 | 0.347261 | 0.0110883 | 0.310376 | 0.329494 | 0.339639 | 0.347189 | 0.355108 | 0.365648 | 0.384006 |
| tossup | drop_share_3_d5 | 1240 | 0.346023 | 0.0131286 | 0.278662 | 0.322352 | 0.33874 | 0.346998 | 0.355151 | 0.365722 | 0.379932 |
| tossup | r_1 | 1240 | 0.223794 | 0.285347 | 0.0106115 | 0.0228225 | 0.0328229 | 0.0457635 | 0.59467 | 0.732237 | 0.826006 |
| tossup | r_2 | 1240 | 0.578648 | 0.319746 | 0.0401649 | 0.0649516 | 0.124644 | 0.736051 | 0.819589 | 0.885324 | 0.953244 |
| tossup | r_3 | 1240 | 0.0593988 | 0.0326182 | 0.0113935 | 0.024024 | 0.0381472 | 0.0515981 | 0.0705844 | 0.122991 | 0.280696 |
| tossup | r_4 | 1240 | 0.0677767 | 0.0401864 | 0.0123244 | 0.0271332 | 0.0421118 | 0.056656 | 0.0796317 | 0.150969 | 0.274521 |
| tossup | r_5 | 1240 | 0.0703826 | 0.0438332 | 0.0124268 | 0.0258209 | 0.0411948 | 0.0583175 | 0.0827517 | 0.164743 | 0.322622 |
| tossup | r_norm | 1240 | 0.761192 | 0.0818189 | 0.54916 | 0.627601 | 0.69775 | 0.763546 | 0.825716 | 0.887219 | 0.953532 |
