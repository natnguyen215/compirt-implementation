# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.909508 | 0.918246 | 0.00873797 | synergy |
| log_loss | 0.381065 | 0.364504 | -0.0165617 | synergy |
| ece | 0.0137997 | 0.0177973 | 0.00399761 | no-synergy |
| part_accuracy | 0.826466 | 0.838125 | 0.0116588 | synergy |
| part_accuracy_macro_team | 0.827285 | 0.840304 | 0.0130185 | synergy |
| part_accuracy_macro_game | 0.826371 | 0.838457 | 0.0120862 | synergy |
| part_accuracy_macro_bonus | 0.832129 | 0.840561 | 0.0084323 | synergy |
| exact_acc | 0.550992 | 0.576663 | 0.0256704 | synergy |
| ppb_mae | 1.69657 | 0.533572 | -1.163 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
