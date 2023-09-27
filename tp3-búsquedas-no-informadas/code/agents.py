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

    def search(self):
        solution = []
        if (self.initial_position == self.board.target_position):
            solution.append(self.initial_position)
            return solution
        frontier = []
        print(self.initial_position)
        print(self.board.target_position)
        frontier.append(self.initial_position)
        explored = []
        searching = True
        while (searching):
            frontier_position = frontier.pop(frontier.__len__()-1)
            explored.append(frontier_position)
            child_states = self.board.get_frontier_states(frontier_position, explored)
            for child in child_states:
                print("Child: " + str(child))
                if child not in frontier:
                    if child == self.board.target_position:
                        print("Encontrado objetivo")
                        return child
                    frontier.append(child)
            if frontier == []:
                searching = False

        return (-1,-1)
        
    
    def idle(self) -> bool:
        print("El agente se encuentra inactivo")
        return True
    
class Graph:
    node_name_list = None
    edge_list = None
    addressed : bool
    # nodes lista de los nodos que conforman el grafo.
    # edges es una lista de los nodos que se ven desde un nodo y la correspondencia es directa con la lista nodes 
    def __init__(self, nodes, edges, addressed : bool):
            self.node_name_list = nodes
            self.edge_list = []
            self.addressed = addressed
            if (addressed):
                len_edges_list = edges.__len__()
                for i in range(0, nodes.__len__(), 1):
                    node_name = nodes[i]
                    if i < len_edges_list:
                        edge_list = edges[i]
                        new_node = GraphNode(node_name, edge_list, [])
                        self.edge_list.append(new_node)
                    else:
                        new_node = GraphNode(node_name, [], [])
                        self.edge_list.append(new_node)

                for node in self.edge_list:
                    for i in range(0,self.edge_list.__len__(),1):
                        if ((node.name in self.edge_list[i].edges) and not(node.name in node.parent)):
                            node.parent.append(self.edge_list[i].name)

            else:
                for node_name in nodes:
                    for edge_list in edges:
                        new_node = GraphNode(node_name, edge_list)
                        self.node_list.append(new_node)           

    def __str__(self):
        out_string = "Graph:{\n- Nodes: " + str(self.node_name_list) + "\n- Edges:\n"
        if (self.addressed):
            for node in self.edge_list:
                out_string += "[Name: " + str(node.name) + ", Parent: " + str(node.parent) + ", Edges: " + str(node.edges) + "]\n"
            out_string += "}"
        return out_string

class GraphNode:
    name = None
    edges = None
    parent = None

    def __init__(self, node_name, edge_list, parent):
        self.name = node_name
        self.edges = edge_list
        self.parent = parent