# TF-IDF CompIRT Equation Flow

This note documents the isolated `tfidf` pyramidal experiment. It keeps the
root `pyramidal_model.py` untouched and selects the cumulative TF-IDF form with
`--tfidf-variant cumulative-difficulty`.

## Shared Feature Construction

Feature construction happens before Pyro sees the data. The trainer calls
`attach_tfidf_prefix_scores`, which attaches one matrix aligned to
`data["tossup_ids"]`:

```text
tfidf_prefix[j, t] = cumulative TF-IDF revealed through token t
```

By default `tfidf_prefix[j, T_j] = 1.0` for every nonempty tossup.

Each token's weight is its document-normalized term frequency times the corpus
IDF (no `+1` floor, so ubiquitous words with `df == N` collapse to ~0):

```text
tfidf(w) = (count(w) / doc_length) * idf(w)
idf(w)   = log((1 + N) / (1 + df(w)))
```

## Shared Baseline Terms

The original CompIRT player and tossup priors are unchanged:

```text
theta_i ~ Normal(0, I)
c_i     ~ Normal(0, 1)
alpha_j ~ Normal(0, I)
beta_j  ~ Normal(0, 1)
gamma_j ~ HalfCauchy(5)
mu_j    ~ Beta(2, 2)
```

The baseline difficulty, correctness, and hazard are:

```text
d_j(t) = beta_j * sigmoid(gamma_j * (mu_j - t / T_j))
correctness_ij(t) = theta_i^T alpha_j - d_j(t)
hazard_ij(t) = correctness_ij(t) - c_i
```

## Cumulative TF-IDF difficulty

Keep the base position curve and learn how much cumulative TF-IDF lowers
difficulty:

```text
lambda_tfidf ~ HalfNormal(tfidf_effect_prior_scale)
d'_j(t) = d_j(t) - lambda_tfidf * tfidf_prefix[j, t]
correctness_ij(t) = theta_i^T alpha_j - d'_j(t)
hazard_ij(t) = correctness_ij(t) - c_i
```

This variant saves `tfidf_adjustment_curves.csv` as a signed additive difficulty
delta. Evaluators replay `d'_j(t)` by adding that negative delta to the saved
base curve.

## Likelihood and Replay

The cumulative model uses the competing-risks likelihood:

```text
log S_ij(t*) = sum_{u < t*} log(1 - sigmoid(hazard_ij(u)))

log L =
  sum_i log S_ij(t*)
  + log sigmoid(hazard_i*j(t*))
  + log Bernoulli(y_i*j | sigmoid(correctness_i*j(t*)))
```

`posterior_row_predictions` and `expected_first_buzz_positions` replay the same
cumulative equations used during training. `tossup_predictions.csv` gets
`tfidf_prefix_score`.

## Code Flow

```text
train_tfidf_pyramidal.py
  -> load_hf_tables / filter_tournament
  -> build_tossup_observations
  -> tossup_tensors
  -> attach_tfidf_prefix_scores
  -> fit_svi(competing_risks_model, ..., cumulative-difficulty)
  -> posterior_row_predictions
  -> optional expected_first_buzz_positions
  -> save CSVs, plots, and summary.json
```

Important outputs:

- `summary.json`: records `tfidf_variant`, formula, feature metadata, and the
  learned cumulative TF-IDF coefficient.
- `tossup_predictions.csv`: per-row fitted correctness, hazard, survival, and
  IDF diagnostics.
- `tfidf_adjustment_curves.csv`: only for `cumulative-difficulty`.
