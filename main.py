from problem import Problem
from node import Node
from tree import Tree

def main():
    initial_state = [1,2,4,0,3,5,6,7,8]
    goal_state = [1,2,4,6,3,5,0,7,8]

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

        if curr.state == problem.goal_state:
            while curr.parent:
                path.append(curr.operator)
                curr = curr.parent
            path.reverse()
            return path

        explored.add(curr)

        for child in curr.expand(problem):
            if tuple(child.state) not in explored:
                tree.add_node(child)

    return None



if __name__ == "__main__":
    main()
