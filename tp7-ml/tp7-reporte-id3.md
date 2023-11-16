# UNCuyo - Inteligencia Artificial - 2023
## Trabajo Práctico 7 - Machine Learning

### Id3

## Resultados de la ejecución del código:

Este es el árbol devuelto por el algoritmo, cada nodo está representado por (padre, arco_padre, atributo). El valor de padre, es el valor de atributo para el padre del nodo, el valor de arco_padre es el valor que debe tomar el atributo del padre para llegar hasta este nodo, y atributo es el atributo que representa este nodo. En cada línea se representa cada nivel del árbol

(p:None, a:temp), 

(p:temp, p_arcv:mild, a:outlook), (p:temp, p_arcv:cool, a:humidity), (p:temp, p_arcv:hot, a:humidity), 

(p:outlook, p_arcv:overcast, a:yes), (p:outlook, p_arcv:sunny, a:humidity), (p:outlook, p_arcv:rainy, a:humidity), (p:humidity, p_arcv:normal, a:play), (p:humidity, p_arcv:high, a:outlook), (p:humidity, p_arcv:normal, a:yes), 

(p:humidity, p_arcv:high, a:no), (p:humidity, p_arcv:normal, a:yes), (p:humidity, p_arcv:high, a:windy), (p:humidity, p_arcv:normal, a:yes), (p:play, p_arcv:no, a:no), (p:play, p_arcv:yes, a:yes), (p:outlook, p_arcv:overcast, a:yes), (p:outlook, p_arcv:sunny, a:no), 

(p:windy, p_arcv:False, a:yes), (p:windy, p_arcv:True, a:no), 


## Investigación de las estrategias de árboles de decisión para valores reales

Los atributos contínuos e incluso los enteros como por ejemplo la Altura o Peso de una persona, tienen un conjunto de valores posibles infinitos. Preferiblemente antes que generar infinitas ramas para el árbol, el algoritmo de aprendizaje encuentra un punto de división que de la mayor ganancia de información. Por ejemplo, dado un nodo en el árbol, quizá pueda ser el caso que probar con Peso > 160 nos da la mayor información. Métodos eficientes existen para encontrar buenos valores de división: 

- Iniciar por ordenar los valores del atributo.
- Considerar solo los puntos de división que se encuentran entre dos ejemplos, viendolos de forma ordenada, que tienen clasificaciones diferentes, mientras seguimos los totales de ejemplos positivos y negativos en cada lado del punto de división.

La división de valores es la parte más costosa de las aplicaciones de los árboles de decisión.

Dos estrategias comúnes de elección de puntos de división son:

- División binaria:

En la división binaria, el árbol elige un umbral y divide los datos en dos grupos: aquellos cuyos valores son mayores que el umbral y aquellos cuyos valores son iguales o menores que el umbral. Esta estrategia se repite en cada nodo del árbol, dividiendo recursivamente los conjuntos de datos en subconjuntos más pequeños.

- Selección de umbrales:

En lugar de realizar una única división binaria en cada nodo, se pueden probar varios umbrales en busca del mejor. El árbol evalúa diferentes umbrales para cada atributo y selecciona el umbral que optimiza algún criterio de división, como la reducción de impureza (en el caso de la clasificación) o la reducción de la varianza (en el caso de la regresión).

Fuentes: 

- https://chat.openai.com
- Artificial Inteligence: a Modern Approach 3ra Edición, Cap. 18
