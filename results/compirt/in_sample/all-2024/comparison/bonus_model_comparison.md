# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.93318 | 0.939144 | 0.0059641 | synergy |
| log_loss | 0.341453 | 0.328479 | -0.0129744 | synergy |
| ece | 0.0415155 | 0.0447856 | 0.0032701 | no-synergy |
| accuracy | 0.852301 | 0.858693 | 0.00639138 | synergy |
| part_accuracy | 0.852301 | 0.858693 | 0.00639138 | synergy |
| exact_acc | 0.611662 | 0.626453 | 0.0147908 | synergy |
| per_bonus_points_mae | 4.82035 | 4.5566 | -0.263754 | synergy |
| ppb_mae | 2.17874 | 1.76204 | -0.416696 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
