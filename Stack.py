# -*- coding: utf-8 -*-
"""
Created on Sun May 08 14:08:26 2016

@author: John Fuini
"""

class Stack:
    

    def __init__(self):
        self.items = []

    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
            
    def push(self, item):
        self.items.append(item)
        return self
     
    def pop(self):
        print('pop!')
        item = self.items[-1]
        self.items = self.items[0:(len(self.items)-1)]
        return item

    def peek(self):
        return self.items[len(self.items)-1]

    def print_stack_items(self):
        print('printing stack')
        for i in range(len(self.items)):
            print(self.items[i])
            
    def size(self):
        return len(self.items)

stack1 = Stack()
print(stack1.is_empty())
stack1.push(4)
print(stack1.is_empty())
stack1.push(3)
stack1.push(5)
stack1.print_stack_items()
print(stack1.pop())
stack1.print_stack_items()
print(stack1.peek())