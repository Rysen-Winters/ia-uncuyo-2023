import random
import math

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

def best_candidate(N,solution):
    lista = neighbours(N,solution)# Obtener la lista de neighbours de la solución  
    best_neighbour = lista[0] # Inicializar el mejor vecino y el mejor valor con el primero de la lista
    poss_atks = posible_attacks(N,best_neighbour)
    
    for i in range(1, len(lista)): # Para cada vecino de la lista, excepto el primero
        ataques_i = posible_attacks(N,lista[i]) # Calcular el número de posible_attacks del vecino

        if ataques_i < poss_atks:# Si el número de posible_attacks es menor que el mejor valor
            # Actualizar el mejor vecino y el mejor valor con el vecino actual
            best_neighbour = lista[i]
            poss_atks = ataques_i

    return best_neighbour, poss_atks

# Definir una función para implementar el algoritmo Hillclimbing
def nqueens_hillclimbing(N):
    solution = initialize(N) # Crear una solución inicial aleatoria
    possible_atk = posible_attacks(N,solution) # Calcular el número de posible_attacks de la solución inicial
    searching = True
    states_explored = 0
    possible_states = pow(N,N)
    h_history = []
    h_history.append(possible_atk)

    while (searching):
        neighbour, neigbour_poss_atks = best_candidate(N,solution)
        h_history.append(neigbour_poss_atks)
        states_explored += 1
       
        if neigbour_poss_atks < possible_atk:  # Si el número de posible_attacks del vecino es menor que el de la solución actual
            # Actualizar la solución y el valor con el vecino y su valor
            solution = neighbour[:]
            possible_atk = neigbour_poss_atks
        else:
            # Si no hay mejora, terminar el bucle y devolver la solución y el valor actuales
            searching = False

        if states_explored == possible_states:
            searching = False

    return solution, possible_atk, states_explored, h_history


# Algoritmo Simulated Annealing

def temperature(T, i): # Usa un esquema de enfriamiento exponencial
    return T * 0.95**i

def random_neighbour(N, solution):
    i = random.randint(0, N-1) # Elegir una columna al azar
    j = random.choice([k for k in range(N) if k != solution[i]]) # Elegir una row al azar, distinta de la actual
    copy = solution[:]
    copy[i] = j # Cambiar la posición de la reina en la columna i a la row j
    return copy

def nqueens_simulated_annealing(N):
    solution = initialize(N)
    h_history = []
    valor = posible_attacks(N,solution)
    h_history.append(valor)
    T = 1.4  # Inicializar la temperatura
    states_explored = 0

    while T > 1e-3: # Mientras la temperatura sea mayor que un umbral
        vecino = random_neighbour(N,solution)
        valor_vecino = posible_attacks(N,vecino)
        h_history.append(valor_vecino)
        states_explored += 1
        delta = valor_vecino - valor # Calcular la diferencia de posible_attacks entre el vecino y la solución actual
       
        if delta < 0 or random.random() < math.exp(-delta/T):  # Si el vecino es mejor que la solución actual, o si se cumple la condición de probabilidad del algoritmo
            # Actualizar la solución y el valor con el vecino y su valor
            solution = vecino[:]
            valor = valor_vecino

        T = temperature(T, 1) # Disminuir la temperatura
    
    return solution, valor, states_explored, h_history


# Algoritmo genético

def initialize_population(pop_size, N):
    population = []
    for _ in range(pop_size):
        solution = initialize(N)
        population.append(solution)
    return population

def fitness(solution):
    attacks = 0
    N = len(solution)
    attacks = posible_attacks(N,solution)
    return 1 / (attacks + 1)  # Invertir para convertir en función de aptitud

def select_parents(population, num_parents):
    parents = []
    population.sort(key=fitness,reverse=True)
    parents = population[:num_parents]
    return parents

def crossover(parent1, parent2):
    N = len(parent1)
    crossover_point = random.randint(1, N - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

def mutate(solution, mutation_rate):
    for i in range(len(solution)):
        if random.random() < mutation_rate:
            solution[i] = random.randint(0, len(solution) - 1)
    return solution

def nqueens_genetic_algorithm(N):
    pop_size = 100
    num_generations = 1000
    mutation_rate = 0.15
    population = initialize_population(pop_size, N)
    h_history = []
    explored_states = 100

    for person in population:
        h_history.append(posible_attacks(N,person))

    for generation in range(num_generations):
        population.sort(key=fitness, reverse=True)  # Ordenar por aptitud descendente
        if fitness(population[0]) == 1.0:  # Si se encuentra una solución perfecta, terminar
            return population[0], posible_attacks(N,population[0]), explored_states, h_history
        parents = select_parents(population, pop_size // 2)
        new_population = parents.copy()
        while len(new_population) < pop_size:
            parent1, parent2 = random.sample(parents, 2)
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate)
            explored_states += 1
            h_history.append(posible_attacks(N,child))
            new_population.append(child)
        population = new_population

    population.sort(key=fitness, reverse=True)
    pos_attacks = posible_attacks(N,population[0])
    return population[0], pos_attacks, explored_states, h_history