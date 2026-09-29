# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/training/incorrect-loss-weight/weight-2/fold_0/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/training/incorrect-loss-weight/weight-2/fold_0`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 291621 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.714452 |
| log_loss | 0.525175 |
| ece | 0.109364 |
| brier | 0.174086 |
| accuracy | 0.748467 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | -0.0167832 |
| probability_std | 0.189819 |
| probability_p10 | 0.374867 |
| probability_p50 | 0.69226 |
| probability_p90 | 0.875273 |
| mean_predictive_variance | 0.189668 |
| integrated_brier_score | 0.102004 |
| joint_tossup_event_log_loss | 6.65158 |
| buzz_position_mae | 0.15233 |
| buzz_position_median_absolute_error | 0.135818 |
| buzz_position_bias | -0.0426218 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |
| first_buzzer_top1_accuracy | 0.355245 |
| first_buzzer_mean_reciprocal_rank | 0.568737 |
| first_buzzer_log_loss | 1.66509 |
| first_buzzer_events | 9295 |
| neg_auroc | 0.714452 |
| neg_average_precision | 0.444057 |
| neg_precision | 0.459877 |
| neg_recall | 0.409716 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.187897 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.0159069 |
| no_buzz_calibration_error | 0.00263731 |
| no_buzz_brier | 0.0130831 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.714452 | 0.525175 | 0.109364 | 0.174086 | 0.748467 | 0.76525 | -0.0167832 | 0.189819 | 0.374867 | 0.69226 | 0.875273 | 0.189668 |
| tossup_correctness | tier | fall | 2933 | 0.712139 | 0.506808 | 0.12141 | 0.166533 | 0.763723 | 0.791681 | -0.0279577 | 0.191058 | 0.383856 | 0.71199 | 0.887107 | 0.184447 |
| tossup_correctness | tier | nationals | 1584 | 0.708861 | 0.553188 | 0.0921213 | 0.185798 | 0.728535 | 0.724747 | 0.00378788 | 0.199031 | 0.339209 | 0.681844 | 0.866445 | 0.192313 |
| tossup_correctness | tier | regionals | 1886 | 0.707555 | 0.547487 | 0.106789 | 0.183974 | 0.723754 | 0.746023 | -0.0222694 | 0.183845 | 0.376604 | 0.665094 | 0.858779 | 0.196815 |
| tossup_correctness | tier | winter | 2892 | 0.719166 | 0.513908 | 0.109436 | 0.168884 | 0.760028 | 0.773167 | -0.0131397 | 0.185302 | 0.39264 | 0.695649 | 0.877433 | 0.188855 |
| tossup_correctness | category | Current Events | 124 | 0.685397 | 0.57516 | 0.164272 | 0.195156 | 0.725806 | 0.75 | -0.0241935 | 0.207063 | 0.349721 | 0.611028 | 0.876647 | 0.193551 |
| tossup_correctness | category | Fine Arts | 1103 | 0.711298 | 0.524808 | 0.101892 | 0.173515 | 0.743427 | 0.759746 | -0.0163191 | 0.192237 | 0.383325 | 0.701673 | 0.878777 | 0.186509 |
| tossup_correctness | category | Geography | 197 | 0.786713 | 0.551312 | 0.120645 | 0.182489 | 0.751269 | 0.670051 | 0.0812183 | 0.236471 | 0.222187 | 0.592877 | 0.850423 | 0.190343 |
| tossup_correctness | category | History | 1491 | 0.721086 | 0.510967 | 0.126682 | 0.168535 | 0.761234 | 0.787391 | -0.0261569 | 0.187544 | 0.3865 | 0.693486 | 0.883844 | 0.189 |
| tossup_correctness | category | Literature | 1472 | 0.726876 | 0.466047 | 0.0966511 | 0.147991 | 0.800951 | 0.804348 | -0.00339674 | 0.166617 | 0.462083 | 0.74436 | 0.888657 | 0.179101 |
| tossup_correctness | category | Mythology | 332 | 0.689964 | 0.489971 | 0.125772 | 0.157919 | 0.774096 | 0.813253 | -0.0391566 | 0.165859 | 0.447364 | 0.725009 | 0.872233 | 0.185738 |
| tossup_correctness | category | Other Academic | 69 | 0.684389 | 0.550823 | 0.124995 | 0.184493 | 0.753623 | 0.753623 | 0 | 0.144514 | 0.432367 | 0.648784 | 0.814312 | 0.210631 |
| tossup_correctness | category | Philosophy | 324 | 0.690882 | 0.515698 | 0.134906 | 0.170553 | 0.756173 | 0.799383 | -0.0432099 | 0.179151 | 0.400147 | 0.699317 | 0.879045 | 0.190628 |
| tossup_correctness | category | Popular Culture | 102 | 0.456055 | 0.518386 | 0.139102 | 0.165036 | 0.803922 | 0.833333 | -0.0294118 | 0.117185 | 0.579505 | 0.749804 | 0.85027 | 0.179028 |
| tossup_correctness | category | Religion | 372 | 0.715593 | 0.566454 | 0.103476 | 0.193311 | 0.688172 | 0.709677 | -0.0215054 | 0.193423 | 0.32718 | 0.625583 | 0.844344 | 0.201309 |
| tossup_correctness | category | Science | 1487 | 0.690582 | 0.553136 | 0.113897 | 0.186821 | 0.72764 | 0.752522 | -0.0248823 | 0.199451 | 0.344884 | 0.673592 | 0.874138 | 0.190927 |
| tossup_correctness | category | Social Science | 336 | 0.726017 | 0.560722 | 0.0934458 | 0.189057 | 0.732143 | 0.702381 | 0.0297619 | 0.215677 | 0.301143 | 0.654176 | 0.867099 | 0.190789 |
| tossup_correctness | category | Unknown | 1886 | 0.707555 | 0.547487 | 0.106789 | 0.183974 | 0.723754 | 0.746023 | -0.0222694 | 0.183845 | 0.376604 | 0.665094 | 0.858779 | 0.196815 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.690186 | 0.578052 | 0.169906 | 0.1916 | 0.751269 | 0.736041 | 0.0152284 | 0.190459 | 0.329395 | 0.62351 | 0.846167 | 0.202317 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.713157 | 0.544848 | 0.0946757 | 0.183264 | 0.715736 | 0.735025 | -0.0192893 | 0.190972 | 0.359098 | 0.678239 | 0.862354 | 0.193735 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.700646 | 0.528863 | 0.105798 | 0.175188 | 0.757441 | 0.769436 | -0.0119947 | 0.185854 | 0.395641 | 0.694517 | 0.877776 | 0.188681 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.702582 | 0.511569 | 0.109449 | 0.168194 | 0.763084 | 0.78402 | -0.0209351 | 0.182467 | 0.407618 | 0.713331 | 0.882308 | 0.186173 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.735403 | 0.525474 | 0.116062 | 0.174725 | 0.738318 | 0.756008 | -0.0176903 | 0.196835 | 0.348122 | 0.679975 | 0.869437 | 0.191586 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1186 | 2.67182 | 0.763253 | 0.496364 | 1.44277 | 2.14627 | 2.6698 | 3.18102 | 3.98203 | 4.65225 |
| player | theta_1 | 1186 | -1.21996 | 0.909017 | -3.7136 | -2.63107 | -1.79119 | -1.25579 | -0.6865 | 0.384007 | 2.42584 |
| player | theta_2 | 1186 | -1.0441 | 0.722878 | -3.72708 | -2.2 | -1.48299 | -1.07301 | -0.5718 | 0.119367 | 1.31197 |
| player | theta_3 | 1186 | -1.12978 | 0.824278 | -3.5588 | -2.43469 | -1.67863 | -1.19225 | -0.63152 | 0.299737 | 2.33743 |
| player | theta_norm | 1186 | 2.32206 | 0.699924 | 0.456412 | 1.24447 | 1.84357 | 2.26725 | 2.77445 | 3.5093 | 4.70493 |
| tossup | start_difficulty_d1 | 1240 | -1.12479 | 0.634288 | -3.68248 | -2.01459 | -1.54161 | -1.17584 | -0.756542 | -0.0603749 | 1.90238 |
| tossup | start_difficulty_d2 | 1240 | -1.11109 | 0.582774 | -2.93962 | -2.0334 | -1.48321 | -1.15372 | -0.753856 | -0.0553943 | 1.20677 |
| tossup | start_difficulty_d3 | 1240 | -1.10912 | 0.586267 | -3.50272 | -2.03624 | -1.51432 | -1.13015 | -0.748028 | -0.13935 | 2.2214 |
| tossup | end_difficulty_d1 | 1240 | -2.11899 | 0.741092 | -4.98254 | -3.22296 | -2.5779 | -2.16541 | -1.67318 | -0.896726 | 1.32073 |
| tossup | end_difficulty_d2 | 1240 | -2.0988 | 0.684059 | -4.35788 | -3.17894 | -2.52889 | -2.13345 | -1.69152 | -0.859524 | 0.59061 |
| tossup | end_difficulty_d3 | 1240 | -2.09393 | 0.68379 | -4.9269 | -3.17071 | -2.55778 | -2.10318 | -1.65959 | -1.00119 | 1.53325 |
| tossup | total_drop_d1 | 1240 | 0.9942 | 0.149316 | 0.581648 | 0.773952 | 0.904829 | 0.989691 | 1.07506 | 1.21543 | 2.41229 |
| tossup | total_drop_d2 | 1240 | 0.987712 | 0.126504 | 0.607718 | 0.786745 | 0.910458 | 0.986409 | 1.06035 | 1.19955 | 1.84113 |
| tossup | total_drop_d3 | 1240 | 0.984815 | 0.127328 | 0.577462 | 0.791087 | 0.901212 | 0.981604 | 1.06058 | 1.21221 | 1.55046 |
| tossup | drop_share_1_d1 | 1240 | 0.302476 | 0.01952 | 0.191764 | 0.270749 | 0.291691 | 0.30348 | 0.314514 | 0.331112 | 0.383439 |
| tossup | drop_share_2_d1 | 1240 | 0.347248 | 0.0126727 | 0.307359 | 0.326391 | 0.339072 | 0.347341 | 0.355565 | 0.36741 | 0.4398 |
| tossup | drop_share_3_d1 | 1240 | 0.350276 | 0.0205405 | 0.287052 | 0.319959 | 0.337144 | 0.349042 | 0.361856 | 0.385394 | 0.456479 |
| tossup | drop_share_1_d2 | 1240 | 0.302445 | 0.0165164 | 0.22178 | 0.27442 | 0.29245 | 0.303298 | 0.31351 | 0.327541 | 0.359835 |
| tossup | drop_share_2_d2 | 1240 | 0.346944 | 0.0122691 | 0.306689 | 0.327271 | 0.338963 | 0.346797 | 0.354871 | 0.366284 | 0.410227 |
| tossup | drop_share_3_d2 | 1240 | 0.350611 | 0.0184772 | 0.292751 | 0.321169 | 0.33873 | 0.350766 | 0.361262 | 0.380388 | 0.441176 |
| tossup | drop_share_1_d3 | 1240 | 0.302332 | 0.0178064 | 0.225366 | 0.274188 | 0.291356 | 0.303064 | 0.31355 | 0.330209 | 0.375745 |
| tossup | drop_share_2_d3 | 1240 | 0.347122 | 0.0118754 | 0.302278 | 0.328027 | 0.339589 | 0.347016 | 0.354919 | 0.366644 | 0.398111 |
| tossup | drop_share_3_d3 | 1240 | 0.350546 | 0.0190095 | 0.293397 | 0.322445 | 0.338145 | 0.350073 | 0.360608 | 0.382281 | 0.454203 |
| tossup | r_1 | 1240 | 0.337141 | 0.195143 | 0.0446545 | 0.0952563 | 0.176858 | 0.288739 | 0.475127 | 0.712195 | 0.827478 |
| tossup | r_2 | 1240 | 0.326338 | 0.169006 | 0.0502062 | 0.108234 | 0.192213 | 0.295241 | 0.428154 | 0.653726 | 0.864101 |
| tossup | r_3 | 1240 | 0.336521 | 0.174133 | 0.0595693 | 0.109554 | 0.198349 | 0.306593 | 0.446807 | 0.67428 | 0.892346 |
| tossup | r_norm | 1240 | 0.652974 | 0.0626384 | 0.577607 | 0.582495 | 0.603797 | 0.636669 | 0.688776 | 0.785091 | 0.895681 |
| tossup_hazard | hazard_start_difficulty_d1 | 1240 | 4.47412 | 0.49936 | 1.72175 | 3.70235 | 4.19771 | 4.43326 | 4.73223 | 5.41232 | 6.34675 |
| tossup_hazard | hazard_start_difficulty_d2 | 1240 | 4.44709 | 0.436846 | 2.77568 | 3.74094 | 4.21748 | 4.41821 | 4.66045 | 5.18585 | 6.62025 |
| tossup_hazard | hazard_start_difficulty_d3 | 1240 | 4.46545 | 0.439604 | 2.56903 | 3.7561 | 4.22901 | 4.45049 | 4.70247 | 5.20499 | 6.25952 |
| tossup_hazard | hazard_end_difficulty_d1 | 1240 | 1.73088 | 2.34395 | -11.7398 | -3.25738 | 0.636553 | 2.85515 | 3.29061 | 3.64915 | 4.48839 |
| tossup_hazard | hazard_end_difficulty_d2 | 1240 | 2.23988 | 2.09535 | -8.41993 | -2.7466 | 2.33317 | 3.10707 | 3.36762 | 3.71296 | 4.30644 |
| tossup_hazard | hazard_end_difficulty_d3 | 1240 | 2.21882 | 2.18806 | -10.3797 | -2.97415 | 2.26353 | 3.1259 | 3.39823 | 3.74017 | 4.22408 |
| tossup_hazard | hazard_total_drop_d1 | 1240 | 2.74324 | 2.51574 | 0.884776 | 0.982335 | 1.0555 | 1.33332 | 4.09832 | 8.10957 | 16.4433 |
| tossup_hazard | hazard_total_drop_d2 | 1240 | 2.20721 | 2.2514 | 0.889138 | 0.959031 | 1.02299 | 1.17495 | 1.86586 | 7.64572 | 13.7515 |
| tossup_hazard | hazard_total_drop_d3 | 1240 | 2.24663 | 2.323 | 0.849477 | 0.966418 | 1.0266 | 1.17681 | 1.87941 | 7.5502 | 14.8209 |
| tossup_hazard | hazard_drop_share_1_d1 | 1240 | 0.236987 | 0.0799714 | 0.0419163 | 0.0821258 | 0.175788 | 0.270317 | 0.294341 | 0.317252 | 0.538171 |
| tossup_hazard | hazard_drop_share_2_d1 | 1240 | 0.342636 | 0.0728259 | 0.0607897 | 0.189345 | 0.335135 | 0.351137 | 0.365434 | 0.440231 | 0.712905 |
| tossup_hazard | hazard_drop_share_3_d1 | 1240 | 0.420377 | 0.127624 | 0.134567 | 0.311645 | 0.348668 | 0.369942 | 0.44347 | 0.723219 | 0.89513 |
| tossup_hazard | hazard_drop_share_1_d2 | 1240 | 0.252261 | 0.0703645 | 0.0304456 | 0.0887133 | 0.230987 | 0.279728 | 0.296591 | 0.314519 | 0.599398 |
| tossup_hazard | hazard_drop_share_2_d2 | 1240 | 0.348223 | 0.0631433 | 0.0671362 | 0.222711 | 0.340755 | 0.35145 | 0.363871 | 0.421742 | 0.689565 |
| tossup_hazard | hazard_drop_share_3_d2 | 1240 | 0.399516 | 0.10756 | 0.100258 | 0.318694 | 0.349913 | 0.36504 | 0.399535 | 0.67195 | 0.888987 |
| tossup_hazard | hazard_drop_share_1_d3 | 1240 | 0.251115 | 0.0699765 | 0.0359215 | 0.0881745 | 0.231663 | 0.276632 | 0.296519 | 0.315232 | 0.572632 |
| tossup_hazard | hazard_drop_share_2_d3 | 1240 | 0.348766 | 0.0618242 | 0.0932111 | 0.237144 | 0.339538 | 0.351323 | 0.363702 | 0.427177 | 0.704005 |
| tossup_hazard | hazard_drop_share_3_d3 | 1240 | 0.400119 | 0.105859 | 0.130249 | 0.319096 | 0.349361 | 0.366333 | 0.400344 | 0.670227 | 0.870867 |
| tossup_hazard | hazard_r_1 | 1240 | 0.382336 | 0.273282 | 0.0322958 | 0.0574066 | 0.133349 | 0.316751 | 0.606342 | 0.871159 | 0.935993 |
| tossup_hazard | hazard_r_2 | 1240 | 0.302903 | 0.217306 | 0.025174 | 0.0509034 | 0.113546 | 0.244913 | 0.467337 | 0.717259 | 0.86072 |
| tossup_hazard | hazard_r_3 | 1240 | 0.314762 | 0.229283 | 0.0225764 | 0.0491846 | 0.133105 | 0.249717 | 0.456534 | 0.776125 | 0.938977 |
