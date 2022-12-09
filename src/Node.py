class Node:
    def __init__(self, state, parent=None, action=None, path='', cost=None):
        self.state = state
        self.parent = parent
        self.action = action
        self.action_path = path
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