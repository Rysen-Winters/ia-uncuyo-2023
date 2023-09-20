from enviroment import*
from agents import*

sizeX = 50
sizeY = 50
dirt_rate = 0.8
print("entorno de "+str(sizeX) + "x" + str(sizeY))
print("cantidad de celdas: "+ str(sizeX*sizeY))
print("dirt_rate: " + str(dirt_rate))
entorno = Enviroment(sizeX, sizeY, dirt_rate)
init_posX = random.randint(0,sizeX - 1)
init_posY = random.randint(0,sizeY - 1)
ttl = 2500
agente_random = RandomReflexiveAgent(init_posX,init_posY,ttl,entorno)
entorno.print_enviroment(agente_random)
agente_random.think()
entorno.print_enviroment(agente_random)
print("Informe del agente_random")
print("Posición del agente_random: x: " + str(agente_random.posX) + ", y: "+ str(agente_random.posY))
print("Acciones realizadas: " + str(agente_random.actions_consumed))
print("Acciones restantes: " + str(agente_random.ttl))
print("Performance del agente_random: "+ str(entorno.get_performance()))
print("Fin iteración: --------------------------------------------")

entorno2 = Enviroment(sizeX, sizeY, dirt_rate)
init_posX = random.randint(0,sizeX - 1)
init_posY = random.randint(0,sizeY - 1)
agente_teleport = TeleportingRandomReflexiveAgent(init_posX,init_posY,ttl,entorno2)
entorno2.print_enviroment(agente_teleport)
agente_teleport.think()
entorno2.print_enviroment(agente_teleport)
print("Informe del agente_teleport")
print("Posición del agente_random: x: " + str(agente_teleport.posX) + ", y: "+ str(agente_teleport.posY))
print("Acciones realizadas: " + str(agente_teleport.actions_consumed))
print("Acciones restantes: " + str(agente_teleport.ttl))
print("Performance del agente: "+ str(entorno2.get_performance()))
print("Fin iteración: --------------------------------------------")