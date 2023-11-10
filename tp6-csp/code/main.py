from csp import*

def test_algorithm(algorithm : str, n : int):

    solucion = [None] * n # Lista para almacenar la solución
    dominios = [list(range(n))] * n # Lista de listas para almacenar los dominios

    if algorithm == "n_queens_backtracking":
        results = n_queens_backtracking(n, 0, solucion)
    elif algorithm == "n_queens_forward_checking":
        results = n_queens_forward_checking(n, 0, solucion, dominios)

    if results is not None:
        solution = results[0]
        states_explored = results[1]
        print(f"\nLa solución encontrada en el algoritmo {algorithm} es: {solution} y se exploraron {states_explored} estados.\n")
    else:
        print("\nNo se encontró solución.\n")

n = 8
test_algorithm("n_queens_backtracking", n)
test_algorithm("n_queens_forward_checking", n)