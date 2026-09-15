# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.889469 | 0.897739 | 0.00827021 | synergy |
| log_loss | 0.420593 | 0.406895 | -0.0136987 | synergy |
| ece | 0.0233037 | 0.0283473 | 0.00504365 | no-synergy |
| brier | 0.134192 | 0.12952 | -0.00467201 | synergy |
| accuracy_lift_over_all_correct | 0.282752 | 0.29044 | 0.00768776 | synergy |
| part_accuracy | 0.808437 | 0.816125 | 0.00768776 | synergy |
| part_accuracy_macro_team | 0.811544 | 0.815394 | 0.00385027 | synergy |
| part_accuracy_macro_bonus | 0.80738 | 0.815415 | 0.00803504 | synergy |
| exact_acc | 0.509639 | 0.526198 | 0.0165582 | synergy |
| ranked_probability_score | 0.117635 | 0.112225 | -0.00540967 | synergy |
| bonus_total_score_log_loss | 1.02287 | 0.988558 | -0.0343075 | synergy |
| ppb_mae | 2.34471 | 1.80908 | -0.535628 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
