from enviroment import Enviroment
import random
from graph import *

class BFSAgent:
    initial_position : (int, int)
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
                    misplaced = False
        else:
            self.initial_position = initial_position

    def search(self):
        solution = []
        frontier = []
        frontier.append(self.initial_position)
        explored = []
        if (self.initial_position == self.board.target_position):
            solution.append(self.initial_position)
            return solution
        searching = True
        graph_bfs = Graph([],[],True)
        parent = None
        while (searching):
            frontier_position = frontier.pop(frontier.__len__()-1)
            graph_bfs.add_node(parent, frontier_position, [])
            child_states = self.board.get_frontier_states(frontier_position, explored)
            parent = frontier_position
            for child in child_states:
                if not(child in frontier):
                    if child == self.board.target_position:
                        graph_bfs.add_node(parent, child, [])
                        searching = False
                    frontier.append(child)
                    graph_bfs.add_node(parent, child, [])
            explored.append(frontier_position)
            if frontier == []:
                searching = False
        
        generating_solution = True
        current_node = graph_bfs.get_ady_list(self.board.target_position)
        while (generating_solution):
            solution.append(current_node.name)
            if (current_node.parent != []):
                current_node = graph_bfs.get_ady_list(current_node.parent[0])
            else:
                generating_solution = False
        solution.reverse()
        return solution
        
    
    def idle(self) -> bool:
        print("El agente se encuentra inactivo")
        return True
    
class DFSAgent:
    initial_position : (int, int)
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
                    misplaced = False
        else:
            self.initial_position = initial_position

    def search(self):
        solution = []
        frontier = []
        frontier.append(self.initial_position)
        explored = []
        if (self.initial_position == self.board.target_position):
            solution.append(self.initial_position)
            return solution
        searching = True
        graph_bfs = Graph([],[],True)
        parent = None
        while (searching):
            frontier_position = frontier.pop(0)
            graph_bfs.add_node(parent, frontier_position, [])
            child_states = self.board.get_frontier_states(frontier_position, explored)
            parent = frontier_position
            for child in child_states:
                if not(child in frontier):
                    if child == self.board.target_position:
                        graph_bfs.add_node(parent, child, [])
                        searching = False
                    frontier.append(child)
                    graph_bfs.add_node(parent, child, [])
            explored.append(frontier_position)
            if frontier == []:
                searching = False
        
        generating_solution = True
        current_node = graph_bfs.get_ady_list(self.board.target_position)
        while (generating_solution):
            solution.append(current_node.name)
            if (current_node.parent != []):
                current_node = graph_bfs.get_ady_list(current_node.parent[0])
            else:
                generating_solution = False
        solution.reverse()
        return solution
        
    
    def idle(self) -> bool:
        print("El agente se encuentra inactivo")
        return True
    
class UniformAgent:
    initial_position : (int, int)
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
                    misplaced = False
        else:
            self.initial_position = initial_position

    def search(self):
        solution = []
        frontier = []
        frontier.append(self.initial_position)
        explored = []
        if (self.initial_position == self.board.target_position):
            solution.append(self.initial_position)
            return solution
        searching = True
        graph_bfs = Graph([],[],True)
        parent = None
        while (searching):
            frontier_position = frontier.pop(0)
            graph_bfs.add_node(parent, frontier_position, [])
            child_states = self.board.get_frontier_states(frontier_position, explored)
            parent = frontier_position
            for child in child_states:
                if not(child in frontier):
                    if child == self.board.target_position:
                        graph_bfs.add_node(parent, child, [])
                        searching = False
                    frontier.append(child)
                    graph_bfs.add_node(parent, child, [])
            explored.append(frontier_position)
            if frontier == []:
                searching = False
        
        generating_solution = True
        current_node = graph_bfs.get_ady_list(self.board.target_position)
        while (generating_solution):
            solution.append(current_node.name)
            if (current_node.parent != []):
                current_node = graph_bfs.get_ady_list(current_node.parent[0])
            else:
                generating_solution = False
        solution.reverse()
        return solution
        
    
    def idle(self) -> bool:
        print("El agente se encuentra inactivo")
        return True