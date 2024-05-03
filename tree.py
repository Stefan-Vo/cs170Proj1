import heapq

class Tree:
    def __init__(self):
        self.nodes = {}
        self.priority_queue = []  

    def add_node(self, node):
        self.nodes[node.state] = node
        heapq.heappush(self.priority_queue, (node.path_cost, node))

    def get_node(self, state):
        return self.nodes.get(state, None)

    def pop_node(self):
        return heapq.heappop(self.priority_queue)[1]