from enviroment import*
from agents import*

sizeX = 10
sizeY = 10
obstacle_percentage = 0.08
agents_position = (random.randint(0,sizeX-1), random.randint(0,sizeY-1))
target_pos = (random.randint(0, sizeX-1), random.randint(0,sizeY-1))
env = Enviroment(sizeX,sizeY,obstacle_percentage,target_pos)
agent = BFSAgent(agents_position, env)
print("AgenteBFS: " + str(agent.initial_position))
print("Objetivo:" + str(agent.board.target_position))
env.print_enviroment(agent)
print("Buscando...")
solution_bfs = agent.search()
print("La solución es: " + str(solution_bfs))
env.print_solution(agent.initial_position,solution_bfs)
agent_dfs = DFSAgent(agents_position, env)
print("AgenteDFS: " + str(agent_dfs.initial_position))
print("DFS: Buscando...")
solution_dfs = agent_dfs.search()
print("La solución DFS es: " + str(solution_dfs))
env.print_solution(agent_dfs.initial_position, solution_dfs)