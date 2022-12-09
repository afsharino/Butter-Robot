from Node import Node

class Stack:
    
    def __init__(self):
        self.stack = []
    
    def push(self, node:Node):
        self.stack.append(node)   
        
    def pop(self):
        try:
            return self.stack.pop()
        
        except:
            return
        
    def top(self):
        try:
            return self.stack[-1]
        
        except:
            return
    
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        
        else:
            return False
        
        
