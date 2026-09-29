# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/training/incorrect-loss-weight/weight-2/fold_1/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/training/incorrect-loss-weight/weight-2/fold_1`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 292820 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.709228 |
| log_loss | 0.532209 |
| ece | 0.10994 |
| brier | 0.176749 |
| accuracy | 0.745958 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.0161663 |
| probability_std | 0.194779 |
| probability_p10 | 0.365932 |
| probability_p50 | 0.688474 |
| probability_p90 | 0.880393 |
| mean_predictive_variance | 0.188487 |
| integrated_brier_score | 0.100931 |
| joint_tossup_event_log_loss | 6.64259 |
| buzz_position_mae | 0.151387 |
| buzz_position_median_absolute_error | 0.13403 |
| buzz_position_bias | -0.0480406 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |
| first_buzzer_top1_accuracy | 0.351039 |
| first_buzzer_mean_reciprocal_rank | 0.562887 |
| first_buzzer_log_loss | 1.68294 |
| first_buzzer_events | 9093 |
| neg_auroc | 0.709228 |
| neg_average_precision | 0.445145 |
| neg_precision | 0.462671 |
| neg_recall | 0.421174 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.190501 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0151147 |
| no_buzz_calibration_error | -0.000794359 |
| no_buzz_brier | 0.0154285 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.709228 | 0.532209 | 0.10994 | 0.176749 | 0.745958 | 0.762125 | -0.0161663 | 0.194779 | 0.365932 | 0.688474 | 0.880393 | 0.188487 |
| tossup_correctness | tier | fall | 2842 | 0.726047 | 0.501713 | 0.109479 | 0.164218 | 0.768825 | 0.785362 | -0.0165376 | 0.193603 | 0.38936 | 0.715767 | 0.901465 | 0.181583 |
| tossup_correctness | tier | nationals | 1564 | 0.714956 | 0.556395 | 0.0940044 | 0.186841 | 0.721867 | 0.718031 | 0.00383632 | 0.196419 | 0.339211 | 0.658073 | 0.863876 | 0.194953 |
| tossup_correctness | tier | regionals | 1937 | 0.68628 | 0.550017 | 0.113824 | 0.183829 | 0.738255 | 0.758389 | -0.0201342 | 0.188751 | 0.366991 | 0.677798 | 0.870284 | 0.192603 |
| tossup_correctness | tier | winter | 2750 | 0.699964 | 0.537429 | 0.119137 | 0.178972 | 0.741455 | 0.765818 | -0.0243636 | 0.196851 | 0.361595 | 0.6891 | 0.874962 | 0.189045 |
| tossup_correctness | category | Current Events | 126 | 0.71454 | 0.556187 | 0.172255 | 0.188069 | 0.706349 | 0.769841 | -0.0634921 | 0.18382 | 0.335403 | 0.623599 | 0.836976 | 0.204307 |
| tossup_correctness | category | Fine Arts | 1071 | 0.745462 | 0.509881 | 0.118301 | 0.168013 | 0.763772 | 0.766573 | -0.00280112 | 0.205059 | 0.341653 | 0.692856 | 0.882963 | 0.185966 |
| tossup_correctness | category | Geography | 185 | 0.789037 | 0.560805 | 0.160833 | 0.186388 | 0.724324 | 0.697297 | 0.027027 | 0.235972 | 0.186894 | 0.582721 | 0.834375 | 0.191668 |
| tossup_correctness | category | History | 1440 | 0.707024 | 0.537209 | 0.0956915 | 0.179552 | 0.731944 | 0.754167 | -0.0222222 | 0.196653 | 0.370426 | 0.693142 | 0.893001 | 0.185839 |
| tossup_correctness | category | Literature | 1422 | 0.677939 | 0.4961 | 0.118506 | 0.161149 | 0.778481 | 0.814346 | -0.035865 | 0.176555 | 0.444816 | 0.736082 | 0.900685 | 0.179577 |
| tossup_correctness | category | Mythology | 318 | 0.666052 | 0.517681 | 0.132596 | 0.168372 | 0.757862 | 0.789308 | -0.0314465 | 0.179837 | 0.447884 | 0.723035 | 0.89196 | 0.182245 |
| tossup_correctness | category | Other Academic | 66 | 0.81411 | 0.507052 | 0.130767 | 0.16451 | 0.742424 | 0.712121 | 0.030303 | 0.183774 | 0.354037 | 0.67346 | 0.853066 | 0.197231 |
| tossup_correctness | category | Philosophy | 311 | 0.720864 | 0.527313 | 0.0937828 | 0.176558 | 0.749196 | 0.745981 | 0.00321543 | 0.185183 | 0.382808 | 0.690226 | 0.874702 | 0.190467 |
| tossup_correctness | category | Popular Culture | 102 | 0.535185 | 0.438028 | 0.156356 | 0.132091 | 0.833333 | 0.882353 | -0.0490196 | 0.120461 | 0.57865 | 0.771083 | 0.866465 | 0.176513 |
| tossup_correctness | category | Religion | 358 | 0.715553 | 0.571591 | 0.112204 | 0.193023 | 0.717877 | 0.712291 | 0.00558659 | 0.202495 | 0.309782 | 0.646766 | 0.844358 | 0.198767 |
| tossup_correctness | category | Science | 1433 | 0.696257 | 0.55526 | 0.100152 | 0.187096 | 0.722261 | 0.738311 | -0.0160502 | 0.197737 | 0.350437 | 0.665658 | 0.874269 | 0.191682 |
| tossup_correctness | category | Social Science | 324 | 0.779281 | 0.518431 | 0.113674 | 0.170613 | 0.774691 | 0.731481 | 0.0432099 | 0.199796 | 0.319902 | 0.657904 | 0.849802 | 0.195844 |
| tossup_correctness | category | Unknown | 1937 | 0.68628 | 0.550017 | 0.113824 | 0.183829 | 0.738255 | 0.758389 | -0.0201342 | 0.188751 | 0.366991 | 0.677798 | 0.870284 | 0.192603 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.619573 | 0.63498 | 0.130441 | 0.218041 | 0.676647 | 0.712575 | -0.0359281 | 0.188446 | 0.363205 | 0.642538 | 0.841537 | 0.200222 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.723065 | 0.553881 | 0.108051 | 0.187033 | 0.718202 | 0.729167 | -0.0109649 | 0.207566 | 0.315135 | 0.65191 | 0.866448 | 0.192074 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.711127 | 0.528005 | 0.0970417 | 0.1747 | 0.748463 | 0.755083 | -0.00661939 | 0.188567 | 0.387108 | 0.695732 | 0.881715 | 0.187847 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.692603 | 0.519505 | 0.109749 | 0.17098 | 0.759845 | 0.780942 | -0.021097 | 0.181105 | 0.411956 | 0.705343 | 0.882312 | 0.187313 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.720568 | 0.534859 | 0.12227 | 0.178211 | 0.743372 | 0.762029 | -0.0186579 | 0.204981 | 0.329362 | 0.67353 | 0.8817 | 0.18831 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1167 | 2.6782 | 0.776024 | 0.440136 | 1.45987 | 2.13684 | 2.67225 | 3.20269 | 3.97546 | 4.66393 |
| player | theta_1 | 1167 | -1.24088 | 0.902314 | -3.8304 | -2.67494 | -1.80749 | -1.3112 | -0.720646 | 0.360094 | 1.86253 |
| player | theta_2 | 1167 | -1.04723 | 0.752552 | -3.64066 | -2.23242 | -1.50404 | -1.08753 | -0.615926 | 0.209776 | 1.95621 |
| player | theta_3 | 1167 | -1.08334 | 0.808506 | -3.5444 | -2.35204 | -1.59904 | -1.13122 | -0.614395 | 0.358001 | 1.97705 |
| player | theta_norm | 1167 | 2.3122 | 0.704781 | 0.390938 | 1.23862 | 1.80222 | 2.26843 | 2.76509 | 3.57235 | 4.60604 |
| tossup | start_difficulty_d1 | 1220 | -1.13285 | 0.637711 | -3.25851 | -2.06506 | -1.55163 | -1.16662 | -0.765043 | -0.108245 | 1.96973 |
| tossup | start_difficulty_d2 | 1220 | -1.11645 | 0.588983 | -3.26879 | -2.02205 | -1.49475 | -1.13646 | -0.761271 | -0.100211 | 1.06986 |
| tossup | start_difficulty_d3 | 1220 | -1.1146 | 0.583181 | -3.45074 | -2.03317 | -1.51304 | -1.11672 | -0.748232 | -0.105895 | 0.973012 |
| tossup | end_difficulty_d1 | 1220 | -2.12722 | 0.743638 | -4.83471 | -3.2471 | -2.61134 | -2.14856 | -1.68982 | -0.944288 | 1.3112 |
| tossup | end_difficulty_d2 | 1220 | -2.10472 | 0.688522 | -4.90345 | -3.1933 | -2.53972 | -2.11737 | -1.67741 | -0.918622 | 0.366433 |
| tossup | end_difficulty_d3 | 1220 | -2.09966 | 0.680855 | -4.85834 | -3.17488 | -2.54935 | -2.08484 | -1.6807 | -0.965853 | 0.279513 |
| tossup | total_drop_d1 | 1220 | 0.994367 | 0.150143 | 0.593445 | 0.760287 | 0.899502 | 0.98672 | 1.07411 | 1.23444 | 1.92284 |
| tossup | total_drop_d2 | 1220 | 0.988274 | 0.129062 | 0.62934 | 0.797055 | 0.907008 | 0.983778 | 1.05738 | 1.21019 | 1.74278 |
| tossup | total_drop_d3 | 1220 | 0.985059 | 0.125518 | 0.646676 | 0.797072 | 0.900271 | 0.979591 | 1.05868 | 1.20214 | 1.52743 |
| tossup | drop_share_1_d1 | 1220 | 0.302409 | 0.019883 | 0.15881 | 0.270467 | 0.292308 | 0.30359 | 0.315047 | 0.330404 | 0.372555 |
| tossup | drop_share_2_d1 | 1220 | 0.347201 | 0.0124143 | 0.306048 | 0.326554 | 0.339318 | 0.347369 | 0.355372 | 0.36681 | 0.398158 |
| tossup | drop_share_3_d1 | 1220 | 0.35039 | 0.021127 | 0.289314 | 0.319907 | 0.336833 | 0.349533 | 0.361665 | 0.384588 | 0.531384 |
| tossup | drop_share_1_d2 | 1220 | 0.302294 | 0.0173129 | 0.195221 | 0.272876 | 0.292097 | 0.303115 | 0.312895 | 0.329354 | 0.366112 |
| tossup | drop_share_2_d2 | 1220 | 0.34686 | 0.0122877 | 0.309643 | 0.326804 | 0.338539 | 0.346698 | 0.354909 | 0.366563 | 0.418532 |
| tossup | drop_share_3_d2 | 1220 | 0.350847 | 0.0185427 | 0.278107 | 0.322578 | 0.339043 | 0.350668 | 0.361463 | 0.379682 | 0.469083 |
| tossup | drop_share_1_d3 | 1220 | 0.302259 | 0.0176179 | 0.216092 | 0.27364 | 0.292168 | 0.303081 | 0.3135 | 0.33014 | 0.375331 |
| tossup | drop_share_2_d3 | 1220 | 0.347066 | 0.0118312 | 0.307457 | 0.327877 | 0.339337 | 0.347058 | 0.354648 | 0.367057 | 0.390015 |
| tossup | drop_share_3_d3 | 1220 | 0.350675 | 0.0188309 | 0.295199 | 0.322603 | 0.338756 | 0.349731 | 0.361262 | 0.383795 | 0.450535 |
| tossup | r_1 | 1220 | 0.341119 | 0.197073 | 0.0480482 | 0.0936967 | 0.174801 | 0.294628 | 0.484695 | 0.711132 | 0.873487 |
| tossup | r_2 | 1220 | 0.328435 | 0.168453 | 0.0460246 | 0.103821 | 0.199509 | 0.302008 | 0.428245 | 0.678191 | 0.881992 |
| tossup | r_3 | 1220 | 0.330446 | 0.171148 | 0.0627577 | 0.10926 | 0.195545 | 0.297314 | 0.434529 | 0.672383 | 0.875551 |
| tossup | r_norm | 1220 | 0.652501 | 0.064021 | 0.577365 | 0.582403 | 0.601606 | 0.633568 | 0.688099 | 0.784923 | 0.885949 |
| tossup_hazard | hazard_start_difficulty_d1 | 1220 | 4.49543 | 0.485417 | 1.83255 | 3.79789 | 4.21124 | 4.44094 | 4.73421 | 5.40226 | 6.39644 |
| tossup_hazard | hazard_start_difficulty_d2 | 1220 | 4.44044 | 0.435262 | 1.90681 | 3.77936 | 4.20881 | 4.41809 | 4.6561 | 5.182 | 6.59733 |
| tossup_hazard | hazard_start_difficulty_d3 | 1220 | 4.44783 | 0.4242 | 2.15978 | 3.78444 | 4.21988 | 4.43961 | 4.67562 | 5.16961 | 6.00438 |
| tossup_hazard | hazard_end_difficulty_d1 | 1220 | 1.70177 | 2.3494 | -11.25 | -3.50031 | 0.611894 | 2.82363 | 3.29171 | 3.64677 | 4.37551 |
| tossup_hazard | hazard_end_difficulty_d2 | 1220 | 2.17973 | 2.10474 | -9.44517 | -2.48172 | 2.08166 | 3.07259 | 3.36118 | 3.71567 | 4.09891 |
| tossup_hazard | hazard_end_difficulty_d3 | 1220 | 2.23353 | 2.19675 | -9.60087 | -2.83804 | 2.31156 | 3.15202 | 3.40486 | 3.7368 | 4.45829 |
| tossup_hazard | hazard_total_drop_d1 | 1220 | 2.79366 | 2.52041 | 0.907472 | 0.981264 | 1.0554 | 1.3731 | 4.04524 | 8.19792 | 15.818 |
| tossup_hazard | hazard_total_drop_d2 | 1220 | 2.26071 | 2.25042 | 0.899651 | 0.962455 | 1.02454 | 1.20094 | 2.09995 | 7.35609 | 14.1045 |
| tossup_hazard | hazard_total_drop_d3 | 1220 | 2.2143 | 2.31567 | 0.869354 | 0.966331 | 1.02435 | 1.16184 | 1.81519 | 7.81525 | 14.1577 |
| tossup_hazard | hazard_drop_share_1_d1 | 1220 | 0.233242 | 0.0803146 | 0.0429874 | 0.0814966 | 0.172978 | 0.266565 | 0.294452 | 0.315368 | 0.533841 |
| tossup_hazard | hazard_drop_share_2_d1 | 1220 | 0.342545 | 0.0760629 | 0.0569254 | 0.174002 | 0.335861 | 0.351371 | 0.366564 | 0.442574 | 0.672112 |
| tossup_hazard | hazard_drop_share_3_d1 | 1220 | 0.424214 | 0.130491 | 0.113935 | 0.308942 | 0.348789 | 0.370083 | 0.450746 | 0.731163 | 0.900087 |
| tossup_hazard | hazard_drop_share_1_d2 | 1220 | 0.250833 | 0.0709576 | 0.031305 | 0.0911173 | 0.229913 | 0.278373 | 0.295822 | 0.313864 | 0.533145 |
| tossup_hazard | hazard_drop_share_2_d2 | 1220 | 0.347957 | 0.0646295 | 0.0657199 | 0.215756 | 0.340099 | 0.351273 | 0.364664 | 0.418675 | 0.706558 |
| tossup_hazard | hazard_drop_share_3_d2 | 1220 | 0.40121 | 0.109768 | 0.0941135 | 0.316056 | 0.349862 | 0.36464 | 0.399996 | 0.671252 | 0.88803 |
| tossup_hazard | hazard_drop_share_1_d3 | 1220 | 0.25344 | 0.0683403 | 0.0391314 | 0.0915975 | 0.236245 | 0.278331 | 0.296452 | 0.314022 | 0.575331 |
| tossup_hazard | hazard_drop_share_2_d3 | 1220 | 0.350687 | 0.0574602 | 0.0831763 | 0.251446 | 0.340386 | 0.351554 | 0.364654 | 0.417494 | 0.688461 |
| tossup_hazard | hazard_drop_share_3_d3 | 1220 | 0.395873 | 0.100062 | 0.0724345 | 0.321167 | 0.349668 | 0.367255 | 0.396986 | 0.635402 | 0.86875 |
| tossup_hazard | hazard_r_1 | 1220 | 0.392091 | 0.27772 | 0.0307751 | 0.0596564 | 0.133465 | 0.321437 | 0.641542 | 0.874236 | 0.942083 |
| tossup_hazard | hazard_r_2 | 1220 | 0.303559 | 0.222362 | 0.0228366 | 0.052903 | 0.118766 | 0.231483 | 0.466177 | 0.736918 | 0.861245 |
| tossup_hazard | hazard_r_3 | 1220 | 0.30435 | 0.224289 | 0.0228399 | 0.051985 | 0.124123 | 0.233803 | 0.461457 | 0.750116 | 0.918978 |
