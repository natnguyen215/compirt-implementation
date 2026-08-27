# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/in_sample/baseline/all-2024/evaluation`
Result root: `results/compirt/in_sample/baseline/all-2024`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: in-sample fit.** Player and question parameters were estimated on the same observations these metrics score, so they are optimization and inspection diagnostics, not generalization estimates.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all 2024 |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 5000 |
| pyramidal | final_loss | 363263 |
| pyramidal | calibrate_correctness | False |
| compositional | tournament | all 2024 |
| compositional | dimensions | 5 |
| compositional | steps | 3000 |
| compositional | final_loss | 65784.5 |
| compositional | calibrate_correctness | False |
| compositional | synergy_dimensions | 0 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.175618 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.932678 |
| log_loss | 0.342423 |
| ece | 0.0411874 |
| brier | 0.105804 |
| part_accuracy | 0.852594 |
| part_all_correct_accuracy | 0.520489 |
| accuracy_lift_over_all_correct | 0.332105 |
| part_accuracy_macro_team | 0.855296 |
| part_accuracy_macro_bonus | 0.860211 |
| probability_std | 0.342499 |
| probability_p10 | 0.0750338 |
| probability_p50 | 0.475163 |
| probability_p90 | 0.954589 |
| mean_predictive_variance | 0.13266 |
| exact_acc | 0.612404 |
| ranked_probability_score | 0.0960612 |
| bonus_total_score_log_loss | 0.859128 |
| ppb_mae | 1.57744 |
| ranked_probability_score_responses | 44487 |
| bonus_total_score_log_loss_responses | 44487 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.701385 |
| log_loss | 0.579618 |
| ece | 0.149084 |
| brier | 0.195886 |
| accuracy | 0.705952 |
| all_correct_accuracy | 0.767271 |
| accuracy_lift_over_all_correct | -0.0613182 |
| probability_std | 0.239614 |
| probability_p10 | 0.249051 |
| probability_p50 | 0.668611 |
| probability_p90 | 0.895095 |
| mean_predictive_variance | 0.178617 |
| integrated_brier_score | 0.0904948 |
| joint_tossup_event_log_loss | 6.26439 |
| buzz_position_mae | 0.139008 |
| buzz_position_median_absolute_error | 0.121411 |
| buzz_position_bias | -0.0595034 |
| survival_events | 48612 |
| joint_tossup_event_log_loss_events | 48612 |
| first_buzzer_top1_accuracy | 0.489544 |
| first_buzzer_mean_reciprocal_rank | 0.677112 |
| first_buzzer_log_loss | 1.34911 |
| first_buzzer_events | 47914 |
| neg_auroc | 0.701385 |
| neg_average_precision | 0.42674 |
| neg_precision | 0.395579 |
| neg_recall | 0.499058 |
| full_pmf_events | 48612 |
| full_pmf_final_decile_mass | 0.0763893 |
| no_buzz_observed_rate | 0.0143586 |
| no_buzz_predicted_rate | 0.0808153 |
| no_buzz_calibration_error | 0.0664567 |
| no_buzz_brier | 0.0242857 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Match Winner Simulation

