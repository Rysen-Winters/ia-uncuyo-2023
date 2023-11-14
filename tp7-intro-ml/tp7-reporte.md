# UNCuyo - Inteligencia Artificial I - 2023
## Trabajo Práctico 7 - Introducción - Machine Learning


### 1. For each of parts (a) through (d), indicate whether we would generally expect the performance of a flexible statistical learning method to be better or worse than an inflexible method. Justify your answer.

- (a) The sample size n is extremely large, and the number of predictors p is small.

La performance del modelo sería buena ya que el modelo puede adaptarse a la variabilidad de los observaciones y al estas tener una cantidad de variables predictoras pequeña esto lo hace aún mejor para el caso.  

- (b) The number of predictors p is extremely large, and the number of observations n is small.

La performance del modelo sería mala ya que no se tendrían las suficientes observaciones para aproximar con precisión la función. Además la cantidad de variables provocaría una peor 
precisión ya que si estas tienen grandes relaciones entre ellas, estas no se detectarían debido a la baja cantidad de observaciones.

- (c) The relationship between the predictors and response is highly non-linear.

El modelo es el adecuado para este caso y se adaptará increíblemente bien a los cambios de las respuestas y logrará "detectar" las relaciones entre las variables predictoras.

- (d) The variance of the error terms, i.e. σ2 = Var(ϵ), is extremely high.

El rendimiento del modelo sería malo, ya que la varianza del error irreducible sería extremadamente grande.

### 2. Explain whether each scenario is a classification or regression problem, and indicate whether we are most interested in inference or prediction. Finally, provide n and p.

- (a) We collect a set of data on the top 500 firms in the US. For each firm we record profit, number of employees, industry and the CEO salary. We are interested in understanding which factors affect CEO salary.

Es un problema de regresión, ya que nuestra variable resultante es un número, el salario del CEO. Además este es un problema donde estamos interesados en inferencia ya que queremos ver que relación hay entre las variables predictorias y la resultante. n = 500, p = 4.

- (b) We are considering launching a new product and wish to know whether it will be a success or a failure. We collect data on 20 similar products that were previously launched. For each product we have recorded whether it was a success or failure, price charged for the product, marketing budget, competition price, and ten other variables.

Este es un problema de clasificación ya que estamos buscando clasificar si un producto será exitoso o no. Estamos interesados en una predicción ya que buscamos determinar si un producto será exitoso o no según una serie de atributos. n = 20, p = 14.

- (c) We are interested in predicting the % change in the USD/Euro exchange rate in relation to the weekly changes in the world stock markets. Hence we collect weekly data for all of 2012. For each week we record the % change in the USD/Euro, the % change in the US market, the % change in the British market, and the % change in the German market.

El problema es de regresión ya que la variable que queremos predecir es cuantitativa. En este problema estamos interesados en predecir la información basado en las variables predictoras porque nos interesa saber el valor de una variable de respuesta a partir de las variables de entrada. n = 52, p = 4. 

### 5. What are the advantages and disadvantages of a very flexible (versus a less flexible) approach for regression or classification? Under what circumstances might a more flexible approach be preferred to a less flexible approach? When might a less flexible approach be preferred?

Un acercamiento muy flexible nos permite captar relaciones complejas entre las variables, lo que mejora la precisión y ajuste del modelo, tambien puede aprovechar las muestras grandes de datos, lo que redice el sesgo y la varianza del modelo, pero puede manejar datos de altas dimensiones donde podemos extraer características y hasta nuevos predictores. Pero tenemos las desventajas que puede requerir una capacidad de cómputo muy grande si tiene que estimar un número grande de parámetros, y la misma flexibilidad puede hacer que el modelo se sobreajuste y además corre riesgo de ser muy difícil de interpretar.

