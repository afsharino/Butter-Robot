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
    
    def is_empty(self):
        if len(self.queue) == 0:
            return True
        
        else:
            return False
        
    def ucs_enqueue(self, node:Node):
        for i in range(len(self.queue)):
            if node.path_cost < self.queue[i].path_cost:
                self.queue.insert(i, node)
                return
            
        self.queue.append(node)
        
    def bfs_enqueue(self, node:Node):
        for i in range(len(self.queue)):
            if node.h_n < self.queue[i].h_n:
                self.queue.insert(i, node)
                return
            
        self.queue.append(node)
        
    def a_star_enqueue(self, node:Node):
        for i in range(len(self.queue)):
            if (node.h_n + node.path_cost) < (self.queue[i].h_n + self.queue[i].path_cost):
                self.queue.insert(i, node)
                return
            
        self.queue.append(node)