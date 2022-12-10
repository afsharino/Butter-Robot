from Move import Move

class ButterRobot:
    def __init__(self, initial_state:list):
        self.initial_state = initial_state
        
    def actions(self, state:list) -> list:
        # List of available directions that robot can go.
        available_actions = []
        
        # Get location of robot in tuple form. 
        r_place = self.find_robot_place(state)
        
        # create an instance from move module.
        move = Move()
        
        # Iterate over directions to find possible directions.
        for direction in [move.left, move.right, move.up, move.down]:
            # Check that robot does not throw itself down from table.
            if self.is_out_of_bound(r_place, direction, state):
                continue
            
            # Check that the robot does not move other
            # -food and obstacles on the table. 
            elif self.is_obstacle(r_place, direction, state):
                continue
            
            # Check that if the robot can move the butter or not.
            elif self.is_butter(r_place, direction, state):
                if self.is_butter_movable(r_place, direction, state):
                    available_actions.append(direction)
                else:
                    continue
            else:
                available_actions.append(direction)
        
        return available_actions
    
    def successor(self, state:list, action:tuple) -> list:
        # Get location of robot in tuple form.
        r_place = self.find_robot_place(state)
        
        # The "successor place" the robot is going to go to.
        result = (r_place[0] + action[0], r_place[1] + action[1])
        
        # remove r from previoust place.
        # robot is not in goal place.
        if len (state[r_place[0]][r_place[1]]) == 2:
            state[r_place[0]][r_place[1]] = state[r_place[0]][r_place[1]][0]
        
        # robot is in goal place.
        elif len (state[r_place[0]][r_place[1]]) == 3:
            state[r_place[0]][r_place[1]] = state[r_place[0]][r_place[1]][:2]
        
        # Move butter if there is butter in "successor place".
        if self.is_butter(r_place, action, state):
            # remove b from previoust grid
            state[result[0]][result[1]] = state[result[0]][result[1]][0]
            
            # add b to "successor place".
            result2 = (result[0] + action[0], result[1] + action[1])
            state[result2[0]][result2[1]] = (state[result2[0]][result2[1]] + 'b')
            
            # add r to "successor place".
            state[result[0]][result[1]] = (state[result[0]][result[1]] + 'r')
            
        else:
            # add r to "successor place".
            state[result[0]][result[1]] = (state[result[0]][result[1]] + 'r')
            
        return state
        
    def action_cost(self, state2:list) -> int:
        # Get location of robot in tuple form.
        r_place = self.find_robot_place(state2)
        
        # The "successor place" the robot has come to.
        new_r_place = state2[r_place[0]][r_place[1]]
        
        # Extract the cost of new place.  
        cost = 0
        for char in new_r_place:
            if char.isdigit():
                cost = int(char)
                break
        return cost
    
    def is_goal(self, state:list) -> bool:
        # Get set of butters locations.
        b_places = self.find_butter_places(state)
        
        # Get set of goal locations.
        t_places = self.find_target_places(state)

        if b_places == t_places:
            return True
        
        else:
            return False
        
    def get_direction(self, action:tuple) -> str:
        
        if action == (0, -1):
            return 'L'
        
        elif action == (0,1):
            return 'R'
        
        elif action == (-1,0):
            return 'U'
        
        elif action == (1,0):
            return 'D'
        
        else:
            return ''
        
    def find_robot_place(self, state:list) -> tuple:
        # find the location of the robot.
        for row in range(len(state)):
            for column in range(len(state[0])):
                if 'r' in state[row][column]:
                    r_place = (row,column)
        
        return r_place
                    
    def find_butter_places(self, state:list) -> tuple:
        b_places = set()
        
        # find the location of the butters.
        for row in range(len(state)):
            for column in range(len(state[0])):
                if 'b' in state[row][column]:
                    b_places.add((row,column))
        
        return b_places
    
    def find_target_places(self, state:list) -> tuple:
        t_places = set()
        
        # find the location of the goals.
        for row in range(len(state)):
            for column in range(len(state[0])):
                if 'p' in state[row][column]:
                    t_places.add((row,column))
                    
        return t_places
    
    def is_obstacle(self, r_place:tuple, move_direction:tuple, state:list) -> bool:
        # The "successor place" the robot is going to go to.
        result = (r_place[0] + move_direction[0], r_place[1] + move_direction[1])
        
        # Check The "successor place" not to be an obstacle.
        if state[result[0]][result[1]] == 'x':
            return True
        
        else:
            return False
    
    def is_out_of_bound(self, r_place:tuple, move_direction:tuple, state:list) -> bool:
        # The "successor place" the robot is going to go to.
        result = (r_place[0] + move_direction[0], r_place[1] + move_direction[1])
        
        # Check The "successor place" does not cause
        # -it to robot throw itself down from the table.
        if ((0 <= result[0] < len(state)) and (0 <= result[1] < len(state[0]))):
            return False
        
        else:
            return True
        
    def is_butter(self, r_place:tuple, move_direction:tuple, state:list) -> bool:
        # The "successor place" the robot is going to go to.
        result = (r_place[0] + move_direction[0], r_place[1] + move_direction[1])
        
        # Check that The "successor place" contains any butters.
        if 'b' in state[result[0]][result[1]]:
            return True
        
        else:
            return False
        
    def is_butter_movable(self, r_place:tuple, move_direction:tuple, state:list) -> bool:
        # The "successor place" the robot is going to go to.
        result = (r_place[0] + move_direction[0], r_place[1] + move_direction[1])
        
        # The "successor place" for butter if the robot move it.
        result2 = (result[0] + move_direction[0], result[1] + move_direction[1])
        
        # Check The "successor place" of butter does not cause
        # -it to robot throw butter down from the table.
        if not ((0 <= result2[0] < len(state)) and (0 <= result2[1] < len(state[0]))):
            return False
         
        # Check The "successor place" of butter does not 
        # contains any butters.   
        elif state[result2[0]][result2[1]] == 'x':
            return False
        
        # Check that the robot does not move two butter in a row .
        elif 'b' in state[result2[0]][result2[1]]:
            return False
        
        elif len(state[result[0]][result[1]]) == 3:
            return False
        
        else:
            return True