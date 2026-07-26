# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.934747 | 0.938159 | 0.00341183 | synergy |
| log_loss | 0.341591 | 0.328526 | -0.0130653 | synergy |
| ece | 0.0490555 | 0.0410124 | -0.00804314 | synergy |
| part_accuracy | 0.853598 | 0.858288 | 0.00469051 | synergy |
| part_accuracy_macro_team | 0.855695 | 0.860849 | 0.00515433 | synergy |
| part_accuracy_macro_game | 0.853845 | 0.858615 | 0.00477065 | synergy |
| part_accuracy_macro_bonus | 0.860256 | 0.860805 | 0.000549673 | synergy |
| exact_acc | 0.614494 | 0.625666 | 0.0111718 | synergy |
| ppb_mae | 1.42893 | 0.783493 | -0.645434 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
