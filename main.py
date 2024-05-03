import problem
import node
import tree


def uniformCostSearch(startState, goalState):
    problem = Problem(startState, goalState, operators)
    tree = Tree()
    startNode = Node(problem.initial_state)
    tree.add_node(startNode)
    path = []
    explored = set()

    while tree.priority_queue:
        curr = tree.pop_node()

        if curr.state == goalState:
            while curr.parent:
                path.append(curr.action)
                curr = curr.parent
            path.reverse()
            return path

        explored.add(curr.state)

        for child in curr.expand(problem):
            if child.state not in explored:
                tree.add_node(child)

    return None


