# Research Log models: in-sample versus held-out metrics

Both samples use unweighted fold means, matching the Research Log main table. Each model has one fitted-training row and one frozen-held-out row.

| model | sample | accuracy | Neg F1 | lift | joint event LL | correctness LL | AUC | ECE | position MAE | first-buzzer top-1 | no-buzz error | final-decile mass |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `.` | in-sample | 0.810907 | 0.514289 | 0.043572 | 6.073468 | 0.425029 | 0.818831 | 0.056585 | 0.127629 | 0.433022 | -0.005036 | 0.191641 |
| `.` | held-out | 0.765455 | 0.411095 | -0.001536 | 6.437505 | 0.505854 | 0.716635 | 0.070584 | 0.136436 | 0.379875 | -0.004869 | 0.189412 |
