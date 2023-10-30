from local_search_algorithms import*
import csv
import time

queen_sizes = [4,8,10,12,15]
results_hc = []
results_sa = []
results_ga = []
variability_hc = []
variability_sa = []
variability_ga = []
total_results = []
total_variability = []
for n in queen_sizes:
    for i in range(30):
        # Hill climbing
        hc_start = time.time()
        hc_solution = nqueens_hillclimbing(n)
        hc_end = time.time()
        results_hc.append(["Hill Climbing", n, (hc_end - hc_start), hc_solution[2], True if (hc_solution[1] == 0) else False])
        # Simulated Annealing
        sa_start = time.time()
        sa_solution = nqueens_simulated_annealing(n)
        sa_end = time.time()
        results_sa.append(["Simulated Annealing", n, (sa_end - sa_start), sa_solution[2], True if (sa_solution[1] == 0) else False])
        # Genetic Algorithm
        ga_start = time.time()
        ga_solution = nqueens_genetic_algorithm(n)
        ga_end = time.time()
        results_ga.append(["Genetic Algorithm", n, (ga_end - ga_start), ga_solution[2], True if (ga_solution[1] == 0) else False])
        if n == 15 and i == 0:
            for j in range(hc_solution[3].__len__()):
                variability_hc.append(["Hill Climbing", j, hc_solution[3][j]])

            for x in range(sa_solution[3].__len__()):
                variability_sa.append(["Simulated Annealing", x, sa_solution[3][x]])

            for k in range(ga_solution[3].__len__()):
                variability_ga.append(["Genetic Algorithm", k, ga_solution[3][k]])


total_results += results_hc + results_sa + results_ga
total_variability += variability_hc + variability_sa + variability_ga

nombre_archivo = "local_search_results.csv"
nombre_archivo2 = "local_search_variability.csv"

with open(nombre_archivo, mode='w', newline='') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["Algoritmo", "Cantidad de reinas", "Tiempo de ejecución","Numero de soluciones exploradas", "Solución encontrada"])
    escritor.writerows(total_results)

with open(nombre_archivo2, mode='w', newline='') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["Algoritmo","Numero de estado", "Valores de h"])
    escritor.writerows(total_variability)

print(f"Archivo {nombre_archivo} creado exitosamente.")