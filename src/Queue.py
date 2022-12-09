from Node import Node

class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, node:Node):
        self.queue.append(node)
           
    def dequeue(self):
        try:
            return self.queue.pop(0)
        except:
            return
        
    def front(self):
        try:
            return self.queue[0]
        except:
            return
        
    def enqueue(self, node:Node):
        self.queue.append(node)
    
    def is_empty(self):
        if len(self.queue) == 0:
            return True
        
        else:
            return False