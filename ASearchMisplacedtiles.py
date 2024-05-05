from problem import Problem
from node import Node
from tree import Tree
import time
from uniformCostSearch import print_state


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
    matrixOrder = [] #used to store the changes in the matrix 
    nodes_expanded = 0


    
    #A* heuristic search (misplaced tiles)
    while tree.priority_queue:
        start_time = time.time()
        max_queue_size = max(max_queue_size, len(tree.priority_queue))
        curr = tree.pop_node()
        if curr.state == problem.goal_state:
            path = []
            print_state(curr.state)
            while curr.parent:
                path.append(curr.operator)
                matrixOrder.append(curr)
                curr = curr.parent

            print("Initial State")
            print_state(problem.initial_state)

            matrixOrder.reverse()
            for matrix in matrixOrder: #This prints out the the trace matrix
                print("Best State to Expand: ", "G(n):", matrix.g_cost, "H(n):", matrix.h_cost, "  Operation:", matrix.operator)
                print_state(matrix.state)

            path.reverse()
            print("Goal State", " Depth:", len(matrixOrder))
            print("Max queue size:", max_queue_size)
            end_time = time.time()  # Record the end time
            print("Time taken:", end_time - start_time, "seconds")
            print("Nodes expanded:", nodes_expanded)
            return path
            
        explored.add(tuple(curr.state))
        
        for child in curr.expand(problem):
            if tuple(child.state) not in explored:
                child.h_cost = misplacedTiles(child.state, problem.goal_state)
                nodes_expanded += 1
                tree.add_node(child)
    print("Max queue size:", max_queue_size)
    end_time = time.time()  # Record the end time
    print("Time taken:", end_time - start_time, "seconds")
    print("Nodes expanded:", nodes_expanded)
    print("Could not Solve")
    return []
    
    
