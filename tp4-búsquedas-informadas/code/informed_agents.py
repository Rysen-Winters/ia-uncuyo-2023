from enviroment import Enviroment
from graph import *
import random
import copy
import heapq

class Agent:
    initial_position : (int, int) # La posición inicial desde la que va a buscar.
    board : Enviroment # El entorno en el que el agente va a buscar.

    def __init__(self, initial_position: (int, int), board:Enviroment):
        initial_position = self.verify_initial_position(initial_position, board)
        self.board = board
        self.initial_position = initial_position

    def verify_initial_position(self, initial_position : (int, int), board : Enviroment) -> tuple[int, int]:
        if (board.is_obstacle(initial_position[0], initial_position[1])):
            print("Error: El agente ha sido reubicado a una posición que no esté obstaculizada. \n")
            misplaced = True
            while (misplaced):
                new_init_posX = random.randint(0, board.width-1)
                new_init_posY = random.randint(0, board.height-1)
                if (board.is_obstacle(new_init_posX, new_init_posY) == False):
                    new_initial_position = (new_init_posX, new_init_posY)
                    misplaced = False
            return new_initial_position
        else:
            return initial_position
        
    def search(self):
        print("El agente no sabe que hacer ya que no tiene una estrategia definida ya que esta es una clase abstracta conceptualmente. \n *Convulsiona y muere.")

class AstarAgent(Agent):

    def __init__(self, initial_position : (int, int), board : Enviroment):
        super().__init__(initial_position, board)



    def search(self) -> tuple[list, int]:
        solution = []
        frontier = []
        heapq.heappush(frontier, (0, self.initial_position))
        explored = []
        cost_so_far = {self.initial_position: 0}
        came_from = {self.initial_position: None}

        while frontier:
            _, current = heapq.heappop(frontier)

            if current == self.board.target_position:
                break

            for next in self.board.get_frontier_states(current, explored):
                new_cost = cost_so_far[current] + self.board.get_cost(current, next)
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + self.heuristic(next)
                    heapq.heappush(frontier, (priority, next))
                    came_from[next] = current

        current_node = self.board.target_position
        while current_node is not None:
            solution.append(current_node)
            current_node = came_from[current_node]

        solution.reverse()
        cant_explored = len(explored)
        return solution, cant_explored

    def heuristic(self, node):
        return 1
    
"""
class DFSAgent(Agent):

    def __init__(self, initial_position : (int, int), board : Enviroment):
        super().__init__(initial_position, board)

    def search(self) -> tuple[list, int]:
        solution = []
        frontier = []
        frontier.append(self.initial_position)
        explored = []
        if (self.initial_position == self.board.target_position):
            solution.append(self.initial_position)
            return solution
        searching = True
        graph_dfs = Graph([],[],True)
        parent = None
        while (searching):
            frontier_position = frontier.pop(frontier.__len__()-1)
            graph_dfs.add_node(parent, frontier_position, [])
            child_states = self.board.get_frontier_states(frontier_position, explored)
            parent = frontier_position
            for child in child_states:
                if not(child in frontier):
                    if child == self.board.target_position:
                        searching = False
                    else:
                        frontier.append(child)
                    graph_dfs.add_node(parent, child, [])
            explored.append(frontier_position)
            if frontier == []:
                searching = False
        generating_solution = True
        current_node = graph_dfs.get_ady_list(self.board.target_position)
        while (generating_solution):
            solution.append(current_node.name)
            if (current_node.parent != []):
                current_node = graph_dfs.get_ady_list(current_node.parent[0])
            else:
                generating_solution = False
        solution.reverse()
        cant_explored = explored.__len__()
        return solution, cant_explored
    
class LDSAgent(Agent):
    depth_allowed : int

    def __init__(self, initial_position : (int, int), board : Enviroment, depth):
        super().__init__(initial_position, board)
        self.depth_allowed = depth
    
    def search(self) -> tuple[list, int]:
        solution = []
        frontier = []
        frontier.append((self.initial_position, 0))
        explored = []
        if (self.initial_position == self.board.target_position):
            solution.append(self.initial_position)
            return solution
        searching = True
        graph_dfs = Graph([],[],True)
        parent = None
        while (searching):
            frontier_position, depth = frontier.pop(frontier.__len__()-1)
            if depth > self.depth_allowed:
                continue
            graph_dfs.add_node(parent, frontier_position, [])
            child_states = self.board.get_frontier_states(frontier_position, explored)
            parent = frontier_position
            for child in child_states:
                if not(child in frontier):
                    if child == self.board.target_position:
                        searching = False
                    else:
                        frontier.append((child, depth + 1))
                    graph_dfs.add_node(parent, child, [])
            explored.append(frontier_position)
            if frontier == []:
                searching = False
        generating_solution = True
        current_node = graph_dfs.get_ady_list(self.board.target_position)
        while (generating_solution):
            solution.append(current_node.name)
            if (current_node.parent != []):
                current_node = graph_dfs.get_ady_list(current_node.parent[0])
            else:
                generating_solution = False
        solution.reverse()
        cant_explored = explored.__len__()
        return solution, cant_explored



class UCSAgent(Agent):

    def __init__(self, initial_position : (int, int), board : Enviroment):
        super().__init__(initial_position, board)
    
    def search(self) -> tuple[list, int]:
        solution = []
        frontier = []
        heapq.heappush(frontier, (0, self.initial_position, 0))  # Añade el costo acumulado inicial de 0
        explored = {}
        if (self.initial_position == self.board.target_position):
            solution.append(self.initial_position)
            return solution
        searching = True
        graph_bfs = Graph([],[],True)
        parent = None
        while (searching):
            _, frontier_position, path_cost = heapq.heappop(frontier)  # Extrae el costo acumulado
            graph_bfs.add_node(parent, frontier_position, [])
            child_states = self.board.get_frontier_states(frontier_position, explored)
            parent = frontier_position
            for child in child_states:
                cost = 1  # Aquí debes calcular el costo real
                total_cost = path_cost + cost  # Calcula el costo acumulado
                if child not in explored or total_cost < explored[child]:
                    if child == self.board.target_position:
                        graph_bfs.add_node(parent, child, [])
                        searching = False
                    else:
                        heapq.heappush(frontier, (total_cost, child, total_cost))  # Añade el costo acumulado a la frontera
                    graph_bfs.add_node(parent, child, [])
                    explored[child] = total_cost
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
        cant_explored = explored.__len__()
        return solution, cant_explored
"""