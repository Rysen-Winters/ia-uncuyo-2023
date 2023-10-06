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
for i in range(30):
    env = Enviroment(width,height,obstacle_percentage,target_pos)
    env.board[agents_position[0]][agents_position[1]] = False
    agent_bfs = BFSAgent(agents_position, env)
    agent_dfs = DFSAgent(agents_position, env)
    agent_lds = LDSAgent(agents_position, env, depth_allowed)
    agent_ucs = UCSAgent(agents_position, env)
    env.print_enviroment(agent_bfs)
    bfs_results = ["Agente BFS",agent_bfs.search()[1]]
    dfs_results = ["Agente DFS",agent_dfs.search()[1]]
    lds_results = ["Agente LDS",agent_lds.search()[1]]
    ucs_results = ["Agente UCS",agent_ucs.search()[1]]
    bfs_total.append(bfs_results)
    dfs_total.append(dfs_results)
    lds_total.append(lds_results)
    ucs_total.append(ucs_results)

nombre_archivo = "agent_results.csv"

with open(nombre_archivo, mode='w', newline='') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["Agente", "Nodos explorados"])
    escritor.writerows(bfs_total)
    escritor.writerows(dfs_total)
    escritor.writerows(lds_total)
    escritor.writerows(ucs_total)

print(f"Archivo {nombre_archivo} creado exitosamente.")