# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/relevance-locations-terminal/dd-bernstein-332-simplex-terminal/degree_3/curves_3/dirichlet_2/fold_0/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/relevance-locations-terminal/dd-bernstein-332-simplex-terminal/degree_3/curves_3/dirichlet_2/fold_0`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 301514 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.711118 |
| log_loss | 0.504833 |
| ece | 0.0683354 |
| brier | 0.165118 |
| accuracy | 0.770629 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | 0.00537924 |
| probability_std | 0.163428 |
| probability_p10 | 0.466919 |
| probability_p50 | 0.723877 |
| probability_p90 | 0.890267 |
| mean_predictive_variance | 0.184308 |
| integrated_brier_score | 0.110131 |
| joint_tossup_event_log_loss | 6.72412 |
| buzz_position_mae | 0.166572 |
| buzz_position_median_absolute_error | 0.14879 |
| buzz_position_bias | -0.0746779 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |
| first_buzzer_top1_accuracy | 0.335772 |
| first_buzzer_mean_reciprocal_rank | 0.554564 |
| first_buzzer_log_loss | 1.69245 |
| first_buzzer_events | 9295 |
| neg_auroc | 0.711118 |
| neg_average_precision | 0.446318 |
| neg_precision | 0.520973 |
| neg_recall | 0.284601 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.175714 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.0130871 |
| no_buzz_calibration_error | -0.000182562 |
| no_buzz_brier | 0.0125715 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.711118 | 0.504833 | 0.0683354 | 0.165118 | 0.770629 | 0.76525 | 0.00537924 | 0.163428 | 0.466919 | 0.723877 | 0.890267 | 0.184308 |
| tossup_correctness | tier | fall | 2933 | 0.707969 | 0.480449 | 0.0728006 | 0.154791 | 0.791681 | 0.791681 | 0 | 0.163596 | 0.490066 | 0.747402 | 0.912402 | 0.174778 |
| tossup_correctness | tier | nationals | 1584 | 0.698654 | 0.54849 | 0.0724617 | 0.183642 | 0.73548 | 0.724747 | 0.0107323 | 0.16526 | 0.405076 | 0.680717 | 0.845048 | 0.199408 |
| tossup_correctness | tier | regionals | 1886 | 0.70557 | 0.530219 | 0.0759884 | 0.176107 | 0.742842 | 0.746023 | -0.00318134 | 0.158773 | 0.447149 | 0.693669 | 0.865462 | 0.195016 |
| tossup_correctness | tier | winter | 2892 | 0.716061 | 0.489097 | 0.058829 | 0.158278 | 0.786653 | 0.773167 | 0.0134855 | 0.157976 | 0.496492 | 0.742709 | 0.896611 | 0.178719 |
| tossup_correctness | category | Current Events | 124 | 0.692334 | 0.529932 | 0.0904884 | 0.17574 | 0.741935 | 0.75 | -0.00806452 | 0.173323 | 0.441268 | 0.684221 | 0.898322 | 0.189385 |
| tossup_correctness | category | Fine Arts | 1103 | 0.70023 | 0.508163 | 0.0543674 | 0.165584 | 0.779692 | 0.759746 | 0.0199456 | 0.164064 | 0.46383 | 0.744857 | 0.891797 | 0.179214 |
| tossup_correctness | category | Geography | 197 | 0.762587 | 0.545948 | 0.11461 | 0.181139 | 0.761421 | 0.670051 | 0.0913706 | 0.21242 | 0.297177 | 0.61906 | 0.862504 | 0.194938 |
| tossup_correctness | category | History | 1491 | 0.722177 | 0.482781 | 0.0859121 | 0.156733 | 0.782696 | 0.787391 | -0.00469484 | 0.162359 | 0.472521 | 0.725395 | 0.894845 | 0.183046 |
| tossup_correctness | category | Literature | 1472 | 0.724495 | 0.453864 | 0.0654036 | 0.14299 | 0.815897 | 0.804348 | 0.0115489 | 0.137633 | 0.549198 | 0.76622 | 0.904538 | 0.171079 |
| tossup_correctness | category | Mythology | 332 | 0.681004 | 0.475346 | 0.101378 | 0.150883 | 0.792169 | 0.813253 | -0.0210843 | 0.147235 | 0.514697 | 0.746969 | 0.896089 | 0.178061 |
| tossup_correctness | category | Other Academic | 69 | 0.69457 | 0.535184 | 0.088179 | 0.179351 | 0.724638 | 0.753623 | -0.0289855 | 0.136454 | 0.485436 | 0.695734 | 0.82635 | 0.202099 |
| tossup_correctness | category | Philosophy | 324 | 0.678052 | 0.487226 | 0.0897272 | 0.157931 | 0.783951 | 0.799383 | -0.0154321 | 0.145467 | 0.510612 | 0.723292 | 0.888661 | 0.183535 |
| tossup_correctness | category | Popular Culture | 102 | 0.473356 | 0.501274 | 0.165357 | 0.154676 | 0.813725 | 0.833333 | -0.0196078 | 0.115063 | 0.648475 | 0.787846 | 0.922684 | 0.157183 |
| tossup_correctness | category | Religion | 372 | 0.703458 | 0.558436 | 0.0683239 | 0.189389 | 0.725806 | 0.709677 | 0.016129 | 0.16028 | 0.434521 | 0.668095 | 0.856528 | 0.200141 |
| tossup_correctness | category | Science | 1487 | 0.686507 | 0.526672 | 0.0633338 | 0.174966 | 0.751177 | 0.752522 | -0.00134499 | 0.172413 | 0.440918 | 0.716047 | 0.896041 | 0.183969 |
| tossup_correctness | category | Social Science | 336 | 0.756059 | 0.524158 | 0.0660696 | 0.173526 | 0.758929 | 0.702381 | 0.0565476 | 0.186434 | 0.377953 | 0.681623 | 0.878595 | 0.191837 |
| tossup_correctness | category | Unknown | 1886 | 0.70557 | 0.530219 | 0.0759884 | 0.176107 | 0.742842 | 0.746023 | -0.00318134 | 0.158773 | 0.447149 | 0.693669 | 0.865462 | 0.195016 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.712467 | 0.538965 | 0.127836 | 0.177618 | 0.756345 | 0.736041 | 0.0203046 | 0.166449 | 0.39021 | 0.658181 | 0.834143 | 0.204381 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.711368 | 0.53115 | 0.0575105 | 0.177255 | 0.743147 | 0.735025 | 0.00812183 | 0.173887 | 0.428409 | 0.700926 | 0.884344 | 0.188252 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.686468 | 0.514921 | 0.0712905 | 0.168946 | 0.766326 | 0.769436 | -0.00310973 | 0.164121 | 0.478137 | 0.728473 | 0.897319 | 0.18227 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.705841 | 0.49005 | 0.0764812 | 0.15852 | 0.788555 | 0.78402 | 0.00453594 | 0.159425 | 0.487056 | 0.738239 | 0.899859 | 0.17983 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.732293 | 0.5005 | 0.0667981 | 0.16374 | 0.766689 | 0.756008 | 0.0106809 | 0.160962 | 0.462009 | 0.72017 | 0.877827 | 0.187506 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1186 | 4.39056 | 0.533214 | 2.66952 | 3.50175 | 4.03242 | 4.39211 | 4.75657 | 5.25939 | 5.71724 |
| player | theta_1 | 1186 | -1.28733 | 0.876789 | -3.35689 | -2.50459 | -1.92413 | -1.4065 | -0.679897 | 0.245927 | 2.19928 |
| player | theta_2 | 1186 | -1.1005 | 0.776285 | -3.19447 | -2.20763 | -1.64889 | -1.20695 | -0.65949 | 0.405533 | 2.16891 |
| player | theta_3 | 1186 | -0.999836 | 0.672407 | -2.85031 | -2.02825 | -1.47268 | -1.03152 | -0.55413 | 0.0961499 | 1.4271 |
| player | theta_norm | 1186 | 2.28725 | 0.677384 | 0.259951 | 1.14262 | 1.80618 | 2.31765 | 2.76856 | 3.3601 | 4.35049 |
| tossup | start_difficulty_d1 | 1240 | -0.765698 | 0.655456 | -3.55031 | -2.07993 | -1.0873 | -0.695751 | -0.370491 | 0.184318 | 1.24701 |
| tossup | start_difficulty_d2 | 1240 | -0.64529 | 0.520592 | -3.259 | -1.55607 | -0.854805 | -0.600703 | -0.384706 | 0.16508 | 1.40144 |
| tossup | start_difficulty_d3 | 1240 | -0.65359 | 0.540506 | -3.19 | -1.62571 | -0.881862 | -0.625925 | -0.379835 | 0.155011 | 1.32936 |
| tossup | end_difficulty_d1 | 1240 | -1.93224 | 0.836694 | -5.34013 | -3.56344 | -2.32295 | -1.81172 | -1.42476 | -0.740057 | 0.375334 |
| tossup | end_difficulty_d2 | 1240 | -1.78187 | 0.668471 | -5.49673 | -2.98877 | -2.0417 | -1.70939 | -1.44742 | -0.779172 | 0.523998 |
| tossup | end_difficulty_d3 | 1240 | -1.79153 | 0.693281 | -5.09393 | -3.02344 | -2.07209 | -1.73738 | -1.45136 | -0.757729 | 0.594816 |
| tossup | total_drop_d1 | 1240 | 1.16654 | 0.226504 | 0.707882 | 0.902401 | 1.0387 | 1.12461 | 1.24045 | 1.55106 | 3.22268 |
| tossup | total_drop_d2 | 1240 | 1.13658 | 0.199001 | 0.764649 | 0.920639 | 1.03382 | 1.10931 | 1.1949 | 1.41352 | 3.23294 |
| tossup | total_drop_d3 | 1240 | 1.13794 | 0.18623 | 0.734546 | 0.914627 | 1.03616 | 1.11378 | 1.20307 | 1.44133 | 2.52736 |
| tossup | drop_share_1_d1 | 1240 | 0.317035 | 0.0209074 | 0.247394 | 0.288372 | 0.304395 | 0.314526 | 0.326475 | 0.356239 | 0.419977 |
| tossup | drop_share_2_d1 | 1240 | 0.349381 | 0.012279 | 0.310281 | 0.32964 | 0.34152 | 0.349075 | 0.356694 | 0.368777 | 0.412913 |
| tossup | drop_share_3_d1 | 1240 | 0.333585 | 0.0206659 | 0.246764 | 0.294749 | 0.323423 | 0.335691 | 0.347193 | 0.362115 | 0.394137 |
| tossup | drop_share_1_d2 | 1240 | 0.314059 | 0.0175798 | 0.215108 | 0.289443 | 0.303502 | 0.313255 | 0.322827 | 0.342 | 0.40033 |
| tossup | drop_share_2_d2 | 1240 | 0.34931 | 0.012369 | 0.305329 | 0.329623 | 0.341941 | 0.349238 | 0.356126 | 0.369665 | 0.47553 |
| tossup | drop_share_3_d2 | 1240 | 0.336631 | 0.0179243 | 0.240513 | 0.307851 | 0.326813 | 0.337005 | 0.347314 | 0.36359 | 0.406153 |
| tossup | drop_share_1_d3 | 1240 | 0.315481 | 0.0184161 | 0.246427 | 0.287657 | 0.303947 | 0.314504 | 0.324922 | 0.346028 | 0.420493 |
| tossup | drop_share_2_d3 | 1240 | 0.348562 | 0.0114612 | 0.306914 | 0.329991 | 0.340691 | 0.348614 | 0.355989 | 0.367095 | 0.39117 |
| tossup | drop_share_3_d3 | 1240 | 0.335957 | 0.0183679 | 0.24388 | 0.306067 | 0.32609 | 0.337369 | 0.346882 | 0.363664 | 0.399807 |
| tossup | r_1 | 1240 | 0.351228 | 0.185903 | 0.0472299 | 0.0987597 | 0.206841 | 0.322455 | 0.459585 | 0.73651 | 0.870087 |
| tossup | r_2 | 1240 | 0.320004 | 0.17734 | 0.0509099 | 0.095397 | 0.187804 | 0.279729 | 0.414948 | 0.694451 | 0.888758 |
| tossup | r_3 | 1240 | 0.328767 | 0.166075 | 0.0592334 | 0.105952 | 0.204979 | 0.302662 | 0.42204 | 0.651588 | 0.898284 |
| tossup | r_norm | 1240 | 0.649683 | 0.072683 | 0.577401 | 0.58136 | 0.597281 | 0.622347 | 0.675287 | 0.81364 | 0.901159 |
| tossup_hazard | hazard_start_difficulty_d1 | 1240 | 1.7975 | 0.82172 | 0.250257 | 0.665641 | 1.10477 | 1.71593 | 2.42212 | 3.21389 | 4.16801 |
| tossup_hazard | hazard_start_difficulty_d2 | 1240 | 1.56395 | 0.790808 | 0.252227 | 0.560908 | 0.914964 | 1.3947 | 2.11983 | 3.02125 | 4.39797 |
| tossup_hazard | hazard_start_difficulty_d3 | 1240 | 1.53031 | 0.80228 | 0.308693 | 0.599441 | 0.920826 | 1.29607 | 1.95665 | 3.19651 | 4.66127 |
| tossup_hazard | hazard_end_difficulty_d1 | 1240 | -0.386649 | 1.45328 | -9.31044 | -3.26476 | -0.573796 | 0.0309911 | 0.499043 | 0.996794 | 1.85726 |
| tossup_hazard | hazard_end_difficulty_d2 | 1240 | -0.339466 | 1.33245 | -9.5349 | -3.08554 | -0.393101 | -0.0393299 | 0.317729 | 0.849114 | 1.87089 |
| tossup_hazard | hazard_end_difficulty_d3 | 1240 | -0.204098 | 1.26731 | -9.35141 | -2.90716 | -0.276093 | 0.0484322 | 0.384541 | 0.922786 | 2.23405 |
| tossup_hazard | hazard_total_drop_d1 | 1240 | 2.18415 | 1.9413 | 0.734289 | 0.951729 | 1.01335 | 1.11338 | 2.66284 | 6.23792 | 12.6715 |
| tossup_hazard | hazard_total_drop_d2 | 1240 | 1.90342 | 1.81057 | 0.813642 | 0.950567 | 1.00383 | 1.0724 | 1.69212 | 6.02975 | 12.7273 |
| tossup_hazard | hazard_total_drop_d3 | 1240 | 1.7344 | 1.74466 | 0.708215 | 0.946726 | 0.998425 | 1.05122 | 1.27647 | 6.25384 | 12.3195 |
| tossup_hazard | hazard_drop_share_1_d1 | 1240 | 0.224535 | 0.0762028 | 0.036946 | 0.0769994 | 0.171281 | 0.254477 | 0.28283 | 0.304368 | 0.401547 |
| tossup_hazard | hazard_drop_share_2_d1 | 1240 | 0.348866 | 0.0768319 | 0.0758942 | 0.197121 | 0.337776 | 0.35126 | 0.366896 | 0.475252 | 0.727805 |
| tossup_hazard | hazard_drop_share_3_d1 | 1240 | 0.426599 | 0.121621 | 0.113178 | 0.322066 | 0.358976 | 0.382266 | 0.443571 | 0.719798 | 0.884852 |
| tossup_hazard | hazard_drop_share_1_d2 | 1240 | 0.238459 | 0.0729731 | 0.0260853 | 0.0775942 | 0.206565 | 0.269471 | 0.289996 | 0.30722 | 0.476152 |
| tossup_hazard | hazard_drop_share_2_d2 | 1240 | 0.34351 | 0.0641079 | 0.066152 | 0.200411 | 0.3387 | 0.350291 | 0.362082 | 0.413644 | 0.750818 |
| tossup_hazard | hazard_drop_share_3_d2 | 1240 | 0.41803 | 0.11585 | 0.137051 | 0.335613 | 0.355691 | 0.375137 | 0.421623 | 0.704296 | 0.891067 |
| tossup_hazard | hazard_drop_share_1_d3 | 1240 | 0.245956 | 0.0690687 | 0.0340409 | 0.0762151 | 0.231852 | 0.273434 | 0.290412 | 0.307509 | 0.386071 |
| tossup_hazard | hazard_drop_share_2_d3 | 1240 | 0.346644 | 0.0584804 | 0.0525458 | 0.245854 | 0.340541 | 0.350202 | 0.361197 | 0.3969 | 0.674341 |
| tossup_hazard | hazard_drop_share_3_d3 | 1240 | 0.4074 | 0.103575 | 0.195792 | 0.336472 | 0.356028 | 0.372499 | 0.405157 | 0.662775 | 0.909573 |
| tossup_hazard | hazard_r_1 | 1240 | 0.401552 | 0.303735 | 0.0189966 | 0.0443708 | 0.108634 | 0.319869 | 0.704583 | 0.892876 | 0.945917 |
| tossup_hazard | hazard_r_2 | 1240 | 0.325093 | 0.286079 | 0.0158041 | 0.037821 | 0.0806904 | 0.193821 | 0.556751 | 0.868311 | 0.953963 |
| tossup_hazard | hazard_r_3 | 1240 | 0.273355 | 0.255 | 0.0150445 | 0.0420123 | 0.0808027 | 0.159639 | 0.410189 | 0.82493 | 0.939113 |
