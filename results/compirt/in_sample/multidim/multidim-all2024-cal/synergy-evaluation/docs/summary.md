# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/in_sample/multidim-all2024-cal/synergy-evaluation`
Result root: `results/compirt/in_sample/multidim-all2024-cal`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: in-sample fit.** Player and question parameters were estimated on the same observations these metrics score, so they are optimization and inspection diagnostics, not generalization estimates.

**Correctness calibration was fit on the scored outcomes.** This run learned a Platt scale/bias on the same split these metrics score, so tossup ECE and log loss are flattered by construction and are not comparable to uncalibrated runs.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all 2024 |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 341196 |
| pyramidal | calibrate_correctness | True |
| synergy | tournament | all 2024 |
| synergy | dimensions | 5 |
| synergy | steps | 2000 |
| synergy | final_loss | 64348.2 |
| synergy | calibrate_correctness | True |
| synergy | synergy_dimensions | 3 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.686067 |
| mean_synergy_contribution | 0.113098 |
| median_synergy_contribution | 0.0122685 |
| negative_synergy_fraction | 0.41565 |
| positive_synergy_fraction | 0.552948 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.937058 |
| log_loss | 0.329052 |
| ece | 0.0370202 |
| brier | 0.102179 |
| part_accuracy | 0.856939 |
| part_all_correct_accuracy | 0.520489 |
| accuracy_lift_over_all_correct | 0.33645 |
| ranked_probability_score | 0.0912963 |
| bonus_total_score_log_loss | 0.822843 |
| part_accuracy_macro_team | 0.859393 |
| part_accuracy_macro_game | 0.857336 |
| part_accuracy_macro_bonus | 0.860519 |
| exact_acc | 0.623261 |
| ppb_mae | 0.846956 |
| probability_std | 0.3592 |
| probability_p10 | 0.0444141 |
| probability_p50 | 0.465508 |
| probability_p90 | 0.968575 |
| mean_predictive_variance | 0.120946 |
| ranked_probability_score_responses | 44487 |
| bonus_total_score_log_loss_responses | 44487 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.655844 |
| log_loss | 0.514258 |
| ece | 0.0098768 |
| brier | 0.167994 |
| accuracy | 0.770234 |
| all_correct_accuracy | 0.767271 |
| accuracy_lift_over_all_correct | 0.00296364 |
| integrated_brier_score | 0.0836097 |
| first_buzzer_top1_accuracy | 0.49138 |
| first_buzzer_mean_reciprocal_rank | 0.678047 |
| first_buzzer_log_loss | 1.32475 |
| joint_tossup_event_log_loss | 5.99378 |
| buzz_position_mae | 0.129225 |
| buzz_position_median_absolute_error | 0.109887 |
| probability_std | 0.0903405 |
| probability_p10 | 0.648164 |
| probability_p50 | 0.786729 |
| probability_p90 | 0.870591 |
| mean_predictive_variance | 0.168544 |
| joint_tossup_event_log_loss_events | 48612 |
| survival_events | 48612 |
| survival_events_skipped | 0 |
| first_buzzer_events | 47914 |

## Match Winner Simulation

