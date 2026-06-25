# CompIRT Bonus Model Comparison

| metric               |   no_synergy |   synergy |   synergy_minus_no_synergy | better_in_sample   |
|:---------------------|-------------:|----------:|---------------------------:|:-------------------|
| auc                  |    0.931396  | 0.932551  |                0.00115538  | synergy            |
| log_loss             |    0.339466  | 0.33882   |               -0.000645668 | synergy            |
| ece                  |    0.0326297 | 0.0358422 |                0.00321244  | no-synergy         |
| part_accuracy        |    0.848727  | 0.851207  |                0.00248013  | synergy            |
| exact_score_accuracy |    0.601771  | 0.609751  |                0.00797986  | synergy            |
| per_bonus_points_mae |    4.84208   | 4.68489   |               -0.157188    | synergy            |
| ppb_mae              |    2.22444   | 1.79197   |               -0.432473    | synergy            |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
