# Learned-topic CompIRT (joint sLDA)

Learns each question's topic mixture jointly with CompIRT instead of loading it
from a CSV. A document's Dirichlet topic proportions `theta_doc` generate its
bag of words and, for tossups, serve as the relevance vector `r_j`, so buzz and
correctness outcomes shape the topics. This follows supervised LDA (Blei and
McAuliffe, [arXiv:1003.0783](https://arxiv.org/abs/1003.0783)) except that the
CompIRT likelihood replaces sLDA's response regression `eta^T z_bar`.

## Model

```text
theta_doc ~ Dirichlet(topic_concentration * 1_K)       every tossup and bonus document
topic_word = softmax(topic_word_logits)                 point estimate, shape (K, V)
bow ~ Multinomial(theta_doc @ topic_word)               scaled by bow_weight
tossup logit = sum_k r_jk * (theta_ik - d_jk(t)),   r_j = theta_doc_j
```

- Summing out the per-word topic assignments leaves the multinomial mixture,
  so there are no discrete latents. One `AutoNormal` guide covers every latent
  and training uses `utils.training.fit_svi`.
- `K` is both the topic count and the skill dimension.
- Documents are ordered tossups first, in `data["tossup_ids"]` order, so
  `theta_doc[:n_tossups]` lines up with the IRT rows.
- Bonuses enter Stage 1 as word-only documents, which places them in the
  tossup topic space.
- The difficulty curve, hazard, and first-buzz likelihood come from
  [`../fixed/topic_compirt/pyramidal.py`](../fixed/topic_compirt/pyramidal.py);
  see [`../fixed/equation_flow.md`](../fixed/equation_flow.md).
- Saved `beta_*` columns are CompIRT difficulty. The topic-word matrix is saved
  separately as `topic_word_matrix.npy` with `vocabulary.json`.

| Paper symbol | Code |
| --- | --- |
| LDA `alpha` | `topic_concentration` (`--topic-concentration`, default 1.0) |
| `theta_d` | `theta_doc` |
| `phi` | `topic_word` |
| `z_dn`, LDA word prior | not present |
| CompIRT `beta` | `difficulty_beta`; Pyro site and CSV prefix `beta` |

**Stage 2.** `train_joint_compositional.py` fixes Stage-1 `theta` and
`topic_word`, then refits each bonus's `theta_doc` against its words and its
part correctness, using it as `r_b`. Freezing `topic_word` keeps topic axis `k`
aligned with skill axis `k`. The three parts of a bonus share one `theta_doc`.

**Held-out runs.** `train_joint_pyramidal.py --train-topic-model <train dir>`,
used with `--train-posterior`, freezes the training `topic_word` and vocabulary
so held-out documents are placed on the trained axes.

**Limits.** There is no encoder, so a new question has no topic vector until it
is fitted with `topic_word` held fixed. Stage 2 cannot move player skills or the
topic axes.

## Files

| File | Role |
| --- | --- |
| `bow.py` | Vocabulary and count matrix aligned to a given ID order |
| `joint_pyramidal.py`, `train_joint_pyramidal.py` | Stage 1 model and trainer; writes `topic_word_matrix.npy`, `vocabulary.json`, `topics.csv`, and `document_latent_vectors.csv` |
| `joint_compositional.py`, `train_joint_compositional.py` | Stage 2 model and trainer |
| `slda_responses.py`, `topic_response_profiles.py` | Diagnostics: outcomes grouped by each question's dominant topic |

## Commands

```bash
.venv/bin/python -m topic.learned.train_joint_pyramidal \
  --split year_2024 --dimensions 5 --steps 2000 --output-dir <ROOT>/pyramidal
.venv/bin/python -m topic.learned.train_joint_compositional --split year_2024 \
  --player-skills <ROOT>/pyramidal/players.csv \
  --topic-model-dir <ROOT>/pyramidal --output-dir <ROOT>/compositional
.venv/bin/python -m topic.fixed.evaluate_topic_compirt \
  --pyramidal-results <ROOT>/pyramidal \
  --compositional-results <ROOT>/compositional --output-dir <ROOT>/evaluation
.venv/bin/python -m topic.learned.topic_response_profiles \
  --vectors <ROOT>/pyramidal/document_latent_vectors.csv --split year_2024
```

Stage 2 infers `K` from `theta` and takes the vocabulary from Stage 1, so
`--vocab-size`, `--min-df`, and `--rm-top` are set in Stage 1.
`--bow-weight` balances the word likelihood against the IRT likelihood; at the
default 1.0 the word counts dominate. `--topic-concentration` below 1 favors
sparser mixtures. Results are sensitive to both, so record them with each run.

`run_scripts/topic/run_learned_topic_ablation.py` sweeps `K` on held-out runs.

## Saved runs

`learned-topic-all2024` and `learned-topic-all2024-cal` are in
[`results/compirt/in_sample/topic/`](../../../results/compirt/in_sample/topic/)
and [`results/compirt/holdout/topic/`](../../../results/compirt/holdout/topic/).
