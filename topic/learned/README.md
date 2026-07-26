# Joint topic-gated CompIRT (sLDA-style)

A Dirichlet topic model implemented in **Pyro** and trained *jointly* with the
CompIRT IRT model, so the buzz/answer outcomes propagate into the topics.

This is supervised-LDA in *spirit* (Blei & McAuliffe, *Supervised Topic Models*,
NeurIPS 2007 / [arXiv:1003.0783](https://arxiv.org/abs/1003.0783)) but **not** the
canonical form: there is no separate response-regression coefficient `eta`.
Instead, each question's topic proportions `theta_doc` **double as** the CompIRT
topic weight `r_j`, which gates the IRT likelihood directly — so the same vector
explains the words *and* weights the skill dimensions. Read it as "learned `r_j`,"
not as a drop-in Blei–McAuliffe sLDA.

Unlike the unsupervised `topic/fixed/` pipeline (LDA/PLDA with fixed topic
weights from a CSV), here the per-question topic proportions are a **latent of
the CompIRT model itself** and are learned in the same SVI as the player skills
and tossup difficulties.

## Notation map

The same Greek letters mean different things in LDA, sLDA, and CompIRT. In this
directory, use this map first:

| Concept | Paper notation | Code name | Notes |
|---|---|---|---|
| Dirichlet concentration | `alpha` | `topic_concentration` | Hyperparameter, default `1.0`; the prior is `Dirichlet(topic_concentration * 1_K)`. |
| Document topic mixture | `theta_d` | `theta_doc` | Latent topic proportions for one tossup/bonus; sums to 1. |
| Word topic assignment | `z_dn` | not sampled | Integrated out; there is no `z` tensor in the code. |
| Average topic usage | `z_bar_d` | `theta_doc` / `topic_weight` | Canonical sLDA averages sampled `z`; this implementation uses the smooth latent `theta_doc` directly. |
| Topic-word matrix | often `phi`; sometimes LDA `beta` | `topic_word` | `topic_word[k, w] = P(word=w | topic=k)`. It is point-estimated from `topic_word_logits`, not sampled from a Dirichlet prior. |
| LDA word prior | `beta` or `eta` | none | Classic LDA may use `phi_k ~ Dirichlet(beta)`. This implementation does not have that hyperparameter. |
| CompIRT difficulty size | CompIRT `beta` | `difficulty_beta` in locals; saved as `beta_*` | Different from LDA `beta`; this is part of the tossup/bonus difficulty curve. The Pyro site remains `"beta"` for compatibility. |
| sLDA response coefficient | `eta` | none | Replaced by the CompIRT likelihood; there is no separate `eta^T z_bar` regression. |

## How it works

- Each document (tossup or bonus) has a Dirichlet topic-proportion latent
  `theta_doc`. Its prior is controlled by `--topic-concentration`, the Dirichlet
  `alpha`. The discrete per-word topic assignments of classic LDA marginalize
  out, so the word model is the LDA **mixture**
  `Multinomial(theta_doc @ topic_word)`
- For **tossups**, `theta_doc` is also the topic weight `r_j` that gates the
  competing-risks likelihood `sum_k r_jk (theta_ik - d_jk(t))`. So correctness
  supervises the topics directly.
- **Bonuses** can be supervised the same way: the learned compositional stage
  (`train_joint_compositional.py`) freezes the pyramidal stage's player skills
  `theta` and topic-word matrix `topic_word`, then re-learns each bonus's `theta_doc`
  so the bonus's own **part-correctness** outcomes reshape its place in topic
  space (sLDA-style supervision for bonuses). `topic_word` stays fixed so the bonus
  topic axes match the player-skill axes. (Alternatively, the original fixed-vector bonus stage reuses
  the pyramidal run's word-only bonus vectors without bonus-correctness.)
- The topic-word matrix `topic_word` is a point-estimated parameter (the variational-EM
  M-step). Because there is no amortizing encoder, **one `AutoNormal` guide**
  covers every latent (including `theta_doc`), so training reuses the existing
  `utils.training.fit_svi`.

The competing-risks math is reused from
`topic/fixed/topic_compirt/pyramidal.py`; the source of the topic weight is the
only difference (a learned Dirichlet latent in place of a fixed CSV).

## Files

- `bow.py` — vocabulary + bag-of-words matrix aligned to the model's document order (tested).
- `joint_pyramidal.py` — the joint Pyro tossup model (Dirichlet topics + LDA word model + topic-weighted competing-risks).
- `train_joint_pyramidal.py` — builds the corpus/BoW, runs the joint SVI, and exports the topic vectors, IRT parameters, and (for the bonus stage) the fixed `topic_word` as `topic_word_matrix.npy` + `vocabulary.json`.
- `joint_compositional.py` — the joint Pyro bonus model (Dirichlet topics + LDA word model with **fixed** `topic_word` + topic-weighted compositional likelihood).
- `train_joint_compositional.py` — loads the pyramidal stage's `theta` and `topic_word`, then runs the joint SVI so bonus part-correctness supervises the bonus topics.
- `slda_responses.py` / `topic_response_profiles.py` — **diagnostics** (not used in training): per-question correctness/buzz aggregates, and a profile of each learned topic by the outcomes of the questions that load on it.
- `tests/` — unit tests for BoW alignment, the response aggregation, and the joint compositional model.

## Usage

`--dimensions` is both the number of topics and the IRT skill dimension.

```bash
# 1. Jointly train topics + pyramidal tossup IRT.
.venv/bin/python -m topic.learned.train_joint_pyramidal \
  --split year_2024 --dimensions 5 --steps 2000 \
  --output-dir results/compirt/in_sample/topic/joint-slda-2024

# 2. Bonus stage (learned / sLDA): freeze the joint run's player skills + topic
#    axes (topic_word), and re-learn each bonus's topics supervised by its part-
#    correctness. --topic-model-dir points at the pyramidal output (for
#    topic_word_matrix.npy + vocabulary.json); --dimensions is inferred from theta.
.venv/bin/python -m topic.learned.train_joint_compositional \
  --split year_2024 \
  --player-skills results/compirt/in_sample/topic/joint-slda-2024/players.csv \
  --topic-model-dir results/compirt/in_sample/topic/joint-slda-2024 \
  --output-dir results/compirt/in_sample/topic/joint-slda-2024/compositional

#    (Alternative) original fixed-vector bonus stage: reuse the word-only bonus
#    vectors as fixed weights, with no bonus-correctness supervision of topics.
.venv/bin/python -m topic.fixed.train_topic_compositional \
  --split year_2024 \
  --player-skills results/compirt/in_sample/topic/joint-slda-2024/players.csv \
  --topic-vectors results/compirt/in_sample/topic/joint-slda-2024/document_latent_vectors.csv \
  --output-dir results/compirt/in_sample/topic/joint-slda-2024/compositional-fixed

# 3. Evaluate both stages together.
.venv/bin/python -m topic.fixed.evaluate_topic_compirt \
  --pyramidal-results results/compirt/in_sample/topic/joint-slda-2024 \
  --compositional-results results/compirt/in_sample/topic/joint-slda-2024/compositional \
  --output-dir results/compirt/in_sample/topic/joint-slda-2024/evaluation

# 4. (Optional) profile what each learned topic captures.
.venv/bin/python -m topic.learned.topic_response_profiles \
  --vectors results/compirt/in_sample/topic/joint-slda-2024/document_latent_vectors.csv \
  --split year_2024
```

In the **learned** bonus stage, each bonus's `theta_doc` is a fresh latent fit to
both its words (via the frozen `topic_word`) and its part-correctness, so bonus outcomes
*do* reshape the bonus topics — within the fixed topic axes, which keep them
aligned with the player skills `theta`. (The **fixed-vector** alternative instead
reuses the pyramidal run's word-only bonus vectors, so part-correctness does not
move the topics; the stage then only learns bonus-part difficulty.)

Key knobs (shared by both joint stages): `--bow-weight` scales the LDA word
likelihood against the IRT factor (too low → topics ignore words; too high →
topics ignore outcomes); `--topic-concentration` is the Dirichlet alpha (lower →
sparser topic mixes). The bonus stage takes the vocabulary from the pyramidal
stage, so `--vocab-size`, `--min-df`, `--rm-top` are set there.

**Choosing `--bow-weight`.** It is a likelihood-tempering knob, not something the
generative model pins down — each document has ~50–150 word tokens fighting only a
handful of buzz/answer outcomes, so at the default `1.0` the word likelihood
dominates and the topics come out nearly unsupervised. Do **not** leave it at the
default on faith: sweep it (e.g. `0.05`–`1.0`) and pick the value that maximizes a
**held-out IRT metric** (tossup correctness AUC / bonus-part log-loss), not the one
that gives the prettiest topics. Record the chosen value in the run notes — results
are sensitive to it, so an undocumented `bow_weight` makes a run irreproducible.

## Tests

```bash
PYTHONPATH=.:topic/fixed:topic/learned .venv/bin/python -m unittest discover -s topic/learned/tests -v
```

## Notes / limitations

- **No amortization.** `theta_doc` is a per-document latent fit directly, so
  there is no inference network to produce a topic vector for an unseen question
  without a fold-in step (a few SVI steps holding the topic-word matrix fixed).
- The joint step is heavier than the fixed-weight pyramidal stage (it adds one
  Dirichlet latent per document plus the word likelihood); use `--device cuda`
  or more `--steps` for a converged run. A few-step run produces well-formed but
  untrained topics.
- The learned bonus stage holds `theta` and `topic_word` fixed from the pyramidal run;
  it cannot move player skills or rotate the topic axes (faithful to the paper's
  two-stage design). Only the bonus `theta_doc` and bonus-part difficulty are
  learned, so the supervision reshapes *where each bonus sits* in topic space.
