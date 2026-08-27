# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/incorrect-loss-weight/weight-3/fold_0/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/incorrect-loss-weight/weight-3/fold_0`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 297496 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.711536 |
| log_loss | 0.586409 |
| ece | 0.183534 |
| brier | 0.200428 |
| accuracy | 0.696181 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | -0.0690694 |
| probability_std | 0.2133 |
| probability_p10 | 0.272008 |
| probability_p50 | 0.605793 |
| probability_p90 | 0.84962 |
| mean_predictive_variance | 0.197826 |
| integrated_brier_score | 0.102031 |
| joint_tossup_event_log_loss | 6.71197 |
| buzz_position_mae | 0.152367 |
| buzz_position_median_absolute_error | 0.13577 |
| buzz_position_bias | -0.0425474 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |
| first_buzzer_top1_accuracy | 0.353201 |
| first_buzzer_mean_reciprocal_rank | 0.567101 |
| first_buzzer_log_loss | 1.66616 |
| first_buzzer_events | 9295 |
| neg_auroc | 0.711536 |
| neg_average_precision | 0.440017 |
| neg_precision | 0.398546 |
| neg_recall | 0.57791 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.188025 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.015834 |
| no_buzz_calibration_error | 0.00256435 |
| no_buzz_brier | 0.0130475 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.711536 | 0.586409 | 0.183534 | 0.200428 | 0.696181 | 0.76525 | -0.0690694 | 0.2133 | 0.272008 | 0.605793 | 0.84962 | 0.197826 |
| tossup_correctness | tier | fall | 2933 | 0.707401 | 0.570275 | 0.190498 | 0.193806 | 0.70849 | 0.791681 | -0.0831913 | 0.214803 | 0.282033 | 0.634826 | 0.864864 | 0.193622 |
| tossup_correctness | tier | nationals | 1584 | 0.706894 | 0.610462 | 0.167889 | 0.210422 | 0.675505 | 0.724747 | -0.0492424 | 0.220738 | 0.237571 | 0.589651 | 0.838634 | 0.198042 |
| tossup_correctness | tier | regionals | 1886 | 0.705842 | 0.609288 | 0.185358 | 0.210348 | 0.672322 | 0.746023 | -0.073701 | 0.207328 | 0.269727 | 0.571665 | 0.830569 | 0.203332 |
| tossup_correctness | tier | winter | 2892 | 0.71652 | 0.574678 | 0.183869 | 0.195202 | 0.710581 | 0.773167 | -0.0625864 | 0.208914 | 0.295057 | 0.607353 | 0.854379 | 0.198381 |
| tossup_correctness | category | Current Events | 124 | 0.673951 | 0.652933 | 0.213371 | 0.229912 | 0.604839 | 0.75 | -0.145161 | 0.228057 | 0.246235 | 0.526012 | 0.855983 | 0.196169 |
| tossup_correctness | category | Fine Arts | 1103 | 0.709213 | 0.579968 | 0.170641 | 0.197199 | 0.712602 | 0.759746 | -0.0471442 | 0.214679 | 0.27664 | 0.613962 | 0.854945 | 0.195682 |
| tossup_correctness | category | Geography | 197 | 0.788811 | 0.61164 | 0.182742 | 0.205916 | 0.71066 | 0.670051 | 0.0406091 | 0.244457 | 0.150089 | 0.503709 | 0.798277 | 0.19008 |
| tossup_correctness | category | History | 1491 | 0.717765 | 0.577463 | 0.19998 | 0.19731 | 0.696177 | 0.787391 | -0.091214 | 0.212977 | 0.279979 | 0.611047 | 0.856424 | 0.197 |
| tossup_correctness | category | Literature | 1472 | 0.723988 | 0.518875 | 0.165625 | 0.17048 | 0.758152 | 0.804348 | -0.0461957 | 0.193639 | 0.352852 | 0.670327 | 0.865721 | 0.19326 |
| tossup_correctness | category | Mythology | 332 | 0.688949 | 0.554016 | 0.193068 | 0.185982 | 0.73494 | 0.813253 | -0.0783133 | 0.196093 | 0.33522 | 0.646848 | 0.846787 | 0.197103 |
| tossup_correctness | category | Other Academic | 69 | 0.664027 | 0.629123 | 0.212718 | 0.22021 | 0.666667 | 0.753623 | -0.0869565 | 0.159795 | 0.313716 | 0.562535 | 0.751319 | 0.222309 |
| tossup_correctness | category | Philosophy | 324 | 0.688209 | 0.589027 | 0.210048 | 0.203085 | 0.685185 | 0.799383 | -0.114198 | 0.209497 | 0.288954 | 0.604941 | 0.858906 | 0.198064 |
| tossup_correctness | category | Popular Culture | 102 | 0.466436 | 0.574082 | 0.200925 | 0.190239 | 0.764706 | 0.833333 | -0.0686275 | 0.142977 | 0.483629 | 0.669169 | 0.823652 | 0.2019 |
| tossup_correctness | category | Religion | 372 | 0.707421 | 0.631355 | 0.18512 | 0.221786 | 0.623656 | 0.709677 | -0.0860215 | 0.213277 | 0.242901 | 0.518153 | 0.803883 | 0.20391 |
| tossup_correctness | category | Science | 1487 | 0.688535 | 0.617432 | 0.187892 | 0.214507 | 0.670477 | 0.752522 | -0.0820444 | 0.221599 | 0.242834 | 0.586782 | 0.849753 | 0.196717 |
| tossup_correctness | category | Social Science | 336 | 0.726737 | 0.612751 | 0.16362 | 0.211084 | 0.681548 | 0.702381 | -0.0208333 | 0.230775 | 0.207579 | 0.565346 | 0.847588 | 0.195171 |
| tossup_correctness | category | Unknown | 1886 | 0.705842 | 0.609288 | 0.185358 | 0.210348 | 0.672322 | 0.746023 | -0.073701 | 0.207328 | 0.269727 | 0.571665 | 0.830569 | 0.203332 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.688462 | 0.648845 | 0.245646 | 0.225187 | 0.675127 | 0.736041 | -0.0609137 | 0.213396 | 0.232254 | 0.545554 | 0.822866 | 0.203423 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.704976 | 0.601307 | 0.166982 | 0.207671 | 0.679188 | 0.735025 | -0.0558376 | 0.214077 | 0.261479 | 0.5876 | 0.8399 | 0.199541 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.698157 | 0.588237 | 0.179838 | 0.200452 | 0.694358 | 0.769436 | -0.0750777 | 0.210816 | 0.288635 | 0.61216 | 0.854577 | 0.197276 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.70065 | 0.571007 | 0.182221 | 0.194101 | 0.707955 | 0.78402 | -0.0760642 | 0.207175 | 0.304554 | 0.628277 | 0.859786 | 0.196715 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.733053 | 0.590767 | 0.19273 | 0.202455 | 0.693258 | 0.756008 | -0.0627503 | 0.218235 | 0.247407 | 0.587928 | 0.839307 | 0.198369 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1186 | 2.67069 | 0.779772 | 0.557701 | 1.42463 | 2.12853 | 2.66159 | 3.20198 | 4.02905 | 4.69592 |
| player | theta_1 | 1186 | -1.23187 | 0.961367 | -3.86718 | -2.77601 | -1.81084 | -1.26111 | -0.666218 | 0.450532 | 2.46415 |
| player | theta_2 | 1186 | -1.08005 | 0.806329 | -3.93525 | -2.38845 | -1.59362 | -1.09202 | -0.543693 | 0.213209 | 1.45875 |
| player | theta_3 | 1186 | -1.11332 | 0.852795 | -3.79245 | -2.46562 | -1.66995 | -1.14824 | -0.606555 | 0.360187 | 2.08841 |
| player | theta_norm | 1186 | 2.37879 | 0.751689 | 0.41515 | 1.18775 | 1.86645 | 2.32514 | 2.8782 | 3.66025 | 4.87574 |
| tossup | start_difficulty_d1 | 1240 | -0.746517 | 0.673601 | -3.57893 | -1.73761 | -1.14971 | -0.782242 | -0.369096 | 0.363645 | 2.37331 |
| tossup | start_difficulty_d2 | 1240 | -0.730454 | 0.623 | -2.84928 | -1.68572 | -1.10346 | -0.758592 | -0.392186 | 0.395497 | 1.61734 |
| tossup | start_difficulty_d3 | 1240 | -0.720899 | 0.609384 | -3.41699 | -1.69342 | -1.12706 | -0.736188 | -0.366921 | 0.318714 | 2.76075 |
| tossup | end_difficulty_d1 | 1240 | -1.74728 | 0.792494 | -5.17939 | -2.96538 | -2.20029 | -1.7693 | -1.28335 | -0.480231 | 1.79854 |
| tossup | end_difficulty_d2 | 1240 | -1.72457 | 0.735808 | -4.71398 | -2.86675 | -2.15947 | -1.74505 | -1.32024 | -0.426527 | 1.00364 |
| tossup | end_difficulty_d3 | 1240 | -1.71154 | 0.71276 | -4.95397 | -2.84712 | -2.1588 | -1.71796 | -1.28329 | -0.56988 | 2.07891 |
| tossup | total_drop_d1 | 1240 | 1.00076 | 0.178242 | 0.574766 | 0.749006 | 0.90212 | 0.988797 | 1.07633 | 1.28013 | 2.6284 |
| tossup | total_drop_d2 | 1240 | 0.994112 | 0.169863 | 0.578356 | 0.762269 | 0.908157 | 0.982866 | 1.06156 | 1.23182 | 4.15636 |
| tossup | total_drop_d3 | 1240 | 0.990643 | 0.182945 | 0.549243 | 0.782358 | 0.894921 | 0.98186 | 1.05685 | 1.22522 | 4.83069 |
| tossup | drop_share_1_d1 | 1240 | 0.301347 | 0.0223472 | 0.176593 | 0.264598 | 0.290121 | 0.30285 | 0.314078 | 0.333294 | 0.390372 |
| tossup | drop_share_2_d1 | 1240 | 0.347289 | 0.0136428 | 0.283438 | 0.325317 | 0.338646 | 0.347113 | 0.355937 | 0.368712 | 0.420742 |
| tossup | drop_share_3_d1 | 1240 | 0.351364 | 0.0237992 | 0.272046 | 0.317501 | 0.336783 | 0.349735 | 0.363696 | 0.391371 | 0.513545 |
| tossup | drop_share_1_d2 | 1240 | 0.301449 | 0.0191634 | 0.155497 | 0.269008 | 0.291459 | 0.302921 | 0.313146 | 0.328992 | 0.370673 |
| tossup | drop_share_2_d2 | 1240 | 0.347037 | 0.0137657 | 0.294423 | 0.326107 | 0.338591 | 0.346758 | 0.355031 | 0.368119 | 0.501262 |
| tossup | drop_share_3_d2 | 1240 | 0.351514 | 0.0210768 | 0.277627 | 0.319222 | 0.338787 | 0.351025 | 0.362473 | 0.385069 | 0.475026 |
| tossup | drop_share_1_d3 | 1240 | 0.301203 | 0.0210979 | 0.0925467 | 0.269891 | 0.290437 | 0.302344 | 0.313635 | 0.331757 | 0.389137 |
| tossup | drop_share_2_d3 | 1240 | 0.34701 | 0.0128128 | 0.269032 | 0.327175 | 0.33917 | 0.346859 | 0.355021 | 0.367593 | 0.406659 |
| tossup | drop_share_3_d3 | 1240 | 0.351788 | 0.023215 | 0.280038 | 0.321121 | 0.338481 | 0.350547 | 0.362067 | 0.386926 | 0.587538 |
| tossup | r_1 | 1240 | 0.345778 | 0.227419 | 0.0319015 | 0.0770593 | 0.149518 | 0.279725 | 0.532085 | 0.763941 | 0.859142 |
| tossup | r_2 | 1240 | 0.325872 | 0.20961 | 0.0384417 | 0.0816327 | 0.155452 | 0.264775 | 0.451804 | 0.73545 | 0.903359 |
| tossup | r_3 | 1240 | 0.32835 | 0.208385 | 0.0330668 | 0.0867473 | 0.154365 | 0.264948 | 0.472144 | 0.738333 | 0.915602 |
| tossup | r_norm | 1240 | 0.683278 | 0.0753143 | 0.577381 | 0.587914 | 0.62114 | 0.665987 | 0.737005 | 0.827206 | 0.91766 |
| tossup_hazard | hazard_start_difficulty_d1 | 1240 | 4.4747 | 0.50618 | 1.71451 | 3.69615 | 4.1947 | 4.43627 | 4.75012 | 5.40657 | 6.34954 |
| tossup_hazard | hazard_start_difficulty_d2 | 1240 | 4.44712 | 0.443285 | 2.7674 | 3.72594 | 4.21287 | 4.40549 | 4.66472 | 5.2192 | 6.62349 |
| tossup_hazard | hazard_start_difficulty_d3 | 1240 | 4.45697 | 0.432125 | 2.5698 | 3.74776 | 4.22666 | 4.44411 | 4.6812 | 5.21947 | 6.28724 |
| tossup_hazard | hazard_end_difficulty_d1 | 1240 | 1.71861 | 2.34802 | -11.7288 | -3.26689 | 0.566952 | 2.84471 | 3.28548 | 3.64906 | 4.40342 |
| tossup_hazard | hazard_end_difficulty_d2 | 1240 | 2.17037 | 2.14836 | -9.42939 | -2.84341 | 2.16432 | 3.07368 | 3.34932 | 3.70487 | 4.31703 |
| tossup_hazard | hazard_end_difficulty_d3 | 1240 | 2.24201 | 2.22517 | -9.56476 | -3.1353 | 2.39999 | 3.16022 | 3.40546 | 3.74254 | 4.29903 |
| tossup_hazard | hazard_total_drop_d1 | 1240 | 2.75608 | 2.52021 | 0.883474 | 0.98364 | 1.0576 | 1.32984 | 4.14461 | 8.07401 | 16.4326 |
| tossup_hazard | hazard_total_drop_d2 | 1240 | 2.27675 | 2.31728 | 0.894174 | 0.961049 | 1.0228 | 1.179 | 2.04416 | 7.78075 | 14.6135 |
| tossup_hazard | hazard_total_drop_d3 | 1240 | 2.21496 | 2.34324 | 0.847601 | 0.964986 | 1.02363 | 1.15208 | 1.77959 | 7.58884 | 14.4951 |
| tossup_hazard | hazard_drop_share_1_d1 | 1240 | 0.236481 | 0.0804429 | 0.0414423 | 0.0824189 | 0.176236 | 0.26968 | 0.294642 | 0.316885 | 0.541291 |
| tossup_hazard | hazard_drop_share_2_d1 | 1240 | 0.341967 | 0.0729398 | 0.0605892 | 0.187479 | 0.334569 | 0.351279 | 0.365502 | 0.433191 | 0.709481 |
| tossup_hazard | hazard_drop_share_3_d1 | 1240 | 0.421552 | 0.128459 | 0.133589 | 0.30951 | 0.348522 | 0.370237 | 0.450129 | 0.716082 | 0.895254 |
| tossup_hazard | hazard_drop_share_1_d2 | 1240 | 0.250083 | 0.0714207 | 0.0360105 | 0.0883668 | 0.223859 | 0.278639 | 0.296589 | 0.314656 | 0.608472 |
| tossup_hazard | hazard_drop_share_2_d2 | 1240 | 0.348902 | 0.0650076 | 0.0673363 | 0.21288 | 0.340228 | 0.351613 | 0.364583 | 0.436972 | 0.674757 |
| tossup_hazard | hazard_drop_share_3_d2 | 1240 | 0.401014 | 0.109052 | 0.0986743 | 0.319824 | 0.349732 | 0.36484 | 0.403844 | 0.675681 | 0.889031 |
| tossup_hazard | hazard_drop_share_1_d3 | 1240 | 0.253703 | 0.0693089 | 0.0359469 | 0.0919542 | 0.23864 | 0.278284 | 0.296385 | 0.315518 | 0.566134 |
| tossup_hazard | hazard_drop_share_2_d3 | 1240 | 0.348121 | 0.0607775 | 0.092461 | 0.2348 | 0.339945 | 0.351115 | 0.363602 | 0.417063 | 0.699638 |
| tossup_hazard | hazard_drop_share_3_d3 | 1240 | 0.398176 | 0.105185 | 0.12771 | 0.321061 | 0.349447 | 0.365282 | 0.39481 | 0.669286 | 0.870338 |
| tossup_hazard | hazard_r_1 | 1240 | 0.386338 | 0.271737 | 0.0341075 | 0.0570002 | 0.139372 | 0.327798 | 0.609629 | 0.864588 | 0.937589 |
| tossup_hazard | hazard_r_2 | 1240 | 0.313336 | 0.224909 | 0.0232822 | 0.0478659 | 0.118062 | 0.252258 | 0.476136 | 0.737998 | 0.881588 |
| tossup_hazard | hazard_r_3 | 1240 | 0.300326 | 0.219609 | 0.0270536 | 0.0523773 | 0.12821 | 0.22632 | 0.44539 | 0.748671 | 0.938118 |
