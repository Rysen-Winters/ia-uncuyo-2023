from enviroment import*
from agents import*

sizeX = 100
sizeY = 100
obstacle_percentage = 0.08
target_pos = (random.randint(0, sizeX-1), random.randint(0,sizeY-1))
env = Enviroment(sizeX,sizeY,obstacle_percentage,target_pos)
agent = BFSAgent((random.randint(0,sizeX-1), random.randint(0,sizeY-1)), env)
print("AgenteBFS: " + str(agent.initial_position))
print("Objetivo:" + str(agent.board.target_position))
env.print_enviroment(agent)
print("Buscando...")
solution_bfs = agent.search()
print("La solución es: " + str(solution_bfs))
env.print_solution(agent.initial_position,solution_bfs)