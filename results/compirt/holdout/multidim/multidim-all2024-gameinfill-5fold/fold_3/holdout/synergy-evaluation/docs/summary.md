# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/multidim/multidim-all2024-gameinfill-5fold/fold_3/holdout/synergy-evaluation`
Result root: `results/compirt/holdout/multidim/multidim-all2024-gameinfill-5fold/fold_3`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 299650 |
| pyramidal | calibrate_correctness | False |
| synergy | tournament | all tournaments |
| synergy | dimensions | 5 |
| synergy | calibrate_correctness | False |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.550063 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.897762 |
| log_loss | 0.406814 |
| ece | 0.0283349 |
| brier | 0.12947 |
| part_accuracy | 0.816834 |
| part_all_correct_accuracy | 0.525685 |
| accuracy_lift_over_all_correct | 0.291149 |
| part_accuracy_macro_team | 0.816055 |
| part_accuracy_macro_bonus | 0.815844 |
| probability_std | 0.340181 |
| probability_p10 | 0.0647862 |
| probability_p50 | 0.474848 |
| probability_p90 | 0.952001 |
| mean_predictive_variance | 0.13427 |
| exact_acc | 0.52738 |
| ranked_probability_score | 0.112153 |
| bonus_total_score_log_loss | 0.988394 |
| ppb_mae | 1.80858 |
| ranked_probability_score_responses | 8455 |
| bonus_total_score_log_loss_responses | 8455 |

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
| joint_tossup_event_log_loss | 6.69696 |
| buzz_position_mae | 0.145242 |
| buzz_position_median_absolute_error | 0.124564 |
| buzz_position_bias | -0.0477531 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |
| first_buzzer_top1_accuracy | 0.396145 |
| first_buzzer_mean_reciprocal_rank | 0.60188 |
| first_buzzer_log_loss | 1.59285 |
| first_buzzer_events | 9080 |

## Match Winner Simulation

