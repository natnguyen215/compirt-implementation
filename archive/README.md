# Archive

Retired model families and studies. Live code must not import from here, and
`run_scripts/common/check_repo.py` does not run these tests. Each path mirrors
where it lived before it was archived: drop the `archive/` prefix to get the
original location.

| Path | What it was | Saved results |
| --- | --- | --- |
| [`topic/`](topic/) | Fixed-topic (PLDA, LDA, category), learned-topic (joint sLDA), and topic-TF-IDF CompIRT | [`in_sample/topic/`](../results/compirt/in_sample/topic/), [`holdout/topic/`](../results/compirt/holdout/topic/) |
| [`tfidf/`](tfidf/) | Cumulative TF-IDF difficulty, scalar and multidimensional | [`in_sample/tfidf/`](../results/compirt/in_sample/tfidf/) |
| [`multidimensional/embedding_mirt/`](multidimensional/embedding_mirt/) | Relevance projected from frozen Qwen3-Embedding-8B question embeddings | [`in_sample/embedding/`](../results/compirt/in_sample/embedding/) |
| `multidimensional/multidim_mirt/*_tanhbias.py` | Biased-tanh multidimensional difficulty | [`holdout/multidim/multidim-tanhbias-all2024/`](../results/compirt/holdout/multidim/multidim-tanhbias-all2024/) |
| [`dd_linear_spline/`](dd_linear_spline/) | Double-difficulty curves with knots at clue boundaries, plus a monotone variant | [`dd-linear-spline/`](../results/compirt/in_sample/double-difficulty/dd-linear-spline/), [`dd-monotone-linear-spline/`](../results/compirt/in_sample/double-difficulty/dd-monotone-linear-spline/) |
| `polynomial_compirt/` (gitignored) | Monotone Bernstein curves; parent of `hazard_double_difficulty/bernstein/` | [`in_sample/polynomial/`](../results/compirt/in_sample/polynomial/) |
| `test_additions/` (gitignored) | Decoupled buzz timing and position-varying neg calibration | [`in_sample/test_additions/`](../results/compirt/in_sample/test_additions/) |
| [`neg_test/`](neg_test/) | Five-fold neg and buzz-timing comparison of the curve families above | [`holdout/common/bad-experiments/`](../results/compirt/holdout/common/bad-experiments/) |
| [`frozen_skills/`](frozen_skills/), [`docs/`](docs/) | Timing-first frozen-skills models, their guide, and their research-log section | [`holdout/frozen-skills/`](../results/compirt/holdout/frozen-skills/) |
| [`simple_mirt/`](simple_mirt/) | Original pedagogical MIRT baseline and the plain-IRT comparator | — |
| [`compirt_eval/SCENARIO_C.md`](compirt_eval/SCENARIO_C.md), `compirt_eval/scenario_c_rosters/`, `scenario_c_model.py`, `run_scripts/common/run_scenario_c.py` | Paper Scenario C (C1–C4 roster generalization) | never run |
| [`run_scripts/`](run_scripts/) | Runners for TF-IDF, learned topics, the monotone spline holdout, embeddings, and Scenario C | — |
| [`analysis/buzz_accuracy_timing/`](analysis/buzz_accuracy_timing/report.md) | Player buzz accuracy versus buzz timing | beside the code |
| [`grace_analysis/`](grace_analysis/), `grace_data/` | Exploratory analysis of GRACE live-competition buzzes; `grace_data/` is its input | beside the code |
| `tests/` | Root-suite tests for archived code | — |

## Running archived code

Commands in the family READMEs use the original paths. From the repository
root, put `archive/` on the Python path for modules and add the `archive/`
prefix for files and shell scripts:

```bash
PYTHONPATH=archive:. .venv/bin/python -m tfidf.train_tfidf_pyramidal --help
PYTHONPATH=archive:. .venv/bin/python -B -m pytest -q archive/tests archive/tfidf/tests archive/topic \
  archive/polynomial_compirt/tests --ignore=archive/tests/test_scenario_c.py
```

Known breakage:

- The live `compirt_eval/` and `multidimensional/` packages shadow
  `compirt_eval.scenario_c_rosters`, `multidimensional.embedding_mirt`, and the
  `_tanhbias` modules. Those, and `tests/test_scenario_c.py`, run only after
  copying them back into the live tree.
- Repository-root paths found with `Path(__file__).parents[N]` or
  `dirname .../..` now stop inside `archive/`. `grace_analysis/` is unaffected
  because `grace_data/` moved with it.
- The shell runners source `run_scripts/common/lib/result_root.sh`, which has
  been deleted.
- Live modules that archived code imports have moved or been deleted:
  `compirt_eval.drop_robustness` (used by `simple_mirt/train_plain_irt.py` and
  `test_additions/`) is in
  `results/compirt/in_sample/common/drop-robustness/code/`;
  `compirt_eval.diagnostics.posterior_predictive` (used by `test_additions/`) is
  in `results/compirt/in_sample/multidim/multidim-all2024/code/`; and
  `run_scripts.common.lib.ablation` (used by `polynomial_compirt/run_sweep.py`
  and `run_scripts/topic/run_learned_topic_ablation.py`) exists only in git
  history.
- Held-out runs for these families went through
  `run_scripts/common/run_compirt_holdout.py`, which now accepts only
  `MODEL=baseline` or `MODEL=multidim` and no longer has `RUN_C1_C4`.
  `holdout/frozen_predict.py` refuses polynomial and linear-spline fits.
- Archived model code other than `test_additions/` now uses the normalized
  first-buzz law in `compirt_race.py`
  ([`docs/first-buzz-likelihood.md`](../docs/first-buzz-likelihood.md)). The
  saved topic, TF-IDF, linear-spline, and embedding runs predate it (their
  `summary.json` has no `first_buzz_likelihood`), so refits will not reproduce
  their numbers.
