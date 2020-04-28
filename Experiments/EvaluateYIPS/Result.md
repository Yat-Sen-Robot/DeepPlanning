## Sample Classification

| Predictor | $\mbox{AP}$ | $\mbox{AP}_{\mbox{WFS}}$ | $\mbox{AP}_{\mbox{IOV.125}}$ | $\mbox{AP}_{\mbox{WFS}\mbox{&}\mbox{IOC.125}}$ |
| --------- | ----------- | ------------------------ | ---------------------------- | ---------------------------------------------- |
| vgg19v1   | 96.9        | 77.4                     | 93.3                         | 73.3                                           |
| vgg16     | 96.8        | 77.5                     | 93.5                         | 73.8                                           |
| vgg19     | **97.0**    | **78.5**                 | **93.7**                     | **75.0**                                       |
| res50P    | 96.5        | 74.4                     | 91.3                         | 69.0                                           |
| svg16     | 96.7        | 76.5                     | 93.4                         | 73.6                                           |
| svg16v1P  | *96.8*      | *76.6*                   | *92.7*                       | 72.7                                           |
| vgg19v2   | 96.9        | 77.4                     | 93.7                         | 74.3                                           |



| Predictor: res50P                       | 0.   | 0.125 | 0.25 | 0.375 | 0.5  | 0.625 | 0.750 | 0.875 | mAP  |
| --------------------------------------- | ---- | ----- | ---- | ----- | ---- | ----- | ----- | ----- | ---- |
| $\mbox{AP}_{\mbox{IOV.125}}$            | 75.1 | 91.3  | 94.6 | 95.8  | 96.3 | 96.4  | 96.5  | 96.5  | 92.8 |
| $\mbox{AP}_{\mbox{WFS}+\mbox{IOC.125}}$ | 50.6 | 69.0  | 72.4 | 73.7  | 74.1 | 74.3  | 74.4  | 74.4  | 70.4 |



| Predictor: svg16v1P                 | 0.   | 0.125 | 0.25 | 0.375 | 0.5  | 0.625 | 0.750 | 0.875 | mAP  |
| ----------------------------------- | ---- | ----- | ---- | ----- | ---- | ----- | ----- | ----- | ---- |
| $\mbox{AP}_{\mbox{IOV}}$            | 74.0 | 92.6  | 95.2 | 96.3  | 96.6 | 96.8  | 96.8  | 96.8  | 93.1 |
| $\mbox{AP}_{\mbox{WFS}+\mbox{IOV}}$ | 52.8 | 72.7  | 75.4 | 76.4  | 76.6 | 76.6  | 76.6  | 76.6  | 73.0 |



| Predictor: svg16                    | 0.   | 0.125 | 0.25 | 0.375 | 0.5  | 0.625 | 0.750 | 0.875 | mAP  |
| ----------------------------------- | ---- | ----- | ---- | ----- | ---- | ----- | ----- | ----- | ---- |
| $\mbox{AP}_{\mbox{IOV}}$            | 76.6 | 93.4  | 95.3 | 96.1  | 96.4 | 96.6  | 96.7  | 96.7  | 93.5 |
| $\mbox{AP}_{\mbox{WFS}+\mbox{IOV}}$ | 55.9 | 73.6  | 75.6 | 76.0  | 76.3 | 76.5  | 76.5  | 76.5  | 73.4 |



| Predictor: vgg19                    | 0.   | 0.125 | 0.25 | 0.375 | 0.5  | 0.625 | 0.750 | 0.875 | mAP  |
| ----------------------------------- | ---- | ----- | ---- | ----- | ---- | ----- | ----- | ----- | ---- |
| $\mbox{AP}_{\mbox{IOV}}$            | 75.1 | 93.7  | 95.6 | 96.4  | 96.9 | 97.0  | 97.0  | 97.0  | 93.6 |
| $\mbox{AP}_{\mbox{WFS}+\mbox{IOV}}$ | 55.5 | 75.0  | 77.5 | 78.2  | 78.5 | 78.5  | 78.5  | 78.5  | 75.0 |



