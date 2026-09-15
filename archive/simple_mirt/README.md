# Simple MIRT

The project's original compensatory multidimensional IRT example. It is not
part of the two-stage CompIRT pipeline.

```text
P(player i answers question j correctly) = sigmoid(alpha_j^T theta_i - d_j)
```

| File | Role |
| --- | --- |
| `model.py` | The Pyro model |
| `train.py` | SVI or MCMC fit on `data/response_matrix.csv`; writes `players.csv` and `questions.csv` to `results/` |
| `visualize.py` | Diagnostic plots from those CSVs |
| `tossups_matrix.py` | Builds the response matrix from the SQLite database |
| `train_plain_irt.py` | Fits `model.py` on CompIRT tossup observations (1 only for a correct first buzz) as the plain-IRT comparator in the drop-robustness study, whose code is in `results/compirt/in_sample/common/drop-robustness/code/` |

```bash
.venv/bin/python simple_mirt/train.py --device cpu
.venv/bin/python simple_mirt/visualize.py
.venv/bin/python -m simple_mirt.train_plain_irt --help
```
