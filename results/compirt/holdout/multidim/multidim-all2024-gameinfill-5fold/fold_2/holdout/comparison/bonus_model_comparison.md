# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.886487 | 0.894051 | 0.00756392 | synergy |
| log_loss | 0.425455 | 0.414519 | -0.0109356 | synergy |
| ece | 0.0195432 | 0.0328488 | 0.0133056 | no-synergy |
| brier | 0.135467 | 0.132156 | -0.0033111 | synergy |
| accuracy_lift_over_all_correct | 0.286224 | 0.292583 | 0.00635881 | synergy |
| part_accuracy | 0.805591 | 0.81195 | 0.00635881 | synergy |
| part_accuracy_macro_team | 0.809463 | 0.81624 | 0.00677697 | synergy |
| part_accuracy_macro_bonus | 0.805242 | 0.808329 | 0.00308709 | synergy |
| exact_acc | 0.507619 | 0.523787 | 0.0161684 | synergy |
| ranked_probability_score | 0.116623 | 0.112259 | -0.00436389 | synergy |
| bonus_total_score_log_loss | 1.02168 | 0.992657 | -0.0290258 | synergy |
| ppb_mae | 2.35346 | 1.87625 | -0.477213 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
