from enviroment import Enviroment
import random

class SimpleReflexiveAgent:
    posX : int # Su posición en el eje X
    posY : int # Su posición en el eje Y
    board : Enviroment # El entorno en el que el agente va a limpiar

    def __init__(self, init_posX: int, init_posY: int, board:Enviroment):
        self.board = board
        if (board.is_obstacle(init_posX, init_posY)):
            print("Error: El agente ha sido reubicado a una posición que no esté obstaculizada. \n")
            misplaced = True
            while (misplaced):
                new_init_posX = random.randint(0, self.board.width-1)
                new_init_posY = random.randint(0, self.board.height-1)
                if (board.is_obstacle(new_init_posX, new_init_posY) == False):
                    self.posX = new_init_posX
                    self.posY = new_init_posY
                    misplaced = False
        else:
            self.posX = init_posX
            self.posY = init_posY

    def think(self) -> bool:
        while self.ttl:
            if self.board.is_dirty(self.posX, self.posY):
                self.clean()
            else:
                self.move()
        return self.idle()

    def clean(self) -> bool:
        if self.board.accept_action(self.posX, self.posY, "clean"):
            self.board.set_state(self.posX,self.posY,False)
            self.board.aug_cleanedcells()
            self.ttl -= 1
            self.actions_consumed += 1
        return True
    
    def move(self) -> bool:
        moving = True
        while (moving):
            if self.advancing:
                if self.descending:
                    if self.board.accept_action(self.posX,self.posY,"move right"):
                        self.posX += 1
                        moving = False
                    elif self.board.accept_action(self.posX,self.posY,"move down"):
                        self.posY += 1
                        self.advancing = False
                        moving = False
                    else:
                        self.advancing = False
                        self.descending = False
                else:
                    if self.board.accept_action(self.posX,self.posY,"move right"):
                        self.posX += 1
                        moving = False
                    elif self.board.accept_action(self.posX,self.posY,"move up"):
                        self.posY -= 1
                        moving = False
                        self.advancing = False
                    else:
                        self.advancing = False
                        self.descending = True                        
            else:
                if self.descending:
                    if self.board.accept_action(self.posX,self.posY,"move left"):
                        self.posX -= 1
                        moving = False
                    elif self.board.accept_action(self.posX,self.posY,"move down"):
                        self.posY += 1
                        self.advancing = True
                        moving = False
                    else:
                        self.advancing = True
                        self.descending = False
                else:
                    if self.board.accept_action(self.posX,self.posY,"move left"):
                        self.posX -= 1
                        moving = False
                    elif self.board.accept_action(self.posX,self.posY,"move up"):
                        self.posY -= 1
                        moving = False
                        self.advancing = True
                    else:
                        self.advancing = True
                        self.descending = True     
        self.ttl -= 1  
        self.actions_consumed += 1            
        return True
    
    def idle(self) -> bool:
        print("El agente se encuentra inactivo")
        return True
    
class RandomReflexiveAgent:
    posX : int # Su posición en el eje X
    posY : int # Su posición en el eje Y
    ttl : int # Indica la cantidad máxima de acciones que puede realizar el agente
    actions_consumed : int # La cantidad de acciones realizadas
    board : Enviroment # El entorno en el que el agente va a limpiar

    def __init__(self, init_posX: int, init_posY: int, ttl: int, board:Enviroment):
        self.posX = init_posX
        self.posY = init_posY
        self.ttl = ttl
        self.actions_consumed = 0
        self.board = board

    def think(self) -> bool:
        while self.ttl > 0:
            if self.board.is_dirty(self.posX, self.posY): 
                if random.randint(0,10) <= 8: # 80% de probabilidades de que limpie
                    self.clean()
                elif random.randint(0,1) == 0: # 50% de probabilidades de que no se mueva
                    self.move()
            else:
                if random.randint(0,1) == 0: # 50% de probabilidades de que no se mueva
                    self.move()
        return self.idle()

    def clean(self) -> bool:
        if self.board.accept_action(self.posX, self.posY, "clean"):
            self.board.set_state(self.posX,self.posY,False)
            self.board.aug_cleanedcells()
            self.ttl -= 1
            self.actions_consumed += 1
        return True
    
    def move(self) -> bool:
        actions = ["move right", "move left", "move up", "move down"]
        possible_movements = []
        for action in actions:
            if self.board.accept_action(self.posX,self.posY,action):
                possible_movements.append(action)
        move = possible_movements[random.randint(0,(len(possible_movements)-1))]
        if move == "move right":
            self.posX += 1
        elif move == "move left":
            self.posX -= 1
        elif move == "move down":
            self.posY += 1
        elif move == "move up":
            self.posY -= 1
        self.ttl -= 1  
        self.actions_consumed += 1             
        return True
    
    def idle(self) -> bool:
        print("El agente se encuentra inactivo")
        return True
    
class TeleportingRandomReflexiveAgent:
    posX : int # Su posición en el eje X
    posY : int # Su posición en el eje Y
    ttl : int # Indica la cantidad máxima de acciones que puede realizar el agente
    actions_consumed : int # La cantidad de acciones realizadas
    board : Enviroment # El entorno en el que el agente va a limpiar

    def __init__(self, init_posX: int, init_posY: int, ttl: int, board:Enviroment):
        self.posX = init_posX
        self.posY = init_posY
        self.ttl = ttl
        self.actions_consumed = 0
        self.board = board

    def think(self) -> bool:
        while self.ttl > 0:
            if self.board.is_dirty(self.posX, self.posY): 
                if random.randint(0,10) <= 8: # 80% de probabilidades de que limpie
                    self.clean()
                elif random.randint(0,1) == 0: # 50% de probabilidades de que no se mueva
                    self.move()
            else:
                if random.randint(0,1) == 0: # 50% de probabilidades de que no se mueva
                    self.move()
        return self.idle()

    def clean(self) -> bool:
        if self.board.accept_action(self.posX, self.posY, "clean"):
            self.board.set_state(self.posX,self.posY,False)
            self.board.aug_cleanedcells()
            self.ttl -= 1
            self.actions_consumed += 1
        return True
    
    def move(self) -> bool:
        self.posX = random.randint(0,(self.board.width-1))
        self.posY = random.randint(0,(self.board.height-1))
        self.ttl -= 1  
        self.actions_consumed += 1             
        return True
    
    def idle(self) -> bool:
        print("El agente se encuentra inactivo")
        return True