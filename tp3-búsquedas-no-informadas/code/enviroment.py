from colorama import Fore, Style
import random
import multiprocessing

class Enviroment:
    width : int # El ancho del tablero
    height : int # La altura del tablero
    board = None # El tablero en que se va a mover el agente.
    obstacle_percentage : float # Un valor entre 0.01 y 1.0 que indica el porcentaje de la tabla que estará obstaculizada.
    target_position : (int, int) # La medida de performance.

    def __init__(self, sizeX: int, sizeY: int, obstacle_percentage: float, target_position : (int, int)):
        self.width = sizeX
        self.height = sizeY
        self.obstacle_percentage = obstacle_percentage
        self.target_position = target_position
        self.board = []
        obstacle_amount = int((sizeX*sizeY)*obstacle_percentage)
        obstacles_in_place = 0
        for i in range(0,sizeX,1):
            self.board.append([])
            for j in range(0,sizeY,1):
                self.board[i].append(False)

        while (obstacles_in_place < obstacle_amount):
            x = random.randint(0, sizeX-1)
            y = random.randint(0, sizeY-1)
            if ((self.board[x][y] == False) and ((x,y) != self.target_position)):
                self.board[x][y] = True
                obstacles_in_place += 1

    def print_enviroment(self, agent) -> str:
        out_string = ""
        total_cells = self.width*self.height
        obstaculed_cells = 0
        for y in range(0,self.height,1):
            out_string += "|"
            for x in range(0,self.width,1):
                #out_string += f"({x}, {y})" #
                if ((agent.initial_position[0] == x) and (agent.initial_position[1] == y)):
                    if (self.board[x][y] == False):
                        out_string += " A"
                    else:
                        print("Error: El agente se encuentra en una celda obstaculizada.\n")
                        return "\n"
                elif ((x, y) == self.target_position):
                    if (self.board[x][y] == False):
                        out_string += " T"
                    else:
                        print("Error: El objetivo se encuentra en una celda obstaculizada.\n")
                        return "\n"
                else:
                    if (self.board[x][y] == True):
                        out_string += " O"
                        obstaculed_cells += 1
                    else:
                        out_string += " C"
            out_string += " |\n"
        out_string = out_string.replace("A",f"{Fore.GREEN}{'A'}{Style.RESET_ALL}")
        out_string = out_string.replace("T",f"{Fore.GREEN}{'T'}{Style.RESET_ALL}")
        out_string = out_string.replace("C",f"{Fore.BLUE}{'C'}{Style.RESET_ALL}")
        out_string = out_string.replace("O",f"{Fore.RED}{'O'}{Style.RESET_ALL}")
        out_string += "Celdas: " + str(total_cells) + ", Celdas libres: " + str(total_cells-obstaculed_cells) + ", Celdas con obstáculos: " + str(obstaculed_cells) +"\n"
        print(out_string)
        return out_string
    
    def print_solution(self, agent_position, solution):
        matrix = [["0" for i in range(self.height)] for j in range(self.width)]
        for x in range(self.width):
            for y in range(self.height):
                if self.board[x][y] == False:
                    matrix[x][y] = "C"
                else:
                    matrix[x][y] = "O"
        for position in solution:
            matrix[position[0]][position[1]] = "P"
        matrix[agent_position[0]][agent_position[1]] = "A"
        matrix[self.target_position[0]][self.target_position[1]] = "T"
        out_string = ""
        for y in range(self.height):
            out_string += "|"
            for x in range(self.width):
                out_string += " " + matrix[x][y]
            out_string += "|\n"
        out_string = out_string.replace("A",f"{Fore.GREEN}{'A'}{Style.RESET_ALL}")
        out_string = out_string.replace("T",f"{Fore.GREEN}{'T'}{Style.RESET_ALL}")
        out_string = out_string.replace("C",f"{Fore.BLUE}{'C'}{Style.RESET_ALL}")
        out_string = out_string.replace("O",f"{Fore.RED}{'O'}{Style.RESET_ALL}")
        out_string = out_string.replace("P",f"{Fore.WHITE}{'P'}{Style.RESET_ALL}")
        print(out_string)
        return out_string
        
        
    
    def get_target(self) -> int:
        return self.target_position
    
    def get_frontier_states(self, agent_position : (int, int), explored_states):
        reachable_states = []
        if self.accept_action(agent_position[0], agent_position[1], "move up") and ((agent_position[0], agent_position[1] - 1) not in explored_states):
            reachable_states.append((agent_position[0], agent_position[1] - 1))
        if self.accept_action(agent_position[0], agent_position[1], "move down") and ((agent_position[0], agent_position[1] + 1) not in explored_states):
            reachable_states.append((agent_position[0], agent_position[1] + 1))
        if self.accept_action(agent_position[0], agent_position[1], "move left") and ((agent_position[0] - 1, agent_position[1]) not in explored_states):
            reachable_states.append((agent_position[0] - 1, agent_position[1]))
        if self.accept_action(agent_position[0], agent_position[1], "move right") and ((agent_position[0] + 1, agent_position[1]) not in explored_states):
            reachable_states.append((agent_position[0] + 1, agent_position[1]))
        return reachable_states

    def is_obstacle(self,posX: int,posY: int) -> bool:
        return self.board[posX][posY]

    def accept_action(self, posX: int, posY: int, action: str) -> bool:
        if action == "move right":
            if (0 <= posX < (self.width-1)):
                return not(self.is_obstacle(posX + 1, posY))
        elif action == "move left":
            if (0 < posX <= (self.width-1)):
                return not(self.is_obstacle(posX - 1, posY))
        elif action == "move up":
            if (0 < posY <= (self.height-1)):
                return not(self.is_obstacle(posX, posY - 1))
        elif action == "move down":
            if (0 <= posY < (self.height-1)):
                return not(self.is_obstacle(posX, posY + 1))
        return False