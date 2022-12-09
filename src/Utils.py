from Node import Node
from Utils import heuristic
from copy import deepcopy
from ButterRobot import ButterRobot
def expand(problem:ButterRobot, node:Node):
    state1 = node.state
    
    for action in problem.actions(state1):
        state2 = problem.successor(deepcopy(state1), action)
        cost = node.path_cost +  problem.action_cost(state2)
        path = node.action_path + problem.get_direction(action)
        depth = node.depth + 1
        h_n = heuristic(problem, state2)
        yield Node(state=state2, parent=node, action=action, path=path, depth=depth, h_n=h_n, cost=cost)