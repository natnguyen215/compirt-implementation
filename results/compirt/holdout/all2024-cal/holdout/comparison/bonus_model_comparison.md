# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.930974 | 0.933332 | 0.00235761 | synergy |
| log_loss | 0.337875 | 0.333378 | -0.0044966 | synergy |
| ece | 0.0254287 | 0.0270304 | 0.00160163 | no-synergy |
| accuracy | 0.850018 | 0.854396 | 0.00437798 | synergy |
| part_accuracy | 0.850018 | 0.854396 | 0.00437798 | synergy |
| exact_acc | 0.604112 | 0.614401 | 0.0102888 | synergy |
| per_bonus_points_mae | 4.87328 | 4.66279 | -0.210484 | synergy |
| ppb_mae | 2.17029 | 1.67029 | -0.499999 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
