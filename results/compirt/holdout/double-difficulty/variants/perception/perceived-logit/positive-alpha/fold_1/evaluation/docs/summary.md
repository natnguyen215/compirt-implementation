# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/perceived-logit/positive-alpha/fold_1/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/perceived-logit/positive-alpha/fold_1`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 302834 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.601715 |
| log_loss | 0.784413 |
| ece | 0.338711 |
| brier | 0.293014 |
| accuracy | 0.384142 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.377983 |
| probability_std | 0.09832 |
| probability_p10 | 0.296978 |
| probability_p50 | 0.422684 |
| probability_p90 | 0.548682 |
| mean_predictive_variance | 0.23447 |
| integrated_brier_score | 0.0926069 |
| joint_tossup_event_log_loss | 6.73927 |
| buzz_position_mae | 0.136742 |
| buzz_position_median_absolute_error | 0.115431 |
| buzz_position_bias | -0.00951106 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |
| first_buzzer_top1_accuracy | 0.39173 |
| first_buzzer_mean_reciprocal_rank | 0.597909 |
| first_buzzer_log_loss | 1.60232 |
| first_buzzer_events | 9093 |
| neg_auroc | 0.601715 |
| neg_average_precision | 0.315142 |
| neg_precision | 0.259415 |
| neg_recall | 0.856681 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.128574 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.052657 |
| no_buzz_calibration_error | 0.0367479 |
| no_buzz_brier | 0.0221619 |
| full_pmf_max_mass_error | 1.55431e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.601715 | 0.784413 | 0.338711 | 0.293014 | 0.384142 | 0.762125 | -0.377983 | 0.09832 | 0.296978 | 0.422684 | 0.548682 | 0.23447 |
| tossup_correctness | tier | fall | 2842 | 0.621834 | 0.786397 | 0.361529 | 0.294376 | 0.364532 | 0.785362 | -0.42083 | 0.0914672 | 0.306124 | 0.423596 | 0.540375 | 0.235832 |
| tossup_correctness | tier | nationals | 1564 | 0.571176 | 0.76904 | 0.287608 | 0.285214 | 0.423913 | 0.718031 | -0.294118 | 0.106496 | 0.292168 | 0.433276 | 0.564125 | 0.23386 |
| tossup_correctness | tier | regionals | 1937 | 0.607735 | 0.769401 | 0.325175 | 0.285695 | 0.426433 | 0.758389 | -0.331957 | 0.106725 | 0.294041 | 0.431505 | 0.564855 | 0.23416 |
| tossup_correctness | tier | winter | 2750 | 0.604809 | 0.801681 | 0.353901 | 0.301199 | 0.352 | 0.765818 | -0.413818 | 0.0928071 | 0.293026 | 0.412158 | 0.531214 | 0.233628 |
| tossup_correctness | category | Current Events | 126 | 0.596872 | 0.823926 | 0.370566 | 0.311091 | 0.349206 | 0.769841 | -0.420635 | 0.0910904 | 0.283197 | 0.402874 | 0.516318 | 0.231557 |
| tossup_correctness | category | Fine Arts | 1071 | 0.616234 | 0.799196 | 0.355501 | 0.300165 | 0.365079 | 0.766573 | -0.401494 | 0.0991833 | 0.284537 | 0.40677 | 0.540754 | 0.232255 |
| tossup_correctness | category | Geography | 185 | 0.563953 | 0.804512 | 0.309534 | 0.302165 | 0.372973 | 0.697297 | -0.324324 | 0.0950311 | 0.284332 | 0.396363 | 0.52509 | 0.230038 |
| tossup_correctness | category | History | 1440 | 0.608089 | 0.773332 | 0.32686 | 0.288118 | 0.384028 | 0.754167 | -0.370139 | 0.0926472 | 0.307546 | 0.426385 | 0.544472 | 0.236181 |
| tossup_correctness | category | Literature | 1422 | 0.565316 | 0.796614 | 0.378888 | 0.298126 | 0.38045 | 0.814346 | -0.433896 | 0.103327 | 0.295033 | 0.438476 | 0.563882 | 0.235158 |
| tossup_correctness | category | Mythology | 318 | 0.562883 | 0.827442 | 0.384004 | 0.314007 | 0.295597 | 0.789308 | -0.493711 | 0.0838302 | 0.305298 | 0.402502 | 0.516728 | 0.234005 |
| tossup_correctness | category | Other Academic | 66 | 0.723404 | 0.761184 | 0.325287 | 0.283181 | 0.409091 | 0.712121 | -0.30303 | 0.0980635 | 0.270264 | 0.382111 | 0.521966 | 0.2289 |
| tossup_correctness | category | Philosophy | 311 | 0.659374 | 0.771797 | 0.330401 | 0.286759 | 0.401929 | 0.745981 | -0.344051 | 0.0993603 | 0.288913 | 0.421476 | 0.544064 | 0.233001 |
| tossup_correctness | category | Popular Culture | 102 | 0.386111 | 0.948906 | 0.501296 | 0.370116 | 0.147059 | 0.882353 | -0.735294 | 0.0836445 | 0.256094 | 0.381712 | 0.492786 | 0.228856 |
| tossup_correctness | category | Religion | 358 | 0.614544 | 0.76412 | 0.293467 | 0.283438 | 0.407821 | 0.712291 | -0.304469 | 0.0960562 | 0.302673 | 0.42373 | 0.548241 | 0.234587 |
| tossup_correctness | category | Science | 1433 | 0.605497 | 0.776353 | 0.317897 | 0.289499 | 0.381717 | 0.738311 | -0.356595 | 0.0901517 | 0.306232 | 0.419846 | 0.537624 | 0.235629 |
| tossup_correctness | category | Social Science | 324 | 0.606528 | 0.775061 | 0.314278 | 0.289467 | 0.354938 | 0.731481 | -0.376543 | 0.0832865 | 0.304177 | 0.420516 | 0.522161 | 0.236208 |
| tossup_correctness | category | Unknown | 1937 | 0.607735 | 0.769401 | 0.325175 | 0.285695 | 0.426433 | 0.758389 | -0.331957 | 0.106725 | 0.294041 | 0.431505 | 0.564855 | 0.23416 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.594188 | 0.936589 | 0.407059 | 0.361176 | 0.281437 | 0.712575 | -0.431138 | 0.0907645 | 0.200401 | 0.314382 | 0.429868 | 0.207032 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.5946 | 0.889628 | 0.382435 | 0.340376 | 0.309211 | 0.729167 | -0.419956 | 0.089483 | 0.236321 | 0.346588 | 0.456439 | 0.218553 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.628016 | 0.828285 | 0.36687 | 0.313732 | 0.321986 | 0.755083 | -0.433097 | 0.0903316 | 0.275642 | 0.383903 | 0.504316 | 0.229344 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.608043 | 0.785054 | 0.354528 | 0.293894 | 0.361814 | 0.780942 | -0.419128 | 0.0892712 | 0.313605 | 0.423115 | 0.539067 | 0.236616 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.604741 | 0.713716 | 0.28826 | 0.259988 | 0.475941 | 0.762029 | -0.286088 | 0.0839294 | 0.369482 | 0.469398 | 0.584159 | 0.242274 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | alpha | 1167 | 5.12367 | 1.57488 | 1.71501 | 3.53462 | 4.21456 | 4.74788 | 5.53698 | 7.62162 | 14.3765 |
| player | beta | 1167 | -2.88856 | 0.830172 | -6.39792 | -4.33786 | -3.39468 | -2.78691 | -2.30972 | -1.69895 | -0.912534 |
| player | theta_1 | 1167 | -1.61454 | 0.557018 | -4.13728 | -2.5257 | -1.96013 | -1.61151 | -1.24991 | -0.731744 | 0.217146 |
| player | theta_2 | 1167 | -1.63032 | 0.627116 | -3.75019 | -2.55423 | -2.03751 | -1.68541 | -1.284 | -0.462292 | 0.488123 |
| player | theta_3 | 1167 | -1.49186 | 0.561395 | -3.10566 | -2.38621 | -1.87624 | -1.49376 | -1.11812 | -0.553388 | 0.719416 |
| player | theta_norm | 1167 | 2.86916 | 0.525682 | 0.743629 | 1.95552 | 2.53082 | 2.90339 | 3.23769 | 3.6893 | 4.58918 |
| tossup | start_difficulty_d1 | 1220 | 0.142527 | 0.31813 | -0.992962 | -0.408599 | -0.0608174 | 0.149874 | 0.354921 | 0.646013 | 1.16534 |
| tossup | start_difficulty_d2 | 1220 | 0.167414 | 0.307024 | -0.996158 | -0.337122 | -0.0381923 | 0.175133 | 0.380608 | 0.647865 | 1.12629 |
| tossup | start_difficulty_d3 | 1220 | 0.175105 | 0.305764 | -0.892369 | -0.342698 | -0.03378 | 0.191241 | 0.380649 | 0.654134 | 1.22987 |
| tossup | end_difficulty_d1 | 1220 | -1.36525 | 0.575924 | -3.96526 | -2.26684 | -1.71551 | -1.41036 | -0.953338 | -0.418713 | -0.0193865 |
| tossup | end_difficulty_d2 | 1220 | -1.25406 | 0.512661 | -3.78057 | -2.03131 | -1.6066 | -1.29732 | -0.875407 | -0.397114 | 0.07759 |
| tossup | end_difficulty_d3 | 1220 | -1.14541 | 0.525057 | -3.54804 | -1.98998 | -1.472 | -1.14806 | -0.758443 | -0.317077 | 0.372392 |
| tossup | total_drop_d1 | 1220 | 1.50777 | 0.542421 | 0.543097 | 0.884816 | 1.05778 | 1.42549 | 1.83505 | 2.43903 | 4.9611 |
| tossup | total_drop_d2 | 1220 | 1.42148 | 0.487512 | 0.536663 | 0.873052 | 0.971268 | 1.33688 | 1.75409 | 2.2995 | 4.69167 |
| tossup | total_drop_d3 | 1220 | 1.32052 | 0.452427 | 0.724997 | 0.869861 | 0.958882 | 1.18087 | 1.54803 | 2.20624 | 3.74843 |
| tossup | drop_share_1_d1 | 1220 | 0.259272 | 0.0947391 | 0.0467266 | 0.131383 | 0.197581 | 0.255633 | 0.294548 | 0.463024 | 0.737565 |
| tossup | drop_share_2_d1 | 1220 | 0.273666 | 0.0643223 | 0.0760686 | 0.152512 | 0.230296 | 0.286132 | 0.324412 | 0.353953 | 0.503161 |
| tossup | drop_share_3_d1 | 1220 | 0.467062 | 0.123822 | 0.0858488 | 0.287947 | 0.380582 | 0.442228 | 0.550743 | 0.695013 | 0.874068 |
| tossup | drop_share_1_d2 | 1220 | 0.250726 | 0.0786494 | 0.0602468 | 0.134046 | 0.199227 | 0.253395 | 0.29122 | 0.376011 | 0.717018 |
| tossup | drop_share_2_d2 | 1220 | 0.276763 | 0.0669528 | 0.0656429 | 0.152539 | 0.231183 | 0.291843 | 0.329876 | 0.354894 | 0.565331 |
| tossup | drop_share_3_d2 | 1220 | 0.472511 | 0.117158 | 0.0841011 | 0.325909 | 0.381401 | 0.447299 | 0.55855 | 0.691215 | 0.856245 |
| tossup | drop_share_1_d3 | 1220 | 0.260959 | 0.071591 | 0.0743759 | 0.15273 | 0.219002 | 0.264522 | 0.29152 | 0.356854 | 0.689251 |
| tossup | drop_share_2_d3 | 1220 | 0.29018 | 0.0572778 | 0.0838905 | 0.175412 | 0.260969 | 0.306692 | 0.330804 | 0.351626 | 0.519899 |
| tossup | drop_share_3_d3 | 1220 | 0.448861 | 0.102883 | 0.117117 | 0.328372 | 0.379822 | 0.423667 | 0.504531 | 0.653042 | 0.823143 |
| tossup | r_1 | 1220 | 0.365074 | 0.193344 | 0.0272758 | 0.084348 | 0.208853 | 0.345916 | 0.508946 | 0.705058 | 0.89227 |
| tossup | r_2 | 1220 | 0.343803 | 0.184568 | 0.0249734 | 0.0844781 | 0.198277 | 0.317965 | 0.46833 | 0.690039 | 0.893965 |
| tossup | r_3 | 1220 | 0.291123 | 0.172938 | 0.025704 | 0.0760139 | 0.154342 | 0.252697 | 0.38516 | 0.635956 | 0.794441 |
| tossup | r_norm | 1220 | 0.658706 | 0.0601118 | 0.577399 | 0.58281 | 0.608744 | 0.647821 | 0.694501 | 0.773961 | 0.897935 |
