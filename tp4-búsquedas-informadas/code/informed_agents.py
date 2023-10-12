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
        if (board.is_obstaculized((initial_position[0], initial_position[1]))):
            print("Error: El agente ha sido reubicado a una posición que no esté obstaculizada. \n")
            misplaced = True
            while (misplaced):
                new_init_posX = random.randint(0, board.width-1)
                new_init_posY = random.randint(0, board.height-1)
                if (board.is_obstaculized((new_init_posX, new_init_posY)) == False):
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
 
    def search(self) -> tuple[list, int, int]:
        solution = []
        frontier = []
        heapq.heappush(frontier, (0, self.initial_position))
        explored = set()
        cost_so_far = {self.initial_position: 0}
        came_from = {self.initial_position: None}
        while frontier:
            _, current = heapq.heappop(frontier)
            if current == self.board.target_position:
                break
            for next in self.board.get_frontier_states(current):
                new_cost = cost_so_far[current] + self.board.get_cost(current, next)
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + self.heuristic(next)
                    heapq.heappush(frontier, (priority, next))
                    came_from[next] = current
            explored.add(current)
        current_node = self.board.target_position
        while current_node is not None:
            solution.append(current_node)
            current_node = came_from[current_node]
        solution.reverse()
        cant_explored = len(explored)
        path_cost = self.board.get_path_cost(solution)
        return solution, cant_explored, path_cost
    
    def heuristic(self, node : (int,int)):
        distance = ((node[0] - self.board.target_position[0])**2 + (node[1] - self.board.target_position[1])**2)**0.5
        return distance