# UNCuyo - Inteligencia Artificial I - 2023
## Trabajo Práctico 7 - Machine Learning

## Parte B:

### Proceso de preprocesamiento:

- Del dataset de test se eliminaron las columnas id y ultima_modificacion
- Se dividió el 3% de los datos para entrenar al modelo y restante 97% para testearlo

### Resultados obtenidos sobre el conjunto de validación:

- Se obtuvo que la precisión del modelo es de: 0.883379098691649.
- Se mostró la siguiente información de probabilidades de pertenencia al probarlos sobre data_test:

|   |        0|          1|
|---|---------|-----------|
|  1|0.9898810| 0.01011905|
|  2|0.9887698| 0.01123016|
|  3|0.9874603| 0.01253968|
|  4|0.9785714| 0.02142857|
|  5|0.9585714| 0.04142857|
|  6|0.9698214| 0.03017857|

- Luego se tomaron estas pertenencias al grupo 1, que significa que la inclinacion es peligrosa:

|id| inclinacion_peligrosa|
|--|----------------------|
| 1|            0.01011905|
| 2|            0.01123016|
| 4|            0.01253968|
| 6|            0.02142857|
| 9|            0.04142857|
|13|            0.03017857|

### Kaggle.

- El puntaje obtenido en Kaggle es del: 0.69138

### Descripción del algoritmo:

- Lee el archivo "arbolado-mza-dataset.csv" para usar para entrenar y testear el modelo
- Lee el archivo "arbolado-mza-dataset-test.csv" para usar en el test final.
- Quita de los datos de entrenamiento las columnas id y ultima_modificacion.
- Separa el conjunto de entrenamiento en dos partes, una para entrenar que es del 3% del tamaño del conjunto, y otro para testear, que es el restante 97%
- Entrena un modelo con random forest generando 100 árboles de decisión con 4 parámetros elegidos al azar para cada uno.
- Se calculan las predicciones con el conjunto de testeo (el 97% restante que dividimos anteriormente).
- Se calcula la precisión del algoritmo.
- Se calculan las predicciones con el dataframe de testeo que cargamos al inicio del programa.
- Se cargan en un archivo para su entrega en Kaggle.
