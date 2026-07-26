# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.920612 | 0.925131 | 0.00451986 | synergy |
| log_loss | 0.367469 | 0.357551 | -0.00991714 | synergy |
| ece | 0.039716 | 0.0386346 | -0.00108141 | synergy |
| part_accuracy | 0.839137 | 0.84331 | 0.0041735 | synergy |
| part_accuracy_macro_team | 0.841863 | 0.846946 | 0.0050832 | synergy |
| part_accuracy_macro_game | 0.839304 | 0.843593 | 0.00428934 | synergy |
| part_accuracy_macro_bonus | 0.837622 | 0.84297 | 0.00534779 | synergy |
| exact_acc | 0.579945 | 0.591229 | 0.0112842 | synergy |
| ppb_mae | 1.58176 | 1.01464 | -0.567125 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
