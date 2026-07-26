# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.909968 | 0.917409 | 0.00744109 | synergy |
| log_loss | 0.396585 | 0.379104 | -0.0174814 | synergy |
| ece | 0.0641315 | 0.0555877 | -0.00854383 | synergy |
| part_accuracy | 0.822918 | 0.837981 | 0.0150638 | synergy |
| part_accuracy_macro_team | 0.825531 | 0.839864 | 0.0143329 | synergy |
| part_accuracy_macro_game | 0.823111 | 0.838312 | 0.0152007 | synergy |
| part_accuracy_macro_bonus | 0.80259 | 0.831649 | 0.0290591 | synergy |
| exact_acc | 0.542131 | 0.575396 | 0.033265 | synergy |
| ppb_mae | 1.85949 | 0.603642 | -1.25585 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
