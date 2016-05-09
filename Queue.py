# -*- coding: utf-8 -*-
"""
Created on Sun May 08 14:08:26 2016

@author: John Fuini
"""

class Queue:
    

    def __init__(self):
        self.items = []

    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
            
    def enqueue(self, item):
        self.items.append(item)
        return self
     
    def dequeue(self):
        item = self.items[0]
        self.items = self.items[1:]
        return item

    def print_que_items(self):
        for i in range(len(self.items)):
            print(self.items[i])
            
    def size(self):
        return len(self.items)

que1 = Queue()
print(que1.is_empty())   
que1.enqueue('a')          
que1.enqueue('b')
que1.enqueue('c')
que1.enqueue('d')
que1.print_que_items()
removed_item = que1.dequeue()
print("removed item %s" % removed_item)
que1.print_que_items()
print(que1.size())
