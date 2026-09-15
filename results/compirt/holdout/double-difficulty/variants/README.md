# Variants

These experiments change model structure rather than a reference-model setting.
Each is compared with [`dd-bernstein-332-simplex-locations-terminal`](../ablations/relevance-locations-terminal/dd-bernstein-332-simplex-locations-terminal/).

| Folder | Change | Result |
| --- | --- | --- |
| [`player-neg-propensity/`](player-neg-propensity/) | Adds a hierarchical per-player neg propensity term. | Results are close to the reference on the main metrics (joint LL 6.5831 versus 6.6124); the added parameter has little effect. §3.10 |
| [`perceived-difficulty/`](perceived-difficulty/) | Players respond to a *perceived* difficulty rather than the true curve. Six arms: `unconstrained`, `positive-alpha`, `three-slice`, `three-slice-10000-steps`, `three-slice-alternating`, `three-slice-alternating-10000-steps`. | All arms underperform the reference on correctness LL and ECE; several fall below the 0.7670 always-correct accuracy baseline. §3.8 |
| [`perceived-logit/`](perceived-logit/) | Applies perception on the logit scale. Includes `unconstrained` and `positive-alpha`. | Both underperform the reference; `positive-alpha` has 0.3458 ECE and 0.3758 accuracy. §3.9 |

The perceived-difficulty and perceived-logit families are retained as negative
results, not candidate models.
