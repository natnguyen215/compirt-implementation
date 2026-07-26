# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/in_sample/tfidf-multidim-cumulative-difficulty-all2024-cal/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/in_sample/tfidf-multidim-cumulative-difficulty-all2024-cal`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: in-sample fit.** Player and question parameters were estimated on the same observations these metrics score, so they are optimization and inspection diagnostics, not generalization estimates.

**Correctness calibration was fit on the scored outcomes.** This run learned a Platt scale/bias on the same split these metrics score, so tossup ECE and log loss are flattered by construction and are not comparable to uncalibrated runs.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all 2024 |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 5000 |
| pyramidal | final_loss | 341332 |
| pyramidal | calibrate_correctness | True |
| compositional | tournament | all 2024 |
| compositional | dimensions | 5 |
| compositional | steps | 3000 |
| compositional | final_loss | 61582.5 |
| compositional | calibrate_correctness | True |
| compositional | synergy_dimensions | 0 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 1.0289 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.928679 |
| log_loss | 0.342165 |
| ece | 0.0183743 |
| part_accuracy | 0.846472 |
| part_accuracy_macro_team | 0.84877 |
| part_accuracy_macro_game | 0.846498 |
| part_accuracy_macro_bonus | 0.851405 |
| exact_acc | 0.597163 |
| ppb_mae | 1.30245 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.6611 |
| log_loss | 0.512472 |
| ece | 0.0114909 |
| accuracy | 0.770965 |
| buzz_position_mae | 0.124387 |
| buzz_position_median_absolute_error | 0.102399 |

