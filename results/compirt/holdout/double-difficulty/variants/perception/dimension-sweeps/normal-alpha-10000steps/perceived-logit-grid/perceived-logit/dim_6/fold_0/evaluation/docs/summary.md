# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-10000steps/perceived-logit-grid/perceived-logit/dim_6/fold_0/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-10000steps/perceived-logit-grid/perceived-logit/dim_6/fold_0`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 6 |
| pyramidal | steps | 10000 |
| pyramidal | final_loss | 324223 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.600645 |
| log_loss | 0.577217 |
| ece | 0.106681 |
| brier | 0.188841 |
| accuracy | 0.741044 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | -0.0242066 |
| probability_std | 0.16518 |
| probability_p10 | 0.478315 |
| probability_p50 | 0.712921 |
| probability_p90 | 0.915143 |
| mean_predictive_variance | 0.182477 |
| integrated_brier_score | 0.115174 |
| joint_tossup_event_log_loss | 6.89459 |
| buzz_position_mae | 0.188863 |
| buzz_position_median_absolute_error | 0.167143 |
| buzz_position_bias | -0.125608 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |
| first_buzzer_top1_accuracy | 0.391716 |
| first_buzzer_mean_reciprocal_rank | 0.596336 |
| first_buzzer_log_loss | 1.60121 |
| first_buzzer_events | 9295 |
| first_buzzer_team_top1_accuracy | 0.653577 |
| tossup_scorer_player_top1_accuracy | 0.31104 |
| tossup_scorer_team_top1_accuracy | 0.453397 |
| tossup_game_winner_accuracy | 0.777533 |
| tossup_game_margin_mae | 37.4995 |
| tournament_player_ppg_spearman | 0.554747 |
| tournament_player_ppg_mae | 10.6301 |
| tournament_player_ppg_top10_overlap | 0.575862 |
| neg_auroc | 0.600645 |
| neg_average_precision | 0.331983 |
| neg_precision | 0.4 |
| neg_recall | 0.206233 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.100259 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.0987895 |
| no_buzz_calibration_error | 0.0855198 |
| no_buzz_brier | 0.0297298 |
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
| tossup_correctness | aggregate | all | 9295 | 0.600645 | 0.577217 | 0.106681 | 0.188841 | 0.741044 | 0.76525 | -0.0242066 | 0.16518 | 0.478315 | 0.712921 | 0.915143 | 0.182477 |
| tossup_correctness | tier | fall | 2933 | 0.567883 | 0.559236 | 0.111843 | 0.177658 | 0.778043 | 0.791681 | -0.0136379 | 0.155745 | 0.524848 | 0.751253 | 0.939611 | 0.168252 |
| tossup_correctness | tier | nationals | 1584 | 0.605219 | 0.610622 | 0.107573 | 0.209642 | 0.677399 | 0.724747 | -0.0473485 | 0.160091 | 0.409954 | 0.657635 | 0.831568 | 0.205075 |
| tossup_correctness | tier | regionals | 1886 | 0.610902 | 0.594026 | 0.107651 | 0.199456 | 0.706257 | 0.746023 | -0.0397667 | 0.168552 | 0.422609 | 0.676482 | 0.87055 | 0.195698 |
| tossup_correctness | tier | winter | 2892 | 0.59914 | 0.566195 | 0.105289 | 0.181866 | 0.761065 | 0.773167 | -0.0121024 | 0.159571 | 0.508275 | 0.730783 | 0.932023 | 0.175904 |
| tossup_correctness | category | Current Events | 124 | 0.532431 | 0.621922 | 0.138024 | 0.203815 | 0.709677 | 0.75 | -0.0403226 | 0.173222 | 0.464406 | 0.730634 | 0.923821 | 0.175734 |
| tossup_correctness | category | Fine Arts | 1103 | 0.539618 | 0.630631 | 0.146739 | 0.203503 | 0.739801 | 0.759746 | -0.0199456 | 0.16575 | 0.48656 | 0.704226 | 0.936584 | 0.180382 |
| tossup_correctness | category | Geography | 197 | 0.575291 | 0.676325 | 0.135903 | 0.231768 | 0.649746 | 0.670051 | -0.0203046 | 0.182684 | 0.423714 | 0.686638 | 0.927216 | 0.183073 |
| tossup_correctness | category | History | 1491 | 0.61483 | 0.539252 | 0.103144 | 0.173846 | 0.777331 | 0.787391 | -0.0100604 | 0.155877 | 0.509395 | 0.730733 | 0.913619 | 0.178349 |
| tossup_correctness | category | Literature | 1472 | 0.585964 | 0.544318 | 0.107721 | 0.171801 | 0.772418 | 0.804348 | -0.0319293 | 0.160824 | 0.505277 | 0.753638 | 0.935925 | 0.170598 |
| tossup_correctness | category | Mythology | 332 | 0.596655 | 0.533466 | 0.147389 | 0.174019 | 0.78012 | 0.813253 | -0.0331325 | 0.156961 | 0.509467 | 0.680692 | 0.915816 | 0.188606 |
| tossup_correctness | category | Other Academic | 69 | 0.473982 | 0.66512 | 0.192797 | 0.231035 | 0.637681 | 0.753623 | -0.115942 | 0.161119 | 0.393483 | 0.673475 | 0.828809 | 0.20417 |
| tossup_correctness | category | Philosophy | 324 | 0.667716 | 0.51299 | 0.117533 | 0.167476 | 0.753086 | 0.799383 | -0.0462963 | 0.166082 | 0.470224 | 0.706193 | 0.919955 | 0.184648 |
| tossup_correctness | category | Popular Culture | 102 | 0.473356 | 0.563203 | 0.1689 | 0.186298 | 0.745098 | 0.833333 | -0.0882353 | 0.170997 | 0.469906 | 0.745654 | 0.925437 | 0.172532 |
| tossup_correctness | category | Religion | 372 | 0.652252 | 0.593986 | 0.0636777 | 0.198503 | 0.712366 | 0.709677 | 0.00268817 | 0.16737 | 0.462617 | 0.679789 | 0.909579 | 0.18736 |
| tossup_correctness | category | Science | 1487 | 0.626425 | 0.564065 | 0.0852875 | 0.185164 | 0.743107 | 0.752522 | -0.00941493 | 0.158771 | 0.505852 | 0.727968 | 0.916993 | 0.180012 |
| tossup_correctness | category | Social Science | 336 | 0.550127 | 0.676521 | 0.123466 | 0.224541 | 0.699405 | 0.702381 | -0.00297619 | 0.171147 | 0.468627 | 0.706192 | 0.924127 | 0.183563 |
| tossup_correctness | category | Unknown | 1886 | 0.610902 | 0.594026 | 0.107651 | 0.199456 | 0.706257 | 0.746023 | -0.0397667 | 0.168552 | 0.422609 | 0.676482 | 0.87055 | 0.195698 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.500133 | 0.703206 | 0.214853 | 0.248164 | 0.609137 | 0.736041 | -0.126904 | 0.18035 | 0.361038 | 0.56707 | 0.868018 | 0.209444 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.598654 | 0.628025 | 0.159271 | 0.216298 | 0.670051 | 0.735025 | -0.0649746 | 0.185057 | 0.364861 | 0.629552 | 0.86829 | 0.201846 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.613026 | 0.573863 | 0.131808 | 0.192105 | 0.729009 | 0.769436 | -0.0404265 | 0.167889 | 0.432381 | 0.66379 | 0.890779 | 0.195856 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.60057 | 0.556208 | 0.117244 | 0.18066 | 0.76448 | 0.78402 | -0.0195394 | 0.157431 | 0.498641 | 0.712108 | 0.923936 | 0.182636 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.614664 | 0.574845 | 0.0554011 | 0.181285 | 0.75968 | 0.756008 | 0.00367156 | 0.136628 | 0.579245 | 0.770287 | 0.946301 | 0.164132 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | alpha | 1186 | 0.508813 | 1.51684 | -3.25485 | -2.14393 | -0.899076 | 1.34645 | 1.80682 | 2.13243 | 2.73656 |
| player | beta | 1186 | -5.46386 | 1.27237 | -7.65372 | -6.97489 | -6.41053 | -5.84209 | -4.70784 | -2.75277 | -1.97788 |
| player | theta_1 | 1186 | -0.550535 | 1.39674 | -3.92518 | -2.76194 | -1.68076 | -0.577683 | 0.513559 | 1.80708 | 2.80536 |
| player | theta_2 | 1186 | -0.571526 | 1.45131 | -3.64208 | -2.7344 | -1.77481 | -0.767413 | 0.719813 | 1.69027 | 2.4332 |
| player | theta_3 | 1186 | -0.82232 | 1.97148 | -4.77129 | -3.62718 | -2.60731 | -1.09128 | 1.12189 | 2.05117 | 4.23179 |
| player | theta_4 | 1186 | -0.427747 | 1.10389 | -3.38246 | -2.26652 | -1.20241 | -0.42763 | 0.361569 | 1.44583 | 2.57393 |
| player | theta_5 | 1186 | -0.409999 | 0.830988 | -3.2218 | -1.84804 | -1.02614 | -0.314203 | 0.265844 | 0.734868 | 1.79667 |
| player | theta_6 | 1186 | -0.388995 | 0.910576 | -3.93452 | -1.90584 | -1.07834 | -0.252304 | 0.337698 | 0.882488 | 2.92358 |
| player | theta_norm | 1186 | 3.30932 | 1.23739 | 0.334597 | 1.20449 | 2.44753 | 3.26265 | 4.25052 | 5.25687 | 6.63701 |
| tossup | start_difficulty_d1 | 1240 | -0.102338 | 0.566935 | -1.94471 | -1.35492 | -0.343387 | 0.0151558 | 0.277291 | 0.601377 | 1.88914 |
| tossup | start_difficulty_d2 | 1240 | -0.121347 | 0.659818 | -2.42539 | -1.53456 | -0.372072 | 0.057355 | 0.313668 | 0.618759 | 1.45285 |
| tossup | start_difficulty_d3 | 1240 | -0.20971 | 0.742719 | -2.73469 | -1.74455 | -0.540355 | -0.0497 | 0.299142 | 0.704001 | 1.74426 |
| tossup | start_difficulty_d4 | 1240 | 0.0300486 | 0.590438 | -2.3249 | -1.54559 | -0.104213 | 0.214803 | 0.364038 | 0.606065 | 1.54821 |
| tossup | start_difficulty_d5 | 1240 | 0.146079 | 0.370218 | -2.18283 | -0.531577 | -0.010356 | 0.21416 | 0.356492 | 0.614883 | 1.64318 |
| tossup | start_difficulty_d6 | 1240 | 0.130842 | 0.397353 | -1.98916 | -0.595523 | -0.0331394 | 0.219109 | 0.364473 | 0.634569 | 1.27524 |
| tossup | end_difficulty_d1 | 1240 | -1.73236 | 1.68798 | -10.5807 | -5.5448 | -1.72454 | -1.06804 | -0.733327 | -0.39333 | 0.32411 |
| tossup | end_difficulty_d2 | 1240 | -1.86105 | 1.80744 | -9.72404 | -5.8459 | -2.27634 | -1.07068 | -0.706758 | -0.401997 | 0.325556 |
| tossup | end_difficulty_d3 | 1240 | -2.54287 | 2.35721 | -11.5676 | -7.01074 | -4.56789 | -1.33965 | -0.784272 | -0.417977 | 0.381382 |
| tossup | end_difficulty_d4 | 1240 | -1.32349 | 1.50769 | -11.5821 | -5.08706 | -1.26077 | -0.783634 | -0.600019 | -0.345934 | 0.167007 |
| tossup | end_difficulty_d5 | 1240 | -1.12089 | 1.40256 | -14.2527 | -2.22805 | -1.08817 | -0.776676 | -0.615228 | -0.349075 | 0.00954467 |
| tossup | end_difficulty_d6 | 1240 | -0.976702 | 0.90185 | -10.4952 | -1.93974 | -1.08348 | -0.767027 | -0.596858 | -0.290943 | 0.0898601 |
| tossup | total_drop_d1 | 1240 | 1.63002 | 1.47183 | 0.810845 | 0.904481 | 0.965766 | 1.02771 | 1.19804 | 5.13361 | 11.0499 |
| tossup | total_drop_d2 | 1240 | 1.7397 | 1.61248 | 0.807325 | 0.903887 | 0.963604 | 1.02364 | 1.34586 | 5.45261 | 10.1074 |
| tossup | total_drop_d3 | 1240 | 2.33316 | 2.16089 | 0.805732 | 0.909681 | 0.980196 | 1.0757 | 3.62049 | 6.97399 | 12.5786 |
| tossup | total_drop_d4 | 1240 | 1.35354 | 1.25346 | 0.808709 | 0.893416 | 0.942631 | 0.985287 | 1.07071 | 4.46045 | 10.2536 |
| tossup | total_drop_d5 | 1240 | 1.26697 | 1.39959 | 0.844124 | 0.892863 | 0.944974 | 0.983897 | 1.04368 | 1.40878 | 15.6881 |
| tossup | total_drop_d6 | 1240 | 1.10754 | 0.778647 | 0.708269 | 0.891429 | 0.939708 | 0.981556 | 1.03725 | 1.2887 | 11.1957 |
| tossup | drop_share_1_d1 | 1240 | 0.267617 | 0.0593533 | 0.0406789 | 0.114738 | 0.269556 | 0.287432 | 0.299205 | 0.318431 | 0.392223 |
| tossup | drop_share_2_d1 | 1240 | 0.332221 | 0.0530779 | 0.0552042 | 0.20006 | 0.33273 | 0.343919 | 0.35413 | 0.371559 | 0.488448 |
| tossup | drop_share_3_d1 | 1240 | 0.400162 | 0.104573 | 0.213665 | 0.333218 | 0.352185 | 0.365215 | 0.387264 | 0.683555 | 0.904117 |
| tossup | drop_share_1_d2 | 1240 | 0.262402 | 0.0663748 | 0.0495936 | 0.103941 | 0.267202 | 0.288933 | 0.300604 | 0.317749 | 0.455083 |
| tossup | drop_share_2_d2 | 1240 | 0.326206 | 0.0602861 | 0.0711363 | 0.165532 | 0.331431 | 0.343646 | 0.353211 | 0.369447 | 0.533042 |
| tossup | drop_share_3_d2 | 1240 | 0.411392 | 0.119517 | 0.241849 | 0.331755 | 0.35164 | 0.365504 | 0.388893 | 0.730681 | 0.864453 |
| tossup | drop_share_1_d3 | 1240 | 0.246762 | 0.0775297 | 0.0432295 | 0.0863676 | 0.194891 | 0.284597 | 0.298743 | 0.315198 | 0.480895 |
| tossup | drop_share_2_d3 | 1240 | 0.310354 | 0.0772237 | 0.0499177 | 0.13326 | 0.310322 | 0.341226 | 0.352719 | 0.369879 | 0.619478 |
| tossup | drop_share_3_d3 | 1240 | 0.442884 | 0.146779 | 0.212036 | 0.329759 | 0.353166 | 0.370483 | 0.492614 | 0.774706 | 0.902748 |
| tossup | drop_share_1_d4 | 1240 | 0.282233 | 0.0444992 | 0.0573926 | 0.168196 | 0.28255 | 0.293401 | 0.302884 | 0.315236 | 0.41584 |
| tossup | drop_share_2_d4 | 1240 | 0.340394 | 0.0386871 | 0.0745997 | 0.309045 | 0.336897 | 0.344935 | 0.354111 | 0.37013 | 0.520718 |
| tossup | drop_share_3_d4 | 1240 | 0.377373 | 0.0749626 | 0.241741 | 0.335738 | 0.350316 | 0.361033 | 0.371744 | 0.526944 | 0.868008 |
| tossup | drop_share_1_d5 | 1240 | 0.287765 | 0.038036 | 0.0326633 | 0.262186 | 0.284856 | 0.293935 | 0.302807 | 0.316267 | 0.361472 |
| tossup | drop_share_2_d5 | 1240 | 0.341886 | 0.0343099 | 0.0530002 | 0.322153 | 0.337656 | 0.345976 | 0.35444 | 0.367321 | 0.569404 |
| tossup | drop_share_3_d5 | 1240 | 0.370349 | 0.067187 | 0.225627 | 0.333885 | 0.349498 | 0.35889 | 0.369281 | 0.394889 | 0.914337 |
| tossup | drop_share_1_d6 | 1240 | 0.290418 | 0.0281312 | 0.0774497 | 0.257759 | 0.285274 | 0.294892 | 0.303232 | 0.315786 | 0.358199 |
| tossup | drop_share_2_d6 | 1240 | 0.343471 | 0.0239767 | 0.0978156 | 0.323985 | 0.336769 | 0.345093 | 0.353514 | 0.366301 | 0.457131 |
| tossup | drop_share_3_d6 | 1240 | 0.366111 | 0.0458584 | 0.303906 | 0.33479 | 0.350002 | 0.359325 | 0.369278 | 0.39874 | 0.824735 |
| tossup | r_1 | 1240 | 0.19347 | 0.153895 | 0.031583 | 0.0573933 | 0.0908875 | 0.130359 | 0.229187 | 0.546612 | 0.683281 |
| tossup | r_2 | 1240 | 0.204995 | 0.177 | 0.0318128 | 0.0574044 | 0.085627 | 0.123585 | 0.254348 | 0.586491 | 0.730826 |
| tossup | r_3 | 1240 | 0.245971 | 0.188979 | 0.0277621 | 0.0627285 | 0.098001 | 0.152169 | 0.406192 | 0.617996 | 0.770466 |
| tossup | r_4 | 1240 | 0.133211 | 0.118049 | 0.0317798 | 0.0448089 | 0.0661378 | 0.0894951 | 0.137782 | 0.422947 | 0.653155 |
| tossup | r_5 | 1240 | 0.110149 | 0.0748699 | 0.0276023 | 0.0464178 | 0.0649587 | 0.0878779 | 0.126782 | 0.280449 | 0.48647 |
| tossup | r_6 | 1240 | 0.112205 | 0.0797999 | 0.0310756 | 0.0465224 | 0.0654698 | 0.0864946 | 0.128892 | 0.28411 | 0.715338 |
| tossup | r_norm | 1240 | 0.542245 | 0.0702731 | 0.411497 | 0.440659 | 0.488727 | 0.534144 | 0.59204 | 0.66816 | 0.777587 |
