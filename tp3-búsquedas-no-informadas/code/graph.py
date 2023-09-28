
class Graph:
    node_name_list = None
    edge_list = None
    addressed : bool
    # node_name_list lista de los nodos que conforman el grafo.
    # edge_list es una lista de los nodos que se ven desde un nodo y la correspondencia es directa con la lista nodes
    # addressed es el valor que dirá si el grafo es dirigido o no. 
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

    def __str__(self):
        out_string = "Graph:{\n- Nodes: " + str(self.node_name_list) + "\n- Edges:\n"
        if (self.addressed):
            for node in self.edge_list:
                out_string += "[Name: " + str(node.name) + ", Parent: " + str(node.parent) + ", Edges: " + str(node.edges) + "]\n"
            out_string += "}"
        return out_string
    
    def get_ady_list(self,node_name):
        for node in self.edge_list:
            if node.name == node_name:
                return node

    def add_node(self, parent_name, node_name, edges):
        if (self.addressed):
            self.node_name_list.append(node_name)
            parent = []
            if parent_name != None:
                parent.append(parent_name)
                for node in self.edge_list:
                    if node.name == parent_name:
                        node.edges.append(node_name)
            graph_node = GraphNode(node_name, edges, parent)
            self.edge_list.append(graph_node)
            for edge_name in edges:
                if not(edge_name in self.node_name_list):
                    self.node_name_list.append(edge_name)
                    new_node = GraphNode(edge_name, [], [node_name])
                    self.edge_list.append(new_node)

class GraphNode:
    name = None
    edges = None
    parent = None

    def __init__(self, node_name, edge_list, parent):
        self.name = node_name
        self.edges = edge_list
        self.parent = parent