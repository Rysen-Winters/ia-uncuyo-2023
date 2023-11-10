# UNCUYO - Inteligencia Artificial I.
## Trabajo Práctico 6 - Constraint Satisfaction Problems.

### 1. Describir en detalle una formulación CSP para el Sudoku

  - **Variables:** el conjunto de celdas vacías del tablero de Sudoku, que se pueden denotar como X[i,j], donde i y j son los índices de fila y columna respectivamente.

  - **Dominio:** el conjunto de valores posibles para cada variable es el conjunto D = {1, 2, 3, 4, 5, 6, 7, 8, 9}.

  - **Restricciones:** el conjunto de condiciones que deben cumplir las variables para que la solución sea válida, que en el caso del Sudoku son las siguientes:
    - Cada fila debe contener todos los números del 1 al 9 sin que se repitan.

    - Cada columna debe contener todos los números del 1 al 9 sin que se repitan tampoco.

    - Cada "cuadrante" de 3x3 debe contener todos los números del 1 al 9 sin repetir.

### 2. Utilizar el algoritmo AC-3 para demostrar que la arco consistencia puede detectar la inconsistencia de la asignación parcial {WA=red, V=blue} para el problema del colorar el mapa de Australia (Figura 5.1 AIMA 2da edición ).


Inicialmente tendríamos las variables y sus dominios parciales, debido a la asignación parcial, de la siguiente forma:

- Western Australia = {red}
- Northern Territory = {red, green, blue}
- South Australia = {red, green, blue}
- Queensland = {red, green, blue}
- New South Wales = {red, green, blue}
- Victoria = {blue}
- Tasmania = {red, green, blue}

Y tendríamos la siguiente cola de aristas:

- (SA, WA)
- (WA, SA)
- (SA, NT)
- (NT, SA)
- (SA, Q)
- (Q, SA)
- (SA, NSW)
- (NSW, SA)
- (SA, V)
- (V, SA)
- (WA, NT)
- (NT, WA)
- (NT, Q)
- (Q, NT)
- (Q, NSW)
- (NSW, Q)
- (NSW, V)
- (V, NSW)

**Siguiendo el algoritmo:**

**1:**

Tomamos el arco (SA, WA), se encuentra la inconsistencia SA = red WA = red y el dominio de SA se reduce a {green, blue}, y los arcos (WA, SA), (NT, SA), (Q, SA), (NSW, SA), (V, SA) no se agregan porque ya están en la cola.

Dominios:
- WA = {red}
- NT = {red, green, blue}
- Q = {red, green, blue}
- NSW = {red, green, blue}
- V = {blue}
- SA = {green, blue}
- T = {red, green, blue}

Aristas:
- (WA, SA)
- (SA, NT)
- (NT, SA)
- (SA, Q)
- (Q, SA)
- (SA, NSW)
- (NSW, SA)
- (SA, V)
- (V, SA)
- (WA, NT)
- (NT, WA)
- (NT, Q)
- (Q, NT)
- (Q, NSW)
- (NSW, Q)
- (NSW, V)
- (V, NSW)

**2:**

Tomamos el arco (WA, SA), no se encuentran inconsistencias, no se modifica la cola

Dominios:
- WA = {red}
- NT = {red, green, blue}
- Q = {red, green, blue}
- NSW = {red, green, blue}
- V = {blue}
- SA = {green, blue}
- T = {red, green, blue}

Aristas:
- (SA, NT)
- (NT, SA)
- (SA, Q)
- (Q, SA)
- (SA, NSW)
- (NSW, SA)
- (SA, V)
- (V, SA)
- (WA, NT)
- (NT, WA)
- (NT, Q)
- (Q, NT)
- (Q, NSW)
- (NSW, Q)
- (NSW, V)
- (V, NSW)

**3 a 8:**

No se encuentran inconsistencias, no se modifica la cola.

Dominios:
- WA = {red}
- NT = {red, green, blue}
- Q = {red, green, blue}
- NSW = {red, green, blue}
- V = {blue}
- SA = {green, blue}
- T = {red, green, blue}

Aristas:
- (SA, V)
- (V, SA)
- (WA, NT)
- (NT, WA)
- (NT, Q)
- (Q, NT)
- (Q, NSW)
- (NSW, Q)
- (NSW, V)
- (V, NSW)

**9:**

Tomamos el arco (SA, V), encontramos la inconsistencia SA = blue V = blue y el dominio de SA se reduce a {green}, se agregan los arcos (WA, SA), (NT, SA), (Q, SA), (NSW, SA) a la cola.

Dominios: 
- WA = {red}
- NT = {red, green, blue}
- Q = {red, green, blue}
- NSW = {red, green, blue}
- V = {blue}
- SA = {green}
- T = {red, green, blue}

