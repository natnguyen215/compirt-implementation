# Research Log models: in-sample versus held-out metrics

Both samples use unweighted fold means, matching the Research Log main table. Each model has one fitted-training row and one frozen-held-out row.

| model | sample | accuracy | Neg F1 | lift | joint event LL | correctness LL | AUC | ECE | position MAE | first-buzzer top-1 | no-buzz error | final-decile mass |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `.` | in-sample | 0.806299 | 0.498207 | 0.038964 | 6.148097 | 0.430863 | 0.812355 | 0.057210 | 0.130552 | 0.433970 | 0.045654 | 0.130964 |
| `.` | held-out | 0.762799 | 0.400738 | -0.004192 | 6.495917 | 0.509441 | 0.711382 | 0.072503 | 0.138891 | 0.380824 | 0.045312 | 0.129172 |
