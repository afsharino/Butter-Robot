from Node import Node
from Queue import Queue
from ButterRobot import ButterRobot
from Utils import expand


def breadth_first_search(problem:ButterRobot):
    node = Node(state=problem.initial_state)
    
    if problem.is_goal(node.state):
        return node
    
    frontier = Queue()
    frontier.enqueue(node)
    reached = [problem.initial_state]
    
    while not frontier.is_empty():
        node = frontier.dequeue()
        
        for child in expand(problem, node):
            state = child.state
            
            if problem.is_goal(state):
                return child
            
            if state not in reached:
                reached.append(state)
                frontier.enqueue(child)
                
    return 