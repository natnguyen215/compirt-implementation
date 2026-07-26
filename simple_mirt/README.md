# Simple MIRT Baseline (Legacy/Pedagogical)

This folder contains the project's original, deliberately simple MIRT example.
It is useful for learning the basic Pyro workflow, but it is not part of the
two-stage CompIRT paper pipeline and is not used by the full-pipeline
experiment runners. New CompIRT development should start with the model files
in the project root.

One exception: `train_plain_irt.py` reuses `model.py` as the "plain IRT"
comparator for the drop-robustness study (`run_scripts/common/run_drop_robustness.py`),
fed from the CompIRT observation tables rather than the legacy SQLite matrix.

## Files

- `model.py`: the compensatory multidimensional IRT model.
- `train.py`: SVI and MCMC training plus CSV output.
- `train_plain_irt.py`: fits `model.py` on the CompIRT tossup observations
  (run as `-m simple_mirt.train_plain_irt` from the repo root); supports the
  `--drop-events` lists used by the drop-robustness runners.
- `visualize.py`: diagnostic plots for fitted baseline results.
- `tossups_matrix.py`: standalone helper for building a response matrix directly
  from SQLite.

The baseline reads `data/response_matrix.csv` and writes to `results/` at the
project root.

From the project root, run:

```bash
.venv/bin/python simple_mirt/train.py --device cpu
.venv/bin/python simple_mirt/visualize.py
```
