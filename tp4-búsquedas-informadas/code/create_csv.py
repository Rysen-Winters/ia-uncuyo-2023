from enviroment import*
from informed_agents import*
import csv

width = 100
height = 100
obstacle_percentage = 0.08
agents_position = (random.randint(0,width-1), random.randint(0,height-1))
target_pos = (random.randint(0, width-1), random.randint(0,height-1))
star_total = []
env_n = 0

for i in range(30):
    env = Enviroment(width,height,obstacle_percentage,target_pos)
    env.deobstaculize(agents_position)
    agent_star = AstarAgent(agents_position,env)
    env.print_enviroment(agent_star)
    result_star = agent_star.search()
    star_results = ["A*",result_star[1], env_n, True if (result_star[0] != []) else False]
    star_total.append(star_results)
    env_n += 1

nombre_archivo = "informed_agent_results.csv"

with open(nombre_archivo, mode='w', newline='') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["Agente", "Nodos explorados","Numero de enviroment", "Solución encontrada"])
    escritor.writerows(star_total)

print(f"Archivo {nombre_archivo} creado exitosamente.")