from Node import Node
from ButterRobot import ButterRobot
from copy import deepcopy

def expand(problem:ButterRobot, node:Node):
    state1 = node.state
    
    for action in problem.actions(state1):
        state2 = problem.successor(deepcopy(state1), action)
        cost = node.path_cost +  problem.action_cost(state2)
        path = node.action_path + problem.get_direction(action)
        depth = node.depth + 1
        yield Node(state=state2, parent=node, action=action, path=path, depth=depth, cost=cost)