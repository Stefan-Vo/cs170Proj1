import heapq

class Tree:
    def __init__(self):
        self.priority_queue = []  
        heapq.heapify(self.priority_queue)

    def add_node(self, node):
        heapq.heappush(self.priority_queue, node)

    def get_node(self):
        return self.priority_queue

    def pop_node(self):
        return heapq.heappop(self.priority_queue)
