# Research Log models: in-sample versus held-out metrics

Both samples use unweighted fold means, matching the Research Log main table. Each model has one fitted-training row and one frozen-held-out row.

| model | sample | accuracy | Neg F1 | lift | joint event LL | correctness LL | AUC | ECE | position MAE | first-buzzer top-1 | no-buzz error | final-decile mass |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `.` | in-sample | 0.680686 | 0.420073 | -0.086650 | 6.280054 | 0.608138 | 0.671653 | 0.198744 | 0.129757 | 0.422249 | 0.035885 | 0.144310 |
| `.` | held-out | 0.628580 | 0.380605 | -0.138411 | 6.765616 | 0.661202 | 0.616429 | 0.220678 | 0.138908 | 0.366702 | 0.036269 | 0.142022 |
