# Research Log models: in-sample versus held-out metrics

Both samples use unweighted fold means, matching the Research Log main table. Each model has one fitted-training row and one frozen-held-out row.

| model | sample | accuracy | Neg F1 | lift | joint event LL | correctness LL | AUC | ECE | position MAE | first-buzzer top-1 | no-buzz error | final-decile mass |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `.` | in-sample | 0.784115 | 0.270023 | 0.016780 | 7.430461 | 0.479097 | 0.741427 | 0.037165 | 0.324755 | 0.396005 | 0.208716 | 0.033066 |
| `.` | held-out | 0.768330 | 0.217730 | 0.001339 | 7.617837 | 0.516634 | 0.660483 | 0.035030 | 0.327728 | 0.350968 | 0.208150 | 0.032263 |
