# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/learned-topic-tfidf-all2024/holdout/synergy-evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/learned-topic-tfidf-all2024`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 5000 |
| pyramidal | final_loss | 849994 |
| pyramidal | calibrate_correctness | False |
| synergy | tournament | all tournaments |
| synergy | dimensions | 5 |
| synergy | steps | 3000 |
| synergy | final_loss | 283781 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 3 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.420173 |
| mean_synergy_contribution | -0.0189193 |
| median_synergy_contribution | 0 |
| negative_synergy_fraction | 0.48584 |
| positive_synergy_fraction | 0.489777 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.920613 |
| log_loss | 0.372648 |
| ece | 0.0559651 |
| part_accuracy | 0.841996 |
| part_accuracy_macro_team | 0.843601 |
| part_accuracy_macro_game | 0.842397 |
| part_accuracy_macro_bonus | 0.837406 |
| exact_acc | 0.58375 |
| ppb_mae | 0.49215 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.644869 |
| log_loss | 0.575621 |
| ece | 0.11642 |
| accuracy | 0.71279 |
| buzz_position_mae | 0.146604 |
| buzz_position_median_absolute_error | 0.128708 |

## No-Synergy Versus Synergy Deltas

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.915671 | 0.920613 | 0.00494138 | synergy |
| log_loss | 0.383908 | 0.372648 | -0.0112597 | synergy |
| ece | 0.0565121 | 0.0559651 | -0.000546993 | synergy |
| part_accuracy | 0.835484 | 0.841996 | 0.00651184 | synergy |
| part_accuracy_macro_team | 0.836636 | 0.843601 | 0.00696525 | synergy |
| part_accuracy_macro_game | 0.835732 | 0.842397 | 0.00666522 | synergy |
| part_accuracy_macro_bonus | 0.827187 | 0.837406 | 0.0102197 | synergy |
| exact_acc | 0.568565 | 0.58375 | 0.0151851 | synergy |
| ppb_mae | 1.38685 | 0.49215 | -0.8947 | synergy |

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 5.67926 | 0.456245 | 3.63187 | 4.95 | 5.38311 | 5.67522 | 5.98428 | 6.43632 | 7.07732 |
| player | theta_1 | 1755 | -0.634515 | 0.7231 | -2.67733 | -1.62277 | -1.1075 | -0.787799 | -0.238882 | 0.716715 | 2.40676 |
| player | theta_2 | 1755 | -0.876766 | 1.08436 | -3.47731 | -2.27978 | -1.73209 | -1.08062 | -0.256251 | 1.24505 | 3.1121 |
| player | theta_3 | 1755 | -0.881763 | 1.1429 | -4.31318 | -2.47391 | -1.74906 | -1.03316 | -0.0694675 | 1.21105 | 2.50821 |
| player | theta_4 | 1755 | -1.09685 | 1.2014 | -3.8114 | -2.63626 | -2.02346 | -1.33374 | -0.392249 | 1.27603 | 3.30198 |
| player | theta_5 | 1755 | -0.548687 | 0.781471 | -2.65727 | -1.47278 | -1.029 | -0.749087 | -0.236534 | 1.0262 | 3.16119 |
| player | theta_norm | 1755 | 2.81343 | 0.770721 | 0.350178 | 1.47992 | 2.2977 | 2.83385 | 3.37373 | 3.97826 | 5.91427 |
| tossup | beta_1 | 1350 | 0.723834 | 1.16197 | -4.3339 | -0.0421229 | 0.10437 | 0.227168 | 0.613412 | 3.50845 | 4.88423 |
| tossup | beta_2 | 1350 | 0.765952 | 1.16802 | -3.39508 | -0.0391391 | 0.0931104 | 0.192948 | 0.713544 | 3.30541 | 5.00204 |
| tossup | beta_3 | 1350 | 0.961736 | 1.2904 | -2.91534 | -0.0335037 | 0.0995734 | 0.267296 | 1.80677 | 3.56172 | 5.41969 |
| tossup | beta_4 | 1350 | 1.01379 | 1.3653 | -3.43216 | -0.0650121 | 0.125727 | 0.309671 | 1.79149 | 3.93944 | 4.97044 |
| tossup | beta_5 | 1350 | 0.425929 | 0.834912 | -1.55558 | -0.0479024 | 0.0827665 | 0.173087 | 0.32101 | 2.91476 | 4.36797 |
| tossup | gamma_1 | 1350 | 23.0572 | 105.173 | 1.36656 | 4.49106 | 4.85558 | 5.11581 | 5.47315 | 52.1897 | 1817.84 |
| tossup | gamma_2 | 1350 | 20.6612 | 99.9266 | 0.82665 | 4.49438 | 4.85337 | 5.10646 | 5.48428 | 47.6566 | 1700.97 |
| tossup | gamma_3 | 1350 | 30.1789 | 136.916 | 0.63408 | 4.24183 | 4.85307 | 5.15352 | 6.51038 | 70.9431 | 1872.48 |
| tossup | gamma_4 | 1350 | 28.7846 | 117.285 | 1.52955 | 4.3817 | 4.87134 | 5.16301 | 6.60515 | 109.632 | 2004.55 |
| tossup | gamma_5 | 1350 | 13.5744 | 73.7566 | 0.271179 | 4.49757 | 4.81126 | 5.03981 | 5.27015 | 12.0401 | 1656.95 |
| tossup | mu_1 | 1350 | 0.542044 | 0.110663 | 0.266845 | 0.475277 | 0.491236 | 0.501965 | 0.519895 | 0.83612 | 0.993842 |
| tossup | mu_2 | 1350 | 0.547132 | 0.12289 | 0.147305 | 0.47107 | 0.491624 | 0.50269 | 0.522344 | 0.851159 | 0.990427 |
| tossup | mu_3 | 1350 | 0.555797 | 0.130602 | 0.152791 | 0.455895 | 0.490214 | 0.504057 | 0.545237 | 0.861708 | 0.990058 |
| tossup | mu_4 | 1350 | 0.574015 | 0.151189 | 0.15019 | 0.464801 | 0.492065 | 0.506037 | 0.574383 | 0.920848 | 0.992502 |
| tossup | mu_5 | 1350 | 0.524388 | 0.0917182 | 0.357049 | 0.473981 | 0.490601 | 0.500555 | 0.513017 | 0.793099 | 0.985487 |
| tossup | topic_weight_1 | 1350 | 0.157042 | 0.22853 | 0.00698172 | 0.012651 | 0.0232299 | 0.0455329 | 0.145715 | 0.699752 | 0.848397 |
| tossup | topic_weight_2 | 1350 | 0.212968 | 0.319323 | 0.0062088 | 0.0114942 | 0.0194318 | 0.0418805 | 0.189055 | 0.90328 | 0.956158 |
| tossup | topic_weight_3 | 1350 | 0.250928 | 0.303222 | 0.00490809 | 0.0121073 | 0.0251929 | 0.0732259 | 0.515477 | 0.838289 | 0.960606 |
| tossup | topic_weight_4 | 1350 | 0.266426 | 0.31041 | 0.00657582 | 0.018 | 0.0382314 | 0.0975423 | 0.495554 | 0.877793 | 0.9703 |
| tossup | topic_weight_5 | 1350 | 0.112636 | 0.202795 | 0.00738876 | 0.01514 | 0.0243334 | 0.0406724 | 0.082582 | 0.75258 | 0.954855 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta_1 | 4716 | 0.0394812 | 0.852485 | -3.90765 | -1.44609 | -0.164902 | 0.0167376 | 0.192678 | 1.66771 | 3.53004 |
| bonus_part | beta_2 | 4716 | 0.0687732 | 0.907661 | -4.11428 | -1.47013 | -0.13651 | 0.0152092 | 0.162829 | 1.98315 | 4.26213 |
| bonus_part | beta_3 | 4716 | -0.002236 | 0.953062 | -3.94492 | -1.88022 | -0.183751 | 0.0176223 | 0.200733 | 1.78536 | 4.31897 |
| bonus_part | beta_4 | 4716 | 0.0318257 | 0.959945 | -4.14789 | -1.73128 | -0.174557 | 0.0148687 | 0.216315 | 1.86529 | 3.92939 |
| bonus_part | beta_5 | 4716 | 0.0373246 | 0.624593 | -3.78727 | -0.6042 | -0.126799 | 0.0167478 | 0.151345 | 0.790198 | 3.96988 |
