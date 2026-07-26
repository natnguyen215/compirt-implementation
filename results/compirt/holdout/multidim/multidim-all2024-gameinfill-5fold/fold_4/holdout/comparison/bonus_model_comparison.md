# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.891115 | 0.897278 | 0.0061627 | synergy |
| log_loss | 0.418661 | 0.409088 | -0.00957274 | synergy |
| ece | 0.0260805 | 0.034084 | 0.00800349 | no-synergy |
| brier | 0.133346 | 0.130176 | -0.00317049 | synergy |
| accuracy_lift_over_all_correct | 0.284582 | 0.290497 | 0.0059151 | synergy |
| part_accuracy | 0.810137 | 0.816052 | 0.0059151 | synergy |
| part_accuracy_macro_team | 0.814245 | 0.822032 | 0.00778697 | synergy |
| part_accuracy_macro_bonus | 0.801593 | 0.808825 | 0.0072327 | synergy |
| exact_acc | 0.514498 | 0.529344 | 0.0148457 | synergy |
| ranked_probability_score | 0.117458 | 0.113478 | -0.00397957 | synergy |
| bonus_total_score_log_loss | 1.02381 | 1.00004 | -0.0237656 | synergy |
| ppb_mae | 2.32011 | 1.85769 | -0.462412 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
