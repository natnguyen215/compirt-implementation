# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perceived-difficulty/three-slice-10000-steps/fold_3/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perceived-difficulty/three-slice-10000-steps/fold_3`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 10000 |
| pyramidal | final_loss | 306313 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.625209 |
| log_loss | 0.634528 |
| ece | 0.203605 |
| brier | 0.220693 |
| accuracy | 0.654626 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | -0.115419 |
| probability_std | 0.169737 |
| probability_p10 | 0.319444 |
| probability_p50 | 0.590609 |
| probability_p90 | 0.76998 |
| mean_predictive_variance | 0.216775 |
| integrated_brier_score | 0.0933127 |
| joint_tossup_event_log_loss | 6.66622 |
| buzz_position_mae | 0.137081 |
| buzz_position_median_absolute_error | 0.113652 |
| buzz_position_bias | -0.0037748 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |
| first_buzzer_top1_accuracy | 0.375 |
| first_buzzer_mean_reciprocal_rank | 0.581981 |
| first_buzzer_log_loss | 1.64024 |
| first_buzzer_events | 9080 |
| neg_auroc | 0.625209 |
| neg_average_precision | 0.322367 |
| neg_precision | 0.320425 |
| neg_recall | 0.447797 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.141288 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.047807 |
| no_buzz_calibration_error | 0.0326226 |
| no_buzz_brier | 0.0181346 |
| full_pmf_max_mass_error | 1.44329e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.625209 | 0.634528 | 0.203605 | 0.220693 | 0.654626 | 0.770044 | -0.115419 | 0.169737 | 0.319444 | 0.590609 | 0.76998 | 0.216775 |
| tossup_correctness | tier | fall | 2817 | 0.626998 | 0.62137 | 0.206236 | 0.2148 | 0.673411 | 0.781683 | -0.108271 | 0.169464 | 0.326917 | 0.602921 | 0.77208 | 0.21559 |
| tossup_correctness | tier | nationals | 1542 | 0.608728 | 0.617192 | 0.144254 | 0.2143 | 0.655642 | 0.73476 | -0.079118 | 0.144106 | 0.387702 | 0.601285 | 0.768142 | 0.221042 |
| tossup_correctness | tier | regionals | 1934 | 0.662406 | 0.623659 | 0.196368 | 0.216296 | 0.658221 | 0.75698 | -0.098759 | 0.172005 | 0.314823 | 0.579551 | 0.775906 | 0.21674 |
| tossup_correctness | tier | winter | 2787 | 0.61182 | 0.664962 | 0.238807 | 0.233236 | 0.63258 | 0.786868 | -0.154288 | 0.179035 | 0.286408 | 0.571922 | 0.762045 | 0.215637 |
| tossup_correctness | category | Current Events | 125 | 0.626229 | 0.649303 | 0.117267 | 0.227027 | 0.624 | 0.704 | -0.08 | 0.170193 | 0.347616 | 0.614517 | 0.765688 | 0.213512 |
| tossup_correctness | category | Fine Arts | 1072 | 0.602025 | 0.645144 | 0.203883 | 0.225876 | 0.633396 | 0.770522 | -0.137127 | 0.167677 | 0.32541 | 0.590109 | 0.767571 | 0.217444 |
| tossup_correctness | category | Geography | 185 | 0.612168 | 0.692719 | 0.18842 | 0.247223 | 0.578378 | 0.702703 | -0.124324 | 0.179601 | 0.268267 | 0.524728 | 0.738592 | 0.217507 |
| tossup_correctness | category | History | 1443 | 0.631156 | 0.627245 | 0.191877 | 0.216808 | 0.671518 | 0.765073 | -0.0935551 | 0.168754 | 0.327747 | 0.600322 | 0.767706 | 0.216165 |
| tossup_correctness | category | Literature | 1411 | 0.577833 | 0.619744 | 0.224828 | 0.214381 | 0.678951 | 0.81219 | -0.133239 | 0.156892 | 0.356609 | 0.60666 | 0.773019 | 0.217753 |
| tossup_correctness | category | Mythology | 320 | 0.588046 | 0.623015 | 0.206059 | 0.215478 | 0.653125 | 0.79375 | -0.140625 | 0.170479 | 0.336758 | 0.617439 | 0.79289 | 0.212582 |
| tossup_correctness | category | Other Academic | 64 | 0.647135 | 0.592655 | 0.157725 | 0.202504 | 0.6875 | 0.75 | -0.0625 | 0.143298 | 0.373034 | 0.635812 | 0.75535 | 0.220951 |
| tossup_correctness | category | Philosophy | 312 | 0.599484 | 0.601316 | 0.207655 | 0.205922 | 0.685897 | 0.801282 | -0.115385 | 0.160268 | 0.393207 | 0.618151 | 0.789061 | 0.215548 |
| tossup_correctness | category | Popular Culture | 104 | 0.537642 | 0.843881 | 0.380644 | 0.306061 | 0.471154 | 0.846154 | -0.375 | 0.197243 | 0.18514 | 0.478166 | 0.726739 | 0.209906 |
| tossup_correctness | category | Religion | 358 | 0.63854 | 0.640058 | 0.170086 | 0.222339 | 0.634078 | 0.726257 | -0.0921788 | 0.183088 | 0.297601 | 0.5885 | 0.782128 | 0.212919 |
| tossup_correctness | category | Science | 1431 | 0.623084 | 0.652313 | 0.217043 | 0.228873 | 0.638015 | 0.765199 | -0.127184 | 0.170024 | 0.307043 | 0.572035 | 0.754517 | 0.218773 |
| tossup_correctness | category | Social Science | 321 | 0.667925 | 0.621825 | 0.183871 | 0.214535 | 0.697819 | 0.744548 | -0.046729 | 0.171807 | 0.349316 | 0.591852 | 0.766712 | 0.216211 |
| tossup_correctness | category | Unknown | 1934 | 0.662406 | 0.623659 | 0.196368 | 0.216296 | 0.658221 | 0.75698 | -0.098759 | 0.172005 | 0.314823 | 0.579551 | 0.775906 | 0.21674 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.706639 | 0.67818 | 0.226072 | 0.239615 | 0.598958 | 0.697917 | -0.0989583 | 0.164424 | 0.24035 | 0.482535 | 0.689033 | 0.222172 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.645524 | 0.682048 | 0.230126 | 0.2421 | 0.5973 | 0.733408 | -0.136108 | 0.170776 | 0.259797 | 0.529729 | 0.71141 | 0.220825 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.632799 | 0.658219 | 0.21858 | 0.230494 | 0.633484 | 0.759276 | -0.125792 | 0.170635 | 0.295643 | 0.566488 | 0.745831 | 0.219227 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.607196 | 0.631554 | 0.213733 | 0.219272 | 0.661206 | 0.789125 | -0.127919 | 0.165366 | 0.336707 | 0.60111 | 0.769665 | 0.21697 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.620753 | 0.602181 | 0.172769 | 0.206909 | 0.685274 | 0.775342 | -0.0900685 | 0.162292 | 0.370793 | 0.627423 | 0.795107 | 0.21314 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1133 | 0.0953302 | 0.91033 | -3.16846 | -1.38227 | -0.410658 | -0.0226541 | 0.588975 | 1.70346 | 3.36697 |
| player | theta_2 | 1133 | -0.0292233 | 1.02747 | -3.22332 | -1.49704 | -0.59915 | -0.161579 | 0.48201 | 1.88168 | 5.33841 |
| player | theta_3 | 1133 | 1.09845 | 1.37624 | -4.11903 | -1.184 | 0.011371 | 1.28607 | 2.22343 | 3.07052 | 4.16341 |
| player | theta_norm | 1133 | 2.0016 | 0.993016 | 0.0779805 | 0.544698 | 1.18988 | 1.96079 | 2.70508 | 3.72664 | 5.48778 |
| tossup | start_difficulty_d1 | 1240 | 1.25014 | 0.721578 | -0.831155 | 0.0704971 | 0.672924 | 1.35938 | 1.8122 | 2.28764 | 2.81285 |
| tossup | start_difficulty_d2 | 1240 | 0.505146 | 0.656414 | -1.72308 | -0.579203 | 0.114116 | 0.473089 | 0.906649 | 1.59155 | 3.10119 |
| tossup | start_difficulty_d3 | 1240 | 1.56077 | 1.12689 | -0.975226 | 0.0628546 | 0.524032 | 1.24176 | 2.64346 | 3.17007 | 4.11614 |
| tossup | end_difficulty_d1 | 1240 | 0.0978383 | 0.547377 | -1.91916 | -0.917803 | -0.255953 | 0.253642 | 0.49068 | 0.794266 | 1.29434 |
| tossup | end_difficulty_d2 | 1240 | -0.432564 | 0.747832 | -4.6958 | -1.64634 | -0.883205 | -0.475682 | 0.031407 | 0.806257 | 2.42466 |
| tossup | end_difficulty_d3 | 1240 | 0.308868 | 0.804943 | -1.84179 | -0.919206 | -0.402197 | 0.291432 | 1.04171 | 1.45019 | 2.14725 |
| tossup | total_drop_d1 | 1240 | 1.1523 | 0.338445 | 0.41035 | 0.777356 | 0.90326 | 1.04254 | 1.36166 | 1.7803 | 2.97274 |
| tossup | total_drop_d2 | 1240 | 0.93771 | 0.201601 | 0.626345 | 0.767328 | 0.859619 | 0.919426 | 0.986123 | 1.09566 | 5.46211 |
| tossup | total_drop_d3 | 1240 | 1.2519 | 0.50629 | 0.582669 | 0.76287 | 0.882255 | 0.991821 | 1.59878 | 2.21818 | 3.68375 |
| tossup | drop_share_1_d1 | 1240 | 0.206375 | 0.0876445 | 0.0477807 | 0.0890344 | 0.124489 | 0.204586 | 0.286221 | 0.311634 | 0.739658 |
| tossup | drop_share_2_d1 | 1240 | 0.266441 | 0.0964689 | 0.067616 | 0.112904 | 0.17688 | 0.309796 | 0.343924 | 0.364801 | 0.658497 |
| tossup | drop_share_3_d1 | 1240 | 0.527185 | 0.169315 | 0.12776 | 0.341486 | 0.369946 | 0.475984 | 0.690652 | 0.787592 | 0.884603 |
| tossup | drop_share_1_d2 | 1240 | 0.286233 | 0.0251589 | 0.0803749 | 0.246302 | 0.277668 | 0.290099 | 0.300451 | 0.315415 | 0.342715 |
| tossup | drop_share_2_d2 | 1240 | 0.341114 | 0.018523 | 0.135237 | 0.318494 | 0.334641 | 0.34306 | 0.351154 | 0.361549 | 0.38494 |
| tossup | drop_share_3_d2 | 1240 | 0.372652 | 0.0371993 | 0.312209 | 0.340323 | 0.354289 | 0.364663 | 0.37952 | 0.42544 | 0.784388 |
| tossup | drop_share_1_d3 | 1240 | 0.233416 | 0.0929206 | 0.0386026 | 0.078876 | 0.145814 | 0.274433 | 0.294785 | 0.321931 | 0.645047 |
| tossup | drop_share_2_d3 | 1240 | 0.297624 | 0.0983077 | 0.0471606 | 0.109665 | 0.233415 | 0.334419 | 0.348162 | 0.424823 | 0.714718 |
| tossup | drop_share_3_d3 | 1240 | 0.46896 | 0.162425 | 0.0801943 | 0.331005 | 0.361527 | 0.384379 | 0.576569 | 0.801214 | 0.914237 |
| tossup | r_1 | 1240 | 0.375151 | 0.29551 | 0.0128746 | 0.0202393 | 0.0507846 | 0.437712 | 0.631296 | 0.832797 | 0.912468 |
| tossup | r_2 | 1240 | 0.145511 | 0.12633 | 0.0155003 | 0.0255182 | 0.0538292 | 0.100051 | 0.196266 | 0.430521 | 0.590529 |
| tossup | r_3 | 1240 | 0.479339 | 0.337776 | 0.0280737 | 0.0555118 | 0.128108 | 0.4122 | 0.839126 | 0.931395 | 0.964439 |
| tossup | r_norm | 1240 | 0.773763 | 0.100894 | 0.581812 | 0.634589 | 0.679686 | 0.766204 | 0.865742 | 0.932895 | 0.96477 |