Aristas:
- (V, SA)
- (WA, NT)
- (NT, WA)
- (NT, Q)
- (Q, NT)
- (Q, NSW)
- (NSW, Q)
- (NSW, V)
- (V, NSW)
- (WA, SA)
- (NT, SA)
- (Q, SA)
- (NSW, SA)

**10 y 11:**

No se encuentran inconsistencias, no se modifica la cola.

Dominios: 
- WA = {red}
- NT = {red, green, blue}
- Q = {red, green, blue}
- NSW = {red, green, blue}
- V = {blue}
- SA = {green}
- T = {red, green, blue}

Aristas:
- (NT, WA)
- (NT, Q)
- (Q, NT)
- (Q, NSW)
- (NSW, Q)
- (NSW, V)
- (V, NSW)
- (WA, SA)
- (NT, SA)
- (Q, SA)
- (NSW, SA)

**12:**

Tomamos el arco (NT, WA), se encuentra la inconsistencia NT = red WA = red, el dominio de NT se reduce a {green, blue}, se agregan los arcos: (SA, NT), (WA, NT)

Dominios:
- WA = {red}
- NT = {green, blue}
- Q = {red, green, blue}
- NSW = {red, green, blue}
- V = {blue}
- SA = {green}
- T = {red, green, blue}

Aristas:
- (NT, WA)
- (NT, Q)
- (Q, NT)
- (Q, NSW)
- (NSW, Q)
- (NSW, V)
- (V, NSW)
- (WA, SA)
- (NT, SA)
- (Q, SA)
- (NSW, SA)
- (SA, NT)
- (WA, NT)

**13 a 16:**

No se encuentran inconsistencias, no se modifica la cola.

Dominios:
- WA = {red}
- NT = {green, blue}
- Q = {red, green, blue}
- NSW = {red, green, blue}
- V = {blue}
- SA = {green}
- T = {red, green, blue}

Aristas:
- (NSW, V)
- (V, NSW)
- (WA, SA)
- (NT, SA)
- (Q, SA)
- (NSW, SA)
- (SA, NT)
- (WA, NT)

**17:**

Tomamos el arco (NSW, V), se encuentra la inconsistencia NSW = blue V = blue, el dominio de NSW se reduce a {red, green} y se agregan los arcos: (SA, NSW), (Q, NSW)

Dominios:
- WA = {red}
- NT = {green, blue}
- Q = {red, green, blue}
- NSW = {red, green}
- V = {blue}
- SA = {green}
- T = {red, green, blue}

Aristas:
- (V, NSW)
- (WA, SA)
- (NT, SA)
- (Q, SA)
- (NSW, SA)
- (SA, NT)
- (WA, NT)
- (SA, NSW)
- (Q, NSW)

**18 a 19:**

No se encuentran inconsistencias, no se modifica la cola.

Dominios:
- WA = {red}
- NT = {green, blue}
- Q = {red, green, blue}
- NSW = {red, green}
- V = {blue}
- SA = {green}
- T = {red, green, blue}

Aristas:
- (NT, SA)
- (Q, SA)
- (NSW, SA)
- (SA, NT)
- (WA, NT)
- (SA, NSW)
- (Q, NSW)

**20:**

Tomamos el arco (NT, SA), se encuentra la inconsistencia NT = green SA = green, el dominio de NT se reduce a {blue} y se agrega el arco: (Q, NT)

Dominios: 
- WA = {red}
- NT = {blue}
- Q = {red, green, blue}
- NSW = {red, green}
- V = {blue}
- SA = {green}
- T = {red, green, blue}

Aristas:
- (Q, SA)
- (NSW, SA)
- (SA, NT)
- (WA, NT)
- (SA, NSW)
- (Q, NSW)
- (Q, NT)

**21:**

Tomamos el arco (Q, SA), se encuentra la inconsistencia Q = green SA = green, el dominio de Q se reduce a {red, blue} y se agregan los arcos: (SA, Q), (NT, Q), (NSW, Q)

Dominios:
- WA = {red}
- NT = {blue}
- Q = {red, blue}
- NSW = {red, green}
- V = {blue}
- SA = {green}
- T = {red, green, blue}
 
Aristas:
- (NSW, SA)
- (SA, NT)
- (WA, NT)
- (SA, NSW)
- (Q, NSW)
- (Q, NT)
- (SA, Q)
- (NT, Q)
- (NSW, Q)

**22:**
Tomamos el arco (NSW, SA), se encuentra la inconsistencia NSW = green SA = green, el dominio de NSW se reduce a {red} y se agrega el arco: (V, NSW)

Dominios:
- WA = {red}
- NT = {blue}
- Q = {red, blue}
- NSW = {red}
- V = {blue}
- SA = {green}
- T = {red, green, blue}

