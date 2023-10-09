from enviroment import*
from agents import*
import csv

width = 100
height = 100
obstacle_percentage = 0.08
agents_position = (random.randint(0,width-1), random.randint(0,height-1))
target_pos = (random.randint(0, width-1), random.randint(0,height-1))
depth_allowed = int((width*height)/5)
bfs_total = []
dfs_total = []
lds_total = []
ucs_total = []
env_n = 0
for i in range(30):
    env = Enviroment(width,height,obstacle_percentage,target_pos)
    env.board[agents_position[0]][agents_position[1]] = False
    agent_bfs = BFSAgent(agents_position, env)
    agent_dfs = DFSAgent(agents_position, env)
    agent_lds = LDSAgent(agents_position, env, depth_allowed)
    agent_ucs = UCSAgent(agents_position, env)
    env.print_enviroment(agent_bfs)
    result_bfs = agent_bfs.search()
    result_dfs = agent_dfs.search()
    result_lds = agent_lds.search()
    result_ucs = agent_ucs.search()
    bfs_results = ["BFS",result_bfs[1], env_n, True if (result_bfs[0] != []) else False]
    dfs_results = ["DFS",result_dfs[1], env_n, True if (result_dfs[0] != []) else False]
    lds_results = ["LDS",result_lds[1], env_n, True if (result_lds[0] != []) else False]
    ucs_results = ["UCS",result_ucs[1], env_n, True if (result_ucs[0] != []) else False]
    bfs_total.append(bfs_results)
    dfs_total.append(dfs_results)
    lds_total.append(lds_results)
    ucs_total.append(ucs_results)
    env_n += 1

nombre_archivo = "agent_results.csv"

with open(nombre_archivo, mode='w', newline='') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["Agente", "Numero de enviroment","Nodos explorados", "Solución encontrada"])
    escritor.writerows(bfs_total)
    escritor.writerows(dfs_total)
    escritor.writerows(lds_total)
    escritor.writerows(ucs_total)

print(f"Archivo {nombre_archivo} creado exitosamente.")