from agents import SimpleReflexiveAgent
from colorama import Fore, Style
import random

class Enviroment:
    width : int # El ancho del tablero
    height : int # La altura del tablero
    board = None # El tablero en que se va a mover el agente.
    dirt_rate : float # Un valor entre 0.0 y 1.0 que indica las posibilidades que tiene una celda de que esté sucia
    cleaned_cells : int # La medida de performance.
    agent = None # El agente que limpiará el entorno.

    def __init__(self, sizeX, sizeY, dirt_rate, init_posX, init_posY, ttl):
        self.width = sizeX
        self.height = sizeY
        self.dirt_rate = dirt_rate
        self.cleaned_cells = 0
        self.board = []
        for i in range(0,sizeX,1):
            self.board.append([])
            for j in range(0,sizeY,1):
                if (random.randint(1,10) <= (dirt_rate*10)):
                    self.board[i].append(True)
                else:
                    self.board[i].append(False)
        self.agent = SimpleReflexiveAgent(init_posX, init_posY, ttl, self)

    def __str__(self) -> str:
        out_string = ""
        total_cells = self.width*self.height
        dirty_cells = 0
        for i in range(0,self.width,1):
            for j in range(0,self.height,1):
                if ((self.agent.posX == i) and (self.agent.posY == j)):
                    if (self.board[i][j] == True):
                        out_string += "AD"
                        dirty_cells+=1
                    else:
                        out_string += "AC"
                else:
                    if (self.board[i][j] == True):
                        out_string += " D"
                        dirty_cells+=1
                    else:
                        out_string += " C"
            out_string += "\n"
        out_string = out_string.replace("A",f"{Fore.GREEN}{'A'}{Style.RESET_ALL}")
        out_string = out_string.replace("C",f"{Fore.BLUE}{'C'}{Style.RESET_ALL}")
        out_string = out_string.replace("D",f"{Fore.RED}{'D'}{Style.RESET_ALL}")
        out_string += "Celdas: " + str(total_cells) + ", Celdas Sucias: " + str(dirty_cells) + ", Celdas limpias: " + str(total_cells-dirty_cells) +"\n"
        return out_string

    def get_performance(self) -> int:
        return self.cleaned_cells
    
    def get_state(self, posX, posY) -> bool:
        return self.board[posX][posY]
    
    def set_state(self, posX, posY, state) -> bool:
        self.board[posX][posY] = state
        return True
    
    def aug_cleanedcells(self) -> bool:
        self.cleaned_cells += 1
        return True

    def accept_action(self,action,posX,posY) -> bool:
        if action=="clean":
            if self.is_dirty(posX,posY):
                self.cleaned_cells += 1
                return True
        elif action == "move right":
            if posX < 99:
                return True
        elif action == "move left":
            if posX > 0:
                return True
        elif action == "move up":
            if posY > 0:
                return True
        elif action == "move down":
            if posY < 99:
                return True
        return False

    def is_dirty(self,posX,posY) -> bool:
        if self.board[posX][posY] == True:
            return True
        else:
            return False