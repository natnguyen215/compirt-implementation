# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/incorrect-loss-weight/weight-2/fold_3/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/incorrect-loss-weight/weight-2/fold_3`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 293284 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.70801 |
| log_loss | 0.525086 |
| ece | 0.113832 |
| brier | 0.17392 |
| accuracy | 0.74989 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | -0.0201542 |
| probability_std | 0.1917 |
| probability_p10 | 0.379487 |
| probability_p50 | 0.689825 |
| probability_p90 | 0.876929 |
| mean_predictive_variance | 0.188849 |
| integrated_brier_score | 0.101352 |
| joint_tossup_event_log_loss | 6.62329 |
| buzz_position_mae | 0.152056 |
| buzz_position_median_absolute_error | 0.136026 |
| buzz_position_bias | -0.0490917 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |
| first_buzzer_top1_accuracy | 0.351652 |
| first_buzzer_mean_reciprocal_rank | 0.567483 |
| first_buzzer_log_loss | 1.67123 |
| first_buzzer_events | 9080 |
| neg_auroc | 0.70801 |
| neg_average_precision | 0.447568 |
| neg_precision | 0.452566 |
| neg_recall | 0.418103 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.183493 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0150874 |
| no_buzz_calibration_error | -9.69646e-05 |
| no_buzz_brier | 0.0137037 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.70801 | 0.525086 | 0.113832 | 0.17392 | 0.74989 | 0.770044 | -0.0201542 | 0.1917 | 0.379487 | 0.689825 | 0.876929 | 0.188849 |
| tossup_correctness | tier | fall | 2817 | 0.700186 | 0.5177 | 0.110535 | 0.170423 | 0.758963 | 0.781683 | -0.0227192 | 0.191705 | 0.380032 | 0.711359 | 0.885865 | 0.183958 |
| tossup_correctness | tier | nationals | 1542 | 0.726157 | 0.543251 | 0.107556 | 0.182328 | 0.726329 | 0.73476 | -0.00843061 | 0.197074 | 0.338403 | 0.661972 | 0.864445 | 0.194869 |
| tossup_correctness | tier | regionals | 1934 | 0.711317 | 0.531043 | 0.105663 | 0.176604 | 0.747673 | 0.75698 | -0.00930714 | 0.188521 | 0.380272 | 0.680262 | 0.872763 | 0.191563 |
| tossup_correctness | tier | winter | 2787 | 0.697939 | 0.518368 | 0.12655 | 0.170942 | 0.755292 | 0.786868 | -0.0315752 | 0.188993 | 0.393534 | 0.695179 | 0.87869 | 0.18858 |
| tossup_correctness | category | Current Events | 125 | 0.744472 | 0.542137 | 0.102432 | 0.184188 | 0.704 | 0.704 | 0 | 0.201553 | 0.339214 | 0.632765 | 0.878239 | 0.19614 |
| tossup_correctness | category | Fine Arts | 1072 | 0.720004 | 0.516664 | 0.117021 | 0.170697 | 0.754664 | 0.770522 | -0.0158582 | 0.195898 | 0.363854 | 0.696582 | 0.875996 | 0.18765 |
| tossup_correctness | category | Geography | 185 | 0.774126 | 0.545798 | 0.151033 | 0.183126 | 0.745946 | 0.702703 | 0.0432432 | 0.232585 | 0.236495 | 0.604851 | 0.840543 | 0.191739 |
| tossup_correctness | category | History | 1443 | 0.732106 | 0.525419 | 0.122841 | 0.175206 | 0.735967 | 0.765073 | -0.029106 | 0.197941 | 0.351567 | 0.675708 | 0.874526 | 0.190484 |
| tossup_correctness | category | Literature | 1411 | 0.657496 | 0.497772 | 0.10556 | 0.161136 | 0.781715 | 0.81219 | -0.0304748 | 0.168214 | 0.460489 | 0.741897 | 0.890418 | 0.179008 |
| tossup_correctness | category | Mythology | 320 | 0.66267 | 0.518203 | 0.111511 | 0.167833 | 0.778125 | 0.79375 | -0.015625 | 0.170788 | 0.442606 | 0.715975 | 0.888874 | 0.184214 |
| tossup_correctness | category | Other Academic | 64 | 0.643229 | 0.585434 | 0.103576 | 0.198379 | 0.6875 | 0.75 | -0.0625 | 0.160247 | 0.460889 | 0.690511 | 0.849251 | 0.195346 |
| tossup_correctness | category | Philosophy | 312 | 0.664645 | 0.509321 | 0.128516 | 0.167584 | 0.769231 | 0.801282 | -0.0320513 | 0.162163 | 0.454388 | 0.690226 | 0.881238 | 0.193136 |
| tossup_correctness | category | Popular Culture | 104 | 0.607955 | 0.459731 | 0.136556 | 0.140027 | 0.846154 | 0.846154 | 0 | 0.117997 | 0.579946 | 0.766476 | 0.878124 | 0.174248 |
| tossup_correctness | category | Religion | 358 | 0.712127 | 0.568131 | 0.114364 | 0.19264 | 0.709497 | 0.726257 | -0.0167598 | 0.186245 | 0.350293 | 0.621292 | 0.842984 | 0.202793 |
| tossup_correctness | category | Science | 1431 | 0.6971 | 0.538658 | 0.122968 | 0.179971 | 0.733753 | 0.765199 | -0.0314465 | 0.197143 | 0.355677 | 0.674045 | 0.87295 | 0.190772 |
| tossup_correctness | category | Social Science | 321 | 0.728595 | 0.540141 | 0.122041 | 0.180108 | 0.741433 | 0.744548 | -0.00311526 | 0.217519 | 0.29502 | 0.661842 | 0.874969 | 0.187677 |
| tossup_correctness | category | Unknown | 1934 | 0.711317 | 0.531043 | 0.105663 | 0.176604 | 0.747673 | 0.75698 | -0.00930714 | 0.188521 | 0.380272 | 0.680262 | 0.872763 | 0.191563 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.747427 | 0.572242 | 0.117167 | 0.193173 | 0.713542 | 0.697917 | 0.015625 | 0.192258 | 0.299977 | 0.601252 | 0.812204 | 0.205538 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.745405 | 0.525479 | 0.10176 | 0.17445 | 0.745782 | 0.733408 | 0.0123735 | 0.195341 | 0.341413 | 0.664656 | 0.862705 | 0.194332 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.682567 | 0.542832 | 0.0959564 | 0.180706 | 0.742081 | 0.759276 | -0.0171946 | 0.19071 | 0.388209 | 0.698165 | 0.885538 | 0.186758 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.691031 | 0.510863 | 0.11083 | 0.168144 | 0.755315 | 0.789125 | -0.0338097 | 0.178085 | 0.418603 | 0.711895 | 0.880315 | 0.186434 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.7275 | 0.522411 | 0.134988 | 0.173032 | 0.75411 | 0.775342 | -0.0212329 | 0.200656 | 0.34769 | 0.676172 | 0.871894 | 0.190038 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1133 | 2.66046 | 0.777416 | 0.546122 | 1.3978 | 2.10329 | 2.66209 | 3.17465 | 4.00791 | 4.64345 |
| player | theta_1 | 1133 | -1.24187 | 0.929982 | -4.06554 | -2.65252 | -1.82671 | -1.3175 | -0.709376 | 0.466505 | 2.59853 |
| player | theta_2 | 1133 | -1.00374 | 0.683677 | -3.36533 | -2.12837 | -1.42023 | -1.01418 | -0.558186 | 0.136008 | 1.34607 |
| player | theta_3 | 1133 | -1.13359 | 0.811878 | -3.3679 | -2.42755 | -1.67266 | -1.18351 | -0.648332 | 0.302302 | 1.68633 |
| player | theta_norm | 1133 | 2.30015 | 0.73088 | 0.197029 | 1.14692 | 1.79923 | 2.28729 | 2.75986 | 3.55283 | 4.6381 |
| tossup | start_difficulty_d1 | 1240 | -1.12514 | 0.635357 | -3.49823 | -2.06459 | -1.5137 | -1.17672 | -0.772087 | -0.0326059 | 2.07911 |
| tossup | start_difficulty_d2 | 1240 | -1.10581 | 0.576703 | -3.65929 | -2.01605 | -1.48594 | -1.12191 | -0.749195 | -0.124539 | 0.925358 |
| tossup | start_difficulty_d3 | 1240 | -1.10655 | 0.587947 | -3.43595 | -2.0523 | -1.49096 | -1.1352 | -0.736927 | -0.0985701 | 1.03563 |
| tossup | end_difficulty_d1 | 1240 | -2.11946 | 0.747558 | -5.4003 | -3.22046 | -2.59113 | -2.18243 | -1.68938 | -0.83167 | 1.40398 |
| tossup | end_difficulty_d2 | 1240 | -2.09291 | 0.679188 | -5.19919 | -3.19849 | -2.51815 | -2.10542 | -1.67366 | -0.924152 | 0.28074 |
| tossup | end_difficulty_d3 | 1240 | -2.09225 | 0.68661 | -4.87596 | -3.22539 | -2.54003 | -2.10507 | -1.64544 | -0.945814 | 0.29191 |
| tossup | total_drop_d1 | 1240 | 0.994319 | 0.15059 | 0.58141 | 0.758877 | 0.898147 | 0.991725 | 1.07189 | 1.22348 | 1.90207 |
| tossup | total_drop_d2 | 1240 | 0.987095 | 0.129502 | 0.644619 | 0.789332 | 0.904659 | 0.981631 | 1.06008 | 1.20898 | 1.56812 |
| tossup | total_drop_d3 | 1240 | 0.985705 | 0.129722 | 0.574353 | 0.791877 | 0.897457 | 0.983171 | 1.06049 | 1.21075 | 1.66233 |
| tossup | drop_share_1_d1 | 1240 | 0.30259 | 0.0194318 | 0.200514 | 0.271693 | 0.291759 | 0.303725 | 0.314609 | 0.330747 | 0.39739 |
| tossup | drop_share_2_d1 | 1240 | 0.347285 | 0.012574 | 0.2998 | 0.326287 | 0.338995 | 0.347423 | 0.35564 | 0.36744 | 0.408129 |
| tossup | drop_share_3_d1 | 1240 | 0.350125 | 0.0205039 | 0.253373 | 0.31981 | 0.336992 | 0.349443 | 0.361941 | 0.383246 | 0.439896 |
| tossup | drop_share_1_d2 | 1240 | 0.302443 | 0.0166776 | 0.225771 | 0.274205 | 0.292756 | 0.302738 | 0.313259 | 0.328267 | 0.381118 |
| tossup | drop_share_2_d2 | 1240 | 0.346895 | 0.0121591 | 0.306909 | 0.327228 | 0.338802 | 0.346978 | 0.354795 | 0.366417 | 0.409559 |
| tossup | drop_share_3_d2 | 1240 | 0.350662 | 0.0182911 | 0.266234 | 0.321784 | 0.338934 | 0.350893 | 0.361354 | 0.380403 | 0.454259 |
| tossup | drop_share_1_d3 | 1240 | 0.302249 | 0.0182025 | 0.216531 | 0.272067 | 0.292822 | 0.302651 | 0.313576 | 0.329595 | 0.376752 |
| tossup | drop_share_2_d3 | 1240 | 0.347168 | 0.0120483 | 0.301904 | 0.327941 | 0.339444 | 0.346979 | 0.354535 | 0.366508 | 0.407106 |
| tossup | drop_share_3_d3 | 1240 | 0.350583 | 0.019176 | 0.293724 | 0.321069 | 0.3383 | 0.349969 | 0.360573 | 0.381204 | 0.478121 |
| tossup | r_1 | 1240 | 0.340079 | 0.195163 | 0.0460575 | 0.0935811 | 0.178472 | 0.293358 | 0.480106 | 0.704995 | 0.851103 |
| tossup | r_2 | 1240 | 0.325597 | 0.157683 | 0.0498355 | 0.116969 | 0.204498 | 0.304445 | 0.412615 | 0.634253 | 0.879792 |
| tossup | r_3 | 1240 | 0.334323 | 0.169512 | 0.0594707 | 0.116368 | 0.198907 | 0.305856 | 0.43822 | 0.67063 | 0.872254 |
| tossup | r_norm | 1240 | 0.648991 | 0.062175 | 0.577412 | 0.581444 | 0.599818 | 0.631643 | 0.679855 | 0.779331 | 0.883889 |
| tossup_hazard | hazard_start_difficulty_d1 | 1240 | 4.47304 | 0.499267 | 2.10626 | 3.75417 | 4.17969 | 4.42914 | 4.72459 | 5.41978 | 6.35108 |
| tossup_hazard | hazard_start_difficulty_d2 | 1240 | 4.44835 | 0.419367 | 2.19952 | 3.81135 | 4.21956 | 4.42906 | 4.65001 | 5.18333 | 6.5854 |
| tossup_hazard | hazard_start_difficulty_d3 | 1240 | 4.45531 | 0.443059 | 2.43487 | 3.74348 | 4.2075 | 4.43541 | 4.69852 | 5.20641 | 6.04496 |
| tossup_hazard | hazard_end_difficulty_d1 | 1240 | 1.69544 | 2.33971 | -11.7739 | -3.03298 | 0.523126 | 2.8161 | 3.28499 | 3.6098 | 4.4996 |
| tossup_hazard | hazard_end_difficulty_d2 | 1240 | 2.39731 | 1.92033 | -8.14499 | -2.04266 | 2.53276 | 3.13015 | 3.39727 | 3.71492 | 4.14734 |
| tossup_hazard | hazard_end_difficulty_d3 | 1240 | 2.15799 | 2.05183 | -9.17491 | -2.34014 | 1.91854 | 3.03211 | 3.36426 | 3.75135 | 4.23209 |
| tossup_hazard | hazard_total_drop_d1 | 1240 | 2.7776 | 2.50535 | 0.848771 | 0.984579 | 1.06287 | 1.33643 | 4.21549 | 7.99361 | 16.3924 |
| tossup_hazard | hazard_total_drop_d2 | 1240 | 2.05104 | 2.07894 | 0.894242 | 0.957878 | 1.02071 | 1.15197 | 1.64886 | 7.06726 | 13.5459 |
| tossup_hazard | hazard_total_drop_d3 | 1240 | 2.29732 | 2.19016 | 0.875258 | 0.96751 | 1.0301 | 1.22224 | 2.37851 | 7.29278 | 13.7307 |
| tossup_hazard | hazard_drop_share_1_d1 | 1240 | 0.235695 | 0.0811622 | 0.0321254 | 0.0799723 | 0.177939 | 0.270941 | 0.294535 | 0.316384 | 0.510932 |
| tossup_hazard | hazard_drop_share_2_d1 | 1240 | 0.341897 | 0.0756719 | 0.0605596 | 0.180483 | 0.334557 | 0.350975 | 0.364687 | 0.449002 | 0.716067 |
| tossup_hazard | hazard_drop_share_3_d1 | 1240 | 0.422408 | 0.131505 | 0.107546 | 0.304791 | 0.347955 | 0.36952 | 0.448555 | 0.72849 | 0.895891 |
| tossup_hazard | hazard_drop_share_1_d2 | 1240 | 0.255586 | 0.0670919 | 0.038507 | 0.0914107 | 0.240948 | 0.279759 | 0.296024 | 0.313875 | 0.549044 |
| tossup_hazard | hazard_drop_share_2_d2 | 1240 | 0.348669 | 0.0585566 | 0.0529448 | 0.247437 | 0.341046 | 0.351001 | 0.362683 | 0.409121 | 0.687621 |
| tossup_hazard | hazard_drop_share_3_d2 | 1240 | 0.395745 | 0.100775 | 0.198136 | 0.321205 | 0.349225 | 0.364471 | 0.394513 | 0.642655 | 0.908548 |
| tossup_hazard | hazard_drop_share_1_d3 | 1240 | 0.247962 | 0.0707845 | 0.0415131 | 0.0895076 | 0.22347 | 0.274651 | 0.295947 | 0.31517 | 0.540929 |
| tossup_hazard | hazard_drop_share_2_d3 | 1240 | 0.349386 | 0.0601268 | 0.0839975 | 0.234815 | 0.339133 | 0.35125 | 0.364982 | 0.426721 | 0.706514 |
| tossup_hazard | hazard_drop_share_3_d3 | 1240 | 0.402652 | 0.105335 | 0.0699176 | 0.317873 | 0.349449 | 0.367419 | 0.407044 | 0.665634 | 0.863167 |
| tossup_hazard | hazard_r_1 | 1240 | 0.384083 | 0.279843 | 0.0256618 | 0.0605067 | 0.134849 | 0.293138 | 0.609005 | 0.892294 | 0.953958 |
| tossup_hazard | hazard_r_2 | 1240 | 0.280839 | 0.202002 | 0.0284293 | 0.0568595 | 0.121351 | 0.21671 | 0.403809 | 0.700653 | 0.841091 |
| tossup_hazard | hazard_r_3 | 1240 | 0.335079 | 0.238263 | 0.0176128 | 0.0462377 | 0.135294 | 0.268869 | 0.519007 | 0.768755 | 0.930923 |
