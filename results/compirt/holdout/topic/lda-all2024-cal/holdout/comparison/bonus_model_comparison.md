# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.911379 | 0.922076 | 0.0106972 | synergy |
| log_loss | 0.37593 | 0.354969 | -0.0209618 | synergy |
| ece | 0.00933296 | 0.0145648 | 0.00523182 | no-synergy |
| part_accuracy | 0.82874 | 0.842034 | 0.0132939 | synergy |
| part_accuracy_macro_team | 0.829541 | 0.843252 | 0.0137107 | synergy |
| part_accuracy_macro_game | 0.82899 | 0.842432 | 0.0134421 | synergy |
| part_accuracy_macro_bonus | 0.838758 | 0.848295 | 0.00953678 | synergy |
| exact_acc | 0.554769 | 0.584246 | 0.029477 | synergy |
| ppb_mae | 1.8009 | 0.434311 | -1.36659 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
