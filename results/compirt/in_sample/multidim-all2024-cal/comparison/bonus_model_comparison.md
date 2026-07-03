# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.936419 | 0.937036 | 0.000617486 | synergy |
| log_loss | 0.328264 | 0.328901 | 0.000636746 | no-synergy |
| ece | 0.0338917 | 0.0371937 | 0.00330198 | no-synergy |
| accuracy | 0.854669 | 0.856812 | 0.00214295 | synergy |
| part_accuracy | 0.854669 | 0.856812 | 0.00214295 | synergy |
| exact_acc | 0.617776 | 0.622586 | 0.00481039 | synergy |
| rounded_score_accuracy | 0.613662 | 0.619664 | 0.00600175 | synergy |
| per_bonus_points_mae | 4.70808 | 4.58288 | -0.125197 | synergy |
| ppb_mae | 2.11717 | 1.74626 | -0.370915 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
