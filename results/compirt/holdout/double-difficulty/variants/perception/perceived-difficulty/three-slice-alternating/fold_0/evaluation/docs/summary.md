# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/perceived-difficulty/three-slice-alternating/fold_0/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/perceived-difficulty/three-slice-alternating/fold_0`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 326453 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.599927 |
| log_loss | 0.732452 |
| ece | 0.281189 |
| brier | 0.264226 |
| accuracy | 0.549758 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | -0.215492 |
| probability_std | 0.159985 |
| probability_p10 | 0.255289 |
| probability_p50 | 0.499498 |
| probability_p90 | 0.684203 |
| mean_predictive_variance | 0.224151 |
| integrated_brier_score | 0.0954455 |
| joint_tossup_event_log_loss | 6.86464 |
| buzz_position_mae | 0.139895 |
| buzz_position_median_absolute_error | 0.116492 |
| buzz_position_bias | -0.000969683 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |
| first_buzzer_top1_accuracy | 0.369661 |
| first_buzzer_mean_reciprocal_rank | 0.575914 |
| first_buzzer_log_loss | 1.65801 |
| first_buzzer_events | 9295 |
| neg_auroc | 0.599927 |
| neg_average_precision | 0.304087 |
| neg_precision | 0.285132 |
| neg_recall | 0.609074 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.137678 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.049627 |
| no_buzz_calibration_error | 0.0363573 |
| no_buzz_brier | 0.0196755 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.599927 | 0.732452 | 0.281189 | 0.264226 | 0.549758 | 0.76525 | -0.215492 | 0.159985 | 0.255289 | 0.499498 | 0.684203 | 0.224151 |
| tossup_correctness | tier | fall | 2933 | 0.606184 | 0.776235 | 0.334873 | 0.283174 | 0.50017 | 0.791681 | -0.29151 | 0.161964 | 0.222708 | 0.466916 | 0.660207 | 0.221902 |
| tossup_correctness | tier | nationals | 1584 | 0.578084 | 0.67677 | 0.192615 | 0.240842 | 0.603535 | 0.724747 | -0.121212 | 0.139208 | 0.333646 | 0.54755 | 0.699627 | 0.229564 |
| tossup_correctness | tier | regionals | 1886 | 0.628939 | 0.711371 | 0.255376 | 0.254144 | 0.586426 | 0.746023 | -0.159597 | 0.165716 | 0.253058 | 0.51317 | 0.698143 | 0.222451 |
| tossup_correctness | tier | winter | 2892 | 0.6127 | 0.732295 | 0.292304 | 0.264392 | 0.54668 | 0.773167 | -0.226487 | 0.158298 | 0.260637 | 0.489894 | 0.683538 | 0.224575 |
| tossup_correctness | category | Current Events | 124 | 0.591051 | 0.789791 | 0.306096 | 0.289306 | 0.491935 | 0.75 | -0.258065 | 0.173111 | 0.213296 | 0.456906 | 0.685519 | 0.217614 |
| tossup_correctness | category | Fine Arts | 1103 | 0.61386 | 0.722118 | 0.272745 | 0.259388 | 0.566636 | 0.759746 | -0.19311 | 0.162231 | 0.249481 | 0.502436 | 0.685177 | 0.223512 |
| tossup_correctness | category | Geography | 197 | 0.525058 | 0.817638 | 0.247909 | 0.302356 | 0.477157 | 0.670051 | -0.192893 | 0.165598 | 0.205524 | 0.420059 | 0.642835 | 0.216702 |
| tossup_correctness | category | History | 1491 | 0.624009 | 0.733865 | 0.312711 | 0.265951 | 0.538565 | 0.787391 | -0.248826 | 0.152738 | 0.258337 | 0.490843 | 0.666648 | 0.22603 |
| tossup_correctness | category | Literature | 1472 | 0.577345 | 0.704321 | 0.286417 | 0.251095 | 0.58288 | 0.804348 | -0.221467 | 0.157136 | 0.299055 | 0.539207 | 0.70624 | 0.224987 |
| tossup_correctness | category | Mythology | 332 | 0.576464 | 0.768404 | 0.338376 | 0.278987 | 0.548193 | 0.813253 | -0.26506 | 0.159496 | 0.241131 | 0.503408 | 0.666066 | 0.223946 |
| tossup_correctness | category | Other Academic | 69 | 0.578054 | 0.701605 | 0.260051 | 0.253561 | 0.507246 | 0.753623 | -0.246377 | 0.150355 | 0.288242 | 0.520295 | 0.665113 | 0.227392 |
| tossup_correctness | category | Philosophy | 324 | 0.539412 | 0.700626 | 0.273459 | 0.250683 | 0.567901 | 0.799383 | -0.231481 | 0.149737 | 0.335072 | 0.538471 | 0.706949 | 0.226907 |
| tossup_correctness | category | Popular Culture | 102 | 0.509343 | 0.986388 | 0.462467 | 0.372855 | 0.343137 | 0.833333 | -0.490196 | 0.154782 | 0.165499 | 0.373643 | 0.574505 | 0.20978 |
| tossup_correctness | category | Religion | 372 | 0.60564 | 0.73385 | 0.235196 | 0.264196 | 0.545699 | 0.709677 | -0.163978 | 0.153768 | 0.261976 | 0.482814 | 0.676948 | 0.225704 |
| tossup_correctness | category | Science | 1487 | 0.570766 | 0.759907 | 0.285784 | 0.277167 | 0.502354 | 0.752522 | -0.250168 | 0.152638 | 0.256486 | 0.474303 | 0.664143 | 0.225595 |
| tossup_correctness | category | Social Science | 336 | 0.601992 | 0.731934 | 0.237789 | 0.265415 | 0.526786 | 0.702381 | -0.175595 | 0.158269 | 0.237051 | 0.48131 | 0.667013 | 0.223697 |
| tossup_correctness | category | Unknown | 1886 | 0.628939 | 0.711371 | 0.255376 | 0.254144 | 0.586426 | 0.746023 | -0.159597 | 0.165716 | 0.253058 | 0.51317 | 0.698143 | 0.222451 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.644695 | 0.82581 | 0.343764 | 0.305266 | 0.446701 | 0.736041 | -0.28934 | 0.146635 | 0.19157 | 0.38565 | 0.589214 | 0.216894 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.600384 | 0.817221 | 0.321593 | 0.300778 | 0.470051 | 0.735025 | -0.264975 | 0.151548 | 0.203676 | 0.417746 | 0.605573 | 0.219539 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.582424 | 0.770669 | 0.311293 | 0.281281 | 0.493558 | 0.769436 | -0.275877 | 0.152557 | 0.242454 | 0.469112 | 0.649068 | 0.224974 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.615621 | 0.724697 | 0.295391 | 0.26058 | 0.564899 | 0.78402 | -0.219121 | 0.159302 | 0.258403 | 0.50563 | 0.689983 | 0.224494 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.598099 | 0.677148 | 0.227588 | 0.240185 | 0.610481 | 0.756008 | -0.145527 | 0.154902 | 0.301534 | 0.551229 | 0.714204 | 0.225198 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1186 | 0.304947 | 0.955705 | -1.80205 | -1.23703 | -0.403399 | 0.298934 | 0.942237 | 1.94774 | 2.92051 |
| player | theta_2 | 1186 | 0.172142 | 0.849135 | -1.97272 | -1.19167 | -0.467648 | 0.141184 | 0.832761 | 1.53255 | 2.53574 |
| player | theta_3 | 1186 | 0.243503 | 0.892204 | -1.89442 | -1.16109 | -0.460883 | 0.230755 | 0.898443 | 1.71883 | 2.51847 |
| player | theta_norm | 1186 | 1.46042 | 0.691297 | 0.132643 | 0.474348 | 0.914826 | 1.37 | 1.9423 | 2.69287 | 3.68746 |
| tossup | start_difficulty_d1 | 1240 | 1.63587 | 0.359518 | 0.0523026 | 1.0026 | 1.44466 | 1.66604 | 1.87004 | 2.16547 | 2.76945 |
| tossup | start_difficulty_d2 | 1240 | 1.5683 | 0.367287 | -0.268216 | 0.887346 | 1.37454 | 1.61079 | 1.80788 | 2.08521 | 2.45601 |
| tossup | start_difficulty_d3 | 1240 | 1.53952 | 0.350926 | 0.215772 | 0.86746 | 1.35869 | 1.57442 | 1.78336 | 2.05378 | 2.687 |
| tossup | end_difficulty_d1 | 1240 | 0.457614 | 0.4005 | -1.6203 | -0.274246 | 0.259122 | 0.475038 | 0.703786 | 1.05364 | 1.50534 |
| tossup | end_difficulty_d2 | 1240 | 0.269755 | 0.400843 | -1.79833 | -0.479209 | 0.0779541 | 0.323911 | 0.537899 | 0.824736 | 1.28125 |
| tossup | end_difficulty_d3 | 1240 | 0.465471 | 0.42096 | -1.58133 | -0.26691 | 0.233837 | 0.522747 | 0.747673 | 1.05714 | 1.6793 |
| tossup | total_drop_d1 | 1240 | 1.17826 | 0.395278 | 0.485906 | 0.724479 | 0.861685 | 1.08131 | 1.42145 | 1.91194 | 3.19897 |
| tossup | total_drop_d2 | 1240 | 1.29855 | 0.466697 | 0.516837 | 0.744751 | 0.923917 | 1.22166 | 1.58874 | 2.11563 | 4.01014 |
| tossup | total_drop_d3 | 1240 | 1.07404 | 0.342802 | 0.488577 | 0.719089 | 0.844608 | 0.976348 | 1.21638 | 1.72769 | 2.98149 |
| tossup | drop_share_1_d1 | 1240 | 0.199951 | 0.0619708 | 0.0531066 | 0.103261 | 0.151451 | 0.201284 | 0.245087 | 0.289576 | 0.45825 |
| tossup | drop_share_2_d1 | 1240 | 0.272511 | 0.0713175 | 0.0570127 | 0.137727 | 0.231108 | 0.288008 | 0.321383 | 0.35925 | 0.535107 |
| tossup | drop_share_3_d1 | 1240 | 0.527538 | 0.12228 | 0.19968 | 0.370798 | 0.432829 | 0.503758 | 0.61289 | 0.748568 | 0.87507 |
| tossup | drop_share_1_d2 | 1240 | 0.194619 | 0.0645182 | 0.046559 | 0.0991239 | 0.140469 | 0.192655 | 0.249092 | 0.295486 | 0.469039 |
| tossup | drop_share_2_d2 | 1240 | 0.267476 | 0.0731075 | 0.0756374 | 0.138331 | 0.214307 | 0.28076 | 0.323704 | 0.359173 | 0.576566 |
| tossup | drop_share_3_d2 | 1240 | 0.537905 | 0.12869 | 0.152416 | 0.368458 | 0.42384 | 0.526823 | 0.635112 | 0.759165 | 0.873233 |
| tossup | drop_share_1_d3 | 1240 | 0.219378 | 0.053075 | 0.0572839 | 0.119976 | 0.1851 | 0.227807 | 0.256423 | 0.290872 | 0.431314 |
| tossup | drop_share_2_d3 | 1240 | 0.291858 | 0.0576931 | 0.0638547 | 0.167029 | 0.268611 | 0.305214 | 0.327903 | 0.356032 | 0.498295 |
| tossup | drop_share_3_d3 | 1240 | 0.488765 | 0.100468 | 0.22577 | 0.375202 | 0.415708 | 0.463801 | 0.538248 | 0.703697 | 0.876758 |
| tossup | r_1 | 1240 | 0.385724 | 0.21277 | 0.0333096 | 0.0779591 | 0.210537 | 0.36744 | 0.543801 | 0.762664 | 0.928536 |
| tossup | r_2 | 1240 | 0.33034 | 0.185173 | 0.0226178 | 0.0600077 | 0.180745 | 0.308631 | 0.468242 | 0.665473 | 0.849267 |
| tossup | r_3 | 1240 | 0.283936 | 0.171215 | 0.0379003 | 0.0685322 | 0.145797 | 0.247163 | 0.386887 | 0.618885 | 0.895647 |
| tossup | r_norm | 1240 | 0.665504 | 0.0664973 | 0.577664 | 0.585814 | 0.61695 | 0.649699 | 0.698586 | 0.80045 | 0.929961 |
