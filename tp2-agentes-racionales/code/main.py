from enviroment import*
from agents import*

sizeX = 2
sizeY = 2
dirt_rate = 0.8
entorno = Enviroment(sizeX, sizeY, dirt_rate)
init_posX = 0 #random.randint(0,sizeX - 1)
init_posY = 0 #random.randint(0,sizeY - 1)
ttl = 10000
agente = SimpleReflexiveAgent(init_posX,init_posY,ttl,entorno)
entorno.print_enviroment(agente)
agente.think()
entorno.print_enviroment(agente)
print("-----------------Informe del agente-----------------")
#print("Posición del agente: x: " + str(agente.posX) + ", y: "+ str(agente.posY))
#print("Celdas visitadas: " + str(agente.cells_visited))
print("Acciones realizadas: " + str(agente.actions_consumed))
#print("Acciones restantes: " + str(agente.ttl))
print("Performance del agente: "+ str(entorno.get_performance()))