| Predictor: vgg16                    | 0.   | 0.125 | 0.25 | 0.375 | 0.5  | 0.625 | 0.750 | 0.875 | mAP  |
| ----------------------------------- | ---- | ----- | ---- | ----- | ---- | ----- | ----- | ----- | ---- |
| $\mbox{AP}_{\mbox{IOV}}$            | 75.2 | 93.5  | 95.4 | 96.3  | 96.7 | 96.8  | 96.8  | 96.8  | 93.4 |
| $\mbox{AP}_{\mbox{WFS}+\mbox{IOV}}$ | 54.5 | 73.8  | 76.2 | 77.2  | 77.4 | 77.5  | 77.5  | 77.5  | 74.0 |



## Sequence Classification

Len: 1.0, Number: 1529/2741 = 0.557825611091
Len: 2.0, Number: 964/2741 = 0.351696461146
Len: 3.0, Number: 230/2741 = 0.0839109813937
Len: 4.0, Number: 18/2741 = 0.00656694636994

| Predictor | $\mbox{Acc}$-Max | $\mbox{Acc}_{\mbox{LOS1}}$-Max | $\mbox{Acc}_{\mbox{LOS2}}$-Max | $\mbox{Acc}_{\mbox{LOS3}}$-Max | $\mbox{Acc}_{\mbox{LOS4}}$-Max |
| --------- | ---------------- | ------------------------------ | ------------------------------ | ------------------------------ | ------------------------------ |
| vgg19v1   | 71.4             | 100.0                          | 72.5                           | 68.3                           | 66.7                           |
| vgg16     | 71.2             | 100.0                          | 68.0                           | 68.3                           | 72.2                           |
| vgg19     | **71.7**         | **100.0**                      | **73.0**                       | **64.3**                       | **77.8**                       |
| res50P    | 69.1             | 100.0                          | 74.6                           | 71.7                           | 72.2                           |
| svg16     | 69.8             | 100.0                          | 71.9                           | 73.6                           | 72.2                           |
| svg16v1P  | 70.2             | *100.0*                        | 706                            | 66.1                           | 77.8                           |
| vgg19v2   | 71.4             | *100*                          | 70.6                           | 69.6                           | 72.2                           |



| Predictor | $\mbox{Acc}$-Max​  | $\mbox{Acc}_{\mbox{LOS1}}$ | $\mbox{Acc}_{\mbox{LOS2}}$ | $\mbox{Acc}_{\mbox{LOS3}}$ | $\mbox{Acc}_{\mbox{LOS4}}$ |
| --------- | ----------------- | -------------------------- | -------------------------- | -------------------------- | -------------------------- |
| vgg19v1   | 71.4 / 0.5851     | 83.6                       | **68.2**                   | **9.1**                    | 0.0                        |
| vgg16     | 71.2 / 0.6311     | 86.8                       | 62.9                       | 7.8                        | 0.0                        |
| vgg19     | **71.7 / 0.7080** | **87.4**                   | 63.8                       | 5.6                        | 0.0                        |
| res50P    | 69.1 / 0.5769     | 82.2                       | 65.4                       | 2.6                        | 0.0                        |
| svg16     | 69.8 / 0.5878     | 85.0                       | 61.8                       | 7.4                        | 0.0                        |
| svg16v1P  | *70.2 / 0.5904*   | *84.3*                     | *64.2*                     | *6.5*                      | 0.0                        |
| vgg19v2   | 71.4 / 0.6569     | 86.8                       | 64.1                       | 5.2                        | 0.0                        |





| Predictor:vgg19 | $\mbox{Acc}^\mbox{max}$ | $\mbox{Acc}^1$ | $\mbox{Acc}^2$ | $\mbox{Acc}^3$ | $\mbox{Acc}^4$ |
| --------------- | ----------------------- | -------------- | -------------- | -------------- | -------------- |
| 0               | 47.8 / 0.429            | 58.8           | 41.3           | 5.2            | 0.0            |
| 0.125           | 67.7/ 0.691             | 83.0           | 59.8           | 4.8            | 0.0            |
| 0.25            | 70.1/ 0.691             | 84.8           | 63.7           | 5.2            | 0.0            |
| 0.375           | 71.2 / 0.691            | 86.0           | 64.7           | 5.7            | 0.0            |
| 0.5             | 71.5/0.708              | 87.1           | 63.8           | 5.7            | 0.0            |
| 0.625           | 71.7/0.708              | 87.4           | 63.8           | 5.7            | 0.0            |
| 0.75            | 71.7/0.708              | 87.4           | 63.8           | 5.7            | 0.0            |
| 0.825           | 71.7/0.708              | 87.4           | 63.8           | 5.7            | 0.0            |
| mAcc            | 67.9                    | 82.7           | 60.6           | 5.5            | 0              |



