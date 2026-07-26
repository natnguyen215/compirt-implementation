# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/multidim/multidim-all2024-gameinfill-5fold/fold_4/holdout/evaluation`
Result root: `results/compirt/holdout/multidim/multidim-all2024-gameinfill-5fold/fold_4`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 297638 |
| pyramidal | calibrate_correctness | False |
| compositional | tournament | all tournaments |
| compositional | dimensions | 5 |
| compositional | calibrate_correctness | False |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.148439 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.891115 |
| log_loss | 0.418661 |
| ece | 0.0260805 |
| brier | 0.133346 |
| part_accuracy | 0.810137 |
| part_all_correct_accuracy | 0.525555 |
| accuracy_lift_over_all_correct | 0.284582 |
| part_accuracy_macro_team | 0.814245 |
| part_accuracy_macro_bonus | 0.801593 |
| probability_std | 0.327596 |
| probability_p10 | 0.0853943 |
| probability_p50 | 0.467923 |
| probability_p90 | 0.933284 |
| mean_predictive_variance | 0.142681 |
| exact_acc | 0.514498 |
| ranked_probability_score | 0.117458 |
| bonus_total_score_log_loss | 1.02381 |
| ppb_mae | 2.32011 |
| ranked_probability_score_responses | 8622 |
| bonus_total_score_log_loss_responses | 8622 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.635744 |
| log_loss | 0.832833 |
| ece | 0.226928 |
| brier | 0.261801 |
| accuracy | 0.623517 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | -0.149838 |
| probability_std | 0.297878 |
| probability_p10 | 0.0894543 |
| probability_p50 | 0.613305 |
| probability_p90 | 0.913538 |
| mean_predictive_variance | 0.158042 |
| integrated_brier_score | 0.0950408 |
| joint_tossup_event_log_loss | 6.82337 |
| buzz_position_mae | 0.145527 |
| buzz_position_median_absolute_error | 0.127177 |
| buzz_position_bias | -0.040406 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.395146 |
| first_buzzer_mean_reciprocal_rank | 0.601402 |
| first_buzzer_log_loss | 1.62485 |
| first_buzzer_events | 9270 |

## Match Winner Simulation

