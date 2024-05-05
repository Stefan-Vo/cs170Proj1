
from problem import Problem
from node import Node
from tree import Tree
import time

def print_state(state):
    for i in range(0, len(state), 3):
        print(state[i:i+3])

def uniformCostSearch(problem):
    start_time = time.time()

    tree = Tree()
    startNode = Node(problem.initial_state)
    tree.add_node(startNode)
    path = []
    explored = set()
    max_queue_size = 0
    matrixOrder = [] #used to store the changes in the matrix 
    nodes_expanded = 0

    while tree.priority_queue:

        max_queue_size = max(max_queue_size, len(tree.priority_queue))

        curr = tree.pop_node()
        #print //
        if tuple(curr.state) in explored:
            continue
        explored.add(tuple(curr.state))


        #////////
        if curr.state == problem.goal_state:
            while curr.parent:
                path.append(curr.operator)
                matrixOrder.append(curr)
                print()
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
            print("Nodes Expanded", nodes_expanded)
            return path
        
        else:
            newNode = curr.expand(problem)
            for nodes in newNode:
                #print_state(curr.state)
                #nodes.g_cost += curr.g_cost
                nodes_expanded += 1
                tree.add_node(nodes)
    print("Max queue size:", max_queue_size)
    end_time = time.time()  # Record the end time
    print("Time taken:", end_time - start_time, "seconds")
    print("Nodes Expanded", nodes_expanded)
    print("Could not Solve")
    return None