# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/compact-vs-332/compact/compact-terminal/seed_42/fold_2/evaluation`
Result root: `results/compirt/holdout/compact-vs-332/compact/compact-terminal/seed_42/fold_2`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 288974 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.707079 |
| log_loss | 0.534907 |
| ece | 0.0795498 |
| brier | 0.176374 |
| accuracy | 0.744302 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.0198768 |
| probability_std | 0.23119 |
| probability_p10 | 0.336122 |
| probability_p50 | 0.756847 |
| probability_p90 | 0.938325 |
| mean_predictive_variance | 0.159179 |
| integrated_brier_score | 0.0994914 |
| joint_tossup_event_log_loss | 6.49073 |
| buzz_position_mae | 0.149506 |
| buzz_position_median_absolute_error | 0.130601 |
| buzz_position_bias | -0.0476609 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.396673 |
| first_buzzer_mean_reciprocal_rank | 0.602998 |
| first_buzzer_log_loss | 1.56561 |
| first_buzzer_events | 9257 |
| neg_auroc | 0.707079 |
| neg_average_precision | 0.427285 |
| neg_precision | 0.450324 |
| neg_recall | 0.382043 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.17381 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.00863803 |
| no_buzz_calibration_error | -0.00447498 |
| no_buzz_brier | 0.012296 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.707079 | 0.534907 | 0.0795498 | 0.176374 | 0.744302 | 0.764178 | -0.0198768 | 0.23119 | 0.336122 | 0.756847 | 0.938325 | 0.159179 |
| tossup_correctness | tier | fall | 2798 | 0.724441 | 0.498259 | 0.0725584 | 0.161877 | 0.769121 | 0.785204 | -0.0160829 | 0.22107 | 0.377 | 0.774833 | 0.941255 | 0.15591 |
| tossup_correctness | tier | nationals | 1545 | 0.697693 | 0.577496 | 0.0726851 | 0.1949 | 0.697087 | 0.721036 | -0.0239482 | 0.222765 | 0.307846 | 0.693044 | 0.894696 | 0.178368 |
| tossup_correctness | tier | regionals | 2039 | 0.696429 | 0.553357 | 0.0952913 | 0.182979 | 0.738107 | 0.762138 | -0.0240314 | 0.239418 | 0.312463 | 0.747968 | 0.936131 | 0.159815 |
| tossup_correctness | tier | winter | 2875 | 0.698615 | 0.534602 | 0.0890069 | 0.175845 | 0.749913 | 0.768348 | -0.0184348 | 0.235512 | 0.333854 | 0.780089 | 0.948335 | 0.151597 |
| tossup_correctness | category | Current Events | 129 | 0.689562 | 0.588463 | 0.0703211 | 0.203558 | 0.689922 | 0.666667 | 0.0232558 | 0.219813 | 0.331811 | 0.719226 | 0.923092 | 0.168981 |
| tossup_correctness | category | Fine Arts | 1074 | 0.689968 | 0.529779 | 0.0928036 | 0.174991 | 0.752328 | 0.776536 | -0.0242086 | 0.223106 | 0.346977 | 0.754422 | 0.93268 | 0.163403 |
| tossup_correctness | category | Geography | 180 | 0.755582 | 0.553451 | 0.0737833 | 0.189365 | 0.705556 | 0.616667 | 0.0888889 | 0.263498 | 0.170044 | 0.696725 | 0.893947 | 0.166816 |
| tossup_correctness | category | History | 1454 | 0.691862 | 0.559035 | 0.0896112 | 0.184154 | 0.727648 | 0.757909 | -0.0302613 | 0.235062 | 0.314488 | 0.745934 | 0.940672 | 0.159363 |
| tossup_correctness | category | Literature | 1435 | 0.724407 | 0.484435 | 0.0733164 | 0.155545 | 0.773519 | 0.810453 | -0.0369338 | 0.229442 | 0.383782 | 0.813545 | 0.958685 | 0.140672 |
| tossup_correctness | category | Mythology | 324 | 0.681282 | 0.493542 | 0.0679328 | 0.159706 | 0.777778 | 0.79321 | -0.0154321 | 0.182559 | 0.465274 | 0.808637 | 0.928833 | 0.155452 |
| tossup_correctness | category | Other Academic | 71 | 0.683007 | 0.537922 | 0.110256 | 0.175842 | 0.746479 | 0.760563 | -0.0140845 | 0.177828 | 0.413116 | 0.735746 | 0.878457 | 0.182672 |
| tossup_correctness | category | Philosophy | 310 | 0.759963 | 0.491599 | 0.103565 | 0.162711 | 0.735484 | 0.76129 | -0.0258065 | 0.232596 | 0.317122 | 0.754994 | 0.940216 | 0.159196 |
| tossup_correctness | category | Popular Culture | 108 | 0.473958 | 0.401371 | 0.100557 | 0.116538 | 0.888889 | 0.888889 | 0 | 0.0945443 | 0.664238 | 0.824511 | 0.911899 | 0.147862 |
| tossup_correctness | category | Religion | 361 | 0.706066 | 0.55165 | 0.092514 | 0.184977 | 0.725762 | 0.742382 | -0.0166205 | 0.208457 | 0.336033 | 0.681351 | 0.896544 | 0.184085 |
| tossup_correctness | category | Science | 1445 | 0.703859 | 0.553644 | 0.077382 | 0.18488 | 0.737024 | 0.746021 | -0.00899654 | 0.232016 | 0.334325 | 0.740025 | 0.933719 | 0.163906 |
| tossup_correctness | category | Social Science | 327 | 0.733996 | 0.54379 | 0.0910721 | 0.180944 | 0.724771 | 0.718654 | 0.00611621 | 0.233408 | 0.292003 | 0.720625 | 0.912792 | 0.16759 |
| tossup_correctness | category | Unknown | 2039 | 0.696429 | 0.553357 | 0.0952913 | 0.182979 | 0.738107 | 0.762138 | -0.0240314 | 0.239418 | 0.312463 | 0.747968 | 0.936131 | 0.159815 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.751721 | 0.557042 | 0.148376 | 0.184967 | 0.704918 | 0.743169 | -0.0382514 | 0.23507 | 0.250774 | 0.634027 | 0.867074 | 0.185756 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.719334 | 0.543216 | 0.0750786 | 0.179359 | 0.746597 | 0.728796 | 0.017801 | 0.231421 | 0.311822 | 0.725631 | 0.917194 | 0.16749 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.712714 | 0.529885 | 0.065601 | 0.175608 | 0.748995 | 0.752568 | -0.00357302 | 0.225736 | 0.350753 | 0.769826 | 0.937221 | 0.156888 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.695031 | 0.515295 | 0.0746734 | 0.169493 | 0.751652 | 0.786087 | -0.0344348 | 0.219947 | 0.387511 | 0.786863 | 0.947328 | 0.152352 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.707784 | 0.553424 | 0.10246 | 0.182058 | 0.735441 | 0.764393 | -0.0289517 | 0.240481 | 0.298354 | 0.728494 | 0.935576 | 0.163157 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1197 | 2.86433 | 0.596584 | 1.0539 | 1.90844 | 2.44493 | 2.85948 | 3.2495 | 3.85796 | 4.67863 |
| player | theta_1 | 1197 | -1.27088 | 0.704555 | -3.18325 | -2.46634 | -1.80375 | -1.2373 | -0.75467 | -0.153806 | 0.361507 |
| player | theta_2 | 1197 | -1.26497 | 0.703558 | -3.07686 | -2.39142 | -1.78509 | -1.27193 | -0.789511 | -0.0511598 | 0.63068 |
| player | theta_3 | 1197 | -1.17254 | 0.684388 | -3.04603 | -2.26301 | -1.69036 | -1.16014 | -0.667775 | -0.0464932 | 0.685504 |
| player | theta_norm | 1197 | 2.34845 | 0.730707 | 0.438534 | 1.15594 | 1.8318 | 2.34315 | 2.84746 | 3.62614 | 4.2578 |
| tossup | start_difficulty | 1240 | -1.60982 | 0.729559 | -3.57565 | -2.77334 | -2.10072 | -1.6482 | -1.17376 | -0.3783 | 1.13178 |
| tossup | end_difficulty | 1240 | -3.54374 | 1.50099 | -9.32692 | -6.3307 | -4.40331 | -3.35089 | -2.48598 | -1.42497 | 0.429926 |
| tossup | total_drop | 1240 | 1.93392 | 1.13238 | 0.692757 | 0.909052 | 1.15934 | 1.48774 | 2.38216 | 4.41825 | 7.30685 |
| tossup | drop_share_1 | 1240 | 0.337121 | 0.0609461 | 0.10707 | 0.258429 | 0.303156 | 0.326501 | 0.357367 | 0.462928 | 0.656127 |
| tossup | drop_share_2 | 1240 | 0.352262 | 0.0300058 | 0.198452 | 0.310725 | 0.338129 | 0.350658 | 0.363746 | 0.401265 | 0.593878 |
| tossup | drop_share_3 | 1240 | 0.310618 | 0.0538 | 0.124418 | 0.208861 | 0.286146 | 0.317676 | 0.340849 | 0.383456 | 0.694478 |
| tossup | r_1 | 1240 | 0.924405 | 0.679194 | 0.0414465 | 0.133241 | 0.397785 | 0.748409 | 1.28212 | 2.2742 | 4.0412 |
| tossup | r_2 | 1240 | 0.923144 | 0.78971 | 0.0327991 | 0.118336 | 0.304709 | 0.658863 | 1.32664 | 2.62127 | 4.22233 |
| tossup | r_3 | 1240 | 0.777928 | 0.70504 | 0.03386 | 0.124935 | 0.29081 | 0.530465 | 0.971082 | 2.36796 | 3.6639 |
| tossup | r_norm | 1240 | 1.85717 | 0.666282 | 0.438749 | 0.885242 | 1.36124 | 1.79105 | 2.26498 | 3.05734 | 4.333 |
| tossup_hazard | hazard_start_difficulty | 1240 | 2.57309 | 0.563084 | 0.559753 | 1.66185 | 2.19334 | 2.57816 | 2.96209 | 3.51469 | 4.32714 |
| tossup_hazard | hazard_end_difficulty | 1240 | -1.61969 | 1.54866 | -7.3991 | -4.20915 | -2.59822 | -1.59484 | -0.507668 | 0.733901 | 2.04333 |
| tossup_hazard | hazard_total_drop | 1240 | 4.19279 | 1.54841 | 0.603786 | 1.56286 | 3.21583 | 4.22221 | 5.08423 | 6.84829 | 10.4581 |
| tossup_hazard | hazard_drop_share_1 | 1240 | 0.133329 | 0.0728606 | 0.0287859 | 0.0578795 | 0.0835653 | 0.113153 | 0.165436 | 0.26708 | 0.5635 |
| tossup_hazard | hazard_drop_share_2 | 1240 | 0.305103 | 0.138937 | 0.0566351 | 0.111993 | 0.191313 | 0.294021 | 0.392487 | 0.559964 | 0.763674 |
| tossup_hazard | hazard_drop_share_3 | 1240 | 0.561568 | 0.184469 | 0.0654804 | 0.239631 | 0.417648 | 0.585725 | 0.715163 | 0.82448 | 0.899614 |
