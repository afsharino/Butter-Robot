from Utils import manhatan_distance

class Node:
    def __init__(self, state, parent=None, action=None, path='',depth=0, h_n=None, cost=None):
        self.state = state
        self.parent = parent
        self.action = action
        self.action_path = path
        self.depth = depth
        if h_n == None:
            self.h_n = self.find_h_n_for_initial_State(self.state)
            
        else:
            self.h_n = h_n
            
        if cost == None:
            self.path_cost = self.find_initial_cost(self.state)
            
        else:
            self.path_cost = cost
    
    def find_initial_cost(self, state:list):
        for row in range(len(self.state)):
                for column in range(len(self.state[0])):
                    if 'r' in self.state[row][column]:
                        r_place = (row,column)
        
        r_grid = self.state[r_place[0]][r_place[1]]
        cost = 0
        for char in r_grid:
            if char.isdigit():
                cost = int(char)
                break
            
        return cost
    
    def find_h_n_for_initial_State(self, state:list):
        b_places = set()
        # find butters places
        for row in range(len(state)):
            for column in range(len(state[0])):
                if 'b' in state[row][column]:
                    b_places.add((row,column))
    
        p_places = set()
        # find goal places
        for row in range(len(state)):
            for column in range(len(state[0])):
                if 'p' in state[row][column]:
                    p_places.add((row,column))
        b_places = list(b_places)
        p_places = list(p_places)
        return sum([manhatan_distance(b_places[index], p_places[index]) for index in range(len(b_places))])