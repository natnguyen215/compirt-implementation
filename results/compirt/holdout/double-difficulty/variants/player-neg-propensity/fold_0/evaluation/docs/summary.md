# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/player-neg-propensity/fold_0/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/player-neg-propensity/fold_0`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 283016 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.716044 |
| log_loss | 0.489612 |
| ece | 0.013727 |
| brier | 0.158877 |
| accuracy | 0.777945 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | 0.012695 |
| probability_std | 0.141948 |
| probability_p10 | 0.575835 |
| probability_p50 | 0.817341 |
| probability_p90 | 0.919423 |
| mean_predictive_variance | 0.152357 |
| integrated_brier_score | 0.101839 |
| joint_tossup_event_log_loss | 6.62695 |
| buzz_position_mae | 0.152336 |
| buzz_position_median_absolute_error | 0.135878 |
| buzz_position_bias | -0.0435555 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |
| first_buzzer_top1_accuracy | 0.344379 |
| first_buzzer_mean_reciprocal_rank | 0.561379 |
| first_buzzer_log_loss | 1.67439 |
| first_buzzer_events | 9295 |
| neg_auroc | 0.716044 |
| neg_average_precision | 0.452002 |
| neg_precision | 0.612595 |
| neg_recall | 0.147113 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.18796 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.0163264 |
| no_buzz_calibration_error | 0.00305676 |
| no_buzz_brier | 0.0129631 |
| full_pmf_max_mass_error | 1.55431e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.716044 | 0.489612 | 0.013727 | 0.158877 | 0.777945 | 0.76525 | 0.012695 | 0.141948 | 0.575835 | 0.817341 | 0.919423 | 0.152357 |
| tossup_correctness | tier | fall | 2933 | 0.715771 | 0.461503 | 0.00860498 | 0.147552 | 0.795772 | 0.791681 | 0.00409137 | 0.145554 | 0.569989 | 0.826042 | 0.927617 | 0.148234 |
| tossup_correctness | tier | nationals | 1584 | 0.709657 | 0.534056 | 0.0415272 | 0.17641 | 0.746843 | 0.724747 | 0.022096 | 0.147581 | 0.544703 | 0.809046 | 0.917211 | 0.157661 |
| tossup_correctness | tier | regionals | 1886 | 0.717228 | 0.511655 | 0.0255329 | 0.169302 | 0.757158 | 0.746023 | 0.0111347 | 0.133519 | 0.586976 | 0.799919 | 0.905851 | 0.159809 |
| tossup_correctness | tier | winter | 2892 | 0.714661 | 0.479401 | 0.0138395 | 0.153961 | 0.790456 | 0.773167 | 0.0172891 | 0.139589 | 0.598909 | 0.823774 | 0.919947 | 0.148775 |
| tossup_correctness | category | Current Events | 124 | 0.654873 | 0.53424 | 0.0798045 | 0.174207 | 0.774194 | 0.75 | 0.0241935 | 0.150864 | 0.529461 | 0.767412 | 0.927676 | 0.16402 |
| tossup_correctness | category | Fine Arts | 1103 | 0.700216 | 0.505648 | 0.0298562 | 0.164062 | 0.771532 | 0.759746 | 0.011786 | 0.146375 | 0.580139 | 0.825226 | 0.924242 | 0.149217 |
| tossup_correctness | category | Geography | 197 | 0.776923 | 0.51985 | 0.0657063 | 0.171289 | 0.741117 | 0.670051 | 0.071066 | 0.210989 | 0.411114 | 0.730882 | 0.907162 | 0.170663 |
| tossup_correctness | category | History | 1491 | 0.723811 | 0.461911 | 0.0171337 | 0.148111 | 0.794769 | 0.787391 | 0.0073776 | 0.134537 | 0.582948 | 0.813966 | 0.918137 | 0.154175 |
| tossup_correctness | category | Literature | 1472 | 0.728222 | 0.436458 | 0.0230966 | 0.136776 | 0.814538 | 0.804348 | 0.0101902 | 0.120518 | 0.650621 | 0.852832 | 0.93065 | 0.134622 |
| tossup_correctness | category | Mythology | 332 | 0.677897 | 0.451197 | 0.0149949 | 0.141351 | 0.816265 | 0.813253 | 0.00301205 | 0.118871 | 0.62633 | 0.832547 | 0.914308 | 0.143678 |
| tossup_correctness | category | Other Academic | 69 | 0.707014 | 0.504401 | 0.0739716 | 0.165108 | 0.782609 | 0.753623 | 0.0289855 | 0.114494 | 0.615759 | 0.782187 | 0.901122 | 0.166301 |
| tossup_correctness | category | Philosophy | 324 | 0.690288 | 0.464656 | 0.0168848 | 0.148682 | 0.802469 | 0.799383 | 0.00308642 | 0.122279 | 0.617119 | 0.818889 | 0.929423 | 0.149039 |
| tossup_correctness | category | Popular Culture | 102 | 0.483737 | 0.474702 | 0.0522305 | 0.145179 | 0.813725 | 0.833333 | -0.0196078 | 0.0876152 | 0.754379 | 0.866481 | 0.915828 | 0.125466 |
| tossup_correctness | category | Religion | 372 | 0.716786 | 0.54532 | 0.0573779 | 0.184601 | 0.725806 | 0.709677 | 0.016129 | 0.148763 | 0.528061 | 0.773617 | 0.904338 | 0.169525 |
| tossup_correctness | category | Science | 1487 | 0.691201 | 0.514441 | 0.0260927 | 0.168388 | 0.764627 | 0.752522 | 0.0121049 | 0.151672 | 0.5453 | 0.80865 | 0.920422 | 0.155254 |
| tossup_correctness | category | Social Science | 336 | 0.74661 | 0.526778 | 0.0696516 | 0.174455 | 0.747024 | 0.702381 | 0.0446429 | 0.17586 | 0.476767 | 0.796337 | 0.907258 | 0.160682 |
| tossup_correctness | category | Unknown | 1886 | 0.717228 | 0.511655 | 0.0255329 | 0.169302 | 0.757158 | 0.746023 | 0.0111347 | 0.133519 | 0.586976 | 0.799919 | 0.905851 | 0.159809 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.703316 | 0.512923 | 0.0636375 | 0.164286 | 0.781726 | 0.736041 | 0.0456853 | 0.154196 | 0.524374 | 0.766492 | 0.891121 | 0.172783 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.713432 | 0.522518 | 0.0343811 | 0.172921 | 0.746193 | 0.735025 | 0.0111675 | 0.147208 | 0.551578 | 0.800436 | 0.912053 | 0.159527 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.702525 | 0.494507 | 0.0200962 | 0.160685 | 0.775211 | 0.769436 | 0.00577521 | 0.139391 | 0.598569 | 0.820137 | 0.917749 | 0.151225 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.708129 | 0.473661 | 0.0117263 | 0.152156 | 0.792742 | 0.78402 | 0.00872296 | 0.131043 | 0.612158 | 0.828083 | 0.924455 | 0.146462 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.732662 | 0.488841 | 0.0141873 | 0.158975 | 0.776035 | 0.756008 | 0.0200267 | 0.149163 | 0.552844 | 0.813986 | 0.918538 | 0.155148 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1186 | 2.672 | 0.700099 | 0.877681 | 1.53697 | 2.2014 | 2.64975 | 3.12748 | 3.93083 | 4.54703 |
| player | theta_1 | 1186 | -1.2498 | 0.760084 | -3.69214 | -2.41156 | -1.74621 | -1.33788 | -0.766969 | 0.154156 | 1.66813 |
| player | theta_2 | 1186 | -1.00151 | 0.636737 | -2.95173 | -2.00757 | -1.4477 | -1.03567 | -0.603304 | 0.0887977 | 1.07614 |
| player | theta_3 | 1186 | -0.968748 | 0.655504 | -2.67238 | -1.93879 | -1.40169 | -1.01534 | -0.596655 | 0.203895 | 2.2665 |
| player | theta_norm | 1186 | 2.15857 | 0.505914 | 0.736037 | 1.35561 | 1.81507 | 2.13612 | 2.50146 | 3.02356 | 3.76702 |
| tossup | start_difficulty_d1 | 1240 | -1.76457 | 0.563645 | -3.75458 | -2.53771 | -2.14987 | -1.82608 | -1.45192 | -0.747731 | 1.46621 |
| tossup | start_difficulty_d2 | 1240 | -1.75017 | 0.508593 | -3.63506 | -2.51779 | -2.10981 | -1.80735 | -1.42643 | -0.869573 | 0.298262 |
| tossup | start_difficulty_d3 | 1240 | -1.74831 | 0.510424 | -3.2133 | -2.51984 | -2.10151 | -1.79903 | -1.41503 | -0.847396 | 0.347972 |
| tossup | end_difficulty_d1 | 1240 | -2.75537 | 0.654755 | -4.99963 | -3.65372 | -3.20692 | -2.82964 | -2.38582 | -1.57094 | 0.733877 |
| tossup | end_difficulty_d2 | 1240 | -2.73863 | 0.594395 | -4.83317 | -3.63631 | -3.15284 | -2.79254 | -2.35607 | -1.72308 | -0.505077 |
| tossup | end_difficulty_d3 | 1240 | -2.73609 | 0.598452 | -4.44148 | -3.66069 | -3.1422 | -2.77309 | -2.33844 | -1.70374 | -0.328253 |
| tossup | total_drop_d1 | 1240 | 0.990802 | 0.112128 | 0.645081 | 0.798184 | 0.921053 | 0.99248 | 1.0659 | 1.16221 | 1.50268 |
| tossup | total_drop_d2 | 1240 | 0.988464 | 0.103649 | 0.633691 | 0.820651 | 0.916289 | 0.991009 | 1.05875 | 1.15901 | 1.39753 |
| tossup | total_drop_d3 | 1240 | 0.987781 | 0.104586 | 0.676225 | 0.815902 | 0.914532 | 0.985751 | 1.0587 | 1.16022 | 1.36069 |
| tossup | drop_share_1_d1 | 1240 | 0.304131 | 0.0155272 | 0.199318 | 0.278231 | 0.294902 | 0.304427 | 0.314484 | 0.328902 | 0.357811 |
| tossup | drop_share_2_d1 | 1240 | 0.347119 | 0.011802 | 0.308668 | 0.328576 | 0.339417 | 0.346985 | 0.354828 | 0.366975 | 0.4209 |
| tossup | drop_share_3_d1 | 1240 | 0.348751 | 0.0162671 | 0.304594 | 0.324206 | 0.337437 | 0.348366 | 0.35926 | 0.376015 | 0.439374 |
| tossup | drop_share_1_d2 | 1240 | 0.304102 | 0.0144917 | 0.237099 | 0.279479 | 0.294598 | 0.304808 | 0.313968 | 0.327359 | 0.34591 |
| tossup | drop_share_2_d2 | 1240 | 0.347037 | 0.0113199 | 0.30948 | 0.3288 | 0.339283 | 0.347519 | 0.354543 | 0.365371 | 0.380739 |
| tossup | drop_share_3_d2 | 1240 | 0.348861 | 0.0154093 | 0.301724 | 0.325369 | 0.338258 | 0.348342 | 0.358625 | 0.375636 | 0.411602 |
| tossup | drop_share_1_d3 | 1240 | 0.303979 | 0.0141425 | 0.246572 | 0.280434 | 0.294808 | 0.304003 | 0.313273 | 0.326467 | 0.351152 |
| tossup | drop_share_2_d3 | 1240 | 0.347255 | 0.0112983 | 0.303938 | 0.328575 | 0.339831 | 0.347259 | 0.354925 | 0.365495 | 0.388167 |
| tossup | drop_share_3_d3 | 1240 | 0.348766 | 0.0152904 | 0.307324 | 0.324895 | 0.338041 | 0.347663 | 0.358471 | 0.373923 | 0.418377 |
| tossup | r_1 | 1240 | 0.317644 | 0.145768 | 0.0636402 | 0.137693 | 0.206995 | 0.286398 | 0.398456 | 0.614258 | 0.842101 |
| tossup | r_2 | 1240 | 0.339062 | 0.104282 | 0.0756687 | 0.172373 | 0.268176 | 0.337124 | 0.399586 | 0.51538 | 0.730241 |
| tossup | r_3 | 1240 | 0.343294 | 0.11226 | 0.0822301 | 0.1688 | 0.269385 | 0.338705 | 0.409604 | 0.540183 | 0.80463 |
| tossup | r_norm | 1240 | 0.613842 | 0.0400072 | 0.577357 | 0.578739 | 0.586356 | 0.601168 | 0.626254 | 0.696939 | 0.849483 |
| tossup_hazard | hazard_start_difficulty_d1 | 1240 | 4.51993 | 0.511577 | 1.90052 | 3.74328 | 4.23561 | 4.48237 | 4.79545 | 5.4304 | 6.63 |
| tossup_hazard | hazard_start_difficulty_d2 | 1240 | 4.48977 | 0.403711 | 2.37556 | 3.82652 | 4.26618 | 4.49502 | 4.70326 | 5.14869 | 6.55591 |
| tossup_hazard | hazard_start_difficulty_d3 | 1240 | 4.49223 | 0.402772 | 2.85534 | 3.86226 | 4.26675 | 4.48576 | 4.68504 | 5.15333 | 6.5926 |
| tossup_hazard | hazard_end_difficulty_d1 | 1240 | 1.56929 | 2.2939 | -9.48377 | -2.80904 | 0.0977986 | 2.63291 | 3.26343 | 3.66393 | 4.28407 |
| tossup_hazard | hazard_end_difficulty_d2 | 1240 | 2.40472 | 2.0465 | -9.62955 | -2.70015 | 2.5725 | 3.19969 | 3.45883 | 3.75235 | 4.17353 |
| tossup_hazard | hazard_end_difficulty_d3 | 1240 | 2.47517 | 1.91848 | -11.6386 | -2.36483 | 2.55481 | 3.1913 | 3.44563 | 3.71739 | 4.23905 |
| tossup_hazard | hazard_total_drop_d1 | 1240 | 2.95064 | 2.47138 | 0.814107 | 0.985942 | 1.08605 | 1.55508 | 4.66879 | 7.77279 | 14.6468 |
| tossup_hazard | hazard_total_drop_d2 | 1240 | 2.08505 | 2.15359 | 0.857634 | 0.965516 | 1.02587 | 1.17832 | 1.66092 | 7.40241 | 14.6464 |
| tossup_hazard | hazard_total_drop_d3 | 1240 | 2.01706 | 2.07038 | 0.870204 | 0.960295 | 1.02158 | 1.15595 | 1.6685 | 7.15057 | 16.447 |
| tossup_hazard | hazard_drop_share_1_d1 | 1240 | 0.230259 | 0.0834209 | 0.0448788 | 0.0794961 | 0.162393 | 0.263412 | 0.292265 | 0.317601 | 0.606691 |
| tossup_hazard | hazard_drop_share_2_d1 | 1240 | 0.34517 | 0.0808367 | 0.0695498 | 0.175002 | 0.335043 | 0.351386 | 0.368235 | 0.473752 | 0.717466 |
| tossup_hazard | hazard_drop_share_3_d1 | 1240 | 0.42457 | 0.133977 | 0.0949365 | 0.299084 | 0.34974 | 0.372421 | 0.455545 | 0.737012 | 0.883802 |
| tossup_hazard | hazard_drop_share_1_d2 | 1240 | 0.254596 | 0.0653611 | 0.0303114 | 0.0987459 | 0.239481 | 0.278382 | 0.294725 | 0.314099 | 0.480469 |
| tossup_hazard | hazard_drop_share_2_d2 | 1240 | 0.348241 | 0.0533846 | 0.0802464 | 0.254106 | 0.341527 | 0.351362 | 0.362618 | 0.404492 | 0.709776 |
| tossup_hazard | hazard_drop_share_3_d2 | 1240 | 0.397164 | 0.0972335 | 0.134845 | 0.323479 | 0.350473 | 0.36673 | 0.398383 | 0.633355 | 0.878244 |
| tossup_hazard | hazard_drop_share_1_d3 | 1240 | 0.25535 | 0.0655365 | 0.0342663 | 0.0947824 | 0.241653 | 0.280508 | 0.295575 | 0.314301 | 0.39353 |
| tossup_hazard | hazard_drop_share_2_d3 | 1240 | 0.348571 | 0.0568431 | 0.0562699 | 0.258605 | 0.341023 | 0.351496 | 0.362115 | 0.399956 | 0.679054 |
| tossup_hazard | hazard_drop_share_3_d3 | 1240 | 0.396079 | 0.09912 | 0.114162 | 0.324072 | 0.349787 | 0.365373 | 0.395836 | 0.637926 | 0.904605 |
| tossup_hazard | hazard_r_1 | 1240 | 0.41889 | 0.279388 | 0.0215937 | 0.061459 | 0.147194 | 0.37877 | 0.674011 | 0.86191 | 0.948725 |
| tossup_hazard | hazard_r_2 | 1240 | 0.291748 | 0.205324 | 0.0258604 | 0.0575926 | 0.122333 | 0.231867 | 0.422623 | 0.700738 | 0.911944 |
| tossup_hazard | hazard_r_3 | 1240 | 0.289362 | 0.215979 | 0.0254147 | 0.0663934 | 0.117528 | 0.213288 | 0.407594 | 0.74368 | 0.934943 |
