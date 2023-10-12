from enviroment import*
from informed_agents import*

def test_agent(agent : Agent, agent_type : str, env: Enviroment):
    print("Agente ("+agent_type+"): " + str(agent.initial_position))
    print("Objetivo:" + str(agent.board.target_position))
    print(agent_type + ": Buscando...")
    results = agent.search()
    solution = results[0]
    cant_explored = results[1]
    cost = results[2]
    if (solution != []):
        print("La solución es: " + str(solution))
        print("El camino solución del agente ("+agent_type+") tiene longitud: " + str(solution.__len__()))
        print("El agente ("+agent_type+") exploró "+ str(cant_explored)+ " nodos.")
        print("El costo del camino encontrado por el agente es: " + str(cost))
        env.print_solution(agent.initial_position,solution)
    else:
        print("El agente ("+agent_type+") no encontró el camino.")
        print("El agente ("+agent_type+") exploró "+ str(cant_explored)+ " nodos.\n")

width = 100
height = 100
obstacle_percentage = 0.08
agents_position = (random.randint(0,width-1), random.randint(0,height-1))
target_pos = (random.randint(0, width-1), random.randint(0,height-1))
env = Enviroment(width,height,obstacle_percentage,target_pos)
agent_star = AstarAgent(agents_position, env)
print("El entorno es: ")
env.print_enviroment(agent_star)
test_agent(agent_star, "Agente A*", env)