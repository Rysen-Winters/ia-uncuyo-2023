from enviroment import Enviroment

class SimpleReflexiveAgent:
    posX : int
    posY : int
    advancing : bool
    descending : bool
    ttl : int
    board : Enviroment

    def __init__(self, init_posX: int, init_posY: int, ttl: int, board:Enviroment):
        self.posX = init_posX
        self.posY = init_posY
        self.advancing = True
        self.descending = True
        self.ttl = ttl
        self.board = board

    def think(self) -> bool:
        while (self.ttl > 0):
            if self.board.is_dirty(self.posX, self.posY):
                self.clean()
            else:
                self.move()
        return True

    def clean(self) -> bool:
        if self.board.accept_action(self.posX, self.posY, "clean"):
            self.board.set_state(self.posX,self.posY,False)
            self.board.aug_cleanedcells()
            self.ttl -= 1
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
        return True