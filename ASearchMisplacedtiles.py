from problem import Problem
from node import Node
from tree import Tree

def misplacedTiles(startState, goalState):
    tiles_sum = 0;
    for i,j in zip(startState, goalState):
        if i != j: tiles_sum +=1
    return tiles_sum
    
def ASearchHeuristic(problem):
    #setting the scope
    tree = Tree()
    startNode = Node(problem.initial_state)
    tree.add_node(startNode)
    path = []
    explored = set()
    max_queue_size = 0

    
    #A* heuristic search (misplaced tiles)
    while tree.priority_queue:
        max_queue_size = max(max_queue_size, len(tree.priority_queue))
        curr = tree.pop_node()
        if curr.state == problem.goal_state:
            path = []
            while curr.parent:
                path.append(curr.operator)
                curr = curr.parent
            path.reverse()
            print("Max queue size:", max_queue_size)
            return path
            
        explored.add(tuple(curr.state))
        
        for child in curr.expand(problem):
            if tuple(child.state) not in explored:
                child.h_cost = misplacedTiles(child.state, problem.goal_state)
                tree.add_node(child)
    print("Max queue size:", max_queue_size)
    return []
    
    
