# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.912494 | 0.927395 | 0.0149013 | synergy |
| log_loss | 0.376319 | 0.345773 | -0.0305459 | synergy |
| ece | 0.0210548 | 0.0244892 | 0.00343436 | no-synergy |
| accuracy | 0.82847 | 0.847168 | 0.0186974 | synergy |
| part_accuracy | 0.82847 | 0.847168 | 0.0186974 | synergy |
| exact_acc | 0.554422 | 0.597181 | 0.0427598 | synergy |
| per_bonus_points_mae | 5.32994 | 4.81641 | -0.513523 | synergy |
| ppb_mae | 2.63971 | 1.68331 | -0.956404 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
