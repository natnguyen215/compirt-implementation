# CompIRT Bonus Model Comparison

| metric               |   no_synergy |   synergy |   synergy_minus_no_synergy | better_in_sample   |
|:---------------------|-------------:|----------:|---------------------------:|:-------------------|
| auc                  |    0.933114  | 0.93904   |                 0.00592558 | synergy            |
| log_loss             |    0.342574  | 0.32892   |                -0.0136535  | synergy            |
| ece                  |    0.0425078 | 0.0449132 |                 0.00240544 | no-synergy         |
| part_accuracy        |    0.852661  | 0.857854  |                 0.00519253 | synergy            |
| exact_score_accuracy |    0.606289  | 0.62416   |                 0.0178704  | synergy            |
| per_bonus_points_mae |    4.82858   | 4.56524   |                -0.26334    | synergy            |
| ppb_mae              |    2.1686    | 1.80906   |                -0.35954    | synergy            |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
