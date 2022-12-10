from ButterRobot import ButterRobot
from Node import Node
from Utils import expand, is_cycle
from Stack import Stack

def depth_limited_search(problem:ButterRobot,depth):
    node = Node(state=problem.initial_state)
    
    frontier = Stack()
    frontier.push(node)
    result = None

    while not frontier.is_empty():
        node = frontier.pop()

        if problem.is_goal(node.state):
            return node
        
        if node.depth > depth:
            result="cutoff"
            
        if not is_cycle(node):            
            for child in expand(problem, node):
                frontier.push(child)
                
    return result
            
def iterative_deeping_search(problem:ButterRobot):
    depth = 0 
    while True:
        result=depth_limited_search(problem, depth)
        
        if not (result == "cutoff"):
            return result
        depth += 1