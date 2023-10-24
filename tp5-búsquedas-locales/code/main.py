from local_search_algorithms import *

def test_algorithm(algorithm, algorithm_name : str, queens : int):
    solution, possible_atks, states_explored = algorithm(queens)
    print("\n")
    print(f"Solución encontrada por {algorithm_name}:", solution)
    print(f"Número de posibles ataques de la solución:", possible_atks)
    print(f"Número de estados explorados por {algorithm_name}:", states_explored)
    print("\n")

N = 8
test_algorithm(nqueens_hillclimbing, "Hill climbing", N)
test_algorithm(nqueens_simulated_annealing, "Simulated Annealing", N)