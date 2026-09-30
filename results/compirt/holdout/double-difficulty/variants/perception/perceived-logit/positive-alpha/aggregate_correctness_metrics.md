# Research Log models: in-sample versus held-out metrics

Both samples use unweighted fold means, matching the Research Log main table. Each model has one fitted-training row and one frozen-held-out row.

| model | sample | accuracy | Neg F1 | lift | joint event LL | correctness LL | AUC | ECE | position MAE | first-buzzer top-1 | no-buzz error | final-decile mass |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `.` | in-sample | 0.396744 | 0.399181 | -0.370592 | 6.437382 | 0.764628 | 0.628399 | 0.334871 | 0.129701 | 0.437494 | 0.036821 | 0.129145 |
| `.` | held-out | 0.375861 | 0.392111 | -0.391130 | 6.758884 | 0.787527 | 0.606510 | 0.345781 | 0.137620 | 0.391814 | 0.036482 | 0.127520 |
