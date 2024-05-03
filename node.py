class Node:
    def __init__(self, state, parent=None, action=None, cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost


    # Ideas for Functions to implement in this class:
        # imnplement expand()  in Node class
        # implement path(): Returns the sequence of actions from the initial state to this node.
        # total_cost(): returns cost of reaching this node from start
