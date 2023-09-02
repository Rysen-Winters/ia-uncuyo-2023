from enviroment import Enviroment

class SimpleReflexiveAgent:
    posX : int
    posY : int
    advancing : bool
    ttl : int
    board : Enviroment

    def __init__(self, init_posX, init_posY, ttl, board:Enviroment):
        self.posX = init_posX
        self.posY = init_posY
        self.advancing = True
        self.ttl = ttl
        self.board = board

    def start(self) -> bool:
        while (self.ttl > 0):
            if self.board.get_state(self.posX, self.posY):
                if self.board.accept_action(self.posX, self.posY, "clean"):
                    self.clean() # Continuar desde acá 01-09-2023

    def clean(self) -> bool:
        self.board.set_state(self.posX,self.posY,False)
        self.board.aug_cleanedcells()
        return True