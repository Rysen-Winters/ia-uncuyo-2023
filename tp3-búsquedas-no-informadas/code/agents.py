from enviroment import Enviroment
import random

class BFSAgent:
    initial_position : (int, int)
    current_position : (int, int)
    board : Enviroment # El entorno en el que el agente va a limpiar

    def __init__(self, initial_position: (int, int), board:Enviroment):
        self.board = board
        if (board.is_obstacle(initial_position[0], initial_position[1])):
            print("Error: El agente ha sido reubicado a una posición que no esté obstaculizada. \n")
            misplaced = True
            while (misplaced):
                new_init_posX = random.randint(0, self.board.width-1)
                new_init_posY = random.randint(0, self.board.height-1)
                if (board.is_obstacle(new_init_posX, new_init_posY) == False):
                    self.initial_position = (new_init_posX, new_init_posY)
                    self.current_position = (new_init_posX, new_init_posY)
                    misplaced = False
        else:
            self.initial_position = initial_position
            self.current_position = initial_position

    def search(self, target_position : (int, int)):
        solution = []
        if (self.initial_position == target_position):
            solution.append(self.initial_position)
            return solution
        
        frontier = []
        frontier.append(self.initial_position)
        explored = []
    
    def idle(self) -> bool:
        print("El agente se encuentra inactivo")
        return True