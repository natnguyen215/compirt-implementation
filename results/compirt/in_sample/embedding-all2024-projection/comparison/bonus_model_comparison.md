# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.905696 | 0.913158 | 0.00746207 | synergy |
| log_loss | 0.398597 | 0.380812 | -0.0177853 | synergy |
| ece | 0.0496548 | 0.0356412 | -0.0140136 | synergy |
| accuracy | 0.820075 | 0.830452 | 0.0103776 | synergy |
| part_accuracy | 0.820075 | 0.830452 | 0.0103776 | synergy |
| exact_acc | 0.537011 | 0.560838 | 0.0238272 | synergy |
| per_bonus_points_mae | 5.45068 | 5.11329 | -0.337392 | synergy |
| ppb_mae | 2.68396 | 1.90665 | -0.777312 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
