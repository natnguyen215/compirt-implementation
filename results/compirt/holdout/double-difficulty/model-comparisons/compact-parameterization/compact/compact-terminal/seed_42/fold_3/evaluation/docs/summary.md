# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/compact-vs-332/compact/compact-terminal/seed_42/fold_3/evaluation`
Result root: `results/compirt/holdout/compact-vs-332/compact/compact-terminal/seed_42/fold_3`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 290382 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.712085 |
| log_loss | 0.51967 |
| ece | 0.0776917 |
| brier | 0.169396 |
| accuracy | 0.755066 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | -0.014978 |
| probability_std | 0.229123 |
| probability_p10 | 0.352093 |
| probability_p50 | 0.771493 |
| probability_p90 | 0.945461 |
| mean_predictive_variance | 0.15483 |
| integrated_brier_score | 0.0990884 |
| joint_tossup_event_log_loss | 6.44595 |
| buzz_position_mae | 0.150063 |
| buzz_position_median_absolute_error | 0.130925 |
| buzz_position_bias | -0.0570578 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |
| first_buzzer_top1_accuracy | 0.39967 |
| first_buzzer_mean_reciprocal_rank | 0.604231 |
| first_buzzer_log_loss | 1.56844 |
| first_buzzer_events | 9080 |
| neg_auroc | 0.712085 |
| neg_average_precision | 0.442246 |
| neg_precision | 0.459524 |
| neg_recall | 0.369732 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.163139 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0084357 |
| no_buzz_calibration_error | -0.00674868 |
| no_buzz_brier | 0.0131088 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.712085 | 0.51967 | 0.0776917 | 0.169396 | 0.755066 | 0.770044 | -0.014978 | 0.229123 | 0.352093 | 0.771493 | 0.945461 | 0.15483 |
| tossup_correctness | tier | fall | 2817 | 0.711109 | 0.495865 | 0.0632812 | 0.158317 | 0.777778 | 0.781683 | -0.00390486 | 0.213301 | 0.410331 | 0.799645 | 0.953038 | 0.147533 |
| tossup_correctness | tier | nationals | 1542 | 0.706863 | 0.562562 | 0.0798874 | 0.188617 | 0.715953 | 0.73476 | -0.0188067 | 0.223493 | 0.322893 | 0.710798 | 0.904257 | 0.175177 |
| tossup_correctness | tier | regionals | 1934 | 0.701501 | 0.547111 | 0.0942806 | 0.180659 | 0.738366 | 0.75698 | -0.0186143 | 0.240598 | 0.299808 | 0.749298 | 0.933118 | 0.159649 |
| tossup_correctness | tier | winter | 2787 | 0.716414 | 0.500958 | 0.0849714 | 0.162145 | 0.765339 | 0.786868 | -0.0215285 | 0.232874 | 0.3532 | 0.790752 | 0.954894 | 0.147603 |
| tossup_correctness | category | Current Events | 125 | 0.751536 | 0.518811 | 0.0704956 | 0.173052 | 0.72 | 0.704 | 0.016 | 0.17167 | 0.475026 | 0.737035 | 0.900209 | 0.180419 |
| tossup_correctness | category | Fine Arts | 1072 | 0.71401 | 0.502845 | 0.0762606 | 0.162648 | 0.768657 | 0.770522 | -0.00186567 | 0.219976 | 0.366301 | 0.774981 | 0.941209 | 0.156303 |
| tossup_correctness | category | Geography | 185 | 0.752448 | 0.529847 | 0.085277 | 0.179888 | 0.72973 | 0.702703 | 0.027027 | 0.253813 | 0.255175 | 0.732869 | 0.926181 | 0.163406 |
| tossup_correctness | category | History | 1443 | 0.739304 | 0.50746 | 0.0739711 | 0.166509 | 0.751906 | 0.765073 | -0.013167 | 0.232456 | 0.335122 | 0.755119 | 0.939628 | 0.158948 |
| tossup_correctness | category | Literature | 1411 | 0.688268 | 0.500523 | 0.0954814 | 0.161337 | 0.771084 | 0.81219 | -0.0411056 | 0.223924 | 0.3893 | 0.82292 | 0.965395 | 0.137555 |
| tossup_correctness | category | Mythology | 320 | 0.676092 | 0.506444 | 0.105378 | 0.160719 | 0.771875 | 0.79375 | -0.021875 | 0.182759 | 0.450138 | 0.803281 | 0.953331 | 0.150387 |
| tossup_correctness | category | Other Academic | 64 | 0.583333 | 0.59333 | 0.0711105 | 0.198538 | 0.734375 | 0.75 | -0.015625 | 0.160539 | 0.54784 | 0.756612 | 0.893925 | 0.170771 |
| tossup_correctness | category | Philosophy | 312 | 0.730323 | 0.460976 | 0.0860704 | 0.147637 | 0.769231 | 0.801282 | -0.0320513 | 0.209485 | 0.408996 | 0.789313 | 0.951428 | 0.150991 |
| tossup_correctness | category | Popular Culture | 104 | 0.567472 | 0.441662 | 0.070853 | 0.131934 | 0.846154 | 0.846154 | 0 | 0.0827157 | 0.725125 | 0.84671 | 0.924034 | 0.132063 |
| tossup_correctness | category | Religion | 358 | 0.720173 | 0.539528 | 0.0681873 | 0.180594 | 0.715084 | 0.726257 | -0.0111732 | 0.209585 | 0.35332 | 0.694692 | 0.905405 | 0.179905 |
| tossup_correctness | category | Science | 1431 | 0.701803 | 0.536832 | 0.0822735 | 0.17403 | 0.754018 | 0.765199 | -0.011181 | 0.234498 | 0.333564 | 0.775322 | 0.949289 | 0.151618 |
| tossup_correctness | category | Social Science | 321 | 0.741912 | 0.526219 | 0.0849869 | 0.167998 | 0.775701 | 0.744548 | 0.0311526 | 0.240668 | 0.294253 | 0.751516 | 0.934799 | 0.162094 |
| tossup_correctness | category | Unknown | 1934 | 0.701501 | 0.547111 | 0.0942806 | 0.180659 | 0.738366 | 0.75698 | -0.0186143 | 0.240598 | 0.299808 | 0.749298 | 0.933118 | 0.159649 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.770072 | 0.550815 | 0.102838 | 0.178919 | 0.734375 | 0.697917 | 0.0364583 | 0.224358 | 0.25723 | 0.671788 | 0.862574 | 0.187793 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.755125 | 0.506422 | 0.0521105 | 0.166872 | 0.75703 | 0.733408 | 0.023622 | 0.23414 | 0.308402 | 0.750492 | 0.93056 | 0.16231 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.702992 | 0.52739 | 0.0663843 | 0.170601 | 0.754751 | 0.759276 | -0.00452489 | 0.223258 | 0.376052 | 0.789212 | 0.947728 | 0.151077 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.695171 | 0.504256 | 0.0685588 | 0.163113 | 0.766469 | 0.789125 | -0.022656 | 0.211734 | 0.419298 | 0.79518 | 0.95515 | 0.148534 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.716293 | 0.530958 | 0.106927 | 0.1748 | 0.744863 | 0.775342 | -0.0304795 | 0.242333 | 0.295367 | 0.746477 | 0.937255 | 0.159411 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1133 | 2.86986 | 0.60954 | 1.08358 | 1.9015 | 2.4338 | 2.84055 | 3.25936 | 3.90291 | 5.01798 |
| player | theta_1 | 1133 | -1.26451 | 0.690859 | -3.24088 | -2.36773 | -1.78041 | -1.24641 | -0.733022 | -0.149405 | 0.345536 |
| player | theta_2 | 1133 | -1.27356 | 0.703157 | -3.02878 | -2.40916 | -1.79487 | -1.28804 | -0.776781 | -0.0567305 | 0.553925 |
| player | theta_3 | 1133 | -1.18817 | 0.686651 | -2.96989 | -2.28781 | -1.69083 | -1.19682 | -0.699268 | -0.0623131 | 0.680842 |
| player | theta_norm | 1133 | 2.34922 | 0.745852 | 0.371414 | 1.14822 | 1.80824 | 2.34641 | 2.91919 | 3.57995 | 4.7283 |
| tossup | start_difficulty | 1240 | -1.60934 | 0.724005 | -3.62346 | -2.75615 | -2.08728 | -1.6384 | -1.16138 | -0.399499 | 1.18385 |
| tossup | end_difficulty | 1240 | -3.55784 | 1.52392 | -9.29946 | -6.52657 | -4.48961 | -3.34987 | -2.52451 | -1.40774 | 0.487443 |
| tossup | total_drop | 1240 | 1.94849 | 1.16022 | 0.669099 | 0.901439 | 1.16221 | 1.49119 | 2.36011 | 4.48426 | 7.38024 |
| tossup | drop_share_1 | 1240 | 0.337683 | 0.0631264 | 0.131908 | 0.257673 | 0.302426 | 0.327322 | 0.358568 | 0.464676 | 0.625574 |
| tossup | drop_share_2 | 1240 | 0.351639 | 0.0298175 | 0.219294 | 0.308826 | 0.338211 | 0.351078 | 0.363356 | 0.40045 | 0.53934 |
| tossup | drop_share_3 | 1240 | 0.310678 | 0.0557707 | 0.128523 | 0.206959 | 0.283826 | 0.318304 | 0.341957 | 0.385217 | 0.648798 |
| tossup | r_1 | 1240 | 0.878311 | 0.684816 | 0.0367169 | 0.143572 | 0.350556 | 0.658752 | 1.2519 | 2.26264 | 3.51518 |
| tossup | r_2 | 1240 | 0.942936 | 0.79868 | 0.0386544 | 0.129081 | 0.330454 | 0.668484 | 1.34435 | 2.59407 | 3.907 |
| tossup | r_3 | 1240 | 0.787835 | 0.710115 | 0.0350069 | 0.120196 | 0.30107 | 0.541418 | 0.993228 | 2.44017 | 3.86294 |
| tossup | r_norm | 1240 | 1.8569 | 0.665851 | 0.40561 | 0.887582 | 1.35068 | 1.82726 | 2.27927 | 3.03996 | 4.04349 |
| tossup_hazard | hazard_start_difficulty | 1240 | 2.56602 | 0.569945 | 0.681215 | 1.6408 | 2.17717 | 2.56242 | 2.98906 | 3.50285 | 4.5602 |
| tossup_hazard | hazard_end_difficulty | 1240 | -1.63061 | 1.50883 | -7.62231 | -4.15912 | -2.56664 | -1.59682 | -0.552832 | 0.767124 | 2.49276 |
| tossup_hazard | hazard_total_drop | 1240 | 4.19663 | 1.52584 | 0.710281 | 1.53408 | 3.29789 | 4.20837 | 5.11934 | 6.63072 | 10.5147 |
| tossup_hazard | hazard_drop_share_1 | 1240 | 0.133174 | 0.0719798 | 0.0308308 | 0.0577054 | 0.0819919 | 0.112157 | 0.165524 | 0.270337 | 0.54955 |
| tossup_hazard | hazard_drop_share_2 | 1240 | 0.305977 | 0.139655 | 0.0506506 | 0.113286 | 0.188349 | 0.294611 | 0.396013 | 0.557879 | 0.745774 |
| tossup_hazard | hazard_drop_share_3 | 1240 | 0.56085 | 0.184898 | 0.0783781 | 0.241319 | 0.418452 | 0.578893 | 0.717386 | 0.823517 | 0.9123 |
