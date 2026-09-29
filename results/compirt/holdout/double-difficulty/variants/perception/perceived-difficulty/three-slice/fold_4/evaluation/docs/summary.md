# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/perceived-difficulty/three-slice/fold_4/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/perceived-difficulty/three-slice/fold_4`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 316595 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.608341 |
| log_loss | 0.707005 |
| ece | 0.266491 |
| brier | 0.252211 |
| accuracy | 0.589752 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | -0.183603 |
| probability_std | 0.168339 |
| probability_p10 | 0.260836 |
| probability_p50 | 0.529282 |
| probability_p90 | 0.711663 |
| mean_predictive_variance | 0.221615 |
| integrated_brier_score | 0.0942462 |
| joint_tossup_event_log_loss | 6.83365 |
| buzz_position_mae | 0.137579 |
| buzz_position_median_absolute_error | 0.114038 |
| buzz_position_bias | 0.000685034 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.371953 |
| first_buzzer_mean_reciprocal_rank | 0.578874 |
| first_buzzer_log_loss | 1.65152 |
| first_buzzer_events | 9270 |
| neg_auroc | 0.608341 |
| neg_average_precision | 0.303221 |
| neg_precision | 0.289043 |
| neg_recall | 0.554974 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.137581 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0503501 |
| no_buzz_calibration_error | 0.038623 |
| no_buzz_brier | 0.018078 |
| full_pmf_max_mass_error | 1.22125e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.608341 | 0.707005 | 0.266491 | 0.252211 | 0.589752 | 0.773355 | -0.183603 | 0.168339 | 0.260836 | 0.529282 | 0.711663 | 0.221615 |
| tossup_correctness | tier | fall | 2876 | 0.618606 | 0.724884 | 0.298529 | 0.259212 | 0.579624 | 0.793115 | -0.213491 | 0.170932 | 0.240651 | 0.518449 | 0.703588 | 0.220753 |
| tossup_correctness | tier | nationals | 1579 | 0.605238 | 0.6614 | 0.192271 | 0.234076 | 0.608613 | 0.729576 | -0.120963 | 0.143758 | 0.344536 | 0.54733 | 0.716548 | 0.227942 |
| tossup_correctness | tier | regionals | 1990 | 0.624603 | 0.68948 | 0.251322 | 0.244686 | 0.613568 | 0.765829 | -0.152261 | 0.174696 | 0.255548 | 0.541009 | 0.723816 | 0.219271 |
| tossup_correctness | tier | winter | 2825 | 0.600731 | 0.726639 | 0.286045 | 0.26052 | 0.572743 | 0.783009 | -0.210265 | 0.171417 | 0.23649 | 0.519344 | 0.706012 | 0.220607 |
| tossup_correctness | category | Current Events | 123 | 0.671313 | 0.705112 | 0.287182 | 0.252775 | 0.536585 | 0.764228 | -0.227642 | 0.158929 | 0.258428 | 0.478952 | 0.688399 | 0.224286 |
| tossup_correctness | category | Fine Arts | 1093 | 0.618812 | 0.701428 | 0.257702 | 0.249098 | 0.588289 | 0.769442 | -0.181153 | 0.16989 | 0.261478 | 0.535933 | 0.713601 | 0.221 |
| tossup_correctness | category | Geography | 191 | 0.527478 | 0.795713 | 0.242536 | 0.291132 | 0.497382 | 0.691099 | -0.193717 | 0.159893 | 0.205052 | 0.449242 | 0.628788 | 0.221788 |
| tossup_correctness | category | History | 1469 | 0.60815 | 0.709847 | 0.260609 | 0.254275 | 0.57386 | 0.758339 | -0.184479 | 0.157359 | 0.272031 | 0.519344 | 0.69202 | 0.225233 |
| tossup_correctness | category | Literature | 1436 | 0.600583 | 0.676469 | 0.280524 | 0.238001 | 0.643454 | 0.81546 | -0.172006 | 0.165027 | 0.288676 | 0.562135 | 0.72618 | 0.221546 |
| tossup_correctness | category | Mythology | 325 | 0.448333 | 0.763489 | 0.341984 | 0.278783 | 0.529231 | 0.843077 | -0.313846 | 0.158063 | 0.268631 | 0.524137 | 0.698074 | 0.225015 |
| tossup_correctness | category | Other Academic | 67 | 0.618598 | 0.747598 | 0.315261 | 0.269353 | 0.552239 | 0.791045 | -0.238806 | 0.160484 | 0.243797 | 0.499743 | 0.655603 | 0.223658 |
| tossup_correctness | category | Philosophy | 322 | 0.678868 | 0.638561 | 0.251514 | 0.222485 | 0.639752 | 0.785714 | -0.145963 | 0.168907 | 0.294237 | 0.566014 | 0.73449 | 0.220301 |
| tossup_correctness | category | Popular Culture | 100 | 0.531154 | 0.840779 | 0.432063 | 0.308454 | 0.48 | 0.89 | -0.41 | 0.166198 | 0.236308 | 0.450744 | 0.657546 | 0.220796 |
| tossup_correctness | category | Religion | 365 | 0.634188 | 0.695726 | 0.224077 | 0.247507 | 0.624658 | 0.723288 | -0.0986301 | 0.166947 | 0.261364 | 0.519782 | 0.693817 | 0.222128 |
| tossup_correctness | category | Science | 1456 | 0.582896 | 0.744964 | 0.277923 | 0.268082 | 0.553571 | 0.76717 | -0.213599 | 0.1712 | 0.233183 | 0.509874 | 0.705085 | 0.220582 |
| tossup_correctness | category | Social Science | 333 | 0.598537 | 0.708104 | 0.238568 | 0.255261 | 0.534535 | 0.72973 | -0.195195 | 0.165222 | 0.249182 | 0.501877 | 0.705944 | 0.222632 |
| tossup_correctness | category | Unknown | 1990 | 0.624603 | 0.68948 | 0.251322 | 0.244686 | 0.613568 | 0.765829 | -0.152261 | 0.174696 | 0.255548 | 0.541009 | 0.723816 | 0.219271 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.616086 | 0.825926 | 0.348357 | 0.306445 | 0.446927 | 0.748603 | -0.301676 | 0.156468 | 0.167113 | 0.425311 | 0.585683 | 0.215567 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.612012 | 0.773728 | 0.307153 | 0.281803 | 0.512017 | 0.754441 | -0.242424 | 0.162912 | 0.21349 | 0.46598 | 0.65579 | 0.220681 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.63021 | 0.742416 | 0.293512 | 0.266351 | 0.567862 | 0.766682 | -0.19882 | 0.164392 | 0.233363 | 0.495019 | 0.666956 | 0.222255 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.602895 | 0.704648 | 0.277693 | 0.251285 | 0.589993 | 0.787441 | -0.197448 | 0.164568 | 0.270858 | 0.534752 | 0.707985 | 0.222822 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.603014 | 0.654132 | 0.216897 | 0.229717 | 0.639688 | 0.771758 | -0.132069 | 0.162487 | 0.319477 | 0.581826 | 0.74245 | 0.220588 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1196 | 0.225804 | 0.95049 | -2.02959 | -1.07535 | -0.490144 | 0.0677464 | 0.910151 | 1.95923 | 3.08547 |
| player | theta_2 | 1196 | 0.178006 | 0.855003 | -1.98053 | -1.0948 | -0.423804 | 0.0903377 | 0.701819 | 1.74025 | 3.49926 |
| player | theta_3 | 1196 | 0.602884 | 1.12891 | -2.07094 | -1.16494 | -0.317374 | 0.57313 | 1.48621 | 2.49494 | 3.43213 |
| player | theta_norm | 1196 | 1.66021 | 0.772529 | 0.147407 | 0.554536 | 1.06609 | 1.56714 | 2.1841 | 3.00991 | 4.14492 |
| tossup | start_difficulty_d1 | 1240 | 1.56631 | 0.374959 | -0.378935 | 0.885558 | 1.38372 | 1.61695 | 1.806 | 2.09753 | 2.66009 |
| tossup | start_difficulty_d2 | 1240 | 1.44555 | 0.456905 | -0.778814 | 0.585029 | 1.22029 | 1.49796 | 1.73684 | 2.11118 | 2.45527 |
| tossup | start_difficulty_d3 | 1240 | 1.60302 | 0.53571 | -0.568641 | 0.539781 | 1.33597 | 1.71492 | 1.97608 | 2.28888 | 2.73925 |
| tossup | end_difficulty_d1 | 1240 | 0.355696 | 0.463166 | -2.06176 | -0.492034 | 0.138465 | 0.384254 | 0.64224 | 1.03998 | 1.7397 |
| tossup | end_difficulty_d2 | 1240 | 0.26763 | 0.553428 | -2.25434 | -0.830755 | -0.0305605 | 0.316429 | 0.647573 | 1.05925 | 1.68957 |
| tossup | end_difficulty_d3 | 1240 | 0.528135 | 0.617902 | -2.77951 | -0.653057 | 0.263814 | 0.642694 | 0.920117 | 1.3124 | 1.90774 |
| tossup | total_drop_d1 | 1240 | 1.21062 | 0.374315 | 0.477043 | 0.735955 | 0.917877 | 1.16302 | 1.43933 | 1.85712 | 3.408 |
| tossup | total_drop_d2 | 1240 | 1.17792 | 0.438765 | 0.51515 | 0.700509 | 0.863702 | 1.04623 | 1.38943 | 2.02823 | 4.02185 |
| tossup | total_drop_d3 | 1240 | 1.07488 | 0.392565 | 0.443094 | 0.681827 | 0.795433 | 0.949307 | 1.2612 | 1.81993 | 3.24941 |
| tossup | drop_share_1_d1 | 1240 | 0.187391 | 0.0637969 | 0.0610612 | 0.0982931 | 0.135501 | 0.179502 | 0.237397 | 0.295338 | 0.486692 |
| tossup | drop_share_2_d1 | 1240 | 0.264187 | 0.0762453 | 0.0717823 | 0.140163 | 0.204283 | 0.273687 | 0.323259 | 0.368935 | 0.63432 |
| tossup | drop_share_3_d1 | 1240 | 0.548422 | 0.130533 | 0.149156 | 0.362065 | 0.435246 | 0.5428 | 0.654957 | 0.756828 | 0.867157 |
| tossup | drop_share_1_d2 | 1240 | 0.207024 | 0.0652613 | 0.043038 | 0.0985677 | 0.154531 | 0.213082 | 0.262023 | 0.299889 | 0.39146 |
| tossup | drop_share_2_d2 | 1240 | 0.279924 | 0.0695454 | 0.0822018 | 0.139515 | 0.235623 | 0.299041 | 0.331412 | 0.361994 | 0.516318 |
| tossup | drop_share_3_d2 | 1240 | 0.513052 | 0.127484 | 0.265219 | 0.357491 | 0.406608 | 0.485368 | 0.604238 | 0.758532 | 0.8655 |
| tossup | drop_share_1_d3 | 1240 | 0.211603 | 0.070864 | 0.035868 | 0.0884028 | 0.153553 | 0.233593 | 0.267328 | 0.299155 | 0.516341 |
| tossup | drop_share_2_d3 | 1240 | 0.287317 | 0.0741845 | 0.0535951 | 0.133268 | 0.249392 | 0.313913 | 0.333464 | 0.362931 | 0.575648 |
| tossup | drop_share_3_d3 | 1240 | 0.50108 | 0.133105 | 0.177832 | 0.361566 | 0.40021 | 0.449008 | 0.59023 | 0.767084 | 0.910163 |
| tossup | r_1 | 1240 | 0.378902 | 0.218774 | 0.0229669 | 0.0558519 | 0.181115 | 0.389271 | 0.562377 | 0.729362 | 0.881095 |
| tossup | r_2 | 1240 | 0.258047 | 0.163514 | 0.021563 | 0.0470456 | 0.122663 | 0.23198 | 0.363705 | 0.569839 | 0.827873 |
| tossup | r_3 | 1240 | 0.363051 | 0.246365 | 0.0328307 | 0.0625529 | 0.139507 | 0.283069 | 0.58035 | 0.785038 | 0.891787 |
| tossup | r_norm | 1240 | 0.687639 | 0.0655917 | 0.577581 | 0.595782 | 0.637973 | 0.679077 | 0.727726 | 0.813587 | 0.895067 |
