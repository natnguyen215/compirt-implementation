# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.922341 | 0.926801 | 0.00446066 | synergy |
| log_loss | 0.361265 | 0.351346 | -0.00991933 | synergy |
| ece | 0.0354595 | 0.0335056 | -0.00195392 | synergy |
| part_accuracy | 0.839873 | 0.846043 | 0.00616998 | synergy |
| part_accuracy_macro_team | 0.842249 | 0.848592 | 0.0063426 | synergy |
| part_accuracy_macro_game | 0.840312 | 0.846489 | 0.00617714 | synergy |
| part_accuracy_macro_bonus | 0.831943 | 0.85392 | 0.0219764 | synergy |
| exact_acc | 0.580259 | 0.595395 | 0.0151355 | synergy |
| ppb_mae | 1.40142 | 0.846249 | -0.555168 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