| Predictor:vgg16 | $\mbox{Acc}^\mbox{max}$ | $\mbox{Acc}^1$ | $\mbox{Acc}^2$ | $\mbox{Acc}^3$ | $\mbox{Acc}^4$ |
| --------------- | ----------------------- | -------------- | -------------- | -------------- | -------------- |
| 0               | 47.8 / 0.357            | 57.4           | 42.2           | 10.0           | 0.0            |
| 0.125           | 67.2/0.632              | 83.4           | 56.7           | 7.8            | 0.0            |
| 0.25            | 69.8/0.632              | 85.8           | 60.6           | 7.8            | 0.0            |
| 0.375           | 70.7/0.632              | 86.6           | 61.8           | 7.8            | 0.0            |
| 0.5             | 71.0/0.632              | 86.7           | 62.4           | 7.8            | 0.0            |
| 0.625           | 71.2/0.632              | 86.9           | 62.8           | 7.8            | 0.0            |
| 0.75            | 71.2/0.632              | 86.9           | 62.8           | 7.8            | 0.0            |
| 0.825           | 71.2/0.632              | 86.9           | 62.8           | 7.8            | 0.0            |
| mAcc            | 67.5                    | 82.6           | 59.0           | 8.0            | 0              |



| Predictor:res50p | $\mbox{Acc}^\mbox{max}$ | $\mbox{Acc}^1$ | $\mbox{Acc}^2$ | $\mbox{Acc}^3$ | $\mbox{Acc}^4$ |
| ---------------- | ----------------------- | -------------- | -------------- | -------------- | -------------- |
| 0                | 47.7/0.535              | 65.5           | 31.4           | 1.7            | 0.0            |
| 0.125            | 64.4/0.577              | 80.8           | 54.4           | 2.6            | 0.0            |
| 0.25             | 67.1/0.577              | 81.7           | 60.5           | 2.6            | 0.0            |
| 0.375            | 68.5                    | 82.4           | 63.5           | 2.6            | 0.0            |
| 0.5              | 68.9                    | 82.1           | 64.9           | 2.6            | 0.0            |
| 0.625            | 69.0                    | 82.2           | 65.2           | 2.6            | 0.0            |
| 0.75             | 69.1                    | 82.2           | 65.4           | 2.6            | 0.0            |
| 0.825            | 69.1                    | 82.2           | 65.4           | 2.6            | 0.0            |
| mAcc             | 65.5                    | 79.9           | 58.8           | 2.5            | 0              |



| Predictor:svg16p | $\mbox{Acc}^\mbox{max}$ | $\mbox{Acc}^1$ | $\mbox{Acc}^2$ | $\mbox{Acc}^3$ | $\mbox{Acc}^4$ |
| ---------------- | ----------------------- | -------------- | -------------- | -------------- | -------------- |
| 0                | 46.5/0.385              | 55.6           | 41.2           | 11.3           | 0.0            |
| 0.125            | 65.4/0.548              | 78.2           | 60.0           | 7.8            | 0.0            |
| 0.25             | 68.3/0.532              | 79.8           | 65.2           | 9.6            | 0.0            |
| 0.375            | 69.8/0.532              | 81.2           | 67.2           | 9.6            | 0.0            |
| 0.5              | 70.0                    | 81.4           | 67.5           | 9.6            | 0.0            |
| 0.625            | 70.1                    | 81.4           | 67.8           | 9.6            | 0.0            |
| 0.75             | 70.1                    | 81.5           | 67.8           | 9.6            | 0.0            |
| 0.825            | 70.1                    | 81.5           | 67.8           | 9.6            | 0.0            |
| mAcc             | 66.3                    | 77.6           | 63.1           | 9.6            | 0              |