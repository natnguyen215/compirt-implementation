# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.91558 | 0.924547 | 0.0089666 | synergy |
| log_loss | 0.367053 | 0.349022 | -0.0180312 | synergy |
| ece | 0.00921776 | 0.0138288 | 0.00461103 | no-synergy |
| accuracy | 0.833184 | 0.844003 | 0.0108181 | synergy |
| part_accuracy | 0.833184 | 0.844003 | 0.0108181 | synergy |
| exact_acc | 0.563767 | 0.588084 | 0.024316 | synergy |
| per_bonus_points_mae | 5.06535 | 4.7613 | -0.304053 | synergy |
| ppb_mae | 2.35344 | 1.65488 | -0.69856 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
