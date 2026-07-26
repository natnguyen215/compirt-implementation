# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.928178 | 0.932839 | 0.00466122 | synergy |
| log_loss | 0.342408 | 0.333042 | -0.00936658 | synergy |
| ece | 0.0212791 | 0.0211868 | -9.22858e-05 | synergy |
| part_accuracy | 0.845795 | 0.852847 | 0.00705219 | synergy |
| part_accuracy_macro_team | 0.846868 | 0.854075 | 0.00720723 | synergy |
| part_accuracy_macro_game | 0.84611 | 0.853134 | 0.00702345 | synergy |
| part_accuracy_macro_bonus | 0.852925 | 0.8591 | 0.00617413 | synergy |
| exact_acc | 0.594237 | 0.609521 | 0.0152843 | synergy |
| ppb_mae | 1.34287 | 0.536299 | -0.806568 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
