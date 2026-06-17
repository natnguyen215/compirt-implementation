# CompIRT Tests

All automated CompIRT tests belong in this directory.

Run them with:

```bash
.venv/bin/python -B -m unittest discover -s tests -v
```

Tests must use synthetic in-memory data or a temporary directory. They must not
run full training experiments or write files under `results/`.