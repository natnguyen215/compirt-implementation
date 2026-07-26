# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.933325 | 0.937103 | 0.00377846 | synergy |
| log_loss | 0.341114 | 0.328551 | -0.0125634 | synergy |
| ece | 0.0429504 | 0.0350151 | -0.00793532 | synergy |
| part_accuracy | 0.852692 | 0.858895 | 0.00620306 | synergy |
| part_accuracy_macro_team | 0.854526 | 0.86042 | 0.00589472 | synergy |
| part_accuracy_macro_game | 0.853124 | 0.859296 | 0.00617183 | synergy |
| part_accuracy_macro_bonus | 0.863262 | 0.86947 | 0.006208 | synergy |
| exact_acc | 0.610381 | 0.625583 | 0.0152016 | synergy |
| ppb_mae | 1.33213 | 0.690905 | -0.641225 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
