# Embedding-Relevance CompIRT

This package contains the content-aware sibling of `multidimensional/multidim_mirt/`. Instead of
a freely learned, positive `alpha ~ Gamma(2, 2)` discrimination vector, every
tossup and bonus gets a relevance vector `r` computed from a frozen text
embedding, following CAIMIRA (`docs/2410.06524v1.pdf`, arXiv 2410.06524, Eq. 5/7):

```text
e_j = Qwen3-Embedding-8B("Instruct: ...\nQuery: " + question text)
e'_j = e_j - mean_e
r_j = softmax(W_2 gelu(W_1 @ e'_j + b_1) + b_2)
d_jk(t) = beta_jk * sigmoid(gamma_jk * (mu_jk - t / T_j))
logit_ij(t) = sum_k r_jk * (theta_ik - d_jk(t))
```

CAIMIRA uses a single linear `W_R`/`b_R` map; this implementation now uses a
small FFN projection and centers embeddings first to remove the shared Qwen
mean direction. The FFN weights are point-estimated jointly with
`theta`/`beta`/`gamma`/`mu` by the same `AutoNormal` + SVI loop the rest of
CompIRT uses. Everything else is reused, not reimplemented:
`difficulty_curve`/`correctness_logit`/`hazard_logit`/`log_survival` are
imported directly from `multidimensional.multidim_mirt.pyramidal_model` (they
already take an `alpha`-shaped argument positionally -- `r` fills that slot),
and `lse_aggregation`/`synergy_contribution` are imported directly from the
root `compositional_model.py`.

The bonus (compositional) stage reuses the **same fitted FFN projection and
tossup embedding mean** from the pyramidal run, frozen -- it does not learn its
own projection, the same way it already reuses `theta` as fixed input from
Stage 1.

## Pipeline

```text
embed_questions.py            -> outputs/{tossup,bonus}_embeddings.npz
train_pyramidal.py            -> players.csv, tossups.csv, r_projection.npz
train_compositional.py        -> bonus_parts.csv, team_predictions.csv
evaluate_compirt.py           -> metrics, plots, experiment_report.md
```

**`embed_questions.py`**: loads the linked HF tables, embeds each tossup's full
question text and each bonus's leadin + part text through
`Qwen/Qwen3-Embedding-8B` (one embedding per tossup/bonus, shared across a
bonus's three parts), and caches the vectors to `.npz` (the embedding
dimensionality is in the thousands, so a wide CSV like the topic model's
`latent_topic_N` columns isn't practical here).

**`train_pyramidal.py`** (Stage 1): attaches each tossup's cached embedding,
subtracts the tossup embedding mean, fits player skills `theta`, per-dimension
difficulty curves, and the `r` FFN projection via Pyro SVI, then saves the
usual player/tossup CSVs plus `r_projection.npz`.

**`train_compositional.py`** (Stage 2): loads the fixed `theta` from Stage 1
and the frozen `r_projection.npz`, subtracts the saved tossup embedding mean
from bonus embeddings, computes each bonus's `r` through that frozen
projection, and fits only bonus-part difficulty, `tau`, and optional synergy.

Both stages reuse `evaluate_compirt.py` unmodified -- it only reads the
numbered-column CSV schema (`theta_1..K`, `r_1..K`, etc.), the same schema
`multidim_mirt` already produces.

## Running it

```bash
.venv/bin/python -m multidimensional.embedding_mirt.embed_questions --device cuda
.venv/bin/python -m multidimensional.embedding_mirt.train_pyramidal --device cuda
.venv/bin/python -m multidimensional.embedding_mirt.train_compositional --device cuda \
    --player-skills results/compirt/embedding-pyramidal/players.csv \
    --projection results/compirt/embedding-pyramidal/r_projection.npz
.venv/bin/python evaluate_compirt.py --help  # Stage 2 + eval reuse the root evaluator
```

The default relevance/skill width is 5 dimensions, matching the CAIMIRA
ablation (validation loss plateaus at `m = 5`) and the width `multidim_mirt`'s
own convenience run scripts use (its bare CLI default is 1).

Note `r_j` is a softmax and always sums to 1 across dimensions, unlike
`alpha ~ Gamma(2, 2)`, which is unbounded above with mean 1 per dimension
regardless of `n_dimensions`. Raising `--dimensions` here spreads a fixed
relevance budget thinner rather than adding independent discriminative
capacity, so `--dimensions` sweeps are not directly comparable between the two
packages -- this is CAIMIRA's design, not a bug.

## Held-out (temporal split) runs

`train_pyramidal.py` supports `--train-posterior`/`--new-player-prior` like the
other variants, which carries the **player** prior across a temporal split.
The `r` projection is *not* frozen across splits the way `topic/learned`'s
topic-word matrix is -- a held-out run fits its own projection jointly with
that split's `theta`/`beta`/`gamma`/`mu`, the same way
`multidim_mirt`/baseline never freeze `alpha` across splits either. This
matches the repo's established "co-estimate item parameters on held-out
responses" approach (see `docs/compirt_deep_dive.md` §7); it means dimension
`k`'s content in a held-out run isn't guaranteed to line up with dimension `k`
from the training run, but that's true of `alpha`'s dimensions too and doesn't
affect either run's own internal fit.
