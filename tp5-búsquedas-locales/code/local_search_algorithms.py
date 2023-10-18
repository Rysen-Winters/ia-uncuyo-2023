import random

def initialize(N):
    # Crear una lista vacía para almacenar la posición de las reinas
    solution = []
    # Para cada columna del tablero
    for i in range(N):
        # Elegir una row al azar entre 0 y N-1
        row = random.randint(0, N-1)
        # Añadir la row a la solución
        solution.append(row)
    # Devolver la solución
    return solution

# Definir una función para calcular el número de posible_attacks entre reinas
def posible_attacks(N,solution):
    # Inicializar el contador de posible_attacks a cero
    attacks = 0
    # Para cada par de reinas
    for i in range(N):
        for j in range(i+1, N):
            # Si están en la misma row o en la misma diagonal
            if solution[i] == solution[j] or abs(solution[i] - solution[j]) == abs(i - j):
                # Incrementar el contador de posible_attacks
                attacks += 1
    # Devolver el contador de posible_attacks
    return attacks

# Definir una función para generar los neighbours de una solución
def neighbours(N,solution):
  # Crear una lista vacía para almacenar los neighbours
    neighbours = []
  # Para cada columna del tablero
    for i in range(N):
        # Para cada row distinta de la actual
        for j in range(N):
            if j != solution[i]:
                # Crear una copia de la solución
                copia = solution[:]
                # Cambiar la posición de la reina en la columna i a la row j
                copia[i] = j
                # Añadir la copia a la lista de neighbours
                neighbours.append(copia)
    # Devolver la lista de neighbours
    return neighbours

# Definir una función para elegir el mejor vecino de una solución
def best_candidate(N,solution):
    # Obtener la lista de neighbours de la solución
    lista = neighbours(N,solution)
    # Inicializar el mejor vecino y el mejor valor con el primero de la lista
    mejor = lista[0]
    valor = posible_attacks(N,mejor)
    # Para cada vecino de la lista, excepto el primero
    for i in range(1, len(lista)):
        # Calcular el número de posible_attacks del vecino
        ataques_i = posible_attacks(N,lista[i])
        # Si el número de posible_attacks es menor que el mejor valor
        if ataques_i < valor:
        # Actualizar el mejor vecino y el mejor valor con el vecino actual
            mejor = lista[i]
            valor = ataques_i
    # Devolver el mejor vecino y el mejor valor
    return mejor, valor

# Definir una función para implementar el algoritmo Hillclimbing
def nqueens_hillclimbing(N):
    # Crear una solución inicial aleatoria
    solution = initialize(N)
    # Calcular el número de posible_attacks de la solución inicial
    valor = posible_attacks(N,solution)
    # Mientras haya posibilidad de mejora
    searching = True
    states_explored = 0
    while (searching):
        # Elegir el mejor vecino de la solución actual
        vecino, valor_vecino = best_candidate(N,solution)
        states_explored += 1
        # Si el número de posible_attacks del vecino es menor que el de la solución actual
        if valor_vecino < valor:
            # Actualizar la solución y el valor con el vecino y su valor
            solution = vecino[:]
            valor = valor_vecino
        else:
            # Si no hay mejora, terminar el bucle y devolver la solución y el valor actuales
            searching = False
    return solution, valor, states_explored