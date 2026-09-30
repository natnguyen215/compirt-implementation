# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/perceived-difficulty/three-slice-10000-steps/fold_1/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/perceived-difficulty/three-slice-10000-steps/fold_1`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 10000 |
| pyramidal | final_loss | 305645 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.610693 |
| log_loss | 0.645311 |
| ece | 0.194259 |
| brier | 0.22518 |
| accuracy | 0.649181 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.112944 |
| probability_std | 0.174224 |
| probability_p10 | 0.319826 |
| probability_p50 | 0.591657 |
| probability_p90 | 0.77806 |
| mean_predictive_variance | 0.21504 |
| integrated_brier_score | 0.0934756 |
| joint_tossup_event_log_loss | 6.70594 |
| buzz_position_mae | 0.13795 |
| buzz_position_median_absolute_error | 0.114544 |
| buzz_position_bias | -0.00311037 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |
| first_buzzer_top1_accuracy | 0.370285 |
| first_buzzer_mean_reciprocal_rank | 0.579352 |
| first_buzzer_log_loss | 1.64047 |
| first_buzzer_events | 9093 |
| neg_auroc | 0.610693 |
| neg_average_precision | 0.313848 |
| neg_precision | 0.324684 |
| neg_recall | 0.439667 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.145664 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0507069 |
| no_buzz_calibration_error | 0.0347978 |
| no_buzz_brier | 0.0206719 |
| full_pmf_max_mass_error | 1.55431e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.610693 | 0.645311 | 0.194259 | 0.22518 | 0.649181 | 0.762125 | -0.112944 | 0.174224 | 0.319826 | 0.591657 | 0.77806 | 0.21504 |
| tossup_correctness | tier | fall | 2842 | 0.635726 | 0.613998 | 0.201311 | 0.211079 | 0.690711 | 0.785362 | -0.0946517 | 0.171629 | 0.347735 | 0.603086 | 0.795462 | 0.213479 |
| tossup_correctness | tier | nationals | 1564 | 0.604766 | 0.622674 | 0.121844 | 0.216063 | 0.658568 | 0.718031 | -0.0594629 | 0.151218 | 0.383253 | 0.615063 | 0.775513 | 0.217864 |
| tossup_correctness | tier | regionals | 1937 | 0.604153 | 0.649935 | 0.19674 | 0.228391 | 0.635003 | 0.758389 | -0.123387 | 0.173055 | 0.313787 | 0.585043 | 0.776108 | 0.216251 |
| tossup_correctness | tier | winter | 2750 | 0.600396 | 0.68729 | 0.226459 | 0.242676 | 0.610909 | 0.765818 | -0.154909 | 0.185084 | 0.268458 | 0.565193 | 0.76358 | 0.214195 |
| tossup_correctness | category | Current Events | 126 | 0.573765 | 0.695401 | 0.243033 | 0.249115 | 0.603175 | 0.769841 | -0.166667 | 0.171065 | 0.297304 | 0.54788 | 0.722834 | 0.220018 |
| tossup_correctness | category | Fine Arts | 1071 | 0.623225 | 0.650304 | 0.20578 | 0.226787 | 0.644258 | 0.766573 | -0.122316 | 0.184993 | 0.291217 | 0.595562 | 0.780276 | 0.212082 |
| tossup_correctness | category | Geography | 185 | 0.597868 | 0.711112 | 0.213537 | 0.256881 | 0.556757 | 0.697297 | -0.140541 | 0.168803 | 0.270009 | 0.491411 | 0.705123 | 0.221388 |
| tossup_correctness | category | History | 1440 | 0.598412 | 0.640476 | 0.178631 | 0.223708 | 0.650694 | 0.754167 | -0.103472 | 0.168258 | 0.346449 | 0.59521 | 0.7844 | 0.215819 |
| tossup_correctness | category | Literature | 1422 | 0.59698 | 0.597656 | 0.198881 | 0.202272 | 0.718003 | 0.814346 | -0.0963432 | 0.167196 | 0.386492 | 0.648137 | 0.809311 | 0.208713 |
| tossup_correctness | category | Mythology | 318 | 0.559493 | 0.642648 | 0.192811 | 0.222305 | 0.666667 | 0.789308 | -0.122642 | 0.172962 | 0.329037 | 0.630833 | 0.790594 | 0.210772 |
| tossup_correctness | category | Other Academic | 66 | 0.792833 | 0.558147 | 0.16456 | 0.186969 | 0.712121 | 0.712121 | 0 | 0.173243 | 0.307332 | 0.578508 | 0.739788 | 0.217559 |
| tossup_correctness | category | Philosophy | 311 | 0.621344 | 0.627879 | 0.153408 | 0.218275 | 0.662379 | 0.745981 | -0.0836013 | 0.176114 | 0.351901 | 0.604182 | 0.794309 | 0.210414 |
| tossup_correctness | category | Popular Culture | 102 | 0.485185 | 0.819046 | 0.396632 | 0.298388 | 0.470588 | 0.882353 | -0.411765 | 0.185742 | 0.202022 | 0.513061 | 0.698023 | 0.215296 |
| tossup_correctness | category | Religion | 358 | 0.610699 | 0.647972 | 0.132362 | 0.226234 | 0.659218 | 0.712291 | -0.0530726 | 0.1773 | 0.309254 | 0.608034 | 0.792298 | 0.212086 |
| tossup_correctness | category | Science | 1433 | 0.62028 | 0.668693 | 0.202286 | 0.235446 | 0.619679 | 0.738311 | -0.118632 | 0.166481 | 0.308676 | 0.550222 | 0.742986 | 0.220986 |
| tossup_correctness | category | Social Science | 324 | 0.635579 | 0.650814 | 0.185274 | 0.227956 | 0.645062 | 0.731481 | -0.0864198 | 0.162899 | 0.299095 | 0.566307 | 0.738087 | 0.221329 |
| tossup_correctness | category | Unknown | 1937 | 0.604153 | 0.649935 | 0.19674 | 0.228391 | 0.635003 | 0.758389 | -0.123387 | 0.173055 | 0.313787 | 0.585043 | 0.776108 | 0.216251 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.507178 | 0.775699 | 0.260175 | 0.283323 | 0.532934 | 0.712575 | -0.179641 | 0.170355 | 0.220018 | 0.503139 | 0.690178 | 0.220749 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.621333 | 0.707463 | 0.233845 | 0.252656 | 0.586623 | 0.729167 | -0.142544 | 0.170719 | 0.245976 | 0.512877 | 0.698038 | 0.220833 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.634006 | 0.65774 | 0.210282 | 0.229632 | 0.649173 | 0.755083 | -0.10591 | 0.172617 | 0.296829 | 0.569459 | 0.7504 | 0.218196 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.605088 | 0.640505 | 0.206774 | 0.222748 | 0.656118 | 0.780942 | -0.124824 | 0.172739 | 0.327924 | 0.599218 | 0.778963 | 0.21466 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.604171 | 0.6155 | 0.157868 | 0.212981 | 0.667758 | 0.762029 | -0.0942717 | 0.167281 | 0.36882 | 0.62868 | 0.804609 | 0.211168 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1167 | 0.0823616 | 1.02071 | -3.37277 | -1.51497 | -0.545811 | -0.07716 | 0.751604 | 1.91619 | 3.40057 |
| player | theta_2 | 1167 | -0.0517092 | 1.00643 | -3.3734 | -1.63778 | -0.585232 | -0.141817 | 0.394813 | 1.70856 | 4.6174 |
| player | theta_3 | 1167 | 1.11699 | 1.39431 | -3.72656 | -1.19625 | -0.010319 | 1.311 | 2.21688 | 3.0444 | 4.4936 |
| player | theta_norm | 1167 | 2.05452 | 1.01605 | 0.0713282 | 0.546371 | 1.22903 | 1.99267 | 2.80885 | 3.79547 | 5.01444 |
| tossup | start_difficulty_d1 | 1220 | 1.23819 | 0.722766 | -0.895567 | 0.0673973 | 0.61779 | 1.35005 | 1.79863 | 2.30217 | 2.87754 |
| tossup | start_difficulty_d2 | 1220 | 0.46137 | 0.591548 | -1.77413 | -0.465562 | 0.109201 | 0.42287 | 0.808007 | 1.44051 | 2.78283 |
| tossup | start_difficulty_d3 | 1220 | 1.57325 | 1.13553 | -0.8469 | 0.0512322 | 0.520029 | 1.27125 | 2.65068 | 3.18723 | 3.99967 |
| tossup | end_difficulty_d1 | 1220 | 0.0777804 | 0.545669 | -2.02476 | -0.935075 | -0.318948 | 0.243323 | 0.477143 | 0.791378 | 1.22582 |
| tossup | end_difficulty_d2 | 1220 | -0.46902 | 0.670238 | -3.84168 | -1.54851 | -0.871353 | -0.504834 | -0.0700977 | 0.637355 | 2.11942 |
| tossup | end_difficulty_d3 | 1220 | 0.310827 | 0.815849 | -2.06539 | -0.932926 | -0.396638 | 0.314864 | 1.04539 | 1.48295 | 2.20311 |
| tossup | total_drop_d1 | 1220 | 1.16041 | 0.358232 | 0.5066 | 0.773153 | 0.905921 | 1.02896 | 1.36572 | 1.80568 | 3.47077 |
| tossup | total_drop_d2 | 1220 | 0.93039 | 0.148618 | 0.63299 | 0.770413 | 0.869499 | 0.92594 | 0.980347 | 1.06999 | 4.13476 |
| tossup | total_drop_d3 | 1220 | 1.26242 | 0.506601 | 0.525234 | 0.761005 | 0.881653 | 0.997238 | 1.60054 | 2.22727 | 3.94131 |
| tossup | drop_share_1_d1 | 1220 | 0.20517 | 0.0870724 | 0.0388771 | 0.0881927 | 0.123386 | 0.20032 | 0.286157 | 0.310411 | 0.66406 |
| tossup | drop_share_2_d1 | 1220 | 0.266965 | 0.0974812 | 0.0668687 | 0.110845 | 0.174346 | 0.310783 | 0.343722 | 0.367722 | 0.676904 |
| tossup | drop_share_3_d1 | 1220 | 0.527864 | 0.168894 | 0.134869 | 0.343217 | 0.369548 | 0.494986 | 0.691205 | 0.793903 | 0.883803 |
| tossup | drop_share_1_d2 | 1220 | 0.288818 | 0.021591 | 0.0731396 | 0.251363 | 0.280386 | 0.292045 | 0.3017 | 0.314737 | 0.337083 |
| tossup | drop_share_2_d2 | 1220 | 0.342973 | 0.0147378 | 0.123382 | 0.322837 | 0.335979 | 0.343846 | 0.351714 | 0.362387 | 0.398062 |
| tossup | drop_share_3_d2 | 1220 | 0.368208 | 0.0296704 | 0.32013 | 0.339444 | 0.352252 | 0.363058 | 0.375418 | 0.412452 | 0.803478 |
| tossup | drop_share_1_d3 | 1220 | 0.233159 | 0.0935931 | 0.0353675 | 0.0773092 | 0.144622 | 0.273611 | 0.294551 | 0.319447 | 0.616727 |
| tossup | drop_share_2_d3 | 1220 | 0.297461 | 0.10019 | 0.0430414 | 0.110438 | 0.23287 | 0.334204 | 0.348168 | 0.434974 | 0.770692 |
| tossup | drop_share_3_d3 | 1220 | 0.469381 | 0.16377 | 0.0683511 | 0.325561 | 0.360716 | 0.38457 | 0.578644 | 0.801622 | 0.921591 |
| tossup | r_1 | 1220 | 0.377609 | 0.293622 | 0.0115665 | 0.0192104 | 0.0548163 | 0.427194 | 0.630804 | 0.835481 | 0.915168 |
| tossup | r_2 | 1220 | 0.139702 | 0.128858 | 0.0133074 | 0.0212173 | 0.0471987 | 0.0902837 | 0.182126 | 0.443875 | 0.567425 |
| tossup | r_3 | 1220 | 0.482688 | 0.341643 | 0.0309824 | 0.0509409 | 0.129525 | 0.411548 | 0.845975 | 0.940766 | 0.966228 |
| tossup | r_norm | 1220 | 0.777182 | 0.102217 | 0.585736 | 0.635682 | 0.683472 | 0.765964 | 0.870089 | 0.941744 | 0.966528 |
