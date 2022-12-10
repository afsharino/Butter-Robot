import Input
from ButterRobot import ButterRobot
from Algorithms.Uninformed.BFS import breadth_first_search
from Algorithms.Uninformed.DFS import depth_first_search
from Algorithms.Uninformed.UCS import uniform_cost_search
from Algorithms.Uninformed.IDS import iterative_deeping_search
from Algorithms.Informed.BFS import best_first_search
from Algorithms.Informed.A_STAR import a_star

if __name__ == "__main__":
    # Get input matrix from the user.
    matrix = Input.get_input()
    
    # Create an instance from butter-robot
    problem = ButterRobot(matrix)
    
    result = breadth_first_search(problem)
    print(f"algorithm: bfs\n\tpath = {result.action_path}\n\tcost = {result.path_cost}\n\tdepth = {result.depth}")
    
    result1 = depth_first_search(problem)
    print(f"algorithm: dfs\n\tpath = {result1.action_path}\n\tcost = {result1.path_cost}\n\tdepth = {result1.depth}")
    
    result2 = uniform_cost_search(problem)
    print(f"algorithm: ucs\n\tpath = {result2.action_path}\n\tcost = {result2.path_cost}\n\tdepth = {result2.depth}")
    
    # result3 = iterative_deeping_search(problem)
    # print(f"algorithm: ids\n\tpath = {result3.action_path}\n\tcost = {result3.path_cost}\n\tdepth = {result3.depth}")
    
    result4 = best_first_search(problem)
    print(f"algorithm: bfs\n\tpath = {result4.action_path}\n\tcost = {result4.path_cost}\n\tdepth = {result4.depth}")
    
    result5 = a_star(problem)
    print(f"algorithm: astar\n\tpath = {result5.action_path}\n\tcost = {result5.path_cost}\n\tdepth = {result5.depth}")

