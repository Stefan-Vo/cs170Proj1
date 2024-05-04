import problem
import node
import tree

def misplacedTiles(startState, goalState):
    tiles_sum = 0;
    for i,j in zip(startState, goalState):
        if i != j: tiles_sum +=1
    return tiles_sum
    
def ASearchHeuristic(startState, goalState):
    #setting the scope
    problem = Problem(startState, goalState, operators)
    tree = Tree()
    startNode = Node(problem.initial_state)
    tree.add_node(startNode)
    path = []
    explored = set()
    
    #A* heuristic search (misplaced tiles)
    while tree.priority_queue:
        curr = tree.pop_node()
        if curr.state == goalState:
            path = []
            while curr.parent:
                path.append(curr.operator)
                curr = curr.parent
            path.reverse()
            return path
            
        explored.add(curr.state)
        
        problem_child = problem.Problem(curr.state, goalState, operators)
        for child in curr.expand(problem_child):
            if child.state not in explored:
                total_cost = child.g_cost + misplacedTiles(child.state, goalState)
                tree.add_node(child, total_cost)
                
    return []
    
    
