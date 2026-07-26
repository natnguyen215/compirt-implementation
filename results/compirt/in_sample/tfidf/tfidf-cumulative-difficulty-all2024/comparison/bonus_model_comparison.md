# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.919946 | 0.93257 | 0.0126244 | synergy |
| log_loss | 0.364257 | 0.339477 | -0.0247804 | synergy |
| ece | 0.0284211 | 0.0355157 | 0.00709462 | no-synergy |
| part_accuracy | 0.837466 | 0.852047 | 0.014581 | synergy |
| part_accuracy_macro_team | 0.840357 | 0.853518 | 0.0131611 | synergy |
| part_accuracy_macro_game | 0.837479 | 0.851993 | 0.0145145 | synergy |
| part_accuracy_macro_bonus | 0.838049 | 0.855025 | 0.0169758 | synergy |
| exact_acc | 0.578821 | 0.609459 | 0.0306382 | synergy |
| ppb_mae | 1.80164 | 0.649585 | -1.15206 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
