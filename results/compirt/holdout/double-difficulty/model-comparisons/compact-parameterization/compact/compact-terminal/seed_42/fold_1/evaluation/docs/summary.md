# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/compact-vs-332/compact/compact-terminal/seed_42/fold_1/evaluation`
Result root: `results/compirt/holdout/compact-vs-332/compact/compact-terminal/seed_42/fold_1`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 289896 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.700198 |
| log_loss | 0.546453 |
| ece | 0.0860523 |
| brier | 0.178885 |
| accuracy | 0.74112 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.0210052 |
| probability_std | 0.236817 |
| probability_p10 | 0.320694 |
| probability_p50 | 0.760713 |
| probability_p90 | 0.940953 |
| mean_predictive_variance | 0.156356 |
| integrated_brier_score | 0.0984608 |
| joint_tossup_event_log_loss | 6.49815 |
| buzz_position_mae | 0.148944 |
| buzz_position_median_absolute_error | 0.130621 |
| buzz_position_bias | -0.052552 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |
| first_buzzer_top1_accuracy | 0.386231 |
| first_buzzer_mean_reciprocal_rank | 0.594679 |
| first_buzzer_log_loss | 1.59086 |
| first_buzzer_events | 9093 |
| neg_auroc | 0.700198 |
| neg_average_precision | 0.425434 |
| neg_precision | 0.448406 |
| neg_recall | 0.383726 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.172708 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.00908107 |
| no_buzz_calibration_error | -0.00682802 |
| no_buzz_brier | 0.0150661 |
| full_pmf_max_mass_error | 1.11022e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.700198 | 0.546453 | 0.0860523 | 0.178885 | 0.74112 | 0.762125 | -0.0210052 | 0.236817 | 0.320694 | 0.760713 | 0.940953 | 0.156356 |
| tossup_correctness | tier | fall | 2842 | 0.711415 | 0.503591 | 0.0719129 | 0.163268 | 0.771992 | 0.785362 | -0.0133709 | 0.219821 | 0.385039 | 0.791509 | 0.948732 | 0.150614 |
| tossup_correctness | tier | nationals | 1564 | 0.692888 | 0.584073 | 0.0823959 | 0.195559 | 0.703325 | 0.718031 | -0.0147059 | 0.232146 | 0.275699 | 0.708434 | 0.906102 | 0.174018 |
| tossup_correctness | tier | regionals | 1937 | 0.691332 | 0.561237 | 0.0970397 | 0.182959 | 0.734641 | 0.758389 | -0.0237481 | 0.241413 | 0.301326 | 0.756199 | 0.935269 | 0.156966 |
| tossup_correctness | tier | winter | 2750 | 0.694496 | 0.558939 | 0.10263 | 0.182672 | 0.735273 | 0.765818 | -0.0305455 | 0.248047 | 0.293705 | 0.762791 | 0.951667 | 0.151815 |
| tossup_correctness | category | Current Events | 126 | 0.72236 | 0.538969 | 0.130723 | 0.179904 | 0.730159 | 0.769841 | -0.0396825 | 0.213959 | 0.294103 | 0.696269 | 0.888053 | 0.183596 |
| tossup_correctness | category | Fine Arts | 1071 | 0.730465 | 0.507527 | 0.0764647 | 0.16594 | 0.771242 | 0.766573 | 0.00466853 | 0.231889 | 0.344049 | 0.764048 | 0.93982 | 0.157465 |
| tossup_correctness | category | Geography | 185 | 0.791528 | 0.527374 | 0.11826 | 0.17434 | 0.740541 | 0.697297 | 0.0432432 | 0.263815 | 0.161747 | 0.641846 | 0.896349 | 0.171103 |
| tossup_correctness | category | History | 1440 | 0.694457 | 0.557421 | 0.08933 | 0.183688 | 0.727083 | 0.754167 | -0.0270833 | 0.234995 | 0.332063 | 0.75326 | 0.946081 | 0.157129 |
| tossup_correctness | category | Literature | 1422 | 0.668443 | 0.53881 | 0.108109 | 0.171843 | 0.753868 | 0.814346 | -0.0604782 | 0.239465 | 0.343916 | 0.804571 | 0.958375 | 0.139836 |
| tossup_correctness | category | Mythology | 318 | 0.659511 | 0.508054 | 0.0708974 | 0.164184 | 0.77673 | 0.789308 | -0.0125786 | 0.189389 | 0.451177 | 0.806873 | 0.930804 | 0.153428 |
| tossup_correctness | category | Other Academic | 66 | 0.774916 | 0.499504 | 0.0743127 | 0.165324 | 0.742424 | 0.712121 | 0.030303 | 0.215888 | 0.256895 | 0.729696 | 0.875412 | 0.177884 |
| tossup_correctness | category | Philosophy | 311 | 0.765277 | 0.503377 | 0.0598804 | 0.167435 | 0.755627 | 0.745981 | 0.0096463 | 0.233333 | 0.320082 | 0.747001 | 0.947627 | 0.156932 |
| tossup_correctness | category | Popular Culture | 102 | 0.498148 | 0.405448 | 0.0862139 | 0.119551 | 0.872549 | 0.882353 | -0.00980392 | 0.094246 | 0.69645 | 0.828147 | 0.904892 | 0.145875 |
| tossup_correctness | category | Religion | 358 | 0.683876 | 0.595898 | 0.0983125 | 0.199499 | 0.692737 | 0.712291 | -0.0195531 | 0.230473 | 0.29092 | 0.710648 | 0.924789 | 0.170676 |
| tossup_correctness | category | Science | 1433 | 0.685462 | 0.578219 | 0.0928694 | 0.192336 | 0.716678 | 0.738311 | -0.0216329 | 0.244038 | 0.292595 | 0.747375 | 0.94003 | 0.15844 |
| tossup_correctness | category | Social Science | 324 | 0.727339 | 0.523195 | 0.0786407 | 0.173669 | 0.762346 | 0.731481 | 0.0308642 | 0.220416 | 0.308497 | 0.712396 | 0.906094 | 0.175282 |
| tossup_correctness | category | Unknown | 1937 | 0.691332 | 0.561237 | 0.0970397 | 0.182959 | 0.734641 | 0.758389 | -0.0237481 | 0.241413 | 0.301326 | 0.756199 | 0.935269 | 0.156966 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.685224 | 0.600624 | 0.0971053 | 0.201987 | 0.688623 | 0.712575 | -0.0239521 | 0.227038 | 0.283243 | 0.682679 | 0.880503 | 0.181058 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.709202 | 0.575699 | 0.0947429 | 0.188782 | 0.724781 | 0.729167 | -0.00438596 | 0.248371 | 0.262149 | 0.720525 | 0.926997 | 0.164695 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.704208 | 0.539459 | 0.0665698 | 0.176913 | 0.734752 | 0.755083 | -0.020331 | 0.225266 | 0.366337 | 0.77461 | 0.939805 | 0.155195 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.683405 | 0.537016 | 0.0897962 | 0.174235 | 0.754219 | 0.780942 | -0.0267229 | 0.226481 | 0.363398 | 0.784355 | 0.945368 | 0.151925 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.708729 | 0.548387 | 0.0961012 | 0.180362 | 0.74108 | 0.762029 | -0.0209493 | 0.247368 | 0.281375 | 0.740978 | 0.94203 | 0.157444 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1167 | 2.8673 | 0.605467 | 0.763346 | 1.88687 | 2.4519 | 2.86191 | 3.23793 | 3.90426 | 4.84825 |
| player | theta_1 | 1167 | -1.25987 | 0.692479 | -2.99549 | -2.37599 | -1.78016 | -1.24279 | -0.720755 | -0.15708 | 0.309055 |
| player | theta_2 | 1167 | -1.28724 | 0.706772 | -3.03458 | -2.40614 | -1.81253 | -1.27773 | -0.794114 | -0.0653956 | 0.538758 |
| player | theta_3 | 1167 | -1.18875 | 0.689231 | -2.9675 | -2.25521 | -1.7387 | -1.17494 | -0.690324 | -0.0859145 | 0.71486 |
| player | theta_norm | 1167 | 2.35825 | 0.741199 | 0.255854 | 1.14037 | 1.81939 | 2.3434 | 2.89649 | 3.59674 | 4.41049 |
| tossup | start_difficulty | 1220 | -1.61737 | 0.733451 | -3.71549 | -2.77505 | -2.09743 | -1.6654 | -1.14628 | -0.333196 | 0.991903 |
| tossup | end_difficulty | 1220 | -3.57526 | 1.51394 | -9.34066 | -6.36636 | -4.47596 | -3.37268 | -2.4971 | -1.35326 | 0.158471 |
| tossup | total_drop | 1220 | 1.95788 | 1.14372 | 0.700175 | 0.906744 | 1.17552 | 1.49218 | 2.44187 | 4.32226 | 7.53944 |
| tossup | drop_share_1 | 1220 | 0.33776 | 0.0620205 | 0.124135 | 0.253788 | 0.304378 | 0.327681 | 0.35837 | 0.469564 | 0.623692 |
| tossup | drop_share_2 | 1220 | 0.351902 | 0.0300231 | 0.227147 | 0.309374 | 0.337408 | 0.351166 | 0.364134 | 0.40061 | 0.52156 |
| tossup | drop_share_3 | 1220 | 0.310338 | 0.0564137 | 0.124452 | 0.207735 | 0.279878 | 0.316398 | 0.341255 | 0.384589 | 0.648718 |
| tossup | r_1 | 1220 | 0.888243 | 0.6909 | 0.0449042 | 0.139828 | 0.362925 | 0.665931 | 1.29662 | 2.24478 | 3.74399 |
| tossup | r_2 | 1220 | 0.956411 | 0.820519 | 0.0409417 | 0.126894 | 0.317057 | 0.679553 | 1.38404 | 2.61233 | 4.28273 |
| tossup | r_3 | 1220 | 0.795194 | 0.704527 | 0.0413406 | 0.117 | 0.292566 | 0.559155 | 1.02749 | 2.35782 | 3.93996 |
| tossup | r_norm | 1220 | 1.87814 | 0.674251 | 0.375232 | 0.908941 | 1.37101 | 1.81274 | 2.3123 | 3.06523 | 4.34758 |
| tossup_hazard | hazard_start_difficulty | 1220 | 2.57684 | 0.560254 | 0.677001 | 1.64884 | 2.17909 | 2.58901 | 2.9605 | 3.51202 | 4.20371 |
| tossup_hazard | hazard_end_difficulty | 1220 | -1.68314 | 1.53707 | -8.36218 | -4.30717 | -2.66016 | -1.69675 | -0.656118 | 0.788659 | 2.2596 |
| tossup_hazard | hazard_total_drop | 1220 | 4.25999 | 1.52496 | 0.774949 | 1.5886 | 3.31418 | 4.27251 | 5.16573 | 6.77457 | 10.8019 |
| tossup_hazard | hazard_drop_share_1 | 1220 | 0.131543 | 0.0713494 | 0.0319558 | 0.0572371 | 0.0819786 | 0.112117 | 0.163669 | 0.272815 | 0.526472 |
| tossup_hazard | hazard_drop_share_2 | 1220 | 0.306041 | 0.141099 | 0.0484387 | 0.111677 | 0.189686 | 0.29557 | 0.401544 | 0.561789 | 0.77758 |
| tossup_hazard | hazard_drop_share_3 | 1220 | 0.562416 | 0.18553 | 0.0768302 | 0.229317 | 0.416066 | 0.58189 | 0.719453 | 0.826961 | 0.915364 |
