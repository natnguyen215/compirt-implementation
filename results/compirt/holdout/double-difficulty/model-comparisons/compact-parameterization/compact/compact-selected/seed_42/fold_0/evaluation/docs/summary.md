# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/compact-vs-332/compact/compact-selected/seed_42/fold_0/evaluation`
Result root: `results/compirt/holdout/compact-vs-332/compact/compact-selected/seed_42/fold_0`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 278108 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.706841 |
| log_loss | 0.513677 |
| ece | 0.0559149 |
| brier | 0.166219 |
| accuracy | 0.766649 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | 0.0013986 |
| probability_std | 0.209246 |
| probability_p10 | 0.441545 |
| probability_p50 | 0.82909 |
| probability_p90 | 0.95834 |
| mean_predictive_variance | 0.138585 |
| integrated_brier_score | 0.0947871 |
| joint_tossup_event_log_loss | 6.40662 |
| buzz_position_mae | 0.140909 |
| buzz_position_median_absolute_error | 0.120541 |
| buzz_position_bias | -0.0259399 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |
| first_buzzer_top1_accuracy | 0.403981 |
| first_buzzer_mean_reciprocal_rank | 0.608249 |
| first_buzzer_log_loss | 1.55604 |
| first_buzzer_events | 9295 |
| neg_auroc | 0.706841 |
| neg_average_precision | 0.437453 |
| neg_precision | 0.505376 |
| neg_recall | 0.280018 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.175101 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.00948875 |
| no_buzz_calibration_error | -0.00378089 |
| no_buzz_brier | 0.0126108 |
| full_pmf_max_mass_error | 1.66533e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.706841 | 0.513677 | 0.0559149 | 0.166219 | 0.766649 | 0.76525 | 0.0013986 | 0.209246 | 0.441545 | 0.82909 | 0.95834 | 0.138585 |
| tossup_correctness | tier | fall | 2933 | 0.698766 | 0.486546 | 0.0550485 | 0.15603 | 0.779748 | 0.791681 | -0.0119332 | 0.19903 | 0.463672 | 0.84048 | 0.961133 | 0.135823 |
| tossup_correctness | tier | nationals | 1584 | 0.714547 | 0.545271 | 0.0571169 | 0.177816 | 0.752525 | 0.724747 | 0.0277778 | 0.219584 | 0.408385 | 0.817424 | 0.95211 | 0.143456 |
| tossup_correctness | tier | regionals | 1886 | 0.707082 | 0.538117 | 0.0579484 | 0.175558 | 0.744433 | 0.746023 | -0.00159067 | 0.214902 | 0.404351 | 0.817949 | 0.957651 | 0.141308 |
| tossup_correctness | tier | winter | 2892 | 0.70664 | 0.50795 | 0.0606864 | 0.164111 | 0.775588 | 0.773167 | 0.00242047 | 0.208765 | 0.455509 | 0.832374 | 0.958347 | 0.136943 |
| tossup_correctness | category | Current Events | 124 | 0.654873 | 0.582032 | 0.150173 | 0.188001 | 0.717742 | 0.75 | -0.0322581 | 0.218713 | 0.404491 | 0.778089 | 0.967431 | 0.145739 |
| tossup_correctness | category | Fine Arts | 1103 | 0.714957 | 0.500561 | 0.0470718 | 0.160785 | 0.782412 | 0.759746 | 0.0226655 | 0.192967 | 0.480796 | 0.835405 | 0.951749 | 0.138871 |
| tossup_correctness | category | Geography | 197 | 0.752098 | 0.559995 | 0.0924618 | 0.184859 | 0.715736 | 0.670051 | 0.0456853 | 0.264298 | 0.247034 | 0.761367 | 0.949432 | 0.152702 |
| tossup_correctness | category | History | 1491 | 0.727989 | 0.478157 | 0.0453793 | 0.154549 | 0.782025 | 0.787391 | -0.00536553 | 0.203985 | 0.452944 | 0.824138 | 0.954434 | 0.141398 |
| tossup_correctness | category | Literature | 1472 | 0.702763 | 0.478101 | 0.0659495 | 0.149896 | 0.803668 | 0.804348 | -0.000679348 | 0.212423 | 0.465696 | 0.874022 | 0.97049 | 0.120443 |
| tossup_correctness | category | Mythology | 332 | 0.63172 | 0.486122 | 0.0622155 | 0.15347 | 0.792169 | 0.813253 | -0.0210843 | 0.16152 | 0.565506 | 0.842276 | 0.94275 | 0.138919 |
| tossup_correctness | category | Other Academic | 69 | 0.774887 | 0.467644 | 0.074948 | 0.155163 | 0.768116 | 0.753623 | 0.0144928 | 0.170035 | 0.572473 | 0.815631 | 0.926651 | 0.153214 |
| tossup_correctness | category | Philosophy | 324 | 0.683279 | 0.470937 | 0.0569072 | 0.152072 | 0.802469 | 0.799383 | 0.00308642 | 0.170727 | 0.528901 | 0.836793 | 0.951699 | 0.140801 |
| tossup_correctness | category | Popular Culture | 102 | 0.46436 | 0.506055 | 0.095225 | 0.145525 | 0.823529 | 0.833333 | -0.00980392 | 0.0901583 | 0.766024 | 0.90036 | 0.959498 | 0.102722 |
| tossup_correctness | category | Religion | 372 | 0.672384 | 0.583804 | 0.0803382 | 0.199488 | 0.696237 | 0.709677 | -0.0134409 | 0.18011 | 0.455941 | 0.779456 | 0.931234 | 0.161068 |
| tossup_correctness | category | Science | 1487 | 0.684634 | 0.54871 | 0.089367 | 0.180419 | 0.744452 | 0.752522 | -0.00806994 | 0.22405 | 0.417352 | 0.820858 | 0.963199 | 0.139906 |
| tossup_correctness | category | Social Science | 336 | 0.750932 | 0.528171 | 0.0551071 | 0.17109 | 0.755952 | 0.702381 | 0.0535714 | 0.221903 | 0.367991 | 0.790214 | 0.934405 | 0.153123 |
| tossup_correctness | category | Unknown | 1886 | 0.707082 | 0.538117 | 0.0579484 | 0.175558 | 0.744433 | 0.746023 | -0.00159067 | 0.214902 | 0.404351 | 0.817949 | 0.957651 | 0.141308 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.690716 | 0.535136 | 0.0802044 | 0.166541 | 0.786802 | 0.736041 | 0.0507614 | 0.200733 | 0.454072 | 0.825328 | 0.947545 | 0.144915 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.715226 | 0.534532 | 0.0689521 | 0.175308 | 0.751269 | 0.735025 | 0.0162437 | 0.195012 | 0.49494 | 0.843498 | 0.962199 | 0.134122 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.694172 | 0.519385 | 0.0652893 | 0.16776 | 0.760995 | 0.769436 | -0.00844069 | 0.194942 | 0.492056 | 0.850507 | 0.963001 | 0.131612 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.701572 | 0.49781 | 0.0574945 | 0.160512 | 0.774948 | 0.78402 | -0.00907188 | 0.197585 | 0.465547 | 0.83822 | 0.961662 | 0.135822 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.722741 | 0.516301 | 0.0573139 | 0.167512 | 0.766689 | 0.756008 | 0.0106809 | 0.229564 | 0.351923 | 0.794444 | 0.949691 | 0.14752 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1186 | 2.03348 | 0.562329 | 0.290353 | 1.08607 | 1.65701 | 2.05245 | 2.42831 | 2.93731 | 3.55055 |
| player | theta_1 | 1186 | -1.38947 | 0.666557 | -3.35951 | -2.45898 | -1.88242 | -1.38747 | -0.935306 | -0.273164 | 0.345872 |
| player | theta_2 | 1186 | -1.32772 | 0.636743 | -3.1993 | -2.34159 | -1.82065 | -1.34071 | -0.847699 | -0.270423 | 0.587101 |
| player | theta_3 | 1186 | -1.28759 | 0.646467 | -2.99177 | -2.31022 | -1.77585 | -1.29326 | -0.825811 | -0.225487 | 0.516588 |
| player | theta_norm | 1186 | 2.49914 | 0.610362 | 0.88995 | 1.55873 | 2.05583 | 2.46875 | 2.91475 | 3.54944 | 4.71025 |
| tossup | start_difficulty | 1240 | -3.22757 | 0.79173 | -5.21237 | -4.48349 | -3.78329 | -3.26309 | -2.72871 | -1.84645 | -0.517822 |
| tossup | end_difficulty | 1240 | -4.25361 | 0.958419 | -7.65137 | -5.84841 | -4.90545 | -4.247 | -3.62678 | -2.67673 | -1.39012 |
| tossup | total_drop | 1240 | 1.02604 | 0.28886 | 0.603629 | 0.719964 | 0.854863 | 0.970065 | 1.10937 | 1.50405 | 3.25377 |
| tossup | drop_share_1 | 1240 | 0.294243 | 0.0285245 | 0.148468 | 0.243851 | 0.28013 | 0.297369 | 0.312053 | 0.335888 | 0.404189 |
| tossup | drop_share_2 | 1240 | 0.348118 | 0.0170076 | 0.233847 | 0.323711 | 0.338503 | 0.34744 | 0.357209 | 0.372974 | 0.468651 |
| tossup | drop_share_3 | 1240 | 0.357639 | 0.0319511 | 0.251969 | 0.314448 | 0.338285 | 0.354272 | 0.372848 | 0.410689 | 0.612268 |
| tossup | r_1 | 1240 | 0.969293 | 0.775603 | 0.0394626 | 0.133301 | 0.360377 | 0.740053 | 1.37362 | 2.56411 | 4.24388 |
| tossup | r_2 | 1240 | 0.797642 | 0.626926 | 0.0442598 | 0.129136 | 0.298272 | 0.604893 | 1.14786 | 2.12202 | 3.26231 |
| tossup | r_3 | 1240 | 0.797101 | 0.680694 | 0.0464763 | 0.121146 | 0.300463 | 0.581175 | 1.03952 | 2.32395 | 4.01515 |
| tossup | r_norm | 1240 | 1.80827 | 0.631183 | 0.35921 | 0.87184 | 1.33013 | 1.75657 | 2.22135 | 2.8874 | 4.29137 |
| tossup_hazard | hazard_start_difficulty | 1240 | 3.7927 | 0.614916 | 1.80234 | 2.78174 | 3.35729 | 3.795 | 4.22932 | 4.78171 | 5.6532 |
| tossup_hazard | hazard_end_difficulty | 1240 | -1.07905 | 1.55758 | -7.04833 | -3.53297 | -2.04832 | -1.11886 | -0.0305461 | 1.53479 | 3.36386 |
| tossup_hazard | hazard_total_drop | 1240 | 4.87175 | 1.53499 | 0.713821 | 2.23134 | 3.90522 | 4.91102 | 5.83422 | 7.32921 | 11.1902 |
| tossup_hazard | hazard_drop_share_1 | 1240 | 0.160277 | 0.0869559 | 0.0334754 | 0.066098 | 0.10079 | 0.138092 | 0.195884 | 0.333005 | 0.648928 |
| tossup_hazard | hazard_drop_share_2 | 1240 | 0.316441 | 0.134421 | 0.0536425 | 0.120568 | 0.21602 | 0.306294 | 0.402977 | 0.55759 | 0.73788 |
| tossup_hazard | hazard_drop_share_3 | 1240 | 0.523281 | 0.184824 | 0.0762029 | 0.207955 | 0.374642 | 0.535982 | 0.669988 | 0.803004 | 0.902582 |
