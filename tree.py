import heapq

class Tree:
    def __init__(self):
        self.priority_queue = []  

    def add_node(self, node):
        self.priority_queue.append(node)
        self.priority_queue.sort(key=lambda x: x.g_cost)

    def get_node(self):
        return self.priority_queue

    def pop_node(self):
        return self.priority_queue.pop(0)
