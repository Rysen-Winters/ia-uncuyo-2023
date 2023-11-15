# UNCuyo - Inteligencia Artificial I - 2023
## Trabajo Práctico 7 - Machine Learning

## Parte A

### Ejercicio 6:

Random Classifier:

|n = 6383  |Predicted True                |Predicted False          |                                             |
|----------|------------------------------|-------------------------|---------------------------------------------|
|Real True |369                           |381                      |Sensitivity=369/(369+381)=0.492              |
|Real False|2876                          |2757                     |Specificity=2757/(2876+2757)=0.489           |
|          |Precision=369/(369+2876)=0.113|NPV=2757/(2757+381)=0.878|Accuracy=(369+2757)/(369+2757+2876+381)=0.489|


Bigger Class Classifier:

|n = 6383  |Predicted True                |Predicted False          |                                             |
|----------|------------------------------|-------------------------|---------------------------------------------|
|Real True |0                             |750                      |Sensitivity=0/(0+750)=0                      |
|Real False|0                             |5633                     |Specificity=5633/(5633+0)=1.0                |
|          |Precision=0/(0+0)=NaN         |NPV=5633/(5633+750)=0.882|Accuracy=(0+5633)/(0+5633+0+750)=0.882       |