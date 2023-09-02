from agents import*
from enviroment import*

sizeX = 10
sizeY = 10
dirt_rate = 0.3
init_posX = random.randint(0,sizeX - 1)
init_posY = random.randint(0,sizeY - 1)
ttl = 1000
entorno = Enviroment(sizeX, sizeY, dirt_rate, init_posY, init_posY, ttl)
print(str(entorno))