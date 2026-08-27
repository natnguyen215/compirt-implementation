# Data splits

This directory contains the reference configuration refit on ACF 2023–25 data.
Its event population, no-buzz rate, and always-correct baseline differ from the
`year_2024` runs, so their metrics are not directly comparable.

| Folder | Split | Notes |
| --- | --- | --- |
| [`season-2023-25/`](season-2023-25/) | `base_split=all` (ACF 2023–25) | Same model as [`../reference-model/`](../reference-model/), with three times the data. The lower joint event LL (5.5353) does not establish a model improvement across populations. |
