import Input
from ButterRobot import ButterRobot
from Algorithms.Uninformed.BFS import breadth_first_search
from Algorithms.Uninformed.DFS import depth_first_search

if __name__ == "__main__":
    # Get input matrix from the user.
    matrix = Input.get_input()
    
    # Create an instance from butter-robot
    problem = ButterRobot(matrix)
    
    result = breadth_first_search(problem)
    print(f"algorithm: bfs\n\tpath = {result.action_path}\n\tcost = {result.path_cost}\n\tdepth = {result.depth}")
    
    result1 = depth_first_search(problem)
    print(f"algorithm: dfs\n\tpath = {result1.action_path}\n\tcost = {result1.path_cost}\n\tdepth = {result1.depth}")
    


    

