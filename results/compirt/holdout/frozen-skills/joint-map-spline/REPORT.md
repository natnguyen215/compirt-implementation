# Joint training of the original frozen spline model

Five existing whole-game holdouts: 46,640 race events and 45,995 first buzzes.
Both new arms start from the saved original timing and correctness coefficients, verified against saved held-out probabilities before fitting.
Each arm gets 1000 additional full-batch Adam steps at lr 0.005. This is warm-started MAP fine-tuning, not Pyro VI or training from scratch.
The joint arm lets correctness update theta and speed. The blocked arm detaches those traits from correctness, while timing continues to learn from timing observations. Correctness follows the moving detached traits; this is a matched no-feedback control, not a permanently frozen checkpoint.
The original timing penalty and all correctness L2 penalties are retained; the global correctness intercept stays unpenalized. The objective sums race and correctness log likelihoods with coefficient one, then adds penalties. Dividing the entire objective by training race count only rescales optimization.
Training-buzz-row mean and standard deviation (floor 0.1) are recomputed from current traits at each step; the joint arm differentiates through this training-only standardization. Final transforms are saved for replay.

| Model | Timing MAE | Correctness loss | Correctness accuracy | Joint loss |
| --- | ---: | ---: | ---: | ---: |
| frozen_skills | 0.14307 | 0.48117 | 78.76% | 6.37347 |
| pyro_frozen_skills | 0.14802 | 0.47612 | 78.86% | 6.42435 |
| saved_compirt | 0.15186 | 0.48777 | 77.95% | 6.61553 |
| original_spline_blocked | 0.14298 | 0.48117 | 78.76% | 6.37299 |
| original_spline_joint | 0.14301 | 0.48176 | 78.66% | 6.37390 |

Lower losses are better. Accuracy uses threshold 0.5. No held-out outcomes select settings or stopping.
Use joint versus blocked to assess correctness feedback under this initialization and budget. Comparison with the original saved fit also changes optimization budget. These reused development folds do not establish future-season or unseen-item performance.
Game-bootstrap intervals (2,000 resamples) condition on fixed fits and exclude refit uncertainty and cross-game question dependence. Saved DD predates the likelihood repair; replay is normalized but it is not a repaired refit.
Every correctness prediction replays from a saved artifact on CPU with outcomes erased. The full timing PMFs are checked for normalization.

Reproduce (code archived under `archive/frozen_skills/`): `PYTHONPATH=archive:. .venv/bin/python -m frozen_skills.joint`.
