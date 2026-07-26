# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.905696 | 0.913158 | 0.00746207 | synergy |
| log_loss | 0.398597 | 0.380812 | -0.0177853 | synergy |
| ece | 0.0496548 | 0.0356412 | -0.0140136 | synergy |
| part_accuracy | 0.820075 | 0.830452 | 0.0103776 | synergy |
| part_accuracy_macro_team | 0.82275 | 0.832946 | 0.0101962 | synergy |
| part_accuracy_macro_game | 0.82019 | 0.830577 | 0.0103864 | synergy |
| part_accuracy_macro_bonus | 0.809565 | 0.83049 | 0.0209248 | synergy |
| exact_acc | 0.537011 | 0.560838 | 0.0238272 | synergy |
| ppb_mae | 1.98244 | 0.757519 | -1.22493 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
