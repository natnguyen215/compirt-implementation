# Research Log models: in-sample versus held-out metrics

Both samples use unweighted fold means, matching the Research Log main table. Each model has one fitted-training row and one frozen-held-out row.

| model | sample | accuracy | Neg F1 | lift | joint event LL | correctness LL | AUC | ECE | position MAE | first-buzzer top-1 | no-buzz error | final-decile mass |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `.` | in-sample | 0.809894 | 0.468513 | 0.042558 | 6.548653 | 0.444923 | 0.810267 | 0.074991 | 0.172284 | 0.384083 | 0.064993 | 0.096939 |
| `.` | held-out | 0.771619 | 0.368444 | 0.004629 | 6.744418 | 0.502547 | 0.711492 | 0.067294 | 0.178267 | 0.340354 | 0.064398 | 0.094827 |
