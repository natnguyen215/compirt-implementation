# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.918031 | 0.930324 | 0.0122923 | synergy |
| log_loss | 0.367085 | 0.343419 | -0.023666 | synergy |
| ece | 0.026544 | 0.034373 | 0.00782896 | no-synergy |
| accuracy | 0.836094 | 0.849956 | 0.0138617 | synergy |
| part_accuracy | 0.836094 | 0.849956 | 0.0138617 | synergy |
| exact_acc | 0.576056 | 0.606155 | 0.0300987 | synergy |
| per_bonus_points_mae | 5.14453 | 4.74466 | -0.399866 | synergy |
| ppb_mae | 2.49301 | 1.82214 | -0.67087 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
