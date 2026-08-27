# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/player-neg-propensity/fold_2/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/player-neg-propensity/fold_2`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 283145 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.716674 |
| log_loss | 0.490778 |
| ece | 0.0132066 |
| brier | 0.159601 |
| accuracy | 0.775629 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | 0.0114508 |
| probability_std | 0.142124 |
| probability_p10 | 0.574596 |
| probability_p50 | 0.81342 |
| probability_p90 | 0.919344 |
| mean_predictive_variance | 0.153724 |
| integrated_brier_score | 0.102436 |
| joint_tossup_event_log_loss | 6.62835 |
| buzz_position_mae | 0.152216 |
| buzz_position_median_absolute_error | 0.135748 |
| buzz_position_bias | -0.0438917 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.353678 |
| first_buzzer_mean_reciprocal_rank | 0.567303 |
| first_buzzer_log_loss | 1.66646 |
| first_buzzer_events | 9257 |
| neg_auroc | 0.716674 |
| neg_average_precision | 0.448821 |
| neg_precision | 0.603113 |
| neg_recall | 0.142006 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.190438 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0139698 |
| no_buzz_calibration_error | 0.000856746 |
| no_buzz_brier | 0.0127075 |
| full_pmf_max_mass_error | 1.22125e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.716674 | 0.490778 | 0.0132066 | 0.159601 | 0.775629 | 0.764178 | 0.0114508 | 0.142124 | 0.574596 | 0.81342 | 0.919344 | 0.153724 |
| tossup_correctness | tier | fall | 2798 | 0.736434 | 0.458731 | 0.00773537 | 0.147076 | 0.795211 | 0.785204 | 0.0100071 | 0.143658 | 0.575752 | 0.821715 | 0.924049 | 0.150478 |
| tossup_correctness | tier | nationals | 1545 | 0.716183 | 0.534697 | 0.0421658 | 0.177929 | 0.740453 | 0.721036 | 0.0194175 | 0.14364 | 0.565587 | 0.793211 | 0.914874 | 0.16048 |
| tossup_correctness | tier | regionals | 2039 | 0.70358 | 0.499375 | 0.0115793 | 0.162701 | 0.771457 | 0.762138 | 0.00931829 | 0.135751 | 0.572461 | 0.804741 | 0.917172 | 0.156943 |
| tossup_correctness | tier | winter | 2875 | 0.704404 | 0.492266 | 0.017744 | 0.159742 | 0.778435 | 0.768348 | 0.010087 | 0.143711 | 0.581372 | 0.820386 | 0.918184 | 0.150968 |
| tossup_correctness | category | Current Events | 129 | 0.6947 | 0.606242 | 0.0961145 | 0.209036 | 0.674419 | 0.666667 | 0.00775194 | 0.15122 | 0.506316 | 0.785598 | 0.922888 | 0.162273 |
| tossup_correctness | category | Fine Arts | 1074 | 0.713697 | 0.474454 | 0.0296212 | 0.15245 | 0.791434 | 0.776536 | 0.0148976 | 0.152577 | 0.555532 | 0.807421 | 0.918939 | 0.156112 |
| tossup_correctness | category | Geography | 180 | 0.751404 | 0.569711 | 0.0920089 | 0.191932 | 0.738889 | 0.616667 | 0.122222 | 0.214923 | 0.310187 | 0.762896 | 0.902579 | 0.167967 |
| tossup_correctness | category | History | 1454 | 0.698665 | 0.507321 | 0.0205583 | 0.165555 | 0.768913 | 0.757909 | 0.0110041 | 0.142076 | 0.56351 | 0.810645 | 0.920169 | 0.155029 |
| tossup_correctness | category | Literature | 1435 | 0.732433 | 0.429827 | 0.0157053 | 0.134411 | 0.816028 | 0.810453 | 0.00557491 | 0.12506 | 0.636053 | 0.845407 | 0.929242 | 0.137322 |
| tossup_correctness | category | Mythology | 324 | 0.663511 | 0.483202 | 0.0371451 | 0.154256 | 0.79321 | 0.79321 | 0 | 0.119914 | 0.648435 | 0.835869 | 0.925817 | 0.140644 |
| tossup_correctness | category | Other Academic | 71 | 0.630719 | 0.540807 | 0.068656 | 0.178291 | 0.746479 | 0.760563 | -0.0140845 | 0.122293 | 0.623167 | 0.809913 | 0.89852 | 0.156723 |
| tossup_correctness | category | Philosophy | 310 | 0.742442 | 0.485528 | 0.0444289 | 0.16072 | 0.767742 | 0.76129 | 0.00645161 | 0.121454 | 0.604414 | 0.805411 | 0.922989 | 0.155335 |
| tossup_correctness | category | Popular Culture | 108 | 0.546875 | 0.366113 | 0.0720082 | 0.105754 | 0.87963 | 0.888889 | -0.00925926 | 0.0826721 | 0.747361 | 0.860648 | 0.91947 | 0.128882 |
| tossup_correctness | category | Religion | 361 | 0.689015 | 0.525112 | 0.053577 | 0.173802 | 0.756233 | 0.742382 | 0.0138504 | 0.138978 | 0.537469 | 0.761299 | 0.896785 | 0.174704 |
| tossup_correctness | category | Science | 1445 | 0.732037 | 0.505018 | 0.0368877 | 0.166871 | 0.757093 | 0.746021 | 0.0110727 | 0.139759 | 0.576154 | 0.81024 | 0.910404 | 0.156219 |
| tossup_correctness | category | Social Science | 327 | 0.717946 | 0.537653 | 0.0403352 | 0.180687 | 0.727829 | 0.718654 | 0.00917431 | 0.173279 | 0.480085 | 0.784998 | 0.909889 | 0.165552 |
| tossup_correctness | category | Unknown | 2039 | 0.70358 | 0.499375 | 0.0115793 | 0.162701 | 0.771457 | 0.762138 | 0.00931829 | 0.135751 | 0.572461 | 0.804741 | 0.917172 | 0.156943 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.666145 | 0.537097 | 0.0407332 | 0.17857 | 0.754098 | 0.743169 | 0.010929 | 0.148028 | 0.505447 | 0.770943 | 0.897006 | 0.172825 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.724465 | 0.522433 | 0.031617 | 0.172726 | 0.74555 | 0.728796 | 0.0167539 | 0.1473 | 0.547418 | 0.794018 | 0.911625 | 0.16191 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.731098 | 0.494506 | 0.0251256 | 0.161033 | 0.77356 | 0.752568 | 0.0209915 | 0.143067 | 0.574544 | 0.812955 | 0.917125 | 0.153838 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.711536 | 0.469678 | 0.0186253 | 0.15155 | 0.792348 | 0.786087 | 0.00626087 | 0.128943 | 0.617362 | 0.828108 | 0.922307 | 0.146801 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.708767 | 0.495305 | 0.0184135 | 0.160911 | 0.772047 | 0.764393 | 0.00765391 | 0.14909 | 0.552676 | 0.805232 | 0.920048 | 0.156496 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1197 | 2.65645 | 0.695892 | 0.815473 | 1.55551 | 2.1886 | 2.63068 | 3.10654 | 3.89687 | 4.60395 |
| player | theta_1 | 1197 | -1.23181 | 0.777463 | -3.68444 | -2.40043 | -1.74667 | -1.33742 | -0.762998 | 0.195614 | 1.48947 |
| player | theta_2 | 1197 | -1.08519 | 0.730771 | -3.1965 | -2.23802 | -1.57799 | -1.14355 | -0.622394 | 0.194109 | 1.58589 |
| player | theta_3 | 1197 | -0.871079 | 0.531518 | -2.78704 | -1.70937 | -1.23657 | -0.872163 | -0.52918 | 0.017183 | 1.78325 |
| player | theta_norm | 1197 | 2.14905 | 0.505322 | 0.837673 | 1.33211 | 1.80233 | 2.1398 | 2.48364 | 3.01755 | 3.78088 |
| tossup | start_difficulty_d1 | 1240 | -1.76916 | 0.551027 | -3.32073 | -2.55629 | -2.13806 | -1.82585 | -1.46881 | -0.755028 | 0.587946 |
| tossup | start_difficulty_d2 | 1240 | -1.75707 | 0.510418 | -3.30669 | -2.53334 | -2.10968 | -1.79266 | -1.43826 | -0.931128 | 0.619023 |
| tossup | start_difficulty_d3 | 1240 | -1.75444 | 0.496314 | -3.18145 | -2.53314 | -2.0995 | -1.79396 | -1.4414 | -0.923319 | 0.273479 |
| tossup | end_difficulty_d1 | 1240 | -2.76041 | 0.642406 | -4.4748 | -3.67527 | -3.18766 | -2.82628 | -2.39523 | -1.57266 | -0.0521833 |
| tossup | end_difficulty_d2 | 1240 | -2.74501 | 0.598104 | -4.68593 | -3.65476 | -3.16111 | -2.7885 | -2.35731 | -1.78201 | -0.162225 |
| tossup | end_difficulty_d3 | 1240 | -2.74189 | 0.580067 | -4.3725 | -3.66237 | -3.14699 | -2.77386 | -2.36924 | -1.77305 | -0.486766 |
| tossup | total_drop_d1 | 1240 | 0.991257 | 0.11191 | 0.640129 | 0.808449 | 0.914342 | 0.993008 | 1.06903 | 1.17549 | 1.51089 |
| tossup | total_drop_d2 | 1240 | 0.987947 | 0.105859 | 0.589828 | 0.819828 | 0.916277 | 0.98639 | 1.06215 | 1.15744 | 1.37924 |
| tossup | total_drop_d3 | 1240 | 0.987448 | 0.100438 | 0.720611 | 0.832993 | 0.913203 | 0.983515 | 1.05655 | 1.16182 | 1.30957 |
| tossup | drop_share_1_d1 | 1240 | 0.304098 | 0.0154923 | 0.216704 | 0.278546 | 0.295032 | 0.304628 | 0.314158 | 0.327333 | 0.369124 |
| tossup | drop_share_2_d1 | 1240 | 0.34719 | 0.0118531 | 0.308368 | 0.3285 | 0.339255 | 0.346865 | 0.355004 | 0.367358 | 0.40506 |
| tossup | drop_share_3_d1 | 1240 | 0.348712 | 0.016203 | 0.297898 | 0.324368 | 0.337681 | 0.347317 | 0.359213 | 0.377213 | 0.412437 |
| tossup | drop_share_1_d2 | 1240 | 0.304149 | 0.0143519 | 0.244132 | 0.279931 | 0.294793 | 0.304569 | 0.313505 | 0.327094 | 0.351056 |
| tossup | drop_share_2_d2 | 1240 | 0.347 | 0.0112903 | 0.311656 | 0.32908 | 0.339216 | 0.347472 | 0.354323 | 0.36557 | 0.381527 |
| tossup | drop_share_3_d2 | 1240 | 0.348851 | 0.0151393 | 0.304 | 0.325389 | 0.338324 | 0.348566 | 0.357707 | 0.37487 | 0.413223 |
| tossup | drop_share_1_d3 | 1240 | 0.304003 | 0.0140305 | 0.237878 | 0.282248 | 0.295124 | 0.304406 | 0.312892 | 0.326804 | 0.35523 |
| tossup | drop_share_2_d3 | 1240 | 0.347176 | 0.0112549 | 0.3072 | 0.329092 | 0.339625 | 0.347252 | 0.354743 | 0.365385 | 0.388629 |
| tossup | drop_share_3_d3 | 1240 | 0.348821 | 0.0151446 | 0.309938 | 0.325383 | 0.338254 | 0.348233 | 0.358319 | 0.37391 | 0.416133 |
| tossup | r_1 | 1240 | 0.319348 | 0.144144 | 0.0561698 | 0.133524 | 0.211579 | 0.286367 | 0.408703 | 0.601042 | 0.795799 |
| tossup | r_2 | 1240 | 0.348039 | 0.124636 | 0.0823586 | 0.163043 | 0.258423 | 0.335149 | 0.420801 | 0.575052 | 0.795218 |
| tossup | r_3 | 1240 | 0.332613 | 0.0971756 | 0.0920191 | 0.177188 | 0.26841 | 0.332235 | 0.387286 | 0.503204 | 0.747067 |
| tossup | r_norm | 1240 | 0.614638 | 0.0410489 | 0.57741 | 0.578932 | 0.586564 | 0.601479 | 0.625819 | 0.706218 | 0.809274 |
| tossup_hazard | hazard_start_difficulty_d1 | 1240 | 4.52129 | 0.516444 | 1.91028 | 3.72521 | 4.22371 | 4.48058 | 4.79717 | 5.45463 | 6.5202 |
| tossup_hazard | hazard_start_difficulty_d2 | 1240 | 4.49879 | 0.420385 | 2.24119 | 3.83016 | 4.26683 | 4.4804 | 4.72509 | 5.23681 | 6.58408 |
| tossup_hazard | hazard_start_difficulty_d3 | 1240 | 4.46541 | 0.377689 | 2.7164 | 3.87498 | 4.27366 | 4.45807 | 4.65 | 5.0442 | 6.33645 |
| tossup_hazard | hazard_end_difficulty_d1 | 1240 | 1.54412 | 2.33467 | -9.14924 | -3.32152 | 0.108278 | 2.65647 | 3.25385 | 3.63822 | 4.36386 |
| tossup_hazard | hazard_end_difficulty_d2 | 1240 | 2.2473 | 2.11798 | -11.8271 | -2.4549 | 2.1488 | 3.12371 | 3.41439 | 3.77327 | 4.43713 |
| tossup_hazard | hazard_end_difficulty_d3 | 1240 | 2.61224 | 1.75749 | -10.6858 | -1.89875 | 2.71577 | 3.21953 | 3.47531 | 3.75005 | 4.28665 |
| tossup_hazard | hazard_total_drop_d1 | 1240 | 2.97717 | 2.54196 | 0.765132 | 0.987681 | 1.08583 | 1.52552 | 4.62401 | 8.06051 | 14.1457 |
| tossup_hazard | hazard_total_drop_d2 | 1240 | 2.2515 | 2.21717 | 0.887869 | 0.96869 | 1.02873 | 1.22442 | 2.14271 | 7.3022 | 16.8814 |
| tossup_hazard | hazard_total_drop_d3 | 1240 | 1.85317 | 1.88345 | 0.903185 | 0.961967 | 1.01686 | 1.14034 | 1.48675 | 6.64082 | 15.3248 |
| tossup_hazard | hazard_drop_share_1_d1 | 1240 | 0.229997 | 0.0846794 | 0.0462656 | 0.0782933 | 0.15718 | 0.263256 | 0.292866 | 0.318376 | 0.611506 |
| tossup_hazard | hazard_drop_share_2_d1 | 1240 | 0.343784 | 0.0810911 | 0.0650989 | 0.172664 | 0.333925 | 0.351214 | 0.368347 | 0.471904 | 0.720267 |
| tossup_hazard | hazard_drop_share_3_d1 | 1240 | 0.426218 | 0.136487 | 0.0611645 | 0.297801 | 0.349466 | 0.372018 | 0.459564 | 0.73822 | 0.888134 |
| tossup_hazard | hazard_drop_share_1_d2 | 1240 | 0.248556 | 0.0690264 | 0.0292017 | 0.0939253 | 0.218173 | 0.274145 | 0.294356 | 0.3142 | 0.524717 |
| tossup_hazard | hazard_drop_share_2_d2 | 1240 | 0.347434 | 0.0594478 | 0.0764034 | 0.226647 | 0.339912 | 0.351238 | 0.364345 | 0.414407 | 0.685107 |
| tossup_hazard | hazard_drop_share_3_d2 | 1240 | 0.404009 | 0.105639 | 0.109151 | 0.322098 | 0.350501 | 0.369612 | 0.410176 | 0.651355 | 0.878229 |
| tossup_hazard | hazard_drop_share_1_d3 | 1240 | 0.261272 | 0.0596577 | 0.0421781 | 0.108316 | 0.251762 | 0.281356 | 0.296593 | 0.314348 | 0.428424 |
| tossup_hazard | hazard_drop_share_2_d3 | 1240 | 0.350184 | 0.0498855 | 0.0669304 | 0.298439 | 0.341968 | 0.351861 | 0.36251 | 0.399325 | 0.672219 |
| tossup_hazard | hazard_drop_share_3_d3 | 1240 | 0.388544 | 0.0872209 | 0.167619 | 0.326353 | 0.350196 | 0.36522 | 0.389974 | 0.567842 | 0.887108 |
| tossup_hazard | hazard_r_1 | 1240 | 0.413511 | 0.277699 | 0.0241764 | 0.0688205 | 0.151941 | 0.352711 | 0.666319 | 0.867946 | 0.942048 |
| tossup_hazard | hazard_r_2 | 1240 | 0.32925 | 0.237265 | 0.0198387 | 0.0503938 | 0.123809 | 0.2589 | 0.51268 | 0.766185 | 0.911057 |
| tossup_hazard | hazard_r_3 | 1240 | 0.257238 | 0.18215 | 0.0294161 | 0.0620176 | 0.118346 | 0.197393 | 0.349986 | 0.658588 | 0.866897 |
