from local_search_algorithms import *

N = 9
solucion, valor, states_explored = nqueens_hillclimbing(N)
print("Solución encontrada:", solucion)
print("Número de ataques:", valor)
print("Número de estados explorados:", states_explored)
