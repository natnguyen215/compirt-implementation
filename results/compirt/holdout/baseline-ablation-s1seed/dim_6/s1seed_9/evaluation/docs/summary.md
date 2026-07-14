# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/baseline-ablation-s1seed/dim_6/s1seed_9/evaluation`
Result root: `results/compirt/holdout/baseline-ablation-s1seed/dim_6/s1seed_9`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

No stage summary JSON files were found for this evaluation folder.

## Bonus Stage Scalars

No bonus-stage scalar summary values were found.

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.902577 |
| log_loss | 0.393906 |
| ece | 0.0152299 |
| part_accuracy | 0.817999 |
| exact_acc | 0.532835 |
| per_bonus_points_mae | 5.65931 |
| ppb_mae | 3.25392 |
| accuracy | 0.817999 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.692233 |
| log_loss | 0.587992 |
| ece | 0.151928 |
| accuracy | 0.70298 |
| buzz_position_mae | 0.140714 |
| buzz_position_median_absolute_error | 0.121283 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 4.97889 | 0.777861 | 1.70258 | 3.4639 | 4.59101 | 5.08772 | 5.5105 | 6.01418 | 6.92866 |
| player | theta_1 | 1755 | 0.0480335 | 0.671434 | -1.8928 | -0.98178 | -0.436405 | 0.029469 | 0.517621 | 1.21045 | 2.48021 |
| player | theta_2 | 1755 | 0.110394 | 0.637677 | -2.10168 | -0.991866 | -0.315984 | 0.127288 | 0.513396 | 1.14862 | 2.08038 |
| player | theta_3 | 1755 | -0.0929189 | 0.635422 | -2.04965 | -1.10525 | -0.503418 | -0.109064 | 0.274304 | 1.03973 | 1.87352 |
| player | theta_4 | 1755 | -0.00213456 | 0.541778 | -1.77218 | -0.87257 | -0.371104 | 0.00820055 | 0.36985 | 0.87646 | 1.63093 |
| player | theta_5 | 1755 | -0.166598 | 0.813598 | -2.2121 | -1.29827 | -0.744222 | -0.268078 | 0.304636 | 1.42343 | 2.2975 |
| player | theta_6 | 1755 | 0.198033 | 0.751941 | -2.4433 | -1.08988 | -0.239016 | 0.228818 | 0.606113 | 1.35613 | 3.36331 |
| player | theta_norm | 1755 | 1.62251 | 0.488067 | 0.321624 | 0.910257 | 1.27414 | 1.58113 | 1.90698 | 2.47009 | 3.60608 |
| tossup | beta | 1350 | 3.34563 | 0.771545 | 0.396959 | 2.04525 | 2.92511 | 3.41107 | 3.85546 | 4.45255 | 5.33516 |
| tossup | gamma | 1350 | 58.2535 | 189.595 | 2.84125 | 5.84899 | 8.96416 | 13.3801 | 27.8384 | 212.253 | 2541.18 |
| tossup | mu | 1350 | 0.587037 | 0.131671 | 0.113391 | 0.36468 | 0.502372 | 0.584823 | 0.673769 | 0.804939 | 0.986002 |
| tossup | alpha_1 | 1350 | 0.307359 | 0.680498 | -1.33488 | -0.65254 | -0.164669 | 0.199138 | 0.671424 | 1.65548 | 2.51983 |
| tossup | alpha_2 | 1350 | 0.0683112 | 0.60653 | -1.77264 | -0.958674 | -0.338223 | 0.0745627 | 0.457393 | 1.05554 | 2.18827 |
| tossup | alpha_3 | 1350 | -0.109347 | 0.747111 | -3.13332 | -1.453 | -0.54754 | -0.069574 | 0.378422 | 1.08641 | 1.81905 |
| tossup | alpha_4 | 1350 | -0.0922466 | 0.59857 | -1.63572 | -1.13316 | -0.47616 | -0.0937414 | 0.333809 | 0.889785 | 1.71585 |
| tossup | alpha_5 | 1350 | -0.457771 | 0.790497 | -2.88282 | -1.78885 | -0.981765 | -0.483202 | 0.101617 | 0.835227 | 1.754 |
| tossup | alpha_6 | 1350 | -0.815088 | 0.71703 | -2.84924 | -2.04405 | -1.29337 | -0.822305 | -0.300614 | 0.35875 | 1.11382 |
| tossup | alpha_norm | 1350 | 1.91045 | 0.477684 | 0.398762 | 1.12707 | 1.58842 | 1.89302 | 2.22742 | 2.70139 | 3.55574 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 4716 | 0.650486 | 1.59073 | -2.64737 | -1.86231 | -0.738824 | 0.751707 | 2.01211 | 2.97435 | 4.39152 |
| bonus_part | alpha_1 | 4716 | 0.833881 | 0.414061 | 0.226944 | 0.360365 | 0.522583 | 0.739998 | 1.04884 | 1.59349 | 3.56274 |
| bonus_part | alpha_2 | 4716 | 0.744463 | 0.326197 | 0.179014 | 0.371776 | 0.510354 | 0.672219 | 0.903837 | 1.31392 | 2.9644 |
| bonus_part | alpha_3 | 4716 | 0.679425 | 0.261188 | 0.107749 | 0.306175 | 0.530206 | 0.663415 | 0.785611 | 1.1083 | 2.8535 |
| bonus_part | alpha_4 | 4716 | 0.638841 | 0.210205 | 0.111993 | 0.283954 | 0.503625 | 0.648615 | 0.765213 | 0.967094 | 1.75419 |
| bonus_part | alpha_5 | 4716 | 0.590624 | 0.255383 | 0.0908035 | 0.20439 | 0.416905 | 0.572226 | 0.739729 | 1.00644 | 2.60517 |
| bonus_part | alpha_6 | 4716 | 0.522691 | 0.26834 | 0.0910933 | 0.18351 | 0.313038 | 0.479013 | 0.679932 | 1.01181 | 2.18342 |
| bonus_part | alpha_norm | 4716 | 1.76607 | 0.386994 | 0.684011 | 1.15882 | 1.48262 | 1.77409 | 2.03147 | 2.36766 | 3.89267 |
