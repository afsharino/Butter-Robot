from Node import Node
from copy import deepcopy
from ButterRobot import ButterRobot


def is_cycle(node: Node):
        state = node.state
        
        while node.parent is not None:
            if state == node.parent.state:
                return True
            
            node = node.parent
            
        return False

def manhatan_distance(b_place:tuple, p_place:tuple):
    x_b, y_b = b_place
    x_p, y_p = p_place
    return (abs(x_p - x_b) + abs(y_p - y_b))


def heuristic(problem:ButterRobot, state:list):
    b_places = list(problem.find_butter_places(state))
    p_places = list(problem.find_target_places(state))
    
    return sum([manhatan_distance(b_places[index], p_places[index]) for index in range(len(b_places))])
        

def expand(problem:ButterRobot, node:Node):
    state1 = node.state
    
    for action in problem.actions(state1):
        state2 = problem.successor(deepcopy(state1), action)
        cost = node.path_cost +  problem.action_cost(state2)
        path = node.action_path + problem.get_direction(action)
        depth = node.depth + 1
        h_n = heuristic(problem, state2)
        yield Node(state=state2, parent=node, action=action, path=path, depth=depth, h_n=h_n, cost=cost)