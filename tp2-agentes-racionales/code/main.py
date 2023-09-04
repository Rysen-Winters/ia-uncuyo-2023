from enviroment import*
from agents import*

sizeX = 50
sizeY = 50
dirt_rate = 0.3
entorno = Enviroment(sizeX, sizeY, dirt_rate)
init_posX = 0 #random.randint(0,sizeX - 1)
init_posY = 0 #random.randint(0,sizeY - 1)
ttl = 10000
agente = SimpleReflexiveAgent(init_posX,init_posY,ttl,entorno)
entorno.print_enviroment(agente)
agente.think()
entorno.print_enviroment(agente)
print("Posición del agente: x: " + str(agente.posX) + ", y: "+ str(agente.posY))
print("Performance del agente: "+ str(entorno.get_performance()))