# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perceived-difficulty/three-slice/fold_2/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perceived-difficulty/three-slice/fold_2`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 317570 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.595159 |
| log_loss | 0.708387 |
| ece | 0.256768 |
| brier | 0.253321 |
| accuracy | 0.583234 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.180944 |
| probability_std | 0.166151 |
| probability_p10 | 0.264328 |
| probability_p50 | 0.527078 |
| probability_p90 | 0.710262 |
| mean_predictive_variance | 0.222339 |
| integrated_brier_score | 0.0955413 |
| joint_tossup_event_log_loss | 6.80208 |
| buzz_position_mae | 0.139455 |
| buzz_position_median_absolute_error | 0.116647 |
| buzz_position_bias | -0.00182625 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.380145 |
| first_buzzer_mean_reciprocal_rank | 0.58744 |
| first_buzzer_log_loss | 1.61441 |
| first_buzzer_events | 9257 |
| neg_auroc | 0.595159 |
| neg_average_precision | 0.307066 |
| neg_precision | 0.293668 |
| neg_recall | 0.546038 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.137558 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0518724 |
| no_buzz_calibration_error | 0.0387594 |
| no_buzz_brier | 0.0194886 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.595159 | 0.708387 | 0.256768 | 0.253321 | 0.583234 | 0.764178 | -0.180944 | 0.166151 | 0.264328 | 0.527078 | 0.710262 | 0.222339 |
| tossup_correctness | tier | fall | 2798 | 0.609506 | 0.7435 | 0.306366 | 0.268895 | 0.541816 | 0.785204 | -0.243388 | 0.172169 | 0.231579 | 0.495076 | 0.69465 | 0.21991 |
| tossup_correctness | tier | nationals | 1545 | 0.564408 | 0.682427 | 0.189822 | 0.243719 | 0.594175 | 0.721036 | -0.126861 | 0.143071 | 0.329431 | 0.548009 | 0.706896 | 0.228557 |
| tossup_correctness | tier | regionals | 2039 | 0.608431 | 0.708483 | 0.251754 | 0.25154 | 0.604218 | 0.762138 | -0.157921 | 0.175121 | 0.252497 | 0.536296 | 0.720221 | 0.219225 |
| tossup_correctness | tier | winter | 2875 | 0.603431 | 0.688098 | 0.24803 | 0.244588 | 0.602783 | 0.768348 | -0.165565 | 0.161299 | 0.284065 | 0.539236 | 0.714572 | 0.22357 |
| tossup_correctness | category | Current Events | 129 | 0.567063 | 0.744163 | 0.203456 | 0.270392 | 0.565891 | 0.666667 | -0.100775 | 0.176011 | 0.203442 | 0.508285 | 0.685484 | 0.218128 |
| tossup_correctness | category | Fine Arts | 1074 | 0.574395 | 0.730068 | 0.2776 | 0.262831 | 0.565177 | 0.776536 | -0.211359 | 0.170556 | 0.25798 | 0.521729 | 0.713557 | 0.220911 |
| tossup_correctness | category | Geography | 180 | 0.536885 | 0.743459 | 0.179586 | 0.26999 | 0.516667 | 0.616667 | -0.1 | 0.154497 | 0.240089 | 0.488753 | 0.655143 | 0.225472 |
| tossup_correctness | category | History | 1454 | 0.586614 | 0.708671 | 0.257886 | 0.25509 | 0.556396 | 0.757909 | -0.201513 | 0.154319 | 0.28027 | 0.51186 | 0.687784 | 0.226186 |
| tossup_correctness | category | Literature | 1435 | 0.589082 | 0.68354 | 0.28032 | 0.242404 | 0.611847 | 0.810453 | -0.198606 | 0.162711 | 0.281326 | 0.554662 | 0.724935 | 0.222617 |
| tossup_correctness | category | Mythology | 324 | 0.59022 | 0.710726 | 0.284044 | 0.25388 | 0.574074 | 0.79321 | -0.219136 | 0.161226 | 0.273122 | 0.536767 | 0.699634 | 0.223922 |
| tossup_correctness | category | Other Academic | 71 | 0.528322 | 0.689959 | 0.229688 | 0.247735 | 0.619718 | 0.760563 | -0.140845 | 0.153124 | 0.333571 | 0.545 | 0.702439 | 0.225404 |
| tossup_correctness | category | Philosophy | 310 | 0.616984 | 0.664451 | 0.238113 | 0.23551 | 0.583871 | 0.76129 | -0.177419 | 0.154396 | 0.321258 | 0.534361 | 0.712056 | 0.225625 |
| tossup_correctness | category | Popular Culture | 108 | 0.474826 | 0.939309 | 0.474025 | 0.352515 | 0.37963 | 0.888889 | -0.509259 | 0.161942 | 0.206725 | 0.401495 | 0.629151 | 0.216527 |
| tossup_correctness | category | Religion | 361 | 0.58887 | 0.711551 | 0.252537 | 0.256856 | 0.556787 | 0.742382 | -0.185596 | 0.153772 | 0.274057 | 0.509602 | 0.683987 | 0.226328 |
| tossup_correctness | category | Science | 1445 | 0.604761 | 0.709719 | 0.241048 | 0.253464 | 0.594464 | 0.746021 | -0.151557 | 0.169562 | 0.248411 | 0.526489 | 0.709367 | 0.221224 |
| tossup_correctness | category | Social Science | 327 | 0.630527 | 0.668637 | 0.207585 | 0.237576 | 0.59633 | 0.718654 | -0.122324 | 0.157211 | 0.269281 | 0.524747 | 0.711195 | 0.225153 |
| tossup_correctness | category | Unknown | 2039 | 0.608431 | 0.708483 | 0.251754 | 0.25154 | 0.604218 | 0.762138 | -0.157921 | 0.175121 | 0.252497 | 0.536296 | 0.720221 | 0.219225 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.650344 | 0.816974 | 0.335928 | 0.299148 | 0.469945 | 0.743169 | -0.273224 | 0.162124 | 0.156626 | 0.420624 | 0.595417 | 0.215112 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.622626 | 0.753207 | 0.280705 | 0.273668 | 0.508901 | 0.728796 | -0.219895 | 0.160861 | 0.221206 | 0.461679 | 0.649276 | 0.221429 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.618391 | 0.729913 | 0.270643 | 0.261806 | 0.568111 | 0.752568 | -0.184457 | 0.166759 | 0.234822 | 0.501606 | 0.688124 | 0.221865 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.589486 | 0.706605 | 0.274473 | 0.25267 | 0.588174 | 0.786087 | -0.197913 | 0.16247 | 0.275724 | 0.533298 | 0.710738 | 0.223468 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.570262 | 0.673198 | 0.217062 | 0.238365 | 0.6203 | 0.764393 | -0.144093 | 0.159433 | 0.321343 | 0.570547 | 0.737803 | 0.222341 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1197 | 0.199568 | 0.921635 | -2.21258 | -1.07782 | -0.511705 | 0.078906 | 0.830733 | 1.80929 | 2.98274 |
| player | theta_2 | 1197 | 0.204529 | 0.878683 | -2.0675 | -1.09271 | -0.39893 | 0.0637647 | 0.747988 | 1.86131 | 3.33631 |
| player | theta_3 | 1197 | 0.636721 | 1.16227 | -2.0612 | -1.21172 | -0.26048 | 0.669058 | 1.52393 | 2.49237 | 3.30975 |
| player | theta_norm | 1197 | 1.68009 | 0.796724 | 0.0960455 | 0.516903 | 1.06506 | 1.59755 | 2.26991 | 3.06401 | 4.10483 |
| tossup | start_difficulty_d1 | 1240 | 1.54592 | 0.381833 | -0.65186 | 0.812072 | 1.37442 | 1.60813 | 1.79244 | 2.02525 | 2.54262 |
| tossup | start_difficulty_d2 | 1240 | 1.45314 | 0.454437 | -0.486447 | 0.596402 | 1.21835 | 1.49394 | 1.762 | 2.10703 | 2.62163 |
| tossup | start_difficulty_d3 | 1240 | 1.72414 | 0.41492 | -0.250413 | 0.942382 | 1.50804 | 1.78005 | 1.98618 | 2.30484 | 3.01937 |
| tossup | end_difficulty_d1 | 1240 | 0.316711 | 0.473777 | -1.89615 | -0.551449 | 0.0710082 | 0.380411 | 0.635856 | 0.96035 | 1.59397 |
| tossup | end_difficulty_d2 | 1240 | 0.281209 | 0.562166 | -2.25208 | -0.791359 | -0.0101598 | 0.325494 | 0.637967 | 1.11408 | 1.86639 |
| tossup | end_difficulty_d3 | 1240 | 0.652125 | 0.505715 | -1.57114 | -0.216617 | 0.374759 | 0.68355 | 0.955268 | 1.45588 | 2.40528 |
| tossup | total_drop_d1 | 1240 | 1.22921 | 0.40155 | 0.485661 | 0.730098 | 0.916094 | 1.17486 | 1.47055 | 1.92585 | 3.57631 |
| tossup | total_drop_d2 | 1240 | 1.17193 | 0.44148 | 0.503551 | 0.693313 | 0.857647 | 1.03495 | 1.38567 | 2.03266 | 3.52319 |
| tossup | total_drop_d3 | 1240 | 1.07202 | 0.378574 | 0.450988 | 0.664494 | 0.78921 | 0.943685 | 1.30197 | 1.78799 | 2.92164 |
| tossup | drop_share_1_d1 | 1240 | 0.188976 | 0.0648164 | 0.0457103 | 0.0989437 | 0.136121 | 0.178077 | 0.239009 | 0.298846 | 0.465587 |
| tossup | drop_share_2_d1 | 1240 | 0.265782 | 0.0737039 | 0.0699435 | 0.135647 | 0.209724 | 0.276177 | 0.32487 | 0.365918 | 0.546331 |
| tossup | drop_share_3_d1 | 1240 | 0.545242 | 0.129934 | 0.142963 | 0.361179 | 0.432394 | 0.543792 | 0.647556 | 0.761064 | 0.884346 |
| tossup | drop_share_1_d2 | 1240 | 0.207843 | 0.0644133 | 0.0541836 | 0.101618 | 0.156804 | 0.212516 | 0.261099 | 0.299248 | 0.421358 |
| tossup | drop_share_2_d2 | 1240 | 0.281044 | 0.0682246 | 0.0748672 | 0.145391 | 0.237237 | 0.300958 | 0.331044 | 0.359616 | 0.498996 |
| tossup | drop_share_3_d2 | 1240 | 0.511113 | 0.124985 | 0.208231 | 0.362564 | 0.407276 | 0.479906 | 0.599876 | 0.749186 | 0.870949 |
| tossup | drop_share_1_d3 | 1240 | 0.201986 | 0.067904 | 0.0415373 | 0.0890563 | 0.147819 | 0.210009 | 0.257224 | 0.288432 | 0.463814 |
| tossup | drop_share_2_d3 | 1240 | 0.278226 | 0.0752454 | 0.0487724 | 0.131583 | 0.236124 | 0.300203 | 0.327394 | 0.360486 | 0.592151 |
| tossup | drop_share_3_d3 | 1240 | 0.519788 | 0.130242 | 0.205543 | 0.370257 | 0.417353 | 0.48109 | 0.606907 | 0.766848 | 0.901352 |
| tossup | r_1 | 1240 | 0.350269 | 0.203477 | 0.0213752 | 0.0514372 | 0.17954 | 0.343092 | 0.492116 | 0.712513 | 0.875011 |
| tossup | r_2 | 1240 | 0.252313 | 0.160761 | 0.0230389 | 0.0494812 | 0.12041 | 0.222622 | 0.354963 | 0.554385 | 0.782221 |
| tossup | r_3 | 1240 | 0.397418 | 0.223557 | 0.0361446 | 0.0758691 | 0.207876 | 0.386987 | 0.56857 | 0.778611 | 0.89605 |
| tossup | r_norm | 1240 | 0.675771 | 0.0689787 | 0.577648 | 0.584666 | 0.618526 | 0.665429 | 0.71971 | 0.805416 | 0.899261 |
