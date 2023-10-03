from enviroment import Enviroment
import random
from graph import *

class BFSAgent:
    initial_position : (int, int)
    board : Enviroment # El entorno en el que el agente va a buscar.

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
    
class DFSAgent:
    initial_position : (int, int)
    board : Enviroment # El entorno en el que el agente va a buscar.

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
                        graph_dfs.add_node(parent, child, [])
                        searching = False
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
        return solution
        
    
    def idle(self) -> bool:
        print("El agente se encuentra inactivo")
        return True
    
class LDSAgent:
    initial_position : (int, int)
    board : Enviroment # El entorno en el que el agente va a buscar.
    depth_allowed : int

    def __init__(self, initial_position: (int, int), board:Enviroment, depth : int):
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
        self.depth_allowed = depth
        
    """
    def busqueda_profundidad_limitada(grafo, inicio, objetivo, limite):
        visitados = set()
        pila = [(inicio, 0)]

        while pila:
            (nodo, profundidad) = pila.pop()
            if profundidad > limite:
                continue
            if nodo not in visitados:
                visitados.add(nodo)
                if nodo == objetivo:
                    return True
                for vecino in grafo[nodo]:
                    pila.append((vecino, profundidad + 1))
        return False

    # Ejemplo de uso
    grafo = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    print(busqueda_profundidad_limitada(grafo, 'A', 'F', 3))  # Devuelve: True

    # implementación recursiva

    def Recursive-DLS(node, problem, limit):
        cutoff_occurred = False
        if Goal-Test(problem, State[node]):
            return node
        elif Depth[node] == limit:
            return cutoff
        else:
            for each successor in Expand(node, problem):
                result = Recursive-DLS(successor, problem, limit-1)
                if result == cutoff:
                    cutoff_occurred = True
                elif result != failure:
                    return result
            if cutoff_occurred:
                return cutoff
            else:
                return failure


    """
    def lds(self, graph_dfs, parent, frontier, explored, depth):
        if (depth < self.depth_allowed):
            frontier_position = frontier.pop(frontier.__len__()-1)
            graph_dfs.add_node(parent, frontier_position, [])
            child_states = self.board.get_frontier_states(frontier_position, explored)
            for child in child_states:
                if not(child in frontier):
                    if child == self.board.target_position:
                        graph_dfs.add_node(parent, child, [])
                        return True
                    graph_dfs.add_node(parent, child, [])
                    result = self.lds(graph_dfs, child, [child], explored, depth + 1)
                    if (result):
                        return True
            return False
        else:
            return False

    def search(self):
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
        depth = 0
        solution_found = False
        while (searching):
            frontier_position = frontier.pop(frontier.__len__()-1)
            graph_dfs.add_node(parent, frontier_position, [])
            child_states = self.board.get_frontier_states(frontier_position, explored)
            parent = frontier_position
            for child in child_states:
                if not(child in frontier):
                    if child == self.board.target_position:
                        graph_dfs.add_node(parent, child, [])
                        searching = False
                        solution_found = True
                    frontier.append(child)
                    graph_dfs.add_node(parent, child, [])
            depth += 1
            explored.append(frontier_position)
            
            if (frontier == []):
                searching = False
            if ((depth == self.depth_allowed) and (solution_found == False)):
                searching = False
                print("El Agente LDS se ha quedado sin rango de profundidad.\n")

        if (solution_found):        
            generating_solution = True
            current_node = graph_dfs.get_ady_list(self.board.target_position)
            while (generating_solution):
                solution.append(current_node.name)
                if (current_node.parent != []):
                    current_node = graph_dfs.get_ady_list(current_node.parent[0])
                else:
                    generating_solution = False
            solution.reverse()
        return solution
        
    
    def idle(self) -> bool:
        print("El agente se encuentra inactivo")
        return True

class UniformAgent:
    initial_position : (int, int)
    board : Enviroment # El entorno en el que el agente va a buscar.

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