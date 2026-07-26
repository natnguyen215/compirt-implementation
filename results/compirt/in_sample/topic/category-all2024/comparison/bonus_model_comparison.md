# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.91227 | 0.918148 | 0.00587814 | synergy |
| log_loss | 0.385933 | 0.371182 | -0.0147505 | synergy |
| ece | 0.0470387 | 0.0367368 | -0.0103019 | synergy |
| part_accuracy | 0.82801 | 0.837346 | 0.00933606 | synergy |
| part_accuracy_macro_team | 0.829848 | 0.838988 | 0.00914059 | synergy |
| part_accuracy_macro_game | 0.827794 | 0.837286 | 0.00949224 | synergy |
| part_accuracy_macro_bonus | 0.820255 | 0.835018 | 0.0147631 | synergy |
| exact_acc | 0.555488 | 0.576663 | 0.0211747 | synergy |
| ppb_mae | 1.75108 | 0.740982 | -1.0101 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
