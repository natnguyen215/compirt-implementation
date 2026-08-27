# Double-Bernstein grid-search summary

Evaluation regime: 5-fold frozen whole-game matrix infill, tossups only.
Primary selection metric: pooled `joint_tossup_event_log_loss` (lower is better).
Relevance prior: `simplex`.
Terminal intercepts: `False`.

Complete configurations: 1 / 1.

| rank | degree | curves | Dirichlet | joint log loss | correctness log loss | neg AUROC | integrated Brier | no-buzz Brier |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 3 | 3 | 2 | 6.7445 | 0.502545 | 0.711491 | 0.107777 | 0.0234669 |

## Selected configuration

- Degree: 3
- Curves/dimensions: 3
- Dirichlet concentration: 2
- Relevance prior: simplex
- Terminal intercepts: False
- Pooled joint event log loss: 6.7445

This is the CV winner, not an unbiased final-test estimate. Refit and assess it on an untouched test set, or use nested CV, before reporting a final generalization number.
