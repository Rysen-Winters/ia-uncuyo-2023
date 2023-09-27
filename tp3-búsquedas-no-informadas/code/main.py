from enviroment import*
from agents import*
"""
sizeX = 10
sizeY = 10
obstacle_percentage = 0.08
target_pos = (random.randint(0, sizeX-1), random.randint(0,sizeY-1))
env = Enviroment(sizeX,sizeY,obstacle_percentage,target_pos)
agent = BFSAgent((random.randint(0,sizeX-1), random.randint(0,sizeY-1)), env)
print("Agente(X: " + str(agent.initial_position[0]) + ", Y: " + str(agent.initial_position[1]) + ")")
print("Objetivo(X: " + str(env.target_position[0]) + ", Y: " + str(env.target_position[1]) + ")")
env.print_enviroment(agent)
print("move up:", env.accept_action(agent.initial_position[0],agent.initial_position[1],"move up"))
print("move right:", env.accept_action(agent.initial_position[0],agent.initial_position[1],"move right"))
print("move down:", env.accept_action(agent.initial_position[0],agent.initial_position[1],"move down"))
print("move left:", env.accept_action(agent.initial_position[0],agent.initial_position[1],"move left"))

print("Buscando...")
print(agent.search())
"""

nodes = [(1,1),(0,1),(1,0),(2,1),(1,2),(0,2),(0,0)]
edge_list = [[(0,1),(1,0),(2,1),(1,2)],[(0,2),(0,0)]]
graph = Graph(nodes, edge_list, True)
print(graph)