| metric | value |
| --- | --- |
| match_winner_accuracy | 0.800332 |
| match_winner_brier | 0.131467 |
| match_games | 2409 |
| match_simulations_per_game | 500 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 47914 | 0.655844 | 0.514258 | 0.0098768 | 0.167994 | 0.770234 | 0.767271 | 0.00296364 | 0.0903405 | 0.648164 | 0.786729 | 0.870591 | 0.168544 |
| tossup_correctness | tier | fall | 14760 | 0.665012 | 0.488466 | 0.0256506 | 0.156927 | 0.791192 | 0.787466 | 0.00372629 | 0.0874012 | 0.650436 | 0.784552 | 0.865887 | 0.16993 |
| tossup_correctness | tier | nationals | 7940 | 0.638786 | 0.569119 | 0.0509734 | 0.191158 | 0.728086 | 0.72733 | 0.000755668 | 0.0941059 | 0.645986 | 0.795543 | 0.88228 | 0.164163 |
| tossup_correctness | tier | regionals | 10202 | 0.655823 | 0.523133 | 0.016105 | 0.171745 | 0.764948 | 0.758969 | 0.00597922 | 0.0929111 | 0.649896 | 0.789599 | 0.87487 | 0.166556 |
| tossup_correctness | tier | winter | 15012 | 0.664729 | 0.504571 | 0.0162767 | 0.164073 | 0.775513 | 0.774181 | 0.00133227 | 0.0891114 | 0.645181 | 0.782023 | 0.865261 | 0.17085 |
| tossup_correctness | category | Current Events | 640 | 0.635369 | 0.555979 | 0.0251967 | 0.185513 | 0.739062 | 0.734375 | 0.0046875 | 0.0887191 | 0.630838 | 0.767888 | 0.856826 | 0.177269 |
| tossup_correctness | category | Fine Arts | 5640 | 0.659225 | 0.513242 | 0.00775746 | 0.167765 | 0.770745 | 0.766489 | 0.00425532 | 0.0900478 | 0.641397 | 0.78107 | 0.868077 | 0.170921 |
| tossup_correctness | category | Geography | 972 | 0.599913 | 0.628753 | 0.0707004 | 0.217698 | 0.680041 | 0.675926 | 0.00411523 | 0.0882547 | 0.627032 | 0.76111 | 0.849018 | 0.181387 |
| tossup_correctness | category | History | 7599 | 0.67477 | 0.511703 | 0.020813 | 0.167328 | 0.766811 | 0.764969 | 0.00184235 | 0.0879721 | 0.655888 | 0.790118 | 0.869415 | 0.167471 |
| tossup_correctness | category | Literature | 7469 | 0.633274 | 0.46977 | 0.0336481 | 0.148745 | 0.809881 | 0.812157 | -0.00227607 | 0.0935628 | 0.649866 | 0.79794 | 0.878898 | 0.163679 |
| tossup_correctness | category | Mythology | 1692 | 0.635795 | 0.477144 | 0.0593453 | 0.150592 | 0.807329 | 0.80792 | -0.000591017 | 0.0873053 | 0.639351 | 0.768954 | 0.856701 | 0.176713 |
| tossup_correctness | category | Other Academic | 357 | 0.63112 | 0.536827 | 0.0398132 | 0.17613 | 0.759104 | 0.756303 | 0.00280112 | 0.0860862 | 0.623172 | 0.760231 | 0.842446 | 0.181112 |
| tossup_correctness | category | Philosophy | 1649 | 0.685306 | 0.48918 | 0.029127 | 0.157496 | 0.788963 | 0.77926 | 0.00970285 | 0.0920089 | 0.640123 | 0.783817 | 0.866257 | 0.170272 |
| tossup_correctness | category | Popular Culture | 538 | 0.56347 | 0.439121 | 0.118238 | 0.133271 | 0.860595 | 0.864312 | -0.00371747 | 0.0767227 | 0.643281 | 0.754771 | 0.839075 | 0.183561 |
| tossup_correctness | category | Religion | 1889 | 0.679513 | 0.551907 | 0.033172 | 0.184513 | 0.728428 | 0.724722 | 0.00370566 | 0.08931 | 0.634243 | 0.771959 | 0.857286 | 0.175514 |
| tossup_correctness | category | Science | 7556 | 0.662264 | 0.529003 | 0.0266716 | 0.174368 | 0.757279 | 0.754235 | 0.00304394 | 0.0857799 | 0.661159 | 0.79273 | 0.87205 | 0.165728 |
| tossup_correctness | category | Social Science | 1711 | 0.649504 | 0.562709 | 0.035008 | 0.188725 | 0.727645 | 0.722385 | 0.00526008 | 0.0899676 | 0.631825 | 0.771305 | 0.859723 | 0.175655 |
| tossup_correctness | category | Unknown | 10202 | 0.655823 | 0.523133 | 0.016105 | 0.171745 | 0.764948 | 0.758969 | 0.00597922 | 0.0929111 | 0.649896 | 0.789599 | 0.87487 | 0.166556 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 943 | 0.685386 | 0.556833 | 0.0748726 | 0.185796 | 0.740191 | 0.727466 | 0.0127253 | 0.112011 | 0.508429 | 0.661153 | 0.801067 | 0.212948 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 4869 | 0.675029 | 0.543096 | 0.047533 | 0.180218 | 0.747381 | 0.736496 | 0.0108852 | 0.105552 | 0.549682 | 0.706412 | 0.821729 | 0.200899 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 11467 | 0.672104 | 0.516874 | 0.024424 | 0.169365 | 0.765588 | 0.761053 | 0.00453475 | 0.0931197 | 0.618624 | 0.758161 | 0.856838 | 0.180725 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 15035 | 0.667455 | 0.490002 | 0.0192452 | 0.157847 | 0.787496 | 0.786033 | 0.00146325 | 0.0775095 | 0.680541 | 0.792758 | 0.873752 | 0.163794 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 15600 | 0.650778 | 0.524139 | 0.0415871 | 0.171872 | 0.765962 | 0.765769 | 0.000192308 | 0.0643963 | 0.722536 | 0.815187 | 0.882133 | 0.151385 |
| bonus_part_correctness | aggregate | all | 133461 | 0.937058 | 0.329052 | 0.0370202 | 0.102179 | 0.856939 | 0.520489 | 0.33645 | 0.3592 | 0.0444141 | 0.465508 | 0.968575 | 0.120946 |
| bonus_part_correctness | tier | fall | 42336 | 0.929977 | 0.332877 | 0.0221395 | 0.105088 | 0.849206 | 0.598828 | 0.250378 | 0.354769 | 0.0701071 | 0.649133 | 0.98467 | 0.117207 |
| bonus_part_correctness | tier | nationals | 21051 | 0.943218 | 0.328267 | 0.0657812 | 0.0997548 | 0.864044 | 0.428911 | 0.435134 | 0.327864 | 0.0404289 | 0.274071 | 0.892785 | 0.130339 |
| bonus_part_correctness | tier | regionals | 27762 | 0.944772 | 0.32109 | 0.0555972 | 0.098494 | 0.864923 | 0.483611 | 0.381313 | 0.35067 | 0.0353875 | 0.365915 | 0.94223 | 0.123887 |
| bonus_part_correctness | tier | winter | 42312 | 0.934681 | 0.33084 | 0.0276402 | 0.102891 | 0.855904 | 0.511864 | 0.34404 | 0.363099 | 0.038949 | 0.451236 | 0.966881 | 0.118084 |
| bonus_part_correctness | category | Current Events | 1281 | 0.934788 | 0.330975 | 0.0291161 | 0.102526 | 0.857923 | 0.501952 | 0.355972 | 0.365448 | 0.0399989 | 0.466848 | 0.960476 | 0.116187 |
| bonus_part_correctness | category | Fine Arts | 15525 | 0.926172 | 0.351606 | 0.033179 | 0.110558 | 0.842899 | 0.507697 | 0.335201 | 0.353061 | 0.046187 | 0.43749 | 0.966804 | 0.125061 |
| bonus_part_correctness | category | Geography | 2427 | 0.931421 | 0.334063 | 0.0320082 | 0.103514 | 0.857849 | 0.60033 | 0.25752 | 0.348362 | 0.0636601 | 0.664591 | 0.975704 | 0.122221 |
| bonus_part_correctness | category | History | 21273 | 0.936464 | 0.326761 | 0.0325729 | 0.101836 | 0.856062 | 0.555446 | 0.300616 | 0.359894 | 0.0493054 | 0.558147 | 0.976642 | 0.119378 |
| bonus_part_correctness | category | Literature | 21312 | 0.942536 | 0.314795 | 0.0357506 | 0.0967485 | 0.867399 | 0.515813 | 0.351586 | 0.364566 | 0.0435999 | 0.449485 | 0.974472 | 0.11705 |
| bonus_part_correctness | category | Mythology | 4923 | 0.917018 | 0.359233 | 0.0333242 | 0.114542 | 0.833232 | 0.617713 | 0.215519 | 0.335088 | 0.0984023 | 0.646376 | 0.980185 | 0.129127 |
| bonus_part_correctness | category | Other Academic | 1272 | 0.945173 | 0.310251 | 0.0409244 | 0.0938773 | 0.876572 | 0.522799 | 0.353774 | 0.367411 | 0.0379348 | 0.48212 | 0.963646 | 0.114983 |
| bonus_part_correctness | category | Philosophy | 4989 | 0.93113 | 0.345038 | 0.0441185 | 0.107791 | 0.848266 | 0.491481 | 0.356785 | 0.348489 | 0.0465842 | 0.405169 | 0.960153 | 0.127423 |
| bonus_part_correctness | category | Popular Culture | 1536 | 0.908419 | 0.368376 | 0.0175687 | 0.119747 | 0.823568 | 0.622396 | 0.201172 | 0.33824 | 0.0994157 | 0.678629 | 0.988605 | 0.123038 |
| bonus_part_correctness | category | Religion | 5280 | 0.935517 | 0.330182 | 0.0319254 | 0.102506 | 0.854545 | 0.505871 | 0.348674 | 0.362762 | 0.0381817 | 0.4533 | 0.966716 | 0.118206 |
| bonus_part_correctness | category | Science | 21183 | 0.935206 | 0.330484 | 0.0312987 | 0.102893 | 0.853656 | 0.529812 | 0.323845 | 0.361348 | 0.0490822 | 0.495705 | 0.972507 | 0.119355 |
| bonus_part_correctness | category | Social Science | 4698 | 0.942752 | 0.309415 | 0.0292444 | 0.0956637 | 0.869093 | 0.476799 | 0.392295 | 0.370169 | 0.0311881 | 0.35118 | 0.971249 | 0.111112 |
| bonus_part_correctness | category | Unknown | 27762 | 0.944772 | 0.32109 | 0.0555972 | 0.098494 | 0.864923 | 0.483611 | 0.381313 | 0.35067 | 0.0353875 | 0.365915 | 0.94223 | 0.123887 |

