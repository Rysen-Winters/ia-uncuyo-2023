from local_search_algorithms import *

def test_algorithm(algorithm, algorithm_name : str, queens : int):
    results = algorithm(queens)
    solution = results[0] 
    possible_atks = results[1] 
    states_explored = results[2]
    print("\n")
    print(f"Solución encontrada por {algorithm_name}:", solution)
    print(f"Número de posibles ataques de la solución:", possible_atks)
    print(f"Número de estados explorados por {algorithm_name}:", states_explored)
    print("\n")

N = 16
test_algorithm(nqueens_hillclimbing, "Hill climbing", N)
test_algorithm(nqueens_simulated_annealing, "Simulated Annealing", N)
test_algorithm(nqueens_genetic_algorithm, "Genetic Algorithm", N)