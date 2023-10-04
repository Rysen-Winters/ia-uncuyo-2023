from enviroment import*
from agents import*

def test_agent(agent : Agent, agent_type : str, env: Enviroment):
    print("Agente ("+agent_type+"): " + str(agent.initial_position))
    print("Objetivo:" + str(agent.board.target_position))
    print(agent_type + ": Buscando...")
    solution = agent.search()
    if (solution != []):
        print("La solución es: " + str(solution))
        print("El camino solución del agente ("+agent_type+") tiene longitud: " + str(solution.__len__()))
        env.print_solution(agent.initial_position,solution)
    else:
        print("El agente ("+agent_type+") no encontró el camino.\n")

width = 10
height = 10
obstacle_percentage = 0.08
agents_position = (random.randint(0,width-1), random.randint(0,height-1))
target_pos = (random.randint(0, width-1), random.randint(0,height-1))
env = Enviroment(width,height,obstacle_percentage,target_pos)
depth_allowed = int((width*height)/5)
agent_bfs = BFSAgent(agents_position, env)
agent_dfs = DFSAgent(agents_position, env)
agent_lds = LDSAgent(agents_position, env, depth_allowed)
agent_ucs = UCSAgent(agents_position, env)
print("El entorno es: ")
env.print_enviroment(agent_bfs)
test_agent(agent_bfs, "BFS", env)
test_agent(agent_dfs, "DFS", env)
test_agent(agent_lds, "LDS", env)
test_agent(agent_ucs, "UCS", env)