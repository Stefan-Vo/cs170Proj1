from problem import Problem
from node import Node
from tree import Tree

def main():
    initial_state = [1, 0, 3, 4, 2, 6, 7, 5, 8]
    goal_state = [1,2,3,4,5,6,7,8,0]

    operators = ["UP", "DOWN", "LEFT", "RIGHT"]

    problem = Problem(initial_state, goal_state, operators)

    tree = Tree()

    initial_node = Node(initial_state)
    tree.add_node(initial_node)

    path = uniformCostSearch(problem)

    print(path)
    

#def print_state(state):
    #for i in range(0, len(state), 3):
        #print(state[i:i+3])

# Example usage:


def uniformCostSearch(problem):
    tree = Tree()
    startNode = Node(problem.initial_state)
    tree.add_node(startNode)
    path = []
    explored = set()

    while tree.priority_queue:
        curr = tree.pop_node()
        #print //

        if tuple(curr.state) in explored:
            continue
        explored.add(tuple(curr.state))

        for i in range(0, len(problem.goal_state), 3):
            if i == 6:
                print(*problem.goal_state[i:i+3], "Goal")
                print("G(n)", curr.g_cost)
                print()
            else:
                print(*problem.goal_state[i:i+3])
        #////////
        if curr.state == problem.goal_state:
            while curr.parent:
                path.append(curr.operator)
                curr = curr.parent
            path.reverse()
            return path
        
        else:
            newNode = curr.expand(problem)
            for nodes in newNode:
                #print //
                for i in range(0, len(nodes.state), 3):
                    if i == 6:
                        print(*nodes.state[i:i+3], nodes.operator)
                        print()
                    else:
                        print(*nodes.state[i:i+3])
                #////////
                #nodes.g_cost += curr.g_cost
                tree.add_node(nodes)

    return None


if __name__ == "__main__":
    main()
