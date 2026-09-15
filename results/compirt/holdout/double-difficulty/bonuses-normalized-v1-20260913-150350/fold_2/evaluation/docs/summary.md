# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_2/evaluation`
Result root: `results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_2`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| compositional | tournament | all tournaments |
| compositional | dimensions | 3 |
| compositional | calibrate_correctness | False |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 1.56122 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.888976 |
| log_loss | 0.42114 |
| ece | 0.0202859 |
| brier | 0.134456 |
| part_accuracy | 0.807181 |
| part_all_correct_accuracy | 0.519367 |
| accuracy_lift_over_all_correct | 0.287814 |
| part_accuracy_macro_team | 0.810567 |
| part_accuracy_macro_bonus | 0.804731 |
| probability_std | 0.344813 |
| probability_p10 | 0.0528301 |
| probability_p50 | 0.527759 |
| probability_p90 | 0.95619 |
| mean_predictive_variance | 0.130728 |
| exact_acc | 0.509131 |
| ranked_probability_score | 0.116926 |
| bonus_total_score_log_loss | 1.02658 |
| ppb_mae | 2.29287 |
| ranked_probability_score_responses | 8597 |
| bonus_total_score_log_loss_responses | 8597 |

## Stage 1 Tossup Metrics

No tossup metrics CSV was found.

## Tossup Game Replay

No tossup game replay metrics CSV was found.

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part_correctness | aggregate | all | 25791 | 0.888976 | 0.42114 | 0.0202859 | 0.134456 | 0.807181 | 0.519367 | 0.287814 | 0.344813 | 0.0528301 | 0.527759 | 0.95619 | 0.130728 |
| bonus_part_correctness | tier | fall | 7995 | 0.896476 | 0.399748 | 0.0250118 | 0.12844 | 0.814009 | 0.595122 | 0.218887 | 0.332122 | 0.100026 | 0.661051 | 0.966988 | 0.130709 |
| bonus_part_correctness | tier | nationals | 4095 | 0.882154 | 0.428314 | 0.0267983 | 0.13594 | 0.80464 | 0.425153 | 0.379487 | 0.334498 | 0.0392741 | 0.39493 | 0.911049 | 0.135275 |
| bonus_part_correctness | tier | regionals | 5580 | 0.88588 | 0.425235 | 0.0202673 | 0.136198 | 0.806452 | 0.495878 | 0.310573 | 0.340563 | 0.0456263 | 0.45838 | 0.940363 | 0.133771 |
| bonus_part_correctness | tier | winter | 8121 | 0.882326 | 0.435768 | 0.0202618 | 0.138433 | 0.802241 | 0.508435 | 0.293806 | 0.351571 | 0.0420013 | 0.493458 | 0.958491 | 0.126364 |
| bonus_part_correctness | category | Current Events | 216 | 0.907706 | 0.382352 | 0.0675549 | 0.11951 | 0.842593 | 0.467593 | 0.375 | 0.357752 | 0.0373226 | 0.45135 | 0.947756 | 0.121765 |
| bonus_part_correctness | category | Fine Arts | 2970 | 0.874892 | 0.446894 | 0.0261119 | 0.144213 | 0.789562 | 0.512795 | 0.276768 | 0.341703 | 0.0549166 | 0.499682 | 0.952522 | 0.133183 |
| bonus_part_correctness | category | Geography | 501 | 0.892181 | 0.428562 | 0.0653019 | 0.134876 | 0.814371 | 0.572854 | 0.241517 | 0.329245 | 0.0820184 | 0.735607 | 0.951406 | 0.129289 |
| bonus_part_correctness | category | History | 4068 | 0.895297 | 0.409976 | 0.0180266 | 0.129968 | 0.813668 | 0.549164 | 0.264503 | 0.342822 | 0.0568439 | 0.592154 | 0.962151 | 0.129876 |
| bonus_part_correctness | category | Literature | 4065 | 0.895163 | 0.408637 | 0.0268338 | 0.129657 | 0.81353 | 0.510947 | 0.302583 | 0.348509 | 0.0517517 | 0.501168 | 0.959515 | 0.128353 |
| bonus_part_correctness | category | Mythology | 945 | 0.858648 | 0.459304 | 0.0307706 | 0.149897 | 0.785185 | 0.606349 | 0.178836 | 0.313651 | 0.137527 | 0.678451 | 0.967898 | 0.137977 |
| bonus_part_correctness | category | Other Academic | 219 | 0.875042 | 0.452849 | 0.074532 | 0.145007 | 0.799087 | 0.493151 | 0.305936 | 0.360246 | 0.0341152 | 0.549105 | 0.953154 | 0.120214 |
| bonus_part_correctness | category | Philosophy | 963 | 0.879176 | 0.437518 | 0.034677 | 0.139445 | 0.806854 | 0.483904 | 0.322949 | 0.335234 | 0.0613781 | 0.471166 | 0.949731 | 0.137615 |
| bonus_part_correctness | category | Popular Culture | 288 | 0.876029 | 0.428727 | 0.0835045 | 0.141534 | 0.770833 | 0.625 | 0.145833 | 0.330682 | 0.105672 | 0.717178 | 0.974169 | 0.124984 |
| bonus_part_correctness | category | Religion | 1008 | 0.891051 | 0.417062 | 0.0401601 | 0.134554 | 0.809524 | 0.503968 | 0.305556 | 0.352368 | 0.0442925 | 0.491068 | 0.9525 | 0.125818 |
| bonus_part_correctness | category | Science | 4059 | 0.890472 | 0.419263 | 0.0294516 | 0.132782 | 0.810052 | 0.530673 | 0.279379 | 0.346074 | 0.053291 | 0.5487 | 0.958819 | 0.129452 |
| bonus_part_correctness | category | Social Science | 909 | 0.913981 | 0.368681 | 0.0472555 | 0.117991 | 0.820682 | 0.458746 | 0.361936 | 0.357406 | 0.0353921 | 0.437361 | 0.960082 | 0.122052 |
| bonus_part_correctness | category | Unknown | 5580 | 0.88588 | 0.425235 | 0.0202673 | 0.136198 | 0.806452 | 0.495878 | 0.310573 | 0.340563 | 0.0456263 | 0.45838 | 0.940363 | 0.133771 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## No-Synergy Versus Synergy Deltas

No bonus model comparison CSV was found.

## Pyramidal Player And Tossup Parameters

No pyramidal parameter distribution summary CSV was found.

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum | parameter_source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 3768 | -0.195286 | 1.24308 | -2.71848 | -2.25193 | -1.24753 | -0.142025 | 0.846059 | 1.66586 | 2.19093 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_2/train/compositional |
| bonus_part | alpha_1 | 3768 | 0.805467 | 0.441085 | 0.179772 | 0.309257 | 0.437489 | 0.694649 | 1.09379 | 1.60926 | 3.45932 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_2/train/compositional |
| bonus_part | alpha_2 | 3768 | 0.739648 | 0.379625 | 0.20844 | 0.330768 | 0.430017 | 0.628907 | 0.971742 | 1.46502 | 2.87857 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_2/train/compositional |
| bonus_part | alpha_3 | 3768 | 0.765452 | 0.395053 | 0.179929 | 0.318189 | 0.445802 | 0.674218 | 1.01989 | 1.47254 | 2.90146 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_2/train/compositional |
| bonus_part | alpha_norm | 3768 | 1.39106 | 0.584323 | 0.490537 | 0.595365 | 0.860102 | 1.34463 | 1.83817 | 2.37519 | 3.55145 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_2/train/compositional |
