# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/compact-vs-332/compact/compact-terminal/seed_42/fold_0/evaluation`
Result root: `results/compirt/holdout/compact-vs-332/compact/compact-terminal/seed_42/fold_0`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 288815 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.711796 |
| log_loss | 0.527693 |
| ece | 0.0772385 |
| brier | 0.173512 |
| accuracy | 0.752232 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | -0.0130178 |
| probability_std | 0.232061 |
| probability_p10 | 0.341679 |
| probability_p50 | 0.764407 |
| probability_p90 | 0.941542 |
| mean_predictive_variance | 0.156674 |
| integrated_brier_score | 0.0990541 |
| joint_tossup_event_log_loss | 6.46783 |
| buzz_position_mae | 0.149467 |
| buzz_position_median_absolute_error | 0.130812 |
| buzz_position_bias | -0.0490806 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |
| first_buzzer_top1_accuracy | 0.400108 |
| first_buzzer_mean_reciprocal_rank | 0.606797 |
| first_buzzer_log_loss | 1.55805 |
| first_buzzer_events | 9295 |
| neg_auroc | 0.711796 |
| neg_average_precision | 0.43706 |
| neg_precision | 0.466593 |
| neg_recall | 0.387259 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.169002 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.00928608 |
| no_buzz_calibration_error | -0.00398356 |
| no_buzz_brier | 0.012487 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.711796 | 0.527693 | 0.0772385 | 0.173512 | 0.752232 | 0.76525 | -0.0130178 | 0.232061 | 0.341679 | 0.764407 | 0.941542 | 0.156674 |
| tossup_correctness | tier | fall | 2933 | 0.708948 | 0.496953 | 0.076833 | 0.162321 | 0.766792 | 0.791681 | -0.0248892 | 0.220358 | 0.380019 | 0.789649 | 0.946952 | 0.152052 |
| tossup_correctness | tier | nationals | 1584 | 0.704055 | 0.563057 | 0.0812063 | 0.188708 | 0.725379 | 0.724747 | 0.000631313 | 0.230791 | 0.292193 | 0.711967 | 0.904245 | 0.173603 |
| tossup_correctness | tier | regionals | 1886 | 0.706612 | 0.559836 | 0.0798244 | 0.185137 | 0.740191 | 0.746023 | -0.00583245 | 0.240745 | 0.283465 | 0.741825 | 0.932519 | 0.161271 |
| tossup_correctness | tier | winter | 2892 | 0.716133 | 0.518538 | 0.0756758 | 0.168957 | 0.760028 | 0.773167 | -0.0131397 | 0.233408 | 0.359462 | 0.784192 | 0.954066 | 0.149092 |
| tossup_correctness | category | Current Events | 124 | 0.676032 | 0.565953 | 0.112545 | 0.189613 | 0.725806 | 0.75 | -0.0241935 | 0.224862 | 0.32615 | 0.720025 | 0.929746 | 0.168023 |
| tossup_correctness | category | Fine Arts | 1103 | 0.714315 | 0.512617 | 0.0636811 | 0.166866 | 0.766092 | 0.759746 | 0.00634633 | 0.219227 | 0.365512 | 0.779682 | 0.934279 | 0.157772 |
| tossup_correctness | category | Geography | 197 | 0.755128 | 0.576837 | 0.0999932 | 0.190404 | 0.715736 | 0.670051 | 0.0456853 | 0.272859 | 0.18928 | 0.670198 | 0.913505 | 0.164725 |
| tossup_correctness | category | History | 1491 | 0.734626 | 0.501716 | 0.0896049 | 0.16373 | 0.764588 | 0.787391 | -0.0228035 | 0.2301 | 0.346037 | 0.762373 | 0.940035 | 0.157935 |
| tossup_correctness | category | Literature | 1472 | 0.713715 | 0.487237 | 0.0783645 | 0.156426 | 0.782609 | 0.804348 | -0.0217391 | 0.2312 | 0.374677 | 0.826499 | 0.958735 | 0.13717 |
| tossup_correctness | category | Mythology | 332 | 0.658901 | 0.496032 | 0.103505 | 0.160313 | 0.774096 | 0.813253 | -0.0391566 | 0.189227 | 0.445649 | 0.781026 | 0.920983 | 0.162667 |
| tossup_correctness | category | Other Academic | 69 | 0.702489 | 0.527965 | 0.100981 | 0.17514 | 0.768116 | 0.753623 | 0.0144928 | 0.202324 | 0.366375 | 0.739105 | 0.862682 | 0.180959 |
| tossup_correctness | category | Philosophy | 324 | 0.703416 | 0.477184 | 0.0998628 | 0.158472 | 0.762346 | 0.799383 | -0.037037 | 0.205421 | 0.404034 | 0.771335 | 0.947901 | 0.156333 |
| tossup_correctness | category | Popular Culture | 102 | 0.435294 | 0.496726 | 0.127726 | 0.150961 | 0.843137 | 0.833333 | 0.00980392 | 0.112437 | 0.660102 | 0.850849 | 0.918586 | 0.137595 |
| tossup_correctness | category | Religion | 372 | 0.677504 | 0.587253 | 0.0687482 | 0.2016 | 0.680108 | 0.709677 | -0.0295699 | 0.205531 | 0.373355 | 0.716686 | 0.914416 | 0.177383 |
| tossup_correctness | category | Science | 1487 | 0.688969 | 0.558638 | 0.0916514 | 0.187572 | 0.724277 | 0.752522 | -0.0282448 | 0.240788 | 0.321801 | 0.755957 | 0.945222 | 0.156751 |
| tossup_correctness | category | Social Science | 336 | 0.756907 | 0.53278 | 0.0707238 | 0.173225 | 0.758929 | 0.702381 | 0.0565476 | 0.237796 | 0.274457 | 0.710417 | 0.909114 | 0.170163 |
| tossup_correctness | category | Unknown | 1886 | 0.706612 | 0.559836 | 0.0798244 | 0.185137 | 0.740191 | 0.746023 | -0.00583245 | 0.240745 | 0.283465 | 0.741825 | 0.932519 | 0.161271 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.70756 | 0.549007 | 0.118683 | 0.182988 | 0.736041 | 0.736041 | 0 | 0.226025 | 0.3013 | 0.671897 | 0.882995 | 0.18212 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.717205 | 0.537808 | 0.066059 | 0.180067 | 0.745178 | 0.735025 | 0.0101523 | 0.227862 | 0.331 | 0.736324 | 0.928924 | 0.165497 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.693839 | 0.532295 | 0.0791054 | 0.175434 | 0.743225 | 0.769436 | -0.0262106 | 0.222757 | 0.367925 | 0.781212 | 0.942457 | 0.154764 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.702786 | 0.51649 | 0.081804 | 0.168592 | 0.762387 | 0.78402 | -0.0216329 | 0.223246 | 0.375534 | 0.782407 | 0.951002 | 0.151978 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.72967 | 0.530225 | 0.083248 | 0.173996 | 0.75267 | 0.756008 | -0.00333778 | 0.245476 | 0.287128 | 0.746297 | 0.934691 | 0.158028 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1186 | 2.85936 | 0.57802 | 1.16264 | 1.95145 | 2.47039 | 2.83545 | 3.22021 | 3.85435 | 4.80098 |
| player | theta_1 | 1186 | -1.27347 | 0.687388 | -2.99555 | -2.37746 | -1.81371 | -1.251 | -0.753825 | -0.169749 | 0.364842 |
| player | theta_2 | 1186 | -1.29181 | 0.697833 | -2.89155 | -2.39869 | -1.81272 | -1.29837 | -0.799531 | -0.113386 | 0.493054 |
| player | theta_3 | 1186 | -1.18714 | 0.686826 | -2.99069 | -2.29344 | -1.68671 | -1.17248 | -0.672701 | -0.0719083 | 0.80355 |
| player | theta_norm | 1186 | 2.3645 | 0.734432 | 0.440322 | 1.15252 | 1.82146 | 2.35501 | 2.87221 | 3.63746 | 4.6874 |
| tossup | start_difficulty | 1240 | -1.60892 | 0.734933 | -3.57001 | -2.74045 | -2.09371 | -1.65382 | -1.17315 | -0.352276 | 1.19291 |
| tossup | end_difficulty | 1240 | -3.53481 | 1.48273 | -10.1726 | -6.3215 | -4.40629 | -3.36687 | -2.53372 | -1.3337 | 0.281611 |
| tossup | total_drop | 1240 | 1.92588 | 1.11034 | 0.715398 | 0.893406 | 1.16755 | 1.48799 | 2.33966 | 4.32616 | 8.55211 |
| tossup | drop_share_1 | 1240 | 0.336641 | 0.0593962 | 0.123576 | 0.256821 | 0.303764 | 0.326671 | 0.356941 | 0.459692 | 0.64081 |
| tossup | drop_share_2 | 1240 | 0.352684 | 0.029262 | 0.210306 | 0.314736 | 0.338425 | 0.351154 | 0.363109 | 0.402342 | 0.529404 |
| tossup | drop_share_3 | 1240 | 0.310676 | 0.0531657 | 0.125648 | 0.211469 | 0.283223 | 0.317709 | 0.341088 | 0.385337 | 0.666118 |
| tossup | r_1 | 1240 | 0.873329 | 0.674024 | 0.0332257 | 0.143622 | 0.36318 | 0.670434 | 1.25154 | 2.24342 | 3.76423 |
| tossup | r_2 | 1240 | 0.947514 | 0.809346 | 0.0349865 | 0.13201 | 0.310794 | 0.666911 | 1.37087 | 2.61645 | 4.26451 |
| tossup | r_3 | 1240 | 0.786753 | 0.691517 | 0.0416103 | 0.123352 | 0.276794 | 0.5592 | 1.03636 | 2.38311 | 3.72687 |
| tossup | r_norm | 1240 | 1.85126 | 0.662498 | 0.356394 | 0.897621 | 1.35245 | 1.79785 | 2.29604 | 2.97231 | 4.3727 |
| tossup_hazard | hazard_start_difficulty | 1240 | 2.57378 | 0.561374 | 0.810808 | 1.67739 | 2.18438 | 2.56647 | 2.97109 | 3.50233 | 4.15973 |
| tossup_hazard | hazard_end_difficulty | 1240 | -1.59722 | 1.56467 | -7.39549 | -4.21896 | -2.60619 | -1.56928 | -0.486322 | 0.855606 | 2.04005 |
| tossup_hazard | hazard_total_drop | 1240 | 4.171 | 1.57759 | 0.612076 | 1.4724 | 3.1233 | 4.1911 | 5.15165 | 6.80386 | 10.5252 |
| tossup_hazard | hazard_drop_share_1 | 1240 | 0.133483 | 0.0715638 | 0.0288181 | 0.0567208 | 0.0827797 | 0.114392 | 0.165003 | 0.264713 | 0.587961 |
| tossup_hazard | hazard_drop_share_2 | 1240 | 0.307186 | 0.13956 | 0.050659 | 0.109902 | 0.197849 | 0.294943 | 0.393513 | 0.560662 | 0.76186 |
| tossup_hazard | hazard_drop_share_3 | 1240 | 0.559332 | 0.1837 | 0.0951133 | 0.237153 | 0.413977 | 0.578598 | 0.711215 | 0.825616 | 0.912394 |
