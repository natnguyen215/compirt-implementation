# Research Log models: in-sample versus held-out metrics

Both samples use unweighted fold means, matching the Research Log main table. Each model has one fitted-training row and one frozen-held-out row.

| model | sample | accuracy | Neg F1 | lift | joint event LL | correctness LL | AUC | ECE | position MAE | first-buzzer top-1 | no-buzz error | final-decile mass |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `.` | in-sample | 0.767944 | 0.019759 | 0.000609 | 7.589886 | 0.562989 | 0.622808 | 0.089990 | 0.340038 | 0.400857 | 0.222538 | 0.029189 |
| `.` | held-out | 0.766490 | 0.016726 | -0.000501 | 7.777616 | 0.608011 | 0.548631 | 0.105813 | 0.341802 | 0.351546 | 0.222829 | 0.028632 |
