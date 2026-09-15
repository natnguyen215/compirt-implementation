# CompIRT Tests

Shared pipeline tests live here; model-family tests live in each family's
`tests/` directory. `test_prediction.py` checks first-buzz expectations across
model families against known probabilities, including unequal rosters, different
question lengths, and excluded bounceback rows.

Run them with:

```bash
.venv/bin/python -B -m pytest -q tests
```

The root suite runs under pytest because it mixes `unittest.TestCase` classes
with bare `test_*` functions; `unittest discover` silently skips the latter.

Keep tests focused on required behavior: numerical results, data separation,
frozen parameters, and usable saved artifacts. Prefer positive output checks
and representative cases; parameterize shared setup. Avoid assertions about
absent obsolete names, empty output directories, or hard-coded CLI settings.
Extend related tests instead of adding boilerplate or a file for every helper.

The model families are TestCase-only and have separate discovery roots, so their
local fixtures and import conventions remain explicit:

```bash
.venv/bin/python -B -m unittest discover -s hazard_double_difficulty/tests -t . -v
```

The correctness studies keep their tests beside the code they check and, for
the same reason as the root suite, run under pytest:

```bash
.venv/bin/python -B -m pytest -q analysis/correctness
```

Run the complete repository check with:

```bash
.venv/bin/python -B run_scripts/common/check_repo.py
```

Suites for archived families stay under `archive/` and are not run by the checker.

Tests must use synthetic in-memory data or a temporary directory. They must not
run full training experiments or write files under `results/`.
