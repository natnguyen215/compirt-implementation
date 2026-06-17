# Simple MIRT Baseline

This folder contains the simplest modeling path in the project. Start here
before working on the CompIRT models in the project root.

## Files

- `model.py`: the compensatory multidimensional IRT model.
- `train.py`: SVI and MCMC training plus CSV output.
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
