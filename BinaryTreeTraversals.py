# -*- coding: utf-8 -*-
"""
Created on Thu Jun 02 15:25:11 2016

@author: John Fuini
"""

from Queue import Queue

#traversal of binary trees

class Node:
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
                       
    def set_left(self, node):
        self.left = node
        
    def set_right(self, node):
        self.right = node        
       
    def print_value(self):
        print(self.value)
        

      
# Depth first traversals (recursive algorithms)
      
def pre_order_traversal(node):
    if node == None:
        return
    print(node.value)
    pre_order_traversal(node.left)
    pre_order_traversal(node.right)
    
def in_order_traversal(node):
    if node == None:
        return
    in_order_traversal(node.left)
    print(node.value)
    in_order_traversal(node.right)
    
def post_order_traversal(node):
    if node == None:
        return
    post_order_traversal(node.left)
    post_order_traversal(node.right)
    print(node.value)
    
# Depth First Traversals (interative algorithm)
def pre_order_traversal_iter(node):
    if node == None:
        return    
    stack = []
    stack.append(node)
    while len(stack) != 0:
        node = stack.pop()
        print(node.value)        
        if node.right != None:
            stack.append(node.right)
        if node.left != None:
            stack.append(node.left)
            
def in_order_traversal_iter(node):
    if node == None:
        return    
    stack = []
    stack.append(node)
    while len(stack) != 0:
        if node.left != None:
            stack.append(node.left)
            node = node.left
        else:
            node = stack.pop()
            print(node.value)
            if node.right != None:
                stack.append(node.right)            
                node = node.right
                
def post_order_traversal_iter(node):
    if node == None:
        return    
    stack = []
    last_node = None
    while len(stack) != 0 or node != None:
        if node != None:
            stack.append(node)
            node = node.left
        else:
            peek_node = stack[-1]
            if peek_node.right != None and peek_node.right != last_node:
                node = peek_node.right
            else:
                print(peek_node.value)
                last_node = stack.pop()
                
                
# Breadth First 

# finish this                
        
def level_order_traversal(node):
    if node == None:
        return
    queue = Queue()
    queue.put(node)
    while not queue.empty():
        node = queue.get()
        print node.value
        if node.left != None:
            queue.put(node.left)
        if node.right != None:
            queue.put(node.right)
        
            
        
        
        
A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')
G = Node('G')
H = Node('H')

A.set_left(B)
B.set_left(D)
B.set_right(E)
A.set_right(C)
C.set_left(F)
C.set_right(G)
F.set_right(H)

print "Pre-order Traversal:"
pre_order_traversal(A)
print "In-order Traversal:"
in_order_traversal(A)
print "Post-order Traversal:"
post_order_traversal(A)
print "Pre-order Iterively:"
pre_order_traversal_iter(A)
print "In-order Iterively:"
in_order_traversal_iter(A)
print "Post-order Iterively:"
post_order_traversal_iter(A)
print "Breadth First Traversal"
level_order_traversal(A)
