# -*- coding: utf-8 -*-
"""
Created on Sat Jun 04 17:23:37 2016

@author: John Fuini
"""
from Queue import Queue

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

#Depth First Search (recursive)
def DFsearch(node):
    if node != None:
        print(node.value)
        for child in node.children:
            DFsearch(child)

#Breadth First Search (iterative)
def BFsearch(node):
    if node == None:
        return
    queue = Queue()
    queue.put(node)        
    while queue.empty() == False:
        node = queue.get()
        print(node.value)
        for child in node.children:
            queue.put(child)
            
            

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

print("Depth-first traversal:")
DFsearch(A)
print("Breadth-first traversal:")
BFsearch(A)
        