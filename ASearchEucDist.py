import math
from problem import Problem
from node import Node
from tree import Tree
import time
from uniformCostSearch import print_state

def euclideanDistance(startState, goalState):
    eucDist = eucDistX = eucDistY = x1 = x2 = y1 = y2 = 0
    sizeOfPuzzle = int(math.sqrt(len(startState))) #because its a square the square root would be the dimensions
    for i in range(sizeOfPuzzle):
        x1 = startState.index(i) // sizeOfPuzzle # find the row of the state that we are in 
        y1 = startState.index(i) % sizeOfPuzzle # find the column of the state that we are in 
        x2 = goalState.index(i) // sizeOfPuzzle #inneficient but we calculate the goal state index every time in the for loop
        y2 = goalState.index(i) % sizeOfPuzzle
        eucDistX = pow(x2 - x1,2)
        eucDistY = pow(y2 - y1,2)
        eucDist += math.sqrt(eucDistX + eucDistY)
    return eucDist

def ASearchEucDist(problem):
    start_time = time.time()

    #setting the scope
    # problem = Problem(startState, goalState, operators)
    tree = Tree()
    startNode = Node(problem.initial_state)
    tree.add_node(startNode)
    path = []
    explored = set()
    max_queue_size = 0
    matrixOrder = [] #used to store the changes in the matrix 
    nodes_expanded = 0


    #A* heuristic search (Euclidean Distance)
    while tree.priority_queue:
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
            print("Goal State", " Depth:", len(matrixOrder)+1)
            path.reverse()
            print("Max queue size:", max_queue_size)
            end_time = time.time()  # Record the end time
            print("Time taken:", end_time - start_time, "seconds")
            print("Nodes expanded:", nodes_expanded)
            return path
            
        explored.add(tuple(curr.state))
        
        for child in curr.expand(problem):
            if tuple(child.state) not in explored:
                child.h_cost = euclideanDistance(child.state, problem.goal_state)
                nodes_expanded += 1
                tree.add_node(child)
    print("Max queue size:", max_queue_size)
    end_time = time.time()  # Record the end time
    print("Time taken:", end_time - start_time, "seconds")
    print("Nodes expanded:", nodes_expanded)
    print("Could not Solve")
    return []