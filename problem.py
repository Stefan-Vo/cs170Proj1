class Problem:
    def __init__(self, initial_state, goal_state, operators):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.operators = [self.moveUp, self.moveDown, self.moveRight, self.moveLeft]
        
    def is_goal_state(self, state):
        return state == self.goal_state
    
    #Moving up is -3 based on:
        # 1 2 3
        # 4 5 6 
        # 7 8 9 
        # [1,2,3,4,5,6,7,8,9]
        # Ex: To move 4 to 1 you must shift '4' to the left of the array to the 1 position which is -3

    def moveUp(self, state):
        new_state = state.copy()
        emptyIndex = new_state.index(0)
        if emptyIndex not in new_state[0, 1, 2]:
            new_state[emptyIndex], new_state[emptyIndex -3] = new_state[emptyIndex - 3], new_state[emptyIndex]
            return new_state
        else:
            return None
        

    def moveDown(self, state):
        new_state = state.copy()
        emptyIndex = new_state.index(0)
        if emptyIndex not in new_state[6, 7, 8]:
            new_state[emptyIndex], new_state[emptyIndex + 3] = new_state[emptyIndex + 3], new_state[emptyIndex]
            return new_state
        else:
            return None
        
    def moveRight(self, state):
        new_state = state.copy()
        emptyIndex = new_state.index(0)
        if emptyIndex not in new_state[2, 5, 8]:
            new_state[emptyIndex], new_state[emptyIndex + 1] = new_state[emptyIndex + 1], new_state[emptyIndex]
            return new_state
        else:
            return None
        
    def moveLeft(self, state):
        new_state = state.copy()
        emptyIndex = new_state.index(0)
        if emptyIndex not in new_state[0, 3, 6]:
            new_state[emptyIndex], new_state[emptyIndex - 1] = new_state[emptyIndex  - 1], new_state[emptyIndex]
            return new_state
        else:
            return None

