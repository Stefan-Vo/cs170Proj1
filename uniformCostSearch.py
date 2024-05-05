
from problem import Problem
from node import Node
from tree import Tree
import time



def uniformCostSearch(problem):
    start_time = time.time()

    tree = Tree()
    startNode = Node(problem.initial_state)
    tree.add_node(startNode)
    path = []
    explored = set()
    max_queue_size = 0

    while tree.priority_queue:

        max_queue_size = max(max_queue_size, len(tree.priority_queue))

        curr = tree.pop_node()
        #print //

        if tuple(curr.state) in explored:
            continue
        explored.add(tuple(curr.state))

        for i in range(0, len(problem.goal_state), 3):
            if i == 6:
                print(*problem.goal_state[i:i+3], "Goal")
                print("G(n) =", curr.g_cost,"H(n) =", curr.h_cost)
                print()
            else:
                print(*problem.goal_state[i:i+3])
        #////////
        if curr.state == problem.goal_state:
            while curr.parent:
                path.append(curr.operator)
                curr = curr.parent
            path.reverse()
            print("Max queue size:", max_queue_size)
            end_time = time.time()  # Record the end time
            print("Time taken:", end_time - start_time, "seconds")
            return path
        
        else:
            newNode = curr.expand(problem)
            for nodes in newNode:
                #print //
                for i in range(0, len(nodes.state), 3):
                    if i == 6:
                        print(*nodes.state[i:i+3])
                        print()
                    else:
                        print(*nodes.state[i:i+3])
                #////////
                #nodes.g_cost += curr.g_cost
                tree.add_node(nodes)
    print("Max queue size:", max_queue_size)
    end_time = time.time()  # Record the end time
    print("Time taken:", end_time - start_time, "seconds")
    return None