# Embedding-relevance CompIRT

A `multidim_mirt` variant whose relevance vector `r` is projected from a frozen
question embedding instead of learned freely, following CAIMIRA
([arXiv:2410.06524](../../../docs/2410.06524v1.pdf)):

```text
e_j  = Qwen3-Embedding-8B("Instruct: ...\nQuery: " + question text)
r_j  = softmax(W_2 gelu(W_1 (e_j - mean_e) + b_1) + b_2)
d_jk(t) = beta_jk * sigmoid(gamma_jk * (mu_jk - t / T_j))
logit_ij(t) = sum_k r_jk * (theta_ik - d_jk(t))
```

CAIMIRA uses one linear map; this uses a two-layer FFN (128 hidden units) on
centered embeddings. The FFN weights are point estimates fitted jointly with
`theta`, `beta`, `gamma`, and `mu` by the usual `AutoNormal` SVI. A saved
linear projection (`kind == "linear"`) still loads.

Because `r_j` sums to 1, raising `--dimensions` spreads a fixed relevance
budget rather than adding capacity, so dimension sweeps are not comparable with
`multidim_mirt`, whose `r ~ Gamma(2, 2)` is unnormalized. The default width is
5, where CAIMIRA's validation loss plateaus.

## Pipeline

| Step | Output |
| --- | --- |
| `embed_questions.py` | `outputs/{tossup,bonus}_embeddings.npz`: one vector per tossup and per bonus (leadin plus parts). The model is re-downloaded if its cache is missing. |
| `train_pyramidal.py` | `players.csv`, `tossups.csv`, and `r_projection.npz` (FFN weights and the tossup embedding mean) |
| `train_compositional.py` | Bonus stage: fixed `theta` and the frozen projection give each bonus's `r`; each part learns its own per-dimension difficulty, plus `tau` and optional synergy |
| root `evaluate_compirt.py` | Metrics and report from the numbered-column CSVs |

```bash
.venv/bin/python -m multidimensional.embedding_mirt.embed_questions --device cuda
.venv/bin/python -m multidimensional.embedding_mirt.train_pyramidal --device cuda --output-dir <ROOT>/pyramidal
.venv/bin/python -m multidimensional.embedding_mirt.train_compositional --device cuda \
  --player-skills <ROOT>/pyramidal/players.csv \
  --projection <ROOT>/pyramidal/r_projection.npz --output-dir <ROOT>/compositional
```

`run_scripts/multidimensional/embedding/run_embedding_compirt.py` chains these
with synergy, evaluation, and comparison.

With `--train-posterior` and `--new-player-prior`, a held-out run carries the
player prior across the split but fits its own projection, so dimension `k`
need not mean the same thing in the training and held-out runs.

## Saved runs

[`results/compirt/in_sample/embedding/`](../../../results/compirt/in_sample/embedding/)
holds `embedding-all2024` and `embedding-all2024-cal` with their
`-projection` counterparts.
