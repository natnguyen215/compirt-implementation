# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.908621 | 0.916082 | 0.0074612 | synergy |
| log_loss | 0.400035 | 0.381829 | -0.018206 | synergy |
| ece | 0.0643658 | 0.0525872 | -0.0117786 | synergy |
| accuracy | 0.821933 | 0.835952 | 0.0140191 | synergy |
| part_accuracy | 0.821933 | 0.835952 | 0.0140191 | synergy |
| exact_acc | 0.544294 | 0.573089 | 0.0287949 | synergy |
| per_bonus_points_mae | 5.3557 | 4.97461 | -0.381086 | synergy |
| ppb_mae | 2.67632 | 1.86022 | -0.816098 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
