from colorama import Fore, Style
import random

class Enviroment:
    width : int # El ancho del tablero
    height : int # La altura del tablero
    board = None # El tablero en que se va a mover el agente.
    obstacle_porcentage : float # Un valor entre 0.01 y 1.0 que indica el porcentaje de la tabla que estará obstaculizada.
    cleaned_cells : int # La medida de performance.

    def __init__(self, sizeX: int, sizeY: int, obstacle_porcentage: float):
        self.width = sizeX
        self.height = sizeY
        self.obstacle_porcentage = obstacle_porcentage
        self.cleaned_cells = 0
        self.board = []
        obstacle_amount = int((sizeX*sizeY)*obstacle_porcentage)
        for i in range(0,sizeX,1):
            self.board.append([])
            for j in range(0,sizeY,1):
                if (random.randint(1,100) <= (dirt_rate*10)):
                    self.board[i].append(True)
                else:
                    self.board[i].append(False)

    def print_enviroment(self, agent) -> str:
        out_string = ""
        total_cells = self.width*self.height
        dirty_cells = 0
        for i in range(0,self.width,1):
            for j in range(0,self.height,1):
                if ((agent.posX == j) and (agent.posY == i)):
                    if (self.board[j][i] == True):
                        out_string += "AD"
                        dirty_cells+=1
                    else:
                        out_string += "AC"
                else:
                    if (self.board[j][i] == True):
                        out_string += " D"
                        dirty_cells+=1
                    else:
                        out_string += " C"
            out_string += "\n"
        out_string = out_string.replace("A",f"{Fore.GREEN}{'A'}{Style.RESET_ALL}")
        out_string = out_string.replace("C",f"{Fore.BLUE}{'C'}{Style.RESET_ALL}")
        out_string = out_string.replace("D",f"{Fore.RED}{'D'}{Style.RESET_ALL}")
        out_string += "Celdas: " + str(total_cells) + ", Celdas Sucias: " + str(dirty_cells) + ", Celdas limpias: " + str(total_cells-dirty_cells) +"\n"
        print(out_string)
        return out_string

    def get_performance(self) -> int:
        return self.cleaned_cells
    
    def set_state(self, posX: int, posY: int, state: bool) -> bool:
        self.board[posX][posY] = state
        return True
    
    def is_obstacle(self,posX: int,posY: int) -> bool:
        return self.board[posX][posY]
    
    def aug_cleanedcells(self) -> bool:
        self.cleaned_cells += 1
        return True

    def accept_action(self, posX: int, posY: int, action: str) -> bool:
        if action == "move right":
            if posX < (self.width-1):
                return True
        elif action == "move left":
            if posX > 0:
                return True
        elif action == "move up":
            if posY > 0:
                return True
        elif action == "move down":
            if posY < (self.height-1):
                return True
        return False