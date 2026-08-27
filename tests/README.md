# CompIRT Tests

All automated CompIRT tests belong in this directory.

Run them with:

```bash
.venv/bin/python -B -m pytest -q tests
```

The root suite runs under pytest because it mixes `unittest.TestCase` classes
with bare `test_*` functions; `unittest discover` silently skips the latter.

The model families are TestCase-only and have separate discovery roots, so their
local fixtures and import conventions remain explicit:

```bash
.venv/bin/python -B -m unittest discover -s tfidf/tests -t . -v
PYTHONPATH=.:topic/fixed .venv/bin/python -B -m unittest discover -s topic/fixed/tests -v
PYTHONPATH=.:topic/fixed:topic/learned .venv/bin/python -B -m unittest discover -s topic/learned/tests -v
PYTHONPATH=.:topic/fixed:topic/learned .venv/bin/python -B -m unittest topic.tfidf.tests.test_topic_tfidf -v
.venv/bin/python -B -m unittest discover -s multidimensional/embedding_mirt/tests -t . -v
.venv/bin/python -B -m unittest discover -s polynomial_compirt/tests -t . -v
.venv/bin/python -B -m unittest discover -s hazard_double_difficulty/tests -t . -v
```

Run the complete repository check with:

```bash
.venv/bin/python -B run_scripts/common/check_repo.py
```

Tests must use synthetic in-memory data or a temporary directory. They must not
run full training experiments or write files under `results/`.