| metric | value |
| --- | --- |
| match_winner_accuracy | 0.792123 |
| match_winner_brier | 0.144229 |
| match_games | 457 |
| match_simulations_per_game | 500 |

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
| tossup_correctness | category | Science | 1431 | 0.63576 | 0.761101 | 0.190214 | 0.240351 | 0.655486 | 0.765199 | -0.109713 | 0.291299 | 0.138873 | 0.674613 | 0.9351 | 0.154786 |
| tossup_correctness | category | Social Science | 321 | 0.663282 | 0.711997 | 0.186725 | 0.238095 | 0.647975 | 0.744548 | -0.0965732 | 0.283177 | 0.121621 | 0.631058 | 0.916884 | 0.164691 |
| tossup_correctness | category | Unknown | 1934 | 0.644482 | 0.779849 | 0.202499 | 0.246997 | 0.649948 | 0.75698 | -0.107032 | 0.293665 | 0.121205 | 0.631996 | 0.928627 | 0.157886 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.726325 | 1.22005 | 0.442386 | 0.383216 | 0.479167 | 0.697917 | -0.21875 | 0.236379 | 0.0197442 | 0.179724 | 0.594583 | 0.140525 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.692475 | 1.02958 | 0.361767 | 0.334822 | 0.517435 | 0.733408 | -0.215973 | 0.278679 | 0.0336246 | 0.325818 | 0.80133 | 0.156122 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.657118 | 0.830046 | 0.257971 | 0.27142 | 0.604525 | 0.759276 | -0.154751 | 0.286568 | 0.0826292 | 0.52931 | 0.885988 | 0.167845 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.637546 | 0.69438 | 0.179522 | 0.225267 | 0.66992 | 0.789125 | -0.119205 | 0.269561 | 0.20216 | 0.682394 | 0.930217 | 0.162853 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.613263 | 0.680219 | 0.14985 | 0.217878 | 0.692123 | 0.775342 | -0.0832192 | 0.259337 | 0.250796 | 0.751433 | 0.944129 | 0.152778 |
| bonus_part_correctness | aggregate | all | 25365 | 0.897762 | 0.406814 | 0.0283349 | 0.12947 | 0.816834 | 0.525685 | 0.291149 | 0.340181 | 0.0647862 | 0.474848 | 0.952001 | 0.13427 |
| bonus_part_correctness | tier | fall | 8094 | 0.892423 | 0.408033 | 0.0235574 | 0.130507 | 0.811589 | 0.595132 | 0.216457 | 0.330614 | 0.0995726 | 0.619002 | 0.960136 | 0.13555 |
| bonus_part_correctness | tier | nationals | 4125 | 0.889749 | 0.426874 | 0.0541585 | 0.136065 | 0.811152 | 0.448485 | 0.362667 | 0.324309 | 0.0453488 | 0.28835 | 0.891198 | 0.133657 |
| bonus_part_correctness | tier | regionals | 5247 | 0.898355 | 0.407811 | 0.0354513 | 0.129186 | 0.817229 | 0.481609 | 0.33562 | 0.334918 | 0.0556607 | 0.373698 | 0.933759 | 0.13508 |
| bonus_part_correctness | tier | winter | 7899 | 0.903365 | 0.394428 | 0.0194218 | 0.125153 | 0.824915 | 0.524117 | 0.300798 | 0.342338 | 0.0708145 | 0.48178 | 0.959035 | 0.13274 |
| bonus_part_correctness | category | Current Events | 243 | 0.889431 | 0.426014 | 0.0540905 | 0.134167 | 0.802469 | 0.506173 | 0.296296 | 0.339667 | 0.0507259 | 0.403507 | 0.925253 | 0.1331 |
| bonus_part_correctness | category | Fine Arts | 2937 | 0.885028 | 0.426432 | 0.0292372 | 0.136552 | 0.812394 | 0.508682 | 0.303711 | 0.333063 | 0.0670329 | 0.454578 | 0.948024 | 0.138908 |
| bonus_part_correctness | category | Geography | 456 | 0.89408 | 0.413354 | 0.0622763 | 0.131308 | 0.804825 | 0.622807 | 0.182018 | 0.335313 | 0.0766922 | 0.628749 | 0.959011 | 0.133901 |
| bonus_part_correctness | category | History | 4050 | 0.898569 | 0.403318 | 0.0339523 | 0.128878 | 0.816543 | 0.565185 | 0.251358 | 0.341044 | 0.0684245 | 0.551389 | 0.955486 | 0.132666 |
| bonus_part_correctness | category | Literature | 4029 | 0.90553 | 0.394368 | 0.0380225 | 0.124893 | 0.823529 | 0.536113 | 0.287416 | 0.342493 | 0.067105 | 0.463959 | 0.957835 | 0.132695 |
| bonus_part_correctness | category | Mythology | 936 | 0.883049 | 0.418258 | 0.0353634 | 0.135296 | 0.793803 | 0.619658 | 0.174145 | 0.310587 | 0.133084 | 0.649554 | 0.962115 | 0.144417 |
| bonus_part_correctness | category | Other Academic | 255 | 0.918445 | 0.367001 | 0.0432805 | 0.112349 | 0.843137 | 0.545098 | 0.298039 | 0.35598 | 0.0519847 | 0.551064 | 0.966947 | 0.122796 |
| bonus_part_correctness | category | Philosophy | 948 | 0.889802 | 0.423406 | 0.0547957 | 0.138436 | 0.793249 | 0.504219 | 0.28903 | 0.333635 | 0.0685894 | 0.409095 | 0.943438 | 0.13772 |
| bonus_part_correctness | category | Popular Culture | 285 | 0.887475 | 0.423466 | 0.0719121 | 0.136485 | 0.817544 | 0.578947 | 0.238596 | 0.316722 | 0.127629 | 0.629657 | 0.960383 | 0.140398 |
| bonus_part_correctness | category | Religion | 1014 | 0.906107 | 0.393371 | 0.0292421 | 0.124017 | 0.832347 | 0.50789 | 0.324458 | 0.345411 | 0.060605 | 0.465354 | 0.954435 | 0.130616 |
| bonus_part_correctness | category | Science | 4059 | 0.894029 | 0.411146 | 0.0162097 | 0.130992 | 0.814733 | 0.530426 | 0.284306 | 0.340958 | 0.070117 | 0.512923 | 0.955255 | 0.133545 |
| bonus_part_correctness | category | Social Science | 906 | 0.912694 | 0.372408 | 0.0252617 | 0.11548 | 0.843267 | 0.471302 | 0.371965 | 0.352991 | 0.0533013 | 0.358253 | 0.952019 | 0.123757 |
| bonus_part_correctness | category | Unknown | 5247 | 0.898355 | 0.407811 | 0.0354513 | 0.129186 | 0.817229 | 0.481609 | 0.33562 | 0.334918 | 0.0556607 | 0.373698 | 0.933759 | 0.13508 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## No-Synergy Versus Synergy Deltas

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.889463 | 0.897762 | 0.00829973 | synergy |
| log_loss | 0.420432 | 0.406814 | -0.0136172 | synergy |
| ece | 0.0226479 | 0.0283349 | 0.00568698 | no-synergy |
| brier | 0.134143 | 0.12947 | -0.00467244 | synergy |
| accuracy_lift_over_all_correct | 0.282594 | 0.291149 | 0.0085551 | synergy |
| part_accuracy | 0.808279 | 0.816834 | 0.0085551 | synergy |
| part_accuracy_macro_team | 0.811087 | 0.816055 | 0.00496746 | synergy |
| part_accuracy_macro_bonus | 0.806987 | 0.815844 | 0.0088576 | synergy |
| exact_acc | 0.509639 | 0.52738 | 0.017741 | synergy |
| ranked_probability_score | 0.117621 | 0.112153 | -0.00546823 | synergy |
| bonus_total_score_log_loss | 1.0228 | 0.988394 | -0.0344098 | synergy |
| ppb_mae | 2.34918 | 1.80858 | -0.540596 | synergy |

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

## Bonus And Synergy Parameters

No bonus parameter distribution summary CSV was found.
