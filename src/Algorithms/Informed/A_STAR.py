from ButterRobot import ButterRobot
from Utils import expand
from Node import Node
from Queue import Queue


def a_star(problem:ButterRobot):
    node = Node(state=problem.initial_state)
    
    frontier = Queue()
    frontier.a_star_enqueue(node)
    reached ={}
    reached[str(problem.initial_state)] = node
    
    while not frontier.is_empty():
        node = frontier.dequeue()
        
        if problem.is_goal(node.state):
            return node
        
        for child in expand(problem,node):
            state = child.state
            
            if str(state) not in reached.keys() or\
            (child.h_n + child.path_cost) < (reached[str(state)].h_n + reached[str(state)].path_cost):
                reached[str(state)] = child
                frontier.a_star_enqueue(child)
    return