## Posterior Predictive Checks

| stage | discrepancy | stratum | observed | replicated_mean | replicated_p05 | replicated_p95 | posterior_predictive_p_value | draws |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| compositional | bonus_score_mass | 0 | 0.074 | 0.0724 | 0.0577 | 0.0842 | 0.55 | 20 |
| compositional | bonus_score_mass | 10 | 0.442 | 0.4249 | 0.3895 | 0.4648 | 0.25 | 20 |
| compositional | bonus_score_mass | 20 | 0.378 | 0.3879 | 0.3555 | 0.4188 | 0.6 | 20 |
| compositional | bonus_score_mass | 30 | 0.106 | 0.1148 | 0.0955 | 0.136 | 0.75 | 20 |
| pyramidal | buzz_position_mass | Q1 | 0.0162602 | 0.063854 | 0.039353 | 0.0853154 | 1 | 20 |
| pyramidal | buzz_position_mass | Q2 | 0.0934959 | 0.0954616 | 0.0771949 | 0.114602 | 0.5 | 20 |
| pyramidal | buzz_position_mass | Q3 | 0.25813 | 0.23709 | 0.198619 | 0.27063 | 0.25 | 20 |
| pyramidal | buzz_position_mass | Q4 | 0.329268 | 0.349457 | 0.315317 | 0.392121 | 0.75 | 20 |
| pyramidal | buzz_position_mass | Q5 | 0.302846 | 0.254138 | 0.230915 | 0.283446 | 0 | 20 |
| pyramidal | dead_tossup_rate | all | 0.016 | 0.0735 | 0.0577 | 0.0928 | 1 | 20 |
| pyramidal | neg_rate | all | 0.254065 | 0.235827 | 0.208615 | 0.266438 | 0.15 | 20 |
| pyramidal | player_neg_rate | alec-riso | 0 | 0.297619 | 0 | 0.616667 | 1 | 7 |
| pyramidal | player_neg_rate | arunn-sankar | 0.25 | 0.157407 | 0 | 0.333333 | 0.555556 | 9 |
| pyramidal | player_neg_rate | biniam-alaro | 0 | 0.333333 | 0.333333 | 0.333333 | 1 | 2 |
| pyramidal | player_neg_rate | caleb-kendrick | 0 | 0.347222 | 0.0625 | 0.625 | 1 | 6 |
| pyramidal | player_neg_rate | cormac-beirne | 0 | 0.208333 | 0 | 0.666667 | 1 | 14 |
| pyramidal | player_neg_rate | daniel-chen | 0.666667 | 0.347222 | 0 | 0.875 | 0.166667 | 6 |
| pyramidal | player_neg_rate | henry-bylinowski | 0.4 | 0.187879 | 0 | 0.533333 | 0.181818 | 11 |
| pyramidal | player_neg_rate | jack-rado | 0 | 0.111111 | 0 | 0.333333 | 1 | 9 |
| pyramidal | player_neg_rate | jason-zhang | 0 | 0.333333 | 0.333333 | 0.333333 | 1 | 1 |
| pyramidal | player_neg_rate | jonathan-shauf | 0.333333 | 0.12037 | 0 | 0.433333 | 0.222222 | 9 |
| pyramidal | player_neg_rate | kevin-park | 0.333333 | 0.216667 | 0 | 0.466667 | 0.4 | 5 |
| pyramidal | player_neg_rate | liam-starnes | 0.333333 | 0.222222 | 0.0333333 | 0.333333 | 0.666667 | 3 |
| pyramidal | player_neg_rate | malachi-ledford | 0 | 0.127381 | 0 | 0.333333 | 1 | 14 |
| pyramidal | player_neg_rate | michal-gerasimiuk | 0.666667 | 0.555556 | 0.366667 | 0.666667 | 0.666667 | 3 |
| pyramidal | player_neg_rate | omer-keskin | 0 | 0.0833333 | 0 | 0.433333 | 1 | 15 |
| pyramidal | player_neg_rate | orion-keller | 0 | 0.189394 | 0 | 0.333333 | 1 | 11 |
| pyramidal | player_neg_rate | owen-ashbrook | 0 | 0.416667 | 0.341667 | 0.491667 | 1 | 2 |
| pyramidal | player_neg_rate | rohan-dalal | 0.25 | 0.161905 | 0 | 0.558333 | 0.285714 | 14 |
| pyramidal | player_neg_rate | sam-macchi | 0 | 0.192593 | 0 | 0.333333 | 1 | 9 |
| pyramidal | player_neg_rate | shardul-rao | 0.6 | 0.166667 | 0 | 0.583333 | 0.166667 | 6 |
| pyramidal | player_neg_rate | sinecio-morales | 0 | 0.197917 | 0 | 0.333333 | 1 | 8 |
| pyramidal | player_neg_rate | teigue-kelly | 0.333333 | 0.0833333 | 0 | 0.283333 | 0.25 | 4 |
| pyramidal | player_neg_rate | vedang-singhal | 0.333333 | 0.416667 | 0.341667 | 0.491667 | 1 | 2 |
| pyramidal | player_neg_rate | william-orr | 0 | 0.0740741 | 0 | 0.333333 | 1 | 9 |

