# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/relevance-locations-terminal/dd-bernstein-332-simplex-locations-terminal/fold_3/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/relevance-locations-terminal/dd-bernstein-332-simplex-locations-terminal/fold_3`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 284673 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.710281 |
| log_loss | 0.486178 |
| ece | 0.00762232 |
| brier | 0.157184 |
| accuracy | 0.783921 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | 0.0138767 |
| probability_std | 0.140514 |
| probability_p10 | 0.583649 |
| probability_p50 | 0.812982 |
| probability_p90 | 0.918282 |
| mean_predictive_variance | 0.153208 |
| integrated_brier_score | 0.101498 |
| joint_tossup_event_log_loss | 6.59262 |
| buzz_position_mae | 0.152274 |
| buzz_position_median_absolute_error | 0.135428 |
| buzz_position_bias | -0.0492869 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |
| first_buzzer_top1_accuracy | 0.349009 |
| first_buzzer_mean_reciprocal_rank | 0.565576 |
| first_buzzer_log_loss | 1.67554 |
| first_buzzer_events | 9080 |
| neg_auroc | 0.710281 |
| neg_average_precision | 0.447726 |
| neg_precision | 0.635193 |
| neg_recall | 0.141762 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.184146 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0152375 |
| no_buzz_calibration_error | 5.30907e-05 |
| no_buzz_brier | 0.0136983 |
| full_pmf_max_mass_error | 1.22125e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.710281 | 0.486178 | 0.00762232 | 0.157184 | 0.783921 | 0.770044 | 0.0138767 | 0.140514 | 0.583649 | 0.812982 | 0.918282 | 0.153208 |
| tossup_correctness | tier | fall | 2817 | 0.702997 | 0.477813 | 0.0130997 | 0.153219 | 0.791977 | 0.781683 | 0.0102946 | 0.139096 | 0.579892 | 0.822472 | 0.922112 | 0.14995 |
| tossup_correctness | tier | nationals | 1542 | 0.725097 | 0.515939 | 0.0356965 | 0.170846 | 0.754215 | 0.73476 | 0.0194553 | 0.143813 | 0.565763 | 0.795654 | 0.910204 | 0.160581 |
| tossup_correctness | tier | regionals | 1934 | 0.717364 | 0.497858 | 0.0204373 | 0.162391 | 0.770424 | 0.75698 | 0.0134436 | 0.136765 | 0.589471 | 0.80743 | 0.917354 | 0.155222 |
| tossup_correctness | tier | winter | 2787 | 0.698932 | 0.470061 | 0.01735 | 0.150021 | 0.801579 | 0.786868 | 0.0147112 | 0.141989 | 0.593006 | 0.817028 | 0.919544 | 0.151024 |
| tossup_correctness | category | Current Events | 125 | 0.743243 | 0.533937 | 0.0702981 | 0.180697 | 0.712 | 0.704 | 0.008 | 0.14598 | 0.543485 | 0.784491 | 0.906922 | 0.168168 |
| tossup_correctness | category | Fine Arts | 1072 | 0.725639 | 0.474523 | 0.0261915 | 0.152491 | 0.795709 | 0.770522 | 0.0251866 | 0.146589 | 0.56678 | 0.817353 | 0.917427 | 0.153026 |
| tossup_correctness | category | Geography | 185 | 0.778601 | 0.490822 | 0.0533878 | 0.160681 | 0.756757 | 0.702703 | 0.0540541 | 0.205208 | 0.404101 | 0.764221 | 0.895937 | 0.169362 |
| tossup_correctness | category | History | 1443 | 0.727529 | 0.485888 | 0.024369 | 0.159004 | 0.777547 | 0.765073 | 0.012474 | 0.144829 | 0.561045 | 0.804999 | 0.917147 | 0.156894 |
| tossup_correctness | category | Literature | 1411 | 0.658286 | 0.459504 | 0.0265522 | 0.144491 | 0.811481 | 0.81219 | -0.000708717 | 0.114632 | 0.659936 | 0.844778 | 0.926897 | 0.137745 |
| tossup_correctness | category | Mythology | 320 | 0.664639 | 0.482644 | 0.0286143 | 0.151752 | 0.803125 | 0.79375 | 0.009375 | 0.113092 | 0.647453 | 0.826261 | 0.926422 | 0.144164 |
| tossup_correctness | category | Other Academic | 64 | 0.638021 | 0.569185 | 0.167553 | 0.191623 | 0.71875 | 0.75 | -0.03125 | 0.113587 | 0.648186 | 0.807553 | 0.902563 | 0.154074 |
| tossup_correctness | category | Philosophy | 312 | 0.65729 | 0.468988 | 0.0392921 | 0.149199 | 0.810897 | 0.801282 | 0.00961538 | 0.111989 | 0.64907 | 0.817064 | 0.916894 | 0.151591 |
| tossup_correctness | category | Popular Culture | 104 | 0.603693 | 0.421699 | 0.0311901 | 0.125583 | 0.846154 | 0.846154 | 0 | 0.0710608 | 0.745328 | 0.864448 | 0.91798 | 0.126113 |
| tossup_correctness | category | Religion | 358 | 0.715071 | 0.533889 | 0.0434374 | 0.179173 | 0.73743 | 0.726257 | 0.0111732 | 0.139606 | 0.545192 | 0.771268 | 0.900814 | 0.169332 |
| tossup_correctness | category | Science | 1431 | 0.699853 | 0.492699 | 0.0183851 | 0.1594 | 0.784766 | 0.765199 | 0.0195667 | 0.144158 | 0.570052 | 0.800267 | 0.914252 | 0.157709 |
| tossup_correctness | category | Social Science | 321 | 0.734003 | 0.494296 | 0.0271297 | 0.160084 | 0.772586 | 0.744548 | 0.0280374 | 0.173952 | 0.507727 | 0.794535 | 0.916423 | 0.15909 |
| tossup_correctness | category | Unknown | 1934 | 0.717364 | 0.497858 | 0.0204373 | 0.162391 | 0.770424 | 0.75698 | 0.0134436 | 0.136765 | 0.589471 | 0.80743 | 0.917354 | 0.155222 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.747813 | 0.54453 | 0.0777722 | 0.184578 | 0.71875 | 0.697917 | 0.0208333 | 0.154847 | 0.492973 | 0.748672 | 0.871772 | 0.179072 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.751786 | 0.498225 | 0.0318761 | 0.163556 | 0.770529 | 0.733408 | 0.0371204 | 0.14546 | 0.554089 | 0.79298 | 0.906506 | 0.163096 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.685679 | 0.513203 | 0.0247893 | 0.167404 | 0.767421 | 0.759276 | 0.0081448 | 0.140017 | 0.591694 | 0.815429 | 0.919481 | 0.15177 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.692588 | 0.472925 | 0.0158954 | 0.15146 | 0.800279 | 0.789125 | 0.0111537 | 0.12301 | 0.623584 | 0.828153 | 0.922061 | 0.146651 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.727461 | 0.471241 | 0.0128237 | 0.151333 | 0.788699 | 0.775342 | 0.0133562 | 0.150993 | 0.550576 | 0.80568 | 0.917614 | 0.156027 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1133 | 2.66168 | 0.743034 | 0.627843 | 1.45043 | 2.12593 | 2.66807 | 3.15478 | 3.96679 | 4.61511 |
| player | theta_1 | 1133 | -1.20922 | 0.853431 | -3.50564 | -2.4916 | -1.75755 | -1.26852 | -0.723084 | 0.399 | 2.29836 |
| player | theta_2 | 1133 | -0.976847 | 0.591313 | -3.18806 | -1.93373 | -1.33428 | -0.986196 | -0.584622 | 0.0212826 | 0.94608 |
| player | theta_3 | 1133 | -1.12598 | 0.761612 | -3.29623 | -2.29766 | -1.62834 | -1.17772 | -0.665974 | 0.199515 | 1.48742 |
| player | theta_norm | 1133 | 2.22168 | 0.636655 | 0.354587 | 1.21404 | 1.79907 | 2.20973 | 2.61972 | 3.33455 | 4.43768 |
| tossup | start_difficulty_d1 | 1240 | -1.77825 | 0.550278 | -3.68078 | -2.52646 | -2.14792 | -1.8424 | -1.47761 | -0.782063 | 1.38492 |
| tossup | start_difficulty_d2 | 1240 | -1.76427 | 0.505182 | -3.76251 | -2.54232 | -2.10896 | -1.80349 | -1.43335 | -0.905916 | 0.0354599 |
| tossup | start_difficulty_d3 | 1240 | -1.76605 | 0.512679 | -3.54069 | -2.54878 | -2.11661 | -1.80023 | -1.42595 | -0.883403 | 0.202851 |
| tossup | end_difficulty_d1 | 1240 | -2.76724 | 0.643449 | -5.18485 | -3.64828 | -3.2016 | -2.84041 | -2.40104 | -1.62157 | 0.70752 |
| tossup | end_difficulty_d2 | 1240 | -2.74986 | 0.593212 | -5.12138 | -3.67202 | -3.15983 | -2.78585 | -2.36696 | -1.73609 | -0.718153 |
| tossup | end_difficulty_d3 | 1240 | -2.74988 | 0.598652 | -4.83112 | -3.68967 | -3.15578 | -2.78101 | -2.35664 | -1.71229 | -0.531444 |
| tossup | total_drop_d1 | 1240 | 0.988989 | 0.1126 | 0.59422 | 0.797574 | 0.914321 | 0.995308 | 1.06045 | 1.15812 | 1.50407 |
| tossup | total_drop_d2 | 1240 | 0.98559 | 0.104637 | 0.687421 | 0.82002 | 0.913084 | 0.98176 | 1.05762 | 1.15583 | 1.35887 |
| tossup | total_drop_d3 | 1240 | 0.983826 | 0.104284 | 0.599341 | 0.820779 | 0.911768 | 0.985539 | 1.05134 | 1.15194 | 1.32545 |
| tossup | drop_share_1_d1 | 1240 | 0.304124 | 0.0154135 | 0.237938 | 0.279364 | 0.294355 | 0.30444 | 0.314456 | 0.32746 | 0.372966 |
| tossup | drop_share_2_d1 | 1240 | 0.347109 | 0.0114441 | 0.310278 | 0.327989 | 0.339598 | 0.347321 | 0.35493 | 0.364999 | 0.385776 |
| tossup | drop_share_3_d1 | 1240 | 0.348767 | 0.0164484 | 0.276481 | 0.322811 | 0.337606 | 0.348651 | 0.359224 | 0.375045 | 0.414707 |
| tossup | drop_share_1_d2 | 1240 | 0.303631 | 0.0141484 | 0.251426 | 0.279271 | 0.294831 | 0.303819 | 0.313192 | 0.326432 | 0.357564 |
| tossup | drop_share_2_d2 | 1240 | 0.346917 | 0.0113816 | 0.307779 | 0.328152 | 0.339376 | 0.346885 | 0.354532 | 0.365383 | 0.390947 |
| tossup | drop_share_3_d2 | 1240 | 0.349452 | 0.0154503 | 0.283599 | 0.324582 | 0.339427 | 0.349812 | 0.359239 | 0.374648 | 0.424913 |
| tossup | drop_share_1_d3 | 1240 | 0.303542 | 0.0149994 | 0.244761 | 0.277978 | 0.294266 | 0.303664 | 0.313745 | 0.326948 | 0.357075 |
| tossup | drop_share_2_d3 | 1240 | 0.347142 | 0.0112539 | 0.30974 | 0.328843 | 0.339925 | 0.346882 | 0.354388 | 0.365875 | 0.389112 |
| tossup | drop_share_3_d3 | 1240 | 0.349315 | 0.0157332 | 0.304442 | 0.324731 | 0.338669 | 0.349008 | 0.358848 | 0.376252 | 0.413809 |
| tossup | r_1 | 1240 | 0.320993 | 0.142863 | 0.0550154 | 0.134251 | 0.210864 | 0.293039 | 0.407184 | 0.596555 | 0.848823 |
| tossup | r_2 | 1240 | 0.335758 | 0.104838 | 0.0714188 | 0.17425 | 0.266461 | 0.331921 | 0.395443 | 0.522075 | 0.827566 |
| tossup | r_3 | 1240 | 0.34325 | 0.121373 | 0.0730344 | 0.16627 | 0.256706 | 0.334376 | 0.413737 | 0.577293 | 0.79194 |
| tossup | r_norm | 1240 | 0.614819 | 0.0410437 | 0.577392 | 0.578979 | 0.586174 | 0.600879 | 0.626599 | 0.703217 | 0.855535 |
| tossup_hazard | hazard_start_difficulty_d1 | 1240 | 4.48353 | 0.492158 | 2.15726 | 3.76066 | 4.19449 | 4.43675 | 4.73444 | 5.39594 | 6.39031 |
| tossup_hazard | hazard_start_difficulty_d2 | 1240 | 4.45881 | 0.413339 | 2.25521 | 3.82593 | 4.23326 | 4.44706 | 4.66554 | 5.16486 | 6.58453 |
| tossup_hazard | hazard_start_difficulty_d3 | 1240 | 4.47162 | 0.44291 | 2.46794 | 3.75405 | 4.22122 | 4.45632 | 4.71984 | 5.23009 | 6.09822 |
| tossup_hazard | hazard_end_difficulty_d1 | 1240 | 1.74884 | 2.27442 | -8.31946 | -2.89007 | 0.593925 | 2.85233 | 3.28928 | 3.61246 | 4.3789 |
| tossup_hazard | hazard_end_difficulty_d2 | 1240 | 2.41348 | 1.91829 | -7.97631 | -2.02451 | 2.56154 | 3.13852 | 3.41475 | 3.73022 | 4.15772 |
| tossup_hazard | hazard_end_difficulty_d3 | 1240 | 2.14773 | 2.08024 | -8.96088 | -2.39177 | 1.93692 | 3.03661 | 3.37812 | 3.76225 | 4.26276 |
| tossup_hazard | hazard_total_drop_d1 | 1240 | 2.73469 | 2.44512 | 0.845721 | 0.985113 | 1.06457 | 1.34609 | 4.03624 | 7.95884 | 13.0594 |
| tossup_hazard | hazard_total_drop_d2 | 1240 | 2.04533 | 2.07527 | 0.895619 | 0.958935 | 1.02221 | 1.16491 | 1.65959 | 7.0263 | 13.4691 |
| tossup_hazard | hazard_total_drop_d3 | 1240 | 2.32389 | 2.20687 | 0.875189 | 0.967265 | 1.03188 | 1.24302 | 2.42796 | 7.34006 | 13.5311 |
| tossup_hazard | hazard_drop_share_1_d1 | 1240 | 0.236399 | 0.0801788 | 0.0320423 | 0.0826483 | 0.181192 | 0.270566 | 0.293778 | 0.316362 | 0.505159 |
| tossup_hazard | hazard_drop_share_2_d1 | 1240 | 0.342657 | 0.0742967 | 0.0604686 | 0.183063 | 0.335896 | 0.351181 | 0.365234 | 0.445631 | 0.715256 |
| tossup_hazard | hazard_drop_share_3_d1 | 1240 | 0.420943 | 0.129695 | 0.109394 | 0.302913 | 0.347991 | 0.370061 | 0.444516 | 0.719812 | 0.896267 |
| tossup_hazard | hazard_drop_share_1_d2 | 1240 | 0.25558 | 0.0664984 | 0.0386304 | 0.0938194 | 0.241029 | 0.280126 | 0.295944 | 0.314274 | 0.529854 |
| tossup_hazard | hazard_drop_share_2_d2 | 1240 | 0.348529 | 0.0566761 | 0.0528213 | 0.247796 | 0.340932 | 0.351274 | 0.363318 | 0.407069 | 0.684308 |
| tossup_hazard | hazard_drop_share_3_d2 | 1240 | 0.395891 | 0.0994786 | 0.199581 | 0.320892 | 0.349501 | 0.364977 | 0.393685 | 0.650894 | 0.908548 |
| tossup_hazard | hazard_drop_share_1_d3 | 1240 | 0.246821 | 0.0710667 | 0.041788 | 0.0897228 | 0.219698 | 0.272814 | 0.295189 | 0.314676 | 0.56715 |
| tossup_hazard | hazard_drop_share_2_d3 | 1240 | 0.349662 | 0.0610823 | 0.0830668 | 0.236206 | 0.339148 | 0.351272 | 0.366403 | 0.424078 | 0.70549 |
| tossup_hazard | hazard_drop_share_3_d3 | 1240 | 0.403517 | 0.105623 | 0.0696441 | 0.31733 | 0.349611 | 0.368528 | 0.409859 | 0.650671 | 0.864452 |
| tossup_hazard | hazard_r_1 | 1240 | 0.380224 | 0.277194 | 0.0264857 | 0.0635495 | 0.132044 | 0.288211 | 0.603541 | 0.887312 | 0.951254 |
| tossup_hazard | hazard_r_2 | 1240 | 0.278419 | 0.197572 | 0.0306976 | 0.0588471 | 0.122186 | 0.214219 | 0.398234 | 0.683831 | 0.849786 |
| tossup_hazard | hazard_r_3 | 1240 | 0.341358 | 0.237604 | 0.0176574 | 0.04505 | 0.142966 | 0.279774 | 0.529094 | 0.773606 | 0.929877 |
