# DD-Bernstein: 3,000 versus 10,000 steps

Fresh fits with identical degree 3, dimensions 3, drop concentration 2, simplex relevance, learned locations, terminal intercepts, learning rate 0.005 and seeds 42. All five year_2024 game folds. Historical 3,000-step comparator already uses the normalized likelihood. No bonus stages were refit in this convergence experiment.

Pooled normalized full-grid event scoring on matched observations. Correctness and position metrics condition on observed buzzes. No-buzz rate is the model probability, not deterministic threshold replay.

| Metric | 3,000 steps | 10,000 steps | Change |
| --- | ---: | ---: | ---: |
| events | 46640.00000000 | 46640.00000000 | +0.00000000 |
| buzz_events | 45995.00000000 | 45995.00000000 | +0.00000000 |
| timing_mae | 0.15442760 | 0.14182322 | -0.01260438 |
| timing_rmse | 0.18857691 | 0.17722770 | -0.01134922 |
| timing_bias | -0.05011504 | -0.01681502 | +0.03330002 |
| integrated_brier | 0.10184051 | 0.09528995 | -0.00655056 |
| timing_nll | 4.47417487 | 4.36050990 | -0.11366497 |
| race_nll | 6.12323137 | 5.97382434 | -0.14940702 |
| joint_nll | 6.60427191 | 6.45597713 | -0.14829478 |
| first_buzzer_accuracy | 0.35332101 | 0.36801826 | +0.01469725 |
| first_buzzer_nll | 1.67218165 | 1.63593838 | -0.03624327 |
| dead_brier | 0.01524258 | 0.01418500 | -0.00105758 |
| predicted_dead_rate | 0.03121129 | 0.02199946 | -0.00921183 |
| observed_dead_rate | 0.01382933 | 0.01382933 | +0.00000000 |
| correctness_auc | 0.71536705 | 0.71308511 | -0.00228194 |
| correctness_log_loss | 0.48778630 | 0.48891414 | +0.00112784 |
| correctness_ece | 0.00965472 | 0.00748409 | -0.00217063 |
| correctness_brier | 0.15823993 | 0.15856546 | +0.00032553 |
| correctness_accuracy | 0.77934558 | 0.77843244 | -0.00091314 |
| correctness_all_correct_accuracy | 0.76699641 | 0.76699641 | +0.00000000 |
| correctness_accuracy_lift_over_all_correct | 0.01234917 | 0.01143603 | -0.00091314 |
| correctness_probability_std | 0.14052190 | 0.14879033 | +0.00826844 |
| correctness_probability_p10 | 0.58120500 | 0.56300937 | -0.01819563 |
| correctness_probability_p50 | 0.81248736 | 0.80806920 | -0.00441816 |
| correctness_probability_p90 | 0.91802656 | 0.92051070 | +0.00248414 |
| correctness_mean_predictive_variance | 0.15398005 | 0.15476777 | +0.00078771 |
| incorrect_probability | 0.22382335 | 0.22964159 | +0.00581824 |
| incorrect_observed_rate | 0.23300359 | 0.23300359 | +0.00000000 |
| neg_f1 | 0.23166023 | 0.25433526 | +0.02267503 |

## Training diagnostics

| Steps | Fold | Terminal hazard intercept | Final loss | Last 100-step loss slope |
| --- | --- | ---: | ---: | ---: |
| 3000 | 0 | 3.999001 | 284523.762 | -4.094974 |
| 3000 | 1 | 3.997535 | 285519.233 | -4.286574 |
| 3000 | 2 | 4.032016 | 284830.107 | -3.822925 |
| 3000 | 3 | 4.005063 | 286269.032 | -4.501195 |
| 3000 | 4 | 3.995170 | 284402.919 | -4.474303 |
| 10000 | 0 | 3.727831 | 277683.285 | -1.122303 |
| 10000 | 1 | 3.749171 | 278693.346 | -1.178201 |
| 10000 | 2 | 3.733216 | 277823.736 | -0.880383 |
| 10000 | 3 | 3.682690 | 279188.919 | -1.507524 |
| 10000 | 4 | 3.703988 | 277353.005 | -1.294201 |

Single optimization seed, reused development folds. The likelihood correction is held fixed; this comparison changes optimization duration.