| metric | value |
| --- | --- |
| match_winner_accuracy | 0.799569 |
| match_winner_brier | 0.142561 |
| match_games | 464 |
| match_simulations_per_game | 500 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.635744 | 0.832833 | 0.226928 | 0.261801 | 0.623517 | 0.773355 | -0.149838 | 0.297878 | 0.0894543 | 0.613305 | 0.913538 | 0.158042 |
| tossup_correctness | tier | fall | 2876 | 0.639197 | 0.825186 | 0.245352 | 0.259173 | 0.624478 | 0.793115 | -0.168637 | 0.294134 | 0.0859813 | 0.613091 | 0.910308 | 0.160301 |
| tossup_correctness | tier | nationals | 1579 | 0.636819 | 0.773812 | 0.176365 | 0.252036 | 0.633946 | 0.729576 | -0.0956301 | 0.29497 | 0.11906 | 0.648037 | 0.9303 | 0.156167 |
| tossup_correctness | tier | regionals | 1990 | 0.639241 | 0.85357 | 0.223428 | 0.263734 | 0.626131 | 0.765829 | -0.139698 | 0.303346 | 0.081775 | 0.60646 | 0.914885 | 0.155089 |
| tossup_correctness | tier | winter | 2825 | 0.635319 | 0.858998 | 0.244468 | 0.268572 | 0.614867 | 0.783009 | -0.168142 | 0.298522 | 0.0840095 | 0.597772 | 0.907862 | 0.15887 |
| tossup_correctness | category | Current Events | 123 | 0.665811 | 0.782202 | 0.257172 | 0.261576 | 0.593496 | 0.764228 | -0.170732 | 0.291921 | 0.0882371 | 0.60751 | 0.872398 | 0.164164 |
| tossup_correctness | category | Fine Arts | 1093 | 0.640885 | 0.858877 | 0.229514 | 0.267973 | 0.612077 | 0.769442 | -0.157365 | 0.30488 | 0.0780955 | 0.606361 | 0.910408 | 0.154928 |
| tossup_correctness | category | Geography | 191 | 0.563559 | 0.912076 | 0.239772 | 0.305957 | 0.518325 | 0.691099 | -0.172775 | 0.2751 | 0.0898841 | 0.546601 | 0.860322 | 0.174151 |
| tossup_correctness | category | History | 1469 | 0.658989 | 0.754552 | 0.196921 | 0.24319 | 0.646018 | 0.758339 | -0.112321 | 0.290793 | 0.110373 | 0.633383 | 0.916795 | 0.159869 |
| tossup_correctness | category | Literature | 1436 | 0.624775 | 0.848689 | 0.253441 | 0.259368 | 0.642061 | 0.81546 | -0.173398 | 0.307696 | 0.0857093 | 0.660536 | 0.934843 | 0.149054 |
| tossup_correctness | category | Mythology | 325 | 0.520896 | 1.00186 | 0.334144 | 0.307822 | 0.566154 | 0.843077 | -0.276923 | 0.290725 | 0.0750957 | 0.585237 | 0.881343 | 0.164562 |
| tossup_correctness | category | Other Academic | 67 | 0.644205 | 0.87095 | 0.283644 | 0.280805 | 0.61194 | 0.791045 | -0.179104 | 0.278888 | 0.0777937 | 0.559487 | 0.855891 | 0.172166 |
| tossup_correctness | category | Philosophy | 322 | 0.666609 | 0.78454 | 0.237351 | 0.256981 | 0.627329 | 0.785714 | -0.158385 | 0.304292 | 0.0824315 | 0.615131 | 0.920663 | 0.15431 |
| tossup_correctness | category | Popular Culture | 100 | 0.53524 | 0.938479 | 0.366562 | 0.299323 | 0.6 | 0.89 | -0.29 | 0.269271 | 0.0832973 | 0.589269 | 0.840109 | 0.176944 |
| tossup_correctness | category | Religion | 365 | 0.665092 | 0.768807 | 0.223183 | 0.249822 | 0.654795 | 0.723288 | -0.0684932 | 0.294005 | 0.101205 | 0.596703 | 0.906941 | 0.161869 |
| tossup_correctness | category | Science | 1456 | 0.615223 | 0.838068 | 0.221476 | 0.262784 | 0.614698 | 0.76717 | -0.152473 | 0.28747 | 0.104145 | 0.628866 | 0.907076 | 0.163408 |
| tossup_correctness | category | Social Science | 333 | 0.679012 | 0.763249 | 0.215664 | 0.250818 | 0.603604 | 0.72973 | -0.126126 | 0.288491 | 0.0822438 | 0.53655 | 0.90923 | 0.166173 |
| tossup_correctness | category | Unknown | 1990 | 0.639241 | 0.85357 | 0.223428 | 0.263734 | 0.626131 | 0.765829 | -0.139698 | 0.303346 | 0.081775 | 0.60646 | 0.914885 | 0.155089 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.706302 | 1.42672 | 0.508553 | 0.443521 | 0.329609 | 0.748603 | -0.418994 | 0.218536 | 0.0139669 | 0.178082 | 0.572547 | 0.136836 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.65773 | 1.19019 | 0.411394 | 0.372858 | 0.46395 | 0.754441 | -0.290491 | 0.264716 | 0.0256471 | 0.292104 | 0.734067 | 0.155291 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.66316 | 0.92448 | 0.291934 | 0.288219 | 0.577848 | 0.766682 | -0.188833 | 0.288978 | 0.0546759 | 0.489136 | 0.860245 | 0.165914 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.649067 | 0.731584 | 0.195902 | 0.235429 | 0.654802 | 0.787441 | -0.132639 | 0.279801 | 0.141187 | 0.659361 | 0.915116 | 0.162955 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.620591 | 0.714756 | 0.145586 | 0.221681 | 0.695564 | 0.771758 | -0.0761937 | 0.268891 | 0.219006 | 0.753587 | 0.942351 | 0.149391 |
| bonus_part_correctness | aggregate | all | 25866 | 0.891115 | 0.418661 | 0.0260805 | 0.133346 | 0.810137 | 0.525555 | 0.284582 | 0.327596 | 0.0853943 | 0.467923 | 0.933284 | 0.142681 |
| bonus_part_correctness | tier | fall | 8259 | 0.887172 | 0.417843 | 0.0315298 | 0.133278 | 0.810994 | 0.601283 | 0.209711 | 0.320589 | 0.116638 | 0.613097 | 0.940922 | 0.142357 |
| bonus_part_correctness | tier | nationals | 4167 | 0.873063 | 0.444235 | 0.0228154 | 0.142042 | 0.797216 | 0.438445 | 0.358771 | 0.314118 | 0.0723458 | 0.324059 | 0.891987 | 0.144412 |
| bonus_part_correctness | tier | regionals | 5457 | 0.890994 | 0.418644 | 0.0272306 | 0.13288 | 0.812901 | 0.493861 | 0.31904 | 0.323329 | 0.0823459 | 0.406836 | 0.922824 | 0.144581 |
| bonus_part_correctness | tier | winter | 7983 | 0.897761 | 0.406169 | 0.0245893 | 0.129197 | 0.814105 | 0.514343 | 0.299762 | 0.330365 | 0.0795741 | 0.45187 | 0.938156 | 0.140813 |
| bonus_part_correctness | category | Current Events | 258 | 0.87988 | 0.450476 | 0.0693102 | 0.145038 | 0.806202 | 0.515504 | 0.290698 | 0.352997 | 0.0692498 | 0.503771 | 0.924068 | 0.125155 |
| bonus_part_correctness | category | Fine Arts | 3000 | 0.883999 | 0.43053 | 0.0274748 | 0.137436 | 0.807 | 0.508 | 0.299 | 0.321269 | 0.0836509 | 0.436476 | 0.928968 | 0.146444 |
| bonus_part_correctness | category | Geography | 450 | 0.889069 | 0.413326 | 0.03933 | 0.130659 | 0.815556 | 0.582222 | 0.233333 | 0.321357 | 0.101703 | 0.653672 | 0.946054 | 0.138878 |
| bonus_part_correctness | category | History | 4116 | 0.893265 | 0.413693 | 0.0329765 | 0.132167 | 0.810739 | 0.562196 | 0.248542 | 0.328236 | 0.0911968 | 0.546952 | 0.935522 | 0.14121 |
| bonus_part_correctness | category | Literature | 4092 | 0.89186 | 0.414889 | 0.0253779 | 0.131497 | 0.814027 | 0.522727 | 0.2913 | 0.331155 | 0.0866614 | 0.454438 | 0.936271 | 0.140329 |
| bonus_part_correctness | category | Mythology | 951 | 0.875795 | 0.436094 | 0.0676894 | 0.141333 | 0.793901 | 0.647739 | 0.146162 | 0.296795 | 0.151749 | 0.607474 | 0.937856 | 0.15532 |
| bonus_part_correctness | category | Other Academic | 276 | 0.915151 | 0.376029 | 0.0423818 | 0.117876 | 0.822464 | 0.532609 | 0.289855 | 0.345784 | 0.0615937 | 0.54437 | 0.939218 | 0.130327 |
| bonus_part_correctness | category | Philosophy | 957 | 0.879963 | 0.436387 | 0.0352995 | 0.140791 | 0.793103 | 0.474399 | 0.318704 | 0.313115 | 0.0906041 | 0.412714 | 0.921347 | 0.151151 |
| bonus_part_correctness | category | Popular Culture | 300 | 0.891845 | 0.410377 | 0.0677009 | 0.132113 | 0.803333 | 0.616667 | 0.186667 | 0.304283 | 0.129311 | 0.612027 | 0.940971 | 0.150001 |
| bonus_part_correctness | category | Religion | 1029 | 0.903569 | 0.397608 | 0.050888 | 0.125818 | 0.813411 | 0.501458 | 0.311953 | 0.333866 | 0.0697341 | 0.435149 | 0.929366 | 0.138223 |
| bonus_part_correctness | category | Science | 4089 | 0.886109 | 0.425942 | 0.0230869 | 0.135926 | 0.806065 | 0.533382 | 0.272683 | 0.328595 | 0.0888732 | 0.497612 | 0.938094 | 0.141865 |
| bonus_part_correctness | category | Social Science | 891 | 0.908571 | 0.381792 | 0.037177 | 0.119891 | 0.830527 | 0.480359 | 0.350168 | 0.34258 | 0.0629467 | 0.33514 | 0.937579 | 0.130629 |
| bonus_part_correctness | category | Unknown | 5457 | 0.890994 | 0.418644 | 0.0272306 | 0.13288 | 0.812901 | 0.493861 | 0.31904 | 0.323329 | 0.0823459 | 0.406836 | 0.922824 | 0.144581 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## No-Synergy Versus Synergy Deltas

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.891115 | 0.897278 | 0.0061627 | synergy |
| log_loss | 0.418661 | 0.409088 | -0.00957274 | synergy |
| ece | 0.0260805 | 0.034084 | 0.00800349 | no-synergy |
| brier | 0.133346 | 0.130176 | -0.00317049 | synergy |
| accuracy_lift_over_all_correct | 0.284582 | 0.290497 | 0.0059151 | synergy |
| part_accuracy | 0.810137 | 0.816052 | 0.0059151 | synergy |
| part_accuracy_macro_team | 0.814245 | 0.822032 | 0.00778697 | synergy |
| part_accuracy_macro_bonus | 0.801593 | 0.808825 | 0.0072327 | synergy |
| exact_acc | 0.514498 | 0.529344 | 0.0148457 | synergy |
| ranked_probability_score | 0.117458 | 0.113478 | -0.00397957 | synergy |
| bonus_total_score_log_loss | 1.02381 | 1.00004 | -0.0237656 | synergy |
| ppb_mae | 2.32011 | 1.85769 | -0.462412 | synergy |

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1196 | 4.54997 | 1.19038 | 0.755633 | 2.01403 | 3.93783 | 4.76805 | 5.39668 | 6.07389 | 7.04246 |
| player | theta_1 | 1196 | 0.00458202 | 0.744024 | -2.27246 | -1.40525 | -0.447792 | 0.13521 | 0.538008 | 1.01896 | 1.87218 |
| player | theta_2 | 1196 | -0.0578906 | 0.734762 | -2.34554 | -1.49974 | -0.442506 | 0.0688121 | 0.435598 | 1.02416 | 1.73369 |
| player | theta_3 | 1196 | 0.101165 | 0.730378 | -2.28672 | -1.3705 | -0.288604 | 0.238302 | 0.589473 | 1.09938 | 1.99244 |
| player | theta_4 | 1196 | 0.0722369 | 0.749098 | -2.00711 | -1.33667 | -0.384272 | 0.168279 | 0.599966 | 1.16015 | 2.25413 |
| player | theta_5 | 1196 | 0.0470948 | 0.753814 | -2.60557 | -1.41789 | -0.340624 | 0.197347 | 0.586808 | 1.0557 | 1.77901 |
| player | theta_norm | 1196 | 1.55569 | 0.595954 | 0.370869 | 0.727278 | 1.10162 | 1.46555 | 1.9161 | 2.6845 | 3.64869 |
| tossup | beta_1 | 1240 | 0.757513 | 0.511162 | -0.177065 | 0.224624 | 0.412595 | 0.570981 | 0.980206 | 1.8662 | 2.64131 |
| tossup | beta_2 | 1240 | 0.825137 | 0.591244 | -1.41006 | 0.191781 | 0.409099 | 0.612744 | 1.19126 | 2.02815 | 2.90349 |
| tossup | beta_3 | 1240 | 0.761432 | 0.528288 | -1.16599 | 0.2323 | 0.423371 | 0.58772 | 0.946694 | 1.8767 | 3.22575 |
| tossup | beta_4 | 1240 | 0.751043 | 0.544923 | -0.564274 | 0.208155 | 0.392655 | 0.567788 | 0.916692 | 1.96497 | 3.16604 |
| tossup | beta_5 | 1240 | 0.799192 | 0.564512 | -2.08066 | 0.216911 | 0.399337 | 0.605614 | 1.10313 | 1.96513 | 2.87292 |
| tossup | gamma_1 | 1240 | 12.0803 | 58.8523 | 1.23643 | 3.26519 | 4.52144 | 5.16538 | 6.18421 | 25.6578 | 1754.22 |
| tossup | gamma_2 | 1240 | 14.0757 | 87.2651 | 0.666491 | 3.37511 | 4.53294 | 5.19899 | 6.35576 | 23.1875 | 2015.44 |
| tossup | gamma_3 | 1240 | 12.1753 | 52.7879 | 0.659095 | 3.08173 | 4.41629 | 5.07974 | 5.96383 | 23.9317 | 899.58 |
| tossup | gamma_4 | 1240 | 12.1984 | 68.974 | 1.13946 | 3.39457 | 4.52232 | 5.13221 | 6.01802 | 19.3785 | 1952.22 |
| tossup | gamma_5 | 1240 | 13.3965 | 66.5748 | 0.320288 | 3.14911 | 4.48781 | 5.15492 | 6.2309 | 23.0295 | 1369.53 |
| tossup | mu_1 | 1240 | 0.499665 | 0.10164 | 0.123771 | 0.381552 | 0.444542 | 0.477845 | 0.518636 | 0.720475 | 0.967239 |
| tossup | mu_2 | 1240 | 0.516087 | 0.121359 | 0.197173 | 0.388721 | 0.443251 | 0.479177 | 0.557108 | 0.784651 | 0.986612 |
| tossup | mu_3 | 1240 | 0.511427 | 0.110867 | 0.149438 | 0.394633 | 0.452392 | 0.483676 | 0.533618 | 0.752055 | 0.98678 |
| tossup | mu_4 | 1240 | 0.506199 | 0.10821 | 0.13041 | 0.396479 | 0.448942 | 0.478409 | 0.520903 | 0.737609 | 0.986083 |
| tossup | mu_5 | 1240 | 0.512624 | 0.110865 | 0.183058 | 0.387809 | 0.4505 | 0.483884 | 0.545325 | 0.744969 | 0.969381 |
| tossup | r_1 | 1240 | 1.02566 | 0.771601 | 0.0913207 | 0.22373 | 0.453748 | 0.786396 | 1.40349 | 2.6002 | 4.45314 |
| tossup | r_2 | 1240 | 1.28172 | 1.02896 | 0.106963 | 0.226863 | 0.503656 | 0.93604 | 1.81094 | 3.39087 | 5.60102 |
| tossup | r_3 | 1240 | 1.07098 | 0.919737 | 0.0822656 | 0.222704 | 0.445123 | 0.760051 | 1.40345 | 3.13018 | 6.66325 |
| tossup | r_4 | 1240 | 1.06804 | 0.934401 | 0.0735487 | 0.219274 | 0.425088 | 0.720454 | 1.31326 | 3.14052 | 5.58356 |
| tossup | r_5 | 1240 | 1.10334 | 0.80038 | 0.09183 | 0.227277 | 0.477379 | 0.860249 | 1.55709 | 2.80485 | 4.00117 |
| tossup | r_norm | 1240 | 3.0899 | 0.814491 | 1.03259 | 1.92507 | 2.52056 | 2.97569 | 3.57754 | 4.57026 | 6.90569 |

## Bonus And Synergy Parameters

No bonus parameter distribution summary CSV was found.
