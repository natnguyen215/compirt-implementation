# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/model-components/relevance-locations-terminal/dd-bernstein-332-simplex-locations-terminal/fold_2/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/model-components/relevance-locations-terminal/dd-bernstein-332-simplex-locations-terminal/fold_2`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 283281 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.715073 |
| log_loss | 0.491436 |
| ece | 0.0125304 |
| brier | 0.159932 |
| accuracy | 0.774333 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | 0.0101545 |
| probability_std | 0.139528 |
| probability_p10 | 0.583954 |
| probability_p50 | 0.811001 |
| probability_p90 | 0.917105 |
| mean_predictive_variance | 0.154806 |
| integrated_brier_score | 0.102703 |
| joint_tossup_event_log_loss | 6.63341 |
| buzz_position_mae | 0.152461 |
| buzz_position_median_absolute_error | 0.134024 |
| buzz_position_bias | -0.0435125 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.350654 |
| first_buzzer_mean_reciprocal_rank | 0.565318 |
| first_buzzer_log_loss | 1.66911 |
| first_buzzer_events | 9257 |
| neg_auroc | 0.715073 |
| neg_average_precision | 0.448449 |
| neg_precision | 0.597917 |
| neg_recall | 0.13147 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.190914 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0139609 |
| no_buzz_calibration_error | 0.000847844 |
| no_buzz_brier | 0.0128568 |
| full_pmf_max_mass_error | 1.55431e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.715073 | 0.491436 | 0.0125304 | 0.159932 | 0.774333 | 0.764178 | 0.0101545 | 0.139528 | 0.583954 | 0.811001 | 0.917105 | 0.154806 |
| tossup_correctness | tier | fall | 2798 | 0.741338 | 0.456664 | 0.0211386 | 0.146374 | 0.794139 | 0.785204 | 0.00893495 | 0.140562 | 0.584277 | 0.821208 | 0.920639 | 0.151249 |
| tossup_correctness | tier | nationals | 1545 | 0.713963 | 0.536228 | 0.0464944 | 0.178467 | 0.744337 | 0.721036 | 0.023301 | 0.142607 | 0.570977 | 0.794296 | 0.911907 | 0.161083 |
| tossup_correctness | tier | regionals | 2039 | 0.708368 | 0.496899 | 0.0142396 | 0.162055 | 0.771457 | 0.762138 | 0.00931829 | 0.132416 | 0.584789 | 0.803793 | 0.914335 | 0.157809 |
| tossup_correctness | tier | winter | 2875 | 0.692259 | 0.497331 | 0.0193926 | 0.16166 | 0.773217 | 0.768348 | 0.00486957 | 0.141252 | 0.594342 | 0.813513 | 0.91752 | 0.152764 |
| tossup_correctness | category | Current Events | 129 | 0.692537 | 0.606658 | 0.0964187 | 0.208678 | 0.682171 | 0.666667 | 0.0155039 | 0.148952 | 0.51833 | 0.786334 | 0.926071 | 0.162145 |
| tossup_correctness | category | Fine Arts | 1074 | 0.710961 | 0.475248 | 0.0225313 | 0.152583 | 0.795158 | 0.776536 | 0.018622 | 0.15209 | 0.573838 | 0.79981 | 0.916681 | 0.157431 |
| tossup_correctness | category | Geography | 180 | 0.754276 | 0.563922 | 0.0783357 | 0.190503 | 0.727778 | 0.616667 | 0.111111 | 0.229061 | 0.232107 | 0.772512 | 0.911369 | 0.162319 |
| tossup_correctness | category | History | 1454 | 0.695997 | 0.508625 | 0.0227611 | 0.166509 | 0.765475 | 0.757909 | 0.00756534 | 0.138133 | 0.574204 | 0.812199 | 0.921517 | 0.154206 |
| tossup_correctness | category | Literature | 1435 | 0.729092 | 0.432391 | 0.027451 | 0.135396 | 0.816028 | 0.810453 | 0.00557491 | 0.118672 | 0.644951 | 0.843395 | 0.924585 | 0.139428 |
| tossup_correctness | category | Mythology | 324 | 0.684535 | 0.47585 | 0.0327682 | 0.152321 | 0.780864 | 0.79321 | -0.0123457 | 0.113043 | 0.669119 | 0.838066 | 0.91804 | 0.141845 |
| tossup_correctness | category | Other Academic | 71 | 0.592593 | 0.548252 | 0.0987533 | 0.177605 | 0.760563 | 0.760563 | 0 | 0.10597 | 0.646575 | 0.807967 | 0.901043 | 0.159484 |
| tossup_correctness | category | Philosophy | 310 | 0.726466 | 0.490118 | 0.0297229 | 0.160801 | 0.770968 | 0.76129 | 0.00967742 | 0.118378 | 0.622423 | 0.799541 | 0.916723 | 0.157847 |
| tossup_correctness | category | Popular Culture | 108 | 0.499132 | 0.372308 | 0.111045 | 0.106227 | 0.888889 | 0.888889 | 0 | 0.0738729 | 0.744983 | 0.85004 | 0.91544 | 0.129463 |
| tossup_correctness | category | Religion | 361 | 0.68095 | 0.533175 | 0.0214046 | 0.177601 | 0.736842 | 0.742382 | -0.00554017 | 0.139897 | 0.534768 | 0.756693 | 0.888395 | 0.174654 |
| tossup_correctness | category | Science | 1445 | 0.722508 | 0.508838 | 0.0290266 | 0.168365 | 0.756401 | 0.746021 | 0.0103806 | 0.136404 | 0.580007 | 0.800029 | 0.908241 | 0.159673 |
| tossup_correctness | category | Social Science | 327 | 0.735245 | 0.528592 | 0.0545658 | 0.177039 | 0.724771 | 0.718654 | 0.00611621 | 0.176086 | 0.473033 | 0.780253 | 0.913347 | 0.164475 |
| tossup_correctness | category | Unknown | 2039 | 0.708368 | 0.496899 | 0.0142396 | 0.162055 | 0.771457 | 0.762138 | 0.00931829 | 0.132416 | 0.584789 | 0.803793 | 0.914335 | 0.157809 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.659105 | 0.539586 | 0.064625 | 0.181439 | 0.73224 | 0.743169 | -0.010929 | 0.142916 | 0.531075 | 0.770318 | 0.897327 | 0.172417 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.72304 | 0.522694 | 0.0278894 | 0.173319 | 0.743455 | 0.728796 | 0.0146597 | 0.143034 | 0.554594 | 0.789889 | 0.906738 | 0.16413 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.730679 | 0.494696 | 0.0260164 | 0.161577 | 0.767753 | 0.752568 | 0.0151854 | 0.141455 | 0.58684 | 0.81024 | 0.913847 | 0.154682 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.710054 | 0.471073 | 0.015676 | 0.151748 | 0.791304 | 0.786087 | 0.00521739 | 0.12561 | 0.623576 | 0.82536 | 0.920572 | 0.147527 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.705718 | 0.495623 | 0.0186438 | 0.160972 | 0.775374 | 0.764393 | 0.0109817 | 0.146894 | 0.557825 | 0.802203 | 0.918564 | 0.157826 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1197 | 2.65478 | 0.738728 | 0.583797 | 1.446 | 2.16841 | 2.63709 | 3.15679 | 3.91689 | 4.57669 |
| player | theta_1 | 1197 | -1.20663 | 0.832647 | -3.55505 | -2.50508 | -1.76467 | -1.24216 | -0.728298 | 0.256412 | 1.84895 |
| player | theta_2 | 1197 | -0.982232 | 0.615099 | -3.19489 | -2.01928 | -1.37374 | -0.994191 | -0.604303 | 0.0214232 | 1.42856 |
| player | theta_3 | 1197 | -1.10005 | 0.764283 | -3.2298 | -2.25247 | -1.59866 | -1.16743 | -0.658519 | 0.262165 | 1.90122 |
| player | theta_norm | 1197 | 2.21322 | 0.622274 | 0.381377 | 1.25781 | 1.76436 | 2.17603 | 2.62569 | 3.25213 | 4.29692 |
| tossup | start_difficulty_d1 | 1240 | -1.77552 | 0.545569 | -3.54262 | -2.55196 | -2.13644 | -1.8413 | -1.47347 | -0.818617 | 1.09894 |
| tossup | start_difficulty_d2 | 1240 | -1.76609 | 0.500561 | -3.31817 | -2.52053 | -2.10539 | -1.8007 | -1.4469 | -0.908235 | 0.350357 |
| tossup | start_difficulty_d3 | 1240 | -1.7701 | 0.508789 | -3.54428 | -2.54687 | -2.12271 | -1.79955 | -1.44805 | -0.899657 | 0.0919928 |
| tossup | end_difficulty_d1 | 1240 | -2.76299 | 0.636751 | -4.64598 | -3.67295 | -3.17543 | -2.83943 | -2.41452 | -1.64241 | 0.40279 |
| tossup | end_difficulty_d2 | 1240 | -2.75151 | 0.586866 | -4.6244 | -3.63517 | -3.14683 | -2.79078 | -2.37448 | -1.7589 | -0.339066 |
| tossup | end_difficulty_d3 | 1240 | -2.75405 | 0.59317 | -4.82996 | -3.66258 | -3.16477 | -2.79352 | -2.37599 | -1.75437 | -0.663209 |
| tossup | total_drop_d1 | 1240 | 0.987475 | 0.112139 | 0.60107 | 0.799073 | 0.912047 | 0.991677 | 1.06519 | 1.14954 | 1.631 |
| tossup | total_drop_d2 | 1240 | 0.985425 | 0.102763 | 0.662815 | 0.823742 | 0.913836 | 0.985855 | 1.05586 | 1.16113 | 1.34137 |
| tossup | total_drop_d3 | 1240 | 0.983948 | 0.102272 | 0.649702 | 0.817465 | 0.908867 | 0.984845 | 1.05133 | 1.15853 | 1.28568 |
| tossup | drop_share_1_d1 | 1240 | 0.304056 | 0.0154254 | 0.230932 | 0.278776 | 0.29456 | 0.303834 | 0.314886 | 0.327452 | 0.364799 |
| tossup | drop_share_2_d1 | 1240 | 0.347015 | 0.0114631 | 0.306476 | 0.328122 | 0.339395 | 0.347213 | 0.354871 | 0.365141 | 0.387116 |
| tossup | drop_share_3_d1 | 1240 | 0.348929 | 0.0164715 | 0.299136 | 0.323855 | 0.338016 | 0.348738 | 0.359395 | 0.375331 | 0.419407 |
| tossup | drop_share_1_d2 | 1240 | 0.303677 | 0.014015 | 0.244925 | 0.280872 | 0.294583 | 0.303743 | 0.313186 | 0.327082 | 0.344511 |
| tossup | drop_share_2_d2 | 1240 | 0.346953 | 0.0113485 | 0.310763 | 0.32832 | 0.339439 | 0.346883 | 0.354738 | 0.365682 | 0.385672 |
| tossup | drop_share_3_d2 | 1240 | 0.34937 | 0.0151336 | 0.302981 | 0.325393 | 0.339186 | 0.349371 | 0.359367 | 0.37362 | 0.40999 |
| tossup | drop_share_1_d3 | 1240 | 0.303607 | 0.0147293 | 0.244486 | 0.279708 | 0.294064 | 0.303943 | 0.313722 | 0.326876 | 0.357108 |
| tossup | drop_share_2_d3 | 1240 | 0.347164 | 0.0111675 | 0.311125 | 0.329218 | 0.339843 | 0.346756 | 0.354462 | 0.36571 | 0.385224 |
| tossup | drop_share_3_d3 | 1240 | 0.349229 | 0.0153738 | 0.309548 | 0.324992 | 0.338667 | 0.348845 | 0.359167 | 0.375477 | 0.412559 |
| tossup | r_1 | 1240 | 0.322 | 0.145478 | 0.0694062 | 0.132516 | 0.211752 | 0.290256 | 0.408408 | 0.617612 | 0.863206 |
| tossup | r_2 | 1240 | 0.332969 | 0.110581 | 0.0667223 | 0.163989 | 0.258677 | 0.325825 | 0.395308 | 0.543378 | 0.696086 |
| tossup | r_3 | 1240 | 0.345031 | 0.122849 | 0.0692567 | 0.160428 | 0.253918 | 0.336215 | 0.416533 | 0.561198 | 0.804211 |
| tossup | r_norm | 1240 | 0.61666 | 0.0421425 | 0.577352 | 0.579425 | 0.587772 | 0.602165 | 0.629507 | 0.709188 | 0.86861 |
| tossup_hazard | hazard_start_difficulty_d1 | 1240 | 4.48588 | 0.489674 | 2.03879 | 3.74984 | 4.21089 | 4.44286 | 4.71718 | 5.38706 | 6.2085 |
| tossup_hazard | hazard_start_difficulty_d2 | 1240 | 4.45761 | 0.426764 | 2.47131 | 3.768 | 4.22327 | 4.44013 | 4.67568 | 5.15453 | 6.70744 |
| tossup_hazard | hazard_start_difficulty_d3 | 1240 | 4.46835 | 0.438611 | 2.31024 | 3.76467 | 4.22671 | 4.44912 | 4.70388 | 5.27434 | 6.10823 |
| tossup_hazard | hazard_end_difficulty_d1 | 1240 | 1.74933 | 2.33063 | -10.9627 | -3.20076 | 0.670064 | 2.86835 | 3.29343 | 3.6568 | 4.35327 |
| tossup_hazard | hazard_end_difficulty_d2 | 1240 | 2.3472 | 1.96638 | -8.72625 | -2.28196 | 2.4003 | 3.11333 | 3.40424 | 3.72477 | 4.26653 |
| tossup_hazard | hazard_end_difficulty_d3 | 1240 | 2.17358 | 2.1704 | -10.8316 | -2.55989 | 2.14283 | 3.07142 | 3.38408 | 3.73834 | 4.2009 |
| tossup_hazard | hazard_total_drop_d1 | 1240 | 2.73656 | 2.4966 | 0.885835 | 0.987162 | 1.06607 | 1.36189 | 3.92194 | 8.12155 | 15.4952 |
| tossup_hazard | hazard_total_drop_d2 | 1240 | 2.11041 | 2.10885 | 0.88039 | 0.961558 | 1.02572 | 1.17831 | 1.80198 | 6.88422 | 13.8245 |
| tossup_hazard | hazard_total_drop_d3 | 1240 | 2.29477 | 2.31114 | 0.8567 | 0.969721 | 1.03423 | 1.21013 | 2.12579 | 7.41155 | 15.537 |
| tossup_hazard | hazard_drop_share_1_d1 | 1240 | 0.235943 | 0.0789597 | 0.0439498 | 0.082623 | 0.180889 | 0.269256 | 0.294082 | 0.315813 | 0.540239 |
| tossup_hazard | hazard_drop_share_2_d1 | 1240 | 0.344931 | 0.0749154 | 0.0676715 | 0.191236 | 0.335717 | 0.351625 | 0.366745 | 0.443897 | 0.683639 |
| tossup_hazard | hazard_drop_share_3_d1 | 1240 | 0.419126 | 0.126764 | 0.110565 | 0.303786 | 0.348126 | 0.369673 | 0.440286 | 0.714938 | 0.88256 |
| tossup_hazard | hazard_drop_share_1_d2 | 1240 | 0.25414 | 0.068174 | 0.0280305 | 0.100199 | 0.236875 | 0.278625 | 0.295998 | 0.314231 | 0.615923 |
| tossup_hazard | hazard_drop_share_2_d2 | 1240 | 0.34852 | 0.0613173 | 0.0641133 | 0.240675 | 0.340747 | 0.351226 | 0.36381 | 0.41145 | 0.691691 |
| tossup_hazard | hazard_drop_share_3_d2 | 1240 | 0.39734 | 0.103494 | 0.10395 | 0.31825 | 0.350366 | 0.365198 | 0.397079 | 0.651572 | 0.889985 |
| tossup_hazard | hazard_drop_share_1_d3 | 1240 | 0.249267 | 0.0705627 | 0.0407691 | 0.0894816 | 0.225786 | 0.275617 | 0.296596 | 0.313253 | 0.533376 |
| tossup_hazard | hazard_drop_share_2_d3 | 1240 | 0.347951 | 0.0583292 | 0.0885651 | 0.229558 | 0.340092 | 0.3513 | 0.365168 | 0.424124 | 0.706198 |
| tossup_hazard | hazard_drop_share_3_d3 | 1240 | 0.402782 | 0.107287 | 0.0607708 | 0.321418 | 0.349703 | 0.368129 | 0.405652 | 0.673263 | 0.865574 |
| tossup_hazard | hazard_r_1 | 1240 | 0.384477 | 0.274001 | 0.0283846 | 0.0646797 | 0.137453 | 0.308096 | 0.610779 | 0.863605 | 0.945249 |
| tossup_hazard | hazard_r_2 | 1240 | 0.29108 | 0.201466 | 0.0243623 | 0.0560042 | 0.120767 | 0.234124 | 0.428371 | 0.682779 | 0.826413 |
| tossup_hazard | hazard_r_3 | 1240 | 0.324443 | 0.236006 | 0.0224653 | 0.052398 | 0.129003 | 0.252412 | 0.488187 | 0.790833 | 0.925423 |
