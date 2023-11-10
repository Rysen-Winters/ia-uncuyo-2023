from csp import*
import csv
import time

queen_sizes = [4,8,10,12,15]
results_backtracking = []
results_fc = []
times_backtracking = []
times_fc = []
total_results = []
for n in queen_sizes:

    # Backtracking.

    bt_start = time.time_ns()
    bt_results = n_queens_backtracking(n, 0, [None]*n)
    bt_end = time.time_ns()
    results_backtracking.append(["Backtracking", n, bt_end - bt_start, bt_results[1]])

    # Forward Checking.
        
    fc_start = time.time_ns()
    fc_results = n_queens_forward_checking(n, 0, [None] * n, [list(range(n))] * n)
    fc_end = time.time_ns()
    results_fc.append(["Forward Checking", n, fc_end - fc_start, fc_results[1]])

total_results += results_backtracking + results_fc
nombre_archivo = "csp_results.csv"


with open(nombre_archivo, mode='w', newline='') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["Algoritmo", "Cantidad de reinas", "Tiempo de ejecucion","Numero de asignaciones exploradas"])
    escritor.writerows(total_results)



print(f"Archivo {nombre_archivo} creado exitosamente.")