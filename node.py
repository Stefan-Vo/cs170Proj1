import problem

class Node:
    def __init__(self, state, parent=None, operator=None, g_cost=0, h_cost = 0):
        self.state = state
        self.parent = parent
        self.operator = operator
        self.g_cost = g_cost
        self.h_cost = h_cost


    def __lt__(self, other):
        return self.g_cost < other.g_cost


    def expand(self, problem):
        operator_names = {
            problem.moveUp: "UP",
            problem.moveDown: "DOWN",
            problem.moveRight: "RIGHT",
            problem.moveLeft: "LEFT"
        }

        operatorList = []
        for operator in problem.operators:
            new_state = operator(self.state)
            if new_state is not None:
                action_name = operator_names.get(operator, "UNKNOWN") #If operator not found then "UNKNOWN" set as default otherwise should display correct operator name
                operatorList.append(Node(new_state, self, action_name, self.g_cost + 1))
        return operatorList


    # Ideas for Functions to implement in this class:
        # implement path(): Returns the sequence of actions from the initial state to this node.
        # total_cost(): returns cost of reaching this node from start
