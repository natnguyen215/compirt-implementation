# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.915078 | 0.921769 | 0.00669171 | synergy |
| log_loss | 0.368554 | 0.355762 | -0.0127922 | synergy |
| ece | 0.00766231 | 0.0133989 | 0.00573655 | no-synergy |
| accuracy | 0.831719 | 0.840965 | 0.00924615 | synergy |
| part_accuracy | 0.831719 | 0.840965 | 0.00924615 | synergy |
| exact_acc | 0.562074 | 0.582799 | 0.0207252 | synergy |
| rounded_score_accuracy | 0.57464 | 0.595635 | 0.0209949 | synergy |
| per_bonus_points_mae | 5.04876 | 4.80533 | -0.243424 | synergy |
| ppb_mae | 2.2458 | 1.71382 | -0.531981 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