Por otro lado, un acercamiento menos flexible es más fácil y rapido de implementar, puede evitar el sobreajuste dependiendo de la función que se está aproximando y comúnmente resulta ser más interpretable que otros. Pero corremos riesgos de perder características, interacciones o relaciones importantes entre las variables predictoras reduciendo así la precisión del modelo. Puede no aprovechar las muestras de gran tamaño, aumentando el sesgo y la varianza. Y finalmente puede que no maneje correctamente los datos de grandes dimensiones llevando al requerimiento de selección de características y reducciónes de dimensiones.

En cuanto a la elección de un acercamiento, si los datos son complejos, el tamaño de la muestra es grande y la cantidad de características es suficiente para soportar un modelo complejo sin sobreajustar, y el número de variables predictoras es grande, entonces querremos usar un modelo más flexible. Sin embargo si los datos son simples, el tamaño de muestra es pequeño y los predictores son pocos, preferiremos usar un modelo menos flexible. 

### 6. Describe the differences between a parametric and a non-parametric statistical learning approach. What are the advantages of a parametric approach to regression or classification (as opposed to a non-parametric approach)? What are its disadvantages?

La principal diferencia entre un acercamiento paramétrico y no paramétrico es que en un enfoque paramétrico asumiremos que la función a aproximar tiene alguna forma y buscaremos los parametros que se requieran para cumplir esa forma. Mientras que el no paramétrico no supone ninguna forma y se vasa en un número variable de parametros que están sujetos al tamaño de los datos.

Un enfoque paramétrico nos puede servir por su simplicidad, el poder estadístico y precisión que se pueden conseguir cuando los supuestos son verdaderos y resulta también simple interpretarlos. En contraste con las ventajas, el acercamiento paramétrico puede ser más sensible a valores atípicos y perder características importantes de los datos y terminar infraajustando el modelo.

### 7. The table below provides a training data set containing six observations, three predictors, and one qualitative response variable.

|Observación|X1 |X2 |X3 |Y    |
|-----------|---|---|---|-----|
|1          |0  |3  |0  |Red  |
|2          |2  |0  |0  |Red  |
|3          |0  |1  |3  |Red  |
|4          |0  |1  |2  |Green|
|5          |-1 |0  |1  |Green|
|6          |1  |1  |1  |Red  |

**Suppose we wish to use this data set to make a prediction for Y when X1 = X2 = X3 = 0 using K-nearest neighbors**

- (a) Compute the Euclidean distance between each observation and the test point, X1 = X2 = X3 = 0.

  - distancia para la observación 1: 3
  - distancia para la observación 2: 2
  - distancia para la observación 3: 3,16
  - distancia para la observación 4: 2,24
  - distancia para la observación 5: 1,41
  - distancia para la observación 6: 1,73

- (b) What is our prediction with K = 1? Why?

Nuestra predicción con K = 1 es Red, porque la observación más cercana al punto de prueba es la número 2, que tiene la etiqueta Red. Esto se debe a que el método de los K vecinos más cercanos asigna la etiqueta de la clase mayoritaria entre las K observaciones más cercanas al punto de prueba.

- (c) What is our prediction with K = 3? Why?

Nuestra predicción con K = 3 es Red, porque las tres observaciones más cercanas al punto de prueba son las números 2, 5 y 6, que tienen dos etiquetas Red y una Green. Y ya que el método de los K vecinos más cercanos toma la etiqueta de la clase mayoritaria entre las K observaciones más cercanas al punto de prueba, se elije la etiqueta Red.

- (d) If the Bayes decision boundary in this problem is highly nonlinear, then would we expect the best value for K to be large or small? Why?

Si el límite de decisión de Bayes en este problema es altamente no lineal, entonces esperaríamos que el mejor valor para K sea pequeño, porque un valor pequeño de K permite que el modelo se adapte mejor a la forma no lineal de los datos. Un valor grande de K, por el contrario, haría que el modelo fuera más suave y lineal, lo que podría provocar un mal ajuste y una baja precisión.
