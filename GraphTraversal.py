# -*- coding: utf-8 -*-
"""
Created on Sat Jun 04 17:47:51 2016

@author: John Fuini
"""

from Queue import Queue

#Directed Graph (this doesn't seem clean or efficient.  Should come back and fix it)

class Graph:
    nodes = []
    node_connections = {}
    node_visited = {}    
    
    
    def add_nodes(self, list_of_nodes = [], dict_of_connections = {}):
        for node in list_of_nodes:
            self.nodes.append(node)
            self.node_connections = dict_of_connections
            for key in dict_of_connections.keys():
                self.node_visited[key] = False
       
    
    def print_nodes(self):
        for node in self.nodes:
            print(node.value)            
    
    def DFsearch(self, root):
        for key in self.node_connections.keys():
            self.node_visited[key] = False #reset all visited values to False
        self.DFsearch_inner_recursion(root)
        
        
    def DFsearch_inner_recursion(self, root): #don't call this on it's own, visited values need to be reset
        if root == None:
            return
        self.node_visited[root.name] = True
        print(root.value)
        for node in self.node_connections[root.name]:
            if self.node_visited[node.name] == False:
                self.DFsearch_inner_recursion(node)
                
    def BFsearch(self, root):
        for key in self.node_connections.keys():
            self.node_visited[key] = False #reset all visited values to False
        if root == None:
            return
        queue = Queue()
        queue.put(root)
        while queue.empty() == False:
            node = queue.get()
            print(node.value)
            for connection in self.node_connections[node.name]:
                if self.node_visited[connection.name] == False:
                    queue.put(connection)
                    self.node_visited[connection.name] = True
                
            
        


            
    
class Node:    
    def __init__(self, name, value):
        self.name = name
        self.value = value
        
                       
    def set_connection(self, node):
        self.connections.append(node)
               
    def print_value(self):
        print(self.value)

    def print_children(self):
        for x in self.children:
            print(x.value),


A = Node('A', 1)
B = Node('B', 4)
C = Node('C', 6)
D = Node('D', 7)
E = Node('E', 9)
F = Node('F', 13)
G = Node('G', 125)
H = Node('H', 2535)

connections_short = {'A': [B, C], 'B': [C], 'C': [A]}
connections = {'A': [B, C, D, H], 'B': [A, C], 'C': [D], 'D': [G], 'E': [A, B], 'F':[H], 'G':[A,B,D], 'H': [F, A]}


my_graph = Graph()
my_graph.add_nodes([A,B,C,D,E,F,G,H], connections)
print('printing nodes:')
my_graph.print_nodes()
print('Depth-first search:')
my_graph.DFsearch(A)
print('Breadth-first search:')
my_graph.BFsearch(A)

