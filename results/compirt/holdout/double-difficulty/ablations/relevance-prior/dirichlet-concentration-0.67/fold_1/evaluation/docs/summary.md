# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/relevance-prior/dirichlet-concentration-0.67/fold_1/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/relevance-prior/dirichlet-concentration-0.67/fold_1`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 284231 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.710435 |
| log_loss | 0.49646 |
| ece | 0.013986 |
| brier | 0.161479 |
| accuracy | 0.772242 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | 0.0101177 |
| probability_std | 0.145301 |
| probability_p10 | 0.569652 |
| probability_p50 | 0.810919 |
| probability_p90 | 0.919962 |
| mean_predictive_variance | 0.154614 |
| integrated_brier_score | 0.0999546 |
| joint_tossup_event_log_loss | 6.59996 |
| buzz_position_mae | 0.148585 |
| buzz_position_median_absolute_error | 0.130386 |
| buzz_position_bias | -0.0405419 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |
| first_buzzer_top1_accuracy | 0.352909 |
| first_buzzer_mean_reciprocal_rank | 0.564909 |
| first_buzzer_log_loss | 1.67898 |
| first_buzzer_events | 9093 |
| neg_auroc | 0.710435 |
| neg_average_precision | 0.447515 |
| neg_precision | 0.581272 |
| neg_recall | 0.152104 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.198646 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0152455 |
| no_buzz_calibration_error | -0.00066364 |
| no_buzz_brier | 0.0156087 |
| full_pmf_max_mass_error | 1.44329e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.710435 | 0.49646 | 0.013986 | 0.161479 | 0.772242 | 0.762125 | 0.0101177 | 0.145301 | 0.569652 | 0.810919 | 0.919962 | 0.154614 |
| tossup_correctness | tier | fall | 2842 | 0.731079 | 0.462597 | 0.0137217 | 0.148645 | 0.790289 | 0.785362 | 0.00492611 | 0.143012 | 0.578898 | 0.823298 | 0.928301 | 0.149196 |
| tossup_correctness | tier | nationals | 1564 | 0.713688 | 0.539896 | 0.0436211 | 0.179497 | 0.740409 | 0.718031 | 0.0223785 | 0.146829 | 0.550753 | 0.797527 | 0.91224 | 0.160624 |
| tossup_correctness | tier | regionals | 1937 | 0.686932 | 0.512719 | 0.0211651 | 0.167441 | 0.762519 | 0.758389 | 0.0041301 | 0.139839 | 0.577491 | 0.805452 | 0.913763 | 0.157139 |
| tossup_correctness | tier | winter | 2750 | 0.700976 | 0.495302 | 0.014639 | 0.160296 | 0.778545 | 0.765818 | 0.0127273 | 0.149726 | 0.564497 | 0.80899 | 0.91928 | 0.155018 |
| tossup_correctness | category | Current Events | 126 | 0.718806 | 0.492981 | 0.0731287 | 0.160566 | 0.761905 | 0.769841 | -0.00793651 | 0.129895 | 0.544496 | 0.75965 | 0.883194 | 0.176162 |
| tossup_correctness | category | Fine Arts | 1071 | 0.751547 | 0.467539 | 0.0153223 | 0.151033 | 0.784314 | 0.766573 | 0.0177404 | 0.157858 | 0.535637 | 0.809791 | 0.923569 | 0.154698 |
| tossup_correctness | category | Geography | 185 | 0.794158 | 0.494123 | 0.0694134 | 0.162193 | 0.751351 | 0.697297 | 0.0540541 | 0.219494 | 0.361692 | 0.753136 | 0.892319 | 0.16884 |
| tossup_correctness | category | History | 1440 | 0.708951 | 0.509975 | 0.0284662 | 0.167422 | 0.759028 | 0.754167 | 0.00486111 | 0.142297 | 0.572876 | 0.814018 | 0.926688 | 0.152704 |
| tossup_correctness | category | Literature | 1422 | 0.677994 | 0.451407 | 0.0147129 | 0.142307 | 0.811533 | 0.814346 | -0.00281294 | 0.124278 | 0.638826 | 0.83857 | 0.930803 | 0.141053 |
| tossup_correctness | category | Mythology | 318 | 0.667301 | 0.480418 | 0.033807 | 0.151356 | 0.808176 | 0.789308 | 0.0188679 | 0.124326 | 0.640424 | 0.827457 | 0.927515 | 0.14519 |
| tossup_correctness | category | Other Academic | 66 | 0.804031 | 0.518319 | 0.157098 | 0.175025 | 0.712121 | 0.712121 | 0 | 0.137172 | 0.565036 | 0.793316 | 0.888593 | 0.16301 |
| tossup_correctness | category | Philosophy | 311 | 0.72883 | 0.506821 | 0.0830603 | 0.168669 | 0.73955 | 0.745981 | -0.00643087 | 0.132706 | 0.600743 | 0.811249 | 0.91517 | 0.154264 |
| tossup_correctness | category | Popular Culture | 102 | 0.526852 | 0.378349 | 0.0512768 | 0.108038 | 0.882353 | 0.882353 | 0 | 0.0709314 | 0.753838 | 0.853835 | 0.911056 | 0.130378 |
| tossup_correctness | category | Religion | 358 | 0.714982 | 0.540409 | 0.0331277 | 0.179621 | 0.743017 | 0.712291 | 0.0307263 | 0.156837 | 0.491284 | 0.783145 | 0.898468 | 0.171327 |
| tossup_correctness | category | Science | 1433 | 0.69575 | 0.52775 | 0.0355812 | 0.174101 | 0.755757 | 0.738311 | 0.0174459 | 0.147693 | 0.549147 | 0.798696 | 0.915137 | 0.160027 |
| tossup_correctness | category | Social Science | 324 | 0.77836 | 0.486808 | 0.057722 | 0.159275 | 0.771605 | 0.731481 | 0.0401235 | 0.15754 | 0.490124 | 0.795656 | 0.899546 | 0.163854 |
| tossup_correctness | category | Unknown | 1937 | 0.686932 | 0.512719 | 0.0211651 | 0.167441 | 0.762519 | 0.758389 | 0.0041301 | 0.139839 | 0.577491 | 0.805452 | 0.913763 | 0.157139 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.619748 | 0.602154 | 0.0758981 | 0.203378 | 0.676647 | 0.712575 | -0.0359281 | 0.136933 | 0.54392 | 0.772227 | 0.887903 | 0.172823 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.723375 | 0.520052 | 0.0254332 | 0.172286 | 0.741228 | 0.729167 | 0.0120614 | 0.160168 | 0.509078 | 0.777113 | 0.905359 | 0.166362 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.716726 | 0.500558 | 0.0233325 | 0.163267 | 0.770686 | 0.755083 | 0.0156028 | 0.138731 | 0.591875 | 0.810758 | 0.918716 | 0.153876 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.693197 | 0.483797 | 0.0152943 | 0.155509 | 0.787975 | 0.780942 | 0.00703235 | 0.130158 | 0.610599 | 0.821583 | 0.920719 | 0.149632 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.718423 | 0.492592 | 0.01146 | 0.160282 | 0.773159 | 0.762029 | 0.0111293 | 0.156178 | 0.532328 | 0.807851 | 0.924832 | 0.155261 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1167 | 2.66084 | 0.73988 | 0.482503 | 1.48728 | 2.16038 | 2.66018 | 3.14811 | 3.92742 | 4.65048 |
| player | theta_1 | 1167 | -1.22567 | 0.847841 | -3.57544 | -2.51771 | -1.76748 | -1.31882 | -0.721792 | 0.265153 | 1.60051 |
| player | theta_2 | 1167 | -1.01642 | 0.705425 | -3.51417 | -2.09566 | -1.45216 | -1.05509 | -0.607506 | 0.213895 | 1.83339 |
| player | theta_3 | 1167 | -1.04251 | 0.759195 | -3.30066 | -2.2079 | -1.53054 | -1.09615 | -0.601222 | 0.368619 | 1.91989 |
| player | theta_norm | 1167 | 2.24683 | 0.604626 | 0.407325 | 1.31154 | 1.82912 | 2.22084 | 2.61631 | 3.2929 | 4.2466 |
| tossup | start_difficulty_d1 | 1220 | -1.78467 | 0.546407 | -3.21546 | -2.55136 | -2.17141 | -1.83166 | -1.47582 | -0.883795 | 1.27164 |
| tossup | start_difficulty_d2 | 1220 | -1.77682 | 0.515407 | -3.31189 | -2.54308 | -2.14957 | -1.81696 | -1.45086 | -0.82993 | 0.204627 |
| tossup | start_difficulty_d3 | 1220 | -1.77169 | 0.508618 | -3.57051 | -2.52958 | -2.14709 | -1.79111 | -1.43913 | -0.899147 | 0.148737 |
| tossup | end_difficulty_d1 | 1220 | -2.77211 | 0.636654 | -4.49431 | -3.68776 | -3.20207 | -2.81989 | -2.39394 | -1.73694 | 0.598764 |
| tossup | end_difficulty_d2 | 1220 | -2.76293 | 0.601649 | -4.67503 | -3.66909 | -3.18502 | -2.79904 | -2.38916 | -1.69314 | -0.530878 |
| tossup | end_difficulty_d3 | 1220 | -2.75453 | 0.591995 | -4.86468 | -3.66792 | -3.17685 | -2.77129 | -2.37095 | -1.76385 | -0.553783 |
| tossup | total_drop_d1 | 1220 | 0.987437 | 0.111699 | 0.619894 | 0.800703 | 0.912157 | 0.990993 | 1.0617 | 1.15959 | 1.36043 |
| tossup | total_drop_d2 | 1220 | 0.986109 | 0.103633 | 0.673179 | 0.820636 | 0.91816 | 0.985815 | 1.05037 | 1.15899 | 1.36314 |
| tossup | total_drop_d3 | 1220 | 0.982835 | 0.101623 | 0.684728 | 0.820932 | 0.912358 | 0.981774 | 1.05069 | 1.15544 | 1.32375 |
| tossup | drop_share_1_d1 | 1220 | 0.248835 | 0.0316799 | 0.0902539 | 0.197629 | 0.229349 | 0.249189 | 0.269553 | 0.299557 | 0.359697 |
| tossup | drop_share_2_d1 | 1220 | 0.3725 | 0.0217354 | 0.270158 | 0.335477 | 0.35887 | 0.373176 | 0.386506 | 0.406103 | 0.447654 |
| tossup | drop_share_3_d1 | 1220 | 0.378665 | 0.0399795 | 0.247976 | 0.31858 | 0.351108 | 0.37745 | 0.40138 | 0.444205 | 0.639588 |
| tossup | drop_share_1_d2 | 1220 | 0.247852 | 0.0294801 | 0.141593 | 0.198155 | 0.229144 | 0.24899 | 0.266617 | 0.294016 | 0.365922 |
| tossup | drop_share_2_d2 | 1220 | 0.371756 | 0.0208579 | 0.300329 | 0.336434 | 0.358444 | 0.372298 | 0.385492 | 0.403894 | 0.476421 |
| tossup | drop_share_3_d2 | 1220 | 0.380392 | 0.0370297 | 0.247371 | 0.324468 | 0.355832 | 0.379196 | 0.402598 | 0.442164 | 0.5477 |
| tossup | drop_share_1_d3 | 1220 | 0.247778 | 0.0300363 | 0.134624 | 0.196047 | 0.228927 | 0.248275 | 0.267963 | 0.295992 | 0.409669 |
| tossup | drop_share_2_d3 | 1220 | 0.372189 | 0.020613 | 0.285482 | 0.34062 | 0.358614 | 0.372248 | 0.386342 | 0.405515 | 0.448891 |
| tossup | drop_share_3_d3 | 1220 | 0.380033 | 0.0373797 | 0.261303 | 0.324702 | 0.35523 | 0.37699 | 0.402164 | 0.442598 | 0.555804 |
| tossup | r_1 | 1220 | 0.32367 | 0.146239 | 0.0623012 | 0.132181 | 0.213025 | 0.297619 | 0.414729 | 0.606145 | 0.845439 |
| tossup | r_2 | 1220 | 0.336768 | 0.121879 | 0.0563158 | 0.149901 | 0.25169 | 0.327972 | 0.407359 | 0.563755 | 0.811845 |
| tossup | r_3 | 1220 | 0.339562 | 0.122291 | 0.0752156 | 0.158236 | 0.25347 | 0.328249 | 0.411175 | 0.565776 | 0.78176 |
| tossup | r_norm | 1220 | 0.618617 | 0.0441077 | 0.57738 | 0.579209 | 0.588442 | 0.603673 | 0.632377 | 0.713785 | 0.85255 |
| tossup_hazard | hazard_start_difficulty_d1 | 1220 | 4.44837 | 0.474716 | 1.99035 | 3.76808 | 4.17579 | 4.39763 | 4.69302 | 5.3037 | 6.40445 |
| tossup_hazard | hazard_start_difficulty_d2 | 1220 | 4.39007 | 0.425235 | 1.91675 | 3.73061 | 4.16303 | 4.3715 | 4.57947 | 5.13234 | 6.57107 |
| tossup_hazard | hazard_start_difficulty_d3 | 1220 | 4.40098 | 0.404561 | 2.14571 | 3.78106 | 4.17835 | 4.40047 | 4.61815 | 5.05089 | 6.22415 |
| tossup_hazard | hazard_end_difficulty_d1 | 1220 | 1.5814 | 2.45509 | -11.6556 | -3.67114 | 0.433725 | 2.76708 | 3.25301 | 3.6119 | 4.34051 |
| tossup_hazard | hazard_end_difficulty_d2 | 1220 | 2.04671 | 2.25304 | -10.4235 | -2.93665 | 2.00079 | 3.0575 | 3.3179 | 3.63358 | 4.14818 |
| tossup_hazard | hazard_end_difficulty_d3 | 1220 | 2.20337 | 2.24803 | -9.67385 | -3.34805 | 2.40279 | 3.14723 | 3.38561 | 3.68904 | 4.29903 |
| tossup_hazard | hazard_total_drop_d1 | 1220 | 2.86697 | 2.59938 | 0.901707 | 0.983162 | 1.0543 | 1.3875 | 4.19806 | 8.34243 | 16.1565 |
| tossup_hazard | hazard_total_drop_d2 | 1220 | 2.34336 | 2.39534 | 0.896982 | 0.966129 | 1.02374 | 1.1669 | 2.09713 | 7.65342 | 14.9086 |
| tossup_hazard | hazard_total_drop_d3 | 1220 | 2.19761 | 2.34601 | 0.875991 | 0.967165 | 1.02094 | 1.14061 | 1.73824 | 8.06804 | 14.153 |
| tossup_hazard | hazard_drop_share_1_d1 | 1220 | 0.154284 | 0.0822477 | 0.0140967 | 0.0310103 | 0.0789737 | 0.165362 | 0.21604 | 0.271876 | 0.596244 |
| tossup_hazard | hazard_drop_share_2_d1 | 1220 | 0.326761 | 0.127216 | 0.0191652 | 0.0820469 | 0.283074 | 0.342945 | 0.378831 | 0.522731 | 0.83725 |
| tossup_hazard | hazard_drop_share_3_d1 | 1220 | 0.518955 | 0.177876 | 0.0573502 | 0.28622 | 0.40158 | 0.471234 | 0.608056 | 0.881728 | 0.966738 |
| tossup_hazard | hazard_drop_share_1_d2 | 1220 | 0.171653 | 0.0761181 | 0.0113865 | 0.0350759 | 0.123714 | 0.18941 | 0.222505 | 0.266926 | 0.615651 |
| tossup_hazard | hazard_drop_share_2_d2 | 1220 | 0.337261 | 0.110258 | 0.0239293 | 0.110929 | 0.309498 | 0.344796 | 0.376476 | 0.50667 | 0.856349 |
| tossup_hazard | hazard_drop_share_3_d2 | 1220 | 0.491087 | 0.153176 | 0.0471149 | 0.309926 | 0.405929 | 0.452215 | 0.53147 | 0.851333 | 0.959998 |
| tossup_hazard | hazard_drop_share_1_d3 | 1220 | 0.173537 | 0.0705807 | 0.0133767 | 0.0358532 | 0.134879 | 0.18622 | 0.218405 | 0.261067 | 0.634981 |
| tossup_hazard | hazard_drop_share_2_d3 | 1220 | 0.340462 | 0.0970425 | 0.0309939 | 0.147373 | 0.308223 | 0.343825 | 0.378114 | 0.485471 | 0.781306 |
| tossup_hazard | hazard_drop_share_3_d3 | 1220 | 0.486001 | 0.138291 | 0.0315927 | 0.32534 | 0.408762 | 0.457745 | 0.531067 | 0.804662 | 0.95153 |
| tossup_hazard | hazard_r_1 | 1220 | 0.401001 | 0.277346 | 0.0305007 | 0.0618059 | 0.133137 | 0.341826 | 0.65598 | 0.8642 | 0.936889 |
| tossup_hazard | hazard_r_2 | 1220 | 0.303242 | 0.226231 | 0.022712 | 0.054811 | 0.119148 | 0.217764 | 0.467292 | 0.741441 | 0.871853 |
| tossup_hazard | hazard_r_3 | 1220 | 0.295757 | 0.219735 | 0.0208198 | 0.0536383 | 0.122617 | 0.218232 | 0.433893 | 0.75178 | 0.919617 |
