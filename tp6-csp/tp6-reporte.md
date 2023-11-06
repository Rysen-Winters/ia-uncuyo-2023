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
