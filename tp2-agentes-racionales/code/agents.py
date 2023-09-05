from enviroment import Enviroment

class SimpleReflexiveAgent:
    posX : int # Su posición en el eje X
    posY : int # Su posición en el eje Y
    advancing : bool # Indica si el agente está avanzando o retrocediendo en una fila
    descending : bool # Indica si el agente está ascendiendo a descendiendo de filas
    ttl : int # Indica la cantidad máxima de acciones que puede realizar el agente
    actions_consumed : int # La cantidad de acciones realizadas
    cells_visited : int # La cantidad de celdas visitadas
    board : Enviroment # El entorno en el que el agente va a limpiar

    def __init__(self, init_posX: int, init_posY: int, ttl: int, board:Enviroment):
        self.posX = init_posX
        self.posY = init_posY
        self.advancing = True
        self.descending = True
        self.ttl = ttl
        self.actions_consumed = 0
        self.cells_visited = 0
        self.board = board

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
        self.cells_visited += 1              
        return True
    
    def idle(self) -> bool:
        print("El agente se encuentra inactivo")
        return True