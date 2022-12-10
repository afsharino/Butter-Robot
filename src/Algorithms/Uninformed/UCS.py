from ButterRobot import ButterRobot
from Node import Node
from Queue import Queue
from Utils import expand


def uniform_cost_search(problem:ButterRobot):
    node = Node(state=problem.initial_state)
    frontier = Queue()
    frontier.ucs_enqueue(node)
    reached ={}
    reached[str(problem.initial_state)] = node
    
    while not frontier.is_empty():
        node = frontier.dequeue()
        if problem.is_goal(node.state):
            return node
        for child in expand(problem,node):
            state = child.state
            if str(state) not in reached.keys() or\
            child.path_cost < reached[str(state)].path_cost:
                reached[str(state)] = child
                frontier.ucs_enqueue(child)
    return
