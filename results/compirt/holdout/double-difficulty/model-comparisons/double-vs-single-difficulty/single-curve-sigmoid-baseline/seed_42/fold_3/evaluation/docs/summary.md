# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/double-difficulty-matrix-infill/single-curve-sigmoid-baseline/seed_42/fold_3/evaluation`
Result root: `results/compirt/holdout/double-difficulty-matrix-infill/single-curve-sigmoid-baseline/seed_42/fold_3`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 299650 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.637679 |
| log_loss | 0.76678 |
| ece | 0.21016 |
| brier | 0.24819 |
| accuracy | 0.642181 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | -0.127863 |
| probability_std | 0.290272 |
| probability_p10 | 0.121749 |
| probability_p50 | 0.637131 |
| probability_p90 | 0.921617 |
| mean_predictive_variance | 0.159697 |
| integrated_brier_score | 0.0944496 |
| joint_tossup_event_log_loss | 6.72286 |
| buzz_position_mae | 0.145242 |
| buzz_position_median_absolute_error | 0.124565 |
| buzz_position_bias | -0.0477531 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |
| first_buzzer_top1_accuracy | 0.396145 |
| first_buzzer_mean_reciprocal_rank | 0.60188 |
| first_buzzer_log_loss | 1.59285 |
| first_buzzer_events | 9080 |
| neg_auroc | 0.637679 |
| neg_average_precision | 0.338728 |
| neg_precision | 0.32625 |
| neg_recall | 0.522031 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.0873424 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0562072 |
| no_buzz_calibration_error | 0.0410229 |
| no_buzz_brier | 0.0201584 |
| full_pmf_max_mass_error | 1.22125e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.637679 | 0.76678 | 0.21016 | 0.24819 | 0.642181 | 0.770044 | -0.127863 | 0.290272 | 0.121749 | 0.637131 | 0.921617 | 0.159697 |
| tossup_correctness | tier | fall | 2817 | 0.638985 | 0.748544 | 0.21391 | 0.243871 | 0.650337 | 0.781683 | -0.131345 | 0.287437 | 0.126846 | 0.639249 | 0.919489 | 0.160722 |
| tossup_correctness | tier | nationals | 1542 | 0.623414 | 0.740346 | 0.187368 | 0.249531 | 0.628405 | 0.73476 | -0.106355 | 0.281201 | 0.153734 | 0.652343 | 0.922518 | 0.162782 |
| tossup_correctness | tier | regionals | 1934 | 0.644482 | 0.779849 | 0.202499 | 0.246997 | 0.649948 | 0.75698 | -0.107032 | 0.293665 | 0.121205 | 0.631996 | 0.928627 | 0.157886 |
| tossup_correctness | tier | winter | 2787 | 0.643257 | 0.790768 | 0.231033 | 0.252642 | 0.636168 | 0.786868 | -0.1507 | 0.295304 | 0.0977378 | 0.626646 | 0.917676 | 0.15821 |
| tossup_correctness | category | Current Events | 125 | 0.596744 | 0.813328 | 0.213777 | 0.27333 | 0.592 | 0.704 | -0.112 | 0.278591 | 0.100909 | 0.590831 | 0.877112 | 0.170534 |
| tossup_correctness | category | Fine Arts | 1072 | 0.604293 | 0.806802 | 0.223139 | 0.265591 | 0.610075 | 0.770522 | -0.160448 | 0.291789 | 0.118516 | 0.630549 | 0.922716 | 0.159916 |
| tossup_correctness | category | Geography | 185 | 0.618601 | 0.822988 | 0.198363 | 0.274814 | 0.616216 | 0.702703 | -0.0864865 | 0.272602 | 0.110004 | 0.531664 | 0.862321 | 0.175522 |
| tossup_correctness | category | History | 1443 | 0.657061 | 0.747501 | 0.202642 | 0.241363 | 0.658351 | 0.765073 | -0.106722 | 0.289924 | 0.113485 | 0.640339 | 0.914371 | 0.160043 |
| tossup_correctness | category | Literature | 1411 | 0.632243 | 0.737746 | 0.215021 | 0.23712 | 0.664777 | 0.81219 | -0.147413 | 0.287904 | 0.137029 | 0.677553 | 0.929067 | 0.155559 |
| tossup_correctness | category | Mythology | 320 | 0.617872 | 0.809141 | 0.286473 | 0.275903 | 0.58125 | 0.79375 | -0.2125 | 0.278764 | 0.122751 | 0.556567 | 0.883228 | 0.171792 |
| tossup_correctness | category | Other Academic | 64 | 0.561198 | 0.704674 | 0.26394 | 0.249252 | 0.609375 | 0.75 | -0.140625 | 0.234176 | 0.188676 | 0.593795 | 0.831408 | 0.191876 |
| tossup_correctness | category | Philosophy | 312 | 0.659032 | 0.728684 | 0.244637 | 0.245076 | 0.644231 | 0.801282 | -0.157051 | 0.286754 | 0.130634 | 0.646908 | 0.913551 | 0.163254 |
| tossup_correctness | category | Popular Culture | 104 | 0.576705 | 0.893842 | 0.344233 | 0.296968 | 0.528846 | 0.846154 | -0.317308 | 0.257905 | 0.161701 | 0.506127 | 0.847799 | 0.183481 |
| tossup_correctness | category | Religion | 358 | 0.663776 | 0.764517 | 0.212335 | 0.255117 | 0.606145 | 0.726257 | -0.120112 | 0.297686 | 0.0838827 | 0.573362 | 0.898645 | 0.160351 |
| tossup_correctness | category | Science | 1431 | 0.63576 | 0.761101 | 0.190214 | 0.240351 | 0.655486 | 0.765199 | -0.109713 | 0.291299 | 0.138874 | 0.674613 | 0.9351 | 0.154786 |
| tossup_correctness | category | Social Science | 321 | 0.663282 | 0.711997 | 0.186725 | 0.238095 | 0.647975 | 0.744548 | -0.0965732 | 0.283177 | 0.121621 | 0.631058 | 0.916884 | 0.164691 |
| tossup_correctness | category | Unknown | 1934 | 0.644482 | 0.779849 | 0.202499 | 0.246997 | 0.649948 | 0.75698 | -0.107032 | 0.293665 | 0.121205 | 0.631996 | 0.928627 | 0.157886 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.726325 | 1.22005 | 0.442386 | 0.383216 | 0.479167 | 0.697917 | -0.21875 | 0.236379 | 0.0197442 | 0.179724 | 0.594583 | 0.140525 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.692475 | 1.02958 | 0.361767 | 0.334822 | 0.517435 | 0.733408 | -0.215973 | 0.278679 | 0.0336246 | 0.325818 | 0.80133 | 0.156122 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.657118 | 0.830046 | 0.257971 | 0.27142 | 0.604525 | 0.759276 | -0.154751 | 0.286568 | 0.0826292 | 0.52931 | 0.885988 | 0.167845 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.637546 | 0.69438 | 0.179522 | 0.225267 | 0.66992 | 0.789125 | -0.119205 | 0.269561 | 0.20216 | 0.682394 | 0.930217 | 0.162853 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.613263 | 0.680219 | 0.14985 | 0.217878 | 0.692123 | 0.775342 | -0.0832192 | 0.259337 | 0.250796 | 0.751433 | 0.944129 | 0.152778 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1133 | 4.59676 | 1.16369 | 0.873654 | 2.09836 | 4.03017 | 4.80645 | 5.39721 | 6.13859 | 7.1143 |
| player | theta_1 | 1133 | 0.033982 | 0.742069 | -2.19386 | -1.38793 | -0.404921 | 0.164303 | 0.575159 | 1.04043 | 1.75373 |
| player | theta_2 | 1133 | -0.0200264 | 0.729879 | -2.32231 | -1.42617 | -0.423411 | 0.0886035 | 0.477149 | 1.07463 | 2.02007 |
| player | theta_3 | 1133 | 0.0969821 | 0.737169 | -2.47082 | -1.33884 | -0.334711 | 0.21367 | 0.598744 | 1.14659 | 2.1564 |
| player | theta_4 | 1133 | 0.0863564 | 0.746022 | -2.47819 | -1.33582 | -0.362765 | 0.214422 | 0.592165 | 1.20802 | 2.21207 |
| player | theta_5 | 1133 | 0.0207773 | 0.744586 | -2.56248 | -1.39046 | -0.421039 | 0.160027 | 0.541181 | 1.03558 | 1.66183 |
| player | theta_norm | 1133 | 1.54987 | 0.593642 | 0.25841 | 0.73756 | 1.10553 | 1.45371 | 1.89942 | 2.6814 | 3.6751 |
| tossup | beta_1 | 1240 | 0.73686 | 0.494043 | -1.27412 | 0.228818 | 0.398121 | 0.57728 | 0.935177 | 1.77424 | 2.71581 |
| tossup | beta_2 | 1240 | 0.836535 | 0.589471 | -1.45902 | 0.209172 | 0.411768 | 0.627908 | 1.22122 | 2.01118 | 2.66773 |
| tossup | beta_3 | 1240 | 0.741053 | 0.495667 | -0.416334 | 0.238228 | 0.419662 | 0.581179 | 0.886744 | 1.84235 | 2.89654 |
| tossup | beta_4 | 1240 | 0.761302 | 0.529123 | -0.181609 | 0.217345 | 0.40985 | 0.582567 | 0.951317 | 1.92067 | 3.94483 |
| tossup | beta_5 | 1240 | 0.826905 | 0.579931 | -0.763334 | 0.213583 | 0.403077 | 0.621098 | 1.17179 | 2.01509 | 2.75924 |
| tossup | gamma_1 | 1240 | 13.2209 | 77.6263 | 0.420572 | 3.215 | 4.47989 | 5.1511 | 6.08341 | 21.103 | 1924.21 |
| tossup | gamma_2 | 1240 | 14.5159 | 79.6193 | 0.37777 | 3.30546 | 4.52635 | 5.15721 | 6.36363 | 21.3147 | 1617.05 |
| tossup | gamma_3 | 1240 | 11.3356 | 54.2623 | 1.07672 | 3.0889 | 4.43103 | 5.06162 | 5.89583 | 26.5239 | 1314.28 |
| tossup | gamma_4 | 1240 | 12.3079 | 75.2665 | 1.37156 | 3.53924 | 4.51467 | 5.13666 | 5.99228 | 17.5273 | 2022.95 |
| tossup | gamma_5 | 1240 | 13.6665 | 71.9181 | 0.887798 | 3.28894 | 4.53081 | 5.20745 | 6.52233 | 25.7976 | 1545.74 |
| tossup | mu_1 | 1240 | 0.499791 | 0.100651 | 0.174636 | 0.385582 | 0.447615 | 0.478142 | 0.524956 | 0.713765 | 0.970189 |
| tossup | mu_2 | 1240 | 0.517954 | 0.121752 | 0.243471 | 0.386354 | 0.444683 | 0.479277 | 0.554455 | 0.794349 | 0.992365 |
| tossup | mu_3 | 1240 | 0.50424 | 0.101208 | 0.196823 | 0.392495 | 0.451431 | 0.480597 | 0.52748 | 0.712031 | 0.978802 |
| tossup | mu_4 | 1240 | 0.503951 | 0.107223 | 0.211188 | 0.395426 | 0.446993 | 0.479168 | 0.515924 | 0.742034 | 0.985832 |
| tossup | mu_5 | 1240 | 0.513308 | 0.113703 | 0.179291 | 0.379354 | 0.447305 | 0.483943 | 0.549666 | 0.758418 | 0.984771 |
| tossup | r_1 | 1240 | 0.980385 | 0.710259 | 0.0987938 | 0.207926 | 0.436802 | 0.782246 | 1.37634 | 2.40955 | 4.58366 |
| tossup | r_2 | 1240 | 1.27117 | 1.04486 | 0.0772127 | 0.224909 | 0.487545 | 0.927701 | 1.71941 | 3.46027 | 7.3931 |
| tossup | r_3 | 1240 | 1.02253 | 0.852307 | 0.0700208 | 0.206867 | 0.414904 | 0.744379 | 1.33763 | 2.8388 | 5.6974 |
| tossup | r_4 | 1240 | 1.05563 | 0.930366 | 0.0774382 | 0.227477 | 0.422885 | 0.739604 | 1.27602 | 3.12925 | 5.49903 |
| tossup | r_5 | 1240 | 1.15019 | 0.820616 | 0.0746481 | 0.215492 | 0.495905 | 0.901688 | 1.66225 | 2.74151 | 4.41156 |
| tossup | r_norm | 1240 | 3.04939 | 0.787482 | 1.3484 | 1.9455 | 2.47365 | 2.96514 | 3.52708 | 4.49633 | 8.20881 |
