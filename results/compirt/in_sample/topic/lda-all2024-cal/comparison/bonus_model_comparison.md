# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.910794 | 0.919409 | 0.00861498 | synergy |
| log_loss | 0.378086 | 0.361808 | -0.0162775 | synergy |
| ece | 0.00953195 | 0.0174484 | 0.00791644 | no-synergy |
| part_accuracy | 0.828167 | 0.838994 | 0.0108271 | synergy |
| part_accuracy_macro_team | 0.829578 | 0.841488 | 0.0119095 | synergy |
| part_accuracy_macro_game | 0.828219 | 0.839209 | 0.0109902 | synergy |
| part_accuracy_macro_bonus | 0.83355 | 0.839971 | 0.00642143 | synergy |
| exact_acc | 0.555039 | 0.578259 | 0.0232203 | synergy |
| ppb_mae | 1.64447 | 0.540928 | -1.10354 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
