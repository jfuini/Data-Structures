# -*- coding: utf-8 -*-
"""
Created on Sat Jun 04 17:47:51 2016

@author: John Fuini
"""

#Directed Graph (Needs more work, finished adding the links)

class Graph:
    nodes = []
    
    def add_nodes(self, list_of_nodes = []):
        for node in list_of_nodes:
            self.nodes.append(node)
    
    def print_nodes(self):
        for node in self.nodes:
            print(node.value)            
    
    def DFsearch(self, root):
        return
    
    
class Node:    
    def __init__(self, value):
        self.value = value
        self.children = []
                       
    def add_child(self, node):
        self.children.append(node)
               
    def print_value(self):
        print(self.value)

    def print_children(self):
        for x in self.children:
            print(x.value),


A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')
G = Node('G')
H = Node('H')

A.add_child(B)
A.add_child(C)
A.add_child(D)
B.add_child(E)
C.add_child(F)
C.add_child(G)
D.add_child(H)

my_graph = Graph()
my_graph.add_nodes([A,B,C,D,E,F,G,H])
my_graph.print_nodes()