import pandas as pd
import numpy as np
from collections import deque

class Tree:
    root = None

    def __init__(self, root):
        self.root = root

    def print_tree(self):
        print("\n")
        queue = deque([(self.root, 0)])
        current_level = 0

        while queue:
            node, level = queue.popleft()

            if level != current_level:
                print()
                current_level = level

            if node.parent is not None:
                print(f'(p:{node.parent.attribute}, p_arcv:{node.parent_arcv}, a:{node.attribute})', end=', ')
            else:
                print(f'(p:None, a:{node.attribute})', end=', ')

            for child in node.children:
                queue.append((child, level + 1))

        print("\n")

            
    

class TreeNode:
    root : bool # Si es el nodo raiz.
    attribute : str # El atributo que representa el nodo.
    parent = None # Una referencia a su nodo padre.
    parent_arc : str # El valor del padre por el cual se llega a este nodo, parent arc value.
    children : list # La lista de hijos del nodo.

    def __init__(self, is_root : bool, attribute : str, parent, parent_arcv, children):
        self.root = is_root
        self.attribute = attribute
        self.parent = parent
        self.parent_arcv = parent_arcv
        self.children = children


def decision_tree_learning(examples : pd.DataFrame, attributes, parent_examples, parent, parent_arcv):
    if examples.empty:

        value = plurality_value(parent_examples)
        tree_node = TreeNode(False,value,parent,parent_arcv,[])
        return tree_node
    
    elif all_same_class(examples):

        tree_node = TreeNode(False,examples.iloc[0][-1],parent,parent_arcv,[])
        return tree_node
    
    elif not attributes:

        value = plurality_value(examples)
        tree_node = TreeNode(False,value,parent,parent_arcv,[])
        return tree_node
    
    else:

        A = choose_best_attribute(attributes, examples)

        if parent == None:
            tree_node = TreeNode(True,A,parent,None,[])
        else:
            tree_node = TreeNode(False,A,parent,parent_arcv,[])
        
        for value in get_values(A, examples):
            new_examples = examples.loc[examples[A] == value]
            subtree_node = decision_tree_learning(new_examples, [attr for attr in attributes if attr != A], examples, tree_node, value)
            tree_node.children.append(subtree_node)

        if tree_node.root:
            tree = Tree(tree_node)
            return tree
        else:
            return tree_node

def plurality_value(examples : pd.DataFrame):
    classes = []
    for i in range(examples.shape[0]):
        classes.append(examples.iloc[i][-1])
    return max(set(classes), key=classes.count)

def all_same_class(examples):
    classes = set()
    for i in range(examples.shape[0]):
        classes.add(examples.iloc[i][-1])
    return len(set(classes)) == 1

def choose_best_attribute(attributes, examples : pd.DataFrame):
    return max(attributes, key=lambda x: gain(x, examples))

def entropy(q):
    if q == 0 or q == 1:
        return 0
    return -(q * np.log2(q) + (1 - q) * np.log2(1 - q))

def remainder(a, example):
    len_example = len(example)
    return sum((len(example[example[a] == vk]) / len_example) * entropy(len(example[example[a] == vk]) / len_example) for vk in example[a].unique())

def gain(a, examples):
    return entropy(len(examples[examples.iloc[:, -1] == examples.iloc[0, -1]])/len(examples)) - remainder(a, examples)

def get_values(attribute, examples):
    values = set()
    for value in examples[attribute]:
        values.add(value)
    return values
