# Research Log models: in-sample versus held-out metrics

Both samples use unweighted fold means, matching the Research Log main table. Each model has one fitted-training row and one frozen-held-out row.

| model | sample | accuracy | Neg F1 | lift | joint event LL | correctness LL | AUC | ECE | position MAE | first-buzzer top-1 | no-buzz error | final-decile mass |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `.` | in-sample | 0.637266 | 0.411483 | -0.130069 | 6.246709 | 0.655321 | 0.650030 | 0.237859 | 0.128748 | 0.436307 | 0.037643 | 0.139734 |
| `.` | held-out | 0.585725 | 0.379898 | -0.181266 | 6.807457 | 0.704994 | 0.600866 | 0.258387 | 0.138301 | 0.375047 | 0.037590 | 0.136705 |
