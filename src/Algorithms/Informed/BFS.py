from ButterRobot import ButterRobot
from Node import Node
from Queue import Queue
from Utils import expand


def best_first_search(problem:ButterRobot):
    node = Node(state=problem.initial_state)
    
    frontier = Queue()
    frontier.bfs_enqueue(node)
    
    reached ={}
    reached[str(problem.initial_state)] = node
    
    while not frontier.is_empty():
        node = frontier.dequeue()
        
        if problem.is_goal(node.state):
            return node
        
        for child in expand(problem,node):
            state = child.state
            if str(state) not in reached.keys() or\
            child.h_n < reached[str(state)].h_n:
                reached[str(state)] = child
                frontier.bfs_enqueue(child)
    return