## No-Synergy Versus Synergy Deltas

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.936507 | 0.937058 | 0.000551069 | synergy |
| log_loss | 0.330569 | 0.329052 | -0.00151681 | synergy |
| ece | 0.0390519 | 0.0370202 | -0.00203175 | synergy |
| brier | 0.10326 | 0.102179 | -0.00108093 | synergy |
| accuracy_lift_over_all_correct | 0.33385 | 0.33645 | 0.00260001 | synergy |
| part_accuracy | 0.854339 | 0.856939 | 0.00260001 | synergy |
| part_accuracy_macro_team | 0.85652 | 0.859393 | 0.00287372 | synergy |
| part_accuracy_macro_game | 0.854685 | 0.857336 | 0.00265074 | synergy |
| part_accuracy_macro_bonus | 0.861601 | 0.860519 | -0.00108124 | no-synergy |
| exact_acc | 0.617012 | 0.623261 | 0.00624902 | synergy |
| ranked_probability_score | 0.0938353 | 0.0912963 | -0.00253901 | synergy |
| bonus_total_score_log_loss | 0.836281 | 0.822843 | -0.0134378 | synergy |
| ppb_mae | 1.55185 | 0.846956 | -0.704891 | synergy |

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1455 | 1.05413 | 0.688304 | -1.05347 | 0.014952 | 0.649031 | 1.0189 | 1.44864 | 2.25705 | 4.59464 |
| player | theta_1 | 1455 | -0.371145 | 0.640879 | -2.90928 | -1.42984 | -0.788157 | -0.368479 | 0.0753891 | 0.633911 | 1.52804 |
| player | theta_2 | 1455 | -0.634934 | 0.691232 | -2.66794 | -1.75322 | -1.12023 | -0.645862 | -0.138417 | 0.473763 | 1.1912 |
| player | theta_3 | 1455 | -0.520303 | 0.67256 | -2.64785 | -1.5425 | -1.01041 | -0.53902 | -0.0418827 | 0.611571 | 1.56714 |
| player | theta_4 | 1455 | -0.510111 | 0.669465 | -2.67491 | -1.56783 | -0.978217 | -0.510508 | -0.0495145 | 0.586073 | 1.54086 |
| player | theta_5 | 1455 | -0.455029 | 0.641504 | -3.11384 | -1.47358 | -0.896924 | -0.455752 | -0.0178874 | 0.595426 | 1.92152 |
| player | theta_norm | 1455 | 1.77895 | 0.559888 | 0.337341 | 0.888184 | 1.35738 | 1.77616 | 2.17517 | 2.70914 | 3.72948 |
| tossup | beta_1 | 1260 | 0.809615 | 0.420388 | -0.620465 | 0.3273 | 0.535416 | 0.712073 | 0.992484 | 1.65486 | 2.67459 |
| tossup | beta_2 | 1260 | 0.94491 | 0.516681 | -0.205824 | 0.303876 | 0.565151 | 0.799518 | 1.28689 | 1.93161 | 2.98026 |
| tossup | beta_3 | 1260 | 0.853689 | 0.487554 | -0.961117 | 0.303287 | 0.520622 | 0.704542 | 1.06915 | 1.88366 | 3.04052 |
| tossup | beta_4 | 1260 | 0.894492 | 0.478514 | -0.504091 | 0.33048 | 0.546219 | 0.766382 | 1.17471 | 1.86867 | 2.98752 |
| tossup | beta_5 | 1260 | 0.834208 | 0.455232 | -0.358658 | 0.30387 | 0.523023 | 0.723812 | 1.02519 | 1.73812 | 2.98389 |
| tossup | gamma_1 | 1260 | 9.98194 | 42.7255 | 0.752633 | 2.87319 | 4.22003 | 4.96372 | 5.93967 | 15.9076 | 1007.66 |
| tossup | gamma_2 | 1260 | 14.8628 | 62.0162 | 0.731197 | 3.27278 | 4.44412 | 5.38024 | 7.20875 | 35.8005 | 1357.38 |
| tossup | gamma_3 | 1260 | 10.8872 | 40.8067 | 1.17231 | 3.21013 | 4.40117 | 5.16576 | 6.34684 | 19.9412 | 781.082 |
| tossup | gamma_4 | 1260 | 12.893 | 67.809 | 1.19732 | 3.13219 | 4.25592 | 5.15353 | 6.75168 | 24.0476 | 1606.67 |
| tossup | gamma_5 | 1260 | 11.4091 | 49.1266 | 1.52439 | 3.03094 | 4.25867 | 5.09137 | 6.22381 | 21.543 | 1059.43 |
| tossup | mu_1 | 1260 | 0.528944 | 0.106049 | 0.144601 | 0.4049 | 0.46755 | 0.50352 | 0.576547 | 0.736194 | 0.980527 |
| tossup | mu_2 | 1260 | 0.542402 | 0.124471 | 0.141331 | 0.397689 | 0.459884 | 0.509494 | 0.60496 | 0.793658 | 0.973608 |
| tossup | mu_3 | 1260 | 0.532761 | 0.116359 | 0.181542 | 0.404436 | 0.460891 | 0.500732 | 0.574181 | 0.789298 | 0.985584 |
| tossup | mu_4 | 1260 | 0.547804 | 0.122627 | 0.122723 | 0.407103 | 0.468692 | 0.510637 | 0.607852 | 0.813354 | 0.987019 |
| tossup | mu_5 | 1260 | 0.533657 | 0.110989 | 0.219157 | 0.406351 | 0.464006 | 0.505353 | 0.5869 | 0.747964 | 0.989746 |
| tossup | r_1 | 1260 | 1.18812 | 0.72348 | 0.134845 | 0.336334 | 0.654417 | 1.02097 | 1.54682 | 2.73333 | 3.75101 |
| tossup | r_2 | 1260 | 1.3944 | 0.819385 | 0.104833 | 0.369398 | 0.78331 | 1.19109 | 1.86116 | 3.00783 | 4.34349 |
| tossup | r_3 | 1260 | 1.25442 | 0.827084 | 0.108878 | 0.359827 | 0.693999 | 1.00412 | 1.56794 | 3.1072 | 4.95425 |
| tossup | r_4 | 1260 | 1.41126 | 0.87668 | 0.13679 | 0.365574 | 0.741453 | 1.17304 | 1.90488 | 3.2075 | 4.92462 |
| tossup | r_5 | 1260 | 1.16463 | 0.679619 | 0.105423 | 0.347908 | 0.692706 | 1.01004 | 1.49449 | 2.58973 | 4.36495 |
| tossup | r_norm | 1260 | 3.3025 | 0.691644 | 1.45443 | 2.20207 | 2.81447 | 3.28435 | 3.76207 | 4.49916 | 5.75939 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 3768 | 0.000270313 | 1.28682 | -2.76485 | -1.85924 | -1.15574 | -0.0680186 | 1.08103 | 2.06531 | 3.10561 |
| bonus_part | alpha_1 | 3768 | 0.147958 | 0.544381 | -1.91608 | -0.708397 | -0.174576 | 0.110715 | 0.437377 | 1.11271 | 2.57965 |
| bonus_part | alpha_2 | 3768 | 0.0789644 | 0.740396 | -2.16879 | -1.25797 | -0.459317 | 0.225062 | 0.651785 | 1.07059 | 2.48406 |
| bonus_part | alpha_3 | 3768 | 0.0768132 | 0.623259 | -2.00439 | -0.988687 | -0.35932 | 0.15613 | 0.491239 | 1.02524 | 2.50582 |
| bonus_part | alpha_4 | 3768 | 0.125995 | 0.639678 | -2.29254 | -0.938714 | -0.308279 | 0.166602 | 0.527694 | 1.19565 | 2.25068 |
| bonus_part | alpha_5 | 3768 | 0.110795 | 0.59759 | -2.15001 | -0.906031 | -0.303079 | 0.171427 | 0.512291 | 1.01996 | 2.37395 |
| bonus_part | alpha_norm | 3768 | 1.34945 | 0.489893 | 0.0986492 | 0.573964 | 1.00147 | 1.33111 | 1.67404 | 2.16111 | 3.08246 |
| synergy_player | psi_1 | 1455 | 0.00754858 | 0.292613 | -2.13447 | -0.445079 | -0.0630436 | 0.00372287 | 0.0686582 | 0.4959 | 1.52276 |
| synergy_player | psi_2 | 1455 | 0.00807284 | 0.276183 | -2.00042 | -0.396965 | -0.0576177 | 0.00132621 | 0.0641538 | 0.460541 | 1.30805 |
| synergy_player | psi_3 | 1455 | 0.00402411 | 0.303474 | -1.7909 | -0.449446 | -0.0671176 | -0.00111347 | 0.0594824 | 0.526716 | 1.55479 |
| synergy_player | psi_norm | 1455 | 0.395406 | 0.312539 | 0.00862383 | 0.0591736 | 0.149324 | 0.327202 | 0.527284 | 1.04387 | 2.13462 |
| synergy | synergy_score | 2521 | -0.00498913 | 0.29029 | -3.23661 | -0.493417 | -0.0432338 | 0.0115438 | 0.117941 | 0.341931 | 1.78502 |
| synergy | synergy_contribution | 44487 | 0.113098 | 0.71472 | -3.59059 | -1.02978 | -0.288088 | 0.0122685 | 0.589826 | 1.30489 | 2.45438 |
