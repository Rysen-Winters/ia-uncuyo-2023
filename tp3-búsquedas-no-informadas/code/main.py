from enviroment import*
from agents import*

sizeX = 10
sizeY = 10
obstacle_percentage = 0.08
agents_position = (random.randint(0,sizeX-1), random.randint(0,sizeY-1))
target_pos = (random.randint(0, sizeX-1), random.randint(0,sizeY-1))
depth_allowed = 25
env = Enviroment(sizeX,sizeY,obstacle_percentage,target_pos)
agent = BFSAgent(agents_position, env)
print("El entorno es: ")
env.print_enviroment(agent)
print("AgenteBFS: " + str(agent.initial_position))
print("Objetivo:" + str(agent.board.target_position))
print("BFS: Buscando...")
solution_bfs = agent.search()
print("La solución es: " + str(solution_bfs))
print("El camino solución del agente BFS tiene longitud: " + str(solution_bfs.__len__()))
env.print_solution(agent.initial_position,solution_bfs)
agent_dfs = DFSAgent(agents_position, env)
print("AgenteDFS: " + str(agent_dfs.initial_position))
print("Objetivo:" + str(agent_dfs.board.target_position))
print("DFS: Buscando...")
solution_dfs = agent_dfs.search()
print("La solución DFS es: " + str(solution_dfs))
print("El camino solución del agente DFS tiene longitud: " + str(solution_dfs.__len__()))
env.print_solution(agent_dfs.initial_position, solution_dfs)
agent_lds = LDSAgent(agents_position, env, depth_allowed)
print("AgenteLDS: " + str(agent_lds.initial_position))
print("Objetivo:" + str(agent_lds.board.target_position))
print("LDS: Buscando...")
solution_lds = agent_lds.search()
print("La solución LDS es: " + str(solution_lds))
print("El camino solución del agente LDS tiene longitud: " + str(solution_lds.__len__()))
env.print_solution(agent_lds.initial_position, solution_lds)