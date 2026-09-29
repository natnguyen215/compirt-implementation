# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/training/incorrect-loss-weight/weight-1.5/fold_0/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/training/incorrect-loss-weight/weight-1.5/fold_0`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 287813 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.715515 |
| log_loss | 0.499773 |
| ece | 0.0572705 |
| brier | 0.163317 |
| accuracy | 0.770199 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | 0.0049489 |
| probability_std | 0.17046 |
| probability_p10 | 0.459719 |
| probability_p50 | 0.748686 |
| probability_p90 | 0.893288 |
| mean_predictive_variance | 0.177688 |
| integrated_brier_score | 0.102098 |
| joint_tossup_event_log_loss | 6.63007 |
| buzz_position_mae | 0.152543 |
| buzz_position_median_absolute_error | 0.135938 |
| buzz_position_bias | -0.0426747 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |
| first_buzzer_top1_accuracy | 0.353954 |
| first_buzzer_mean_reciprocal_rank | 0.567614 |
| first_buzzer_log_loss | 1.66681 |
| first_buzzer_events | 9295 |
| neg_auroc | 0.715515 |
| neg_average_precision | 0.446181 |
| neg_precision | 0.518791 |
| neg_recall | 0.291017 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.188231 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.0159933 |
| no_buzz_calibration_error | 0.00272364 |
| no_buzz_brier | 0.0131 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.715515 | 0.499773 | 0.0572705 | 0.163317 | 0.770199 | 0.76525 | 0.0049489 | 0.17046 | 0.459719 | 0.748686 | 0.893288 | 0.177688 |
| tossup_correctness | tier | fall | 2933 | 0.712919 | 0.478857 | 0.0729176 | 0.154696 | 0.786567 | 0.791681 | -0.00511422 | 0.171673 | 0.46272 | 0.761881 | 0.902544 | 0.172671 |
| tossup_correctness | tier | nationals | 1584 | 0.709888 | 0.532192 | 0.0386417 | 0.176515 | 0.748737 | 0.724747 | 0.0239899 | 0.179315 | 0.422594 | 0.738203 | 0.886619 | 0.181707 |
| tossup_correctness | tier | regionals | 1886 | 0.70924 | 0.522395 | 0.0512285 | 0.173386 | 0.742312 | 0.746023 | -0.00371156 | 0.16425 | 0.463323 | 0.725653 | 0.880729 | 0.185009 |
| tossup_correctness | tier | winter | 2892 | 0.720543 | 0.488476 | 0.0578476 | 0.158264 | 0.783541 | 0.773167 | 0.0103734 | 0.166845 | 0.481219 | 0.75172 | 0.896131 | 0.1758 |
| tossup_correctness | category | Current Events | 124 | 0.681235 | 0.54275 | 0.0889277 | 0.179712 | 0.766129 | 0.75 | 0.016129 | 0.188409 | 0.424529 | 0.684199 | 0.897578 | 0.185513 |
| tossup_correctness | category | Fine Arts | 1103 | 0.710479 | 0.50356 | 0.0480042 | 0.164396 | 0.770626 | 0.759746 | 0.0108794 | 0.17417 | 0.472711 | 0.754418 | 0.899091 | 0.174263 |
| tossup_correctness | category | Geography | 197 | 0.785897 | 0.528858 | 0.0931187 | 0.173555 | 0.741117 | 0.670051 | 0.071066 | 0.227271 | 0.294278 | 0.659832 | 0.876627 | 0.184966 |
| tossup_correctness | category | History | 1491 | 0.72384 | 0.479882 | 0.075407 | 0.15538 | 0.788732 | 0.787391 | 0.00134138 | 0.166081 | 0.469761 | 0.748993 | 0.899058 | 0.177261 |
| tossup_correctness | category | Literature | 1472 | 0.729586 | 0.444445 | 0.0569773 | 0.139517 | 0.821332 | 0.804348 | 0.0169837 | 0.145925 | 0.543911 | 0.791981 | 0.90396 | 0.163739 |
| tossup_correctness | category | Mythology | 332 | 0.693787 | 0.462539 | 0.0725784 | 0.146557 | 0.810241 | 0.813253 | -0.00301205 | 0.14347 | 0.526345 | 0.767262 | 0.892139 | 0.171473 |
| tossup_correctness | category | Other Academic | 69 | 0.684389 | 0.519205 | 0.0662365 | 0.170981 | 0.753623 | 0.753623 | 0 | 0.126969 | 0.508588 | 0.711064 | 0.856867 | 0.194997 |
| tossup_correctness | category | Philosophy | 324 | 0.695575 | 0.48223 | 0.0822276 | 0.155924 | 0.790123 | 0.799383 | -0.00925926 | 0.156293 | 0.500421 | 0.751459 | 0.895385 | 0.177972 |
| tossup_correctness | category | Popular Culture | 102 | 0.442907 | 0.49589 | 0.107755 | 0.154987 | 0.813725 | 0.833333 | -0.0196078 | 0.100473 | 0.653499 | 0.796966 | 0.877263 | 0.159404 |
| tossup_correctness | category | Religion | 372 | 0.717487 | 0.543449 | 0.0500791 | 0.183416 | 0.723118 | 0.709677 | 0.0134409 | 0.176142 | 0.417206 | 0.691379 | 0.872932 | 0.191947 |
| tossup_correctness | category | Science | 1487 | 0.690078 | 0.526845 | 0.0611615 | 0.175173 | 0.743107 | 0.752522 | -0.00941493 | 0.180546 | 0.420022 | 0.733786 | 0.89191 | 0.180749 |
| tossup_correctness | category | Social Science | 336 | 0.726483 | 0.540834 | 0.0561557 | 0.180609 | 0.741071 | 0.702381 | 0.0386905 | 0.20123 | 0.369605 | 0.71641 | 0.887544 | 0.182219 |
| tossup_correctness | category | Unknown | 1886 | 0.70924 | 0.522395 | 0.0512285 | 0.173386 | 0.742312 | 0.746023 | -0.00371156 | 0.16425 | 0.463323 | 0.725653 | 0.880729 | 0.185009 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.691247 | 0.544485 | 0.122894 | 0.176288 | 0.781726 | 0.736041 | 0.0456853 | 0.171443 | 0.416498 | 0.68637 | 0.861814 | 0.195085 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.715904 | 0.523993 | 0.0439976 | 0.174259 | 0.749239 | 0.735025 | 0.0142132 | 0.172418 | 0.441993 | 0.733359 | 0.881325 | 0.18367 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.701159 | 0.504721 | 0.0547117 | 0.165052 | 0.767215 | 0.769436 | -0.00222124 | 0.166197 | 0.478993 | 0.751183 | 0.895297 | 0.176272 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.703087 | 0.486413 | 0.0588849 | 0.157448 | 0.785764 | 0.78402 | 0.00174459 | 0.162402 | 0.490193 | 0.76588 | 0.899863 | 0.172869 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.736586 | 0.497933 | 0.0612605 | 0.163177 | 0.763685 | 0.756008 | 0.0076769 | 0.178113 | 0.428854 | 0.73797 | 0.889578 | 0.180251 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1186 | 2.67344 | 0.752451 | 0.477699 | 1.45117 | 2.15453 | 2.67161 | 3.17289 | 3.97228 | 4.6286 |
| player | theta_1 | 1186 | -1.20875 | 0.871414 | -3.61985 | -2.54315 | -1.74655 | -1.26382 | -0.680347 | 0.334102 | 2.28317 |
| player | theta_2 | 1186 | -1.03339 | 0.688248 | -3.60194 | -2.08559 | -1.46241 | -1.06873 | -0.573769 | 0.0783782 | 1.21073 |
| player | theta_3 | 1186 | -1.12733 | 0.802645 | -3.44653 | -2.37276 | -1.67152 | -1.17149 | -0.639924 | 0.272558 | 2.31581 |
| player | theta_norm | 1186 | 2.2892 | 0.659915 | 0.304459 | 1.2874 | 1.8397 | 2.23613 | 2.71025 | 3.4252 | 4.58103 |
| tossup | start_difficulty_d1 | 1240 | -1.3959 | 0.601268 | -3.73178 | -2.24397 | -1.79784 | -1.46093 | -1.04731 | -0.368633 | 1.56383 |
| tossup | start_difficulty_d2 | 1240 | -1.38312 | 0.555537 | -3.09523 | -2.2424 | -1.75045 | -1.42866 | -1.03354 | -0.372363 | 0.886563 |
| tossup | start_difficulty_d3 | 1240 | -1.38265 | 0.560452 | -3.56087 | -2.26781 | -1.7763 | -1.40708 | -1.03022 | -0.442627 | 1.94284 |
| tossup | end_difficulty_d1 | 1240 | -2.38686 | 0.700956 | -4.9903 | -3.38757 | -2.85005 | -2.44775 | -1.96919 | -1.20091 | 0.976822 |
| tossup | end_difficulty_d2 | 1240 | -2.36938 | 0.651234 | -4.48389 | -3.39467 | -2.80015 | -2.41615 | -1.96356 | -1.18555 | 0.2647 |
| tossup | end_difficulty_d3 | 1240 | -2.36664 | 0.653377 | -4.92468 | -3.39999 | -2.82312 | -2.38382 | -1.94222 | -1.31897 | 1.25526 |
| tossup | total_drop_d1 | 1240 | 0.990959 | 0.129693 | 0.587006 | 0.787651 | 0.908407 | 0.992068 | 1.07272 | 1.1851 | 1.85378 |
| tossup | total_drop_d2 | 1240 | 0.986253 | 0.115484 | 0.621863 | 0.794222 | 0.91049 | 0.987967 | 1.05833 | 1.17798 | 1.45961 |
| tossup | total_drop_d3 | 1240 | 0.983988 | 0.116926 | 0.589567 | 0.800044 | 0.906553 | 0.982152 | 1.0563 | 1.18909 | 1.47233 |
| tossup | drop_share_1_d1 | 1240 | 0.303248 | 0.0175424 | 0.211865 | 0.274044 | 0.293391 | 0.304033 | 0.314307 | 0.329709 | 0.374794 |
| tossup | drop_share_2_d1 | 1240 | 0.347191 | 0.0120697 | 0.309858 | 0.326936 | 0.339279 | 0.347338 | 0.355389 | 0.366218 | 0.425881 |
| tossup | drop_share_3_d1 | 1240 | 0.349561 | 0.0185551 | 0.29343 | 0.322189 | 0.337189 | 0.349048 | 0.360587 | 0.380074 | 0.439888 |
| tossup | drop_share_1_d2 | 1240 | 0.30301 | 0.0153077 | 0.237721 | 0.275792 | 0.293767 | 0.303724 | 0.313392 | 0.327401 | 0.351813 |
| tossup | drop_share_2_d2 | 1240 | 0.346926 | 0.0118192 | 0.309106 | 0.327168 | 0.339069 | 0.346759 | 0.355006 | 0.366067 | 0.391146 |
| tossup | drop_share_3_d2 | 1240 | 0.350064 | 0.0170983 | 0.299094 | 0.323247 | 0.338924 | 0.350323 | 0.360479 | 0.37832 | 0.422301 |
| tossup | drop_share_1_d3 | 1240 | 0.302889 | 0.0164746 | 0.23641 | 0.276628 | 0.292477 | 0.303364 | 0.313927 | 0.328559 | 0.36802 |
| tossup | drop_share_2_d3 | 1240 | 0.347133 | 0.0115253 | 0.303988 | 0.328487 | 0.339833 | 0.347103 | 0.354659 | 0.365762 | 0.392355 |
| tossup | drop_share_3_d3 | 1240 | 0.349978 | 0.0175141 | 0.297386 | 0.32367 | 0.338338 | 0.349705 | 0.359543 | 0.380341 | 0.447443 |
| tossup | r_1 | 1240 | 0.329684 | 0.171768 | 0.0568038 | 0.111724 | 0.192452 | 0.292607 | 0.442051 | 0.661177 | 0.827403 |
| tossup | r_2 | 1240 | 0.329071 | 0.144886 | 0.0565551 | 0.12754 | 0.221553 | 0.309452 | 0.416064 | 0.60619 | 0.836604 |
| tossup | r_3 | 1240 | 0.341246 | 0.153033 | 0.0714231 | 0.128934 | 0.222581 | 0.323309 | 0.431768 | 0.639876 | 0.868769 |
| tossup | r_norm | 1240 | 0.635919 | 0.0537834 | 0.577375 | 0.580457 | 0.595168 | 0.619874 | 0.660441 | 0.747124 | 0.8738 |
| tossup_hazard | hazard_start_difficulty_d1 | 1240 | 4.47813 | 0.492632 | 1.7652 | 3.74624 | 4.19897 | 4.43978 | 4.73228 | 5.39203 | 6.35118 |
| tossup_hazard | hazard_start_difficulty_d2 | 1240 | 4.44746 | 0.435408 | 2.47112 | 3.74615 | 4.22147 | 4.42457 | 4.6615 | 5.18542 | 6.61543 |
| tossup_hazard | hazard_start_difficulty_d3 | 1240 | 4.47197 | 0.439621 | 2.57715 | 3.75196 | 4.23375 | 4.46587 | 4.70883 | 5.20381 | 6.25104 |
| tossup_hazard | hazard_end_difficulty_d1 | 1240 | 1.76007 | 2.31929 | -11.298 | -3.33259 | 0.730547 | 2.86099 | 3.2902 | 3.65261 | 4.45609 |
| tossup_hazard | hazard_end_difficulty_d2 | 1240 | 2.23785 | 2.115 | -8.61415 | -2.79595 | 2.35362 | 3.10138 | 3.37697 | 3.72022 | 4.30231 |
| tossup_hazard | hazard_end_difficulty_d3 | 1240 | 2.22653 | 2.16558 | -10.4543 | -2.84476 | 2.2598 | 3.12009 | 3.39619 | 3.74816 | 4.22767 |
| tossup_hazard | hazard_total_drop_d1 | 1240 | 2.71807 | 2.49472 | 0.889022 | 0.98208 | 1.0576 | 1.33728 | 3.99996 | 8.19812 | 16.0103 |
| tossup_hazard | hazard_total_drop_d2 | 1240 | 2.20961 | 2.26312 | 0.88995 | 0.960659 | 1.02431 | 1.17035 | 1.83222 | 7.72023 | 13.3701 |
| tossup_hazard | hazard_total_drop_d3 | 1240 | 2.24543 | 2.30011 | 0.851548 | 0.966704 | 1.02834 | 1.19189 | 1.90288 | 7.47208 | 14.9288 |
| tossup_hazard | hazard_drop_share_1_d1 | 1240 | 0.237216 | 0.0794341 | 0.0421043 | 0.0824682 | 0.177452 | 0.270516 | 0.294222 | 0.316839 | 0.534161 |
| tossup_hazard | hazard_drop_share_2_d1 | 1240 | 0.343064 | 0.0720573 | 0.0607538 | 0.192998 | 0.335457 | 0.351366 | 0.365389 | 0.442196 | 0.716056 |
| tossup_hazard | hazard_drop_share_3_d1 | 1240 | 0.41972 | 0.126264 | 0.1344 | 0.309093 | 0.348752 | 0.369733 | 0.441395 | 0.713025 | 0.895106 |
| tossup_hazard | hazard_drop_share_1_d2 | 1240 | 0.252559 | 0.0702943 | 0.0300938 | 0.0873115 | 0.232628 | 0.279622 | 0.296454 | 0.314859 | 0.59372 |
| tossup_hazard | hazard_drop_share_2_d2 | 1240 | 0.348074 | 0.0625709 | 0.0671449 | 0.22346 | 0.340771 | 0.351585 | 0.363366 | 0.419872 | 0.694125 |
| tossup_hazard | hazard_drop_share_3_d2 | 1240 | 0.399367 | 0.107475 | 0.100908 | 0.318233 | 0.350097 | 0.365308 | 0.398312 | 0.680046 | 0.888787 |
| tossup_hazard | hazard_drop_share_1_d3 | 1240 | 0.250344 | 0.0698445 | 0.0360019 | 0.0912466 | 0.229723 | 0.275518 | 0.296355 | 0.314516 | 0.574367 |
| tossup_hazard | hazard_drop_share_2_d3 | 1240 | 0.349101 | 0.0622248 | 0.0929915 | 0.237445 | 0.3398 | 0.351612 | 0.364066 | 0.427473 | 0.704859 |
| tossup_hazard | hazard_drop_share_3_d3 | 1240 | 0.400555 | 0.105523 | 0.131411 | 0.319327 | 0.3497 | 0.367246 | 0.40159 | 0.670258 | 0.871007 |
| tossup_hazard | hazard_r_1 | 1240 | 0.379589 | 0.272004 | 0.0307838 | 0.0590882 | 0.132908 | 0.309546 | 0.601561 | 0.871707 | 0.935516 |
| tossup_hazard | hazard_r_2 | 1240 | 0.301601 | 0.215505 | 0.0243647 | 0.0529385 | 0.116006 | 0.238823 | 0.458101 | 0.710821 | 0.854882 |
| tossup_hazard | hazard_r_3 | 1240 | 0.31881 | 0.230618 | 0.0238774 | 0.0476632 | 0.13482 | 0.258167 | 0.46463 | 0.779364 | 0.939882 |