No match-simulation metrics CSV was found.

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 47914 | 0.701385 | 0.579618 | 0.149084 | 0.195886 | 0.705952 | 0.767271 | -0.0613182 | 0.239614 | 0.249051 | 0.668611 | 0.895095 | 0.178617 |
| tossup_correctness | tier | fall | 14760 | 0.70418 | 0.566194 | 0.160056 | 0.189981 | 0.718902 | 0.787466 | -0.0685637 | 0.241054 | 0.253446 | 0.681803 | 0.901547 | 0.17566 |
| tossup_correctness | tier | nationals | 7940 | 0.691545 | 0.585303 | 0.104199 | 0.199512 | 0.698363 | 0.72733 | -0.0289673 | 0.223319 | 0.284016 | 0.667312 | 0.881823 | 0.184968 |
| tossup_correctness | tier | regionals | 10202 | 0.706801 | 0.578042 | 0.143029 | 0.195613 | 0.704176 | 0.758969 | -0.0547932 | 0.24008 | 0.253301 | 0.662893 | 0.897561 | 0.17892 |
| tossup_correctness | tier | winter | 15012 | 0.702001 | 0.59088 | 0.166151 | 0.199959 | 0.698441 | 0.774181 | -0.0757394 | 0.245701 | 0.226097 | 0.660098 | 0.894306 | 0.177961 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 943 | 0.735664 | 0.833925 | 0.34074 | 0.296556 | 0.5228 | 0.727466 | -0.204666 | 0.23624 | 0.0797298 | 0.355305 | 0.727505 | 0.18136 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 4869 | 0.730458 | 0.765358 | 0.300675 | 0.269245 | 0.577942 | 0.736496 | -0.158554 | 0.2455 | 0.110208 | 0.426929 | 0.780037 | 0.185615 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 11467 | 0.72231 | 0.623558 | 0.202564 | 0.213353 | 0.67437 | 0.761053 | -0.0866835 | 0.25151 | 0.187651 | 0.589289 | 0.874376 | 0.183322 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 15035 | 0.712233 | 0.522379 | 0.120945 | 0.173267 | 0.743532 | 0.786033 | -0.0425008 | 0.217943 | 0.339448 | 0.71234 | 0.910339 | 0.175247 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 15600 | 0.69312 | 0.529139 | 0.0780034 | 0.175864 | 0.743974 | 0.765769 | -0.0217949 | 0.196688 | 0.399322 | 0.730937 | 0.90637 | 0.176058 |
| bonus_part_correctness | aggregate | all | 133461 | 0.932678 | 0.342423 | 0.0411874 | 0.105804 | 0.852594 | 0.520489 | 0.332105 | 0.342499 | 0.0750338 | 0.475163 | 0.954589 | 0.13266 |
| bonus_part_correctness | tier | fall | 42336 | 0.925312 | 0.350685 | 0.0358022 | 0.109981 | 0.842522 | 0.598828 | 0.243693 | 0.331618 | 0.108619 | 0.624404 | 0.9619 | 0.133575 |
| bonus_part_correctness | tier | nationals | 21051 | 0.937889 | 0.336467 | 0.0563385 | 0.101884 | 0.860909 | 0.428911 | 0.431998 | 0.325643 | 0.063504 | 0.301427 | 0.907249 | 0.136354 |
| bonus_part_correctness | tier | regionals | 27762 | 0.939895 | 0.328267 | 0.0487845 | 0.0999127 | 0.863158 | 0.483611 | 0.379548 | 0.34307 | 0.0695945 | 0.399132 | 0.949992 | 0.13157 |
| bonus_part_correctness | tier | winter | 42312 | 0.929241 | 0.346407 | 0.0353003 | 0.107442 | 0.851602 | 0.511864 | 0.339738 | 0.345513 | 0.0695458 | 0.459646 | 0.956337 | 0.13062 |
| bonus_part_correctness | category | Current Events | 1281 | 0.93713 | 0.336148 | 0.0437089 | 0.10238 | 0.857143 | 0.501952 | 0.355191 | 0.348849 | 0.057512 | 0.456093 | 0.938056 | 0.127766 |
| bonus_part_correctness | category | Fine Arts | 15525 | 0.918681 | 0.370725 | 0.0394138 | 0.116206 | 0.836135 | 0.507697 | 0.328438 | 0.332851 | 0.0774747 | 0.44703 | 0.946612 | 0.139081 |
| bonus_part_correctness | category | Geography | 2427 | 0.929586 | 0.345408 | 0.0486974 | 0.107171 | 0.856201 | 0.60033 | 0.255871 | 0.330501 | 0.0826089 | 0.63689 | 0.957872 | 0.134683 |
| bonus_part_correctness | category | History | 21273 | 0.932779 | 0.341124 | 0.0400855 | 0.10563 | 0.851737 | 0.555446 | 0.296291 | 0.340768 | 0.0772088 | 0.558515 | 0.956716 | 0.132318 |
| bonus_part_correctness | category | Literature | 21312 | 0.936354 | 0.332222 | 0.0421659 | 0.101767 | 0.86144 | 0.515813 | 0.345627 | 0.347154 | 0.0768668 | 0.460397 | 0.957836 | 0.129463 |
| bonus_part_correctness | category | Mythology | 4923 | 0.915637 | 0.368413 | 0.0379333 | 0.116681 | 0.8312 | 0.617713 | 0.213488 | 0.313788 | 0.152635 | 0.651411 | 0.95976 | 0.141796 |
| bonus_part_correctness | category | Other Academic | 1272 | 0.946271 | 0.31266 | 0.0439798 | 0.09427 | 0.871069 | 0.522799 | 0.34827 | 0.357173 | 0.0583523 | 0.498957 | 0.952588 | 0.122422 |
| bonus_part_correctness | category | Philosophy | 4989 | 0.920578 | 0.366426 | 0.0450896 | 0.114741 | 0.837041 | 0.491481 | 0.34556 | 0.332559 | 0.0812731 | 0.415152 | 0.948756 | 0.139055 |
| bonus_part_correctness | category | Popular Culture | 1536 | 0.910336 | 0.373796 | 0.0359335 | 0.119966 | 0.830078 | 0.622396 | 0.207682 | 0.322741 | 0.106726 | 0.615377 | 0.964763 | 0.137291 |
| bonus_part_correctness | category | Religion | 5280 | 0.932732 | 0.340589 | 0.0376049 | 0.105787 | 0.851894 | 0.505871 | 0.346023 | 0.348584 | 0.0591716 | 0.43964 | 0.952047 | 0.128374 |
| bonus_part_correctness | category | Science | 21183 | 0.931927 | 0.3439 | 0.0418371 | 0.10643 | 0.850304 | 0.529812 | 0.320493 | 0.342087 | 0.0799052 | 0.491694 | 0.95649 | 0.132742 |
| bonus_part_correctness | category | Social Science | 4698 | 0.938587 | 0.325345 | 0.0449639 | 0.100386 | 0.857599 | 0.476799 | 0.3808 | 0.35334 | 0.0556296 | 0.345305 | 0.953914 | 0.123557 |
| bonus_part_correctness | category | Unknown | 27762 | 0.939895 | 0.328267 | 0.0487845 | 0.0999127 | 0.863158 | 0.483611 | 0.379548 | 0.34307 | 0.0695945 | 0.399132 | 0.949992 | 0.13157 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## No-Synergy Versus Synergy Deltas

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.932678 | 0.939241 | 0.00656315 | synergy |
| log_loss | 0.342423 | 0.327827 | -0.0145957 | synergy |
| ece | 0.0411874 | 0.0435584 | 0.00237102 | no-synergy |
| part_accuracy | 0.852594 | 0.859008 | 0.00641386 | synergy |
| part_accuracy_macro_team | 0.855296 | 0.861651 | 0.00635508 | synergy |
| part_accuracy_macro_game | 0.852995 | 0.859364 | 0.00636888 | synergy |
| part_accuracy_macro_bonus | 0.860211 | 0.862927 | 0.00271542 | synergy |
| exact_acc | 0.612404 | 0.627015 | 0.014611 | synergy |
| ppb_mae | 1.57744 | 0.878661 | -0.698775 | synergy |

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1455 | 4.74177 | 1.02554 | 1.6814 | 2.6041 | 4.23823 | 4.99168 | 5.45991 | 6.00722 | 6.96045 |
| player | theta_1 | 1455 | 0.0514871 | 0.732826 | -2.27826 | -1.20026 | -0.480844 | 0.0727262 | 0.583654 | 1.1966 | 2.14132 |
| player | theta_2 | 1455 | -0.0977626 | 0.674036 | -2.34346 | -1.32009 | -0.515005 | -0.0656795 | 0.329034 | 1.00376 | 2.29596 |
| player | theta_3 | 1455 | 0.0781982 | 0.921686 | -3.25895 | -1.59361 | -0.487319 | 0.176611 | 0.747129 | 1.41908 | 2.3877 |
| player | theta_4 | 1455 | -0.113105 | 0.920372 | -2.63299 | -1.74513 | -0.743532 | -0.0316682 | 0.548065 | 1.28839 | 2.25273 |
| player | theta_5 | 1455 | -0.225188 | 0.709774 | -2.48771 | -1.4306 | -0.703884 | -0.194578 | 0.251767 | 0.940342 | 1.94621 |
| player | theta_norm | 1455 | 1.7133 | 0.579807 | 0.287633 | 0.872913 | 1.29688 | 1.66393 | 2.06672 | 2.76944 | 3.59256 |
| tossup | beta | 1260 | 3.36358 | 0.696832 | 0.365368 | 2.31451 | 3.00604 | 3.40145 | 3.80782 | 4.39127 | 5.74874 |
| tossup | gamma | 1260 | 51.3308 | 175.047 | 3.69545 | 5.63439 | 9.04839 | 12.8435 | 24.4688 | 180.907 | 2177.92 |
| tossup | mu | 1260 | 0.603627 | 0.133326 | 0.190116 | 0.379104 | 0.509968 | 0.609975 | 0.695831 | 0.818911 | 0.982927 |
| tossup | alpha_1 | 1260 | -0.177434 | 0.691993 | -2.50756 | -1.45001 | -0.622188 | -0.129886 | 0.274663 | 0.91949 | 2.02987 |
| tossup | alpha_2 | 1260 | 0.373332 | 0.643072 | -1.26797 | -0.575345 | -0.0671871 | 0.296642 | 0.75889 | 1.54912 | 3.35572 |
| tossup | alpha_3 | 1260 | 0.536921 | 0.782184 | -1.47804 | -0.610107 | -0.023626 | 0.424004 | 1.09822 | 1.94488 | 2.89414 |
| tossup | alpha_4 | 1260 | 0.721764 | 0.66541 | -1.08011 | -0.358458 | 0.263954 | 0.727278 | 1.18771 | 1.83134 | 2.82093 |
| tossup | alpha_5 | 1260 | 0.333625 | 0.657951 | -1.84656 | -0.685983 | -0.121316 | 0.277397 | 0.793698 | 1.42981 | 2.35236 |
| tossup | alpha_norm | 1260 | 1.80439 | 0.462311 | 0.478711 | 1.04603 | 1.49431 | 1.78086 | 2.11531 | 2.60161 | 3.43933 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 3768 | 0.848126 | 1.48751 | -2.26654 | -1.70636 | -0.400696 | 1.11769 | 2.10623 | 2.88737 | 3.76609 |
| bonus_part | alpha_1 | 3768 | -0.0594851 | 0.466306 | -2.30198 | -0.917601 | -0.305228 | -0.0253722 | 0.214588 | 0.650402 | 1.68749 |
| bonus_part | alpha_2 | 3768 | 0.154711 | 0.44882 | -1.50673 | -0.535773 | -0.0907983 | 0.109237 | 0.38802 | 0.926476 | 2.04415 |
| bonus_part | alpha_3 | 3768 | 0.128435 | 0.608996 | -1.68423 | -0.749586 | -0.342946 | 0.0572045 | 0.579638 | 1.15678 | 2.04234 |
| bonus_part | alpha_4 | 3768 | 0.195255 | 0.511859 | -1.70358 | -0.526773 | -0.158699 | 0.128697 | 0.526065 | 1.10995 | 2.22779 |
| bonus_part | alpha_5 | 3768 | 0.130029 | 0.492172 | -1.90903 | -0.618094 | -0.195115 | 0.105318 | 0.40134 | 1.0123 | 2.02069 |
| bonus_part | alpha_norm | 3768 | 1.07102 | 0.495613 | 0.123008 | 0.37017 | 0.692978 | 1.0144 | 1.37367 | 1.99027 | 2.83699 |
