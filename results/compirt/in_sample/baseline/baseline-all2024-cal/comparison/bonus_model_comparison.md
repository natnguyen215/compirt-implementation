# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.930449 | 0.93325 | 0.00280107 | synergy |
| log_loss | 0.341971 | 0.337717 | -0.00425355 | synergy |
| ece | 0.0328726 | 0.0362837 | 0.00341105 | no-synergy |
| part_accuracy | 0.847439 | 0.851859 | 0.00442077 | synergy |
| part_accuracy_macro_team | 0.848741 | 0.853837 | 0.00509561 | synergy |
| part_accuracy_macro_game | 0.847578 | 0.852023 | 0.00444507 | synergy |
| part_accuracy_macro_bonus | 0.853553 | 0.853714 | 0.000160897 | synergy |
| exact_acc | 0.60067 | 0.610043 | 0.00937352 | synergy |
| ppb_mae | 1.66061 | 0.854383 | -0.80623 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
