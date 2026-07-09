# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.933456 | 0.938785 | 0.00532835 | synergy |
| log_loss | 0.337605 | 0.325077 | -0.0125288 | synergy |
| ece | 0.0369495 | 0.0365809 | -0.000368541 | synergy |
| accuracy | 0.853382 | 0.859629 | 0.00624717 | synergy |
| part_accuracy | 0.853382 | 0.859629 | 0.00624717 | synergy |
| exact_acc | 0.612317 | 0.627419 | 0.0151024 | synergy |
| per_bonus_points_mae | 4.82446 | 4.55836 | -0.266103 | synergy |
| ppb_mae | 2.07937 | 1.68455 | -0.394816 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