## No-Synergy Versus Synergy Deltas

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.928679 | 0.934497 | 0.00581828 | synergy |
| log_loss | 0.342165 | 0.330613 | -0.011552 | synergy |
| ece | 0.0183743 | 0.0230218 | 0.00464754 | no-synergy |
| part_accuracy | 0.846472 | 0.854482 | 0.00800983 | synergy |
| part_accuracy_macro_team | 0.84877 | 0.856319 | 0.00754927 | synergy |
| part_accuracy_macro_game | 0.846498 | 0.854567 | 0.00806912 | synergy |
| part_accuracy_macro_bonus | 0.851405 | 0.857408 | 0.00600345 | synergy |
| exact_acc | 0.597163 | 0.614899 | 0.0177355 | synergy |
| ppb_mae | 1.30245 | 0.592242 | -0.710206 | synergy |

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1455 | 1.01152 | 0.65589 | -1.29221 | -0.0611988 | 0.637722 | 0.98544 | 1.38631 | 2.10917 | 4.85117 |
| player | theta_1 | 1455 | -0.548085 | 0.64846 | -2.72766 | -1.59379 | -1.00748 | -0.536449 | -0.125572 | 0.526238 | 1.50492 |
| player | theta_2 | 1455 | -0.463889 | 0.626055 | -2.60723 | -1.47996 | -0.894236 | -0.453825 | -0.0128852 | 0.533459 | 1.64631 |
| player | theta_3 | 1455 | -0.49702 | 0.677268 | -2.71453 | -1.56758 | -0.980142 | -0.508207 | -0.0257082 | 0.64656 | 1.62673 |
| player | theta_4 | 1455 | -0.500869 | 0.609215 | -2.63973 | -1.47086 | -0.921541 | -0.485411 | -0.0985194 | 0.468705 | 1.31568 |
| player | theta_5 | 1455 | -0.638019 | 0.686232 | -2.9286 | -1.73491 | -1.13323 | -0.657459 | -0.155196 | 0.497204 | 1.27875 |
| player | theta_norm | 1455 | 1.79771 | 0.548385 | 0.455222 | 0.948674 | 1.39187 | 1.77051 | 2.19538 | 2.74346 | 3.5828 |
| tossup | beta_1 | 1260 | 0.897263 | 0.442813 | -0.221751 | 0.356971 | 0.573487 | 0.784708 | 1.15197 | 1.79535 | 2.66197 |
| tossup | beta_2 | 1260 | 0.799459 | 0.382896 | -0.273402 | 0.358152 | 0.533123 | 0.706779 | 0.976206 | 1.58624 | 2.70568 |
| tossup | beta_3 | 1260 | 0.84548 | 0.430129 | -0.265969 | 0.369831 | 0.552794 | 0.71787 | 1.04425 | 1.73523 | 2.34813 |
| tossup | beta_4 | 1260 | 0.79382 | 0.375549 | -0.235295 | 0.353757 | 0.544607 | 0.726473 | 0.954113 | 1.50089 | 3.42548 |
| tossup | beta_5 | 1260 | 0.911471 | 0.46804 | -0.186902 | 0.35788 | 0.559722 | 0.789429 | 1.2108 | 1.8174 | 2.75443 |
| tossup | gamma_1 | 1260 | 10.3273 | 41.444 | 0.870683 | 3.20848 | 4.43617 | 5.22736 | 6.83447 | 20.1242 | 1027.26 |
| tossup | gamma_2 | 1260 | 9.20123 | 48.5003 | 0.914531 | 3.20551 | 4.36698 | 5.07454 | 6.06247 | 13.6371 | 1459.32 |
| tossup | gamma_3 | 1260 | 10.628 | 31.1899 | 1.48757 | 3.36128 | 4.47006 | 5.2345 | 6.40049 | 23.7238 | 677.105 |
| tossup | gamma_4 | 1260 | 7.54346 | 31.8305 | 1.19651 | 3.11854 | 4.35252 | 5.11268 | 6.1162 | 12.5063 | 1084.91 |
| tossup | gamma_5 | 1260 | 14.1827 | 56.2866 | 0.773718 | 3.49034 | 4.60016 | 5.46227 | 7.3089 | 38.9627 | 1358.87 |
| tossup | mu_1 | 1260 | 0.550992 | 0.121429 | 0.198651 | 0.412083 | 0.46941 | 0.518425 | 0.612501 | 0.804157 | 0.963091 |
| tossup | mu_2 | 1260 | 0.530999 | 0.10331 | 0.145892 | 0.405939 | 0.469359 | 0.503714 | 0.574095 | 0.73664 | 0.983834 |
| tossup | mu_3 | 1260 | 0.533878 | 0.112783 | 0.221444 | 0.408161 | 0.467099 | 0.504381 | 0.576499 | 0.775447 | 0.985721 |
| tossup | mu_4 | 1260 | 0.528352 | 0.103057 | 0.200164 | 0.40422 | 0.46581 | 0.501792 | 0.574207 | 0.726808 | 0.974223 |
| tossup | mu_5 | 1260 | 0.536201 | 0.113749 | 0.202671 | 0.408383 | 0.464779 | 0.505669 | 0.582825 | 0.768095 | 0.969351 |
| tossup | alpha_1 | 1260 | 1.43962 | 0.910742 | 0.0982912 | 0.367139 | 0.772184 | 1.23188 | 1.82685 | 3.37154 | 5.21763 |
| tossup | alpha_2 | 1260 | 1.17563 | 0.69262 | 0.142956 | 0.330798 | 0.683777 | 1.01916 | 1.50679 | 2.65709 | 4.15797 |
| tossup | alpha_3 | 1260 | 1.31643 | 0.876775 | 0.120436 | 0.401972 | 0.719915 | 1.08027 | 1.55734 | 3.33921 | 5.17579 |
| tossup | alpha_4 | 1260 | 1.19757 | 0.734882 | 0.166142 | 0.391662 | 0.721416 | 1.03798 | 1.44223 | 2.67857 | 6.64727 |
| tossup | alpha_5 | 1260 | 1.31597 | 0.777514 | 0.0895556 | 0.383933 | 0.734878 | 1.09021 | 1.76167 | 2.85057 | 4.23663 |
| tossup | alpha_norm | 1260 | 3.32737 | 0.708872 | 1.63892 | 2.26674 | 2.82169 | 3.28612 | 3.80219 | 4.55183 | 7.26289 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 3768 | 0.0152264 | 1.4789 | -2.88237 | -2.41276 | -1.21139 | 0.0670039 | 1.24115 | 2.28972 | 2.87616 |
| bonus_part | alpha_1 | 3768 | 0.74531 | 0.367844 | 0.197744 | 0.367946 | 0.511612 | 0.669217 | 0.84882 | 1.45331 | 3.68883 |
| bonus_part | alpha_2 | 3768 | 0.738557 | 0.309642 | 0.194137 | 0.371678 | 0.542614 | 0.681955 | 0.859555 | 1.28815 | 4.02872 |
| bonus_part | alpha_3 | 3768 | 0.759417 | 0.343823 | 0.185679 | 0.390522 | 0.545073 | 0.703306 | 0.857919 | 1.38566 | 4.45096 |
| bonus_part | alpha_4 | 3768 | 0.758539 | 0.312121 | 0.241581 | 0.414455 | 0.562471 | 0.71517 | 0.854724 | 1.30512 | 3.87434 |
| bonus_part | alpha_5 | 3768 | 0.774794 | 0.355745 | 0.179801 | 0.371793 | 0.494719 | 0.693781 | 0.981846 | 1.40006 | 3.15213 |
| bonus_part | alpha_norm | 3768 | 1.78407 | 0.493693 | 0.82088 | 1.06278 | 1.42076 | 1.74493 | 2.0633 | 2.65439 | 4.7756 |
