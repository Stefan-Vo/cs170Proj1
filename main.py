from problem import Problem
from node import Node
from tree import Tree

def main():
    initial_state = [1, 2, 0, 4, 5, 3, 7, 8, 6]
    goal_state = [1,2,3,4,5,6,7,8,0]

    operators = ["UP", "DOWN", "LEFT", "RIGHT"]

    problem = Problem(initial_state, goal_state, operators)

    tree = Tree()

    initial_node = Node(initial_state)
    tree.add_node(initial_node)

    path = uniformCostSearch(problem)

    print(path)
    


def uniformCostSearch(problem):
    tree = Tree()
    startNode = Node(problem.initial_state)
    tree.add_node(startNode)
    path = []
    explored = set()

    while tree.priority_queue:
        curr = tree.pop_node()
        print(problem.goal_state)
        if curr.state == problem.goal_state:
            while curr.parent:
                path.append(curr.operator)
                curr = curr.parent
            path.reverse()
            return path
        
        else:
            newNode = curr.expand(problem)
            for nodes in newNode:
                print(nodes.state, nodes.operator)
                nodes.g_cost += curr.g_cost
                tree.add_node(nodes)

    return None



if __name__ == "__main__":
    main()
