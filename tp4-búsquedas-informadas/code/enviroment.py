from colorama import Fore, Style
import random

class Enviroment:
    width : int # El ancho del tablero
    height : int # La altura del tablero
    board = None # El tablero en que se va a mover el agente.
    obstacle_percentage : float # Un valor entre 0.01 y 1.0 que indica el porcentaje de la tabla que estará obstaculizada.
    target_position : (int, int) # El name de la posición objetivo

    def __init__(self, sizeX: int, sizeY: int, obstacle_percentage: float, target_position : (int, int)):
        self.width = sizeX
        self.height = sizeY
        self.obstacle_percentage = obstacle_percentage
        self.target_position = target_position
        self.board = []
        obstacle_amount = int((sizeX*sizeY)*obstacle_percentage)
        obstacles_in_place = 0
        setting_costs = True

        for i in range(0,sizeX,1):
            self.board.append([])
            for j in range(0,sizeY,1):
                new_node = EnviromentNode((i,j), False)
                self.board[i].append(new_node)

        while (obstacles_in_place < obstacle_amount):
            x = random.randint(0, sizeX-1)
            y = random.randint(0, sizeY-1)
            if ((self.is_obstaculized((x,y)) == False) and ((x,y) != self.target_position)):
                self.board[x][y].obstaculize()
                obstacles_in_place += 1

        while (setting_costs):
            for x in range(sizeX):
                for y in range(sizeY):
                    self.set_costs(x,y)
            setting_costs = False
        print("Se creo un enviroment")

    def set_costs(self, x : int, y : int) -> bool:
        cost_list = [0,0,0,0]
        if self.accept_action(x,y,"move up"):
            cost_list[0] = random.randint(1,1)
        if self.accept_action(x,y,"move right"):
            cost_list[1] = random.randint(1,1)
        if self.accept_action(x,y,"move down"):
            cost_list[2] = random.randint(1,1)
        if self.accept_action(x,y,"move left"):
            cost_list[3] = random.randint(1,1)
        self.board[x][y].set_cost_list(cost_list)


    def get_target(self) -> int:
        return self.target_position
    
    def get_frontier_states(self, agent_position : (int, int)):
        reachable_states = []
        if self.accept_action(agent_position[0], agent_position[1], "move up"):
            reachable_states.append((agent_position[0], agent_position[1] - 1))
        if self.accept_action(agent_position[0], agent_position[1], "move down"):
            reachable_states.append((agent_position[0], agent_position[1] + 1))
        if self.accept_action(agent_position[0], agent_position[1], "move left"):
            reachable_states.append((agent_position[0] - 1, agent_position[1]))
        if self.accept_action(agent_position[0], agent_position[1], "move right"):
            reachable_states.append((agent_position[0] + 1, agent_position[1]))
        return reachable_states
    
    def get_cost(self, start_pos : (int,int), next_pos : (int,int)) -> int:
        move_x = next_pos[0] - start_pos[0]
        move_y = next_pos[1] - start_pos[1]
        vector = (move_x,move_y)
        if (vector == (0,-1)):
            return self.board[start_pos[0]][start_pos[1]].cost_list[0]
        elif (vector == (1,0)):
            return self.board[start_pos[0]][start_pos[1]].cost_list[1]
        elif (vector == (0,1)):
            return self.board[start_pos[0]][start_pos[1]].cost_list[2]
        elif (vector == (-1,0)):
            return self.board[start_pos[0]][start_pos[1]].cost_list[3]
        print("Error al obtener el costo.\n")
        return -1
    
    def get_path_cost(self, path : list) -> int:
        cost = 0
        for i in range(1,path.__len__()):
            current_pos = path[0]
            next_pos = path[1]
            cost += self.get_cost(current_pos, next_pos)
        return cost

    def is_obstaculized(self, position : (int,int)) -> bool:
        return self.board[position[0]][position[1]].obstaculized

    def print_enviroment(self, agent) -> str:
        out_string = ""
        total_cells = self.width*self.height
        obstaculed_cells = 0
        for y in range(0,self.height,1):
            out_string += "|"
            for x in range(0,self.width,1):
                #out_string += f"({x}, {y})" #
                if ((agent.initial_position[0] == x) and (agent.initial_position[1] == y)):
                    if (self.is_obstaculized((x,y)) == False):
                        out_string += " A"
                    else:
                        print("Error: El agente se encuentra en una celda obstaculizada.\n")
                        return "\n"
                elif ((x, y) == self.target_position):
                    if (self.is_obstaculized((x,y)) == False):
                        out_string += " T"
                    else:
                        print("Error: El objetivo se encuentra en una celda obstaculizada.\n")
                        return "\n"
                else:
                    if (self.is_obstaculized((x,y)) == True):
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
                if self.is_obstaculized((x,y)) == False:
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

    def accept_action(self, posX: int, posY: int, action: str) -> bool:
        if action == "move right":
            if (0 <= posX < (self.width-1)):
                return not(self.is_obstaculized((posX + 1, posY)))
        elif action == "move left":
            if (0 < posX <= (self.width-1)):
                return not(self.is_obstaculized((posX - 1, posY)))
        elif action == "move up":
            if (0 < posY <= (self.height-1)):
                return not(self.is_obstaculized((posX, posY - 1)))
        elif action == "move down":
            if (0 <= posY < (self.height-1)):
                return not(self.is_obstaculized((posX, posY + 1)))
        return False
    
    def deobstaculize(self, pos : (int,int)) -> bool:
        self.board[pos[0]][pos[1]].obstaculized = False
        self.set_costs(pos[0], pos[1])
        return True
    
class EnviromentNode:
    cost_list : list # Es una lista de los costos a sus nodos vecinos en el orden arriba, derecha, abajo, izquierda, los valores para vecinos no accesibles es 0. Se incializa siempre como [0,0,0,0]
    name : (int, int) # Es la posición que representa este nodo.
    obstaculized : bool # Si la posición está obstaculizada, si es asi, la lista de costos no será inicializada.

    def __init__(self, name : (int,int), obstacled : bool):
        self.name = name
        self.obstaculized = obstacled
        if not(obstacled):
           self.cost_list = [0,0,0,0]

    def set_cost_list(self, cost_list):
        self.cost_list = cost_list
        return True

    def obstaculize(self) -> bool:
        self.cost_list = None
        self.obstaculized = True
        return True