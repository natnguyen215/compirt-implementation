# Research Log models: in-sample versus held-out metrics

Both samples use unweighted fold means, matching the Research Log main table. Each model has one fitted-training row and one frozen-held-out row.

| model | sample | accuracy | Neg F1 | lift | joint event LL | correctness LL | AUC | ECE | position MAE | first-buzzer top-1 | no-buzz error | final-decile mass |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `.` | in-sample | 0.855812 | 0.674079 | 0.088477 | 5.730020 | 0.337989 | 0.898072 | 0.059008 | 0.125385 | 0.477136 | 0.033617 | 0.179825 |
| `.` | held-out | 0.734504 | 0.462773 | -0.032486 | 6.459592 | 0.565126 | 0.722822 | 0.118483 | 0.135931 | 0.397445 | 0.033684 | 0.177649 |
