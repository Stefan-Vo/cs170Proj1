class Problem:
    def __init__(self, initial_state, goal_state, operators):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.operators = operators
    
    def operator_action(self, state, operator):
        pass
    
    def is_goal_state(self, state):
        return state == self.goal_state