Aristas:
- (SA, NT)
- (WA, NT)
- (SA, NSW)
- (Q, NSW)
- (Q, NT)
- (SA, Q)
- (NT, Q)
- (NSW, Q)
- (V, NSW)

**23 a 25:**

No se encuentran inconsistencias, no se modifica la cola.

Dominios:
- WA = {red}
- NT = {blue}
- Q = {red, blue}
- NSW = {red}
- V = {blue}
- SA = {green}
- T = {red, green, blue}

Aristas:
- (Q, NSW)
- (Q, NT)
- (SA, Q)
- (NT, Q)
- (NSW, Q)
- (V, NSW)

**26:**

Tomamos el arco (Q, NSW), se encuentra la inconsistencia Q = red NSW = red, el dominio de Q se reduce a {blue} y los arcos (SA, Q), (NT, Q), (NSW, Q) no se agregan porque ya están en la cola.

Dominios:
- WA = {red}
- NT = {blue}
- Q = {blue}
- NSW = {red}
- V = {blue}
- SA = {green}
- T = {red, green, blue}

Aristas:
- (Q, NT)
- (SA, Q)
- (NT, Q)
- (NSW, Q)
- (V, NSW)

**27:**
- Se toma el arco (Q, NT), se encuentra la inconsistencia Q = blue NT = blue, el dominio de Q se reduce a {} detectamos que la asignación parcial inicial es inconsistente.


### 3. Cuál es la complejidad en el peor caso cuando se ejecuta AC-3 en un árbol estructurado CSP. (i.e. Cuando el grafo de restricciones forma un árbol: cualquiera dos variables están relacionadas por a lo sumo un camino)

Como debemos verificar d posibles valores del dominio para cada par de variables conectadas por un arco, tendremos una complejidad de O(nd^2)

### 4. AC-3 coloca de nuevo en la cola todo arco (Xk, Xi) cuando cualquier valor es removido del dominio de Xi incluso si cada valor de Xk es consistente con los valores restantes de Xi. Supongamos que por cada arco (Xk,Xi) se puede llevar la cuenta del número de valores restantes de Xi que sean consistentes con cada valor de Xk. Explicar como actualizar ese número de manera eficiente y demostrar que la arco consistencia puede lograrse en un tiempo total O((n^2)(d^2))

Implementaría una matriz donde el elemento i,j de la matriz represente la cantidad de valores admitidos de la arista (Xi, Xj), inicialmente todos los valores se inicializan en el valor máximo de valores permitidos y según se van eliminando valores permitidos en una arista (Xi, Xj), se decrementa el valor de la posición i,j y si retrocedemos un paso en el proceso de asignación de valores aumentamos el valor en la posición i,j. Finalmente, ya que se recorren todos los pares posibles de variables y por cada par de variables probamos todos los valores posibles de los dominios para encontrar las asignaciones consistentes, la complejidad temporal es O((n^2)(d^2)).

### 5. Demostrar la correctitud del algoritmo CSP para árboles estructurados (sección 5.4, p.172 AIMA 2da edición). Para ello, demostrar:

**a. Que para un CSP cuyo grafo de restricciones es un árbol, 2-consistencia (consistencia de arco) implica n-consistencia (siendo n número total de variables)**

Demostremos por inducción, Supongamos que tenemos 2-consistencia, esto implica un caso base de n = 2.
La demostración es trivial ya que para el caso base, 2-consistencia y n-consistencia es lo mismo.

Caso inductivo n > 2 Sea X = {x1,x2,...,xn} el conjunto de variables, y sea C = (x1,x2,...,xn) el camino que los une en el árbol. Supongamos que hay una asignación consistente de n-1 variables, es decir, A = {x1 = v1, x2 = v2,..., xk-1 = vk-1}. Queremos mostrar que se puede extender A a xn. Para ello, consideramos el subconjunto de n-1 variables Y = {x2,x3,...,xn}, y el subcamino Q = (x2,x3,...,xn). Por hipótesis inductiva, sabemos que Q es 2-consistente, y por lo tanto se puede extender la asignación consistente de n-2 variables B = {x2 = v2, x3 = v3,..., xn-1 = vn-1} a xn. Es decir, existe un valor vn tal que {xn = vn} es consistente con B. Pero como P es 2-consistente, se tiene que {x1 = v1, xn = vn} es consistente. Por lo tanto, {xn = vn} es consistente con A, y se ha extendido la asignación de n-1 variables a la n-ésima variable.

**b. Argumentar por qué lo demostrado en a. es suficiente.**

La 2-consistencia garantiza que todas las restricciones del algoritmo se cumplan, ya que el algoritmo procesa las restricciones en un orden topológico, resolviéndolas de raíz a hojas. Por lo tanto, no es necesario alcanzar una mayor n-consistencia en este contexto, y la 2-consistencia es adecuada para encontrar una solución o reportar un fallo en el CSP.

