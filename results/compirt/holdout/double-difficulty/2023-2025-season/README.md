# 2023–25 season refit

This directory contains the reference configuration refit on ACF 2023–25 data.
Its event population, no-buzz rate, and always-correct baseline differ from the
`year_2024` runs, so their metrics are not directly comparable.

| Folder | Split | Notes |
| --- | --- | --- |
| [`season-2023-25/`](season-2023-25/) | `base_split=all` (ACF 2023–25) | Same model as [`dd-bernstein-332-simplex-locations-terminal`](../ablations/model-components/relevance-locations-terminal/dd-bernstein-332-simplex-locations-terminal/), with three times the data. Its joint event LL (5.5353) is measured on a different population from the 2024 runs. |
